# 🧪 Benchmark Multi-Modèles RAGilaas

## Modèles disponibles

| Modèle | Taille | Famille |
|--------|--------|---------|
| `llama-3.1-8b` | 8B | Meta LLaMA |
| `mistral-small-3.2-24b` | 24B | Mistral |
| `gemma-4-31b` | 31B | Google Gemma |
| `qwen-3.6-35b-instruct` | 35B | Alibaba Qwen |
| `llama-3.3-70b` | 70B | Meta LLaMA |
| `mistral-small-4-119b` | 119B | Mistral |
| `gpt-oss-120b` | 120B | Open-source GPT |
| `mistral-medium-latest` | ~120B? | Mistral (API) |

## Juge fixe

> [!IMPORTANT]
> Le **juge d'évaluation** est fixé à `gpt-oss-120b` (le plus gros modèle disponible) pour **toutes** les combinaisons afin de garantir une comparaison équitable. Un juge constant élimine le biais inter-juge.

## 10 Combinaisons

| # | Nom | Draft Model (Routeur + HyDE) | Answer Model (Réponse) | Logique |
|---|-----|------------------------------|------------------------|---------|
| 1 | **Baseline** | `mistral-medium-latest` | `mistral-medium-latest` | Configuration actuelle de production → référence |
| 2 | **Fast Draft** | `llama-3.1-8b` | `mistral-medium-latest` | Draft ultra-rapide (8B) + réponse de référence → test si un petit modèle suffit pour HyDE |
| 3 | **Max Quality** | `mistral-small-4-119b` | `gpt-oss-120b` | Les 2 plus gros modèles → plafond de performance |
| 4 | **Meta Stack** | `llama-3.1-8b` | `llama-3.3-70b` | Écosystème Meta complet, petit→gros → cohérence intra-famille |
| 5 | **Mistral Stack** | `mistral-small-3.2-24b` | `mistral-small-4-119b` | Écosystème Mistral, scaling 24B→119B → gain marginal dans la même famille |
| 6 | **Google Mono** | `gemma-4-31b` | `gemma-4-31b` | Gemma partout → performance d'un modèle moyen homogène |
| 7 | **Qwen Mono** | `qwen-3.6-35b-instruct` | `qwen-3.6-35b-instruct` | Qwen partout → alternative non-occidentale |
| 8 | **Economy Cross** | `llama-3.1-8b` | `qwen-3.6-35b-instruct` | Le plus petit draft + modèle moyen cross-family → rapport coût/perf |
| 9 | **Premium Cross** | `gemma-4-31b` | `mistral-small-4-119b` | Draft mid-range Google + réponse Mistral géante → meilleur cross-family |
| 10 | **Big Draft** | `llama-3.3-70b` | `mistral-medium-latest` | Gros modèle en draft → test si un HyDE plus élaboré améliore la recherche |

## Axes d'analyse

Les 10 combinaisons permettent de répondre à ces questions :

1. **La taille du draft compte-t-elle ?** → Comparer #1 vs #2 vs #10 (même answer, draft différent)
2. **Quel plafond de qualité ?** → Combo #3 (Max Quality)
3. **Homogène vs cross-family ?** → #6, #7 vs #8, #9
4. **Scaling intra-famille ?** → #4 (Meta 8B→70B) et #5 (Mistral 24B→119B)
5. **Rapport coût/performance ?** → #2 et #8 (draft 8B, réponse mid-range)

## Test

- **Fichier de questions** : `Query_Mix.txt` (24 questions mixées des 8 fichiers Query)
- **Juge** : `gpt-oss-120b` pour toutes les combinaisons
- **Résultats** : Un JSON par combinaison dans `Test/results_benchmark/`
