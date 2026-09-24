# Rapport d'Évaluation RAG - Query_Mix.txt

- **Date :** 2026-09-23T12:15:33.468561
- **Requêtes évaluées :** 24/24
- **Modèles :** Draft: `mistral-small-4-119b` | Réponse: `gpt-oss-120b` | Juge: `gpt-oss-120b`
- **Temps d'exécution :** Total RAG: 2065.7s (moy. 86.1s/q) | Évaluation: 291.6s

## Scores Moyens (sur 5.0)

| Métrique | Score Moyen | Description |
|:---|:---:|:---|
| **Faithfulness** | **4.79 / 5** | Fidélité aux documents sources (absence d'hallucination) |
| **Answer Relevance** | **3.88 / 5** | Pertinence de la réponse par rapport à la question |
| **Context Precision** | **3.42 / 5** | Précision des passages extraits par le RAG |
| **Completeness** | **3.17 / 5** | Exhaustivité de la réponse fournie |
| **Conciseness** | **5.00 / 5** | Clarté et concision du texte |
| **Score Global Moyen** | **4.05 / 5** | Moyenne des 5 critères |

## Tableau Récapitulatif par Question

| # | Question | Fidélité | Pertinence | Précision | Durée | Statut |
|---|---|:---:|:---:|:---:|:---:|:---:|
| 1 | C’est quoi les SAPS ? | 5/5 | 5/5 | 5/5 | 63.6s |  Succès |
| 2 | Comment peut-on changer le budget d’un projet ? | 5/5 | 5/5 | 5/5 | 114.8s |  Succès |
| 3 | Quelles sont les différentes démarches à effectuer ? | 5/5 | 2/5 | 2/5 | 87.9s |  Succès |
| 4 | - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire ... | 5/5 | 5/5 | 5/5 | 97.1s |  Succès |
| 5 | A quelle adresse postale ou mail dois-je envoyer mon projet ? | 5/5 | 5/5 | 5/5 | 86.4s |  Succès |
| 6 | Comment m’inscrire / me réinscrire ? | 5/5 | 5/5 | 5/5 | 90.8s |  Succès |
| 7 | Quelles ressources le Pôle SAPS peut m’apporter ? | 5/5 | 5/5 | 5/5 | 62.3s |  Succès |
| 8 | Y a-t-il des alumni ? | 5/5 | 1/5 | 1/5 | 90.1s |  Succès |
| 9 | Que propose le Pôle SAPS ? | 5/5 | 5/5 | 5/5 | 61.1s |  Succès |
| 10 | - Qu’est-ce qu’une invention ? | 5/5 | 1/5 | 2/5 | 83.0s |  Succès |
| 11 | - Je souhaite répondre à un Appel à projet? | 5/5 | 4/5 | 2/5 | 89.7s |  Succès |
| 12 | je suis en arrêt de travail, qui dois-je contacter ? | 5/5 | 5/5 | 2/5 | 87.2s |  Succès |
| 13 | Combien de temps va prendre mon inscription ? | 5/5 | 1/5 | 2/5 | 81.0s |  Succès |
| 14 | Comment avoir un email ? | 5/5 | 2/5 | 1/5 | 81.5s |  Succès |
| 15 | - Je souhaite me procurer le formulaire de déclaration d’invention de l’uni... | 5/5 | 5/5 | 5/5 | 89.9s |  Succès |
| 16 | Qui contacter pour toute demande d'ouvrages en service presse ? | 5/5 | 5/5 | 1/5 | 87.3s |  Succès |
| 17 | comment enregistrer ma demande de formation hors-catalogue et quels documen... | 1/5 | 5/5 | 1/5 | 87.0s |  Succès |
| 18 | Mon jury de thèse est-il valide ? | 5/5 | 1/5 | 1/5 | 85.2s |  Succès |
| 19 | quels types de financement de thèse existent ? | 5/5 | 5/5 | 5/5 | 88.5s |  Succès |
| 20 | - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autr... | 5/5 | 5/5 | 5/5 | 95.0s |  Succès |
| 21 | Je souhaite monter un projet, comment faire ? | 5/5 | 5/5 | 5/5 | 93.9s |  Succès |
| 22 | - Comment protéger un savoir-faire ? | 4/5 | 5/5 | 5/5 | 84.7s |  Succès |
| 23 | Je pars en mission, quelle pièce dois-je remplir ? | 5/5 | 5/5 | 5/5 | 90.8s |  Succès |
| 24 | Quel est le délai moyen entre la soumission d’un manuscrit et sa publicatio... | 5/5 | 1/5 | 2/5 | 87.1s |  Succès |

---
*Rapport généré automatiquement par `Test/run_queries_ragilaas.py`.*