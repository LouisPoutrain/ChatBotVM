# 🧪 Benchmark Multi-Modèles RAGilaas (Mis à jour 2026)

## Modèles Actuellement Disponibles sur l'API

| Modèle | Taille | Famille | Type | Statut |
|--------|--------|---------|------|--------|
| `llama-3.1-8b` | 8B | Meta LLaMA | Instruct dense | Actif |
| `qwen-3.8-27b` | 27B | Alibaba Qwen | Reasoning / Thinking | Actif |
| `gemma-4-31b` | 31B | Google Gemma | Instruct dense | Actif |
| `qwen-3.6-35b-instruct` | 35B | Alibaba Qwen | Instruct dense | Actif |
| `mistral-small-4-119b` | 119B | Mistral | Instruct lourd | Actif |
| `gpt-oss-120b` | 120B | Open-source GPT | Généraliste lourd | Actif (Juge impartial) |
| `mistral-medium-latest` | ~120B | Mistral (API) | Équilibré / Prod | Actif (Baseline Prod) |

> ℹ️ *Note : `mistral-small-3.2-24b` et `llama-3.3-70b` ne sont plus fournis par l'API et ont été retirés des combinaisons.*

---

## Juge Fixe

> [!IMPORTANT]
> Le **juge d'évaluation** est fixé à `gpt-oss-120b` (le plus gros modèle ouvert disponible) pour **toutes** les combinaisons afin de garantir une comparaison équitable et éliminer tout biais inter-juge.

---

## 10 Combinaisons Définies

| # | Nom | Draft Model (Routeur + HyDE) | Answer Model (Réponse) | Logique Expérimentale |
|---|-----|------------------------------|------------------------|-----------------------|
| 1 | **01_baseline** | `mistral-medium-latest` | `mistral-medium-latest` | Configuration de référence en production (Mistral Medium homogène) |
| 2 | **02_fast_draft** | `llama-3.1-8b` | `mistral-medium-latest` | Draft ultra-léger 8B + réponse de référence → test HyDE minimal et rapide |
| 3 | **03_max_quality** | `mistral-small-4-119b` | `gpt-oss-120b` | Les deux modèles les plus massifs (119B + 120B) → plafond absolu de performance |
| 4 | **04_meta_mono** | `llama-3.1-8b` | `llama-3.1-8b` | 100% Meta 8B de bout en bout → performance d'un modèle compact ultra-rapide |
| 5 | **05_qwen_reasoning_mono** | `qwen-3.8-27b` | `qwen-3.8-27b` | 100% Qwen 27B avec capacités de réflexion (*thinking*) de bout en bout |
| 6 | **06_google_mono** | `gemma-4-31b` | `gemma-4-31b` | Google Gemma 31B homogène → modèle intermédiaire équilibré |
| 7 | **07_qwen_instruct_mono** | `qwen-3.6-35b-instruct` | `qwen-3.6-35b-instruct` | Alibaba Qwen 35B Instruct homogène → performance de la famille Alibaba sans reasoning |
| 8 | **08_economy_cross** | `llama-3.1-8b` | `qwen-3.6-35b-instruct` | Draft 8B très léger + réponse 35B dense → rapport coût / efficacité optimal |
| 9 | **09_premium_cross** | `gemma-4-31b` | `mistral-small-4-119b` | Draft mid-range Google (31B) + réponse Mistral géante (119B) |
| 10 | **10_reasoning_draft** | `qwen-3.8-27b` | `mistral-medium-latest` | Draft avec raisonnement (Qwen 27B Thinking) + réponse de référence Mistral |

---

## 🔬 Axes d'Analyse Scientifique

Les 10 combinaisons permettent de répondre précisément à 6 questions :

1. **La taille et le type du draft comptent-ils ?**  
   Comparer **#1** (Draft Medium) vs **#2** (Draft 8B rapide) vs **#10** (Draft 27B Reasoning) avec le **même modèle de réponse** (`mistral-medium-latest`).
2. **Impact du raisonnement (*thinking*) vs instruct classique :**  
   Comparer **#5** (`qwen-3.8-27b` Reasoning) vs **#7** (`qwen-3.6-35b-instruct` Instruct classique).
3. **Quel est le plafond de qualité atteignable ?**  
   Combo **#3** (*Max Quality* 119B + 120B).
4. **Comparaison des modèles homogènes par échelle de taille :**  
   **#4** (8B Meta) vs **#5** (27B Qwen Reasoning) vs **#6** (31B Gemma) vs **#7** (35B Qwen Instruct) vs **#1** (Medium Mistral).
5. **Architectures hybrides performantes :**  
   **#8** (Draft 8B + Réponse 35B) et **#9** (Draft 31B + Réponse 119B).
6. **Robustesse du routeur RAC face au reasoning :**  
   Observer si la réflexion préliminaire de `qwen-3.8-27b` en draft améliore l'attribution des fiches de contact par rapport aux modèles directs.
