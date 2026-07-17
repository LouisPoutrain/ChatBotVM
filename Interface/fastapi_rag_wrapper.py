from __future__ import annotations

import sys
from pathlib import Path
import logging
import os
import json
import requests
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from typing import Optional
from pydantic import BaseModel
import uvicorn
import subprocess
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

# Configuration des chemins
PROJECT_ROOT = Path(__file__).resolve().parents[1]
BV_DIR = PROJECT_ROOT / "BV"
RAGILAAS_DIR = PROJECT_ROOT / "RAGilaas"

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
if str(BV_DIR) not in sys.path:
    sys.path.insert(0, str(BV_DIR))
if str(RAGILAAS_DIR) not in sys.path:
    sys.path.insert(0, str(RAGILAAS_DIR))

from BV import BV
from RAGilaas import HypotheticalRAG, log_rag_execution
from loguru import logger

DEFAULT_COLLECTION = "pdf2_documents"
DEFAULT_QDRANT_PATH = PROJECT_ROOT / "TestExtraction" / "qdrant_data"
CONFIG_PATH = PROJECT_ROOT / "Interface" / "config.json"

# Modèles Pydantic pour structurer les requêtes et réponses de l'API
class ModelConfig(BaseModel):
    draft_model: str
    answer_model: str
    rac_model: str = "mistral-medium-latest"

def get_config() -> ModelConfig:
    if CONFIG_PATH.exists():
        try:
            with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                if "rac_model" not in data:
                    data["rac_model"] = "mistral-medium-latest"
                return ModelConfig(**data)
        except Exception as e:
            logger.error(f"Erreur lors de la lecture de {CONFIG_PATH}: {e}")
    return ModelConfig(draft_model="mistral-medium-latest", answer_model="mistral-medium-latest", rac_model="mistral-medium-latest")

def save_config(config: ModelConfig):
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(config.dict(), f, indent=4)

def get_available_models():
    api_key = os.getenv("LLM_API_KEY")
    base_url = os.getenv("LLM_BASE_URL")
    if not api_key or not base_url:
        return []
    try:
        response = requests.get(f"{base_url}/models", headers={"Authorization": f"Bearer {api_key}"}, timeout=5)
        response.raise_for_status()
        data = response.json()
        return [model["id"] for model in data.get("data", [])]
    except Exception as e:
        logger.error(f"Erreur récupération modèles depuis {base_url}: {e}")
        return []

# Modèles Pydantic pour la discussion
class ChatRequest(BaseModel):
    """
    Modèle de requête pour l'endpoint de chat.
    
    Attributes:
        question (str): La question de l'utilisateur.
        history (list[list[str]]): L'historique de la conversation (optionnel).
        session_id (str): Identifiant unique de la session pour la gestion du RAG stateless.
    """
    question: str
    history: list[list[str]] = []  # Historique optionnel pour le futur
    session_id: str = "default"

class ChatResponse(BaseModel):
    """
    Modèle de réponse pour l'endpoint de chat.
    
    Attributes:
        response (str): La réponse générée par l'IA.
        contact_info (Optional[str]): Les informations du contact expert, s'il y en a un.
    """
    response: str
    contact_info: Optional[str] = None

# Configuration du logger pour enregistrer dans Log/YYYY-MM/YYYY-MM-DD.log
logger.add(
    PROJECT_ROOT / "Log" / "{time:YYYY-MM}" / "{time:YYYY-MM-DD}.log",
    rotation="1 day",
    enqueue=True,
    catch=True,
    format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} - {message}"
)

# Initialisation de l'application FastAPI
app = FastAPI(
    title="ChatBot Université API",
    description="API RAG pour le widget web du chatbot de l'université",
    version="1.0.0"
)

# Servir les fichiers statiques (le widget JS et la page de démo)
static_dir = PROJECT_ROOT / "Interface" / "static"
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

