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
│   │   ├── run_logs.txt         # Traces textuelles d'exécution
│   │   └── summary.md           # Rapport de synthèse lisible (tableaux & moyennes)
│   ├── benchmarks/              # Résultats des benchmarks comparatifs multi-modèles
│   ├── rs_pc/                   # Résultats de l'analyse RS & PC
│   └── Archive/                 # Historique des anciens tests (Mix1, etc.)
│
├── run_queries_ragilaas.py      # Script principal d'évaluation avec Juge LLM
├── run_benchmark.sh             # Benchmark automatisé multi-modèles (10 combos)
├── run_rs_pc_benchmark.py       # Évaluation Robustesse Sémantique & Ordre de Contexte
├── summarize_evaluations.py     # Générateur de rapports de synthèse Markdown
└── RS&PC.py                     # Algorithmes de calcul des métriques RS et PC
```

---

## 🚀 Commandes d'Exécution

> **Note :** Si vous lancez depuis la VM hôte, activez l'environnement avec `source /opt/ChatBotV1/.venv/bin/activate`.
> Si vous utilisez Docker, préfixez par `docker exec -it univ-chatbot`.

### 1. Évaluation par lot avec Juge LLM (Recommandé)

Lance l'évaluation complète d'un jeu de questions avec le LLM comme juge (fidélité, pertinence, précision du contexte, exhaustivité, concision) :

```bash
# Lance le test sur Query.txt (résultats automatiquement rangés dans Test/Results/YYYY-MM-DD_HH-MM_Query/)
python Test/run_queries_ragilaas.py --query-file Query.txt

# Spécifier un autre fichier de requêtes
python Test/run_queries_ragilaas.py --query-file Query_Mix.txt

# Spécifier un dossier de sortie personnalisé
python Test/run_queries_ragilaas.py --query-file Query.txt --output-dir Results/mon_test_specifique
```

Chaque exécution génère automatiquement :
- `trials.json` : les données détaillées exploitables par script
- `run_logs.txt` : les logs bruts d'inférence
- `summary.md` : le rapport Markdown avec moyennes et tableau récapitulatif

---

### 2. Benchmark Multi-Modèles (10 Combinaisons)

Compare 10 associations de modèles (Mistral, Llama 3, Gemma, Qwen) sur `Query_Mix.txt` avec un juge impartial :

```bash
chmod +x Test/run_benchmark.sh
./Test/run_benchmark.sh
```
*Les résultats sont rangés dans `Test/Results/benchmarks/<combo_name>/`.*

---

### 3. Benchmark RS & PC (Robustesse Sémantique & Permutation de Contexte)

Mesure la stabilité des réponses face aux variations de prompt et à l'ordre des documents dans le prompt :

```bash
python Test/run_rs_pc_benchmark.py --query-file Query.txt --repeat 3
```
*Les résultats sont rangés dans `Test/Results/rs_pc/`.*

---

### 4. Générer ou Mettre à Jour un Rapport Global

Pour générer un rapport de synthèse Markdown (`conclusion_evaluations.md`) basé sur tous les tests d'un dossier :

```bash
# Synthèse sur le dernier run
python Test/summarize_evaluations.py Test/Results/latest

# Synthèse globale sur tout le dossier Results
python Test/summarize_evaluations.py Test/Results
```
