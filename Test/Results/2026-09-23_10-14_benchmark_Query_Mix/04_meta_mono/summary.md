# Rapport d'Évaluation RAG - Query_Mix.txt

- **Date :** 2026-09-23T12:54:44.674557
- **Requêtes évaluées :** 23/24
- **Modèles :** Draft: `llama-3.1-8b` | Réponse: `llama-3.1-8b` | Juge: `gpt-oss-120b`
- **Temps d'exécution :** Total RAG: 2090.5s (moy. 87.1s/q) | Évaluation: 260.5s

## Scores Moyens (sur 5.0)

| Métrique | Score Moyen | Description |
|:---|:---:|:---|
| **Faithfulness** | **3.96 / 5** | Fidélité aux documents sources (absence d'hallucination) |
| **Answer Relevance** | **4.04 / 5** | Pertinence de la réponse par rapport à la question |
| **Context Precision** | **3.52 / 5** | Précision des passages extraits par le RAG |
| **Completeness** | **3.04 / 5** | Exhaustivité de la réponse fournie |
| **Conciseness** | **4.91 / 5** | Clarté et concision du texte |
| **Score Global Moyen** | **3.90 / 5** | Moyenne des 5 critères |

## Tableau Récapitulatif par Question

| # | Question | Fidélité | Pertinence | Précision | Durée | Statut |
|---|---|:---:|:---:|:---:|:---:|:---:|
| 1 | C’est quoi les SAPS ? | 5/5 | 5/5 | 5/5 | 59.2s |  Succès |
| 2 | Comment peut-on changer le budget d’un projet ? | 5/5 | 5/5 | 5/5 | 108.7s |  Succès |
| 3 | Quelles sont les différentes démarches à effectuer ? | 5/5 | 5/5 | 5/5 | 98.1s |  Succès |
| 4 | - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire ... | 3/5 | 3/5 | 3/5 | 88.1s |  Succès |
| 5 | A quelle adresse postale ou mail dois-je envoyer mon projet ? | 5/5 | 3/5 | 4/5 | 82.4s |  Succès |
| 6 | Comment m’inscrire / me réinscrire ? | 5/5 | 5/5 | 5/5 | 93.9s |  Succès |
| 7 | Quelles ressources le Pôle SAPS peut m’apporter ? | 5/5 | 4/5 | 5/5 | 60.6s |  Succès |
| 8 | Y a-t-il des alumni ? | 2/5 | 4/5 | 2/5 | 92.6s |  Succès |
| 9 | Que propose le Pôle SAPS ? | 5/5 | 4/5 | 5/5 | 63.5s |  Succès |
| 10 | - Qu’est-ce qu’une invention ? | 2/5 | 5/5 | 2/5 | 85.8s |  Succès |
| 11 | - Je souhaite répondre à un Appel à projet? | -/5 | -/5 | -/5 | 113.9s | ⚠️ Erreur Juge |
| 12 | je suis en arrêt de travail, qui dois-je contacter ? | 5/5 | 5/5 | 5/5 | 90.0s |  Succès |
| 13 | Combien de temps va prendre mon inscription ? | 5/5 | 5/5 | 2/5 | 92.0s |  Succès |
| 14 | Comment avoir un email ? | 2/5 | 4/5 | 1/5 | 88.1s |  Succès |
| 15 | - Je souhaite me procurer le formulaire de déclaration d’invention de l’uni... | 5/5 | 5/5 | 5/5 | 85.2s |  Succès |
| 16 | Qui contacter pour toute demande d'ouvrages en service presse ? | 1/5 | 2/5 | 1/5 | 84.1s |  Succès |
| 17 | comment enregistrer ma demande de formation hors-catalogue et quels documen... | 1/5 | 5/5 | 1/5 | 86.4s |  Succès |
| 18 | Mon jury de thèse est-il valide ? | 2/5 | 2/5 | 1/5 | 86.1s |  Succès |
| 19 | quels types de financement de thèse existent ? | 5/5 | 5/5 | 5/5 | 94.0s |  Succès |
| 20 | - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autr... | 5/5 | 1/5 | 2/5 | 90.2s |  Succès |
| 21 | Je souhaite monter un projet, comment faire ? | 5/5 | 5/5 | 5/5 | 90.6s |  Succès |
| 22 | - Comment protéger un savoir-faire ? | 5/5 | 4/5 | 5/5 | 83.8s |  Succès |
| 23 | Je pars en mission, quelle pièce dois-je remplir ? | 5/5 | 5/5 | 5/5 | 87.5s |  Succès |
| 24 | Quel est le délai moyen entre la soumission d’un manuscrit et sa publicatio... | 3/5 | 2/5 | 2/5 | 85.5s |  Succès |

---
*Rapport généré automatiquement par `Test/run_queries_ragilaas.py`.*