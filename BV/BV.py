from __future__ import annotations

import argparse
import json
from loguru import logger
import re
import uuid
import os
import requests
import sys
from typing import Any, Mapping, Sequence
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Chargement env pour API LLM
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv
load_dotenv(Path(__file__).resolve().parents[1] / ".env")

LLM_API_KEY = os.getenv("LLM_API_KEY", "")
LLM_BASE_URL = os.getenv("LLM_BASE_URL", "https://llm.ilaas.fr/v1").rstrip("/")
LLM_HEADERS = {
    "Authorization": f"Bearer {LLM_API_KEY}",
    "Content-Type": "application/json",
}

# pyrefly: ignore [missing-import]
from qdrant_client import QdrantClient
# pyrefly: ignore [missing-import]
from qdrant_client.models import (
    Distance, 
    PointStruct, 
    VectorParams, 
    Filter, 
    FieldCondition, 
    MatchText,
    MatchValue,
    MatchAny,
    Prefetch,
    Fusion,
    FusionQuery,
    SparseVectorParams,
    SparseVector,
    Modifier,
)
# pyrefly: ignore [missing-import]
from sentence_transformers import SentenceTransformer, CrossEncoder
# pyrefly: ignore [missing-import]
from fastembed import SparseTextEmbedding
# pyrefly: ignore [missing-import]
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Configuration du logging



