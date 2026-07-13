# RAG Interface

This folder contains lightweight wrappers around the local RAG CLI.

## Run the Gradio chat wrapper

```bash
python RAG/Interface/gradio_rag_wrapper.py
```

The script launches a temporary public Gradio link with `share=True`.

## Adaptation points

- Update `RAG_SCRIPT` in `gradio_rag_wrapper.py` if your CLI entrypoint changes.
- Update `BASE_COMMAND` if your RAG script needs extra CLI arguments.
