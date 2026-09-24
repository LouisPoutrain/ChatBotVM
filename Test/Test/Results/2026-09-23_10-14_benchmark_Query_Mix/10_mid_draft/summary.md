# Rapport d'Évaluation RAG - Query_Mix.txt

- **Date :** 2026-09-24T14:55:45.973043
- **Requêtes évaluées :** 13/24
- **Modèles :** Draft: `mistral-small-3.2-24b` | Réponse: `mistral-medium-latest` | Juge: `gpt-oss-120b`
- **Temps d'exécution :** Total RAG: 3225.7s (moy. 134.4s/q) | Évaluation: 122.0s

## Scores Moyens (sur 5.0)

| Métrique | Score Moyen | Description |
|:---|:---:|:---|
| **Faithfulness** | **4.77 / 5** | Fidélité aux documents sources (absence d'hallucination) |
| **Answer Relevance** | **3.62 / 5** | Pertinence de la réponse par rapport à la question |
| **Context Precision** | **4.38 / 5** | Précision des passages extraits par le RAG |
| **Completeness** | **3.15 / 5** | Exhaustivité de la réponse fournie |
| **Conciseness** | **5.00 / 5** | Clarté et concision du texte |
| **Score Global Moyen** | **4.18 / 5** | Moyenne des 5 critères |

## Tableau Récapitulatif par Question

| # | Question | Fidélité | Pertinence | Précision | Durée | Statut |
|---|---|:---:|:---:|:---:|:---:|:---:|
| 1 | C’est quoi les SAPS ? | -/5 | -/5 | -/5 | 83.9s | ⚠️ Erreur Juge |
| 2 | Comment peut-on changer le budget d’un projet ? | -/5 | -/5 | -/5 | 164.3s | ⚠️ Erreur Juge |
| 3 | Quelles sont les différentes démarches à effectuer ? | -/5 | -/5 | -/5 | 128.2s | ⚠️ Erreur Juge |
| 4 | - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire ... | -/5 | -/5 | -/5 | 134.9s | ⚠️ Erreur Juge |
| 5 | A quelle adresse postale ou mail dois-je envoyer mon projet ? | -/5 | -/5 | -/5 | 138.1s | ⚠️ Erreur Juge |
| 6 | Comment m’inscrire / me réinscrire ? | -/5 | -/5 | -/5 | 137.3s | ⚠️ Erreur Juge |
| 7 | Quelles ressources le Pôle SAPS peut m’apporter ? | -/5 | -/5 | -/5 | 84.0s | ⚠️ Erreur Juge |
| 8 | Y a-t-il des alumni ? | -/5 | -/5 | -/5 | 134.5s | ⚠️ Erreur Juge |
| 9 | Que propose le Pôle SAPS ? | -/5 | -/5 | -/5 | 88.4s | ⚠️ Erreur Juge |
| 10 | - Qu’est-ce qu’une invention ? | -/5 | -/5 | -/5 | 131.0s | ⚠️ Erreur Juge |
| 11 | - Je souhaite répondre à un Appel à projet? | 5/5 | 5/5 | 5/5 | 137.8s |  Succès |
| 12 | je suis en arrêt de travail, qui dois-je contacter ? | 5/5 | 5/5 | 5/5 | 135.2s |  Succès |
| 13 | Combien de temps va prendre mon inscription ? | 5/5 | 1/5 | 4/5 | 135.3s |  Succès |
| 14 | Comment avoir un email ? | 5/5 | 5/5 | 5/5 | 138.2s |  Succès |
| 15 | - Je souhaite me procurer le formulaire de déclaration d’invention de l’uni... | 5/5 | 5/5 | 5/5 | 140.3s |  Succès |
| 16 | Qui contacter pour toute demande d'ouvrages en service presse ? | 5/5 | 1/5 | 1/5 | 315.7s |  Succès |
| 17 | comment enregistrer ma demande de formation hors-catalogue et quels documen... | 5/5 | 5/5 | 5/5 | 158.2s |  Succès |
| 18 | Mon jury de thèse est-il valide ? | -/5 | -/5 | -/5 | 135.0s | ⚠️ Erreur Juge |
| 19 | quels types de financement de thèse existent ? | 5/5 | 5/5 | 5/5 | 134.3s |  Succès |
| 20 | - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autr... | 5/5 | 5/5 | 5/5 | 140.5s |  Succès |
| 21 | Je souhaite monter un projet, comment faire ? | 5/5 | 2/5 | 5/5 | 95.0s |  Succès |
| 22 | - Comment protéger un savoir-faire ? | 2/5 | 2/5 | 5/5 | 86.7s |  Succès |
| 23 | Je pars en mission, quelle pièce dois-je remplir ? | 5/5 | 5/5 | 5/5 | 151.1s |  Succès |
| 24 | Quel est le délai moyen entre la soumission d’un manuscrit et sa publicatio... | 5/5 | 1/5 | 2/5 | 97.7s |  Succès |

---
*Rapport généré automatiquement par `Test/run_queries_ragilaas.py`.*