class BV:
    """Gestionnaire de base vectorielle Qdrant pour un pipeline RAG.

    Modèle: intfloat/multilingual-e5-large
    Préfixes requis : 'passage: ' (documents) / 'query: ' (requêtes)
    """

    def __init__(
        self,
        collection_name: str = "documents_ed",
        path: str | None = None,
        model_name: str = "intfloat/multilingual-e5-large",
        device: str | None = None,
    ) -> None:
        """Initialise la base vectorielle et le modèle d'embedding.

        Args:
            collection_name: Nom de la collection Qdrant à utiliser.
            path: Chemin de stockage local Qdrant (`None` = instance mémoire).
            model_name: Nom du modèle SentenceTransformer pour générer les vecteurs.
            device: Accélérateur à forcer (`cuda`, `mps`, `cpu`) ou `None` pour auto-détection.

        Returns:
            None: Initialise les attributs (`collection_name`, `model`, `client`) puis prépare la collection.
        """
        # On mémorise le nom de collection pour toutes les opérations ultérieures.
        self.collection_name = collection_name
        self._is_local_qdrant = True
        
        # Sélection automatique du device si non spécifié (CUDA > MPS > CPU)
        if device is None:
            import torch
            if torch.cuda.is_available():
                device = "cuda"
            elif torch.backends.mps.is_available():
                device = "mps"
            else:
                device = "cpu"
                
        # Chargement du modèle d'embedding sur le device détecté/sélectionné.
        logger.info(f"Chargement du modèle dense '{model_name}' sur le device: {device.upper()}")
        self.model = SentenceTransformer(model_name, device=device)
        
        # Chargement du modèle sparse (BM25)
        logger.info("Chargement du modèle sparse 'Qdrant/bm25' (fastembed)")
        self.sparse_model = SparseTextEmbedding("Qdrant/bm25")
        
        # Chargement du reranker (CrossEncoder)
        logger.info(f"Chargement du Reranker 'BAAI/bge-reranker-v2-m3' sur le device: {device.upper()}")
        self.reranker = CrossEncoder("BAAI/bge-reranker-v2-m3", max_length=512, device=device)

        # Connexion à Qdrant (priorité à QDRANT_URL, puis persistant local si `path` fourni, sinon en mémoire).
        qdrant_url = os.getenv("QDRANT_URL")
        if qdrant_url:
            logger.info(f"Connexion à Qdrant (URL: {qdrant_url})")
            self.client = QdrantClient(url=qdrant_url)
            self._is_local_qdrant = False
        else:
            logger.info(f"Connexion à Qdrant (path: {path or ':memory:'})")
            self.client = QdrantClient(path=path) if path else QdrantClient(":memory:")
            self._is_local_qdrant = True

        # Création de la collection uniquement si elle n'existe pas déjà.
        self._create_collection_if_not_exists()

    def _create_collection_if_not_exists(self) -> None:
        """Crée la collection et l'index textuel si nécessaire.

        Args:
            None.

        Returns:
            None: La collection cible existe après l'appel.
        """
        # Récupération de toutes les collections existantes pour éviter une recréation inutile.
        existing_collections = {
            collection.name for collection in self.client.get_collections().collections
        }

        if self.collection_name in existing_collections:
            logger.info(f"Collection '{self.collection_name}' existante trouvée.")
            return

        # Création de la collection vectorielle avec les vecteurs nommés (dense et bm25).
        logger.info(f"Création de la collection '{self.collection_name}' avec vecteurs 'dense' (1024, COSINE) et 'bm25'.")
        self.client.create_collection(
            collection_name=self.collection_name,
            vectors_config={
                "dense": VectorParams(size=1024, distance=Distance.COSINE)
            },
            sparse_vectors_config={
                "bm25": SparseVectorParams(modifier=Modifier.IDF)
            }
        )

    def close(self) -> None:
        """Ferme proprement le client Qdrant."""
        try:
            self.client.close()
        except Exception:
            pass

    def _build_contextualized_chunks(
        self,
        chunks: Sequence[str],
        metadatas: Sequence[Mapping[str, Any]],
        context_chars: int = 350,
    ) -> list[str]:
        """Enrichit chaque chunk avec un contexte local (chunk précédent/suivant).

        Args:
            chunks: Liste des textes à indexer.
            metadatas: Métadonnées alignées avec `chunks` (même longueur).
            context_chars: Nombre de caractères à extraire autour du chunk courant.

        Returns:
            list[str]: Chunks contextualisés, prêts à être préfixés puis vectorisés.
        """
        # Liste de sortie contenant un texte enrichi par chunk d'entrée.
        contextualized: list[str] = []

        # Traitement chunk par chunk pour reconstruire un contexte local cohérent.
        for idx, chunk in enumerate(chunks):
            # Source courante: on ne mélange le contexte que dans un même document.
            current_source = str(metadatas[idx].get("source_file", ""))

            # Contexte précédent (avec coupe propre au premier espace)
            prev_text = ""
            if idx > 0 and str(metadatas[idx - 1].get("source_file", "")) == current_source:
                # Coupe sur les derniers caractères du chunk précédent.
                raw_prev = chunks[idx - 1][-context_chars:]
                space_idx = raw_prev.find(" ")
                if space_idx != -1:
                    # Coupe propre: on évite de démarrer en plein milieu de mot.
                    prev_text = raw_prev[space_idx:].strip()
                else:
                    prev_text = raw_prev.strip()

            # Contexte suivant (avec coupe propre au dernier espace)
            next_text = ""
            if idx + 1 < len(chunks) and str(metadatas[idx + 1].get("source_file", "")) == current_source:
                # Coupe sur les premiers caractères du chunk suivant.
                raw_next = chunks[idx + 1][:context_chars]
                space_idx = raw_next.rfind(" ")
                if space_idx != -1:
                    # Coupe propre: on évite de tronquer le dernier mot.
                    next_text = raw_next[:space_idx].strip()
                else:
                    next_text = raw_next.strip()

            parts: list[str] = []
            if prev_text:
                parts.append(f"[contexte précédent]\n{prev_text}")
            # Le chunk courant est toujours conservé (cœur de l'information).
            parts.append(chunk)
            if next_text:
                parts.append(f"[contexte suivant]\n{next_text}")

            contextualized.append("\n\n".join(parts))

        return contextualized

    def _check_conflicts(self, new_chunk: str, new_embedding: list[float]) -> dict[str, Any]:
        """Étape 1 et 2 du ConflictRAG : Filtre sémantique et vérification LLM."""
        try:
            hits = self.client.search(
                collection_name=self.collection_name,
                query_vector=("dense", new_embedding),
                limit=3,
                with_payload=True,
                score_threshold=0.88,  # Filtre Stage 1 (Similarité forte)
            )
        except Exception:
            return {}

        if not hits:
            return {}

        conflict_result = {}
        for hit in hits:
            existing_chunk = (hit.payload or {}).get("text", "")
            if not existing_chunk or existing_chunk == new_chunk:
                continue
            
            prompt = f"""Tu es un expert en vérification de faits.
Analyse ces deux textes pour voir s'ils contiennent des informations contradictoires.
Texte A (Nouveau) : {new_chunk}
Texte B (Existant) : {existing_chunk}

Réponds UNIQUEMENT au format JSON strict avec ces deux clés :
"has_conflict": true ou false
"conflict_type": "Factual", "Temporal", "Opinion", ou "None"
"""
            try:
                response = requests.post(
                    f"{LLM_BASE_URL}/chat/completions",
                    headers=LLM_HEADERS,
                    json={
                        "model": "mistral-medium-latest",
                        "messages": [{"role": "user", "content": prompt}],
                        "temperature": 0.0,
                    },
                    timeout=30
                )
                if response.ok:
                    data = response.json()
                    content = data.get("choices", [{}])[0].get("message", {}).get("content", "{}")
                    
                    if "```json" in content:
                        content = content.split("```json")[1].split("```")[0].strip()
                    elif "```" in content:
                        content = content.split("```")[1].split("```")[0].strip()
                        
                    res_json = json.loads(content)
                    if res_json.get("has_conflict"):
                        conflict_result = {
                            "has_conflict": True,
                            "conflict_type": res_json.get("conflict_type", "Unknown"),
                            "conflicting_with": hit.id
                        }
                        logger.warning(f"⚠️ CONFLIT DÉTECTÉ ({conflict_result['conflict_type']}) avec {hit.id}")
                        break
            except Exception as e:
                logger.error(f"Erreur lors du LLM conflict check : {e}")
                
        return conflict_result

    def add_documents(
        self,
        chunks: Sequence[str],
        metadatas: Sequence[Mapping[str, Any]],
        batch_size: int = 64,
    ) -> list[str]:
        """Ajoute des documents dans Qdrant via embeddings E5 + upsert par lot.

        Args:
            chunks: Textes à indexer.
            metadatas: Métadonnées associées à chaque chunk.
            batch_size: Taille de lot pour l'encodage et l'upsert.

        Returns:
            list[str]: Liste des IDs (déterministes) envoyés à Qdrant.

        Raises:
            ValueError: Si `chunks` et `metadatas` n'ont pas la même longueur.
        """
        # Validation d'alignement entre contenu et métadonnées.
        if len(chunks) != len(metadatas):
            raise ValueError(f"`chunks` ({len(chunks)}) et `metadatas` ({len(metadatas)}) doivent avoir la même longueur.")

        if not chunks:
            return []

        # Construction du contexte local pour améliorer la qualité sémantique des embeddings.
        contextualized_chunks = self._build_contextualized_chunks(chunks, metadatas)
        # Préfixe E5 obligatoire côté "document".
        prefixed_chunks = [f"passage: {chunk}" for chunk in contextualized_chunks]
        
        # ID Déterministe basé sur les métadonnées et le texte (évite les doublons lors des réindexations)
        ids: list[str] = [
            # Clé stable basée sur chunk_id + texte => idempotence lors des réindexations.
            str(uuid.uuid5(uuid.NAMESPACE_DNS, f"{metadatas[i].get('chunk_id', i)}_{chunk}"))
            for i, chunk in enumerate(chunks)
        ]

        # Encodage + insertion par batch pour limiter l'usage mémoire.
        for start in range(0, len(chunks), batch_size):
            end = min(start + batch_size, len(chunks))
            
            batch_texts = prefixed_chunks[start:end]
            batch_raw_chunks = chunks[start:end]
            batch_metadatas = metadatas[start:end]
            batch_ids = ids[start:end]

            # Encodage du lot courant en vecteurs normalisés (cosine-friendly).
            embeddings = self.model.encode(
                batch_texts,
                batch_size=batch_size,
                show_progress_bar=False,
                normalize_embeddings=True,
            )
            
            # Vérification des conflits (ConflictRAG Stage 1 & 2)
            # Attention: L'appel LLM rendra l'ingestion plus longue.
            for i in range(len(batch_texts)):
                conflict_info = self._check_conflicts(batch_raw_chunks[i], embeddings[i].tolist())
                if conflict_info:
                    # On injecte l'information de conflit dans les métadonnées de ce chunk
                    # On fait une copie du dictionnaire si on ne veut pas modifier l'original,
                    # ou on utilise dict()
                    pass
                
                # Mise à jour des métadonnées pour ce batch
                updated_meta = dict(batch_metadatas[i])
                if conflict_info:
                    updated_meta.update(conflict_info)
                batch_metadatas[i] = updated_meta

            # Encodage sparse BM25
            sparse_embeddings = list(self.sparse_model.embed(batch_texts, batch_size=batch_size))

            points: list[PointStruct] = [
                # Point Qdrant = id + vecteur + payload (texte brut + métadonnées).
                PointStruct(
                    id=batch_ids[i],
                    vector={
                        "dense": embeddings[i].tolist(),
                        "bm25": SparseVector(
                            indices=sparse_embeddings[i].indices.tolist(),
                            values=sparse_embeddings[i].values.tolist()
                        )
                    },
                    payload={
                        "text": batch_raw_chunks[i],
                        "metadata": dict(batch_metadatas[i]),
                    },
                )
                for i in range(len(batch_texts))
            ]

            try:
                # Upsert: ajoute/met à jour les points portant les mêmes IDs.
                self.client.upsert(
                    collection_name=self.collection_name,
                    points=points,
                    wait=True,
                )
            except Exception as e:
                logger.error(f"Échec de l'upsert pour le batch {start}-{end} : {e}")

        return ids

    def search(
        self, 
        query: str, 
        k: int = 5, 
        is_hyde: bool = True, 
        file_keyword: str | None = None, 
        domain_filter: str | list[str] | None = None,
        always_include_domain: str | None = None
    ) -> list[dict[str, Any]]:
        """Recherche des chunks pertinents dans Qdrant.

        Args:
            query: Requête utilisateur ou texte HyDE.
            k: Nombre maximal de résultats à retourner.
            is_hyde: `True` si la requête vient de HyDE (préfixe `passage:`), sinon `query:`.
            file_keyword: Filtre optionnel appliqué sur `metadata.source_file`.
            domain_filter: Filtre optionnel appliqué sur `metadata.domain_tag` (ex: "AFRV", "SPIV"). Peut être une liste.
            always_include_domain: Domaine toujours inclus via une clause OR (ex: "PJR").

        Returns:
            list[dict[str, Any]]: Résultats formatés (`id`, `text`, `metadata`, `score`).
        """
        # Préfixe E5 adapté au type de requête.
        prefix = "passage: " if is_hyde else "query: "
        # Concatène le préfixe attendu par E5 avec la requête brute.
        prefixed_query = f"{prefix}{query}"

        # Encodage de la requête en vecteur dense.
        query_embedding = self.model.encode(
            [prefixed_query],
            show_progress_bar=False,
            normalize_embeddings=True,
        )[0].tolist()

        # Filtres optionnels
        must_conditions = []
        if file_keyword is not None:
            # MatchText sur metadata.source_file pour restreindre le périmètre documentaire.
            must_conditions.append(
                FieldCondition(
                    key="metadata.source_file",
                    match=MatchText(text=file_keyword),
                )
            )
            
        if domain_filter is not None:
            if isinstance(domain_filter, list):
                must_conditions.append(
                    FieldCondition(
                        key="metadata.domain_tag",
                        match=MatchAny(any=domain_filter),
                    )
                )
            else:
                # MatchValue strict sur le tag de domaine
                must_conditions.append(
                    FieldCondition(
                        key="metadata.domain_tag",
                        match=MatchValue(value=domain_filter),
                    )
                )

        query_filter: Filter | None = None
        if must_conditions:
            if always_include_domain:
                query_filter = Filter(
                    should=[
                        Filter(must=must_conditions),
                        FieldCondition(
                            key="metadata.domain_tag",
                            match=MatchValue(value=always_include_domain),
                        )
                    ]
                )
            else:
                query_filter = Filter(must=must_conditions)

        # Génération du vecteur sparse (BM25)
        sparse_query = list(self.sparse_model.query_embed(query))[0]
        sparse_vector = SparseVector(
            indices=sparse_query.indices.tolist(),
            values=sparse_query.values.tolist()
        )

        # Compatibilité API Qdrant: `query_points` (nouveau) ou `search` (ancien).
        if hasattr(self.client, "query_points"):
            response = self.client.query_points(
                collection_name=self.collection_name,
                prefetch=[
                    Prefetch(
                        query=query_embedding,
                        using="dense",
                        limit=20,
                        filter=query_filter,
                    ),
                    Prefetch(
                        query=sparse_vector,
                        using="bm25",
                        limit=20,
                        filter=query_filter,
                    )
                ],
                query=FusionQuery(fusion=Fusion.RRF),
                limit=20,
                with_payload=True,
            )
            hits = response.points
        else:
            hits = self.client.search(
                collection_name=self.collection_name,
                query_vector=query_embedding,
                limit=20,
                with_payload=True,
                query_filter=query_filter,
            )

        # Reranking avec Cross-Encoder
        if hits:
            # Préparation des paires (requête originale, texte du document)
            pairs = [[query, str((hit.payload or {}).get("text", ""))] for hit in hits]
            
            # Calcul des scores de pertinence exacts
            rerank_scores = self.reranker.predict(pairs)
            
            # On met à jour les scores (le RRF de Qdrant est écrasé par le score précis du Reranker)
            for i, hit in enumerate(hits):
                hit.score = float(rerank_scores[i])
                
            # Tri par ordre décroissant
            hits.sort(key=lambda x: x.score, reverse=True)
            
            # Conservation du top K demandé
            hits = hits[:k]

        # Normalisation du format de sortie pour le pipeline appelant.
        return [
            {
                "id": str(hit.id),
                "text": (hit.payload or {}).get("text", ""),
                "metadata": (hit.payload or {}).get("metadata", {}),
                "score": float(hit.score),
            }
            for hit in hits
        ]


