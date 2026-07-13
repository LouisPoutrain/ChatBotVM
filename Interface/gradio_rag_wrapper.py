from __future__ import annotations

import sys
from pathlib import Path

import gradio as gr

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
from RAGilaas import HypotheticalRAG, setup_logging as setup_rag_logging
from RAC.RAC import setup_file_logging as setup_rac_logging

DEFAULT_COLLECTION = "pdf2_documents"
DEFAULT_QDRANT_PATH = PROJECT_ROOT / "TestExtraction" / "qdrant_data"

# Instance globale pour conserver l'état (ex: demande d'acronyme)
_rag_instance = None

def get_rag() -> HypotheticalRAG:
    global _rag_instance
    if _rag_instance is None:
        print("[INFO] Chargement des modèles RAG...")
        
        # Configuration des logs
        setup_rag_logging(PROJECT_ROOT / "data" / "logs" / "rag_chat_logs.txt")
        setup_rac_logging(PROJECT_ROOT / "RAC" / "Data" / "log" / "rag_contacts.txt")
        
        bv = BV(collection_name=DEFAULT_COLLECTION, path=str(DEFAULT_QDRANT_PATH))
        _rag_instance = HypotheticalRAG(
            bv_instance=bv,
            draft_model="mistral-medium-latest",
            answer_model="mistral-medium-latest"
        )
        print("[INFO] Modèles RAG chargés.")
    return _rag_instance

def format_sources(chunks: list[dict]) -> str:
    """Formate les sources de manière esthétique dans un bloc Markdown."""
    if not chunks:
        return ""
    
    seen = set()
    sources_md = "\n\n---\n<details>\n<summary>📚 <b>Sources consultées</b></summary>\n\n"
    
    for chunk in chunks:
        meta = chunk.get("metadata", {})
        source_name = meta.get("source_name", "Inconnu")
        if source_name not in seen:
            seen.add(source_name)
            domain = meta.get("domain_tag", "")
            domain_badge = f" `[{domain}]`" if domain else ""
            sources_md += f"- 📄 **{source_name}**{domain_badge}\n"
    
    sources_md += "\n</details>"
    return sources_md

def ask_rag(question: str, history: list[tuple[str, str]] | None = None) -> str:
    """Interroge le RAG en conservant l'état entre les messages."""
    try:
        rag = get_rag()
        result = rag.ask(question=question, k=5)
        
        # Enregistrement dans les logs
        import logging
        from RAGilaas import log_rag_execution
        log_rag_execution(logging.getLogger("RAG_History"), result)
        
        # Construction de la réponse finale
        final_response = result.final_answer
        
        # Ajout du routage expert si disponible (version courte)
        if result.contact_info:
            final_response += f"\n\n> 🧑‍💼 Contact : {result.contact_info}"
            
        return final_response
    except Exception as exc:
        return f"Erreur lors de l'exécution du RAG:\n\n{exc}"

def main() -> None:
    with gr.Blocks(theme=gr.themes.Default()) as demo:
        gr.Markdown("#ChatBot Recherche\nAssistant virtuel de la direction de la recherche.")
        
        chatbot = gr.Chatbot(height=600, show_label=False, type="messages")
        
        with gr.Row():
            msg = gr.Textbox(
                scale=8,
                show_label=False,
                placeholder="Posez votre question ici...",
                container=False
            )
            submit_btn = gr.Button("Envoyer", variant="primary", scale=1)
            
        clear = gr.ClearButton([msg, chatbot], value="Effacer")
        
        # Fonction d'enrobage pour gérer l'historique avec le format 'messages'
        def respond(message, chat_history):
            # Convertir le format dict (messages) en liste de listes attendue par ask_rag
            formatted_history = []
            if chat_history:
                for i in range(0, len(chat_history)-1, 2):
                    formatted_history.append([chat_history[i]["content"], chat_history[i+1]["content"]])
                    
            bot_message = ask_rag(message, formatted_history)
            
            chat_history.append({"role": "user", "content": message})
            chat_history.append({"role": "assistant", "content": bot_message})
            return "", chat_history

        # Déclenchements sur Entrée et sur le bouton
        msg.submit(respond, [msg, chatbot], [msg, chatbot], api_name=False)
        submit_btn.click(respond, [msg, chatbot], [msg, chatbot], api_name=False)

    try:
        demo.launch(share=True)
    except Exception as exc:
        print(f"[AVERTISSEMENT] Impossible de créer le lien public Gradio: {exc}")
        print("[INFO] L'interface reste disponible en local.")
        demo.launch()

if __name__ == "__main__":
    main()
