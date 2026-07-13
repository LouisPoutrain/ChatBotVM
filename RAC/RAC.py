#!/usr/bin/env python3
"""RAG de contacts pour la base infocontact.

Le pipeline suit deux étapes:
1. interroger directement la base Qdrant infocontact avec la question utilisateur,
2. demander au LLM de choisir une fiche de rôle, puis résoudre le contact via ContactRole.txt.
"""

from __future__ import annotations

import argparse
import json
from loguru import logger
import os
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional
from unicodedata import normalize as unicode_normalize

import requests
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv
# pyrefly: ignore [missing-import]
from qdrant_client import QdrantClient
from qdrant_client.models import Prefetch, FusionQuery, Fusion, SparseVector
# pyrefly: ignore [missing-import]
from sentence_transformers import SentenceTransformer
from fastembed import SparseTextEmbedding

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from Utilitaire.antenne_financiere_table import TABLE_DATA as AFRV_TABLE_DATA
from Utilitaire.spiv_charges_affaires import CHARGES_AFFAIRES_SPIV




load_dotenv(PROJECT_ROOT / ".env")

LLM_API_KEY = os.getenv("LLM_API_KEY", "")
if not LLM_API_KEY:
    raise ValueError("LLM_API_KEY manquant. Ajoute-le dans le fichier .env.")

LLM_BASE_URL = os.getenv("LLM_BASE_URL", "https://llm.ilaas.fr/v1").rstrip("/")
LLM_HEADERS = {
    "Authorization": f"Bearer {LLM_API_KEY}",
    "Content-Type": "application/json",
}

DEFAULT_DATA_DIR = PROJECT_ROOT / "RAC" / "Data"
DEFAULT_QDRANT_PATH = DEFAULT_DATA_DIR / "infocontact"
DEFAULT_COLLECTION_NAME = "infocontact"
DEFAULT_CONTACT_ROLE_PATH = PROJECT_ROOT / "RAC" / "ContactRole.txt"
DEFAULT_AFRV_CONTEXT_PATH = DEFAULT_DATA_DIR / "AFRV_AFRV.txt"
DEFAULT_SPIV_CONTEXT_PATHS = [
    DEFAULT_DATA_DIR / "SPIV_SPIV.txt",
    DEFAULT_DATA_DIR / "SPIV_Chargee_Affaires_Sante_Projets.txt",
    DEFAULT_DATA_DIR / "SPIV_Chargee_Affaires_SHS_Partenariats.txt",
    DEFAULT_DATA_DIR / "SPIV_Chargee_Affaires_Sante_Experimental.txt",
    DEFAULT_DATA_DIR / "SPIV_Chargee_Affaires_Sciences_Materiaux.txt",
    DEFAULT_DATA_DIR / "SPIV_Chargee_Affaires_Science_de_la_vie_SHS.txt",
]
DEFAULT_MODEL_NAME = "intfloat/multilingual-e5-large"
DEFAULT_LOG_DIR = DEFAULT_DATA_DIR / "log"
DEFAULT_LOG_FILE = DEFAULT_LOG_DIR / "rag_contacts.txt"
VALID_ROUTING_TAGS = {"AFRV", "SPIV", "AUTRE"}
AFRV_FALLBACK_KEYWORDS = (
    "budget",
    "budgétaire",
    "crédit",
    "crédits",
    "eotp",
    "prolongation",
    "éligibil",
    "dépense",
    "marché",
    "achat",
    "recrut",
    "stagiaire",
    "cdd",
    "mission",
    "sifac",
    "oscar",
    "colloque",
    "recette",
    "paie",
    "scientifi",
    "budgetaire",
)
SPIV_FALLBACK_KEYWORDS = (
    "spiv",
    "chargé d'affaires",
    "charge d'affaires",
    "laboratoire",
    "acronyme",
    "partenariats innovations valorisation",
    "valorisation",
    "innovation",
)
JURIDIQUE_KEYWORDS = (
    "juridique",
    "droit",
    "contrat",
    "convention",
    "propriété intellectuelle",
    "brevet",
    "accord",
    "licence",
    "mandat",
    "contentieux",
    "pré-contentieux",
    "cession",
    "copropriété",
    "signature",
    "avenant",
)

# =============================================================================
# PROMPTS EXTERNALISÉS
# =============================================================================

