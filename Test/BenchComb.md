# 🧪 Benchmark Multi-Modèles RAGilaas (Mis à jour 2026)

## Modèles Actuellement Disponibles sur l'API

| Modèle | Taille | Famille | Type | Statut | Rôle privilégié |
|--------|--------|---------|------|--------|-----------------|
| `llama-3.1-8b` | 8B | Meta LLaMA | Instruct dense ultra-léger | Actif | Vitesse, frugalité, RAC/Draft rapide |
| `qwen-3.8-27b` | 27B | Alibaba Qwen | Reasoning / Thinking | Actif | Raisonnement approfondi (RAC / HyDE) |
| `gemma-4-31b` | 31B | Google Gemma | Instruct dense | Actif | Modèle intermédiaire équilibré |
| `qwen-3.6-35b-instruct` | 35B | Alibaba Qwen | Instruct dense | Actif | Suivi strict des consignes |
| `mistral-medium-latest` | ~120B | Mistral (API) | Équilibré / Prod | Actif | Baseline de référence Prod |
| `mistral-small-4-119b` | 119B | Mistral | Poids lourd (119B) | Actif | Haute capacité & Juge impartial |

> ℹ️ *Note : `gpt-oss-120b`, `mistral-small-3.2-24b` et `llama-3.3-70b` ne sont plus fournis par l'API et ont été retirés.*

---

## Juge Impartial Fixe

> [!IMPORTANT]
> Le **juge d'évaluation** est fixé à `mistral-small-4-119b` (le plus grand modèle disponible sur l'API, 119 milliards de paramètres) pour **toutes** les combinaisons afin de garantir une comparaison équitable et éliminer tout biais inter-juge.

---

## 10 Combinaisons Définies

| # | Nom | Draft Model (HyDE) | Answer Model (Réponse) | RAC Model (Routeur) | Logique Expérimentale |
|---|-----|---------------------|------------------------|---------------------|-----------------------|
| 1 | **01_baseline** | `mistral-medium-latest` | `mistral-medium-latest` | `mistral-medium-latest` | Baseline de référence homogène (tout Mistral Medium) |
| 2 | **02_fast_draft_rac** | `llama-3.1-8b` | `mistral-medium-latest` | `llama-3.1-8b` | Draft 8B & RAC 8B rapides + réponse de référence Mistral Medium |
| 3 | **03_max_quality** | `mistral-medium-latest` | `mistral-small-4-119b` | `mistral-small-4-119b` | Plafond max qualité (RAC 119B + réponse 119B) |
| 4 | **04_meta_mono** | `llama-3.1-8b` | `llama-3.1-8b` | `llama-3.1-8b` | 100% Meta 8B de bout en bout (vitesse max & ultra-léger) |
| 5 | **05_qwen_reasoning_mono** | `qwen-3.8-27b` | `qwen-3.8-27b` | `qwen-3.8-27b` | 100% Qwen 27B avec raisonnement (*thinking*) sur RAC, HyDE et Réponse |
| 6 | **06_google_mono** | `gemma-4-31b` | `gemma-4-31b` | `gemma-4-31b` | Google Gemma 31B homogène sur l'ensemble du pipeline |
| 7 | **07_qwen_instruct_mono** | `qwen-3.6-35b-instruct` | `qwen-3.6-35b-instruct` | `qwen-3.6-35b-instruct` | Alibaba Qwen 35B Instruct homogène |
| 8 | **08_economy_cross** | `llama-3.1-8b` | `qwen-3.6-35b-instruct` | `llama-3.1-8b` | Architecture frugale : Llama 8B Draft/RAC + Qwen 35B réponse |
| 9 | **09_premium_cross** | `gemma-4-31b` | `mistral-small-4-119b` | `mistral-medium-latest` | Architecture hybride : Gemma 31B Draft + RAC Medium + Réponse 119B |
| 10 | **10_reasoning_rac** | `mistral-medium-latest` | `mistral-medium-latest` | `qwen-3.8-27b` | **Isolation du RAC** : Raisonnement Qwen 27B pour les contacts + Baseline Medium |

---

## 🔬 Axes d'Analyse Scientifique

Les 10 combinaisons permettent de répondre précisément à plusieurs questions clés :

1. **Quel est l'impact du LLM sur le routeur de contacts RAC ?**  
   - Comparer **#1** (RAC Mistral Medium) vs **#2** (RAC LLaMA 8B) vs **#10** (RAC Qwen 27B Reasoning) vs **#3** (RAC 119B) avec des architectures de réponse comparables.
   - Observer si le raisonnement (thinking) de `qwen-3.8-27b` évite les erreurs d'aiguillage de service.
2. **La taille et le type du draft HyDE comptent-ils ?**  
   - Comparer **#1** (Draft Medium) vs **#2** (Draft 8B rapide) vs **#5** (Draft 27B Reasoning).
3. **Comparaison des modèles homogènes par échelle de taille :**  
   - **#4** (8B Meta) vs **#5** (27B Qwen Reasoning) vs **#6** (31B Gemma) vs **#7** (35B Qwen Instruct) vs **#1** (Medium Mistral).
4. **Architectures hybrides (spécialisation des tâches) :**  
   - **#8** (Modèle léger pour Draft & RAC + Modèle dense pour Réponse).
   - **#9** (Draft Gemma 31B + RAC Medium + Réponse Mistral 119B).
   - **#10** (RAC confié à un modèle de raisonnement CoT).
