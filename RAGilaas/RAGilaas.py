from __future__ import annotations

import argparse
import importlib.util
from loguru import logger
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

import requests
from requests.exceptions import RequestException
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv
MODULE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(MODULE_DIR) not in sys.path:
    sys.path.insert(0, str(MODULE_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from Prompt import PROMPT_HYDE, build_answer_prompt

# IMPORT QDRANT
# pyrefly: ignore [missing-import]
from qdrant_client import QdrantClient

# ==============================================================================
# CONFIGURATION ET IMPORT DYNAMIQUE
# ==============================================================================

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

LLM_API_KEY = os.getenv("LLM_API_KEY", "")
if not LLM_API_KEY:
    raise ValueError("LLM_API_KEY manquant. Ajoute-le dans le fichier .env.")

LLM_BASE_URL = os.getenv("LLM_BASE_URL", "https://llm.ilaas.fr/v1").rstrip("/")
LLM_HEADERS = {
    "Authorization": f"Bearer {LLM_API_KEY}",
    "Content-Type": "application/json",
}

candidate_bv_paths = [
    PROJECT_ROOT / "BV" / "BV.py",
    PROJECT_ROOT / "TestExtraction" / "BV" / "BV.py",
    PROJECT_ROOT / "Traitement" / "BV" / "BV_Unstructured.py",
    PROJECT_ROOT / "Traitement " / "BV" / "BV_Unstructured.py",
    PROJECT_ROOT / "Traitement" / "BV" / "BV.py",
    PROJECT_ROOT / "Traitement " / "BV" / "BV.py",
]

BV_PATH = next((p for p in candidate_bv_paths if p.exists()), None)
if BV_PATH is None:
    searched = "\n - ".join(str(p) for p in candidate_bv_paths)
    raise FileNotFoundError(f"Impossible de localiser le module BV. Chemins testés:\n - {searched}")

TRAITEMENT_DIR = BV_PATH.parent
if str(TRAITEMENT_DIR) not in sys.path:
    sys.path.insert(0, str(TRAITEMENT_DIR))

BV_SPEC = importlib.util.spec_from_file_location("traitement_bv", BV_PATH)

if BV_SPEC is None or BV_SPEC.loader is None:
    raise ImportError(f"Impossible de charger BV depuis {BV_PATH}")

BV_MODULE = importlib.util.module_from_spec(BV_SPEC)
sys.modules[BV_SPEC.name] = BV_MODULE
BV_SPEC.loader.exec_module(BV_MODULE)
BV = BV_MODULE.BV

RAC_PATH = PROJECT_ROOT / "RAC" / "RAC.py"
if not RAC_PATH.exists():
    raise FileNotFoundError(f"Impossible de localiser le module RAC. Chemin testé: {RAC_PATH}")

RAC_SPEC = importlib.util.spec_from_file_location("rac_contact", RAC_PATH)
if RAC_SPEC is None or RAC_SPEC.loader is None:
    raise ImportError(f"Impossible de charger RAC depuis {RAC_PATH}")

RAC_MODULE = importlib.util.module_from_spec(RAC_SPEC)
sys.modules[RAC_SPEC.name] = RAC_MODULE
RAC_SPEC.loader.exec_module(RAC_MODULE)
ContactRAG = RAC_MODULE.ContactRAG


# ==============================================================================
# MODÈLES DE DONNÉES
# ==============================================================================

@dataclass
class RAGResponse:
    question: str
    extracted_acronym: Optional[str]
    routed_keyword: Optional[str]
    hyde_model: str
    answer_model: str
    hypothetical_answer: str
    retrieved_chunks: list[dict[str, Any]]
    internal_draft: Optional[str]
    final_answer: str
    prompt_variant: str = "default"
    context_order: str = "preserve"
    routing_message: Optional[str] = None
    contact_info: Optional[str] = None
    agentic_iterations: list[dict[str, Any]] = None # NOUVEAU: Historique de la boucle agentique
    routing_tag: Optional[str] = None
    routing_reason: Optional[str] = None
    decision_reason: Optional[str] = None


# ==============================================================================
# PIPELINE RAG
# ==============================================================================

class HypotheticalRAG:
    """
    Pipeline RAG Hybride combinant le routeur RAC, la génération sémantique HyDE et la réponse finale.
    
    Cette classe gère le flux complet d'une question utilisateur:
    1. Interrogation du routeur RAC pour obtenir la fiche expert.
    2. Génération d'une réponse hypothétique (HyDE) si nécessaire.
    3. Recherche vectorielle dans Qdrant basée sur la question et le HyDE.
    4. Génération de la réponse finale avec le LLM en injectant le contexte.
    """

    def __init__(
        self,
        bv_instance: BV,
        llm_base_url: str = LLM_BASE_URL,
        draft_model: str = "mistral-medium-latest",
        answer_model: str = "mistral-medium-latest",
        rac_model: str = "mistral-medium-latest",
        prompt_variant: str = "default",
        context_order: str = "preserve",
    ) -> None:
        self.bv = bv_instance
        self.llm_base_url = llm_base_url.rstrip("/")
        self.draft_model = draft_model
        self.answer_model = answer_model
        self.rac_model = rac_model
        self.prompt_variant = prompt_variant
        self.context_order = context_order
        self.contact_rag = ContactRAG(
            qdrant_path=PROJECT_ROOT / "RAC" / "Data" / "infocontact",
            contact_role_path=PROJECT_ROOT / "RAC" / "ContactRole.txt",
            llm_base_url=self.llm_base_url,
        )
        self.pending_initial_questions: dict[str, str] = {}

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
                    "max_tokens": 30000,
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
                raise RuntimeError(f"Réponse LLM invalide: contenu manquant")

            return str(content).strip()
        except RequestException as exc:
            logger.error(f"Erreur LLM ({model}): {exc}")
            raise RuntimeError(f"Erreur LLM avec le modèle '{model}'.") from exc
        except Exception as exc:
            logger.error(f"Exception non prévue ({model}): {exc}")
            raise

    @staticmethod
    def _extract_tag_block(text: str, tag: str) -> Optional[str]:
        pattern = rf"<{tag}>\s*(.*?)\s*</{tag}>"
        match = re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL)
        if not match: return None
        return match.group(1).strip() or None

    def _parse_answer_blocks(self, raw_answer: str) -> tuple[Optional[str], str]:
        internal_draft = self._extract_tag_block(raw_answer, "brouillon_interne")
        user_answer = self._extract_tag_block(raw_answer, "reponse_utilisateur")
        return internal_draft, (user_answer or raw_answer).strip()

    @staticmethod
    def _format_contact_info(contact_dict: dict[str, Optional[str]]) -> str:
        name = (contact_dict.get("contact_nom") or "").strip()
        email = (contact_dict.get("contact_email") or "").strip()

        if name and email:
            return f"{name} : {email}"
        if email:
            return email
        if name:
            return name
        return ""

    @staticmethod
    def _ensure_required_contact(answer: str, contact_info: str) -> str:
        if not contact_info:
            return answer
        if contact_info in answer:
            return answer

        parts = [p.strip() for p in contact_info.split(":") if p.strip()]
        if parts and any(part in answer for part in parts if len(part) > 3):
            return answer

        separator = "\n\n" if answer.strip() else ""
        return f"{answer.rstrip()}{separator}Contact a utiliser : {contact_info}"

    def _route_question(self, question: str, session_id: str = "default"):
        """Interroge RAC pour obtenir la fiche de rôle et le contact associé."""
        return self.contact_rag.ask(question=question, llm_model=self.rac_model, limit=5, session_id=session_id)

    def _build_context(self, hits: list[dict[str, Any]]) -> str:
        if not hits: return ""
        parts = [
            f"[DOC {i}] source={hit.get('metadata', {}).get('source_file', 'unknown')} "
            f"| section={hit.get('metadata', {}).get('section', 'unknown')} "
            f"| score={hit.get('score', 0.0):.4f}\n{hit.get('text', '')}"
            for i, hit in enumerate(hits, start=1)
        ]
        return "\n\n".join(parts)

    def _order_hits_for_prompt(self, hits: list[dict[str, Any]], context_order: str) -> list[dict[str, Any]]:
        ordered_hits = list(hits)
        if context_order == "reverse": return list(reversed(ordered_hits))
        if context_order == "score_asc":
            return sorted(ordered_hits, key=lambda h: (float(h.get("score", 0.0)), str(h.get("metadata", {}).get("source_file", ""))))
        if context_order == "score_desc":
            return sorted(ordered_hits, key=lambda h: (float(h.get("score", 0.0)), str(h.get("metadata", {}).get("source_file", ""))), reverse=True)
        if context_order == "source_file":
            return sorted(ordered_hits, key=lambda h: str(h.get("metadata", {}).get("source_file", "")))
        return ordered_hits

    @staticmethod
    def _parse_context_request(requested_context: str) -> tuple[Optional[str], Optional[str]]:
        cleaned = requested_context.strip()
        if not cleaned:
            return None, None

        upper = cleaned.upper()
        if upper.startswith("FICHIER=") or upper.startswith("FILE="):
            value = cleaned.split("=", 1)[1].strip()
            return value or None, None

        if upper.startswith("MOTS_CLES=") or upper.startswith("MOTS-CLES=") or upper.startswith("KEYWORDS="):
            value = cleaned.split("=", 1)[1].strip()
            return None, value or None

        if re.search(r"[\\/]", cleaned):
            return cleaned, None

        if re.search(r"\.[A-Za-z0-9]{2,5}$", cleaned):
            return cleaned, None

        return None, cleaned

    def ask(self, question: str, k: int = 6, prompt_variant: Optional[str] = None, context_order: Optional[str] = None, session_id: str = "default") -> RAGResponse:
        """
        Traite une question utilisateur et génère une réponse documentée.
        
        Args:
            question (str): La question posée par l'utilisateur.
            k (int): Le nombre maximum de chunks de contexte à récupérer.
            prompt_variant (str, optional): La variante du prompt de réponse (ex: 'concise', 'detailed').
            context_order (str, optional): L'ordre de tri des chunks (ex: 'score_desc').
            session_id (str): L'identifiant de la session pour la gestion stateless du RAG.
            
        Returns:
            RAGResponse: Un objet structuré contenant la réponse finale, les infos de contact et les métadonnées de l'exécution.
        """
        was_pending = self.contact_rag.is_pending(session_id)

        # 0. ROUTEUR RAC : sélection de la fiche de rôle, ou demande de l'acronyme du laboratoire
        decision = self._route_question(question, session_id)

        is_pending = self.contact_rag.is_pending(session_id)
        
        if not was_pending and is_pending:
            self.pending_initial_questions[session_id] = decision.question
            actual_question_for_rag = decision.question
        elif was_pending and not is_pending:
            base_question = self.pending_initial_questions.get(session_id, decision.question)
            lab_info = decision.question
            actual_question_for_rag = f"{base_question} (Laboratoire concerné : {lab_info})"
            self.pending_initial_questions.pop(session_id, None)
        elif was_pending and is_pending:
            actual_question_for_rag = self.pending_initial_questions.get(session_id, decision.question)
        else:
            actual_question_for_rag = decision.question

        contact_dict = {
            "contact_nom": decision.contact.contact_name,
            "contact_email": decision.contact.contact_email,
            "selected_file": decision.selected_file,
            "decision_reason": decision.decision_reason,
        }
        contact_info_str = self._format_contact_info(contact_dict)
        
        secondary_contact = getattr(decision, "secondary_contact", None)
        if secondary_contact and secondary_contact.contact_name:
            sec_dict = {
                "contact_nom": secondary_contact.contact_name,
                "contact_email": secondary_contact.contact_email,
            }
            sec_str = self._format_contact_info(sec_dict)
            if contact_info_str:
                contact_info_str += f" | Contact secondaire (Pôle Juridique) : {sec_str}"
            else:
                contact_info_str = f"Contact (Pôle Juridique) : {sec_str}"

        if decision.routing_tag in {"AFRV", "SPIV"} and not contact_info_str:
            return RAGResponse(
                question=actual_question_for_rag,
                extracted_acronym=decision.requested_laboratory_acronym,
                routed_keyword=decision.routing_tag,
                hyde_model=f"{self.draft_model} (Bypass: True)",
                answer_model=self.answer_model,
                hypothetical_answer="N/A (RAC domain routing)",
                retrieved_chunks=[],
                internal_draft=None,
                final_answer=decision.final_answer,
                prompt_variant=prompt_variant or self.prompt_variant,
                context_order=context_order or self.context_order,
                routing_message=decision.final_answer,
                contact_info=None,
                agentic_iterations=[],
                routing_tag=decision.routing_tag,
                routing_reason=decision.routing_reason,
                decision_reason=decision.decision_reason,
            )

        # Mapping des fichiers du RAC (ex: Etude doctorale2.txt) vers les sous-chaînes de noms originaux (ex: ETUDES DOCTORALES)
        file_keyword = decision.selected_file
        if file_keyword:
            lower_kw = file_keyword.lower()
            if "etude doctorale" in lower_kw or "études doctorales" in lower_kw or "etudes doctorales" in lower_kw or "ecole doctorale" in lower_kw or "ecoles doctorales" in lower_kw:
                file_keyword = "ETUDES DOCTORALES"
            elif "pjr" in lower_kw:
                file_keyword = "Juridique"
            elif "saps" in lower_kw:
                file_keyword = "SAPS"
            elif "hdr" in lower_kw:
                file_keyword = "HDR"
            elif file_keyword.endswith(".txt"):
                file_keyword = file_keyword[:-4]
                
        fetch_k = k * 3
        
        # 2. BYPASS HYDE
        def_keywords = ["c'est quoi", "que veut dire", "signifie", "acronyme", "définition", "definition", "que représente", "correspond"]
        is_definition = any(kw in actual_question_for_rag.lower() for kw in def_keywords)
        acronym_pattern = r"\b[A-Z][A-Z0-9-]{1,}\b"
        detected_acronyms = re.findall(acronym_pattern, actual_question_for_rag)
        has_explicit_acronym = len(detected_acronyms) > 0

        should_bypass_hyde = is_definition or has_explicit_acronym

        if should_bypass_hyde:
            dense_query = actual_question_for_rag
            is_hyde_used = False
            bypass_reasons = []
            if is_definition: bypass_reasons.append("question de définition")
            if has_explicit_acronym: bypass_reasons.append(f"acronyme: {', '.join(detected_acronyms)}")
            hypothetical_answer = f"N/A (Bypass - {' ; '.join(bypass_reasons)})"
        else:
            prompt_hyp = PROMPT_HYDE.format(question_utilisateur=actual_question_for_rag)
            hypothetical_answer = self._llm_generate(self.draft_model, prompt_hyp)
            dense_query = hypothetical_answer
            is_hyde_used = True

        is_juridique_query = False
        if file_keyword == "Juridique":
            is_juridique_query = True
        elif secondary_contact and secondary_contact.file_name and "pjr" in secondary_contact.file_name.lower():
            is_juridique_query = True
            
        include_pjr_domain = "PJR" if is_juridique_query else None

        # 3. RECHERCHE SÉMANTIQUE
        domain_mapping = {
            "AFRV": "AFRV",
            "SPIV": "SPIV",
            "AUTRE": "Autre"
        }
        domain_tag = domain_mapping.get(decision.routing_tag.upper()) if decision.routing_tag else None

        domain_filter_list = [domain_tag, "Guide du DU", "Guide du DU "] if domain_tag is not None else None
        if domain_filter_list is not None and include_pjr_domain:
            domain_filter_list.append(include_pjr_domain)

        semantic_hits = self.bv.search(query=dense_query, k=fetch_k, is_hyde=is_hyde_used, file_keyword=file_keyword, domain_filter=domain_filter_list, always_include_domain=include_pjr_domain)

        if not semantic_hits and file_keyword is not None:
            logger.info(f"Aucun fichier trouvé pour '{file_keyword}', recherche par domaine...")
            semantic_hits = self.bv.search(query=dense_query, k=fetch_k, is_hyde=is_hyde_used, file_keyword=None, domain_filter=domain_filter_list, always_include_domain=include_pjr_domain)
            file_keyword = f"{file_keyword} (Échec du filtre fichier)"

        if not semantic_hits and domain_tag is not None:
            logger.info(f"Aucun fichier trouvé pour le domaine '{domain_tag}', recherche globale complète...")
            semantic_hits = self.bv.search(query=dense_query, k=fetch_k, is_hyde=is_hyde_used, file_keyword=None, domain_filter=None, always_include_domain=include_pjr_domain)
            file_keyword = f"{file_keyword} (Échec du filtre domaine)" if file_keyword else "(Échec du filtre domaine)"

        # 4. NETTOYAGE ET DÉDUPLICATION
        cleaned_hits: list[dict[str, Any]] = []
        seen_texts: set[str] = set()

        for hit in semantic_hits:
            text = str(hit.get("text", ""))
            if text in seen_texts: continue

            stripped_text = text.replace("``", "").strip()
            if len(stripped_text) < 30: continue

            alpha_ratio = sum(c.isalpha() for c in stripped_text) / max(1, len(stripped_text))
            if alpha_ratio < 0.5: continue

            cleaned_hits.append(hit)
            seen_texts.add(text)
            if len(cleaned_hits) >= k: break

        active_prompt_variant = prompt_variant or self.prompt_variant
        active_context_order = context_order or self.context_order

        # 5. RÉPONSE FINALE AVEC BOUCLE AGENTIQUE
        max_agent_iterations = 2
        agent_iteration = 0
        agentic_iterations_log = [] # Initialisation de l'historique
        
        while agent_iteration < max_agent_iterations:
            agent_iteration += 1
            
            # Reconstruire le contexte documentaire (qui grandit à chaque itération)
            ordered_hits = self._order_hits_for_prompt(cleaned_hits, active_context_order)
            context_documents = self._build_context(ordered_hits)
            
            if contact_info_str:
                context = (
                    f"[CONTACT RAC OBLIGATOIRE]\n{contact_info_str}\n"
                    f"[DOCUMENTS ET PROCÉDURES RÉTROUVÉS]\n{context_documents}"
                )
            else:
                context = context_documents

            prompt_final = build_answer_prompt(
                contexte_retrouve_depuis_la_base_vectorielle=context,
                question_utilisateur=actual_question_for_rag,
                variant=active_prompt_variant,
            )
            raw_final_answer = self._llm_generate(self.answer_model, prompt_final, temperature=0.0)
            internal_draft, final_answer = self._parse_answer_blocks(raw_final_answer)
            # Nettoyage au cas où le modèle aurait laissé fuiter la balise dans la réponse finale
            final_answer = re.sub(r"\[REQUIERT_PLUS_DE_CONTEXTE:.*?\]", "", final_answer).strip()
            final_answer = self._ensure_required_contact(final_answer, contact_info_str)
            
            # Création du journal pour cette itération spécifique
            current_iteration_log = {
                "iteration": agent_iteration,
                "internal_draft": internal_draft,
                "requested_file": None,
                "requested_keywords": None,
                "new_chunks_added": 0
            }

            # Détection de la demande de contexte supplémentaire (Boucle ReAct)
            if internal_draft and "[REQUIERT_PLUS_DE_CONTEXTE:" in internal_draft:
                match = re.search(r"\[REQUIERT_PLUS_DE_CONTEXTE:\s*(.*?)\]", internal_draft)
                if match:
                    requested_raw = match.group(1).strip()
                    requested_file, requested_keywords = self._parse_context_request(requested_raw)
                    current_iteration_log["requested_file"] = requested_file
                    current_iteration_log["requested_keywords"] = requested_keywords

                    if requested_file:
                        logger.info(
                            f"[Agentic RAG] Itération {agent_iteration} - Demande de contexte fichier : {requested_file}"
                        )
                        extra_hits = self.bv.search(
                            query=dense_query,
                            k=fetch_k * 2,
                            is_hyde=is_hyde_used,
                            file_keyword=requested_file,
                            domain_filter=domain_filter_list,
                            always_include_domain=include_pjr_domain
                        )
                    elif requested_keywords:
                        logger.info(
                            f"[Agentic RAG] Itération {agent_iteration} - Demande de contexte mots_cles : {requested_keywords}"
                        )
                        keyword_query = f"{requested_keywords}\n{dense_query}" if dense_query else requested_keywords
                        extra_hits = self.bv.search(
                            query=keyword_query,
                            k=fetch_k * 2,
                            is_hyde=is_hyde_used,
                            file_keyword=None,
                            domain_filter=domain_filter_list,
                            always_include_domain=include_pjr_domain
                        )
                        if not extra_hits and domain_tag is not None:
                            extra_hits = self.bv.search(
                                query=keyword_query,
                                k=fetch_k * 2,
                                is_hyde=is_hyde_used,
                                file_keyword=None,
                                domain_filter=None,
                                always_include_domain=include_pjr_domain
                            )
                    else:
                        logger.info(
                            f"[Agentic RAG] Itération {agent_iteration} - Demande de contexte vide ou invalide."
                        )
                        extra_hits = []
                    
                    added_new_chunks = 0
                    for eh in extra_hits:
                        eh_text = str(eh.get("text", ""))
                        if eh_text not in seen_texts:
                            cleaned_hits.append(eh)
                            seen_texts.add(eh_text)
                            added_new_chunks += 1
                    
                    current_iteration_log["new_chunks_added"] = added_new_chunks
                    agentic_iterations_log.append(current_iteration_log) # Sauvegarde du log

                    if added_new_chunks > 0 and agent_iteration < max_agent_iterations:
                        logger.info(f"[Agentic RAG] {added_new_chunks} nouveaux extraits trouvés. Relance de la boucle.")
                        continue  # On boucle avec le contexte élargi
            else:
                # Si aucune demande de contexte, on log l'itération classique
                agentic_iterations_log.append(current_iteration_log)

            break  # On sort de la boucle si on ne demande rien ou si on a atteint la limite

        return RAGResponse(
            question=actual_question_for_rag,
            extracted_acronym=None,
            routed_keyword=file_keyword,
            hyde_model=f"{self.draft_model} (Bypass: {not is_hyde_used})",
            answer_model=self.answer_model,
            hypothetical_answer=hypothetical_answer,
            retrieved_chunks=ordered_hits,
            internal_draft=internal_draft, # Garde le dernier pour rétrocompatibilité
            final_answer=final_answer,
            prompt_variant=active_prompt_variant,
            context_order=active_context_order,
            contact_info=contact_info_str or None,
            agentic_iterations=agentic_iterations_log, # On passe l'historique complet
            routing_tag=decision.routing_tag,
            routing_reason=decision.routing_reason,
            decision_reason=decision.decision_reason,
        )

    def close(self) -> None:
        try:
            self.contact_rag.close()
        except Exception:
            pass


# ==============================================================================
# CLI ET LOGS
# ==============================================================================



def log_rag_execution(result: RAGResponse) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    retrieved_lines = [
        f"📄 DOC {i} | score={hit.get('score', 0):.4f} | source={hit.get('metadata', {}).get('source_file', 'unknown')}\n{hit.get('text', '')}"
        for i, hit in enumerate(result.retrieved_chunks, start=1)
    ]
    
    contact_section = result.contact_info or "Aucun contact identifié"
    if isinstance(contact_section, str):
        contact_lines = contact_section.splitlines()
        if contact_lines and contact_lines[0].strip().lower().startswith("question:"):
            contact_section = "\n".join(contact_lines[1:]).strip() or "Aucun contact identifié"

    agent_logs_str = ""
    if result.agentic_iterations:
        for it in result.agentic_iterations:
            agent_logs_str += f"   🔄 Itération {it['iteration']}\n"
            agent_logs_str += f"      [Pensée] :\n      {it['internal_draft'] or 'Aucun brouillon'}\n"
            if it.get('requested_file'):
                agent_logs_str += f"      [Action] : REQUIERT_PLUS_DE_CONTEXTE (Fichier: {it['requested_file']})\n"
                agent_logs_str += f"      [Résultat] : {it['new_chunks_added']} nouveaux fragments ajoutés.\n"
            elif it.get('requested_keywords'):
                agent_logs_str += f"      [Action] : REQUIERT_PLUS_DE_CONTEXTE (Mots-clés: {it['requested_keywords']})\n"
                agent_logs_str += f"      [Résultat] : {it['new_chunks_added']} nouveaux fragments ajoutés.\n"
            else:
                agent_logs_str += "      [Action] : Génération finale.\n"
    else:
        agent_logs_str = "   Aucune itération agentique."

    log_entry = (
        f"\n{'=' * 80}\n"
        f" [TIMESTAMP] {timestamp}\n"
        f" [QUESTION]\n{result.question}\n\n"
        
        f" [ROUTAGE & CONTACTS]\n"
        f"   - Balise Domaine  : {result.routing_tag or 'AUTRE'}\n"
        f"   - Raison Domaine  : {result.routing_reason or 'N/A'}\n"
        f"   - Acronyme Labo   : {result.extracted_acronym or 'Aucun'}\n"
        f"   - Fichier Routeur : {result.routed_keyword or 'Aucun'}\n"
        f"   - Raison Fichier  : {result.decision_reason or 'N/A'}\n"
        f"   - Contact Final   :\n{contact_section}\n\n"
        
        f" [MODÈLES UTILISÉS]\n"
        f"   - HyDE    : {result.hyde_model}\n"
        f"   - Réponse : {result.answer_model}\n\n"
        
        f" [DOCUMENT HYPOTHÉTIQUE (HyDE)]\n"
        f"{result.hypothetical_answer}\n\n"
        
        f" [BOUCLE AGENTIQUE]\n"
        f"{agent_logs_str}\n\n"
        
        f" [DOCUMENTS RÉCUPÉRÉS] (Total: {len(result.retrieved_chunks)})\n"
        f"{chr(10).join(retrieved_lines) if retrieved_lines else 'Aucun document'}\n\n"
        
        f" [RÉPONSE FINALE]\n"
        f"{result.final_answer}\n"
        f"{'=' * 80}\n"
    )
    logger.info(log_entry)

def print_debug_info(result: RAGResponse) -> None:
    print(f"\n{'=' * 80}\n 🎯 ROUTEUR & CONTACTS :\n{'=' * 80}")
    print(f" -> Balise Domaine : {result.routing_tag or 'AUTRE'}")
    print(f" -> Raison Domaine : {result.routing_reason or 'N/A'}")
    print(f" -> Acronyme Labo  : {result.extracted_acronym or 'Aucun'}")
    print(f" -> Fichier Ciblé  : {result.routed_keyword or 'Aucun (Recherche globale)'}")
    print(f" -> Raison Choix   : {result.decision_reason or 'N/A'}")
    contact_str = result.contact_info or 'Aucun contact identifié'
    print(f"\nContact(s) :\n{contact_str}")
    
    print(f"\n{'=' * 80}\n 💡 HYDE (Document Hypothétique)\n{'=' * 80}")
    print(result.hypothetical_answer)
    
    print(f"\n{'=' * 80}\n 🔄 BOUCLE AGENTIQUE (ReAct)\n{'=' * 80}")
    if result.agentic_iterations:
        for it in result.agentic_iterations:
            print(f"  [Itération {it['iteration']}]")
            if it.get('requested_file'):
                print(f"   -> Fichier requis: {it['requested_file']}")
                print(f"   -> Chunks ajoutés: {it['new_chunks_added']}")
            elif it.get('requested_keywords'):
                print(f"   -> Mots-clés requis: {it['requested_keywords']}")
                print(f"   -> Chunks ajoutés: {it['new_chunks_added']}")
            else:
                print("   -> Génération finale validée.")
    else:
        print("   Aucune itération agentique.")
    
    print(f"\n{'=' * 80}\n 📚 QDRANT (Chunks finaux)\n{'=' * 80}")
    for i, hit in enumerate(result.retrieved_chunks, start=1):
        source = hit.get("metadata", {}).get("source_file", "unknown")
        print(f"{i}. score={hit.get('score', 0):.4f} | source={source}")

def main() -> None:
    parser = argparse.ArgumentParser(description="RAG HYBRIDE Filtré (LLM chat/completions + Qdrant)")
    parser.add_argument("--question", type=str, help="Question utilisateur (mode one-shot)")
    parser.add_argument("--chat", action="store_true", help="Active le mode chatbot interactif")
    parser.add_argument("--show-debug", action="store_true", help="Affiche les logs d'exécution")
    parser.add_argument("--k", type=int, default=5, help="Nombre de chunks récupérés")
    parser.add_argument("--collection", type=str, default="pdf2_documents", help="Collection documents")
    parser.add_argument("--qdrant-path", type=str, default=str(PROJECT_ROOT / "TestExtraction" / "qdrant_data"), help="Chemin local Qdrant")
    parser.add_argument("--llm-url", type=str, default=LLM_BASE_URL, help="URL du service LLM")
    parser.add_argument("--draft-model", type=str, default="mistral-medium-latest", help="Modèle Routeur/HyDE")
    parser.add_argument("--answer-model", type=str, default="mistral-medium-latest", help="Modèle réponse finale")
    parser.add_argument("--prompt-variant", type=str, default="default")
    parser.add_argument("--context-order", type=str, default="preserve")
    parser.add_argument("--log-file", type=str, default=str(PROJECT_ROOT / "data" / "logs" / "rag_chat_logs.txt"), help="Fichier de logs")
    parser.add_argument("--output-response-json", type=str, default=None, help="Chemin pour exporter le RAGResponse complet en JSON")
    args = parser.parse_args()

    qdrant_path = Path(args.qdrant_path)
    if not qdrant_path.is_absolute():
        qdrant_path = PROJECT_ROOT / qdrant_path

    log_file_path = Path(args.log_file)
    if not log_file_path.is_absolute():
        log_file_path = PROJECT_ROOT / log_file_path

    from Utilitaire.Utbox import setup_global_logger
    setup_global_logger(log_prefix="Chat")

    # =====================================================================
    # Initialisation de la base documentaire (Qdrant)
    # =====================================================================
    logger.info("Chargement du client Qdrant (documents)...")
    try:
        base_vectorielle = BV(collection_name=args.collection, path=str(qdrant_path))
        logger.info(f"Collection principale '{args.collection}' chargée.")
    except Exception as e:
        logger.error(f"Erreur lors de l'initialisation de la base vectorielle: {e}")
        sys.exit(1)

    rag = HypotheticalRAG(
        bv_instance=base_vectorielle,
        llm_base_url=args.llm_url,
        draft_model=args.draft_model,
        answer_model=args.answer_model,
        prompt_variant=args.prompt_variant,
        context_order=args.context_order,
    )

    if args.chat or not args.question:
        logger.info("Pipeline RAG Hybride prêt. Tapez 'exit' pour quitter.")
        while True:
            try:
                question = input("\nVous: ").strip()
                if not question: continue
                if question.lower() in {"exit", "quit", "q"}: break

                result = rag.ask(question=question, k=args.k)
                log_rag_execution(result)
                
                if args.show_debug:
                    print_debug_info(result)
                    
                print(f"\nAssistant :\n{result.final_answer}\n{'-' * 80}")
            
            except KeyboardInterrupt:
                break
            except Exception as e:
                logger.error(f"Erreur lors du traitement de la question : {e}")
        return

    try:
        result = rag.ask(question=args.question, k=args.k)
        log_rag_execution(result)
        
        if args.show_debug: print_debug_info(result)
        
        if args.output_response_json:
            import json
            import dataclasses
            out_path = Path(args.output_response_json)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            with out_path.open("w", encoding="utf-8") as f:
                json.dump(dataclasses.asdict(result), f, ensure_ascii=False, indent=2)
                
        print(f"\nAssistant :\n{result.final_answer}\n{'-' * 80}")
    except Exception as e:
        logger.error(f"Erreur d'exécution : {e}")

if __name__ == "__main__":
    main()