# Rapport d'Évaluation RAG - Query_Mix.txt

- **Date :** 2026-09-24T11:51:25.204522
- **Requêtes évaluées :** 23/24
- **Modèles :** Draft: `llama-3.1-8b` | Réponse: `llama-3.1-8b` | Juge: `gpt-oss-120b`
- **Temps d'exécution :** Total RAG: 3347.8s (moy. 139.5s/q) | Évaluation: 247.0s

## Scores Moyens (sur 5.0)

| Métrique | Score Moyen | Description |
|:---|:---:|:---|
| **Faithfulness** | **4.00 / 5** | Fidélité aux documents sources (absence d'hallucination) |
| **Answer Relevance** | **4.09 / 5** | Pertinence de la réponse par rapport à la question |
| **Context Precision** | **3.96 / 5** | Précision des passages extraits par le RAG |
| **Completeness** | **3.17 / 5** | Exhaustivité de la réponse fournie |
| **Conciseness** | **4.87 / 5** | Clarté et concision du texte |
| **Score Global Moyen** | **4.02 / 5** | Moyenne des 5 critères |

## Tableau Récapitulatif par Question

| # | Question | Fidélité | Pertinence | Précision | Durée | Statut |
|---|---|:---:|:---:|:---:|:---:|:---:|
| 1 | C’est quoi les SAPS ? | 5/5 | 5/5 | 5/5 | 72.0s |  Succès |
| 2 | Comment peut-on changer le budget d’un projet ? | 5/5 | 5/5 | 5/5 | 144.7s |  Succès |
| 3 | Quelles sont les différentes démarches à effectuer ? | 4/5 | 2/5 | 5/5 | 335.6s |  Succès |
| 4 | - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire ... | 2/5 | 3/5 | 3/5 | 133.1s |  Succès |
| 5 | A quelle adresse postale ou mail dois-je envoyer mon projet ? | 5/5 | 5/5 | 5/5 | 125.8s |  Succès |
| 6 | Comment m’inscrire / me réinscrire ? | 5/5 | 5/5 | 5/5 | 142.9s |  Succès |
| 7 | Quelles ressources le Pôle SAPS peut m’apporter ? | 5/5 | 4/5 | 5/5 | 95.7s |  Succès |
| 8 | Y a-t-il des alumni ? | 1/5 | 5/5 | 1/5 | 143.6s |  Succès |
| 9 | Que propose le Pôle SAPS ? | 5/5 | 5/5 | 5/5 | 89.4s |  Succès |
| 10 | - Qu’est-ce qu’une invention ? | 2/5 | 3/5 | 3/5 | 122.0s |  Succès |
| 11 | - Je souhaite répondre à un Appel à projet? | -/5 | -/5 | -/5 | 156.4s | ⚠️ Erreur Juge |
| 12 | je suis en arrêt de travail, qui dois-je contacter ? | 5/5 | 5/5 | 5/5 | 132.8s |  Succès |
| 13 | Combien de temps va prendre mon inscription ? | 3/5 | 4/5 | 2/5 | 136.4s |  Succès |
| 14 | Comment avoir un email ? | 2/5 | 3/5 | 3/5 | 136.1s |  Succès |
| 15 | - Je souhaite me procurer le formulaire de déclaration d’invention de l’uni... | 5/5 | 5/5 | 5/5 | 137.6s |  Succès |
| 16 | Qui contacter pour toute demande d'ouvrages en service presse ? | 3/5 | 5/5 | 3/5 | 128.4s |  Succès |
| 17 | comment enregistrer ma demande de formation hors-catalogue et quels documen... | 2/5 | 4/5 | 2/5 | 139.7s |  Succès |
| 18 | Mon jury de thèse est-il valide ? | 5/5 | 4/5 | 5/5 | 140.6s |  Succès |
| 19 | quels types de financement de thèse existent ? | 5/5 | 5/5 | 5/5 | 145.9s |  Succès |
| 20 | - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autr... | 5/5 | 1/5 | 2/5 | 134.2s |  Succès |
| 21 | Je souhaite monter un projet, comment faire ? | 5/5 | 5/5 | 5/5 | 140.8s |  Succès |
| 22 | - Comment protéger un savoir-faire ? | 5/5 | 4/5 | 5/5 | 147.9s |  Succès |
| 23 | Je pars en mission, quelle pièce dois-je remplir ? | 3/5 | 4/5 | 5/5 | 131.4s |  Succès |
| 24 | Quel est le délai moyen entre la soumission d’un manuscrit et sa publicatio... | 5/5 | 3/5 | 2/5 | 135.0s |  Succès |

---
*Rapport généré automatiquement par `Test/run_queries_ragilaas.py`.*