def _chunk_text(content: str, max_chars: int = 3200, overlap_chars: int = 350) -> list[str]:
    """Découpe un texte avec Langchain RecursiveCharacterTextSplitter en privilégiant des chunks plus larges."""
    cleaned = content.replace("\r\n", "\n").strip()
    if not cleaned:
        return []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=max_chars,
        chunk_overlap=overlap_chars,
        separators=["\n\n", "\n", " ", ""]
    )
    
    return splitter.split_text(cleaned)


def _load_markdown_for_indexing(md_path: Path, source_root: Path | None = None) -> tuple[list[str], list[dict[str, Any]]]:
    if not md_path.exists():
        logger.warning(f"Fichier introuvable: {md_path}")
        return [], []

    raw_text = md_path.read_text(encoding="utf-8").strip()

    # 1. LECTURE DU META.JSON
    # On déduit le chemin du json à partir du nom du md (comportement standard de Marker)
    meta_path = md_path.with_name(f"{md_path.stem}_meta.json")
    marker_meta: dict[str, Any] = {}
    if meta_path.exists():
        try:
            marker_meta = json.loads(meta_path.read_text(encoding="utf-8"))
        except Exception as e:
            logger.warning(f"Erreur lecture meta.json pour {md_path.name}: {e}")

    # Découpage du texte
    texts = _chunk_text(raw_text)
    relative_source = str(md_path.relative_to(source_root)) if source_root and md_path.is_relative_to(source_root) else str(md_path)

    domain_tag = ""
    if source_root and md_path.is_relative_to(source_root):
        rel_parts = md_path.relative_to(source_root).parts
        if len(rel_parts) > 1:
            domain_tag = rel_parts[0]

    metadatas: list[dict[str, Any]] = []

    for idx, text_chunk in enumerate(texts):
        # 2. DÉTECTION DES IMAGES DANS LE CHUNK
        # Marker génère des balises Markdown standard : ![alt_text](chemin_image.jpg)
        # On extrait les chemins des images présentes spécifiquement dans CE chunk
        chunk_images = re.findall(r'!\[.*?\]\((.*?)\)', text_chunk)

        # On résout le chemin absolu de l'image pour que le frontend puisse la retrouver plus tard
        resolved_image_paths = [str(md_path.parent / img_path) for img_path in chunk_images]

        chunk_meta = {
            "source_file": relative_source,
            "source_name": md_path.name,
            "document_name": md_path.stem,
            "document_folder": md_path.parent.name,
            "section": "marker_markdown",
            "chunk_id": f"{md_path.stem}-md-{idx}",
            "source_type": "markdown",
            "domain_tag": domain_tag,

            # --- INJECTION DU META.JSON ---
            # On récupère les infos utiles si elles existent
            "languages": marker_meta.get("languages", []),
            "has_table_of_contents": bool(marker_meta.get("table_of_contents")),
            "marker_stats": marker_meta.get("ocr_stats", {}),

            # --- INJECTION DES IMAGES ---
            "has_images": len(resolved_image_paths) > 0,
            "image_paths": resolved_image_paths,
        }
        metadatas.append(chunk_meta)

    return texts, metadatas


