#!/bin/bash
# =============================================================================
# Benchmark Multi-Modèles RAGilaas (10 Combinaisons)
# Lance les 10 combinaisons de modèles définies dans BenchComb.md
# Juge impartial : gpt-oss-120b
# =============================================================================

set -e

export PYTHONIOENCODING=utf-8
export PYTHONUTF8=1

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Détection de l'interpréteur Python (environnement virtuel hôte ou Python conteneur)
if [ -n "$PYTHON_EXEC" ]; then
    PYTHON="$PYTHON_EXEC"
elif [ -f "$PROJECT_DIR/.venv/bin/python" ]; then
    PYTHON="$PROJECT_DIR/.venv/bin/python"
elif command -v python3 >/dev/null 2>&1; then
    PYTHON="$(command -v python3)"
else
    PYTHON="$(command -v python)"
fi

# Exécution via le script Python unifié (gère les arguments, les dossiers datés et le rapport)
exec "$PYTHON" "$SCRIPT_DIR/run_benchmark.py" "$@"