PROMPT_SELECT_ROLE_FILE = """Tu es un routeur expert chargé d'identifier le bon interlocuteur au sein d'une université.
On te donne une question utilisateur et les extraits des fiches de rôle/service les plus pertinentes récupérées.

Ton objectif : Déterminer quel document (fichier) correspond au service ou à la personne qui DOIT traiter la demande de l'utilisateur.

Question : {question}

Contexte documentaire (Fiches de rôle) :
{rag_context}

RÈGLES D'ANALYSE :
1. Lis la question pour comprendre le besoin (ex: problème informatique, scolarité, paie).
2. Évalue le contexte : y a-t-il un fichier qui gère EXPLICITEMENT cette thématique ?
3. TRÈS IMPORTANT : Si un fichier sélectionné contient plusieurs contacts avec des rôles distincts (comme le document PJR_PJR.txt), tu dois cibler la personne exacte au lieu de donner le nom du fichier brut. Pour le PJR, choisis parmi : "PJR - Responsable", "PJR - Assistante", "PJR - Juriste", "PJR - Conventions" ou "PJR - Général".
4. NE MENTIONNE QUE LE NOM DU FICHIER EXACT (ex: "LVH1.txt") tel qu'il apparait dans le contexte sous la forme "[FICHIER X] nom_du_fichier_exact.txt". Ne mets jamais de nom de contact ou de personne ici, SAUF pour le cas particulier du PJR décrit à la règle 3.
5. Si aucun fichier ne correspond de manière évidente, tu dois impérativement répondre null.
6. Tu dois faire attention aux négations car certaines fiches affiches ce dont elles ne s'occupe pas 

FORMAT DE RÉPONSE OBLIGATOIRE :
Tu dois impérativement utiliser ces 3 balises XML dans cet ordre (n'utilise PAS de format JSON) :

<analyse>
Rédige ici ton raisonnement en 2 phrases maximum : quel est le besoin, et quel fichier ou rôle y répond le mieux.
</analyse>

<fichier>
nom_du_fichier_exact.txt OU rôle spécifique (ex: PJR - Juriste) (ou null si aucun ne correspond). Ne mets AUCUN nom de personne.
</fichier>

<raison>
Justification finale très courte de ton choix
</raison>
"""


# =============================================================================


@dataclass
class ContactMatch:
    file_name: Optional[str]
    contact_name: Optional[str]
    contact_email: Optional[str]
    raw_line: Optional[str]
    score: float = 0.0



@dataclass
class ContactRAGResult:
    question: str
    routing_tag: str
    routing_reason: Optional[str]
    requested_laboratory_acronym: Optional[str]
    ranked_files: list[dict[str, Any]]
    rag_context: str
    selected_file: Optional[str]
    contact: ContactMatch
    decision_reason: Optional[str]
    final_answer: str
    secondary_contact: Optional[ContactMatch] = None


class ContactRoleIndex:
    """Indexe ContactRole.txt pour retrouver rapidement le contact d'un fichier."""

    def __init__(self, contact_role_path: Path) -> None:
        self.contact_role_path = contact_role_path
        self._mapping = self._load_mapping(contact_role_path)
        self.allowed_file_keys = set(self._mapping.keys())

    @staticmethod
    def _normalize(text: str) -> str:
        text = unicode_normalize("NFKD", text)
        text = "".join(ch for ch in text if not unicodedata_combining(ch))
        text = text.lower().strip()
        text = re.sub(r"\.[a-z0-9]{1,5}$", "", text)
        text = re.sub(r"\s+", " ", text)
        return text

    @staticmethod
    def _load_mapping(contact_role_path: Path) -> dict[str, ContactMatch]:
        mapping: dict[str, ContactMatch] = {}
        if not contact_role_path.exists():
            logger.warning("Fichier ContactRole introuvable: {}", contact_role_path)
            return mapping

        for line in contact_role_path.read_text(encoding="utf-8", errors="ignore").splitlines():
            stripped = line.strip()
            if not stripped or "->" not in stripped or ":" not in stripped:
                continue

            file_part, right_part = stripped.split("->", 1)
            contact_part, email_part = right_part.rsplit(":", 1)

            file_name = file_part.strip()
            contact_name = contact_part.strip()
            contact_email = email_part.strip()
            raw_line = stripped

            key = ContactRoleIndex._normalize(file_name)
            mapping[key] = ContactMatch(
                file_name=file_name,
                contact_name=contact_name,
                contact_email=contact_email,
                raw_line=raw_line,
            )

        return mapping

    def resolve(self, file_name: str) -> ContactMatch:
        key = self._normalize(file_name)
        if key in self._mapping:
            return self._mapping[key]

        best_match: Optional[ContactMatch] = None
        best_score = 0.0
        for candidate_key, candidate in self._mapping.items():
            score = self._similarity(key, candidate_key)
            if score > best_score:
                best_score = score
                best_match = candidate

        if best_match is None:
            return ContactMatch(file_name=file_name, contact_name=None, contact_email=None, raw_line=None)

        return ContactMatch(
            file_name=best_match.file_name,
            contact_name=best_match.contact_name,
            contact_email=best_match.contact_email,
            raw_line=best_match.raw_line,
            score=best_score,
        )

    def is_allowed_file(self, file_name: str) -> bool:
        return self._normalize(file_name) in self.allowed_file_keys

    @staticmethod
    def _similarity(left: str, right: str) -> float:
        left_tokens = set(left.split())
        right_tokens = set(right.split())
        if not left_tokens or not right_tokens:
            return 0.0

        intersection = len(left_tokens & right_tokens)
        union = len(left_tokens | right_tokens)
        return intersection / union if union else 0.0


def unicodedata_combining(character: str) -> bool:
    from unicodedata import combining
    return bool(combining(character))


