# Rapport d'Évaluation RAG - Query_Mix.txt

- **Date :** 2026-09-24T13:59:57.942947
- **Requêtes évaluées :** 24/24
- **Modèles :** Draft: `llama-3.1-8b` | Réponse: `qwen-3.6-35b-instruct` | Juge: `gpt-oss-120b`
- **Temps d'exécution :** Total RAG: 3545.3s (moy. 147.7s/q) | Évaluation: 235.0s

## Scores Moyens (sur 5.0)

| Métrique | Score Moyen | Description |
|:---|:---:|:---|
| **Faithfulness** | **4.33 / 5** | Fidélité aux documents sources (absence d'hallucination) |
| **Answer Relevance** | **3.38 / 5** | Pertinence de la réponse par rapport à la question |
| **Context Precision** | **4.04 / 5** | Précision des passages extraits par le RAG |
| **Completeness** | **2.83 / 5** | Exhaustivité de la réponse fournie |
| **Conciseness** | **4.58 / 5** | Clarté et concision du texte |
| **Score Global Moyen** | **3.83 / 5** | Moyenne des 5 critères |

## Tableau Récapitulatif par Question

| # | Question | Fidélité | Pertinence | Précision | Durée | Statut |
|---|---|:---:|:---:|:---:|:---:|:---:|
| 1 | C’est quoi les SAPS ? | 5/5 | 5/5 | 5/5 | 86.7s |  Succès |
| 2 | Comment peut-on changer le budget d’un projet ? | 5/5 | 5/5 | 5/5 | 173.4s |  Succès |
| 3 | Quelles sont les différentes démarches à effectuer ? | 2/5 | 1/5 | 5/5 | 113.6s |  Succès |
| 4 | - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire ... | 5/5 | 3/5 | 4/5 | 131.7s |  Succès |
| 5 | A quelle adresse postale ou mail dois-je envoyer mon projet ? | 5/5 | 3/5 | 5/5 | 306.6s |  Succès |
| 6 | Comment m’inscrire / me réinscrire ? | 5/5 | 5/5 | 5/5 | 140.1s |  Succès |
| 7 | Quelles ressources le Pôle SAPS peut m’apporter ? | 5/5 | 4/5 | 5/5 | 89.6s |  Succès |
| 8 | Y a-t-il des alumni ? | 5/5 | 1/5 | 1/5 | 119.2s |  Succès |
| 9 | Que propose le Pôle SAPS ? | 5/5 | 4/5 | 5/5 | 74.5s |  Succès |
| 10 | - Qu’est-ce qu’une invention ? | 5/5 | 2/5 | 3/5 | 137.0s |  Succès |
| 11 | - Je souhaite répondre à un Appel à projet? | 5/5 | 5/5 | 5/5 | 120.1s |  Succès |
| 12 | je suis en arrêt de travail, qui dois-je contacter ? | 3/5 | 5/5 | 5/5 | 124.1s |  Succès |
| 13 | Combien de temps va prendre mon inscription ? | 5/5 | 2/5 | 2/5 | 124.7s |  Succès |
| 14 | Comment avoir un email ? | 5/5 | 5/5 | 5/5 | 140.3s |  Succès |
| 15 | - Je souhaite me procurer le formulaire de déclaration d’invention de l’uni... | 5/5 | 5/5 | 5/5 | 128.7s |  Succès |
| 16 | Qui contacter pour toute demande d'ouvrages en service presse ? | 1/5 | 1/5 | 2/5 | 141.4s |  Succès |
| 17 | comment enregistrer ma demande de formation hors-catalogue et quels documen... | 2/5 | 3/5 | 5/5 | 238.7s |  Succès |
| 18 | Mon jury de thèse est-il valide ? | 5/5 | 1/5 | 1/5 | 186.3s |  Succès |
| 19 | quels types de financement de thèse existent ? | 5/5 | 5/5 | 5/5 | 136.4s |  Succès |
| 20 | - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autr... | 1/5 | 1/5 | 2/5 | 311.9s |  Succès |
| 21 | Je souhaite monter un projet, comment faire ? | 5/5 | 4/5 | 5/5 | 131.9s |  Succès |
| 22 | - Comment protéger un savoir-faire ? | 5/5 | 5/5 | 5/5 | 120.4s |  Succès |
| 23 | Je pars en mission, quelle pièce dois-je remplir ? | 5/5 | 5/5 | 5/5 | 135.0s |  Succès |
| 24 | Quel est le délai moyen entre la soumission d’un manuscrit et sa publicatio... | 5/5 | 1/5 | 2/5 | 133.0s |  Succès |

---
*Rapport généré automatiquement par `Test/run_queries_ragilaas.py`.*