# Configuration CORS : CRUCIAL pour autoriser le widget (qui sera sur un autre domaine) à appeler l'API
app.add_middleware(
    CORSMiddleware,
        allow_origins=[
        "https://utnet.univ-tours.fr",
        "https://www.univ-tours.fr",  # Au cas où
        "http://localhost:8600",
        "http://127.0.0.1:8600"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Instance globale pour conserver l'état et éviter de recharger le modèle
_rag_instance = None

def get_rag() -> HypotheticalRAG:
    """
    Instancie ou récupère l'instance globale du modèle RAG.
    
    Returns:
        HypotheticalRAG: L'instance du modèle prête à répondre aux requêtes.
    """
    global _rag_instance
    if _rag_instance is None:
        print("[INFO] Chargement des modèles RAG pour l'API...")
        
        config = get_config()
        bv = BV(collection_name=DEFAULT_COLLECTION, path=str(DEFAULT_QDRANT_PATH))
        _rag_instance = HypotheticalRAG(
            bv_instance=bv,
            draft_model=config.draft_model,
            answer_model=config.answer_model,
            rac_model=config.rac_model
        )
        print("[INFO] Modèles RAG chargés avec succès.")
    return _rag_instance

def run_auto_update():
    logger.info("Démarrage de la mise à jour automatique programmée...")
    script_path = PROJECT_ROOT / "Utilitaire" / "auto_update_pipeline.py"
    try:
        # Run in a subprocess to avoid blocking the asyncio event loop
        subprocess.run([sys.executable, str(script_path)], check=True)
        logger.info("Mise à jour automatique terminée avec succès.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Échec de la mise à jour automatique : {e}")

@app.on_event("startup")
async def startup_event():
    """
    Pré-charge les modèles RAG au démarrage du serveur FastAPI.
    Cela évite un temps d'attente prolongé lors de la première requête utilisateur.
    Initialise également le planificateur pour la mise à jour automatique.
    """
    get_rag()
    
    scheduler = BackgroundScheduler()
    # Tous les dimanches à 3h du matin
    scheduler.add_job(run_auto_update, CronTrigger(day_of_week='sun', hour=3, minute=0))
    scheduler.start()
    logger.info("Planificateur démarré: mise à jour auto programmée le dimanche à 03:00.")

@app.post("/api/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Endpoint principal pour interagir avec le ChatBot.
    
    Args:
        request (ChatRequest): La requête contenant la question et l'ID de session.
        
    Returns:
        ChatResponse: La réponse générée par l'IA et les informations de contact.
        
    Raises:
        HTTPException: Si une erreur survient pendant l'exécution du RAG.
    """
    try:
        rag = get_rag()
        
        # Appel à votre RAG
        result = rag.ask(question=request.question, session_id=request.session_id, k=5)
        
        # Enregistrement dans les logs existants
        log_rag_execution(result)
        
        final_response = result.final_answer
        
        # Injection du contact expert dans la réponse texte (comme dans Gradio)
        if result.contact_info:
            final_response += f"\n\n> 🧑‍💼 Contact : {result.contact_info}"
            
        return ChatResponse(
            response=final_response,
            contact_info=result.contact_info
        )
    except Exception as e:
        logger.exception("Erreur inattendue dans chat_endpoint")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/admin/models")
async def fetch_models():
    """Récupère la liste des modèles LLM disponibles depuis l'API externe."""
    models = get_available_models()
    return {"models": models}

@app.get("/api/admin/config")
async def get_current_config():
    """Renvoie la configuration actuelle des modèles."""
    return get_config()

@app.post("/api/admin/config")
async def update_config(config: ModelConfig):
    """Met à jour la configuration des modèles et force le rechargement du RAG."""
    global _rag_instance
    save_config(config)
    _rag_instance = None  # Force le rechargement à la prochaine requête
    logger.info(f"Configuration mise à jour: {config}")
    return {"status": "success", "message": "Configuration mise à jour avec succès"}

@app.get("/api/admin/logs")
async def get_logs(log_type: str = "main", date: str = None):
    """
    Renvoie le contenu du fichier de log pour une date donnée (aujourd'hui par défaut).
    """
    import datetime
    
    if date:
        try:
            target_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            target_date = datetime.datetime.now()
    else:
        target_date = datetime.datetime.now()
        
    year_month = target_date.strftime("%Y-%m")
    day_str = target_date.strftime("%Y-%m-%d")
    
    if log_type == "update":
        log_file = PROJECT_ROOT / "Log" / year_month / f"{day_str}_Update.log"
    else:
        log_file = PROJECT_ROOT / "Log" / year_month / f"{day_str}.log"
    
    if not log_file.exists():
        return {"logs": f"Aucun log pour le {day_str} ({log_type})."}
    
    # Lecture des 1000 dernières lignes pour éviter de saturer la mémoire
    with open(log_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return {"logs": "".join(lines[-1000:])}

if __name__ == "__main__":
    print("[INFO] Démarrage du serveur API sur http://0.0.0.0:8600")
    # uvicorn lance le serveur. L'option reload=True permet de recharger automatiquement si on modifie le code.
    uvicorn.run("fastapi_rag_wrapper:app", host="0.0.0.0", port=8600, reload=True)