def _discover_markdown_dir(project_root: Path, markdown_dir_arg: str | None) -> Path | None:
    if markdown_dir_arg:
        markdown_dir = Path(markdown_dir_arg)
        if not markdown_dir.is_absolute():
            markdown_dir = project_root / markdown_dir
        return markdown_dir

    # Priorité au dossier PDF2 actuellement utilisé dans ce projet.
    candidate_dirs = [
        project_root / "PDF2",
        project_root / "TestExtraction" / "data" / "marker_markdown" / "PDF2",
    ]

    for directory in candidate_dirs:
        if directory.exists() and directory.is_dir():
            return directory

    return None


def _iter_markdown_files(markdown_dir: Path) -> list[Path]:
    if not markdown_dir.exists() or not markdown_dir.is_dir():
        raise FileNotFoundError(f"Dossier introuvable: {markdown_dir}")

    markdown_files = sorted(markdown_dir.rglob("*.md"))
    if not markdown_files:
        logger.warning(f"Aucun fichier Markdown trouvé dans: {markdown_dir}")
    return markdown_files


if __name__ == "__main__":
    from Utilitaire.Utbox import setup_global_logger
    setup_global_logger(log_prefix="Update")
    parser = argparse.ArgumentParser(description="Création de base vectorielle Qdrant (E5) à partir des markdown PDF2.")
    parser.add_argument("--markdown-dir", type=str, default=None, help="Optionnel: dossier des fichiers Markdown (par défaut: TestExtraction/data/PDF2)")
    parser.add_argument("--collection", type=str, default="pdf2_documents", help="Nom de la collection Qdrant")
    parser.add_argument("--qdrant-path", type=str, default=None, help="Chemin de stockage Qdrant local (par défaut: TestExtraction/qdrant_data)")
    args = parser.parse_args()

    # BV.py est dans ChatBot/BV -> la racine utile est ChatBot
    project_root = Path(__file__).resolve().parents[1]
    markdown_dir = _discover_markdown_dir(project_root, args.markdown_dir)
    qdrant_path = Path(args.qdrant_path) if args.qdrant_path else project_root / "TestExtraction" / "qdrant_data"
    if not qdrant_path.is_absolute():
        qdrant_path = project_root / qdrant_path

    logger.info(f"Répertoire markdown résolu: {markdown_dir}")
    logger.info(f"Qdrant path résolu: {qdrant_path}")

    logger.info("=" * 80)
    logger.info(" CRÉATION BASE VECTORIELLE QDRANT")
    logger.info("=" * 80)
    
    bv: BV | None = None
    try:
        bv = BV(collection_name=args.collection, path=str(qdrant_path))

        if markdown_dir is None:
            logger.warning("Aucun dossier Markdown valide trouvé pour l'indexation.")
        else:
            markdown_files = _iter_markdown_files(markdown_dir)
            total_markdown_vectors = 0

            for idx, md_file in enumerate(markdown_files, start=1):
                texts, metadatas = _load_markdown_for_indexing(md_file, markdown_dir)
                if texts:
                    ids = bv.add_documents(texts, metadatas)
                    total_markdown_vectors += len(ids)
                    logger.info(f"[MD {idx}/{len(markdown_files)}] {md_file.name}: {len(ids)} vecteurs insérés.")
                else:
                    logger.info(f"[MD {idx}/{len(markdown_files)}] {md_file.name}: 0 chunk valide.")

            logger.info(f" Bilan: {total_markdown_vectors} vecteurs Markdown insérés dans '{args.collection}'.")
            
    except Exception as e:
        logger.error(f"Une erreur critique est survenue : {e}")
    finally:
        if bv is not None:
            bv.close()