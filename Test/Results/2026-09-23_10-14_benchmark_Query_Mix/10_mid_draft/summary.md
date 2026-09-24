# Rapport d'Évaluation RAG - Query_Mix.txt

- **Date :** 2026-09-23T17:14:28.138230
- **Requêtes évaluées :** 15/24
- **Modèles :** Draft: `mistral-small-3.2-24b` | Réponse: `mistral-medium-latest` | Juge: `gpt-oss-120b`
- **Temps d'exécution :** Total RAG: 2081.6s (moy. 86.7s/q) | Évaluation: 125.8s

## Scores Moyens (sur 5.0)

| Métrique | Score Moyen | Description |
|:---|:---:|:---|
| **Faithfulness** | **4.47 / 5** | Fidélité aux documents sources (absence d'hallucination) |
| **Answer Relevance** | **3.40 / 5** | Pertinence de la réponse par rapport à la question |
| **Context Precision** | **4.20 / 5** | Précision des passages extraits par le RAG |
| **Completeness** | **3.07 / 5** | Exhaustivité de la réponse fournie |
| **Conciseness** | **5.00 / 5** | Clarté et concision du texte |
| **Score Global Moyen** | **4.03 / 5** | Moyenne des 5 critères |

## Tableau Récapitulatif par Question

| # | Question | Fidélité | Pertinence | Précision | Durée | Statut |
|---|---|:---:|:---:|:---:|:---:|:---:|
| 1 | C’est quoi les SAPS ? | -/5 | -/5 | -/5 | 55.4s | ⚠️ Erreur Juge |
| 2 | Comment peut-on changer le budget d’un projet ? | -/5 | -/5 | -/5 | 106.7s | ⚠️ Erreur Juge |
| 3 | Quelles sont les différentes démarches à effectuer ? | -/5 | -/5 | -/5 | 79.7s | ⚠️ Erreur Juge |
| 4 | - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire ... | -/5 | -/5 | -/5 | 83.9s | ⚠️ Erreur Juge |
| 5 | A quelle adresse postale ou mail dois-je envoyer mon projet ? | -/5 | -/5 | -/5 | 80.1s | ⚠️ Erreur Juge |
| 6 | Comment m’inscrire / me réinscrire ? | -/5 | -/5 | -/5 | 86.0s | ⚠️ Erreur Juge |
| 7 | Quelles ressources le Pôle SAPS peut m’apporter ? | -/5 | -/5 | -/5 | 54.1s | ⚠️ Erreur Juge |
| 8 | Y a-t-il des alumni ? | -/5 | -/5 | -/5 | 87.7s | ⚠️ Erreur Juge |
| 9 | Que propose le Pôle SAPS ? | -/5 | -/5 | -/5 | 54.1s | ⚠️ Erreur Juge |
| 10 | - Qu’est-ce qu’une invention ? | 5/5 | 1/5 | 2/5 | 84.5s |  Succès |
| 11 | - Je souhaite répondre à un Appel à projet? | 5/5 | 5/5 | 5/5 | 88.1s |  Succès |
| 12 | je suis en arrêt de travail, qui dois-je contacter ? | 5/5 | 4/5 | 5/5 | 91.1s |  Succès |
| 13 | Combien de temps va prendre mon inscription ? | 4/5 | 2/5 | 3/5 | 141.8s |  Succès |
| 14 | Comment avoir un email ? | 5/5 | 5/5 | 5/5 | 84.5s |  Succès |
| 15 | - Je souhaite me procurer le formulaire de déclaration d’invention de l’uni... | 5/5 | 5/5 | 5/5 | 86.7s |  Succès |
| 16 | Qui contacter pour toute demande d'ouvrages en service presse ? | 1/5 | 1/5 | 2/5 | 85.8s |  Succès |
| 17 | comment enregistrer ma demande de formation hors-catalogue et quels documen... | 5/5 | 5/5 | 5/5 | 93.5s |  Succès |
| 18 | Mon jury de thèse est-il valide ? | 5/5 | 2/5 | 5/5 | 89.0s |  Succès |
| 19 | quels types de financement de thèse existent ? | 5/5 | 5/5 | 5/5 | 87.8s |  Succès |
| 20 | - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autr... | 5/5 | 5/5 | 5/5 | 87.3s |  Succès |
| 21 | Je souhaite monter un projet, comment faire ? | 5/5 | 3/5 | 4/5 | 94.3s |  Succès |
| 22 | - Comment protéger un savoir-faire ? | 2/5 | 2/5 | 5/5 | 98.5s |  Succès |
| 23 | Je pars en mission, quelle pièce dois-je remplir ? | 5/5 | 5/5 | 5/5 | 85.5s |  Succès |
| 24 | Quel est le délai moyen entre la soumission d’un manuscrit et sa publicatio... | 5/5 | 1/5 | 2/5 | 95.6s |  Succès |

---
*Rapport généré automatiquement par `Test/run_queries_ragilaas.py`.*