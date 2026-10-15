"""
Module centralisé de gestion des modèles LLM et de repli automatique (Fallback).

Règle établie :
Si un modèle LLM demandé n'est pas disponible sur l'API ou rencontre une erreur d'exécution,
il est automatiquement remplacé par le 2ème modèle le plus performant (ou le plus proche disponible).
"""
from __future__ import annotations

import os
import time
from pathlib import Path
from typing import Any, Optional
import requests
from loguru import logger
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / ".env")

# ==============================================================================
# HIÉRARCHIE DE PERFORMANCE DES MODÈLES (Du plus performant au plus léger)
# ==============================================================================
PERFORMANCE_RANKING = [
    "mistral-small-4-119b",    # 1. 119B - Qualité maximale, raisonnement lourd
    "mistral-medium-latest",   # 2. ~120B - Référence production équilibrée (2ème plus performant)
    "qwen-3.6-35b-instruct",   # 3. 35B - Très haute précision sur consignes
    "gemma-4-31b",             # 4. 31B - Modèle Google équilibré
    "qwen-3.8-27b",            # 5. 27B - Raisonnement CoT (thinking)
    "llama-3.1-8b",            # 6. 8B - Ultra-rapide / économique
]

TOP_MODEL = PERFORMANCE_RANKING[0]         # "mistral-small-4-119b"
SECOND_BEST_MODEL = PERFORMANCE_RANKING[1]  # "mistral-medium-latest"

# Alias ou modèles historiques retirés -> modèle recommandé
LEGACY_ALIASES = {
    "gpt-oss-120b": "mistral-small-4-119b",
    "mistral-small-3.2-24b": "mistral-medium-latest",
    "llama-3.3-70b": "mistral-medium-latest",
}

# Cache en mémoire des modèles disponibles (durée: 60s)
_cached_available_models: list[str] = []
_cache_timestamp: float = 0.0
CACHE_TTL = 60.0  # secondes


def get_available_models(
    base_url: Optional[str] = None,
    api_key: Optional[str] = None,
    force_refresh: bool = False
) -> list[str]:
    """
    Récupère la liste des modèles disponibles sur l'API (/models) avec cache de 60s.
    """
    global _cached_available_models, _cache_timestamp
    now = time.time()
    if not force_refresh and _cached_available_models and (now - _cache_timestamp) < CACHE_TTL:
        return _cached_available_models

    base_url = (base_url or os.getenv("LLM_BASE_URL", "https://llm.ilaas.fr/v1")).rstrip("/")
    api_key = api_key or os.getenv("LLM_API_KEY", "")

    if not api_key:
        return PERFORMANCE_RANKING.copy()

    try:
        resp = requests.get(
            f"{base_url}/models",
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=8
        )
        if resp.ok:
            data = resp.json()
            models = [m.get("id") for m in data.get("data", []) if m.get("id")]
            if models:
                _cached_available_models = models
                _cache_timestamp = now
                return models
    except Exception as e:
        logger.warning(f"Impossible de joindre /models ({e}), utilisation de la hiérarchie par défaut.")

    return _cached_available_models or PERFORMANCE_RANKING.copy()


def get_fallback_candidates(requested_model: str, available_models: list[str]) -> list[str]:
    """
    Renvoie la liste des candidats de repli ordonnés selon la règle :
    - Si le modèle demandé était le 1er (mistral-small-4-119b), le repli est le 2ème (mistral-medium-latest).
    - Si le modèle demandé était le 2ème (mistral-medium-latest), le repli est le 1er ou le 3ème.
    - Pour tout autre modèle indisponible (ex: modèle retiré ou en panne),
      on prend en priorité le 2ème plus performant (mistral-medium-latest), puis le 1er, etc.
    """
    requested_model = (requested_model or "").strip()
    norm_req = LEGACY_ALIASES.get(requested_model, requested_model)
    candidates: list[str] = []

    if norm_req == TOP_MODEL:
        priorities = [SECOND_BEST_MODEL] + [m for m in PERFORMANCE_RANKING if m not in (SECOND_BEST_MODEL, TOP_MODEL)]
    elif norm_req == SECOND_BEST_MODEL:
        priorities = [TOP_MODEL] + [m for m in PERFORMANCE_RANKING if m not in (TOP_MODEL, SECOND_BEST_MODEL)]
    else:
        # Règle utilisateur : "on le remplace par le 2eme plus performant"
        priorities = [SECOND_BEST_MODEL, TOP_MODEL] + [m for m in PERFORMANCE_RANKING if m not in (SECOND_BEST_MODEL, TOP_MODEL)]

    for model in priorities:
        if model in available_models and model != requested_model and model not in candidates:
            candidates.append(model)

    for model in available_models:
        if model not in candidates and model != requested_model:
            candidates.append(model)

    # Filet de sécurité si la liste des disponibles était vide
    if not candidates:
        candidates = [m for m in priorities if m != requested_model]

    return candidates


