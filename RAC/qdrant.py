#!/usr/bin/env python3
"""Création d'une base Qdrant locale pour les contacts RAG.

Le script lit les fichiers texte présents dans RAG/RAC/Data, les découpe en
chunks, calcule des embeddings E5 multilingues et les insère dans une
collection Qdrant nommée ``infocontact``.
"""

from __future__ import annotations

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import argparse
import hashlib
from loguru import logger
from pathlib import Path
from typing import Any
from uuid import NAMESPACE_URL, uuid5
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv(Path(__file__).resolve().parent.parent / '.env')

from qdrant_client import QdrantClient
from qdrant_client.models import (
	Distance,
	PointStruct,
	VectorParams,
	SparseVectorParams,
	SparseVector,
	Modifier,
)
from sentence_transformers import SentenceTransformer
from fastembed import SparseTextEmbedding
from langchain_text_splitters import RecursiveCharacterTextSplitter





PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "Data"
DEFAULT_QDRANT_PATH = DATA_DIR / "infocontact"
DEFAULT_COLLECTION_NAME = "infocontact"
DEFAULT_MODEL_NAME = "intfloat/multilingual-e5-large"
SUPPORTED_INPUT_EXTENSIONS = (".txt", ".md")


class ContactVectorDB:
	"""Base vectorielle locale pour les fichiers de contact."""

	def __init__(
		self,
		collection_name: str = DEFAULT_COLLECTION_NAME,
		qdrant_path: str | None = None,
		model_name: str = DEFAULT_MODEL_NAME,
		device: str | None = None,
	) -> None:
		self.collection_name = collection_name
		logger.info("Chargement du modèle dense '{}'...", model_name)
		self.model = SentenceTransformer(model_name, device=device)

		logger.info("Chargement du modèle sparse 'Qdrant/bm25' (fastembed)")
		self.sparse_model = SparseTextEmbedding("Qdrant/bm25")

		qdrant_url = os.getenv("QDRANT_URL")
		if qdrant_url:
			logger.info("Connexion à Qdrant (URL: {})", qdrant_url)
			self.client = QdrantClient(url=qdrant_url)
		else:
			logger.info("Connexion à Qdrant (path: {})", qdrant_path or ":memory:")
			self.client = QdrantClient(path=qdrant_path) if qdrant_path else QdrantClient(":memory:")
		self._create_collection_if_not_exists()

	def _create_collection_if_not_exists(self) -> None:
		existing_collections = {collection.name for collection in self.client.get_collections().collections}

		if self.collection_name in existing_collections:
			logger.info("Collection '{}' déjà existante.", self.collection_name)
			return

		logger.info("Création de la collection '{}' (dense + sparse)...", self.collection_name)
		self.client.create_collection(
			collection_name=self.collection_name,
			vectors_config={
				"dense": VectorParams(size=1024, distance=Distance.COSINE)
			},
			sparse_vectors_config={
				"bm25": SparseVectorParams(modifier=Modifier.IDF)
			}
		)
		logger.info("Collection '{}' créée.", self.collection_name)

	def add_documents(
		self,
		documents: list[dict[str, Any]],
		batch_size: int = 32,
	) -> int:
		if not documents:
			logger.warning("Aucun document à indexer.")
			return 0

		texts = [f"passage: {doc['text']}" for doc in documents]
		embeddings = self.model.encode(
			texts,
			normalize_embeddings=True,
			show_progress_bar=True,
		)
		
		sparse_embeddings = list(self.sparse_model.embed(texts, batch_size=batch_size))

		points: list[PointStruct] = []
		for index, (document, embedding) in enumerate(zip(documents, embeddings)):
			point_id = self._build_point_id(document, index)
			points.append(
				PointStruct(
					id=point_id,
					vector={
						"dense": embedding.tolist(),
						"bm25": SparseVector(
							indices=sparse_embeddings[index].indices.tolist(),
							values=sparse_embeddings[index].values.tolist(),
						)
					},
					payload={
						"text": document["text"],
						"metadata": document["metadata"],
					},
				)
			)

		inserted = 0
		for start in range(0, len(points), batch_size):
			batch = points[start : start + batch_size]
			self.client.upsert(
				collection_name=self.collection_name,
				points=batch,
				wait=True,
			)
			inserted += len(batch)
			logger.info("Batch {} inséré ({} points).", start // batch_size + 1, len(batch))

		return inserted

	@staticmethod
	def _build_point_id(document: dict[str, Any], index: int) -> str:
		metadata = document.get("metadata", {})
		source = str(metadata.get("source_file", "unknown"))
		chunk = str(metadata.get("chunk_index", index))
		text = document.get("text", "")
		digest = hashlib.sha1(f"{source}|{chunk}|{text}".encode("utf-8", errors="ignore")).hexdigest()
		return str(uuid5(NAMESPACE_URL, digest))

	def close(self) -> None:
		try:
			self.client.close()
		except Exception:
			pass


def load_documents(data_dir: Path, chunk_size: int, chunk_overlap: int) -> list[dict[str, Any]]:
	splitter = RecursiveCharacterTextSplitter(
		chunk_size=chunk_size,
		chunk_overlap=chunk_overlap,
		separators=["\n\n", "\n", ". ", " ", ""],
	)

	documents: list[dict[str, Any]] = []
	for file_path in sorted(
		path
		for extension in SUPPORTED_INPUT_EXTENSIONS
		for path in data_dir.glob(f"*{extension}")
	):
		if file_path.name == "infocontact.txt":
			continue

		raw_text = file_path.read_text(encoding="utf-8", errors="ignore").strip()
		if not raw_text:
			logger.warning("Fichier vide ignoré: {}", file_path.name)
			continue

		chunks = splitter.split_text(raw_text)
		for chunk_index, chunk_text in enumerate(chunks):
			documents.append(
				{
					"text": chunk_text,
					"metadata": {
						"source_file": file_path.name,
						"source_path": str(file_path),
						"chunk_index": chunk_index,
						"chunk_count": len(chunks),
					},
				}
			)

	return documents


def build_infocontact_db(
	data_dir: Path = DATA_DIR,
	qdrant_path: Path = DEFAULT_QDRANT_PATH,
	collection_name: str = DEFAULT_COLLECTION_NAME,
	model_name: str = DEFAULT_MODEL_NAME,
	chunk_size: int = 900,
	chunk_overlap: int = 120,
	device: str | None = None,
) -> int:
	data_dir = data_dir.resolve()
	qdrant_path = qdrant_path.resolve()
	qdrant_path.mkdir(parents=True, exist_ok=True)

	documents = load_documents(data_dir, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
	logger.info("{} chunks préparés depuis {}.", len(documents), data_dir)

	database = ContactVectorDB(
		collection_name=collection_name,
		qdrant_path=str(qdrant_path),
		model_name=model_name,
		device=device,
	)
	try:
		inserted = database.add_documents(documents)
	finally:
		database.close()

	logger.info("Base Qdrant '{}' prête dans {}.", collection_name, qdrant_path)
	return inserted


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description="Création de la base Qdrant infocontact à partir des fichiers texte du dossier Data.")
	parser.add_argument("--data-dir", type=Path, default=DATA_DIR, help="Dossier contenant les fichiers .txt à indexer")
	parser.add_argument("--qdrant-path", type=Path, default=DEFAULT_QDRANT_PATH, help="Dossier de stockage local Qdrant")
	parser.add_argument("--collection", type=str, default=DEFAULT_COLLECTION_NAME, help="Nom de la collection Qdrant")
	parser.add_argument("--model", type=str, default=DEFAULT_MODEL_NAME, help="Modèle SentenceTransformer à utiliser")
	parser.add_argument("--chunk-size", type=int, default=900, help="Taille maximale d'un chunk")
	parser.add_argument("--chunk-overlap", type=int, default=120, help="Chevauchement entre chunks")
	parser.add_argument("--device", type=str, default=None, help="Device forcé pour l'embedding (cpu, cuda, mps)")
	return parser.parse_args()


def main() -> None:
	args = parse_args()
	build_infocontact_db(
		data_dir=args.data_dir,
		qdrant_path=args.qdrant_path,
		collection_name=args.collection,
		model_name=args.model,
		chunk_size=args.chunk_size,
		chunk_overlap=args.chunk_overlap,
		device=args.device,
	)


if __name__ == "__main__":
    from Utilitaire.Utbox import setup_global_logger
    setup_global_logger(log_prefix="Update")
    main()
