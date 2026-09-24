# Rapport d'Évaluation RAG - Query_Mix.txt

- **Date :** 2026-09-23T13:38:38.368510
- **Requêtes évaluées :** 24/24
- **Modèles :** Draft: `mistral-small-3.2-24b` | Réponse: `mistral-small-4-119b` | Juge: `gpt-oss-120b`
- **Temps d'exécution :** Total RAG: 2342.0s (moy. 97.6s/q) | Évaluation: 291.4s

## Scores Moyens (sur 5.0)

| Métrique | Score Moyen | Description |
|:---|:---:|:---|
| **Faithfulness** | **4.75 / 5** | Fidélité aux documents sources (absence d'hallucination) |
| **Answer Relevance** | **4.25 / 5** | Pertinence de la réponse par rapport à la question |
| **Context Precision** | **4.38 / 5** | Précision des passages extraits par le RAG |
| **Completeness** | **3.75 / 5** | Exhaustivité de la réponse fournie |
| **Conciseness** | **5.00 / 5** | Clarté et concision du texte |
| **Score Global Moyen** | **4.42 / 5** | Moyenne des 5 critères |

## Tableau Récapitulatif par Question

| # | Question | Fidélité | Pertinence | Précision | Durée | Statut |
|---|---|:---:|:---:|:---:|:---:|:---:|
| 1 | C’est quoi les SAPS ? | 5/5 | 5/5 | 5/5 | 57.5s |  Succès |
| 2 | Comment peut-on changer le budget d’un projet ? | 5/5 | 5/5 | 5/5 | 105.0s |  Succès |
| 3 | Quelles sont les différentes démarches à effectuer ? | 3/5 | 2/5 | 5/5 | 83.7s |  Succès |
| 4 | - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire ... | 4/5 | 5/5 | 5/5 | 88.3s |  Succès |
| 5 | A quelle adresse postale ou mail dois-je envoyer mon projet ? | 5/5 | 5/5 | 4/5 | 185.2s |  Succès |
| 6 | Comment m’inscrire / me réinscrire ? | 5/5 | 5/5 | 5/5 | 85.7s |  Succès |
| 7 | Quelles ressources le Pôle SAPS peut m’apporter ? | 5/5 | 5/5 | 5/5 | 58.0s |  Succès |
| 8 | Y a-t-il des alumni ? | 5/5 | 1/5 | 1/5 | 80.3s |  Succès |
| 9 | Que propose le Pôle SAPS ? | 5/5 | 5/5 | 5/5 | 58.2s |  Succès |
| 10 | - Qu’est-ce qu’une invention ? | 3/5 | 5/5 | 3/5 | 85.1s |  Succès |
| 11 | - Je souhaite répondre à un Appel à projet? | 5/5 | 5/5 | 5/5 | 84.1s |  Succès |
| 12 | je suis en arrêt de travail, qui dois-je contacter ? | 5/5 | 5/5 | 4/5 | 88.3s |  Succès |
| 13 | Combien de temps va prendre mon inscription ? | 5/5 | 5/5 | 5/5 | 83.4s |  Succès |
| 14 | Comment avoir un email ? | 5/5 | 5/5 | 5/5 | 186.0s |  Succès |
| 15 | - Je souhaite me procurer le formulaire de déclaration d’invention de l’uni... | 5/5 | 5/5 | 5/5 | 82.7s |  Succès |
| 16 | Qui contacter pour toute demande d'ouvrages en service presse ? | 4/5 | 2/5 | 2/5 | 84.2s |  Succès |
| 17 | comment enregistrer ma demande de formation hors-catalogue et quels documen... | 5/5 | 2/5 | 1/5 | 82.3s |  Succès |
| 18 | Mon jury de thèse est-il valide ? | 5/5 | 4/5 | 5/5 | 137.3s |  Succès |
| 19 | quels types de financement de thèse existent ? | 5/5 | 5/5 | 5/5 | 83.8s |  Succès |
| 20 | - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autr... | 5/5 | 5/5 | 5/5 | 85.1s |  Succès |
| 21 | Je souhaite monter un projet, comment faire ? | 5/5 | 5/5 | 5/5 | 89.0s |  Succès |
| 22 | - Comment protéger un savoir-faire ? | 5/5 | 5/5 | 5/5 | 93.7s |  Succès |
| 23 | Je pars en mission, quelle pièce dois-je remplir ? | 5/5 | 5/5 | 5/5 | 85.3s |  Succès |
| 24 | Quel est le délai moyen entre la soumission d’un manuscrit et sa publicatio... | 5/5 | 1/5 | 5/5 | 189.9s |  Succès |

---
*Rapport généré automatiquement par `Test/run_queries_ragilaas.py`.*