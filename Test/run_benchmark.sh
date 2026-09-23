#!/bin/bash
# =============================================================================
# Benchmark Multi-Modèles RAGilaas
# Lance 10 combinaisons de modèles sur Query_Mix.txt
# Juge fixe : gpt-oss-120b
# =============================================================================

set -e

export PYTHONIOENCODING=utf-8
export PYTHONUTF8=1

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
PYTHON="$PROJECT_DIR/.venv/bin/python"
RUNNER="$SCRIPT_DIR/run_queries_ragilaas.py"
QUERY_FILE="Query_Mix.txt"
JUDGE="gpt-oss-120b"
OUTPUT_DIR="$SCRIPT_DIR/Results/benchmarks"

mkdir -p "$OUTPUT_DIR"

echo "============================================================"
echo "  BENCHMARK MULTI-MODÈLES RAGilaas"
echo "  Query: $QUERY_FILE (24 questions)"
echo "  Juge: $JUDGE"
echo "  Résultats: $OUTPUT_DIR/"
echo "============================================================"
echo ""

# Définition des 10 combinaisons : NOM|DRAFT|ANSWER
COMBOS=(
  "01_baseline|mistral-medium-latest|mistral-medium-latest"
  "02_fast_draft|llama-3.1-8b|mistral-medium-latest"
  "03_max_quality|mistral-small-4-119b|gpt-oss-120b"
  "04_meta_stack|llama-3.1-8b|llama-3.3-70b"
  "05_mistral_stack|mistral-small-3.2-24b|mistral-small-4-119b"
  "06_google_mono|gemma-4-31b|gemma-4-31b"
  "07_qwen_mono|qwen-3.6-35b-instruct|qwen-3.6-35b-instruct"
  "08_economy_cross|llama-3.1-8b|qwen-3.6-35b-instruct"
  "09_premium_cross|gemma-4-31b|mistral-small-4-119b"
  "10_big_draft|llama-3.3-70b|mistral-medium-latest"
)

TOTAL=${#COMBOS[@]}
START_TIME=$(date +%s)

for i in "${!COMBOS[@]}"; do
  IFS='|' read -r NAME DRAFT ANSWER <<< "${COMBOS[$i]}"
  NUM=$((i + 1))

  echo ""
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "  [$NUM/$TOTAL] $NAME"
  echo "  Draft: $DRAFT | Answer: $ANSWER | Judge: $JUDGE"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo ""

  COMBO_START=$(date +%s)

  "$PYTHON" "$RUNNER" \
    --query-file "$QUERY_FILE" \
    --draft-model "$DRAFT" \
    --answer-model "$ANSWER" \
    --judge-model "$JUDGE" \
    --output-dir "$OUTPUT_DIR/${NAME}" \
    --timeout 600

  COMBO_END=$(date +%s)
  COMBO_DURATION=$((COMBO_END - COMBO_START))
  echo ""
  echo "  ✅ $NAME terminé en ${COMBO_DURATION}s"
done

END_TIME=$(date +%s)
TOTAL_DURATION=$((END_TIME - START_TIME))
MINUTES=$((TOTAL_DURATION / 60))
SECONDS=$((TOTAL_DURATION % 60))

echo ""
echo "============================================================"
echo "  BENCHMARK TERMINÉ"
echo "  Durée totale: ${MINUTES}m ${SECONDS}s"
echo "  Résultats dans: $OUTPUT_DIR/"
echo "============================================================"
