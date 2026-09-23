# Suite de Tests et Benchmarks VICTORIA

Ce répertoire regroupe l'ensemble des jeux de questions, scripts d'évaluation et résultats d'expérimentation du pipeline RAG VICTORIA.

---

## 📁 Organisation des Dossiers

```
Test/
├── Queries/                     # Tous les fichiers de questions sources
│   ├── Query.txt                # Corpus principal de test (22 questions)
│   ├── Query2.txt ... Query8.txt# Variantes et sous-ensembles thématiques
│   └── Query_Mix.txt            # Corpus mixte pour benchmarks comparatifs
│
├── Results/                     # Centralisation de TOUTES les sorties de tests
│   ├── latest                   # Raccourci symbolique vers la dernière exécution
│   ├── 2026-09-23_Query/        # Exemple d'exécution datée
│   │   ├── trials.json          # Données brutes structurées (notes, tokens, réponses)
│   │   ├── run_logs.txt         # Traces textuelles d'inférence
│   │   └── summary.md           # Rapport de synthèse lisible (tableaux & moyennes)
│   ├── YYYY-MM-DD_HH-MM_benchmark_Query_Mix/ # Benchmark multi-modèles (10 combos)
│   │   ├── 01_baseline/         # Dossier par combinaison
│   │   ├── 02_fast_draft/
│   │   └── conclusion_evaluations.md # Synthèse comparative globale automatique
│   └── Archive/                 # Historique des anciens tests (Mix1, etc.)
│
├── run_queries_ragilaas.py      # Script principal d'évaluation avec Juge LLM
├── run_benchmark.py             # Benchmark multi-modèles (10 combinaisons, LLM Judge)
├── run_benchmark.sh             # Lanceur Shell équivalent pour run_benchmark.py
├── run_queries_models.py        # Comparaison de modèles avec découverte API dynamique
├── run_rs_pc_benchmark.py       # Évaluation Robustesse Sémantique & Ordre de Contexte
├── summarize_evaluations.py     # Générateur de rapports de synthèse Markdown
└── RS&PC.py                     # Algorithmes de calcul des métriques RS et PC
```

---

## 🚀 Commandes d'Exécution sur la VM (Docker)

> **Important :** Sur la VM, toutes les dépendances et clés API sont configurées dans le conteneur Docker `univ-chatbot`.
> Il suffit donc de préfixer vos commandes par `docker exec -it univ-chatbot`.

---

### 1. Benchmark Multi-Modèles (10 Combinaisons avec Juge LLM)

Ce script teste les **10 combinaisons architecturales** définies dans `BenchComb.md` (Mistral, LLaMA, Gemma, Qwen) et utilise un **Juge impartial fixe** (`gpt-oss-120b`) pour évaluer fidélité, pertinence et précision du contexte. À la fin, il génère automatiquement le rapport comparatif global `conclusion_evaluations.md`.

```bash
# 🎯 Lancer le benchmark complet (10 combos sur Query_Mix.txt)
docker exec -it univ-chatbot python Test/run_benchmark.py

# ⚡ Test rapide : limiter à 2 questions par modèle pour valider le bon fonctionnement
docker exec -it univ-chatbot python Test/run_benchmark.py --max-questions 2

# 🔍 Tester uniquement des combinaisons spécifiques (ex: baseline et fast draft)
docker exec -it univ-chatbot python Test/run_benchmark.py --combos 1 2

# 📄 Utiliser un autre jeu de questions
docker exec -it univ-chatbot python Test/run_benchmark.py --query-file Query.txt
```

---

### 2. Comparaison Directe des Modèles de l'API (Sans Juge)

Ce script interroge dynamiquement l'API LLM (`/v1/models`), filtre les modèles disponibles et compare leurs réponses et temps de génération :

```bash
# 🔍 Découverte automatique et comparaison sur Query.txt
docker exec -it univ-chatbot python Test/run_queries_models.py --query-file Query.txt

# ⚡ Comparer 2 modèles précis sur 3 questions
docker exec -it univ-chatbot python Test/run_queries_models.py --models mistral-medium-latest,gemma-4-31b --max-questions 3

# 🧪 Mode simulation (dry-run)
docker exec -it univ-chatbot python Test/run_queries_models.py --dry-run
```
*Génère un tableau comparatif et un comparatif question par question dans `Test/Results/YYYY-MM-DD_HH-MM_models_<query>/summary.md`.*

---

### 3. Évaluation par lot d'un modèle unique avec Juge LLM

Lance l'évaluation complète d'un jeu de questions avec le modèle par défaut ou spécifié :

```bash
# Lance le test standard sur Query.txt
docker exec -it univ-chatbot python Test/run_queries_ragilaas.py --query-file Query.txt

# Tester sur 5 questions seulement
docker exec -it univ-chatbot python Test/run_queries_ragilaas.py --query-file Query.txt --max-questions 5
```

---

### 4. Générer ou Mettre à Jour un Rapport Global de Synthèse

Pour recalculer ou regénérer un rapport de synthèse Markdown (`conclusion_evaluations.md`) basé sur tous les tests d'un dossier :

```bash
# Synthèse sur le dernier run
docker exec -it univ-chatbot python Test/summarize_evaluations.py Test/Results/latest

# Synthèse globale sur tout le dossier Results
docker exec -it univ-chatbot python Test/summarize_evaluations.py Test/Results
```