def resolve_model_with_fallback(
    requested_model: str,
    base_url: Optional[str] = None,
    api_key: Optional[str] = None,
    available_models: Optional[list[str]] = None
) -> str:
    """
    Vérifie si le modèle demandé est disponible.
    S'il ne l'est pas, sélectionne et retourne le modèle de repli le plus performant.
    """
    requested_model = (requested_model or "").strip()
    if not requested_model:
        return SECOND_BEST_MODEL

    if available_models is None:
        available_models = get_available_models(base_url, api_key)

    if requested_model in available_models:
        return requested_model

    candidates = get_fallback_candidates(requested_model, available_models)
    if candidates:
        fallback = candidates[0]
        logger.warning(
            f"[FALLBACK MODEL] Le modèle demandé '{requested_model}' n'est pas disponible sur l'API. "
            f"Remplacement automatique par le modèle de repli '{fallback}' (2ème plus performant)."
        )
        return fallback

    return requested_model


def call_llm_with_fallback(
    base_url: str,
    headers: dict[str, str],
    payload: dict[str, Any],
    timeout: int = 300,
    max_retries: int = 2
) -> requests.Response:
    """
    Exécute un appel /chat/completions avec détection d'erreur et bascule automatique
    vers le modèle de repli si le modèle demandé échoue (404, 500, 502, 503, 504, Unknown model, etc.).
    """
    current_model = payload.get("model", SECOND_BEST_MODEL)
    tried_models = [current_model]
    last_resp: Optional[requests.Response] = None

    for attempt in range(max_retries + 1):
        try:
            resp = requests.post(
                f"{base_url.rstrip('/')}/chat/completions",
                headers=headers,
                json=payload,
                timeout=timeout,
            )
            last_resp = resp

            if not resp.ok:
                err_text = resp.text.lower()

                # Cas spécifique : le modèle ne supporte pas response_format json_object
                if resp.status_code == 400 and ("response_format" in err_text or "json_object" in err_text):
                    if "response_format" in payload:
                        logger.warning(
                            f"[FORMAT RETRY] '{current_model}' ne supporte pas response_format=json_object. "
                            f"Réessai sans ce paramètre..."
                        )
                        payload.pop("response_format", None)
                        continue

                # Détecter si l'erreur est liée au modèle ou à une panne serveur/surcharge
                is_model_error = (
                    resp.status_code in (404, 500, 502, 503, 504)
                    or "unknown model" in err_text
                    or "model not found" in err_text
                    or "does not exist" in err_text
                    or "model_not_found" in err_text
                )
                if is_model_error and attempt < max_retries:
                    avail = get_available_models(base_url, force_refresh=True)
                    candidates = get_fallback_candidates(current_model, avail)
                    fallback = next((c for c in candidates if c not in tried_models), None)
                    if fallback:
                        logger.warning(
                            f"[FALLBACK RUNTIME] Échec de l'appel avec '{current_model}' (Code {resp.status_code}). "
                            f"Bascule immédiate sur le modèle de repli '{fallback}'."
                        )
                        current_model = fallback
                        payload["model"] = current_model
                        tried_models.append(current_model)
                        continue

            return resp

        except requests.RequestException as e:
            if attempt < max_retries:
                avail = get_available_models(base_url, force_refresh=True)
                candidates = get_fallback_candidates(current_model, avail)
                fallback = next((c for c in candidates if c not in tried_models), None)
                if fallback:
                    logger.warning(
                        f"[FALLBACK EXCEPTION] Erreur réseau avec '{current_model}': {e}. "
                        f"Nouvel essai avec '{fallback}'."
                    )
                    current_model = fallback
                    payload["model"] = current_model
                    tried_models.append(current_model)
                    continue
            raise

    return last_resp if last_resp is not None else resp