def load_prompt_context(path: Path, *, stop_at_table: bool = False, max_chars: int = 4000) -> str:
    if not path.exists():
        logger.warning("Contexte de prompt introuvable: {}", path)
        return ""

    text = path.read_text(encoding="utf-8", errors="ignore")
    if stop_at_table:
        intro_lines: list[str] = []
        for line in text.splitlines():
            if line.strip().startswith("|"):
                break
            intro_lines.append(line)
        text = "\n".join(intro_lines).strip()

    text = text.strip()
    if len(text) > max_chars:
        return f"{text[:max_chars].rstrip()}\n[...truncated...]"
    return text


def build_afrv_laboratory_index() -> dict[str, dict[str, str]]:
    index: dict[str, dict[str, str]] = {}
    for row in AFRV_TABLE_DATA:
        row_dict = {
            "cf": row.cf,
            "acronyme": row.acronyme,
            "structure": row.structure,
            "antenne_referente": row.antenne_referente,
            "responsable_af": row.responsable_af,
        }
        for key in (row.cf, row.acronyme, row.structure):
            normalized = _normalize_text_key(key)
            if normalized:
                index[normalized] = row_dict
    return index


def build_spiv_laboratory_index() -> dict[str, dict[str, Any]]:
    index: dict[str, dict[str, Any]] = {}
    for row in CHARGES_AFFAIRES_SPIV:
        row_dict = {
            "nom": row.nom,
            "email": row.email,
            "thematique": row.thematique,
            "laboratoires": list(row.laboratoires),
        }
        for laboratoire in row.laboratoires:
            normalized = _normalize_text_key(laboratoire)
            if normalized:
                index[normalized] = row_dict
    return index


def _normalize_text_key(text: str) -> str:
    text = unicode_normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata_combining(ch))
    text = text.lower().strip()
    text = re.sub(r"\.[a-z0-9]{1,5}$", "", text)
    text = re.sub(r"\s+", " ", text)
    return text


def _extract_email(text: str) -> str:
    match = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    return match.group(0) if match else text.strip()


def _contains_any(text: str, keywords: tuple[str, ...]) -> bool:
    normalized_text = _normalize_text_key(text)
    return any(_normalize_text_key(keyword) in normalized_text for keyword in keywords)


def inject_ecole_doctorale(question: str) -> str:
    """Détecte les acronymes de laboratoires et ajoute leur école doctorale à la question."""
    mapping = {
        "gehco": "EMSTU - ED 552", "greman": "EMSTU - ED 552", "lame": "EMSTU - ED 552", "pcm2e": "EMSTU - ED 552",
        "cesr": "H&L - ED 616", "cethis": "H&L - ED 616", "citeres-lat": "H&L - ED 616", "dynadiv": "H&L - ED 616",
        "ees": "H&L - ED 616", "icd": "H&L - ED 616", "intru": "H&L - ED 616", "lll": "H&L - ED 616", "pavea": "H&L - ED 616", "qualipsy": "H&L - ED 616",
        "idp": "MIPTIS - ED 551", "lifat": "MIPTIS - ED 551",
        "bbv": "SSBCV - ED 549", "boa": "SSBCV - ED 549", "воа": "SSBCV - ED 549", "cbm-nmns": "SSBCV - ED 549", "cepr": "SSBCV - ED 549", "cerca": "SSBCV - ED 549",
        "ibrain": "SSBCV - ED 549", "irbi": "SSBCV - ED 549", "ischemia": "SSBCV - ED 549", "isp": "SSBCV - ED 549", "mavivhe": "SSBCV - ED 549",
        "n2cox": "SSBCV - ED 549", "prc": "SSBCV - ED 549", "simba": "SSBCV - ED 549", "sphere": "SSBCV - ED 549",
        "citeres": "SSTED - ED 617", "citeres-cost": "SSTED - ED 617", "citeres-date": "SSTED - ED 617", "citeres-emam": "SSTED - ED 617",
        "irji": "SSTED - ED 617", "leo": "SSTED - ED 617", "prim": "SSTED - ED 617", "vallorem": "SSTED - ED 617"
    }

    search_text = question.lower()
    # Supprimer les espaces autour des tirets pour gérer "CITERES - LAT"
    search_text = re.sub(r"\s*-\s*", "-", search_text)
    search_text = unicode_normalize("NFKD", search_text)
    search_text = "".join(ch for ch in search_text if not unicodedata_combining(ch))
    
    found_eds = set()
    
    # On trie les acronymes par longueur décroissante pour matcher "citeres-lat" avant "citeres"
    for acronyme in sorted(mapping.keys(), key=len, reverse=True):
        pattern = rf"\b{re.escape(acronyme)}\b"
        if re.search(pattern, search_text):
            found_eds.add(mapping[acronyme])
            # Si on matche un acronyme long, on supprime son occurence pour ne pas matcher une sous-partie
            # Par exemple, si "citeres-lat" matche, on ne veut pas que "citeres" matche aussi (bien qu'ici ils aient des ED différentes).
            search_text = re.sub(pattern, " ", search_text)
            
    if found_eds:
        eds_str = ", ".join(sorted(list(found_eds)))
        return f"{question} (Ecole Doctorale : {eds_str})"
    return question


