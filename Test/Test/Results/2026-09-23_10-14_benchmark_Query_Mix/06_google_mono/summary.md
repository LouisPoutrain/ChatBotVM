# Rapport d'Évaluation RAG - Query_Mix.txt

- **Date :** 2026-09-24T12:56:57.227610
- **Requêtes évaluées :** 22/24
- **Modèles :** Draft: `gemma-4-31b` | Réponse: `gemma-4-31b` | Juge: `gpt-oss-120b`
- **Temps d'exécution :** Total RAG: 3668.3s (moy. 152.8s/q) | Évaluation: 263.4s

## Scores Moyens (sur 5.0)

| Métrique | Score Moyen | Description |
|:---|:---:|:---|
| **Faithfulness** | **4.86 / 5** | Fidélité aux documents sources (absence d'hallucination) |
| **Answer Relevance** | **3.55 / 5** | Pertinence de la réponse par rapport à la question |
| **Context Precision** | **4.18 / 5** | Précision des passages extraits par le RAG |
| **Completeness** | **2.91 / 5** | Exhaustivité de la réponse fournie |
| **Conciseness** | **4.86 / 5** | Clarté et concision du texte |
| **Score Global Moyen** | **4.07 / 5** | Moyenne des 5 critères |

## Tableau Récapitulatif par Question

| # | Question | Fidélité | Pertinence | Précision | Durée | Statut |
|---|---|:---:|:---:|:---:|:---:|:---:|
| 1 | C’est quoi les SAPS ? | 5/5 | 5/5 | 5/5 | 90.8s |  Succès |
| 2 | Comment peut-on changer le budget d’un projet ? | 5/5 | 5/5 | 5/5 | 161.9s |  Succès |
| 3 | Quelles sont les différentes démarches à effectuer ? | 4/5 | 1/5 | 5/5 | 238.3s |  Succès |
| 4 | - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire ... | 4/5 | 2/5 | 3/5 | 239.5s |  Succès |
| 5 | A quelle adresse postale ou mail dois-je envoyer mon projet ? | 5/5 | 3/5 | 3/5 | 124.5s |  Succès |
| 6 | Comment m’inscrire / me réinscrire ? | -/5 | -/5 | -/5 | 141.9s | ⚠️ Erreur Juge |
| 7 | Quelles ressources le Pôle SAPS peut m’apporter ? | 5/5 | 4/5 | 5/5 | 85.1s |  Succès |
| 8 | Y a-t-il des alumni ? | 5/5 | 1/5 | 1/5 | 140.1s |  Succès |
| 9 | Que propose le Pôle SAPS ? | 5/5 | 5/5 | 5/5 | 101.6s |  Succès |
| 10 | - Qu’est-ce qu’une invention ? | 4/5 | 5/5 | 5/5 | 209.9s |  Succès |
| 11 | - Je souhaite répondre à un Appel à projet? | 5/5 | 2/5 | 5/5 | 110.2s |  Succès |
| 12 | je suis en arrêt de travail, qui dois-je contacter ? | 5/5 | 3/5 | 5/5 | 121.6s |  Succès |
| 13 | Combien de temps va prendre mon inscription ? | 5/5 | 3/5 | 5/5 | 124.0s |  Succès |
| 14 | Comment avoir un email ? | -/5 | -/5 | -/5 | 115.7s | ⚠️ Erreur Juge |
| 15 | - Je souhaite me procurer le formulaire de déclaration d’invention de l’uni... | 5/5 | 5/5 | 5/5 | 125.8s |  Succès |
| 16 | Qui contacter pour toute demande d'ouvrages en service presse ? | 5/5 | 3/5 | 2/5 | 128.6s |  Succès |
| 17 | comment enregistrer ma demande de formation hors-catalogue et quels documen... | 5/5 | 5/5 | 5/5 | 139.4s |  Succès |
| 18 | Mon jury de thèse est-il valide ? | 5/5 | 3/5 | 3/5 | 227.3s |  Succès |
| 19 | quels types de financement de thèse existent ? | 5/5 | 5/5 | 5/5 | 128.7s |  Succès |
| 20 | - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autr... | 5/5 | 3/5 | 4/5 | 128.0s |  Succès |
| 21 | Je souhaite monter un projet, comment faire ? | 5/5 | 4/5 | 5/5 | 132.7s |  Succès |
| 22 | - Comment protéger un savoir-faire ? | 5/5 | 2/5 | 4/5 | 120.8s |  Succès |
| 23 | Je pars en mission, quelle pièce dois-je remplir ? | 5/5 | 5/5 | 5/5 | 213.2s |  Succès |
| 24 | Quel est le délai moyen entre la soumission d’un manuscrit et sa publicatio... | 5/5 | 4/5 | 2/5 | 318.9s |  Succès |

---
*Rapport généré automatiquement par `Test/run_queries_ragilaas.py`.*