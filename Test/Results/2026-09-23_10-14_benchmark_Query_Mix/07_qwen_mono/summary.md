# Rapport d'Évaluation RAG - Query_Mix.txt

- **Date :** 2026-09-23T15:09:25.897030
- **Requêtes évaluées :** 24/24
- **Modèles :** Draft: `qwen-3.6-35b-instruct` | Réponse: `qwen-3.6-35b-instruct` | Juge: `gpt-oss-120b`
- **Temps d'exécution :** Total RAG: 2451.9s (moy. 102.2s/q) | Évaluation: 270.1s

## Scores Moyens (sur 5.0)

| Métrique | Score Moyen | Description |
|:---|:---:|:---|
| **Faithfulness** | **4.58 / 5** | Fidélité aux documents sources (absence d'hallucination) |
| **Answer Relevance** | **4.08 / 5** | Pertinence de la réponse par rapport à la question |
| **Context Precision** | **4.08 / 5** | Précision des passages extraits par le RAG |
| **Completeness** | **3.33 / 5** | Exhaustivité de la réponse fournie |
| **Conciseness** | **5.00 / 5** | Clarté et concision du texte |
| **Score Global Moyen** | **4.22 / 5** | Moyenne des 5 critères |

## Tableau Récapitulatif par Question

| # | Question | Fidélité | Pertinence | Précision | Durée | Statut |
|---|---|:---:|:---:|:---:|:---:|:---:|
| 1 | C’est quoi les SAPS ? | 5/5 | 5/5 | 5/5 | 56.2s |  Succès |
| 2 | Comment peut-on changer le budget d’un projet ? | 5/5 | 5/5 | 5/5 | 108.0s |  Succès |
| 3 | Quelles sont les différentes démarches à effectuer ? | 4/5 | 4/5 | 4/5 | 84.5s |  Succès |
| 4 | - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire ... | 5/5 | 5/5 | 5/5 | 100.9s |  Succès |
| 5 | A quelle adresse postale ou mail dois-je envoyer mon projet ? | 5/5 | 4/5 | 2/5 | 87.1s |  Succès |
| 6 | Comment m’inscrire / me réinscrire ? | 5/5 | 4/5 | 5/5 | 84.3s |  Succès |
| 7 | Quelles ressources le Pôle SAPS peut m’apporter ? | 5/5 | 5/5 | 5/5 | 116.3s |  Succès |
| 8 | Y a-t-il des alumni ? | 5/5 | 5/5 | 2/5 | 193.0s |  Succès |
| 9 | Que propose le Pôle SAPS ? | 5/5 | 4/5 | 5/5 | 58.4s |  Succès |
| 10 | - Qu’est-ce qu’une invention ? | 5/5 | 1/5 | 2/5 | 82.2s |  Succès |
| 11 | - Je souhaite répondre à un Appel à projet? | 5/5 | 3/5 | 2/5 | 80.0s |  Succès |
| 12 | je suis en arrêt de travail, qui dois-je contacter ? | 4/5 | 5/5 | 4/5 | 148.3s |  Succès |
| 13 | Combien de temps va prendre mon inscription ? | 5/5 | 5/5 | 5/5 | 90.4s |  Succès |
| 14 | Comment avoir un email ? | 5/5 | 5/5 | 5/5 | 145.1s |  Succès |
| 15 | - Je souhaite me procurer le formulaire de déclaration d’invention de l’uni... | 5/5 | 5/5 | 5/5 | 83.8s |  Succès |
| 16 | Qui contacter pour toute demande d'ouvrages en service presse ? | 2/5 | 2/5 | 2/5 | 85.8s |  Succès |
| 17 | comment enregistrer ma demande de formation hors-catalogue et quels documen... | 5/5 | 3/5 | 5/5 | 141.0s |  Succès |
| 18 | Mon jury de thèse est-il valide ? | 5/5 | 4/5 | 5/5 | 140.4s |  Succès |
| 19 | quels types de financement de thèse existent ? | 5/5 | 5/5 | 5/5 | 86.3s |  Succès |
| 20 | - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autr... | 4/5 | 5/5 | 4/5 | 82.4s |  Succès |
| 21 | Je souhaite monter un projet, comment faire ? | 5/5 | 4/5 | 4/5 | 91.4s |  Succès |
| 22 | - Comment protéger un savoir-faire ? | 5/5 | 4/5 | 5/5 | 85.2s |  Succès |
| 23 | Je pars en mission, quelle pièce dois-je remplir ? | 5/5 | 5/5 | 5/5 | 86.4s |  Succès |
| 24 | Quel est le délai moyen entre la soumission d’un manuscrit et sa publicatio... | 1/5 | 1/5 | 2/5 | 134.5s |  Succès |

---
*Rapport généré automatiquement par `Test/run_queries_ragilaas.py`.*