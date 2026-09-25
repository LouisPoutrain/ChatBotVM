# Rapport d'Évaluation RAG - Query_Mix.txt

- **Date :** 2026-09-24T10:51:29.965278
- **Requêtes évaluées :** 24/24
- **Modèles :** Draft: `llama-3.1-8b` | Réponse: `mistral-medium-latest` | Juge: `gpt-oss-120b`
- **Temps d'exécution :** Total RAG: 3572.5s (moy. 148.9s/q) | Évaluation: 210.0s

## Scores Moyens (sur 5.0)

| Métrique | Score Moyen | Description |
|:---|:---:|:---|
| **Faithfulness** | **4.67 / 5** | Fidélité aux documents sources (absence d'hallucination) |
| **Answer Relevance** | **3.71 / 5** | Pertinence de la réponse par rapport à la question |
| **Context Precision** | **4.38 / 5** | Précision des passages extraits par le RAG |
| **Completeness** | **3.38 / 5** | Exhaustivité de la réponse fournie |
| **Conciseness** | **4.58 / 5** | Clarté et concision du texte |
| **Score Global Moyen** | **4.14 / 5** | Moyenne des 5 critères |

## Tableau Récapitulatif par Question

| # | Question | Fidélité | Pertinence | Précision | Durée | Statut |
|---|---|:---:|:---:|:---:|:---:|:---:|
| 1 | C’est quoi les SAPS ? | 5/5 | 5/5 | 5/5 | 83.3s |  Succès |
| 2 | Comment peut-on changer le budget d’un projet ? | 5/5 | 5/5 | 5/5 | 173.2s |  Succès |
| 3 | Quelles sont les différentes démarches à effectuer ? | 5/5 | 1/5 | 5/5 | 117.2s |  Succès |
| 4 | - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire ... | 3/5 | 3/5 | 4/5 | 238.9s |  Succès |
| 5 | A quelle adresse postale ou mail dois-je envoyer mon projet ? | 5/5 | 5/5 | 5/5 | 120.2s |  Succès |
| 6 | Comment m’inscrire / me réinscrire ? | 5/5 | 5/5 | 5/5 | 221.2s |  Succès |
| 7 | Quelles ressources le Pôle SAPS peut m’apporter ? | 5/5 | 5/5 | 5/5 | 81.0s |  Succès |
| 8 | Y a-t-il des alumni ? | 5/5 | 1/5 | 2/5 | 129.1s |  Succès |
| 9 | Que propose le Pôle SAPS ? | 5/5 | 5/5 | 5/5 | 93.4s |  Succès |
| 10 | - Qu’est-ce qu’une invention ? | 4/5 | 5/5 | 3/5 | 224.2s |  Succès |
| 11 | - Je souhaite répondre à un Appel à projet? | 5/5 | 5/5 | 5/5 | 138.6s |  Succès |
| 12 | je suis en arrêt de travail, qui dois-je contacter ? | 5/5 | 5/5 | 5/5 | 134.1s |  Succès |
| 13 | Combien de temps va prendre mon inscription ? | 5/5 | 2/5 | 2/5 | 228.8s |  Succès |
| 14 | Comment avoir un email ? | 5/5 | 4/5 | 5/5 | 124.4s |  Succès |
| 15 | - Je souhaite me procurer le formulaire de déclaration d’invention de l’uni... | 5/5 | 5/5 | 5/5 | 143.1s |  Succès |
| 16 | Qui contacter pour toute demande d'ouvrages en service presse ? | 1/5 | 1/5 | 2/5 | 134.8s |  Succès |
| 17 | comment enregistrer ma demande de formation hors-catalogue et quels documen... | 5/5 | 2/5 | 5/5 | 139.5s |  Succès |
| 18 | Mon jury de thèse est-il valide ? | 5/5 | 3/5 | 5/5 | 133.9s |  Succès |
| 19 | quels types de financement de thèse existent ? | 5/5 | 5/5 | 5/5 | 135.8s |  Succès |
| 20 | - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autr... | 5/5 | 5/5 | 5/5 | 131.9s |  Succès |
| 21 | Je souhaite monter un projet, comment faire ? | 5/5 | 3/5 | 5/5 | 128.8s |  Succès |
| 22 | - Comment protéger un savoir-faire ? | 4/5 | 3/5 | 5/5 | 134.0s |  Succès |
| 23 | Je pars en mission, quelle pièce dois-je remplir ? | 5/5 | 5/5 | 5/5 | 254.2s |  Succès |
| 24 | Quel est le délai moyen entre la soumission d’un manuscrit et sa publicatio... | 5/5 | 1/5 | 2/5 | 129.1s |  Succès |

---
*Rapport généré automatiquement par `Test/run_queries_ragilaas.py`.*