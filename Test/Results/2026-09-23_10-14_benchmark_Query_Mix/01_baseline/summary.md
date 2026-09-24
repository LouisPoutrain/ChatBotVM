# Rapport d'Évaluation RAG - Query_Mix.txt

- **Date :** 2026-09-23T10:59:32.116853
- **Requêtes évaluées :** 23/24
- **Modèles :** Draft: `mistral-medium-latest` | Réponse: `mistral-medium-latest` | Juge: `gpt-oss-120b`
- **Temps d'exécution :** Total RAG: 2443.0s (moy. 101.8s/q) | Évaluation: 264.2s

## Scores Moyens (sur 5.0)

| Métrique | Score Moyen | Description |
|:---|:---:|:---|
| **Faithfulness** | **4.52 / 5** | Fidélité aux documents sources (absence d'hallucination) |
| **Answer Relevance** | **3.39 / 5** | Pertinence de la réponse par rapport à la question |
| **Context Precision** | **4.30 / 5** | Précision des passages extraits par le RAG |
| **Completeness** | **3.00 / 5** | Exhaustivité de la réponse fournie |
| **Conciseness** | **4.74 / 5** | Clarté et concision du texte |
| **Score Global Moyen** | **3.99 / 5** | Moyenne des 5 critères |

## Tableau Récapitulatif par Question

| # | Question | Fidélité | Pertinence | Précision | Durée | Statut |
|---|---|:---:|:---:|:---:|:---:|:---:|
| 1 | C’est quoi les SAPS ? | 5/5 | 5/5 | 5/5 | 64.2s |  Succès |
| 2 | Comment peut-on changer le budget d’un projet ? | 5/5 | 5/5 | 5/5 | 117.5s |  Succès |
| 3 | Quelles sont les différentes démarches à effectuer ? | 5/5 | 1/5 | 5/5 | 91.2s |  Succès |
| 4 | - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire ... | -/5 | -/5 | -/5 | 149.9s | ⚠️ Erreur Juge |
| 5 | A quelle adresse postale ou mail dois-je envoyer mon projet ? | 1/5 | 1/5 | 3/5 | 89.8s |  Succès |
| 6 | Comment m’inscrire / me réinscrire ? | 5/5 | 5/5 | 5/5 | 90.5s |  Succès |
| 7 | Quelles ressources le Pôle SAPS peut m’apporter ? | 5/5 | 4/5 | 5/5 | 70.2s |  Succès |
| 8 | Y a-t-il des alumni ? | 1/5 | 1/5 | 1/5 | 196.7s |  Succès |
| 9 | Que propose le Pôle SAPS ? | 5/5 | 5/5 | 5/5 | 67.0s |  Succès |
| 10 | - Qu’est-ce qu’une invention ? | 5/5 | 1/5 | 4/5 | 91.0s |  Succès |
| 11 | - Je souhaite répondre à un Appel à projet? | 5/5 | 5/5 | 5/5 | 152.9s |  Succès |
| 12 | je suis en arrêt de travail, qui dois-je contacter ? | 5/5 | 3/5 | 4/5 | 89.0s |  Succès |
| 13 | Combien de temps va prendre mon inscription ? | 4/5 | 2/5 | 3/5 | 93.0s |  Succès |
| 14 | Comment avoir un email ? | 3/5 | 5/5 | 5/5 | 87.7s |  Succès |
| 15 | - Je souhaite me procurer le formulaire de déclaration d’invention de l’uni... | 5/5 | 5/5 | 5/5 | 90.2s |  Succès |
| 16 | Qui contacter pour toute demande d'ouvrages en service presse ? | 5/5 | 1/5 | 1/5 | 86.0s |  Succès |
| 17 | comment enregistrer ma demande de formation hors-catalogue et quels documen... | 5/5 | 4/5 | 5/5 | 95.1s |  Succès |
| 18 | Mon jury de thèse est-il valide ? | 5/5 | 3/5 | 5/5 | 89.7s |  Succès |
| 19 | quels types de financement de thèse existent ? | 5/5 | 5/5 | 5/5 | 90.3s |  Succès |
| 20 | - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autr... | 5/5 | 5/5 | 5/5 | 99.5s |  Succès |
| 21 | Je souhaite monter un projet, comment faire ? | 5/5 | 3/5 | 5/5 | 102.0s |  Succès |
| 22 | - Comment protéger un savoir-faire ? | 5/5 | 3/5 | 5/5 | 97.3s |  Succès |
| 23 | Je pars en mission, quelle pièce dois-je remplir ? | 5/5 | 5/5 | 5/5 | 97.6s |  Succès |
| 24 | Quel est le délai moyen entre la soumission d’un manuscrit et sa publicatio... | 5/5 | 1/5 | 3/5 | 145.0s |  Succès |

---
*Rapport généré automatiquement par `Test/run_queries_ragilaas.py`.*