class ContactRAG:
    """
    Routeur Expert (RAC) : Détermine le service ou contact pertinent en fonction de la question de l'utilisateur.
    
    Il utilise une classification basée sur des mots-clés et le LLM pour déterminer le domaine de la question
    (ex: AFRV, SPIV, RH, etc.), puis récupère les informations du contact associé dans la base Qdrant.
    Gère également un état d'attente (pending_states) lorsqu'un acronyme de laboratoire est requis.
    """

    def __init__(
        self,
        qdrant_path: Path = DEFAULT_QDRANT_PATH,
        collection_name: str = DEFAULT_COLLECTION_NAME,
        contact_role_path: Path = DEFAULT_CONTACT_ROLE_PATH,
        afrv_context_path: Path = DEFAULT_AFRV_CONTEXT_PATH,
        spiv_context_paths: list[Path] = DEFAULT_SPIV_CONTEXT_PATHS,
        model_name: str = DEFAULT_MODEL_NAME,
        llm_base_url: str = LLM_BASE_URL,
        device: str | None = None,
    ) -> None:
        self.collection_name = collection_name
        self.qdrant_path = qdrant_path
        self.contact_index = ContactRoleIndex(contact_role_path)
        self.afrv_context = load_prompt_context(afrv_context_path)
        
        spiv_contexts = []
        for path in (spiv_context_paths or []):
            ctx = load_prompt_context(path)
            if ctx:
                spiv_contexts.append(ctx)
        self.spiv_context = "\n\n".join(spiv_contexts)
        self.afrv_laboratory_index = build_afrv_laboratory_index()
        self.spiv_laboratory_index = build_spiv_laboratory_index()
        self.pending_states: dict[str, dict[str, Any]] = {}
        self.llm_base_url = llm_base_url.rstrip("/")
        self.model = SentenceTransformer(model_name, device=device)
        self.sparse_model = SparseTextEmbedding("Qdrant/bm25")

        qdrant_url = os.getenv("QDRANT_URL")
        if qdrant_url:
            logger.info("Connexion à Qdrant (URL: {})", qdrant_url)
            self.client = QdrantClient(url=qdrant_url)
        else:
            logger.info("Connexion à Qdrant (path: {})", qdrant_path or ":memory:")
            self.client = QdrantClient(path=str(qdrant_path))

    def close(self) -> None:
        try:
            self.client.close()
        except Exception:
            pass

    def _llm_generate(self, model: str, prompt: str, temperature: float = 0.0) -> str:
        try:
            response = requests.post(
                f"{self.llm_base_url}/chat/completions",
                headers=LLM_HEADERS,
                json={
                    "model": model,
                    "messages": [{"role": "user", "content": prompt}],
                    "stream": False,
                    "temperature": temperature,
                    "max_tokens": 4000,
                },
                timeout=300,
            )
            data = response.json()

            if not response.ok:
                error_detail = data.get("error") or data.get("detail") or data
                raise RuntimeError(f"Erreur API LLM ({response.status_code}): {error_detail}")

            choices = data.get("choices")
            if not choices:
                raise RuntimeError(f"Réponse LLM invalide pour '{model}'")

            message = choices[0].get("message", {})
            content = message.get("content")
            if content is None:
                raise RuntimeError("Réponse LLM invalide: contenu manquant")

            response_text = str(content).strip()
            logger.info(
                "\n[LLM EXCHANGE]\nMODEL: {}\nTEMPERATURE: {}\nPROMPT:\n{}\nRESPONSE:\n{}\n{}",
                model,
                temperature,
                prompt,
                response_text,
                "-" * 120,
            )
            return response_text
        except requests.RequestException as exc:
            logger.error("Erreur LLM ({}): {}", model, exc)
            raise RuntimeError(f"Erreur LLM avec le modèle '{model}'.") from exc

    @staticmethod
    def _extract_tag_block(text: str, tag: str) -> Optional[str]:
        pattern = rf"<{tag}>\s*(.*?)\s*</{tag}>"
        match = re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL)
        if match:
            return match.group(1).strip() or None
            
        pattern_malformed = rf"</?{tag}>\s*(.*?)\s*</{tag}>"
        match = re.search(pattern_malformed, text, flags=re.IGNORECASE | re.DOTALL)
        if match:
            return match.group(1).strip() or None
            
        return None


    @staticmethod
    def _extract_possible_acronym(question: str) -> str:
        cleaned = question.strip()
        cleaned = cleaned.strip(" .,:;!?\"'()[]{}")
        cleaned = re.sub(r"^(?:acronyme|code|laboratoire|labo)\s*[:=\-]*\s*", "", cleaned, flags=re.IGNORECASE)
        return cleaned.strip()

    @staticmethod
    def _normalize_query_for_search(query: str) -> str:
        """
        Normalise la casse de certains acronymes ou mots-clés courants 
        pour améliorer la récupération Qdrant (le modèle E5 y est sensible).
        """
        acronyms = {
            "dialog": "DIALOG",
            "siham": "Siham",
            "adum": "Adum",
            "saghe": "SAGHE",
            "labbri": "Labbri",
            "saps": "SAPS",
            "rnsr": "RNSR",
            "bqei": "BQEI",
            "paacc": "PAACC",
            "afrv": "AFRV",
            "spiv": "SPIV",
            "pjr": "PJR",
        }
        normalized = query
        for key, value in acronyms.items():
            normalized = re.sub(rf"\b{key}\b", value, normalized, flags=re.IGNORECASE)
        return normalized

    def _resolve_laboratory_contact(self, routing_tag: str, acronym: str) -> tuple[Optional[ContactMatch], Optional[str]]:
        normalized_acronym = _normalize_text_key(acronym)
        if not normalized_acronym:
            return None, None

        if routing_tag == "AFRV":
            row = self.afrv_laboratory_index.get(normalized_acronym)
            if not row:
                return None, None
            file_name = row.get("acronyme") or row.get("cf") or acronym
            return (
                ContactMatch(
                    file_name=file_name,
                    contact_name=row.get("responsable_af"),
                    contact_email=_extract_email(str(row.get("antenne_referente") or "")),
                    raw_line=f"{row.get('cf')} | {row.get('acronyme')} | {row.get('structure')}",
                    score=1.0,
                ),
                file_name,
            )

        if routing_tag == "SPIV":
            row = self.spiv_laboratory_index.get(normalized_acronym)
            if not row:
                return None, None
            file_name = acronym
            return (
                ContactMatch(
                    file_name=file_name,
                    contact_name=row.get("nom"),
                    contact_email=row.get("email"),
                    raw_line=f"{row.get('nom')} | {row.get('email')} | {row.get('thematique')}",
                    score=1.0,
                ),
                file_name,
            )

        return None, None

    @staticmethod
    def _build_laboratory_request_answer(routing_tag: str, routing_reason: Optional[str]) -> str:
        return "Merci d'indiquer l'acronyme de votre laboratoire pour que je puisse vous donner le bon contact."



    def _search_query(self, query: str, limit: int = 5) -> list[dict[str, Any]]:
        query_text = f"query: {query}"
        query_embedding = self.model.encode(
            [query_text],
            show_progress_bar=False,
            normalize_embeddings=True,
        )[0].tolist()

        sparse_query = list(self.sparse_model.query_embed(query))[0]
        sparse_vector = SparseVector(
            indices=sparse_query.indices.tolist(),
            values=sparse_query.values.tolist()
        )

        if hasattr(self.client, "query_points"):
            response = self.client.query_points(
                collection_name=self.collection_name,
                prefetch=[
                    Prefetch(
                        query=query_embedding,
                        using="dense",
                        limit=limit * 2,
                    ),
                    Prefetch(
                        query=sparse_vector,
                        using="bm25",
                        limit=limit * 2,
                    )
                ],
                query=FusionQuery(fusion=Fusion.RRF),
                limit=limit,
                with_payload=True,
            )
            hits = response.points
        else:
            hits = self.client.search(
                collection_name=self.collection_name,
                query_vector=("dense", query_embedding),
                limit=limit,
                with_payload=True,
            )

        results: list[dict[str, Any]] = []
        for hit in hits:
            payload = hit.payload or {}
            results.append(
                {
                    "id": str(hit.id),
                    "text": payload.get("text", ""),
                    "metadata": payload.get("metadata", {}),
                    "score": float(getattr(hit, "score", 0.0) or 0.0),
                    "query": query,
                }
            )
        return results

    @staticmethod
    def _deduplicate_ranked_files(ranked_files: list[dict[str, Any]], top_n: int = 5) -> list[dict[str, Any]]:
        selected: list[dict[str, Any]] = []
        seen_files: set[str] = set()

        for item in ranked_files:
            source_file = str(item.get("source_file", "")).strip()
            if not source_file or source_file in seen_files:
                continue
            selected.append(item)
            seen_files.add(source_file)
            if len(selected) >= top_n:
                break

        return selected

    def _build_rag_context(self, ranked_files: list[dict[str, Any]], top_n: int = 5, max_hits_per_file: int = 3) -> str:
        selected_files = self._deduplicate_ranked_files(ranked_files, top_n=top_n)
        if not selected_files:
            return ""

        sections: list[str] = []
        for index, file_item in enumerate(selected_files, start=1):
            source_file = str(file_item.get("source_file", "unknown"))
            score = float(file_item.get("score", 0.0) or 0.0)
            hits = file_item.get("hits", [])[:max_hits_per_file]
            excerpts = []
            for hit in hits:
                text = str(hit.get("text", "")).strip()
                if text:
                    excerpts.append(text)

            section = [f"[FICHIER {index}] {source_file} | score={score:.4f}"]
            if excerpts:
                for excerpt_index, excerpt in enumerate(excerpts, start=1):
                    section.append(f"Extrait {excerpt_index}:\n{excerpt}")
            else:
                section.append("Aucun extrait disponible.")

            sections.append("\n".join(section))

        return "\n\n".join(sections)

    def _select_role_file_with_llm(
        self,
        question: str,
        rag_context: str,
        model: str = "mistral-medium-latest",
    ) -> dict[str, Optional[str]]:
        prompt = PROMPT_SELECT_ROLE_FILE.format(
            question=question,
            rag_context=rag_context,
        )

        raw = self._llm_generate(model=model, prompt=prompt, temperature=0.0)

        try:
            parsed = json.loads(raw)
            if isinstance(parsed, dict):
                return {
                    "selected_file": str(parsed.get("selected_file") or parsed.get("fichier") or "").strip() or None,
                    "reason": str(parsed.get("reason") or parsed.get("raison") or "").strip() or None,
                }
        except Exception:
            pass

        return {
            "selected_file": self._extract_tag_block(raw, "selected_file") or self._extract_tag_block(raw, "fichier") or None,
            "reason": self._extract_tag_block(raw, "reason") or self._extract_tag_block(raw, "raison") or None,
        }

    def find_relevant_file(self, question: str, limit: int = 5) -> tuple[Optional[str], list[dict[str, Any]]]:
        file_max_scores: dict[str, float] = defaultdict(float)
        file_hits: dict[str, list[dict[str, Any]]] = defaultdict(list)
        file_exact_match_bonus: dict[str, float] = defaultdict(float)

        for hit in self._search_query(question, limit=limit):
            source_file = str(hit.get("metadata", {}).get("source_file", "")).strip()
            if not source_file:
                continue
            if not self.contact_index.is_allowed_file(source_file):
                continue

            score = float(hit.get("score", 0.0) or 0.0)

            if score > file_max_scores[source_file]:
                file_max_scores[source_file] = score

            normalized_question = self._normalize(question)
            normalized_source = self._normalize(source_file)
            if normalized_source in normalized_question or normalized_question in normalized_source:
                file_exact_match_bonus[source_file] = 1.0

            file_hits[source_file].append(hit)

        ranked = sorted(
            [
                {
                    "source_file": source_file,
                    "score": file_max_scores[source_file] + file_exact_match_bonus[source_file],
                    "hits": hits_list,
                }
                for source_file, hits_list in file_hits.items()
            ],
            key=lambda item: (item["score"], item["source_file"]),
            reverse=True,
        )

        selected_file = ranked[0]["source_file"] if ranked else None
        return selected_file, ranked

    @staticmethod
    def _normalize(text: str) -> str:
        text = unicode_normalize("NFKD", text)
        text = "".join(ch for ch in text if not unicodedata_combining(ch))
        text = text.lower().strip()
        text = re.sub(r"\.[a-z0-9]{1,5}$", "", text)
        text = re.sub(r"\s+", " ", text)
        return text

    def is_pending(self, session_id: str = "default") -> bool:
        return session_id in self.pending_states

    def ask(self, question: str, llm_model: str = "mistral-medium-latest", limit: int = 5, session_id: str = "default") -> ContactRAGResult:
        """
        Point d'entrée principal du Routeur Expert.
        
        Args:
            question (str): La question de l'utilisateur.
            llm_model (str): Modèle LLM à utiliser pour la classification si nécessaire.
            limit (int): Nombre de documents à récupérer dans la base Qdrant.
            session_id (str): Identifiant de la session de l'utilisateur.
            
        Returns:
            ContactRAGResult: Un objet structuré contenant le tag de routage (ex: 'AFRV'),
                              le contact identifié, et un éventuel message de demande d'acronyme.
        """
        state = self.pending_states.get(session_id, {})
        pending_routing_tag = state.get("tag")
        pending_routing_reason = state.get("reason")
        pending_is_juridique = state.get("is_juridique", False)
        acronym_from_question = None
        acronym_match = re.search(r"\s*\(Laboratoire:\s*([A-Za-z0-9_-]+)\)", question, re.IGNORECASE)
        if acronym_match:
            acronym_from_question = acronym_match.group(1)
            question = question[:acronym_match.start()] + question[acronym_match.end():]

        if pending_routing_tag in {"AFRV", "SPIV"}:
            acronym = acronym_from_question or self._extract_possible_acronym(question)
            contact, resolved_name = self._resolve_laboratory_contact(pending_routing_tag, acronym)
            if contact is not None:
                secondary_contact = self.contact_index.resolve("PJR - Général") if pending_is_juridique else None
                routing_tag = pending_routing_tag
                routing_reason = pending_routing_reason
                self.pending_states.pop(session_id, None)
                final_answer = self._build_final_answer(
                    question=question,
                    routing_tag=routing_tag,
                    routing_reason=routing_reason,
                    requested_laboratory_acronym=acronym,
                    selected_file=resolved_name,
                    contact=contact,
                    ranked_files=[],
                    decision_reason=None,
                    secondary_contact=secondary_contact,
                )
                return ContactRAGResult(
                    question=inject_ecole_doctorale(question),
                    routing_tag=routing_tag,
                    routing_reason=routing_reason,
                    requested_laboratory_acronym=acronym,
                    ranked_files=[],
                    rag_context="",
                    selected_file=resolved_name,
                    contact=contact,
                    decision_reason=None,
                    final_answer=final_answer,
                    secondary_contact=secondary_contact,
                )

            # Acronym not found: clear the state to prevent getting stuck
            failed_tag = pending_routing_tag
            self.pending_states.pop(session_id, None)

            return ContactRAGResult(
                question=question,
                routing_tag=failed_tag,
                routing_reason="Acronyme non reconnu",
                requested_laboratory_acronym=acronym or None,
                ranked_files=[],
                rag_context="",
                selected_file=None,
                contact=ContactMatch(file_name=None, contact_name=None, contact_email=None, raw_line=None),
                decision_reason=None,
                final_answer=f"⚠️ L'acronyme '{acronym}' n'a pas été reconnu pour le service {failed_tag}. L'opération a été annulée, veuillez reposer votre question (ex: 'Comment contacter l'AFRV du laboratoire iBrain ?').",
            )

        question_injected = inject_ecole_doctorale(question)
        question_injected_norm = self._normalize_query_for_search(question_injected)
        is_juridique = _contains_any(question_injected, JURIDIQUE_KEYWORDS)

        # -------------------------------------------------------------
        # NOUVELLE LOGIQUE : Recherche Qdrant systématique en premier
        # -------------------------------------------------------------
        selected_file, ranked_files = self.find_relevant_file(question=question_injected_norm, limit=limit)
        rag_context = self._build_rag_context(ranked_files, top_n=5)
        
        try:
            decision = self._select_role_file_with_llm(
                question=question_injected,
                rag_context=rag_context,
                model=llm_model,
            )
        except RuntimeError as exc:
            logger.warning("Fallback local de selection de fichier utilisé après échec LLM: {}", exc)
            decision = {"selected_file": None, "reason": "Fallback local: LLM indisponible."}

        decision_reason = decision.get("reason")
        selected_file_decision = decision.get("selected_file")
        if selected_file_decision and selected_file_decision.strip().lower() == "null":
            selected_file = None
        else:
            selected_file = selected_file_decision or selected_file

        # -------------------------------------------------------------
        # Déduction du Routing Tag à partir de la fiche trouvée
        # -------------------------------------------------------------
        routing_tag = "AUTRE"
        if selected_file:
            norm_file = selected_file.upper()
            if norm_file.startswith("AFRV"):
                routing_tag = "AFRV"
            elif norm_file.startswith("SPIV"):
                routing_tag = "SPIV"
            # Les autres (y compris PJR_PJR) restent taggés comme "AUTRE" par défaut 
            # et on récupérera leur contact directement.

        # -------------------------------------------------------------
        # Application de la logique métier AFRV / SPIV
        # -------------------------------------------------------------
        if routing_tag in {"AFRV", "SPIV"}:
            if acronym_from_question:
                acronym = acronym_from_question
                contact, resolved_name = self._resolve_laboratory_contact(routing_tag, acronym)
                if contact is not None:
                    secondary_contact = self.contact_index.resolve("PJR - Général") if is_juridique else None
                    final_answer = self._build_final_answer(
                        question=question_injected,
                        routing_tag=routing_tag,
                        routing_reason=decision_reason,
                        requested_laboratory_acronym=acronym,
                        selected_file=resolved_name,
                        contact=contact,
                        ranked_files=ranked_files,
                        decision_reason=decision_reason,
                        secondary_contact=secondary_contact,
                    )
                    return ContactRAGResult(
                        question=question_injected,
                        routing_tag=routing_tag,
                        routing_reason=decision_reason,
                        requested_laboratory_acronym=acronym,
                        ranked_files=ranked_files,
                        rag_context=rag_context,
                        selected_file=resolved_name,
                        contact=contact,
                        decision_reason=decision_reason,
                        final_answer=final_answer,
                        secondary_contact=secondary_contact,
                    )

            # Acronyme manquant : on met en pause et on demande
            self.pending_states[session_id] = {
                "tag": routing_tag,
                "reason": decision_reason or f"Fiche {routing_tag} identifiée.",
                "is_juridique": is_juridique
            }
            final_answer = self._build_laboratory_request_answer(
                routing_tag=routing_tag,
                routing_reason=decision_reason,
            )
            return ContactRAGResult(
                question=question_injected,
                routing_tag=routing_tag,
                routing_reason=decision_reason,
                requested_laboratory_acronym=None,
                ranked_files=ranked_files,
                rag_context=rag_context,
                selected_file=selected_file,
                contact=ContactMatch(file_name=None, contact_name=None, contact_email=None, raw_line=None),
                decision_reason=decision_reason,
                final_answer=final_answer,
            )

        # -------------------------------------------------------------
        # Si le tag est AUTRE (ou PJR), on résout le contact de la fiche
        # -------------------------------------------------------------
        contact = ContactMatch(file_name=None, contact_name=None, contact_email=None, raw_line=None)
        if selected_file:
            contact = self.contact_index.resolve(selected_file)

        is_already_pjr = selected_file and "pjr" in self.contact_index._normalize(selected_file)
        secondary_contact = self.contact_index.resolve("PJR - Général") if (is_juridique and not is_already_pjr) else None

        final_answer = self._build_final_answer(
            question=question_injected,
            routing_tag=routing_tag,
            routing_reason=decision_reason,
            requested_laboratory_acronym=None,
            selected_file=selected_file,
            contact=contact,
            ranked_files=ranked_files,
            decision_reason=decision_reason,
            secondary_contact=secondary_contact,
        )
        return ContactRAGResult(
            question=question_injected,
            routing_tag=routing_tag,
            routing_reason=decision_reason,
            requested_laboratory_acronym=None,
            ranked_files=ranked_files,
            rag_context=rag_context,
            selected_file=selected_file,
            contact=contact,
            decision_reason=decision_reason,
            final_answer=final_answer,
            secondary_contact=secondary_contact,
        )

    @staticmethod
    def _build_final_answer(
        question: str,
        routing_tag: str,
        routing_reason: Optional[str],
        requested_laboratory_acronym: Optional[str],
        selected_file: Optional[str],
        contact: ContactMatch,
        ranked_files: list[dict[str, Any]],
        decision_reason: Optional[str],
        secondary_contact: Optional[ContactMatch] = None,
    ) -> str:
        lines = [f"Question: {question}"]
        lines.append(f"Balise détectée: {routing_tag}")

        if routing_reason:
            lines.append(f"Justification du routage: {routing_reason}")

        if requested_laboratory_acronym:
            lines.append(f"Acronyme du laboratoire: {requested_laboratory_acronym}")

        if routing_tag != "AUTRE":
            lines.append("Aiguillage spécifique: le contact a été résolu depuis le tableau dédié.")
            if secondary_contact and secondary_contact.contact_name:
                lines.append(f"Contact secondaire: {secondary_contact.contact_name} <{secondary_contact.contact_email}>")
            return "\n".join(lines)

        if selected_file:
            lines.append(f"Fichier le plus probable: {selected_file}")
        else:
            lines.append("Fichier le plus probable: aucun")

        if contact.contact_name and contact.contact_email:
            lines.append(f"Contact: {contact.contact_name} <{contact.contact_email}>")
        elif contact.contact_name:
            lines.append(f"Contact: {contact.contact_name}")
        else:
            lines.append("Contact: introuvable dans ContactRole.txt")

        if decision_reason:
            lines.append(f"Justification: {decision_reason}")

        if ranked_files:
            top = ranked_files[:3]
            details = ", ".join(f"{item['source_file']} ({item['score']:.3f})" for item in top)
            lines.append(f"Classement fichiers: {details}")

        return "\n".join(lines)





