# Rapport d'Évaluation RAG - Query_Mix.txt

- **Date :** 2026-09-23T11:36:15.908544
- **Requêtes évaluées :** 7/24
- **Modèles :** Draft: `llama-3.1-8b` | Réponse: `mistral-medium-latest` | Juge: `gpt-oss-120b`
- **Temps d'exécution :** Total RAG: 2128.4s (moy. 88.7s/q) | Évaluation: 75.2s

## Scores Moyens (sur 5.0)

| Métrique | Score Moyen | Description |
|:---|:---:|:---|
| **Faithfulness** | **4.43 / 5** | Fidélité aux documents sources (absence d'hallucination) |
| **Answer Relevance** | **4.43 / 5** | Pertinence de la réponse par rapport à la question |
| **Context Precision** | **4.86 / 5** | Précision des passages extraits par le RAG |
| **Completeness** | **3.57 / 5** | Exhaustivité de la réponse fournie |
| **Conciseness** | **5.00 / 5** | Clarté et concision du texte |
| **Score Global Moyen** | **4.46 / 5** | Moyenne des 5 critères |

## Tableau Récapitulatif par Question

| # | Question | Fidélité | Pertinence | Précision | Durée | Statut |
|---|---|:---:|:---:|:---:|:---:|:---:|
| 1 | C’est quoi les SAPS ? | 5/5 | 5/5 | 5/5 | 62.4s |  Succès |
| 2 | Comment peut-on changer le budget d’un projet ? | 5/5 | 5/5 | 5/5 | 114.4s |  Succès |
| 3 | Quelles sont les différentes démarches à effectuer ? | 1/5 | 1/5 | 4/5 | 94.5s |  Succès |
| 4 | - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire ... | 5/5 | 5/5 | 5/5 | 167.0s |  Succès |
| 5 | A quelle adresse postale ou mail dois-je envoyer mon projet ? | 5/5 | 5/5 | 5/5 | 87.2s |  Succès |
| 6 | Comment m’inscrire / me réinscrire ? | 5/5 | 5/5 | 5/5 | 90.4s |  Succès |
| 7 | Quelles ressources le Pôle SAPS peut m’apporter ? | 5/5 | 5/5 | 5/5 | 65.5s |  Succès |
| 8 | Y a-t-il des alumni ? | -/5 | -/5 | -/5 | 119.0s | ⚠️ Erreur Juge |
| 9 | Que propose le Pôle SAPS ? | -/5 | -/5 | -/5 | 56.3s | ⚠️ Erreur Juge |
| 10 | - Qu’est-ce qu’une invention ? | -/5 | -/5 | -/5 | 81.2s | ⚠️ Erreur Juge |
| 11 | - Je souhaite répondre à un Appel à projet? | -/5 | -/5 | -/5 | 82.1s | ⚠️ Erreur Juge |
| 12 | je suis en arrêt de travail, qui dois-je contacter ? | -/5 | -/5 | -/5 | 90.7s | ⚠️ Erreur Juge |
| 13 | Combien de temps va prendre mon inscription ? | -/5 | -/5 | -/5 | 85.4s | ⚠️ Erreur Juge |
| 14 | Comment avoir un email ? | -/5 | -/5 | -/5 | 81.3s | ⚠️ Erreur Juge |
| 15 | - Je souhaite me procurer le formulaire de déclaration d’invention de l’uni... | -/5 | -/5 | -/5 | 82.1s | ⚠️ Erreur Juge |
| 16 | Qui contacter pour toute demande d'ouvrages en service presse ? | -/5 | -/5 | -/5 | 81.1s | ⚠️ Erreur Juge |
| 17 | comment enregistrer ma demande de formation hors-catalogue et quels documen... | -/5 | -/5 | -/5 | 88.9s | ⚠️ Erreur Juge |
| 18 | Mon jury de thèse est-il valide ? | -/5 | -/5 | -/5 | 88.3s | ⚠️ Erreur Juge |
| 19 | quels types de financement de thèse existent ? | -/5 | -/5 | -/5 | 86.0s | ⚠️ Erreur Juge |
| 20 | - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autr... | -/5 | -/5 | -/5 | 83.2s | ⚠️ Erreur Juge |
| 21 | Je souhaite monter un projet, comment faire ? | -/5 | -/5 | -/5 | 85.4s | ⚠️ Erreur Juge |
| 22 | - Comment protéger un savoir-faire ? | -/5 | -/5 | -/5 | 83.9s | ⚠️ Erreur Juge |
| 23 | Je pars en mission, quelle pièce dois-je remplir ? | -/5 | -/5 | -/5 | 89.9s | ⚠️ Erreur Juge |
| 24 | Quel est le délai moyen entre la soumission d’un manuscrit et sa publicatio... | -/5 | -/5 | -/5 | 82.2s | ⚠️ Erreur Juge |

---
*Rapport généré automatiquement par `Test/run_queries_ragilaas.py`.*