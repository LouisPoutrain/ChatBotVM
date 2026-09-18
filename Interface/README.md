# Interface Module

Ce module fournit les couches d'exposition et d'interaction pour le système RAG VICTORIA :

1. **Serveur FastAPI (`fastapi_rag_wrapper.py`)** : API REST asynchrone exposant l'endpoint conversationnel `/api/chat`, les endpoints d'administration `/api/admin/models`, `/api/admin/config` et la télémétrie des logs, avec ordonnanceur de synchronisation automatique (APScheduler).
2. **Interface Gradio (`gradio_rag_wrapper.py`)** : Interface interactive web pour l'évaluation humaine en temps réel et le test rapide des réponses et du routage d'experts.
3. **Composants Statiques (`static/`)** :
   - `widget.js` : Widget web embeddable léger pour intégration sur l'intranet universitaire.
   - `demo.html` : Portail de simulation et banc d'essai local.
   - `admin.html` : Console d'administration et d'audit des logs d'inférence.

## Démarrage de l'API FastAPI

```bash
uvicorn Interface.fastapi_rag_wrapper:app --host 0.0.0.0 --port 8600 --reload
```

## Démarrage de l'Interface Gradio

```bash
python Interface/gradio_rag_wrapper.py
```
