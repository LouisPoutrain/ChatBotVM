# =============================================================================
# Benchmark Multi-Modèles RAGilaas (Version Windows)
# Lance 10 combinaisons de modèles sur Query_Mix.txt
# Juge fixe : gpt-oss-120b
# =============================================================================

$ErrorActionPreference = "Stop"

# Forcer l'encodage UTF-8 pour Python (équivalent des 'export' Bash)
$env:PYTHONIOENCODING = "utf-8"
$env:PYTHONUTF8 = "1"

# Forcer l'affichage de la console PowerShell en UTF-8 pour les caractères spéciaux
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# Définition des chemins (PSScriptRoot donne le dossier du script actuel)
$SCRIPT_DIR = $PSScriptRoot
$PROJECT_DIR = Split-Path -Parent $SCRIPT_DIR

# ATTENTION: Sous Windows, les environnements virtuels utilisent \Scripts\python.exe
$PYTHON = Join-Path $PROJECT_DIR ".venv\Scripts\python.exe"
$RUNNER = Join-Path $SCRIPT_DIR "run_queries_ragilaas.py"
$QUERY_FILE = "Query_Mix.txt"
$JUDGE = "gpt-oss-120b"
$OUTPUT_DIR = Join-Path $SCRIPT_DIR "results_benchmark"

# Créer le dossier s'il n'existe pas
New-Item -ItemType Directory -Force -Path $OUTPUT_DIR | Out-Null

Write-Host "============================================================"
Write-Host "  BENCHMARK MULTI-MODÈLES RAGilaas"
Write-Host "  Query: $QUERY_FILE (24 questions)"
Write-Host "  Juge: $JUDGE"
Write-Host "  Résultats: $OUTPUT_DIR\"
Write-Host "============================================================"
Write-Host ""

# Définition des 10 combinaisons : NOM|DRAFT|ANSWER
$COMBOS = @(
  "01_baseline|mistral-medium-latest|mistral-medium-latest",
  "02_fast_draft|llama-3.1-8b|mistral-medium-latest",
  "03_max_quality|mistral-small-4-119b|gpt-oss-120b",
  "04_meta_stack|llama-3.1-8b|llama-3.3-70b",
  "05_mistral_stack|mistral-small-3.2-24b|mistral-small-4-119b",
  "06_google_mono|gemma-4-31b|gemma-4-31b",
  "07_qwen_mono|qwen-3.6-35b-instruct|qwen-3.6-35b-instruct",
  "08_economy_cross|llama-3.1-8b|qwen-3.6-35b-instruct",
  "09_premium_cross|gemma-4-31b|mistral-small-4-119b",
  "10_big_draft|llama-3.3-70b|mistral-medium-latest"
)

$TOTAL = $COMBOS.Length
$START_TIME = Get-Date

for ($i = 0; $i -lt $TOTAL; $i++) {
    # Séparer les variables
    $parts = $COMBOS[$i].Split('|')
    $NAME = $parts[0]
    $DRAFT = $parts[1]
    $ANSWER = $parts[2]
    $NUM = $i + 1

    Write-Host ""
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    Write-Host "  [$NUM/$TOTAL] $NAME"
    Write-Host "  Draft: $DRAFT | Answer: $ANSWER | Judge: $JUDGE"
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    Write-Host ""

    $COMBO_START = Get-Date

    $maxRetries = 10
    $retryCount = 0
    $success = $false

    while (-not $success -and $retryCount -lt $maxRetries) {
        if ($retryCount -gt 0) {
            Write-Host "  ⚠️ Échec détecté. Attente de 10s avant la tentative ($retryCount/$maxRetries)..." -ForegroundColor Yellow
            Start-Sleep -Seconds 10
        }
        
        try {
            # Lancement du script Python
            & $PYTHON $RUNNER `
              --query-file $QUERY_FILE `
              --draft-model $DRAFT `
              --answer-model $ANSWER `
              --judge-model $JUDGE `
              --output-log "$OUTPUT_DIR\${NAME}_log.txt" `
              --output-json "$OUTPUT_DIR\${NAME}_trials.json" `
              --timeout 600

            if ($LASTEXITCODE -eq 0) {
                $success = $true
            } else {
                $retryCount++
            }
        } catch {
            Write-Host "  ⚠️ Erreur inattendue: $_" -ForegroundColor Yellow
            $retryCount++
        }
    }

    $COMBO_END = Get-Date
    $COMBO_DURATION = [math]::Round(($COMBO_END - $COMBO_START).TotalSeconds)
    Write-Host ""
    if ($success) {
        Write-Host "  ✅ $NAME terminé en ${COMBO_DURATION}s"
    } else {
        Write-Host "  ❌ $NAME a échoué définitivement après $maxRetries tentatives (Durée: ${COMBO_DURATION}s)" -ForegroundColor Red
    }
}

$END_TIME = Get-Date
$TOTAL_DURATION = ($END_TIME - $START_TIME)
$MINUTES = [math]::Floor($TOTAL_DURATION.TotalMinutes)
$SECONDS = $TOTAL_DURATION.Seconds

Write-Host ""
Write-Host "============================================================"
Write-Host "  BENCHMARK TERMINÉ"
Write-Host "  Durée totale: ${MINUTES}m ${SECONDS}s"
Write-Host "  Résultats dans: $OUTPUT_DIR\"
Write-Host "============================================================"