def log_contact_rag_result(result: ContactRAGResult) -> None:
    ranked_summary = ", ".join(
        f"{item['source_file']}({item['score']:.3f})" for item in result.ranked_files[:5]
    ) or "aucun"
    contact_label = (
        f"{result.contact.contact_name} <{result.contact.contact_email}>"
        if result.contact.contact_name and result.contact.contact_email
        else result.contact.contact_name or "introuvable"
    )

    logger.info("QUESTION: {}", result.question)
    logger.info("BALISE: {}", result.routing_tag)
    logger.info("ACRONYME: {}", result.requested_laboratory_acronym or "aucun")
    logger.info("FICHIER: {}", result.selected_file or "aucun")
    logger.info("CONTACT: {}", contact_label)
    logger.info("ROUTAGE: {}", result.routing_reason or "aucune")
    logger.info("JUSTIFICATION: {}", result.decision_reason or "aucune")
    logger.info("RANGS: {}", ranked_summary)
    logger.info("REPONSE: {}", result.final_answer.replace("\n", " | "))
    logger.info("{}", "-" * 100)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="RAG de contacts pour la base infocontact.")
    parser.add_argument("--question", type=str, help="Question utilisateur")
    parser.add_argument("--chat", action="store_true", help="Mode interactif")
    parser.add_argument("--qdrant-path", type=Path, default=DEFAULT_QDRANT_PATH, help="Chemin de la base Qdrant locale")
    parser.add_argument("--collection", type=str, default=DEFAULT_COLLECTION_NAME, help="Nom de la collection Qdrant")
    parser.add_argument("--contact-role-path", type=Path, default=DEFAULT_CONTACT_ROLE_PATH, help="Chemin du fichier ContactRole.txt")
    parser.add_argument("--llm-url", type=str, default=LLM_BASE_URL, help="URL du service LLM")
    parser.add_argument("--llm-model", type=str, default="mistral-medium-latest", help="Modèle LLM pour choisir le contact ou la fiche")
    parser.add_argument("--k", type=int, default=5, help="Nombre de résultats récupérés")
    parser.add_argument("--device", type=str, default=None, help="Device forcé pour l'embedding (cpu, cuda, mps)")
    parser.add_argument("--log-file", type=Path, default=DEFAULT_LOG_FILE, help="Fichier texte de logs dans Data/log")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    from Utilitaire.Utbox import setup_global_logger
    setup_global_logger(log_prefix="Chat")
    rag = ContactRAG(
        qdrant_path=args.qdrant_path,
        collection_name=args.collection,
        contact_role_path=args.contact_role_path,
        llm_base_url=args.llm_url,
        device=args.device,
    )

    try:
        if args.chat or not args.question:
            logger.info("Pipeline RAG contacts prêt. Tapez 'exit' pour quitter.")
            while True:
                question = input("\nVous: ").strip()
                if not question:
                    continue
                if question.lower() in {"exit", "quit", "q"}:
                    break

                result = rag.ask(question=question, llm_model=args.llm_model, limit=args.k)
                log_contact_rag_result(result)
                print(f"\n{result.final_answer}\n{'-' * 80}")
            return

        result = rag.ask(question=args.question, llm_model=args.llm_model, limit=args.k)
        log_contact_rag_result(result)
        print(f"\n{result.final_answer}\n{'-' * 80}")
    finally:
        rag.close()


if __name__ == "__main__":
    main()
