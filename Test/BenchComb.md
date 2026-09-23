# 🧪 Benchmark Multi-Modèles RAGilaas (Mis à jour 2026)

## Modèles Actuellement Disponibles sur l'API

| Modèle | Taille | Famille | Statut |
|--------|--------|---------|--------|
| `llama-3.1-8b` | 8B | Meta LLaMA | Actif |
| `mistral-small-3.2-24b` | 24B | Mistral | Actif |
| `gemma-4-31b` | 31B | Google Gemma | Actif |
| `qwen-3.6-35b-instruct` | 35B | Alibaba Qwen | Actif |
| `mistral-small-4-119b` | 119B | Mistral | Actif |
| `gpt-oss-120b` | 120B | Open-source GPT | Actif (Juge impartial) |
| `mistral-medium-latest` | ~120B | Mistral (API) | Actif (Baseline Prod) |

> ℹ️ *Note : `llama-3.3-70b` n'est plus fourni par l'API et a été retiré des combinaisons de test.*

---

## Juge Fixe

> [!IMPORTANT]
> Le **juge d'évaluation** est fixé à `gpt-oss-120b` (le plus gros modèle ouvert disponible) pour **toutes** les combinaisons afin de garantir une comparaison équitable et éliminer tout biais inter-juge.

---

## 10 Combinaisons Définies

| # | Nom | Draft Model (Routeur + HyDE) | Answer Model (Réponse) | Logique Expérimentale |
|---|-----|------------------------------|------------------------|-----------------------|
| 1 | **01_baseline** | `mistral-medium-latest` | `mistral-medium-latest` | Configuration actuelle en production → référence |
| 2 | **02_fast_draft** | `llama-3.1-8b` | `mistral-medium-latest` | Draft ultra-léger (8B) + réponse référence → test HyDE minimal |
| 3 | **03_max_quality** | `mistral-small-4-119b` | `gpt-oss-120b` | Les 2 plus gros modèles (119B + 120B) → plafond absolu de performance |
| 4 | **04_meta_mono** | `llama-3.1-8b` | `llama-3.1-8b` | 100% Meta 8B de bout en bout → performance d'un modèle compact ultra-rapide |
| 5 | **05_mistral_stack** | `mistral-small-3.2-24b` | `mistral-small-4-119b` | Écosystème Mistral complet (24B draft → 119B réponse) |
| 6 | **06_google_mono** | `gemma-4-31b` | `gemma-4-31b` | Gemma 31B homogène → modèle mid-range équilibré |
| 7 | **07_qwen_mono** | `qwen-3.6-35b-instruct` | `qwen-3.6-35b-instruct` | Qwen 35B homogène → performance de la famille Alibaba |
| 8 | **08_economy_cross** | `llama-3.1-8b` | `qwen-3.6-35b-instruct` | Plus petit draft (8B) + réponse moyenne (35B) → rapport coût/efficacité |
| 9 | **09_premium_cross** | `gemma-4-31b` | `mistral-small-4-119b` | Draft mid-range Google (31B) + réponse Mistral géante (119B) |
| 10 | **10_mid_draft** | `mistral-small-3.2-24b` | `mistral-medium-latest` | Draft intermédiaire (24B) + réponse référence → échelle progressive de draft |

---

## 🔬 Axes d'Analyse Scientifique

Les 10 combinaisons permettent de répondre précisément à 5 questions :

1. **La taille du modèle de draft compte-t-elle ?**  
   Comparer **#1** (Draft Medium) vs **#2** (Fast Draft 8B) vs **#10** (Mid Draft 24B) avec le **même modèle de réponse** (`mistral-medium-latest`).
2. **Quel est le plafond de qualité atteignable ?**  
   Combo **#3** (*Max Quality* 119B + 120B).
3. **Modèles homogènes par échelle de taille :**  
   **#4** (8B Meta) vs **#6** (31B Gemma) vs **#7** (35B Qwen) vs **#1** (Medium Mistral).
4. **Gain du scaling intra-famille ?**  
   **#5** (*Mistral Stack* 24B → 119B) vs **#1** (*Baseline*).
5. **Rapport performance / coût (Cross-family) :**  
   **#8** (Draft 8B + Réponse 35B) et **#9** (Draft 31B + Réponse 119B).
