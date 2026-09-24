# Rapport d'Évaluation RAG - Query_Mix.txt

- **Date :** 2026-09-23T16:37:40.486116
- **Requêtes évaluées :** 24/24
- **Modèles :** Draft: `gemma-4-31b` | Réponse: `mistral-small-4-119b` | Juge: `gpt-oss-120b`
- **Temps d'exécution :** Total RAG: 2297.6s (moy. 95.7s/q) | Évaluation: 248.0s

## Scores Moyens (sur 5.0)

| Métrique | Score Moyen | Description |
|:---|:---:|:---|
| **Faithfulness** | **4.58 / 5** | Fidélité aux documents sources (absence d'hallucination) |
| **Answer Relevance** | **3.67 / 5** | Pertinence de la réponse par rapport à la question |
| **Context Precision** | **4.04 / 5** | Précision des passages extraits par le RAG |
| **Completeness** | **3.21 / 5** | Exhaustivité de la réponse fournie |
| **Conciseness** | **4.96 / 5** | Clarté et concision du texte |
| **Score Global Moyen** | **4.09 / 5** | Moyenne des 5 critères |

## Tableau Récapitulatif par Question

| # | Question | Fidélité | Pertinence | Précision | Durée | Statut |
|---|---|:---:|:---:|:---:|:---:|:---:|
| 1 | C’est quoi les SAPS ? | 5/5 | 5/5 | 5/5 | 59.6s |  Succès |
| 2 | Comment peut-on changer le budget d’un projet ? | 5/5 | 5/5 | 5/5 | 107.8s |  Succès |
| 3 | Quelles sont les différentes démarches à effectuer ? | 4/5 | 3/5 | 5/5 | 87.2s |  Succès |
| 4 | - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire ... | 5/5 | 3/5 | 4/5 | 141.9s |  Succès |
| 5 | A quelle adresse postale ou mail dois-je envoyer mon projet ? | 5/5 | 5/5 | 5/5 | 189.7s |  Succès |
| 6 | Comment m’inscrire / me réinscrire ? | 5/5 | 5/5 | 5/5 | 86.4s |  Succès |
| 7 | Quelles ressources le Pôle SAPS peut m’apporter ? | 5/5 | 5/5 | 5/5 | 58.2s |  Succès |
| 8 | Y a-t-il des alumni ? | 5/5 | 5/5 | 5/5 | 132.1s |  Succès |
| 9 | Que propose le Pôle SAPS ? | 5/5 | 5/5 | 5/5 | 57.0s |  Succès |
| 10 | - Qu’est-ce qu’une invention ? | 3/5 | 4/5 | 3/5 | 134.0s |  Succès |
| 11 | - Je souhaite répondre à un Appel à projet? | 5/5 | 3/5 | 2/5 | 83.4s |  Succès |
| 12 | je suis en arrêt de travail, qui dois-je contacter ? | 5/5 | 5/5 | 3/5 | 88.1s |  Succès |
| 13 | Combien de temps va prendre mon inscription ? | 5/5 | 3/5 | 4/5 | 83.5s |  Succès |
| 14 | Comment avoir un email ? | 2/5 | 2/5 | 1/5 | 86.0s |  Succès |
| 15 | - Je souhaite me procurer le formulaire de déclaration d’invention de l’uni... | 5/5 | 5/5 | 5/5 | 84.2s |  Succès |
| 16 | Qui contacter pour toute demande d'ouvrages en service presse ? | 2/5 | 2/5 | 2/5 | 89.8s |  Succès |
| 17 | comment enregistrer ma demande de formation hors-catalogue et quels documen... | 5/5 | 1/5 | 1/5 | 85.7s |  Succès |
| 18 | Mon jury de thèse est-il valide ? | 5/5 | 1/5 | 5/5 | 82.8s |  Succès |
| 19 | quels types de financement de thèse existent ? | 5/5 | 5/5 | 5/5 | 85.3s |  Succès |
| 20 | - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autr... | 5/5 | 1/5 | 2/5 | 136.0s |  Succès |
| 21 | Je souhaite monter un projet, comment faire ? | 5/5 | 4/5 | 5/5 | 85.2s |  Succès |
| 22 | - Comment protéger un savoir-faire ? | 5/5 | 5/5 | 5/5 | 85.0s |  Succès |
| 23 | Je pars en mission, quelle pièce dois-je remplir ? | 4/5 | 5/5 | 5/5 | 86.3s |  Succès |
| 24 | Quel est le délai moyen entre la soumission d’un manuscrit et sa publicatio... | 5/5 | 1/5 | 5/5 | 82.4s |  Succès |

---
*Rapport généré automatiquement par `Test/run_queries_ragilaas.py`.*