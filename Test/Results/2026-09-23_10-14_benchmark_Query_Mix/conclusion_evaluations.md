# Bilan des Évaluations (LLM as a Judge)

## Moyennes Globales

- **Faithfulness** : 4.59 / 5
- **Answer Relevance** : 3.90 / 5
- **Context Precision** : 4.03 / 5
- *Nombre de réponses évaluées avec succès : 210*
- **Temps moyen RAG** : 95.16s
- **Temps moyen Évaluation** : 9.85s
- **Temps moyen Total** : 105.00s
- **Tokens moyens générés** : 0
- *Nombre total de requêtes chronométrées : 240*

## 📊 Tableau Comparatif des Configurations

| Configuration / Modèle | Faithfulness | Relevance | Context Precision | RAG (s) | Eval (s) | Total (s) | Tokens Moy. | Évaluations |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **01_baseline** | 4.52 / 5 | 3.39 / 5 | 4.30 / 5 | 101.79s | 11.01s | 112.80s | 0 | 23 |
| **02_fast_draft** | 4.43 / 5 | 4.43 / 5 | 4.86 / 5 | 88.68s | 3.13s | 91.82s | 0 | 7 |
| **03_max_quality** | 4.79 / 5 | 3.88 / 5 | 3.42 / 5 | 86.07s | 12.15s | 98.22s | 0 | 24 |
| **04_meta_mono** | 3.96 / 5 | 4.04 / 5 | 3.52 / 5 | 87.10s | 10.85s | 97.96s | 0 | 23 |
| **05_mistral_stack** | 4.75 / 5 | 4.25 / 5 | 4.38 / 5 | 97.58s | 12.14s | 109.73s | 0 | 24 |
| **06_google_mono** | 4.70 / 5 | 4.09 / 5 | 3.87 / 5 | 102.27s | 11.27s | 113.54s | 0 | 23 |
| **07_qwen_mono** | 4.58 / 5 | 4.08 / 5 | 4.08 / 5 | 102.16s | 11.25s | 113.41s | 0 | 24 |
| **08_economy_cross** | 4.91 / 5 | 4.00 / 5 | 4.30 / 5 | 103.45s | 11.07s | 114.52s | 0 | 23 |
| **09_premium_cross** | 4.58 / 5 | 3.67 / 5 | 4.04 / 5 | 95.73s | 10.33s | 106.07s | 0 | 24 |
| **10_mid_draft** | 4.47 / 5 | 3.40 / 5 | 4.20 / 5 | 86.73s | 5.24s | 91.98s | 0 | 15 |

## Détails par Configuration

### Configuration : 01_baseline
- Moyenne Faithfulness : 4.52 / 5
- Moyenne Answer Relevance : 3.39 / 5
- Moyenne Context Precision : 4.30 / 5
- *Évaluations réussies : 23*
- Temps moyen RAG : 101.79s
- Temps moyen Évaluation : 11.01s
- Temps moyen Total : 112.80s
- Tokens moyens générés : 0

### Configuration : 02_fast_draft
- Moyenne Faithfulness : 4.43 / 5
- Moyenne Answer Relevance : 4.43 / 5
- Moyenne Context Precision : 4.86 / 5
- *Évaluations réussies : 7*
- Temps moyen RAG : 88.68s
- Temps moyen Évaluation : 3.13s
- Temps moyen Total : 91.82s
- Tokens moyens générés : 0

### Configuration : 03_max_quality
- Moyenne Faithfulness : 4.79 / 5
- Moyenne Answer Relevance : 3.88 / 5
- Moyenne Context Precision : 3.42 / 5
- *Évaluations réussies : 24*
- Temps moyen RAG : 86.07s
- Temps moyen Évaluation : 12.15s
- Temps moyen Total : 98.22s
- Tokens moyens générés : 0

### Configuration : 04_meta_mono
- Moyenne Faithfulness : 3.96 / 5
- Moyenne Answer Relevance : 4.04 / 5
- Moyenne Context Precision : 3.52 / 5
- *Évaluations réussies : 23*
- Temps moyen RAG : 87.10s
- Temps moyen Évaluation : 10.85s
- Temps moyen Total : 97.96s
- Tokens moyens générés : 0

### Configuration : 05_mistral_stack
- Moyenne Faithfulness : 4.75 / 5
- Moyenne Answer Relevance : 4.25 / 5
- Moyenne Context Precision : 4.38 / 5
- *Évaluations réussies : 24*
- Temps moyen RAG : 97.58s
- Temps moyen Évaluation : 12.14s
- Temps moyen Total : 109.73s
- Tokens moyens générés : 0

### Configuration : 06_google_mono
- Moyenne Faithfulness : 4.70 / 5
- Moyenne Answer Relevance : 4.09 / 5
- Moyenne Context Precision : 3.87 / 5
- *Évaluations réussies : 23*
- Temps moyen RAG : 102.27s
- Temps moyen Évaluation : 11.27s
- Temps moyen Total : 113.54s
- Tokens moyens générés : 0

### Configuration : 07_qwen_mono
- Moyenne Faithfulness : 4.58 / 5
- Moyenne Answer Relevance : 4.08 / 5
- Moyenne Context Precision : 4.08 / 5
- *Évaluations réussies : 24*
- Temps moyen RAG : 102.16s
- Temps moyen Évaluation : 11.25s
- Temps moyen Total : 113.41s
- Tokens moyens générés : 0

### Configuration : 08_economy_cross
- Moyenne Faithfulness : 4.91 / 5
- Moyenne Answer Relevance : 4.00 / 5
- Moyenne Context Precision : 4.30 / 5
- *Évaluations réussies : 23*
- Temps moyen RAG : 103.45s
- Temps moyen Évaluation : 11.07s
- Temps moyen Total : 114.52s
- Tokens moyens générés : 0

### Configuration : 09_premium_cross
- Moyenne Faithfulness : 4.58 / 5
- Moyenne Answer Relevance : 3.67 / 5
- Moyenne Context Precision : 4.04 / 5
- *Évaluations réussies : 24*
- Temps moyen RAG : 95.73s
- Temps moyen Évaluation : 10.33s
- Temps moyen Total : 106.07s
- Tokens moyens générés : 0

### Configuration : 10_mid_draft
- Moyenne Faithfulness : 4.47 / 5
- Moyenne Answer Relevance : 3.40 / 5
- Moyenne Context Precision : 4.20 / 5
- *Évaluations réussies : 15*
- Temps moyen RAG : 86.73s
- Temps moyen Évaluation : 5.24s
- Temps moyen Total : 91.98s
- Tokens moyens générés : 0

---
## Détails des évaluations (Notes et Commentaires du Juge)

## 01_baseline

### Question : C’est quoi les SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 64.22s, Eval: 12.32s, Total: 76.54s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : le sigle SAPS signifie Sciences Avec et Pour la Société, il s’inscrit dans le cadre de la loi LPR 2021, et son objectif est de renforcer le dialogue entre chercheurs et citoyens via médiation, co‑construction de projets et organisation d’événements. L’URL saps.univ‑tours.fr apparaît également dans le contexte. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question « C’est quoi les SAPS ? » en donnant une définition claire et concise du dispositif, ce qui correspond parfaitement à la demande.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires pour répondre à la question (définition, cadre législatif, objectifs, activités). Il a été exploité de façon adéquate.

### Question : Comment peut-on changer le budget d’un projet ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 117.45s, Eval: 16.05s, Total: 133.50s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement tirées du contexte : le texte indique que toute demande de modification budgétaire doit passer par le SPIV, qu’il faut fournir un argumentaire scientifique et un budget modifié validé par l’antenne financière. Aucun élément n’est inventé. Le contact ajouté n’est pas pénalisé selon la règle d’exemption des contacts.
- **Avis Answer Relevance** : La réponse répond exactement à la question en expliquant la procédure à suivre pour changer le budget d’un projet, sans digression.
- **Avis Context Precision** : Le contexte fourni contient la section « Gérer les aléas (demande d’avenant ou de modification) » qui décrit la procédure de modification budgétaire, ce qui est exactement l’information requise.

### Question : Quelles sont les différentes démarches à effectuer ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 91.21s, Eval: 12.43s, Total: 103.64s
- **Tokens générés** : 0
- **Avis Faithfulness** : Aucune affirmation n'est présentée dans la réponse, donc aucune information n'est en contradiction avec le contexte. L'absence de contenu implique que la réponse ne peut pas contenir d'hallucination, ce qui justifie le score maximal.
- **Avis Answer Relevance** : La question demande « Quelles sont les différentes démarches à effectuer ? » mais la réponse ne fournit aucune information, ne répond donc pas du tout à la demande.
- **Avis Context Precision** : Le contexte récupéré décrit en détail les démarches à suivre pour la soutenance de thèse (pièces justificatives, validations par les différentes directions, dépôt du PDF, etc.). Il contient donc toutes les informations nécessaires pour répondre à la question.

### Question : - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire extérieur? Est-ce gratuit?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 149.86s, Eval: 0.00s, Total: 149.86s
- **Tokens générés** : 0

### Question : A quelle adresse postale ou mail dois-je envoyer mon projet ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 1.0/5, Context Precision: 3.0/5
- **Temps** : RAG: 89.75s, Eval: 11.56s, Total: 101.31s
- **Tokens générés** : 0
- **Avis Faithfulness** : Aucune réponse n'a été fournie, il n'y a donc aucune affirmation à vérifier par rapport au contexte. L'absence de contenu ne constitue pas une hallucination, mais la note la plus basse reflète le manque total d'information.
- **Avis Answer Relevance** : La question demande l'adresse postale ou mail pour envoyer le projet. Aucun élément de réponse n'est présent, donc la pertinence est nulle.
- **Avis Context Precision** : Le contexte contient plusieurs adresses e‑mail (laura.guillet@insa-clv.fr, cotutelles@univ-orleans.fr, lucie.primault@univ-tours.fr) ainsi que des indications générales de contact, mais il ne précise pas explicitement l'adresse à utiliser pour l'envoi du projet. Le contexte est donc partiellement utile, d'où une note moyenne.

### Question : Comment m’inscrire / me réinscrire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 90.47s, Eval: 12.54s, Total: 103.01s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement tirées du contexte : création d'un compte ADUM, dépôt des pièces en un seul PDF, validation de la Charte du doctorat, transmission du dossier aux différents validateurs, mise à jour des informations, dépôt de la Convention Individuelle de Formation, documents (photo, CV, rapport d'activité) et respect de la date limite du 15 novembre. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question « Comment m’inscrire / me réinscrire ? » en donnant les étapes concrètes pour l’inscription initiale et la réinscription, sans digression.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires (procédure ADUM, documents requis, validation de la charte, chaîne de validation, date limite). Le système a extrait les parties pertinentes.

### Question : Quelles ressources le Pôle SAPS peut m’apporter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 70.15s, Eval: 16.77s, Total: 86.92s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse se retrouvent dans le contexte : le pôle propose un accompagnement personnalisé (conseil, montage de projets, médiation scientifique), des formations comme le mediatraining et le concours « Ma Thèse en 180 s », ainsi qu’un soutien pour des événements ou projets arts/sciences. L’adresse e‑mail fournie figure également dans la section CONTACTS du contexte. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond directement à la question en listant les principales ressources offertes par le Pôle SAPS. Elle reste centrée sur le sujet, même si elle ne détaille pas l’ensemble des services disponibles.
- **Avis Context Precision** : Le contexte récupéré contient une description très détaillée des missions du Pôle SAPS (réponses aux sollicitations, organisation d’événements, accompagnement de projets, formations, projets arts/sciences, label, etc.). Il est donc parfaitement adapté pour répondre à la question.

### Question : Y a-t-il des alumni ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 1.0/5, Context Precision: 1.0/5
- **Temps** : RAG: 196.69s, Eval: 10.18s, Total: 206.87s
- **Tokens générés** : 0
- **Avis Faithfulness** : Aucune réponse n'a été fournie. Par conséquent, il n'y a aucune affirmation à vérifier par rapport au contexte, ce qui conduit à la note minimale de 1.
- **Avis Answer Relevance** : La question porte sur l'existence d'alumni. Le système n'a fourni aucune information, donc il ne répond pas du tout à la question.
- **Avis Context Precision** : Le contexte récupéré ne contient aucune information relative aux alumni ; il traite de la liberté d'expression, d'association, de procédures de domiciliation, etc. Ainsi le contexte n'est pas pertinent pour la question, justifiant la note 1.

### Question : Que propose le Pôle SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 66.95s, Eval: 11.74s, Total: 78.69s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (médiation, événements comme DéTours des sciences, Ma thèse en 180 secondes, Fête de la science, formations mediatraining, accompagnement des chercheurs, aide au dépôt de projets ANR/européens, montage budgétaire, projets arts/sciences Kaléidoscope et Ma thèse en BD) sont directement présentes dans le contexte. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question « Que propose le Pôle SAPS ? » en listant les services et activités proposés. Aucun hors‑sujet n’est introduit.
- **Avis Context Precision** : Le contexte fourni contient une description détaillée des missions, des événements, des formations, de l’accompagnement et des projets collaboratifs du Pôle SAPS, ce qui est suffisant pour répondre à la question.

### Question : - Qu’est-ce qu’une invention ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 4.0/5
- **Temps** : RAG: 90.96s, Eval: 13.32s, Total: 104.28s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient aucune affirmation factuelle sur le sujet de la question, seulement une information de contact. Selon la règle, les contacts ajoutés ne sont pas pénalisés. Ainsi aucune hallucination n'est détectée, ce qui justifie le score maximal.
- **Avis Answer Relevance** : La question porte sur la définition d’une invention, alors que la réponse ne fournit qu’une adresse de contact. Aucun élément de la réponse ne répond à la demande, d’où le score le plus bas.
- **Avis Context Precision** : Le contexte récupéré traite en détail du régime juridique des inventions et mentionne les notions d’invention, d’inventeur et de brevetabilité. Il contient donc les informations nécessaires pour répondre à la question, même s’il ne donne pas une définition concise. Le contexte est donc pertinent, mais légèrement incomplet pour une définition directe, d’où un 4.

### Question : - Je souhaite répondre à un Appel à projet?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 152.86s, Eval: 12.18s, Total: 165.04s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les informations fournies (contact de Mme Caroline Vaslin, adresse e‑mail, format PDF unique de max 5 Mo, pièces à fournir : fiche d'identité, éléments financiers, dossier scientifique, date limite du 2 avril 2026, lien vers l’appel) sont directement présentes dans le contexte. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la demande « Je souhaite répondre à un Appel à projet ? » en indiquant comment procéder, à qui s’adresser et quelles pièces fournir, ainsi que la date limite. Aucun hors‑sujet n’est présent.
- **Avis Context Precision** : Le contexte récupéré contient toutes les informations nécessaires pour répondre à la question : appel à projets 2026, coordonnées, exigences de dépôt, format, taille maximale, etc. Le contexte est donc parfaitement ciblé.

### Question : je suis en arrêt de travail, qui dois-je contacter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 3.0/5, Context Precision: 4.0/5
- **Temps** : RAG: 89.01s, Eval: 12.67s, Total: 101.68s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement tirées du contexte : les deux liens vers les pages « Congés maladie des agents titulaires » et « Congés maladie des agents contractuels » existent bien dans la section « Congés maladie » du contexte. Aucun élément supplémentaire n’a été inventé.
- **Avis Answer Relevance** : La question demande explicitement « qui dois‑je contacter ? ». La réponse indique seulement où consulter les procédures via des liens, sans fournir de nom, service ou coordonnées de contact. Elle touche au sujet mais ne répond pas pleinement à la demande, d’où une note moyenne.
- **Avis Context Precision** : Le contexte contient les liens pertinents relatifs aux congés maladie, ce qui permet de répondre à la question en orientant l’utilisateur. Cependant, le contexte ne fournit pas de contact direct (nom, e‑mail, téléphone) pour la gestion d’un arrêt de travail, ce qui limite la précision du contexte pour la question posée.

### Question : Combien de temps va prendre mon inscription ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 2.0/5, Context Precision: 3.0/5
- **Temps** : RAG: 92.96s, Eval: 11.92s, Total: 104.88s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient aucune affirmation factuelle qui contredit le contexte. Elle se contente de recommander de contacter une personne, ce qui n'est pas explicitement présent dans le contexte mais les règles précisent de ne pas pénaliser les informations de contact. Aucun élément factuel inventé n'est présent, d'où une note élevée (4).
- **Avis Answer Relevance** : La question demande le délai d'inscription. La réponse ne fournit pas de durée ni d'estimation, elle se contente de rediriger vers un contact. Elle ne répond donc pas directement à la question, ce qui justifie une note basse (2).
- **Avis Context Precision** : Le contexte contient des informations pertinentes (date limite du 15 novembre, mention de délais de traitement plus longs pour certains dossiers, étapes de validation). Cependant, il ne donne pas de durée précise, et la réponse n'exploite aucune de ces informations. Le contexte est donc partiellement utile, d'où une note moyenne (3).

### Question : Comment avoir un email ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 87.67s, Eval: 11.83s, Total: 99.50s
- **Tokens générés** : 0
- **Avis Faithfulness** : Le texte indique que le doctorant dispose d'un compte sur le domaine etu.univ-tours.fr, ce qui est présent dans le contexte. Cependant, le format exact "prénom.nom@etu.univ-tours.fr" n'est pas explicitement mentionné dans le contexte ; il s'agit d'une inférence raisonnable mais non citée, d'où la note 3.
- **Avis Answer Relevance** : La réponse répond directement à la question « Comment avoir un email ? » en expliquant que le compte email est attribué automatiquement à l'inscription du doctorant, ce qui correspond à la demande.
- **Avis Context Precision** : Le contexte contient l'information clé que les doctorants de l'Université de Tours reçoivent un compte étudiant sur le domaine etu.univ-tours.fr, ce qui suffit pour répondre à la question.

### Question : - Je souhaite me procurer le formulaire de déclaration d’invention de l’université, à qui dois-je m’adresser ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 90.25s, Eval: 8.47s, Total: 98.72s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les informations fournies (contact du Pôle Juridique Recherche via l'adresse drv-pi@univ-tours.fr) sont présentes dans le contexte. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse indique clairement à qui s'adresser pour obtenir le formulaire, répondant directement à la question "à qui dois-je m’adresser ?".
- **Avis Context Precision** : Le contexte contient l'adresse e‑mail générique drv-pi@univ-tours.fr ainsi que d'autres contacts pertinents, ce qui est suffisant pour répondre à la demande.

### Question : Qui contacter pour toute demande d'ouvrages en service presse ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 1.0/5
- **Temps** : RAG: 86.03s, Eval: 7.19s, Total: 93.22s
- **Tokens générés** : 0
- **Avis Faithfulness** : Aucune affirmation n'est présentée dans la réponse, il n'y a donc aucune information qui puisse être en contradiction avec le contexte. L'absence de contenu empêche toute hallucination, ce qui justifie le score maximal de fidélité.
- **Avis Answer Relevance** : La question demande explicitement « Qui contacter pour toute demande d'ouvrages en service presse ? ». La réponse ne fournit aucun nom, numéro ou adresse e‑mail, ne répond donc pas du tout à la demande.
- **Avis Context Precision** : Le contexte fourni ne contient aucune référence à un « service presse » ni à des contacts liés aux demandes d'ouvrages. Il s'agit principalement d'informations sur les services doctoraux et des contacts universitaires, donc le contexte n'est pas pertinent pour la question.

### Question : comment enregistrer ma demande de formation hors-catalogue et quels documents dois-je fournir ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 95.08s, Eval: 14.00s, Total: 109.08s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (déposer le dossier sur ADUM, rubrique « Déclaration des formations hors catalogue », fichier PDF unique contenant la fiche de validation et les justificatifs) sont directement présentes dans le contexte. Le seul élément ajouté est un contact (Lucie PRIMAULT), mais les consignes indiquent de ne pas pénaliser les contacts injectés.
- **Avis Answer Relevance** : La réponse indique clairement comment enregistrer la demande et quels documents fournir (fiche de validation + justificatifs). Elle ne détaille pas la nature exacte des justificatifs, mais le contexte ne les spécifie pas non plus pour les formations hors catalogue, ce qui rend la réponse globalement pertinente.
- **Avis Context Precision** : Le contexte contient précisément les instructions nécessaires : utilisation d'ADUM, rubrique spécifique, dépôt d'un seul PDF, inclusion de la fiche de validation et des justificatifs. Le contexte est donc parfaitement ciblé.

### Question : Mon jury de thèse est-il valide ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 3.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 89.65s, Eval: 10.26s, Total: 99.91s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations du système (règles de composition du jury, nombre de membres, exigences de moitié de professeurs, extérieurs, HDR, etc.) sont directement tirées du contexte fourni. Aucun élément factuel n'est inventé. Le seul ajout concerne un contact (nom et e‑mail) qui n'apparaît pas dans le contexte, mais les consignes précisent de ne pas pénaliser les contacts pour la fidélité.
- **Avis Answer Relevance** : La question demandait de savoir si le jury est valide. La réponse indique qu’il faut fournir la composition exacte du jury pour pouvoir l’évaluer. Cela répond partiellement à la demande en expliquant ce qui manque, mais ne donne pas d’évaluation concrète du jury actuel, donc la pertinence est moyenne.
- **Avis Context Precision** : Le contexte contient l’ensemble des règles nécessaires pour juger la validité d’un jury (nombre de membres, répartition des professeurs, extérieurs, HDR, etc.). Ainsi le contexte est pleinement pertinent et complet pour répondre à la question si la composition était connue.

### Question : quels types de financement de thèse existent ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 90.33s, Eval: 11.19s, Total: 101.52s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : contrat doctoral, bourses régionales et départementales, ANR, Europe, Labex, convention CIFRE, contrats de recherche/entreprise (DGA, ADEME), bourses industrielles, bourses associatives, financements étrangers, co‑financements régionaux, bourses Rabelaisiennes, bourses présidentielles et statut salarié. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La question porte sur les types de financement de thèse. La réponse fournit une liste claire et exhaustive de ces types, répondant exactement à la demande.
- **Avis Context Precision** : Le contexte récupéré contient l’ensemble des catégories de financement mentionnées dans la réponse. Il est donc parfaitement adapté pour répondre à la question.

### Question : - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autre CHRU?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 99.48s, Eval: 8.91s, Total: 108.39s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement tirées du contexte fourni : le format en deux lignes (ligne 1 avec les tutelles de l'unité, ligne 2 avec CHRU de Tours, Service, 37XXX Tours) apparaît dans les exemples de signatures du contexte. Aucun élément n'est inventé. Le contact ajouté n'est pas pénalisé selon la règle sur les contacts injectés.
- **Avis Answer Relevance** : La question porte sur la manière de procéder avec des échantillons du CHRU de Tours ou d'un autre CHRU. La réponse donne précisément le format de signature à utiliser, ce qui répond directement à la demande.
- **Avis Context Precision** : Le contexte récupéré contient les règles de rédaction des signatures pour le personnel hospitalo‑universitaire du CHRU de Tours, y compris les deux lignes d'affiliation. Il est donc parfaitement pertinent.

### Question : Je souhaite monter un projet, comment faire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 3.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 102.05s, Eval: 10.31s, Total: 112.36s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont soit présentes dans le contexte (l'adresse projets-etablissement@univ-tours.fr), soit concernent des informations de contact. Selon la règle, les contacts absents du contexte ne sont pas pénalisés, donc aucune hallucination n'est comptée.
- **Avis Answer Relevance** : La réponse donne une première étape concrète (envoyer la saisine) et propose un contact pour l'accompagnement, ce qui répond partiellement à la question « comment monter un projet ». Cependant, elle ne détaille pas les étapes supplémentaires décrites dans le contexte (accord du président, COPIL, constitution du dossier, rôle du coordinateur/chef de projet, etc.), ce qui limite sa pertinence globale.
- **Avis Context Precision** : Le contexte récupéré contient l'adresse e‑mail nécessaire ainsi que l’ensemble du processus de montage de projet. Il est donc pleinement pertinent pour répondre à la question.

### Question : - Comment protéger un savoir-faire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 3.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 97.28s, Eval: 7.79s, Total: 105.07s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les informations fournies dans la réponse (contact du PJR, adresse e‑mail drv-pi@univ-tours.fr) figurent exactement dans le contexte. Aucun élément n’est inventé, y compris les contacts qui sont explicitement autorisés à ne pas être pénalisés.
- **Avis Answer Relevance** : La réponse indique une démarche (contacter le PJR) qui est pertinente pour la protection du savoir‑faire, mais elle ne décrit pas les mécanismes concrets (accords de confidentialité, conventions, etc.) attendus par la question. Elle répond donc partiellement.
- **Avis Context Precision** : Le contexte récupéré contient à la fois les informations de contact du PJR et de nombreux éléments relatifs à la protection du savoir‑faire (accords de confidentialité, conventions, procédures). Il est donc pleinement pertinent pour répondre à la question.

### Question : Je pars en mission, quelle pièce dois-je remplir ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 97.59s, Eval: 10.37s, Total: 107.96s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : le formulaire s’appelle « AUTORISATION DE DEPLACEMENT », il doit être transmis au gestionnaire ou à l’antenne financière au moins 15 jours avant le départ (texte « A transmettre à votre gestionnaire ou antenne financière 15 jours minimum avant le départ en mission »), et il faut joindre une copie de la carte grise en cas d’usage d’un véhicule personnel (phrase « Joindre une copie de la carte grise »). Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question « quelle pièce dois‑je remplir ? » en indiquant le formulaire à remplir et en rappelant les pièces annexes éventuelles, sans digression hors sujet.
- **Avis Context Precision** : Le contexte récupéré contient le titre du formulaire, les modalités de transmission et la mention de la carte grise, soit l’ensemble des informations nécessaires pour répondre à la question.

### Question : Quel est le délai moyen entre la soumission d’un manuscrit et sa publication ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 3.0/5
- **Temps** : RAG: 145.04s, Eval: 10.21s, Total: 155.25s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient aucune affirmation factuelle sur le délai de publication. Le seul élément ajouté (coordonnées de contact) n'est pas présent dans le contexte, mais la règle indique de ne pas pénaliser les informations de contact. Ainsi aucune hallucination n'est détectée, ce qui justifie le score maximal.
- **Avis Answer Relevance** : La question porte sur le délai moyen entre la soumission d’un manuscrit et sa publication. La réponse fournie ne répond pas du tout à cette interrogation et ne fournit aucune information pertinente, d'où le score le plus bas.
- **Avis Context Precision** : Le contexte mentionne un « délai au maximum de six mois » (sciences, technique, médecine) et « douze mois » (sciences humaines et sociales) concernant la mise à disposition ouverte d’un manuscrit après publication. Ces informations sont liées aux délais, mais elles ne correspondent pas au délai moyen de soumission à publication demandé. Le contexte est donc partiellement utile, mais ne fournit pas la donnée exacte recherchée.

## 02_fast_draft

### Question : C’est quoi les SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 62.43s, Eval: 12.96s, Total: 75.39s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : le sigle SAPS signifie « Sciences Avec et Pour la Société », il s’inscrit dans le cadre de la loi LPR 2021, son objectif est de renforcer le dialogue entre chercheurs et citoyens, via médiation, événements (ex. Village des sciences) et accompagnement de projets participatifs. Le lien saps.univ-tours.fr apparaît également dans le contexte. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La question « C’est quoi les SAPS ? » attend une définition. La réponse fournit exactement cette définition ainsi que la mission principale, répondant ainsi pleinement à la demande.
- **Avis Context Precision** : Le contexte récupéré contient la définition, les objectifs, le cadre législatif et des exemples d’actions des SAPS. Il est donc parfaitement adapté pour répondre à la question.

### Question : Comment peut-on changer le budget d’un projet ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 114.37s, Eval: 13.22s, Total: 127.59s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations (passer par le SPIV, fournir un argumentaire scientifique, fournir un budget modifié validé par l'Antenne Financière, attendre le retour du financeur) sont directement tirées du contexte. Le seul élément ajouté est le contact "Anne Galopin : af.polytech@univ-tours.fr", qui est un contact injecté et ne pénalise pas la fidélité selon les règles.
- **Avis Answer Relevance** : La réponse répond exactement à la question « Comment peut-on changer le budget d’un projet ? » en décrivant la procédure à suivre. Aucun élément hors sujet n'est présent.
- **Avis Context Precision** : Le contexte contient une section dédiée à la gestion des aléas et aux demandes de modification budgétaire, qui fournit toutes les informations nécessaires. Le système a correctement exploité cette partie.

### Question : Quelles sont les différentes démarches à effectuer ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 1.0/5, Context Precision: 4.0/5
- **Temps** : RAG: 94.51s, Eval: 7.97s, Total: 102.48s
- **Tokens générés** : 0
- **Avis Faithfulness** : Aucune réponse n'a été fournie par le système, il n'est donc pas possible de vérifier la fidélité à un texte. En l'absence de contenu, on considère que la réponse ne s'appuie sur aucun élément du contexte, ce qui correspond à la note minimale.
- **Avis Answer Relevance** : La question "Quelles sont les différentes démarches à effectuer ?" n'a reçu aucune réponse. Par conséquent, la réponse ne traite pas du tout de la demande, justifiant la note la plus basse.
- **Avis Context Precision** : Le contexte récupéré contient de nombreuses informations susceptibles de répondre à la question (ex. démarches RGPD, procédures d'embauche, étapes de mobilité, programme PAUSE, etc.). Le contexte est donc pertinent et assez complet, même s'il ne cible pas une seule procédure précise, d'où une note élevée mais pas parfaite.

### Question : - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire extérieur? Est-ce gratuit?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 167.01s, Eval: 10.15s, Total: 177.16s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : le cadre de "contrat de collaboration de recherche" est décrit, le dispositif CIFRE est mentionné, les frais de structure (ex : 20 % des recettes externes) apparaissent dans le tableau du contexte, et les coordonnées d'Hélène Jullien sont listées. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question en indiquant le cadre approprié pour des expérimentations avec un partenaire extérieur et en précisant que ce n'est pas gratuit, avec un exemple de frais applicables.
- **Avis Context Precision** : Le contexte récupéré contient toutes les informations nécessaires : description des contrats de recherche collaboratifs, mention du dispositif CIFRE, détails sur les frais de structure, et contacts des interlocuteurs. Il est donc parfaitement ciblé.

### Question : A quelle adresse postale ou mail dois-je envoyer mon projet ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 87.19s, Eval: 10.03s, Total: 97.22s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les informations fournies (l'adresse e‑mail de Morgane Guibert) sont présentes dans le contexte. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse donne une adresse e‑mail à laquelle l'utilisateur peut envoyer son projet, ce qui répond directement à la question qui demandait une adresse postale ou mail.
- **Avis Context Precision** : Le contexte contient plusieurs adresses e‑mail, dont celle de Morgane Guibert, ainsi que d'autres contacts pertinents. Le contexte est donc pleinement pertinent pour répondre à la question.

### Question : Comment m’inscrire / me réinscrire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 90.39s, Eval: 8.11s, Total: 98.50s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (connexion à ADUM, suivi du tutoriel, dépôt de la Convention Individuelle de Formation, photo, CV, rapport d’avancement, date limite du 15 novembre) sont directement présentes dans le contexte. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond directement à la question « Comment m’inscrire / me réinscrire ? » en donnant les étapes essentielles pour la réinscription, sans digression.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires sur la procédure de réinscription, le site ADUM, les documents requis et la date limite, ce qui le rend parfaitement adapté.

### Question : Quelles ressources le Pôle SAPS peut m’apporter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 65.50s, Eval: 12.78s, Total: 78.28s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (accompagnement, formations, organisation d'événements, mise à disposition de matériel, soutien aux projets arts/sciences) sont directement présentes dans le contexte (slides 5‑9, 10, 7). Aucun élément n'est inventé ; le lien fourni figure également dans le contexte.
- **Avis Answer Relevance** : La réponse répond exactement à la question en listant les ressources que le Pôle SAPS peut offrir à un chercheur. Aucun hors‑sujet n'est introduit.
- **Avis Context Precision** : Le contexte récupéré contient l’ensemble des informations nécessaires : missions du pôle, types d’accompagnement, catalogue de formations, exemples d’événements et de projets arts/sciences, ainsi que les contacts. Il est donc parfaitement ciblé.

### Question : Y a-t-il des alumni ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 118.96s, Eval: 0.00s, Total: 118.96s
- **Tokens générés** : 0

### Question : Que propose le Pôle SAPS ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 56.34s, Eval: 0.00s, Total: 56.34s
- **Tokens générés** : 0

### Question : - Qu’est-ce qu’une invention ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 81.16s, Eval: 0.00s, Total: 81.16s
- **Tokens générés** : 0

### Question : - Je souhaite répondre à un Appel à projet?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 82.13s, Eval: 0.00s, Total: 82.13s
- **Tokens générés** : 0

### Question : je suis en arrêt de travail, qui dois-je contacter ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 90.72s, Eval: 0.00s, Total: 90.72s
- **Tokens générés** : 0

### Question : Combien de temps va prendre mon inscription ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 85.38s, Eval: 0.00s, Total: 85.38s
- **Tokens générés** : 0

### Question : Comment avoir un email ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 81.31s, Eval: 0.00s, Total: 81.31s
- **Tokens générés** : 0

### Question : - Je souhaite me procurer le formulaire de déclaration d’invention de l’université, à qui dois-je m’adresser ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 82.14s, Eval: 0.00s, Total: 82.14s
- **Tokens générés** : 0

### Question : Qui contacter pour toute demande d'ouvrages en service presse ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 81.12s, Eval: 0.00s, Total: 81.12s
- **Tokens générés** : 0

### Question : comment enregistrer ma demande de formation hors-catalogue et quels documents dois-je fournir ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 88.93s, Eval: 0.00s, Total: 88.93s
- **Tokens générés** : 0

### Question : Mon jury de thèse est-il valide ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 88.27s, Eval: 0.00s, Total: 88.27s
- **Tokens générés** : 0

### Question : quels types de financement de thèse existent ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 85.96s, Eval: 0.00s, Total: 85.96s
- **Tokens générés** : 0

### Question : - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autre CHRU?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 83.16s, Eval: 0.00s, Total: 83.16s
- **Tokens générés** : 0

### Question : Je souhaite monter un projet, comment faire ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 85.42s, Eval: 0.00s, Total: 85.42s
- **Tokens générés** : 0

### Question : - Comment protéger un savoir-faire ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 83.90s, Eval: 0.00s, Total: 83.90s
- **Tokens générés** : 0

### Question : Je pars en mission, quelle pièce dois-je remplir ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 89.88s, Eval: 0.00s, Total: 89.88s
- **Tokens générés** : 0

### Question : Quel est le délai moyen entre la soumission d’un manuscrit et sa publication ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 82.19s, Eval: 0.00s, Total: 82.19s
- **Tokens générés** : 0

## 03_max_quality

### Question : C’est quoi les SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 63.60s, Eval: 17.53s, Total: 81.13s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : le sigle SAPS = Sciences Avec et Pour la Société, le rôle de rapprochement chercheurs‑public, la promotion du dialogue et de la médiation, le soutien à des projets participatifs et artistiques, les missions du pôle (répondre aux sollicitations extérieures, organiser des événements comme DéTours des sciences ou Ma thèse en 180 s) et l’accompagnement des chercheurs (conception, financement, valorisation). Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question « C’est quoi les SAPS ? » en donnant une définition claire et en précisant les principales activités du dispositif, ce qui la rend pleinement pertinente.
- **Avis Context Precision** : Le contexte fourni contient la définition des SAPS, leurs objectifs, leurs missions, ainsi que des exemples d’événements et d’accompagnement. Il est donc parfaitement adapté pour répondre à la question.

### Question : Comment peut-on changer le budget d’un projet ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 114.75s, Eval: 17.32s, Total: 132.07s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations concernant la procédure (contact du SPIV, besoin d’un argumentaire scientifique et d’un budget révisé au format du financeur, traitement par le SPIV) sont directement présentes dans le contexte. Le seul élément absent est le nom et l’e‑mail d’Anne Galopin, mais il s’agit d’une information de contact ; selon les règles, cela ne pénalise pas la fidélité.
- **Avis Answer Relevance** : La réponse répond exactement à la question en indiquant comment soumettre une modification budgétaire, quels documents fournir et à qui s’adresser, sans digression.
- **Avis Context Precision** : Le contexte fourni contient la procédure détaillée de modification budgétaire ainsi que les contacts du SPIV, ce qui est suffisant pour répondre à la question.

### Question : Quelles sont les différentes démarches à effectuer ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 2.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 87.91s, Eval: 10.42s, Total: 98.33s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les informations fournies dans la réponse (adresse e‑mail drv-pi@univ-tours.fr et l’invitation à s’adresser au service général) sont présentes dans le contexte. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La question demande « Quelles sont les différentes démarches à effectuer ? ». La réponse ne décrit aucune démarche, elle ne fournit qu’un contact générique, ce qui ne répond pas à la demande.
- **Avis Context Precision** : Le contexte contient de nombreuses informations (décrets, catégories de personnes, procédures, contacts multiples) mais ne propose pas une liste claire de démarches. Le contexte est donc partiellement utile, mais il manque les étapes précises recherchées.

### Question : - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire extérieur? Est-ce gratuit?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 97.10s, Eval: 12.45s, Total: 109.55s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement soutenues par le contexte : la nécessité d’un contrat pour les projets collaboratifs, le rôle du Service Partenariats Innovations Valorisation (SPIV) dans la négociation, et l’absence d’information sur le coût. Les coordonnées de Hélène Jullien sont des contacts injectés, donc ne sont pas pénalisées.
- **Avis Answer Relevance** : La réponse répond précisément à la question en indiquant le cadre (projet de recherche collaborative avec contrat) et en précisant que le coût n’est pas indiqué, invitant l’utilisateur à se renseigner.
- **Avis Context Precision** : Le contexte fourni contient les informations essentielles sur le besoin de contrat, le rôle du SPIV et l’absence de mention de gratuité, ce qui permet de répondre correctement à la question.

### Question : A quelle adresse postale ou mail dois-je envoyer mon projet ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 86.41s, Eval: 5.29s, Total: 91.70s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les informations fournies dans la réponse (l'adresse e‑mail drv-pi@univ-tours.fr) sont présentes dans le contexte. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond directement à la question en indiquant une adresse e‑mail où envoyer le projet, ce qui satisfait la demande d'une adresse postale ou mail.
- **Avis Context Precision** : Le contexte contient l'e‑mail générique drv-pi@univ-tours.fr, qui est exactement l'information requise. Aucun autre type d'information (par ex. adresse postale) n'est nécessaire pour répondre à la question telle qu'elle est posée.

### Question : Comment m’inscrire / me réinscrire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 90.81s, Eval: 11.10s, Total: 101.91s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (connexion à ADUM, suivi du tutoriel, période de juin à 15 novembre) sont directement présentes dans le contexte. Le contact ajouté n'est pas pénalisé selon la règle d'exemption des contacts.
- **Avis Answer Relevance** : La réponse répond exactement à la question « Comment m’inscrire / me réinscrire ? » en donnant les étapes essentielles.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires (invitation par mail, connexion ADUM, période, tutoriel) pour répondre à la question.

### Question : Quelles ressources le Pôle SAPS peut m’apporter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 62.26s, Eval: 15.74s, Total: 78.00s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (accompagnement, dépôt de projets, aide budgétaire, identification de partenaires, formations, médiatraining, préparation au concours « Ma thèse en 180 s », organisation d’événements comme DéTours des sciences, festivals, résidences artistiques) sont directement présentes dans le contexte. L’adresse e‑mail figure également dans la section CONTACTS, donc aucune hallucination.
- **Avis Answer Relevance** : La réponse répond exactement à la question « Quelles ressources le Pôle SAPS peut‑moi apporter ? » en listant les principales ressources proposées. Aucun élément hors sujet n’est ajouté.
- **Avis Context Precision** : Le contexte fourni contient l’ensemble des informations nécessaires : missions du pôle, types d’accompagnement, catalogue de formations, organisation d’événements, etc. Il est donc parfaitement ciblé.

### Question : Y a-t-il des alumni ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 1.0/5
- **Temps** : RAG: 90.14s, Eval: 5.31s, Total: 95.45s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient aucune affirmation factuelle qui ne provient pas du contexte. Le seul élément ajouté est un contact, qui selon les règles ne doit pas être pénalisé même s'il n'apparaît pas dans le contexte. Aucun autre contenu n'est halluciné.
- **Avis Answer Relevance** : La question porte sur l'existence d'alumni, alors que la réponse fournit uniquement un contact. Aucun lien avec la question n'est établi, ce qui rend la réponse hors sujet.
- **Avis Context Precision** : Le contexte fourni traite de la composition du jury, du recrutement et de la procédure de soutenance, sans aucune mention d'alumni. Ainsi, le contexte ne contenait pas l'information requise pour répondre à la question.

### Question : Que propose le Pôle SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 61.07s, Eval: 12.80s, Total: 73.87s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement tirées du contexte : le pôle répond aux sollicitations extérieures, organise des rencontres (ex. DéTours des sciences, Ma thèse en 180 s), accompagne les chercheurs (conception, financement, diffusion) et propose des formations comme le médiatraining. L’adresse e‑mail fournie figure également dans le contexte. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question « Que propose le Pôle SAPS ? » en listant les services principaux (sollicitations, événements, accompagnement, formations) et en indiquant le contact. Aucun hors‑sujet n’est présent.
- **Avis Context Precision** : Le contexte récupéré contient l’ensemble des informations nécessaires : missions du pôle, exemples d’événements, types d’accompagnement, catalogue de formations, contacts. Il est donc parfaitement ciblé.

### Question : - Qu’est-ce qu’une invention ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 82.98s, Eval: 13.80s, Total: 96.78s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient aucune affirmation factuelle sur le sujet. Le seul élément ajouté est une information de contact, qui selon les règles ne doit pas être pénalisée. Aucun contenu n’est inventé ou contradictoire avec le contexte fourni.
- **Avis Answer Relevance** : La question porte sur la définition d’une invention. La réponse se limite à fournir un contact et ne répond en rien à la demande, ce qui la rend hors‑sujet.
- **Avis Context Precision** : Le contexte récupéré traite du régime juridique des inventions et des créateurs indépendants, mais il ne fournit pas une définition claire de « invention ». Il est donc seulement vaguement lié à la question et ne contient pas l’information nécessaire pour y répondre correctement.

### Question : - Je souhaite répondre à un Appel à projet?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 89.66s, Eval: 9.12s, Total: 98.78s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont soit directement compatibles avec le contexte, soit concernent des informations de contact (nom, email) qui, selon les règles, ne sont pas pénalisées même si elles n'apparaissent pas dans le contexte fourni.
- **Avis Answer Relevance** : La réponse propose un contact qui peut aider l'utilisateur à répondre à un appel à projet, ce qui répond partiellement à la demande. Elle ne fournit pas de procédure détaillée, d'où une note légèrement inférieure à la perfection.
- **Avis Context Precision** : Le contexte retrouvé porte principalement sur la convention individuelle de formation, le suivi de thèse, les procédures de soutenance, etc. Aucun élément du contexte ne traite d'un appel à projet ou d'un contact lié à ce sujet, ce qui rend le contexte peu pertinent pour la question.

### Question : je suis en arrêt de travail, qui dois-je contacter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 87.25s, Eval: 13.95s, Total: 101.20s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont des contacts (nom, e‑mail). Selon la règle, les informations de contact qui n’apparaissent pas dans le contexte ne sont pas comptabilisées comme hallucination, donc la réponse reste totalement fidèle au contexte fourni.
- **Avis Answer Relevance** : La question demande « qui dois‑je contacter ? » en cas d’arrêt de travail. La réponse fournit un nom et une adresse e‑mail, répondant directement à la demande.
- **Avis Context Precision** : Le contexte fourni ne mentionne aucun nom ou e‑mail spécifique lié à un arrêt de travail. Il indique seulement qu’il faut prendre contact avec un gestionnaire de la DRH et renvoie à l’organigramme, ce qui n’est pas assez précis pour identifier la personne exacte. Le contexte est donc peu précis pour la question.

### Question : Combien de temps va prendre mon inscription ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 80.95s, Eval: 8.39s, Total: 89.34s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les informations fournies (nom et adresse e‑mail de Christele Gaudron) sont présentes dans le contexte. Aucun élément n’est inventé, donc la réponse est totalement fidèle aux données récupérées.
- **Avis Answer Relevance** : La question porte sur la durée de l’inscription (« Combien de temps va prendre mon inscription ? »). La réponse ne donne aucune indication de durée, elle fournit seulement un contact, ce qui ne répond pas du tout à la demande.
- **Avis Context Precision** : Le contexte contient de nombreuses informations sur la procédure d’inscription, les étapes à suivre et même une date limite (15 novembre) ainsi que la mention d’éventuels délais plus longs. Cependant, il ne fournit pas de durée précise exprimée en jours ou semaines. Le contexte est donc partiellement pertinent mais ne répond pas directement à la question de durée.

### Question : Comment avoir un email ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 2.0/5, Context Precision: 1.0/5
- **Temps** : RAG: 81.48s, Eval: 11.43s, Total: 92.91s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les informations fournies sont des coordonnées de contact (adresse e‑mail). Selon la règle, les contacts ajoutés qui ne figurent pas dans le contexte ne sont pas considérés comme des hallucinations, donc la réponse reste entièrement fidèle au contexte.
- **Avis Answer Relevance** : La question porte sur la façon d'obtenir un e‑mail. La réponse donne simplement une adresse e‑mail de contact, sans expliquer la procédure pour créer ou obtenir une adresse e‑mail, ce qui ne répond pas réellement à la demande.
- **Avis Context Precision** : Le contexte récupéré traite de la législation de la recherche, de la conservation du capital, etc., et ne contient aucune information relative à la création ou à l'obtention d'une adresse e‑mail. Le contexte est donc hors sujet.

### Question : - Je souhaite me procurer le formulaire de déclaration d’invention de l’université, à qui dois-je m’adresser ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 89.86s, Eval: 7.02s, Total: 96.88s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : le texte indique explicitement que pour toute question générale relative à la propriété intellectuelle il faut privilégier l'adresse générique drv-pi@univ-tours.fr. Aucun élément n’a été inventé.
- **Avis Answer Relevance** : La réponse répond directement à la question en indiquant à qui s’adresser pour obtenir le formulaire de déclaration d’invention, sans digression.
- **Avis Context Precision** : Le contexte fourni contient l'information exacte requise (adresse générique du Pôle Juridique Recherche) ainsi que d’autres contacts, mais l’information essentielle est bien présente et ciblée.

### Question : Qui contacter pour toute demande d'ouvrages en service presse ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 1.0/5
- **Temps** : RAG: 87.34s, Eval: 8.37s, Total: 95.71s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient aucune affirmation qui ne provient pas du contexte. Le seul élément ajouté est un contact (email) qui, selon la règle spéciale, n'est pas considéré comme hallucination même s'il n'apparaît pas dans le contexte fourni.
- **Avis Answer Relevance** : La question demande explicitement qui contacter pour des demandes d'ouvrages en service presse. La réponse fournit directement l'adresse e‑mail du contact, répondant ainsi exactement à la demande.
- **Avis Context Precision** : Le contexte récupéré porte sur le droit d'auteur, les contrats de cession, etc., et ne mentionne aucun service presse ni aucun contact. Il est donc totalement hors sujet par rapport à la question.

### Question : comment enregistrer ma demande de formation hors-catalogue et quels documents dois-je fournir ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 5.0/5, Context Precision: 1.0/5
- **Temps** : RAG: 87.00s, Eval: 16.18s, Total: 103.18s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse introduit des informations (adresse e‑mail drv-pi@univ-tours.fr, mention du formulaire, du CV, du projet pédagogique et des justificatifs de financement) qui ne figurent pas dans le contexte fourni. Même si les contacts ne sont pas pénalisés pour la fidélité, ils restent des éléments absents du texte source, ce qui rend la réponse largement non fondée sur le contexte.
- **Avis Answer Relevance** : La réponse répond directement à la question posée en indiquant comment soumettre la demande et quels documents fournir, même si ces informations sont inventées. Elle est donc très pertinente par rapport à la demande de l'utilisateur.
- **Avis Context Precision** : Le contexte récupéré porte sur les règles d'éméritat, des décrets, des contacts généraux et aucune information relative aux demandes de formation hors‑catalogue. Le contexte n'est donc pas du tout pertinent pour la question.

### Question : Mon jury de thèse est-il valide ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 1.0/5
- **Temps** : RAG: 85.15s, Eval: 9.86s, Total: 95.01s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient aucune affirmation factuelle autre que le contact fourni. Les informations de contact sont exemptées de pénalité selon la règle, donc aucune hallucination n'est détectée. Tous les éléments de la réponse sont donc traçables (ou exemptés).
- **Avis Answer Relevance** : La question porte sur la validité du jury de thèse, alors que la réponse ne fournit qu'un contact administratif, ne répondant pas du tout à la demande. La pertinence est donc très faible.
- **Avis Context Precision** : Le contexte récupéré traite de droit d'auteur, d'originalité, d'éméritat, etc., et ne contient aucune information relative à la composition ou la validité d'un jury de thèse. Le contexte n'est donc pas pertinent pour la question.

### Question : quels types de financement de thèse existent ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 88.55s, Eval: 19.94s, Total: 108.49s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les sources mentionnées dans la réponse (ANR, Europe, Labex, contrats de recherche/entreprise, bourses du Ministère, bourses régionales, départementales, industrielles, CIFRE/DGA/ADEME, financements privés ou associatifs, contrats « Établissement » ou régionaux, postes de doctorants salariés) sont présentes dans le contexte. Aucun élément n’est inventé. Le contact ajouté n’est pas pénalisé selon la règle.
- **Avis Answer Relevance** : La réponse répond directement à la question en listant les différents types de financement de thèse, sans digression.
- **Avis Context Precision** : Le contexte fourni contient une section détaillée sur les « Autres financements doctoraux » qui recense précisément les types de financement cités dans la réponse, montrant que le contexte était pleinement pertinent.

### Question : - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autre CHRU?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 95.03s, Eval: 14.54s, Total: 109.57s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations (nécessité d'un dossier CODECH, soumission au référent de l'unité, rôle du conseiller de prévention) sont directement présentes dans le contexte. Les coordonnées de contact ne sont pas dans le contexte mais, selon la règle, les contacts ajoutés automatiquement ne sont pas pénalisés.
- **Avis Answer Relevance** : La réponse répond précisément à la question en expliquant la procédure à suivre pour utiliser des échantillons provenant du CHRU de Tours ou d'un autre CHRU.
- **Avis Context Precision** : Le contexte récupéré contient les informations essentielles sur le dossier CODECH, l'autorisation MESRI et les interlocuteurs (référent, conseiller de prévention), ce qui est suffisant pour répondre à la question.

### Question : Je souhaite monter un projet, comment faire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 93.88s, Eval: 11.92s, Total: 105.80s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations concernant la constitution du dossier (cahier des charges, descriptif, budget, livrables, grille d’analyse) et la transmission au COPIL, ainsi que le rôle du service SCRIPT, sont directement présentes dans le contexte. Le contact Justine Gillet est une information de contact qui, selon les règles, n'est pas pénalisée même s'il n'apparaît pas dans le contexte.
- **Avis Answer Relevance** : La réponse fournit une procédure claire et concrète pour monter un projet, répondant exactement à la demande « comment faire ? ». Aucun élément hors sujet n'est ajouté.
- **Avis Context Precision** : Le contexte contient les étapes détaillées du dépôt, de la contractualisation et du suivi des projets, ainsi que les acteurs impliqués (COPIL, SCRIPT). Ces informations sont suffisantes pour répondre à la question.

### Question : - Comment protéger un savoir-faire ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 84.65s, Eval: 13.92s, Total: 98.57s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse s’appuie sur le contexte : le texte mentionne l’importance de la confidentialité, les mots‑clés brevet, licence, savoir‑faire et le rôle du Pôle Juridique Recherche. L’idée d’un NDA et d’un contrat de licence/cession est bien présente. Le recours à un dépôt de brevet est une inférence raisonnable à partir du mot‑clé « brevet», mais n’est pas explicitement indiqué pour le savoir‑faire, d’où une note 4.
- **Avis Answer Relevance** : La réponse répond directement à la question «Comment protéger un savoir‑faire ?» en proposant des mesures concrètes (NDA, brevet éventuel, licence/cession) et en indiquant le contact du PJR. Aucun élément hors sujet n’est présent.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires : notions de propriété intellectuelle, confidentialité, rôle du PJR, contacts, modèles de contrats. Il est donc parfaitement pertinent.

### Question : Je pars en mission, quelle pièce dois-je remplir ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 90.76s, Eval: 11.13s, Total: 101.89s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : le formulaire « Autorisation de déplacement » est mentionné, ainsi que l’obligation de joindre la carte grise et d’obtenir l’autorisation de l’ordonnateur. Le nom et l’e‑mail du contact ne figurent pas dans le contexte, mais la consigne indique de ne pas pénaliser les contacts injectés.
- **Avis Answer Relevance** : La réponse répond exactement à la question « quelle pièce dois‑je remplir ? » en indiquant le formulaire à remplir. Aucun élément hors sujet n’est ajouté.
- **Avis Context Precision** : Le contexte récupéré contient le nom du formulaire requis et les consignes associées, ce qui est suffisant pour répondre à la question.

### Question : Quel est le délai moyen entre la soumission d’un manuscrit et sa publication ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 87.13s, Eval: 14.09s, Total: 101.22s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient aucune affirmation factuelle autre que le contact fourni. Les contacts sont explicitement exemptés de pénalité selon les consignes, donc aucune hallucination n'est relevée.
- **Avis Answer Relevance** : La question porte sur le délai moyen entre soumission d’un manuscrit et sa publication. La réponse ne fournit aucun renseignement à ce sujet, se limitant à un contact, ce qui la rend hors‑sujet.
- **Avis Context Precision** : Le contexte fourni ne donne pas le délai moyen recherché, mais il mentionne des délais maximaux (6 mois ou 12 mois) liés à la mise à disposition en accès ouvert. Ainsi le contexte est seulement vaguement lié à la notion de délai, mais ne répond pas directement à la question.

## 04_meta_mono

### Question : C’est quoi les SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 59.17s, Eval: 12.64s, Total: 71.81s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (définition du sigle, rôle de rapprochement entre chercheurs et société, missions de réponse aux sollicitations, organisation de rencontres et accompagnement des chercheurs) sont directement tirées du texte du contexte. L’adresse e‑mail fournie figure également dans la section Contacts du contexte. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La question « C’est quoi les SAPS ? » attend une définition. La réponse fournit exactement cette définition ainsi que les objectifs principaux, répondant ainsi pleinement à la demande.
- **Avis Context Precision** : Le contexte récupéré contient la définition du sigle, les missions du pôle, ainsi que les coordonnées de contact. Il est donc parfaitement adapté pour répondre à la question.

### Question : Comment peut-on changer le budget d’un projet ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 108.68s, Eval: 14.20s, Total: 122.88s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations (contacter le SPIV, fournir un argumentaire scientifique, fournir un budget modifié au formalisme du financeur, analyse par le SPIV en interaction avec l'Antenne Financière) sont directement tirées du texte « Gérer les aléas (demande d’avenant ou de modification) ». Le contact ajouté (Anne Galopin) est un élément de contact qui, selon les consignes, ne doit pas être pénalisé.
- **Avis Answer Relevance** : La réponse répond exactement à la question « Comment peut-on changer le budget d’un projet ? » en décrivant la procédure à suivre, sans digression.
- **Avis Context Precision** : Le contexte fourni contient la procédure complète de modification budgétaire, incluant le rôle du SPIV, les documents requis et le processus d’analyse, ce qui est suffisant pour répondre à la question.

### Question : Quelles sont les différentes démarches à effectuer ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 98.10s, Eval: 11.31s, Total: 109.41s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : la procédure de demande (soumission au président/directeur, avis de la commission recherche ou du conseil scientifique), la nécessité d’un projet détaillé, les critères d’évaluation, la durée maximale de 5 ans renouvelable deux fois (total 15 ans) et les contacts du PJR. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La question porte sur les « démarches à effectuer ». La réponse décrit précisément les démarches pour obtenir l’éméritat, ce qui correspond à l’attente implicite du contexte. Elle fournit également des contacts utiles, ce qui renforce la pertinence.
- **Avis Context Precision** : Le contexte récupéré contient toutes les informations nécessaires : procédure de demande, organes décisionnels, critères d’évaluation, durée et contacts. Il est donc parfaitement ciblé.

### Question : - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire extérieur? Est-ce gratuit?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 3.0/5, Context Precision: 3.0/5
- **Temps** : RAG: 88.11s, Eval: 15.85s, Total: 103.96s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse mentionne le « Guide du DU/La propriété intellectuelle.md », qui n’apparaît pas dans le contexte fourni. Le reste (contact du SPIV, recommandation de le contacter) est présent dans le texte. Ainsi, la réponse est partiellement fidèle mais comporte une information non‑trouvable dans le contexte.
- **Avis Answer Relevance** : La réponse indique où trouver les règles et propose de contacter le SPIV, ce qui répond en partie à la question du cadre. Cependant, elle ne répond pas à la seconde partie de la question (« Est‑ce gratuit ? »), ce qui la rend seulement partiellement pertinente.
- **Avis Context Precision** : Le contexte contient des sections sur la recherche collaborative, la propriété intellectuelle et le rôle du Service Partenariats Innovations Valorisation, ce qui est pertinent. Il ne fournit toutefois pas de réponse explicite sur la gratuité, et le guide cité n’est pas présent. Le contexte est donc partiellement adéquat.

### Question : A quelle adresse postale ou mail dois-je envoyer mon projet ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 3.0/5, Context Precision: 4.0/5
- **Temps** : RAG: 82.40s, Eval: 8.16s, Total: 90.56s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : l'adresse e‑mail générique drv-pi@univ-tours.fr est explicitement listée dans la section « Contacts » du contexte. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La question demande une adresse postale ou e‑mail pour envoyer un projet. La réponse fournit un e‑mail, ce qui répond partiellement à la demande, mais ne précise pas si cet e‑mail est le bon canal pour un projet (il est indiqué pour les questions générales de propriété intellectuelle) et ne propose aucune adresse postale. La pertinence est donc moyenne.
- **Avis Context Precision** : Le contexte contient plusieurs adresses e‑mail et indique clairement l'e‑mail générique drv-pi@univ-tours.fr. Le contexte ne fournit toutefois aucune adresse postale. Ainsi le contexte est pertinent mais incomplet pour couvrir l’ensemble de la question.

### Question : Comment m’inscrire / me réinscrire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 93.86s, Eval: 19.39s, Total: 113.25s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (connexion à ADUM, dépôt de la Convention Individuelle de Formation, validation par les différentes instances, réception d'un mail, procédure de paiement de la CVEC) sont directement présentes dans le contexte. Le contact ajouté n'est pas pénalisé selon la règle sur les contacts injectés.
- **Avis Answer Relevance** : La réponse répond précisément à la question « Comment m’inscrire / me réinscrire ? » en décrivant la procédure à suivre, les documents à fournir et les étapes de validation.
- **Avis Context Precision** : Le contexte fourni contient l’ensemble des informations nécessaires (procédure ADUM, documents, validation, contacts, etc.) pour répondre à la question.

### Question : Quelles ressources le Pôle SAPS peut m’apporter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 60.65s, Eval: 13.98s, Total: 74.63s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (faciliter les échanges, former à la médiation scientifique, organiser des événements/animations, accompagner la participation aux événements nationaux, contacts) sont directement présentes dans le contexte. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond à la question en listant les principales ressources offertes par le Pôle SAPS. Elle reste centrée sur le sujet, même si elle ne couvre pas l’ensemble des services détaillés dans le contexte.
- **Avis Context Precision** : Le contexte fourni contient une description exhaustive des missions du Pôle SAPS, incluant formation, accompagnement de projets, organisation d’événements, etc. Il est donc parfaitement adapté pour répondre à la question.

### Question : Y a-t-il des alumni ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 4.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 92.62s, Eval: 7.91s, Total: 100.53s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse affirme qu'il existe des informations sur les anciens doctorants (alumni) sur le site de l'Université de Tours, or aucune mention d'alumni n'apparaît dans le contexte fourni. Cette affirmation est donc une hallucination. Le contact d'Elysa Ragot est présent dans le contexte, donc cette partie est correcte, mais la majorité de la réponse n'est pas traçable dans le texte.
- **Avis Answer Relevance** : La réponse répond directement à la question « Y a-t-il des alumni ? » en disant « Oui » et en proposant un moyen d'obtenir des informations, ce qui est pertinent même si l'information n'est pas supportée par le contexte.
- **Avis Context Precision** : Le contexte ne contient aucune information concernant des alumni ou anciens doctorants. Il se concentre sur la création de compte ADUM, les documents requis, et les contacts. Ainsi, le contexte n'est pas précis pour répondre à la question.

### Question : Que propose le Pôle SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 63.50s, Eval: 14.82s, Total: 78.32s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : le pôle propose des formations (médiation scientifique, éthique, communication orale), des événements (Fête de la science, Nocturnes de l'Histoire, Festival (Re)Cherche et trouve) et des projets (Boutique des sciences, Label SAPS, Ma thèse en BD, Kaléidoscope). Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond directement à la question « Que propose le Pôle SAPS ? » en listant les grandes catégories d’offres (formations, événements, projets). Elle reste pertinente même si elle ne détaille pas l’ensemble des missions du pôle.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires pour répondre à la question, incluant les missions, formations, événements et projets du pôle. Le système a donc pu s’appuyer sur un contexte très pertinent.

### Question : - Qu’est-ce qu’une invention ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 5.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 85.83s, Eval: 12.92s, Total: 98.75s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse fournit une définition générique d’une invention (« création originale qui répond à un problème… ») qui n’est mentionnée nulle part dans le contexte fourni. Le contexte parle de droits de propriété intellectuelle, d’articles du CPI, etc., mais ne donne aucune définition. Ainsi, la plupart des affirmations ne sont pas traçables dans le texte, ce qui justifie une note faible. Le contact ajouté n’est pas pénalisé selon la règle d’exemption.
- **Avis Answer Relevance** : La question porte sur la définition d’une invention. La réponse répond directement à cette demande en donnant une description de ce qu’est une invention, ce qui la rend très pertinente malgré le manque de référence au contexte.
- **Avis Context Precision** : Le contexte récupéré traite de la législation autour des inventions, des brevets et des droits des émérites, mais ne contient pas d’information explicite permettant de définir une invention. Le texte est donc seulement vaguement lié au sujet et ne fournit pas les éléments nécessaires pour répondre à la question.

### Question : - Je souhaite répondre à un Appel à projet?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 113.91s, Eval: 0.00s, Total: 113.91s
- **Tokens générés** : 0

### Question : je suis en arrêt de travail, qui dois-je contacter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 90.05s, Eval: 8.10s, Total: 98.15s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (contact du médecin du travail, son rattachement au Service Prévention Protection Santé Sécurité, localisation au Plat d'Etain, rôle de surveillance médicale, possibilité de contacter l'Assistant de Prévention) sont directement présentes dans le contexte. Le nom et l'email fournis sont des contacts ajoutés automatiquement, mais la consigne indique de ne pas les pénaliser.
- **Avis Answer Relevance** : La réponse répond exactement à la question « qui dois‑je contacter ? » en indiquant le médecin du travail et l'Assistant de Prévention, ce qui correspond aux interlocuteurs pertinents pour un arrêt de travail.
- **Avis Context Precision** : Le contexte contient les informations nécessaires sur le médecin du travail et l'Assistant de Prévention, ainsi que leurs missions, ce qui permet de répondre à la question sans recherche supplémentaire.

### Question : Combien de temps va prendre mon inscription ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 91.99s, Eval: 9.67s, Total: 101.66s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont vérifiables dans le contexte : le texte ne mentionne effectivement aucune durée pour l'inscription, ce qui justifie la phrase « La durée de l'inscription n'est pas précisée ». Le contact fourni (Christele Gaudron-Bredif, gaudron@univ-tours.fr) n'apparaît pas dans le contexte, mais les règles d'évaluation stipulent de ne pas pénaliser les informations de contact ajoutées automatiquement.
- **Avis Answer Relevance** : La réponse répond directement à la question « Combien de temps va prendre mon inscription ? » en indiquant que le délai n'est pas indiqué dans le contexte et en proposant de contacter une personne pour obtenir l'information, ce qui est pleinement pertinent.
- **Avis Context Precision** : Le contexte récupéré contient de nombreuses informations sur les documents à fournir, les champs du formulaire, etc., mais il ne fournit aucune indication sur la durée du processus d'inscription. Ainsi, le contexte est seulement vaguement lié au sujet et ne contient pas l'information recherchée.

### Question : Comment avoir un email ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 4.0/5, Context Precision: 1.0/5
- **Temps** : RAG: 88.13s, Eval: 7.24s, Total: 95.37s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse mentionne des éléments (site web de l'Université de Tours, procédure de création de compte, contact du service informatique) qui ne figurent pas du tout dans le contexte fourni. Seul le contact e‑mail est exempté selon la règle des contacts injectés. Ainsi la majorité des affirmations sont hallucinées, justifiant un 2.
- **Avis Answer Relevance** : La réponse répond à la question « Comment avoir un email ? » en proposant une démarche concrète, ce qui est pertinent. Elle ne traite pas d’autres aspects, mais reste centrée sur la demande, d’où un 4.
- **Avis Context Precision** : Le contexte récupéré porte sur la confidentialité, les collaborateurs bénévoles, les cahiers de laboratoire, etc., et ne contient aucune information relative à la création d’un compte e‑mail. Le contexte est donc totalement non pertinent, justifiant un 1.

### Question : - Je souhaite me procurer le formulaire de déclaration d’invention de l’université, à qui dois-je m’adresser ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 85.17s, Eval: 7.61s, Total: 92.78s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les informations fournies dans la réponse (Pôle Juridique Recherche, Morgane Guibert, son adresse e‑mail, adresse générique drv-pi@univ‑tours.fr) sont présentes textuellement dans le contexte. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse indique clairement à qui s’adresser pour obtenir le formulaire de déclaration d’invention, répondant ainsi directement à la question posée.
- **Avis Context Precision** : Le contexte contient les coordonnées du PJR et de sa responsable, ainsi que l’adresse générique pour les questions de propriété intellectuelle, ce qui est exactement ce dont la question a besoin.

### Question : Qui contacter pour toute demande d'ouvrages en service presse ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 2.0/5, Context Precision: 1.0/5
- **Temps** : RAG: 84.09s, Eval: 9.34s, Total: 93.43s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse indique qu'il faut contacter le "service presse de l'Université de Tours" et propose l'adresse drv-pi@univ-tours.fr comme contact presse. Aucun de ces éléments n'apparaît dans le contexte fourni, qui ne mentionne que des contacts liés à la propriété intellectuelle (drv-pi@univ-tours.fr) et aucune référence à un service presse. Ainsi, la plupart des affirmations sont hallucinations.
- **Avis Answer Relevance** : La réponse tente de répondre à la question en proposant un contact, mais le contact proposé n'est pas justifié par le contexte. Elle touche au sujet (contact) mais ne fournit pas l'information correcte, d'où une pertinence limitée.
- **Avis Context Precision** : Le contexte ne contient aucune information concernant le service presse ou les demandes d'ouvrages en service presse. Il est donc non pertinent pour la question posée.

### Question : comment enregistrer ma demande de formation hors-catalogue et quels documents dois-je fournir ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 5.0/5, Context Precision: 1.0/5
- **Temps** : RAG: 86.39s, Eval: 12.08s, Total: 98.47s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse contient uniquement des informations qui ne figurent pas dans le contexte fourni (procédure d'enregistrement, documents à fournir, lien web, adresse e‑mail). Aucun élément du texte n'est traçable dans le contexte, qui porte sur des dispositions légales relatives aux chercheurs, aux émérites, etc. Selon la règle, les contacts ne sont pas pénalisés pour la fidélité, mais ils restent absents du contexte, ce qui fait que la majorité de la réponse est hallucination.
- **Avis Answer Relevance** : La réponse répond directement à la question posée : elle indique comment enregistrer une demande de formation hors‑catalogue et quels documents fournir. Elle est donc très pertinente par rapport à la demande de l'utilisateur.
- **Avis Context Precision** : Le contexte retrouvé ne contient aucune information relative aux demandes de formation hors‑catalogue, aux procédures d'inscription ou aux documents requis. Il est donc totalement inapproprié pour répondre à la question.

### Question : Mon jury de thèse est-il valide ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 2.0/5, Context Precision: 1.0/5
- **Temps** : RAG: 86.12s, Eval: 11.73s, Total: 97.85s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse cite le décret n°2021-1645, présent dans le contexte, mais affirme à tort que ce décret détermine la validité d'un jury de thèse, ce qui n'est pas mentionné dans le texte fourni. Cette affirmation est donc une hallucination. Le contact fourni n'est pas pénalisé selon la règle d'exemption des contacts.
- **Avis Answer Relevance** : La question porte sur la validité d'un jury de thèse. La réponse ne fournit pas d'éléments concrets permettant de juger de cette validité, se limitant à une référence générique à un décret et à une suggestion de contact, ce qui ne répond pas réellement à la demande.
- **Avis Context Precision** : Le contexte retrouvé traite de l'éméritat des enseignants-chercheurs et de la législation associée, sans aucune information relative aux jurys de thèse. Ainsi, le contexte n'est pas pertinent pour répondre à la question posée.

### Question : quels types de financement de thèse existent ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 94.05s, Eval: 13.22s, Total: 107.27s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les catégories mentionnées dans la réponse (ANR, Europe, Labex, contrats de recherche, contrats entreprise, CIFRE/DGA/ADEME, gouvernements/associations/établissements étrangers, salariés, bourses régionales, départementales, industrielles, conventions CIFRE, bourses associatives, présidentielles, Rabelaisiennes, Université d'Orléans) apparaissent explicitement dans le contexte. Aucun élément n’est inventé ; le contact ajouté est exempté de pénalité selon les règles.
- **Avis Answer Relevance** : La réponse répond directement à la question en listant les différents types de financement de thèse, ce qui constitue une réponse ciblée et exhaustive du point de vue de la question posée.
- **Avis Context Precision** : Le contexte fourni contient une section détaillée « Autres financements doctoraux » qui recense les mêmes types de financement que ceux listés dans la réponse, ainsi que d’autres mentions (bourses présidentielles, Rabelaisiennes, etc.). Le contexte était donc parfaitement adapté.

### Question : - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autre CHRU?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 90.24s, Eval: 7.28s, Total: 97.52s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations concernant la façon de rédiger la seconde ligne de signature sont directement tirées du contexte fourni. Le contact ajouté (Claude‑Emmanuel Boudet) n'est pas présent dans le contexte mais, selon les règles, les informations de contact ne sont pas pénalisées pour la fidélité.
- **Avis Answer Relevance** : La question porte sur l'utilisation d'échantillons provenant du CHRU de Tours ou d'un autre CHRU, alors que la réponse traite uniquement de la rédaction des affiliations et signatures. Aucun élément de la réponse ne répond à la demande concernant les échantillons.
- **Avis Context Precision** : Le contexte récupéré porte sur les règles de signature des auteurs affiliés au CHRU de Tours, mais ne contient aucune information relative à l'utilisation d'échantillons. Le contexte est donc seulement vaguement lié au sujet de la question.

### Question : Je souhaite monter un projet, comment faire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 90.58s, Eval: 11.44s, Total: 102.02s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (contacter le service SCRIPT, transmettre la saisine à projets-etablissement@univ-tours.fr, rôle du SCRIPT dans le suivi du comité de pilotage, nécessité d’un pilotage continu et du recrutement d’un chef de projet) sont directement présentes dans le contexte. Le nom et les coordonnées de Justine Gillet ne figurent pas dans le contexte, mais la règle d’évaluation stipule de ne pas pénaliser les contacts ajoutés automatiquement.
- **Avis Answer Relevance** : La réponse répond précisément à la question « Je souhaite monter un projet, comment faire ? » en indiquant les étapes concrètes à suivre et les interlocuteurs à contacter, sans digression hors sujet.
- **Avis Context Precision** : Le contexte fourni contient les informations nécessaires pour répondre à la question : procédure de saisine, rôle du service SCRIPT, exigences de pilotage et de recrutement, organisation du COPIL. Le système a exploité ces éléments.

### Question : - Comment protéger un savoir-faire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 83.81s, Eval: 8.75s, Total: 92.56s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse se retrouvent dans le contexte : le texte mentionne l'importance d'un accord de confidentialité ou d'une convention de collaborateur bénévole pour sécuriser les informations, et fournit les coordonnées du Pôle Juridique Recherche (drv-pi@univ-tours.fr). Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond à la question « Comment protéger un savoir‑faire ? » en proposant des mesures concrètes (accord de confidentialité, convention) et en indiquant un point de contact. Elle reste centrée sur la protection, même si elle ne couvre pas d'autres voies possibles (brevets, secret commercial).
- **Avis Context Precision** : Le contexte contient les informations nécessaires : exigences de confidentialité, rôle des conventions pour les bénévoles, et les contacts du PJR. Ces éléments sont directement exploités dans la réponse.

### Question : Je pars en mission, quelle pièce dois-je remplir ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 87.55s, Eval: 9.20s, Total: 96.75s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : le formulaire d'autorisation de déplacement à remplir pour chaque mission, la nécessité de joindre une copie de la carte grise, et l'obligation de le transmettre au gestionnaire ou à l'antenne financière au moins 15 jours avant le départ. Le texte "disponible sur l'Intranet" découle de la mention "cf. procédure sur l'Intranet". Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question en indiquant le document à remplir (formulaire d'autorisation de déplacement) et fournit des précisions utiles (pièce à joindre, délai de transmission). Aucun hors‑sujet n'est introduit.
- **Avis Context Precision** : Le contexte récupéré contient toutes les informations nécessaires : existence du formulaire d'autorisation de déplacement, la mention de la carte grise à joindre et le délai de transmission. Le contexte est donc parfaitement ciblé.

### Question : Quel est le délai moyen entre la soumission d’un manuscrit et sa publication ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 2.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 85.47s, Eval: 13.67s, Total: 99.14s
- **Tokens générés** : 0
- **Avis Faithfulness** : Le texte cite correctement les délais de 6 mois et 12 mois prévus par l'article L533-4 du CPI, qui figurent bien dans le contexte. En revanche, il affirme que ces délais correspondent au "délai moyen entre la soumission d’un manuscrit et sa publication", ce qui n’est pas présent dans le contexte et constitue une interprétation erronée ou une invention.
- **Avis Answer Relevance** : La question porte sur le délai moyen entre la soumission et la publication. La réponse fournit des informations sur le délai légal de mise à disposition du manuscrit après la première publication, qui ne répond pas à la question posée.
- **Avis Context Precision** : Le contexte ne contient pas d’information sur le délai moyen entre soumission et publication ; il ne traite que du délai maximal de mise à disposition en accès ouvert (6 ou 12 mois). Ainsi, le contexte n’est pas réellement pertinent pour répondre à la question.

## 05_mistral_stack

### Question : C’est quoi les SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 57.54s, Eval: 8.53s, Total: 66.07s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : SAPS = Sciences Avec et Pour la Société, initiative du Ministère de l'Enseignement supérieur et de la Recherche, objectif de renforcer les liens entre recherche et société et de favoriser le dialogue entre chercheurs et citoyens, ainsi que la médiation scientifique. Le lien saps.univ-tours.fr apparaît également dans le contexte.
- **Avis Answer Relevance** : La réponse répond exactement à la question « C’est quoi les SAPS ? » en donnant une définition claire et concise.
- **Avis Context Precision** : Le contexte fourni contient la définition, les objectifs et le site web des SAPS, ce qui est suffisant pour répondre à la question.

### Question : Comment peut-on changer le budget d’un projet ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 104.95s, Eval: 16.65s, Total: 121.60s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (contacter le SPIV, fournir un argumentaire scientifique, fournir un budget modifié validé par l'antenne financière, transmission au financeur, délais variables) sont directement présentes dans le contexte sous la section "SPIV # Gérer les aléas (demande d’avenant ou de modification)". Aucun élément n'est inventé ; le contact ajouté est exempté selon la règle sur les contacts injectés.
- **Avis Answer Relevance** : La réponse répond exactement à la question « Comment peut-on changer le budget d’un projet ? » en décrivant la procédure à suivre, sans digression.
- **Avis Context Precision** : Le contexte récupéré contient la procédure complète de modification budgétaire via le SPIV, ce qui est exactement l'information requise pour répondre à la question.

### Question : Quelles sont les différentes démarches à effectuer ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 2.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 83.65s, Eval: 15.59s, Total: 99.24s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse indique que la demande est trop générale et invite à préciser le type de démarche. Cette affirmation n'est pas présente dans le contexte fourni, donc elle constitue une information non traçable. Le seul élément qui pourrait être considéré comme exempt (l'adresse e‑mail) est un contact injecté et ne pénalise pas la fidélité.
- **Avis Answer Relevance** : La question demandait les différentes démarches à effectuer. La réponse ne fournit aucune démarche concrète, se contentant de demander plus de précision et de proposer un contact. Elle ne répond donc pas réellement à la question.
- **Avis Context Precision** : Le contexte récupéré contient de nombreuses informations sur les procédures (mise à disposition d'articles en accès ouvert, réutilisation des données, cession du droit d'auteur, procédure d'éméritat, contrat de valorisation, déclaration d'invention, etc.). Il est donc très pertinent pour répondre à la question.

### Question : - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire extérieur? Est-ce gratuit?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 88.28s, Eval: 14.62s, Total: 102.90s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse reprend correctement les informations du contexte concernant les projets de recherche collaboratifs encadrés par un contrat et le rôle du Service Partenariats Innovations Valorisation. Cependant, l'affirmation « La gratuité dépend des termes du contrat négocié avec le partenaire et des financements associés » n'est pas explicitement mentionnée dans le contexte, ce qui constitue une hallucination mineure.
- **Avis Answer Relevance** : La réponse répond directement à la question en précisant le cadre (projets de recherche collaboratifs avec contrat) et en indiquant que la gratuité dépend des conditions contractuelles, ce qui correspond à la demande de savoir si c'est gratuit.
- **Avis Context Precision** : Le contexte contient une section dédiée à la recherche collaborative et à la nécessité d'un contrat, ainsi que le service à contacter, ce qui fournit toutes les informations nécessaires pour répondre à la question.

### Question : A quelle adresse postale ou mail dois-je envoyer mon projet ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 4.0/5
- **Temps** : RAG: 185.19s, Eval: 18.56s, Total: 203.75s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient aucune affirmation qui contredit le contexte. Elle fournit uniquement une adresse e‑mail, ce qui est autorisé même si cet e‑mail n’apparaît pas explicitement dans le contexte (règle sur les contacts injectés). Aucun autre élément n’est ajouté.
- **Avis Answer Relevance** : La question porte sur l’adresse postale ou e‑mail à laquelle envoyer le projet. La réponse donne un e‑mail, ce qui répond directement à la demande. Aucun hors‑sujet n’est présent.
- **Avis Context Precision** : Le contexte récupéré comporte de nombreuses adresses e‑mail (ex. isabelle.foulon@univ‑tours.fr, guillaume.fialeix@univ‑tours.fr, edemstu@univ‑orleans.fr, etc.) et indique que le dossier doit être envoyé par courrier électronique. Ainsi le contexte est pertinent, même s’il ne contient pas exactement l’e‑mail fourni dans la réponse.

### Question : Comment m’inscrire / me réinscrire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 85.67s, Eval: 10.57s, Total: 96.24s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les étapes décrites (connexion à ADUM, mise à jour des informations, dépôt de la Convention Individuelle de Formation, dépôt des pièces (photo, CV, rapport d'activité), clic sur « Je finalise la procédure », validation du dossier par les différentes instances et date limite du 15 novembre) sont présentes textuellement dans le contexte. Le seul élément absent du contexte est le contact « Marie Clermonte », mais il s'agit d'une information de contact et, selon les règles, cela ne doit pas pénaliser la fidélité.
- **Avis Answer Relevance** : La réponse répond directement à la question « Comment m’inscrire / me réinscrire ? » en donnant les étapes concrètes à suivre, sans digression hors sujet.
- **Avis Context Precision** : Le contexte fourni contient l’ensemble des informations nécessaires pour répondre à la question, notamment les procédures sur ADUM, les documents requis et les validations requises. Le système a correctement exploité ces éléments.

### Question : Quelles ressources le Pôle SAPS peut m’apporter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 57.99s, Eval: 13.54s, Total: 71.53s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (co‑construction via la Boutique des sciences, formations, accompagnement de projets, organisation d’événements, projets arts‑sciences, contact) sont directement présentes dans le contexte. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond précisément à la question en listant les ressources que le Pôle SAPS peut offrir, sans digression.
- **Avis Context Precision** : Le contexte fourni contient l’ensemble des informations nécessaires : missions du pôle, types de formations, accompagnement, événements, projets arts‑sciences, contacts. Il est donc parfaitement ciblé.

### Question : Y a-t-il des alumni ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 1.0/5
- **Temps** : RAG: 80.32s, Eval: 8.47s, Total: 88.79s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne fait qu'énoncer un contact (Elysa Ragot, elysat.ragot@univ-tours.fr). Les contacts injectés sont exclus de la pénalisation de la fidélité, donc aucune affirmation n'est en contradiction avec le contexte. Aucun autre énoncé n'est présent, donc la fidélité est maximale.
- **Avis Answer Relevance** : La question porte sur l'existence d'alumni. La réponse fournit uniquement un contact et ne répond en rien à la question, ce qui la rend hors‑sujet.
- **Avis Context Precision** : Le contexte fourni décrit la procédure de soutenance de thèse et la composition des jurys, sans aucune mention d'alumni. Ainsi le contexte n'est pas pertinent pour répondre à la question.

### Question : Que propose le Pôle SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 58.18s, Eval: 15.97s, Total: 74.15s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : accompagnement des chercheurs (formations, conseils, dépôts de projets ANR/ APR‑IR/ européens, mise en relation avec des professionnels), organisation d’événements (DéTours des sciences, Finale « Ma thèse en 180 s », Village des sciences, festival (Re)Cherche et trouve), projets arts/sciences (Ma thèse en BD, Kaléidoscope, résidences d’artistes, Campement scientifique), actions grand public (Boutique des sciences, Apéro Sciences, Fête de la science) et formations doctorales (Jeudis des SAPS, préparation au concours, mentorat MeFILYA). Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question « Que propose le Pôle SAPS ? » en listant les services et activités proposés. Elle est ciblée et exhaustive au regard de la demande.
- **Avis Context Precision** : Le contexte fourni contient l’ensemble des informations nécessaires : missions du pôle, types d’événements, formations, projets arts/sciences, accompagnement des chercheurs, etc. Le système a donc récupéré un contexte très pertinent.

### Question : - Qu’est-ce qu’une invention ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 3.0/5
- **Temps** : RAG: 85.14s, Eval: 13.63s, Total: 98.77s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse contient des éléments qui ne sont pas présents dans le contexte, notamment la définition « solution technique nouvelle à un problème technique » et la référence à l'article L.611-6 du CPI. D'autres affirmations (ex. protection par brevet, exceptions pour salariés ou agents publics) sont bien présentes dans le texte, mais l'ensemble n'est pas entièrement traçable, d'où une note moyenne.
- **Avis Answer Relevance** : La réponse répond directement à la question « Qu’est‑ce qu’une invention ? » en donnant une définition et en précisant le cadre juridique, sans digression hors sujet.
- **Avis Context Precision** : Le contexte fourni porte principalement sur la mobilité des chercheurs, les dispositifs de valorisation et les règles de propriété intellectuelle, mais il ne contient pas de définition explicite d’une invention. Il offre néanmoins des informations juridiques utiles, ce qui rend le contexte partiellement pertinent.

### Question : - Je souhaite répondre à un Appel à projet?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 84.08s, Eval: 8.89s, Total: 92.97s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : le contexte indique qu’il existe des AAP colloques et des procédures HDR, précise les adresses e‑mail de Caroline Vaslin et d’Aurélie Petereau, ainsi que les dates limites (9 septembre 2026 pour les colloques et 15 jours avant la commission pour les HDR). Aucun élément n’est inventé.
- **Avis Answer Relevance** : La question demande comment répondre à un appel à projet. La réponse indique clairement les deux types d’appels possibles, les contacts à qui adresser le dossier et les échéances, répondant ainsi exactement à la demande.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires (types d’appels, contacts, dates limites). Il a donc été parfaitement ciblé pour répondre à la question.

### Question : je suis en arrêt de travail, qui dois-je contacter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 4.0/5
- **Temps** : RAG: 88.30s, Eval: 9.32s, Total: 97.62s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (liens vers les pages « Congés maladie des agents titulaires » et « Congés maladie des agents contractuels ») sont présentes dans le contexte. Le nom et l'e‑mail fournis sont des contacts ajoutés automatiquement ; selon les consignes, ils ne sont pas comptés comme hallucination.
- **Avis Answer Relevance** : La réponse répond directement à la question « qui dois‑je contacter ? » en indiquant les interlocuteurs selon le statut (titulaire ou contractuel) et en proposant un contact nommé, ce qui est pertinent et utile.
- **Avis Context Precision** : Le contexte contient les liens nécessaires pour orienter les agents vers la procédure de congé maladie, mais il ne fournit pas de nom de contact précis. Ainsi, le contexte est très pertinent mais légèrement incomplet pour la demande de contact exact.

### Question : Combien de temps va prendre mon inscription ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 83.44s, Eval: 12.04s, Total: 95.48s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : le délai dépend du passage par le bureau de l'école doctorale, il peut être plus long, et la date limite du 15 novembre est explicitement mentionnée. Le contact fourni (Christele Gaudron) apparaît dans le contexte ; le suffixe "-Bredif" ajouté n'est pas présent mais les règles précisent que les informations de contact ne sont pas pénalisées pour la fidélité.
- **Avis Answer Relevance** : La réponse répond directement à la question "Combien de temps va prendre mon inscription ?" en expliquant les facteurs qui influencent le délai et en donnant la date limite officielle (15 novembre). Aucun élément hors sujet n'est introduit.
- **Avis Context Precision** : Le contexte contient les informations nécessaires : mention du délai plus long si le bureau de l'école doctorale examine le dossier et la date butoir du 15 novembre. Ces éléments sont exactement ceux exploités dans la réponse.

### Question : Comment avoir un email ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 185.96s, Eval: 12.02s, Total: 197.98s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte. Le texte indique que le compte email du doctorant est créé automatiquement (voir la partie « Nouvel arrivant doctorant ») et que le personnel doit contacter le service informatique ou la DSI (adresse dsi@univ-tours.fr) – ces informations figurent dans le contexte. Le contact général du PJR (drv-pi@univ-tours.fr) est également listé dans le contexte. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La question « Comment avoir un email ? » reçoit une réponse directe : création automatique pour les doctorants, procédure de contact pour le personnel, et un contact générique. La réponse répond exactement à la demande sans digression.
- **Avis Context Precision** : Le contexte fourni contient les informations nécessaires : description du compte email pour les doctorants, procédure de demande pour le personnel, et adresses de contact (dsi@univ-tours.fr, drv-pi@univ-tours.fr). Le système a donc récupéré un contexte parfaitement pertinent.

### Question : - Je souhaite me procurer le formulaire de déclaration d’invention de l’université, à qui dois-je m’adresser ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 82.67s, Eval: 9.73s, Total: 92.40s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les informations fournies dans la réponse (contacter le PJR via l'adresse générique drv-pi@univ-tours.fr) sont présentes dans le contexte. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond directement à la question en indiquant à qui s'adresser pour obtenir le formulaire de déclaration d’invention.
- **Avis Context Precision** : Le contexte contient l'adresse générique recommandée pour les questions de propriété intellectuelle, qui est exactement ce qui est cité dans la réponse.

### Question : Qui contacter pour toute demande d'ouvrages en service presse ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 2.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 84.25s, Eval: 11.07s, Total: 95.32s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient que des informations présentes dans le contexte (l'adresse e‑mail drv-pi@univ-tours.fr). Aucun élément externe n'est ajouté, mais l'attribution de ce contact à la demande d'ouvrages en service presse n'est pas justifiée par le texte, ce qui constitue une légère inférence non explicitée.
- **Avis Answer Relevance** : La question porte sur le contact à joindre pour des demandes d'ouvrages en service presse. La réponse indique un contact générique pour les questions de propriété intellectuelle, ce qui ne répond pas réellement à la demande spécifique.
- **Avis Context Precision** : Le contexte fourni décrit les contacts du Pôle Juridique Recherche et les domaines de compétence (propriété intellectuelle, conventions, etc.). Il ne mentionne aucun service presse ni aucune procédure liée aux ouvrages en service presse, donc le contexte n'est pas pertinent pour la question.

### Question : comment enregistrer ma demande de formation hors-catalogue et quels documents dois-je fournir ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 2.0/5, Context Precision: 1.0/5
- **Temps** : RAG: 82.28s, Eval: 8.98s, Total: 91.26s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient que l'adresse e‑mail drv-pi@univ-tours.fr, qui figure bien dans le contexte fourni. Aucun élément n'est ajouté qui ne provienne pas du contexte, donc la fidélité est maximale.
- **Avis Answer Relevance** : La question porte sur la procédure d'enregistrement d'une demande de formation hors‑catalogue et les documents à fournir. La réponse ne fournit que le contact général du PJR, sans expliquer la démarche ni les pièces requises. Elle ne répond donc pas réellement à la demande.
- **Avis Context Precision** : Le contexte récupéré décrit l'organisation du Pôle Juridique Recherche, ses missions et ses contacts, mais ne contient aucune information relative aux formations hors‑catalogue. Le contexte n'est donc pas pertinent pour répondre à la question.

### Question : Mon jury de thèse est-il valide ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 137.34s, Eval: 13.23s, Total: 150.57s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (nombre de membres, répartition entre professeurs et extérieurs, présence d'un HDR, limitation d'un seul émérite, équilibre femmes/hommes) sont directement tirées du contexte. Le seul élément qui n’apparaît pas dans le texte est l’adresse e‑mail de contact, mais les consignes précisent de ne pas pénaliser les contacts injectés.
- **Avis Answer Relevance** : La réponse répond à la question en donnant les critères à vérifier pour juger de la validité d’un jury. Elle ne fournit pas de jugement définitif (car aucun détail du jury n’est donné), mais elle donne l’information nécessaire pour que l’utilisateur puisse l’évaluer lui‑même.
- **Avis Context Precision** : Le contexte contient de nombreuses sections détaillant la composition du jury (nombre de membres, répartition, rôle de l’émérite, HDR, équilibre de genre, membres invités, etc.). Ces informations sont exactement celles utilisées dans la réponse.

### Question : quels types de financement de thèse existent ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 83.78s, Eval: 13.82s, Total: 97.60s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les catégories mentionnées dans la réponse (contrats doctoraux, bourses régionales, ANR, Europe, Labex, contrats de recherche/entreprise, CIFRE/DGA/ADEME, bourses étrangères, associatives, industrielles, doctorants salariés) sont présentes textuellement dans le contexte. Le contact ajouté n'est pas pénalisé selon la règle d'exemption.
- **Avis Answer Relevance** : La réponse répond directement à la question en listant les différents types de financement de thèse, sans digression majeure.
- **Avis Context Precision** : Le contexte fourni contient une section "Autres financements doctoraux" qui recense précisément les types de financement cités dans la réponse, ainsi que des précisions supplémentaires sur les contrats doctoraux régionaux et d'établissement.

### Question : - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autre CHRU?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 85.14s, Eval: 10.03s, Total: 95.17s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement soutenues par le contexte : le besoin d’un dossier CODECOH pour la manipulation d’échantillons biologiques humains, la disponibilité d’un lien intranet et les contacts du Référent Dossier CODECOH et du Conseiller de prévention. Le contact ajouté (Claude‑Emmanuel Boudet) est un contact injecté et, selon les règles, ne pénalise pas la fidélité.
- **Avis Answer Relevance** : La question porte sur l’utilisation d’échantillons provenant du CHRU de Tours ou d’un autre CHRU. La réponse indique clairement la procédure à suivre (dossier CODECOH) et fournit les contacts utiles, répondant ainsi directement à la demande.
- **Avis Context Precision** : Le contexte récupéré contient l’information nécessaire sur le dossier CODECOH et les contacts associés, ainsi que des mentions générales du CHRU de Tours. Ces éléments sont suffisants pour répondre à la question.

### Question : Je souhaite monter un projet, comment faire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 89.00s, Eval: 16.78s, Total: 105.78s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (contact du service SCRIPT, rôle du chef de projet, dépôt au COPIL, fréquence des réunions, accompagnement du SCRIPT, contact de Caroline Vaslin) sont directement présentes dans le contexte. Le seul contact supplémentaire (Justine Gillet) est un renseignement de contact qui, selon les règles, n’est pas pénalisé même s’il n’apparaît pas dans le contexte.
- **Avis Answer Relevance** : La réponse répond précisément à la question « Je souhaite monter un projet, comment faire ? » en décrivant les étapes concrètes à suivre pour monter un projet à l'Université de Tours. Aucun élément hors sujet n’est introduit.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires (procédure de montage, rôle du SCRIPT, exigences du COPIL, contacts, etc.) et il a été correctement exploité.

### Question : - Comment protéger un savoir-faire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 93.69s, Eval: 13.93s, Total: 107.62s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte. Le texte indique qu'une convention de collaborateur bénévole doit contenir des clauses de confidentialité et de cession des droits de propriété intellectuelle, ce qui correspond exactement à la réponse. L'adresse e‑mail fournie est un contact injecté et, selon les règles, ne doit pas être pénalisée.
- **Avis Answer Relevance** : La réponse répond directement à la question « Comment protéger un savoir‑faire ? » en proposant la mesure principale (signature d’une convention avec clauses de confidentialité et de cession) et en indiquant le point de contact pour mettre en œuvre cette mesure.
- **Avis Context Precision** : Le contexte récupéré contient les informations nécessaires : il décrit l’importance de la confidentialité, l’obligation de conventions pour les bénévoles/émérites, et la nécessité de prévoir la cession des droits de propriété industrielle. Le contexte est donc parfaitement pertinent.

### Question : Je pars en mission, quelle pièce dois-je remplir ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 85.27s, Eval: 7.06s, Total: 92.33s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : le formulaire à remplir est le « formulaire d'autorisation de déplacement » et le lien fourni correspond exactement à celui du contexte. Le contact ajouté n'est pas pénalisé selon la règle d'exemption des contacts.
- **Avis Answer Relevance** : La réponse répond exactement à la question « quelle pièce dois-je remplir ? » en indiquant le formulaire requis, ce qui constitue une réponse ciblée et complète.
- **Avis Context Precision** : Le contexte contient explicitement la mention du formulaire d'autorisation de déplacement ainsi que le lien de téléchargement, ce qui fournit toutes les informations nécessaires pour répondre à la question.

### Question : Quel est le délai moyen entre la soumission d’un manuscrit et sa publication ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 189.92s, Eval: 8.36s, Total: 198.28s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient aucune affirmation factuelle qui contredirait le contexte. Le seul élément ajouté est une information de contact qui, selon les règles, n'est pas pénalisée même si elle n'apparaît pas dans le contexte. Aucun autre contenu n'est halluciné.
- **Avis Answer Relevance** : La question porte sur le délai moyen entre la soumission d’un manuscrit et sa publication. La réponse fournie ne mentionne aucun délai, se limitant à un contact, ce qui ne répond pas du tout à la question.
- **Avis Context Precision** : Le contexte récupéré inclut explicitement les informations sur les délais d'embargo (maximum 6 mois pour les sciences, technique, médecine et 12 mois pour les sciences humaines et sociales), qui sont directement pertinentes pour répondre à la question.

## 06_google_mono

### Question : C’est quoi les SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 61.49s, Eval: 11.80s, Total: 73.29s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (définition de SAPS, objectif de renforcer le dialogue entre chercheurs et citoyens, rôle du Pôle SAPS d’accompagnement, organisation d’événements et réponse aux sollicitations) sont directement présentes dans le contexte. L’adresse e‑mail figure également dans le contexte, et les règles d’évaluation excluent les contacts de la pénalité de fidélité.
- **Avis Answer Relevance** : La question demande « C’est quoi les SAPS ? ». La réponse fournit la définition, le but et les principales activités, répondant ainsi exactement à la demande sans digression.
- **Avis Context Precision** : Le contexte récupéré contient la définition du sigle, les objectifs, les missions et les contacts du Pôle SAPS. Il est donc parfaitement adapté pour répondre à la question.

### Question : Comment peut-on changer le budget d’un projet ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 110.67s, Eval: 15.82s, Total: 126.49s
- **Tokens générés** : 0
- **Avis Faithfulness** : La majorité des informations (passage par le SPIV, besoin d’un argumentaire scientifique, budget modifié validé par l’antenne financière, attente du retour du financeur) sont directement tirées du contexte. En revanche, la réponse invente le nom « Anne Galopin » et l’adresse e‑mail « af.polytech@univ‑tours.fr », qui n’apparaissent nulle part dans le texte fourni. Cette hallucination empêche d’attribuer la note maximale.
- **Avis Answer Relevance** : La réponse répond précisément à la question : elle décrit la procédure à suivre pour modifier le budget d’un projet, en mentionnant le passage obligatoire par le SPIV et les exigences associées. Aucun élément hors sujet n’est introduit.
- **Avis Context Precision** : Le contexte contient une section détaillée sur la gestion des aléas et les demandes de modification budgétaire, incluant toutes les étapes nécessaires. Le système a donc pu puiser les informations requises.

### Question : Quelles sont les différentes démarches à effectuer ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 1.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 87.73s, Eval: 14.29s, Total: 102.02s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne cite aucune information présente dans le contexte. Elle affirme que la demande est trop générale et propose de contacter un service à une adresse e‑mail qui n’apparaît pas dans le texte fourni. Ces affirmations ne sont donc pas traçables au contexte (à l’exception de la règle qui exclut les contacts de la pénalisation, mais elles restent hors du contexte).
- **Avis Answer Relevance** : La question demandait les différentes démarches à effectuer. La réponse se contente de dire que la demande est trop générale et invite à contacter un service, sans fournir aucune des démarches décrites dans le contexte. Elle ne répond donc pas du tout à la question.
- **Avis Context Precision** : Le contexte récupéré contient de nombreuses informations précises sur les démarches (saisine de la HATVP, constitution d’une instance, définition de sa composition, options d’organisation, constitution du dossier, critères d’évaluation, délais, etc.). Il est donc pleinement pertinent et complet pour répondre à la question.

### Question : - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire extérieur? Est-ce gratuit?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 3.0/5, Context Precision: 4.0/5
- **Temps** : RAG: 91.46s, Eval: 12.89s, Total: 104.35s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : le besoin d’un contrat pour tout projet avec un partenaire extérieur et la présence du contact Hélène Jullien. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse traite du cadre (contrat) mais ne répond pas à la seconde partie de la question (« Est‑ce gratuit ? »). Elle ne fournit donc qu’une réponse partielle.
- **Avis Context Precision** : Le contexte contient les informations nécessaires sur l’obligation contractuelle et les interlocuteurs, ce qui permet de répondre à la question du cadre. Il manque toutefois une indication explicite sur la gratuité, ce qui rend le contexte légèrement incomplet pour la question complète.

### Question : A quelle adresse postale ou mail dois-je envoyer mon projet ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 1.0/5
- **Temps** : RAG: 83.89s, Eval: 6.91s, Total: 90.80s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont soit directement tirées du contexte, soit correspondent à des informations de contact qui, selon les règles, ne sont pas pénalisées même si elles n'apparaissent pas dans le contexte. Aucun élément de la réponse n'est donc considéré comme une hallucination.
- **Avis Answer Relevance** : La question demande une adresse postale ou mail pour envoyer le projet. La réponse fournit une adresse e‑mail, ce qui répond directement à la demande, même si aucune justification n'est fournie.
- **Avis Context Precision** : Le contexte fourni porte sur la définition juridique de collaborateurs bénévoles, l'éméritat, la propriété intellectuelle, etc. Il ne contient aucune information relative à une adresse postale ou e‑mail pour l'envoi d'un projet, ce qui rend le contexte non pertinent pour la question.

### Question : Comment m’inscrire / me réinscrire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 98.95s, Eval: 11.56s, Total: 110.51s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations (plateforme ADUM, période de juin à 15 novembre, mise à jour des informations, dépôt de la photo, du CV, du rapport d'activité et de la Convention Individuelle de Formation) sont directement présentes dans le contexte. Le contact ajouté (Marie Clermonte) est un contact et, selon la règle, n'est pas comptabilisé comme hallucination.
- **Avis Answer Relevance** : La réponse répond exactement à la question « Comment m’inscrire / me réinscrire ? » en décrivant la procédure à suivre et en proposant un point de contact, ce qui la rend pleinement pertinente.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires (site ADUM, dates limites, documents à fournir, procédure de finalisation). Il est donc très précis pour répondre à la question.

### Question : Quelles ressources le Pôle SAPS peut m’apporter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 66.43s, Eval: 14.60s, Total: 81.03s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : conseils pour dépôts de projets (ANR, projets européens), aide au montage budgétaire, formations en vulgarisation/mediatraining, participation à la Fête de la science et au concours "Ma thèse en 180 secondes", projets Arts/Sciences comme "Ma thèse en BD", et l'adresse e‑mail saps@univ‑tours.fr. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond directement à la question en listant les ressources offertes par le Pôle SAPS (accompagnement de projets, formations, événements, projets arts/sciences, contact). Elle est donc pleinement pertinente.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations utilisées dans la réponse (missions, formations, événements, accompagnement de projets, contacts). Il était donc parfaitement adapté.

### Question : Y a-t-il des alumni ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 92.34s, Eval: 6.09s, Total: 98.43s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : le texte indique que l'ADUM collecte et diffuse des informations sur les doctorants et docteurs pour l'insertion professionnelle. Le contact fourni est exempté selon la règle des contacts injectés. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La question porte sur l'existence d'alumni. La réponse ne mentionne pas les alumni, se contentant de décrire l'ADUM et de proposer un contact, ce qui ne répond pas du tout à la demande.
- **Avis Context Precision** : Le contexte fourni décrit l'outil ADUM et ses fonctionnalités, mais ne contient aucune information concernant des alumni. Ainsi le contexte n'est que vaguement lié au sujet de la question.

### Question : Que propose le Pôle SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 64.63s, Eval: 15.01s, Total: 79.64s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse se retrouvent dans le contexte : le Pôle SAPS facilite le dialogue entre chercheurs et société, répond aux sollicitations extérieures (Boutique des sciences), organise des événements (DéTours des sciences, Ma thèse en 180 secondes) et accompagne les chercheurs (conseil, formations). Les projets arts‑sciences « Ma thèse en BD » et « Kaléidoscope » sont également mentionnés dans le contexte. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La question porte sur ce que propose le Pôle SAPS. La réponse décrit clairement les trois missions principales et cite des projets concrets, répondant donc directement à la demande.
- **Avis Context Precision** : Le contexte fourni contient l’ensemble des informations nécessaires (missions, exemples d’événements, projets arts‑sciences, contacts). Il est donc parfaitement adapté à la question.

### Question : - Qu’est-ce qu’une invention ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 4.0/5
- **Temps** : RAG: 148.97s, Eval: 7.57s, Total: 156.54s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse se limite à une définition de l'invention (nouveauté, caractère inventif, application industrielle) qui correspond à la notion juridique évoquée dans le contexte (inventions susceptibles d'être protégées par un brevet, références aux articles R.611-1). Aucun élément inventé n'est présent, le seul ajout est une adresse e‑mail de contact, qui selon les règles ne pénalise pas la fidélité.
- **Avis Answer Relevance** : La question demandait simplement la définition d’une invention. La réponse fournit exactement cette définition et ajoute un contact utile, ce qui reste pertinent.
- **Avis Context Precision** : Le contexte récupéré porte largement sur les inventions, les décrets et les régimes applicables, incluant la notion d’invention brevetable. Bien qu’il ne contienne pas une définition formulée mot pour mot, il fournit suffisamment d’informations pour dériver la définition donnée.

### Question : - Je souhaite répondre à un Appel à projet?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 92.58s, Eval: 13.59s, Total: 106.17s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations (remplir le formulaire, inclure un argumentaire, l'avis du responsable d'unité et fournir un budget prévisionnel) sont directement présentes dans le contexte. Le contact mentionné (Caroline Vaslin) n'est pas dans le contexte, mais la règle indique de ne pas pénaliser les informations de contact absentes.
- **Avis Answer Relevance** : La réponse répond à la demande d'aide pour répondre à un appel à projet en se concentrant sur l'appel à projets de colloques 2027, ce qui est pertinent. Elle ne couvre pas les autres types d'appels (mobilité, congrès), d'où une petite perte de pertinence.
- **Avis Context Precision** : Le contexte fourni contient les informations nécessaires sur l'appel à projets de colloques 2027, le formulaire, le budget et les exigences, ce qui permet de répondre correctement.

### Question : je suis en arrêt de travail, qui dois-je contacter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 3.0/5
- **Temps** : RAG: 91.45s, Eval: 8.67s, Total: 100.12s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont soit présentes dans le contexte (les liens vers les pages de congés maladie), soit il s'agit d'un contact (nom et e‑mail) qui, bien que non présent dans le contexte, est explicitement exempté de pénalité selon la règle des contacts injectés. Aucun élément n'est halluciné.
- **Avis Answer Relevance** : La réponse répond directement à la question en indiquant la personne à contacter et fournit en plus des liens utiles pour les procédures de congé maladie, ce qui est pleinement pertinent.
- **Avis Context Precision** : Le contexte fournit des informations générales sur les congés maladie et des liens vers les pages correspondantes, mais il ne mentionne pas explicitement le contact à joindre. Ainsi, le contexte est partiellement utile mais ne contient pas l'information clé recherchée.

### Question : Combien de temps va prendre mon inscription ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 89.05s, Eval: 15.08s, Total: 104.13s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : le texte indique que le délai de traitement peut être rallongé pour les dossiers avec un diplôme étranger ou un DEA. Aucun autre fait n'est ajouté. Les informations de contact sont exemptées de pénalité selon la règle fournie.
- **Avis Answer Relevance** : La réponse traite de la durée de l'inscription en mentionnant la possible rallonge du délai et propose de contacter le service pour plus de précisions, ce qui répond partiellement à la question. Elle ne fournit pas de durée précise, mais le contexte ne le propose pas non plus.
- **Avis Context Precision** : Le contexte contient l'information clé sur le rallongement du délai pour les diplômes étrangers/DEA, ainsi que d'autres détails sur le processus d'inscription. Cette information a été correctement utilisée.

### Question : Comment avoir un email ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 163.66s, Eval: 13.88s, Total: 177.54s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (existence d'un compte étudiant @etu.univ-tours.fr, présence d'une messagerie, contacts dsi@univ-tours.fr et drv-pi@univ-tours.fr) sont directement présentes dans le contexte fourni. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond à la question « Comment avoir un email ? » en indiquant que le doctorant possède automatiquement une adresse e‑mail et en donnant les contacts utiles. Elle ne traite pas d’autres sujets, mais elle ne fournit pas de procédure détaillée, d’où un léger manque de précision.
- **Avis Context Precision** : Le contexte contient clairement l’information selon laquelle chaque doctorant de l'Université de Tours dispose d’un compte informatique incluant une messagerie, ainsi que les adresses de contact. Le contexte est donc parfaitement adapté.

### Question : - Je souhaite me procurer le formulaire de déclaration d’invention de l’université, à qui dois-je m’adresser ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 87.92s, Eval: 7.87s, Total: 95.79s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les informations de la réponse sont présentes dans le contexte : le Pôle Juridique Recherche (PJR) est mentionné comme responsable des déclarations d'invention et l'adresse e‑mail générique drv-pi@univ-tours.fr est fournie dans la section Contacts. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La question demande à qui s’adresser pour obtenir le formulaire de déclaration d’invention. La réponse indique clairement le service (PJR) et l’adresse e‑mail appropriée, répondant directement à la demande.
- **Avis Context Precision** : Le contexte contient les informations nécessaires : rôle du PJR (instruction des déclarations d’invention) et le contact générique drv-pi@univ-tours.fr. Ces éléments sont exactement ceux utilisés dans la réponse.

### Question : Qui contacter pour toute demande d'ouvrages en service presse ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 1.0/5
- **Temps** : RAG: 86.29s, Eval: 8.43s, Total: 94.72s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient aucune affirmation factuelle autre que le contact fourni. Les informations de contact sont explicitement exemptées de pénalisation selon les règles, même si elles n'apparaissent pas dans le contexte. Aucun autre élément n'est halluciné.
- **Avis Answer Relevance** : La question porte sur le contact à joindre pour les ouvrages en service presse. La réponse indique clairement le service (PJR) et l'adresse e‑mail, répondant directement à la demande.
- **Avis Context Precision** : Le contexte récupéré traite de droit d'auteur, de cessions de droits, de jurisprudence, etc., et ne mentionne aucun service PJR ni aucune adresse e‑mail liée aux ouvrages en service presse. Il ne fournit donc aucune information pertinente pour répondre à la question.

### Question : comment enregistrer ma demande de formation hors-catalogue et quels documents dois-je fournir ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 3.0/5, Context Precision: 1.0/5
- **Temps** : RAG: 91.76s, Eval: 9.66s, Total: 101.42s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont compatibles avec le contexte : le texte ne contient aucune information sur la procédure d’enregistrement d’une formation hors‑catalogue, et la réponse indique justement qu’elle ne dispose pas de ces informations. Le contact fourni n’est pas présent dans le contexte, mais la règle d’exemption des contacts injectés empêche de le pénaliser.
- **Avis Answer Relevance** : La réponse reconnaît son incapacité à répondre à la question et propose un contact. Cela répond partiellement à la demande de l’utilisateur (en orientant vers une aide), mais ne fournit pas la procédure ni la liste des documents attendus, ce qui la rend seulement moyennement pertinente.
- **Avis Context Precision** : Le contexte récupéré porte sur le droit d’auteur et la cession de droits d’œuvres d’agents publics, sans aucune mention de formation hors‑catalogue ou de documents requis. Il est donc totalement hors sujet par rapport à la question.

### Question : Mon jury de thèse est-il valide ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 201.22s, Eval: 11.82s, Total: 213.04s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont compatibles avec le contexte. Le système indique qu'il ne possède pas la composition du jury, ce qui est vrai puisque le contexte ne fournit pas ces données. L'adresse e‑mail fournie n'apparaît pas dans le contexte, mais les consignes précisent de ne pas pénaliser les contacts injectés.
- **Avis Answer Relevance** : La réponse répond à la question en expliquant qu'elle ne peut pas vérifier la validité du jury faute de données et en proposant un contact pour obtenir une validation officielle. Elle reste pertinente, bien que n'apporte pas d'analyse du jury.
- **Avis Context Precision** : Le contexte contient de nombreuses informations sur les règles de composition d'un jury de thèse, mais il ne fournit pas la composition spécifique du jury de l'utilisateur. Ainsi, le contexte n'est pas suffisamment précis pour répondre directement à la question.

### Question : quels types de financement de thèse existent ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 84.60s, Eval: 12.94s, Total: 97.54s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les catégories mentionnées dans la réponse (contrats doctoraux d'établissement, régionaux ou ministériels, bourses départementales, industrielles, associatives, étrangères, financements ANR, Europe, Labex, ADEME, DGA, conventions CIFRE, salariés du public ou du privé) sont explicitement présentes dans le contexte fourni. Aucun élément n'est inventé ; le contact ajouté n'est pas pénalisé selon la règle.
- **Avis Answer Relevance** : La réponse répond directement à la question en listant les différents types de financement de thèse, sans digression ni hors-sujet.
- **Avis Context Precision** : Le contexte récupéré contient une section détaillée sur les « Autres financements doctoraux » qui recense exactement les types cités dans la réponse, ainsi que des précisions sur les contrats et les salariés, ce qui montre que le contexte était pleinement pertinent.

### Question : - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autre CHRU?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 3.0/5, Context Precision: 3.0/5
- **Temps** : RAG: 82.73s, Eval: 19.47s, Total: 102.20s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations factuelles de la réponse (nécessité d'un Dossier CODECOH pour manipuler des échantillons biologiques humains) sont directement présentes dans le contexte. Les coordonnées de contact ajoutées ne figurent pas dans le contexte, mais la consigne indique de ne pas pénaliser ces informations pour la fidélité.
- **Avis Answer Relevance** : La réponse traite du besoin d'un dossier réglementaire pour les échantillons humains, ce qui est partiellement lié à la question sur les échantillons du CHRU. Cependant, elle ne répond pas spécifiquement à la question de savoir si l'on peut utiliser des échantillons provenant du CHRU de Tours ou d'un autre CHRU, ni aux modalités d'affiliation ou de partenariat mentionnées dans le contexte.
- **Avis Context Precision** : Le contexte contient des informations sur les exigences réglementaires (Dossier CODECOH) ainsi que des sections sur les affiliations et les signatures pour le CHRU de Tours. Il fournit donc partiellement les éléments nécessaires pour répondre à la question, mais il manque des indications précises sur l'utilisation des échantillons du CHRU.

### Question : Je souhaite monter un projet, comment faire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 97.39s, Eval: 8.70s, Total: 106.09s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : le besoin de saisir le service SCRIPT en amont, l’accompagnement administratif, juridique et financier, et l’obligation de passer par ce service. Les coordonnées ajoutées (Justine Gillet, email, téléphone) ne sont pas pénalisées selon la règle sur les contacts injectés.
- **Avis Answer Relevance** : La réponse répond directement à la question « comment monter un projet » en indiquant la démarche principale (contacter le service SCRIPT). Elle reste pertinente, même si elle ne détaille pas l’ensemble du processus décrit dans le contexte.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires pour répondre à la question, notamment l’obligation de contacter le service SCRIPT, le rôle d’accompagnement, et la nécessité d’une saisine préalable.

### Question : - Comment protéger un savoir-faire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 82.99s, Eval: 11.69s, Total: 94.68s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse se retrouvent dans le contexte : le Pôle Juridique Recherche (PJR) et son adresse e‑mail drv-pi@univ-tours.fr sont mentionnés, tout comme la possibilité de sécuriser les informations via un accord ou une charte de confidentialité. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond à la question en proposant un moyen concret (contacter le PJR) et en rappelant l’usage d’accords de confidentialité, ce qui est pertinent pour protéger un savoir‑faire. Cependant, elle ne développe pas d’autres pistes (brevets, conventions spécifiques, stratégie de protection) présentes dans le contexte, d’où une note légèrement inférieure.
- **Avis Context Precision** : Le contexte fourni contient les informations nécessaires : contacts du PJR, rôle du PJR en propriété intellectuelle, et l’importance des accords de confidentialité. Le contexte est donc parfaitement adapté.

### Question : Je pars en mission, quelle pièce dois-je remplir ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 84.11s, Eval: 0.00s, Total: 84.11s
- **Tokens générés** : 0

### Question : Quel est le délai moyen entre la soumission d’un manuscrit et sa publication ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 3.0/5
- **Temps** : RAG: 212.28s, Eval: 12.12s, Total: 224.40s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient aucune affirmation qui ne se trouve pas dans le contexte. Elle indique simplement qu'aucune information sur le délai moyen n'est disponible, ce qui est conforme au fait que le contexte ne fournit pas de valeur moyenne. Le contact ajouté n'est pas pénalisé selon la règle des contacts injectés.
- **Avis Answer Relevance** : La réponse répond à la question en indiquant l'absence d'information, ce qui est pertinent. Cependant, elle aurait pu exploiter le fait que le texte mentionne un délai maximal (6 mois ou 12 mois) comme information partielle, d'où une petite perte de pertinence.
- **Avis Context Precision** : Le contexte contient des informations sur le délai maximal de mise à disposition (6 mois pour les sciences, 12 mois pour les SHS), mais ne donne pas de délai moyen. Ainsi le contexte est partiellement utile, mais ne répond pas exactement à la question posée.

## 07_qwen_mono

### Question : C’est quoi les SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 56.17s, Eval: 11.32s, Total: 67.49s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement tirées du contexte : SAPS = Sciences Avec et Pour la Société, cadre de la loi de programmation de la recherche 2021, objectif de renouer le pacte entre chercheurs et citoyens, et rôle du Pôle SAPS à l'Université de Tours pour faciliter le dialogue et la médiation scientifique. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question « C’est quoi les SAPS ? » en donnant une définition claire, le cadre législatif et l’objectif principal, ainsi qu’une illustration concrète à l'Université de Tours.
- **Avis Context Precision** : Le contexte fourni contient la définition, le cadre légal, les objectifs et la présence du Pôle SAPS à l'Université de Tours. Il est donc parfaitement adapté pour répondre à la question.

### Question : Comment peut-on changer le budget d’un projet ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 107.96s, Eval: 16.26s, Total: 124.22s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations concernant la procédure (contacter le SPIV, fournir un argumentaire scientifique et un budget actualisé validé par l'antenne financière) sont présentes dans le contexte. Le seul élément qui n’apparaît pas dans le contexte est le nom et l’e‑mail du contact (Anne Galopin, af.polytech@univ-tours.fr). Conformément à la règle, les informations de contact ne sont pas pénalisées pour la fidélité, d’où la note maximale.
- **Avis Answer Relevance** : La réponse répond directement à la question en indiquant les étapes à suivre pour modifier le budget d’un projet. Elle fournit le point de contact et les documents requis, ce qui correspond exactement à ce qui est demandé.
- **Avis Context Precision** : Le contexte contient les informations nécessaires : il indique qu’une modification budgétaire doit passer par le SPIV/SPV, qu’il faut un argumentaire scientifique et un budget révisé validé par l’antenne financière. Le contexte est donc parfaitement adapté.

### Question : Quelles sont les différentes démarches à effectuer ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 4.0/5, Context Precision: 4.0/5
- **Temps** : RAG: 84.53s, Eval: 8.94s, Total: 93.47s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse se base presque exclusivement sur le contexte fourni : elle mentionne le PJR, les domaines d’intervention (propriété intellectuelle, éméritat, conventions) et le contact générique drv-pi@univ-tours.fr, tous présents dans le texte. Cependant, le terme « mobilité » n’apparaît nulle part dans le contexte, ce qui constitue une légère hallucination. D’où la note 4.
- **Avis Answer Relevance** : La question est très vague. La réponse indique correctement que davantage de précision est nécessaire avant de pouvoir lister les démarches, ce qui répond à la demande de clarification. Elle ne fournit pas les démarches elles‑mêmes, mais la demande de précision est pertinente face à l’ambiguïté de la question. Note 4.
- **Avis Context Precision** : Le contexte récupéré contient de nombreuses informations sur les missions du PJR et les types de procédures (déclaration d’invention, conventions, etc.), ce qui est pertinent pour répondre à la question. Il manque toutefois un passage explicite listant « les différentes démarches », ce qui rend le contexte légèrement incomplet pour une réponse directe. Note 4.

### Question : - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire extérieur? Est-ce gratuit?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 100.88s, Eval: 8.14s, Total: 109.02s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : le cadre du montage d'un projet ou d'un contrat de recherche, la nécessité d'une convention, l'absence de contrepartie financière de l'UT, et les contacts du service SPIV. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond précisément à la question en indiquant le cadre (projet/contrat de recherche avec convention) et en précisant que l'accueil est sans contrepartie financière pour l'Université, ce qui répond à la partie « Est‑ce gratuit ? ».
- **Avis Context Precision** : Le contexte fourni contient les informations nécessaires (convention, gratuité de l'accueil, service SPIV, contacts) et celles‑ci sont exploitées dans la réponse.

### Question : A quelle adresse postale ou mail dois-je envoyer mon projet ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 87.11s, Eval: 12.00s, Total: 99.11s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont soit présentes dans le contexte, soit correspondent à un contact injecté (drv-pi@univ-tours.fr). Aucun élément factuel supplémentaire n'est inventé, donc aucune pénalité n'est appliquée conformément à la règle sur les contacts injectés.
- **Avis Answer Relevance** : La réponse fournit une adresse e‑mail où l'utilisateur peut se renseigner, ce qui répond partiellement à la question « adresse postale ou mail ». Elle ne donne pas d’adresse postale précise, mais reste pertinente pour la demande d’envoi du projet.
- **Avis Context Precision** : Le contexte fourni porte sur les règles d’éméritat, la propriété intellectuelle, etc., et ne contient aucune information d’adresse postale ou e‑mail. Le contexte n’est donc pas pertinent pour répondre à la question posée.

### Question : Comment m’inscrire / me réinscrire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 84.27s, Eval: 9.18s, Total: 93.45s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : l'inscription et la réinscription se font via l'espace personnel ADUM. Le contact fourni est exempté de pénalité selon la règle sur les contacts injectés, même s'il n'apparaît pas dans le contexte.
- **Avis Answer Relevance** : La réponse répond à la question en indiquant le canal (espace personnel ADUM) et propose un interlocuteur pour assistance, ce qui est pertinent. Elle reste toutefois très succincte et n'apporte pas les étapes détaillées attendues.
- **Avis Context Precision** : Le contexte contient l'ensemble des informations nécessaires (description d'ADUM, procédure de création de compte, période de réinscription, tutoriels, etc.). Il est donc parfaitement adapté à la question.

### Question : Quelles ressources le Pôle SAPS peut m’apporter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 116.35s, Eval: 18.24s, Total: 134.59s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse se retrouvent textuellement dans le contexte : le Pôle SAPS propose du conseil, du montage de projets (ANR, européens), la mise en relation avec des professionnels, des formations (vulgarisation, mediatraining, mentorat MeFILYA) et organise les "Jeudis des SAPS" ainsi que le concours "Ma thèse en 180 secondes". L’adresse e‑mail saps@univ‑tours.fr figure également dans le contexte. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La question porte sur les ressources que le Pôle SAPS peut apporter. La réponse liste précisément ces ressources (conseil, montage de projets, mise en relation, formations, événements) et indique le contact, répondant ainsi de façon ciblée et exhaustive aux attentes de l’interlocuteur.
- **Avis Context Precision** : Le contexte fourni contient l’ensemble des informations nécessaires : missions du Pôle SAPS, types d’accompagnement, catalogue de formations, événements organisés, contacts. Il est donc parfaitement adapté pour répondre à la question.

### Question : Y a-t-il des alumni ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 193.01s, Eval: 9.73s, Total: 202.74s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont compatibles avec le contexte. Le texte indique correctement que le contexte ne mentionne pas d'alumni. Le contact fourni (Elysa Ragot) n'apparaît pas dans le contexte, mais les consignes précisent de ne pas pénaliser les informations de contact injectées, donc la note reste maximale.
- **Avis Answer Relevance** : La réponse répond directement à la question « Y a-t-il des alumni ? » en précisant l'absence d'information dans le contexte et en proposant une démarche de suivi, ce qui est pleinement pertinent.
- **Avis Context Precision** : Le contexte fourni ne contient aucune information sur un réseau d'alumni ou d'anciens diplômés. Ainsi, le contexte n'est pas pertinent pour répondre à la question, ce qui justifie une note basse.

### Question : Que propose le Pôle SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 58.41s, Eval: 10.45s, Total: 68.86s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse se retrouvent textuellement ou implicitement dans le contexte : organisation d'événements (DéTours des sciences, Ma thèse en 180s), accompagnement de projets (conseil, montage budgétaire, résidences Kaléidoscope), formations (Jeudis des SAPS, médiation scientifique) et le contact saps@univ-tours.fr. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond à la question en décrivant ce que le Pôle SAPS propose, en présentant trois grands axes d'action. Elle est pertinente mais ne couvre pas l’ensemble des missions détaillées dans le contexte, d’où une note légèrement inférieure à la perfection.
- **Avis Context Precision** : Le contexte fourni contient une description très détaillée des missions, projets, formations, événements et contacts du Pôle SAPS, donc il est parfaitement adapté pour répondre à la question.

### Question : - Qu’est-ce qu’une invention ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 82.20s, Eval: 7.16s, Total: 89.36s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient aucune affirmation factuelle sur les inventions ; elle ne fournit qu'une adresse e‑mail de contact. Les informations de contact ne sont pas présentes dans le contexte, mais la consigne indique de ne pas pénaliser ces ajouts. Aucun élément du texte n’est donc halluciné.
- **Avis Answer Relevance** : La question demande la définition d’une « invention ». La réponse se limite à indiquer un contact et ne fournit aucune définition, ni aucune information liée à la question. Elle est donc hors sujet.
- **Avis Context Precision** : Le contexte porte largement sur les aspects juridiques des inventions (décret inventeurs, articles du CPI, droits de propriété industrielle, etc.), mais il ne contient pas de définition explicite du terme « invention ». Le contexte est donc seulement vaguement lié à la question et ne fournit pas l’information recherchée.

### Question : - Je souhaite répondre à un Appel à projet?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 3.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 80.01s, Eval: 8.40s, Total: 88.41s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont compatibles avec le contexte : le texte indique correctement que le contexte ne mentionne aucun appel à projets. Le contact fourni n'est pas présent dans le contexte, mais la règle indique de ne pas pénaliser les contacts ajoutés automatiquement.
- **Avis Answer Relevance** : La réponse répond partiellement à la question en indiquant l'absence d'information dans le contexte et en proposant de consulter d'autres sources, mais elle ne fournit aucune instruction concrète sur la façon de répondre à un appel à projets.
- **Avis Context Precision** : Le contexte récupéré porte exclusivement sur les démarches administratives de soutenance de thèse et d'HDR, aucune information relative aux appels à projets n'est présente, ce qui rend le contexte peu pertinent pour la question.

### Question : je suis en arrêt de travail, qui dois-je contacter ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 4.0/5
- **Temps** : RAG: 148.30s, Eval: 14.22s, Total: 162.52s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient aucune information factuelle erronée, à l'exception du nom et de l'e‑mail du contact qui ne figurent pas dans le contexte. Selon les consignes, les contacts ajoutés ne sont pas comptabilisés comme hallucination, donc la réponse reste fidèle aux informations disponibles. Le reste du texte (guidance sur les pièces à fournir) est une reformulation raisonnable des procédures évoquées dans le contexte, d'où une note de 4.
- **Avis Answer Relevance** : La question demande explicitement « qui dois‑je contacter ? » en cas d’arrêt de travail. La réponse fournit directement un interlocuteur, répondant ainsi parfaitement à la demande.
- **Avis Context Precision** : Le contexte indique qu’en cas d’arrêt ou de congé maladie il faut prendre contact avec un gestionnaire de la DRH (ou consulter l’organigramme). Il ne donne pas de nom précis, mais il fournit les éléments nécessaires pour identifier le bon service. Le contexte est donc pertinent mais ne précise pas le contact exact, justifiant une note de 4.

### Question : Combien de temps va prendre mon inscription ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 90.44s, Eval: 10.03s, Total: 100.47s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : le délai n'est pas fixé précisément, il est rallongé pour les dossiers avec diplôme étranger ou DEA, et il est recommandé de contacter l'interlocuteur administratif. Les informations de contact sont exemptées de pénalité selon la règle fournie.
- **Avis Answer Relevance** : La réponse répond directement à la question sur la durée de l'inscription en expliquant l'absence de durée précise et en indiquant les cas où le délai est plus long, ainsi que la démarche à suivre pour obtenir une estimation.
- **Avis Context Precision** : Le contexte récupéré contient les informations nécessaires (mention du délai rallongé pour certains dossiers, absence de durée fixe, procédure de suivi) pour répondre à la question.

### Question : Comment avoir un email ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 145.09s, Eval: 13.48s, Total: 158.57s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (le rôle du directeur de thèse, la nécessité de signaler le besoin au service informatique de proximité, la remise des identifiants à l'arrivée, le contact dsi@univ-tours.fr) sont directement présentes dans le contexte. Le seul élément supplémentaire est un contact (drv-pi@univ-tours.fr) qui, bien que non présent dans le contexte, est un contact et ne doit pas être pénalisé selon les règles.
- **Avis Answer Relevance** : La question « Comment avoir un email ? » est clairement répondue : la réponse explique la procédure pour obtenir une adresse email universitaire, ce qui correspond exactement à ce qui est demandé.
- **Avis Context Precision** : Le contexte fourni contient plusieurs passages détaillant la création de comptes email pour les doctorants, les interlocuteurs à contacter et les modalités (directeur de thèse, service informatique, adresse dsi@univ-tours.fr). Le contexte est donc parfaitement adapté.

### Question : - Je souhaite me procurer le formulaire de déclaration d’invention de l’université, à qui dois-je m’adresser ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 83.80s, Eval: 11.19s, Total: 94.99s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : le PJR gère les déclarations d'invention et l'adresse générique drv-pi@univ-tours.fr est fournie comme contact. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question en indiquant à qui s'adresser pour obtenir le formulaire de déclaration d’invention.
- **Avis Context Precision** : Le contexte contient l'information précise sur le service responsable (PJR) et l'adresse e‑mail générique à utiliser, ainsi que le rôle du PJR concernant les déclarations d'invention.

### Question : Qui contacter pour toute demande d'ouvrages en service presse ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 2.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 85.80s, Eval: 10.18s, Total: 95.98s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse indique que le contact général drv-pi@univ-tours.fr doit être utilisé. Cette adresse e‑mail figure bien dans le contexte, mais le texte du contexte ne précise pas qu’elle est destinée aux "demandes d'ouvrages en service presse". L’affirmation sur le rôle de ce contact n’est donc pas traçable dans le contexte, ce qui constitue une hallucination partielle.
- **Avis Answer Relevance** : La question porte sur le contact à joindre pour toute demande d'ouvrages en service presse. La réponse fournit un seul contact générique qui, d’après le contexte, concerne les questions générales de propriété intellectuelle, pas spécifiquement le service presse. La réponse ne répond donc pas correctement à la demande.
- **Avis Context Precision** : Le contexte fourni ne contient aucune information relative au "service presse" ou aux demandes d'ouvrages en service presse. Les seules informations pertinentes concernent les contacts du PJR et la propriété intellectuelle, ce qui n’est pas adéquat pour répondre à la question.

### Question : comment enregistrer ma demande de formation hors-catalogue et quels documents dois-je fournir ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 3.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 141.00s, Eval: 15.25s, Total: 156.25s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse se retrouvent dans le contexte : la procédure d'accès à ADUM, la sélection de « Déclaration des formations hors-catalogue », la nécessité de renseigner les détails de l'activité et de joindre la fiche de validation des crédits doctoraux ainsi que les justificatifs en un seul PDF. Aucun élément n'est inventé (les contacts sont exemptés de pénalité selon les règles).
- **Avis Answer Relevance** : La réponse répond à la partie « comment enregistrer » en donnant les étapes précises, mais la partie « quels documents fournir » reste vague (elle indique simplement « tous les justificatifs » sans les détailler). Ainsi, la réponse est partiellement pertinente.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires : procédure de déclaration, liste des documents à fournir (pièce d'identité, diplôme, attestation de présence, programme détaillé, etc.) et exigences de format. Le contexte est donc très précis.

### Question : Mon jury de thèse est-il valide ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 140.44s, Eval: 9.00s, Total: 149.44s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse se contente de demander la composition du jury et fournit un contact présent dans le contexte (drv-pi@univ-tours.fr). Aucun élément n’est inventé ; toutes les affirmations sont directement traçables dans le texte fourni.
- **Avis Answer Relevance** : La réponse répond à la demande de vérification en indiquant qu’il faut connaître la composition du jury pour juger de sa validité. Elle ne donne pas de verdict, mais oriente correctement l’utilisateur vers l’information manquante, ce qui reste pertinent bien que partiel.
- **Avis Context Precision** : Le contexte contient l’ensemble des règles de composition du jury (nombre de membres, proportion d’extérieurs, statut HDR/Professeur, parité, limitation des émérites, etc.) nécessaires pour évaluer la validité d’un jury. Le système a bien identifié que ces informations sont disponibles.

### Question : quels types de financement de thèse existent ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 86.28s, Eval: 11.11s, Total: 97.39s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les catégories de financement mentionnées dans la réponse (contrats doctoraux Ministère/Établissement/Région, bourses régionales, départementales, ANR, Europe, Labex, Campus France, conventions CIFRE/DGA/ADEME, contrats de recherche/entreprise, financement par salariat ou gouvernements étrangers) sont présentes dans le contexte fourni. Le contact ajouté n'est pas présent dans le contexte, mais la règle d'exemption des contacts injectés empêche toute pénalisation.
- **Avis Answer Relevance** : La réponse répond directement à la question en listant les différents types de financement de thèse. L'ajout du contact est une information supplémentaire mais ne détourne pas de la réponse demandée.
- **Avis Context Precision** : Le contexte contient une description détaillée des multiples sources de financement (ANR, Europe, Labex, CIFRE, bourses régionales, départementales, industrielles, associatives, contrats doctoraux, salariat, etc.). Il est donc parfaitement adapté pour répondre à la question.

### Question : - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autre CHRU?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 4.0/5
- **Temps** : RAG: 82.36s, Eval: 8.34s, Total: 90.70s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse se base sur le contexte : il est indiqué que la manipulation d'échantillons biologiques humains relève du dossier CODECOH et que le contact du référent est indiqué. L'affirmation que les documents ne précisent pas de procédure spécifique pour les échantillons du CHRU est une inférence raisonnable, non une invention d'information extérieure. Le contact fourni (Claude‑Emmanuel Boudet) n'est pas présent dans le contexte mais, selon la règle, les contacts injectés ne sont pas pénalisés.
- **Avis Answer Relevance** : La question porte sur l'existence d'une procédure pour des échantillons provenant du CHRU de Tours ou d'un autre CHRU. La réponse indique clairement qu'aucune procédure spécifique n'est mentionnée dans les documents et oriente l'utilisateur vers le référent CODECOH, ce qui répond directement à la demande.
- **Avis Context Precision** : Le contexte contient des informations pertinentes (dossier CODECOH, contacts de référents, mention du CHRU dans les règles d'affiliation) permettant de répondre à la question, mais il ne fournit pas de procédure détaillée propre au CHRU. Ainsi le contexte est pertinent mais incomplet pour une réponse très précise.

### Question : Je souhaite monter un projet, comment faire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 4.0/5
- **Temps** : RAG: 91.41s, Eval: 17.03s, Total: 108.44s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations concernant le rôle du service SCRIPT (accompagnement juridique, financier et administratif, coordination avec le COPIL et l'équipe présidentielle) sont directement présentes dans le contexte. Le seul élément qui n'apparaît pas dans le contexte est le contact "Justine Gillet" avec son e‑mail et téléphone ; selon les consignes, cet ajout de contact ne doit pas être pénalisé pour la fidélité.
- **Avis Answer Relevance** : La réponse propose une démarche concrète (contacter une personne ressource, puis passer par le service SCRIPT) qui répond à la demande de « comment monter un projet ». Elle reste pertinente même si elle ne détaille pas l’ensemble du processus décrit dans le contexte.
- **Avis Context Precision** : Le contexte fourni décrit précisément le processus de montage, le rôle du COPIL, les exigences de dossier, le recrutement, etc. La réponse utilise correctement ces informations pour indiquer que le service SCRIPT assure le montage. Le contexte ne contenait toutefois pas le nom du contact indiqué, mais cela n’affecte pas la pertinence du contexte.

### Question : - Comment protéger un savoir-faire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 85.16s, Eval: 12.81s, Total: 97.97s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes ou déductibles du contexte. Le texte indique que la protection du savoir‑faire passe par des accords de confidentialité et, le cas échéant, le dépôt de brevets. Le contact du Pôle Juridique Recherche (PJR) et son adresse e‑mail ne figurent pas dans le contexte, mais les consignes autorisent de ne pas pénaliser les informations de contact injectées.
- **Avis Answer Relevance** : La réponse répond directement à la question en proposant une démarche concrète (contacter le PJR) et en rappelant les principaux outils de protection (confidentialité, brevets). Elle reste pertinente, même si elle ne développe pas l’ensemble des mesures possibles.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires pour répondre à la question : il décrit l’importance des accords de confidentialité, les obligations liées aux collaborateurs bénévoles, les dispositions du Code de la propriété intellectuelle, et les possibilités de dépôt de brevets. Ainsi le contexte est parfaitement adapté.

### Question : Je pars en mission, quelle pièce dois-je remplir ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 86.41s, Eval: 9.22s, Total: 95.63s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : le formulaire à remplir est l'« Autorisation de Déplacement », la nécessité de joindre la carte grise en cas d'utilisation du véhicule personnel, et la transmission du dossier au gestionnaire 15 jours avant le départ. Le contact ajouté n'est pas pénalisé selon la règle sur les contacts injectés.
- **Avis Answer Relevance** : La réponse répond exactement à la question en indiquant la pièce à remplir (Autorisation de Déplacement) et fournit même des précisions utiles sans s'écarter du sujet.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires (nom du formulaire, pièces à joindre, délai de transmission) et elles sont correctement exploitées.

### Question : Quel est le délai moyen entre la soumission d’un manuscrit et sa publication ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 1.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 134.49s, Eval: 8.40s, Total: 142.89s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient aucune information tirée du contexte fourni. Elle se limite à un contact (PJR - drv-pi@univ-tours.fr) qui n'apparaît pas dans le texte. Bien que les contacts ne soient pas pénalisés pour la fidélité, aucune affirmation du contexte n'est reproduite, d'où la note minimale.
- **Avis Answer Relevance** : La question porte sur le délai moyen entre la soumission d’un manuscrit et sa publication. La réponse fournie ne répond pas du tout à cette interrogation et ne fournit aucune donnée temporelle, donc la pertinence est nulle.
- **Avis Context Precision** : Le contexte mentionne un délai maximal de mise à disposition (6 mois pour les sciences, 12 mois pour les SHS) après la première publication, ce qui est vaguement lié à la notion de délai, mais ne fournit pas le délai moyen demandé. Le contexte est donc seulement partiellement pertinent et manque de l'information exacte recherchée.

## 08_economy_cross

### Question : C’est quoi les SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 58.11s, Eval: 14.36s, Total: 72.47s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (définition de SAPS, lien avec la loi LPR 2021, objectif de renforcer le dialogue entre chercheurs et citoyens, reconnaissance comme dimension de l'activité scientifique) sont directement présentes dans le texte du contexte. L'adresse e‑mail fournie figure également dans la section Contacts, mais les contacts ne sont pas pénalisés selon les règles.
- **Avis Answer Relevance** : La réponse répond exactement à la question « C’est quoi les SAPS ? » en donnant une définition claire et en précisant son objectif principal.
- **Avis Context Precision** : Le contexte récupéré contient la définition, le cadre législatif (loi LPR 2021) et les objectifs des SAPS, ce qui est suffisant pour répondre à la question.

### Question : Comment peut-on changer le budget d’un projet ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 106.26s, Eval: 10.57s, Total: 116.83s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (passer par le SPIV, fournir un argumentaire scientifique, un budget modifié validé par l'antenne financière, attendre l'accord du financeur) sont directement présentes dans le texte du contexte. Le seul élément supplémentaire est le contact "Anne Galopin" et son e‑mail, mais les consignes précisent de ne pas pénaliser les informations de contact.
- **Avis Answer Relevance** : La réponse répond exactement à la question « Comment peut‑on changer le budget d’un projet ? » en décrivant la procédure à suivre. Aucun élément hors sujet n’est ajouté.
- **Avis Context Precision** : Le contexte contient une section dédiée « Gérer les aléas (demande d’avenant ou de modification) » qui fournit toutes les informations nécessaires pour répondre à la question, notamment le rôle du SPIV, les pièces à fournir et la nécessité d’attendre l’accord du financeur.

### Question : Quelles sont les différentes démarches à effectuer ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 142.68s, Eval: 0.00s, Total: 142.68s
- **Tokens générés** : 0

### Question : - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire extérieur? Est-ce gratuit?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 3.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 87.95s, Eval: 6.40s, Total: 94.35s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (cadre du contrat de recherche, rôle du SPIV, contact Hélène Jullien) sont présentes dans le contexte fourni. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse traite du cadre (contrat de recherche/partenariat) mais ne répond pas à la seconde partie de la question concernant la gratuité. Elle est donc partiellement pertinente.
- **Avis Context Precision** : Le contexte contient des sections détaillant le Service Partenariats, Innovations et Valorisation (SPIV), les contrats de recherche et les contacts de Hélène Jullien, ce qui suffit pour répondre à la question sur le cadre.

### Question : A quelle adresse postale ou mail dois-je envoyer mon projet ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 84.12s, Eval: 6.48s, Total: 90.60s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les informations fournies dans la réponse (adresse e‑mail drv-pi@univ-tours.fr) sont présentes dans le contexte. Aucun élément n’a été inventé.
- **Avis Answer Relevance** : La réponse donne une adresse e‑mail, ce qui répond partiellement à la question qui demandait une adresse postale ou mail pour envoyer le projet. Elle ne propose pas d’adresse postale et ne précise pas si cette adresse est la plus adaptée pour un projet, d’où une légère perte de pertinence.
- **Avis Context Precision** : Le contexte contient explicitement l’adresse générique drv-pi@univ-tours.fr ainsi que d’autres contacts. L’information recherchée (une adresse e‑mail) est donc bien couverte par le contexte.

### Question : Comment m’inscrire / me réinscrire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 141.44s, Eval: 23.70s, Total: 165.14s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (utiliser la plateforme ADUM, période de réinscription du début juin au 15 novembre) sont directement présentes dans le contexte. Le seul élément qui n’apparaît pas dans le contexte est le nom du contact, mais les règles d’évaluation excluent les contacts de la pénalisation de la fidélité.
- **Avis Answer Relevance** : La réponse répond directement à la question en indiquant le canal (ADUM) et la période obligatoire, ainsi qu’un point de contact pour obtenir de l’aide, ce qui correspond exactement à ce qui était demandé.
- **Avis Context Precision** : Le contexte fourni contient les informations essentielles sur la procédure d’inscription/réinscription via ADUM, la période de réinscription et les contacts de l’université. Il est donc parfaitement adapté à la question.

### Question : Quelles ressources le Pôle SAPS peut m’apporter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 57.65s, Eval: 9.21s, Total: 66.86s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse se retrouvent dans le contexte : l’adresse e‑mail, l’accompagnement au montage de projets (conseil, budgétisation, mise en relation), les formations en médiation scientifique (Jeudis des SAPS, Ma thèse en 180s) et la participation à des événements comme DéTours des sciences, la Fête de la science ou le festival (Re)Cherche et trouve. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond à la question en indiquant les principales ressources offertes (contact, aide au projet, formations, événements). Elle reste pertinente mais ne couvre pas l’ensemble des services mentionnés dans le contexte, d’où une note légèrement inférieure.
- **Avis Context Precision** : Le contexte fourni contient une description détaillée des missions du Pôle SAPS, incluant les services cités dans la réponse. Il est donc parfaitement adapté pour répondre à la question.

### Question : Y a-t-il des alumni ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 1.0/5
- **Temps** : RAG: 84.85s, Eval: 10.00s, Total: 94.85s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement traçables dans le contexte : le texte indique que le contexte ne mentionne pas d'alumni. Le contact ajouté est exempté de pénalité selon la règle sur les contacts injectés.
- **Avis Answer Relevance** : La réponse répond directement à la question en indiquant que le contexte ne fournit pas d'information sur les alumni et suggère de consulter d'autres sources.
- **Avis Context Precision** : Le contexte récupéré ne contient aucune information relative aux alumni, il est donc totalement inadapté pour répondre à la question.

### Question : Que propose le Pôle SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 109.17s, Eval: 11.83s, Total: 121.00s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : le rôle de faciliter le dialogue, la réponse aux sollicitations via la Boutique des sciences, l’organisation d’événements comme DéTours des sciences et « Ma thèse en 180 secondes », les formations en vulgarisation et médiation, ainsi que le soutien à des projets artistiques (Ma thèse en BD, Kaléidoscope). L’adresse e‑mail figure également dans le contexte, donc aucune hallucination.
- **Avis Answer Relevance** : La réponse répond directement à la question « Que propose le Pôle SAPS ? » en listant les principales offres du pôle. Aucun élément hors sujet n’est introduit.
- **Avis Context Precision** : Le contexte récupéré contient l’ensemble des informations nécessaires pour répondre : missions du pôle, services proposés, exemples d’événements, formations, accompagnement de projets, contacts, etc.

### Question : - Qu’est-ce qu’une invention ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 2.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 81.17s, Eval: 9.28s, Total: 90.45s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont traçables dans le contexte : le texte ne fournit effectivement aucune définition de « invention », et la réponse indique simplement ce manque. Le seul élément ajouté (adresse e‑mail) est un contact, qui selon les consignes ne doit pas être pénalisé pour la fidélité.
- **Avis Answer Relevance** : La question demande une définition de l’invention. La réponse ne fournit pas cette définition, se contentant de dire que le contexte ne la contient pas et en orientant l’utilisateur vers un service. Elle ne répond donc pas directement à la demande.
- **Avis Context Precision** : Le contexte porte sur la propriété intellectuelle des inventions, les articles de loi et les mécanismes de dévolution, mais ne contient pas de définition explicite d’une invention. Ainsi, le contexte est seulement vaguement lié au sujet demandé.

### Question : - Je souhaite répondre à un Appel à projet?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 84.28s, Eval: 10.54s, Total: 94.82s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement soutenues par le contexte : le texte indique que Caroline Vaslin gère les calendriers des appels à projets (AAP) et contrôle les échéances. L'adresse e‑mail fournie n'est pas dans le contexte, mais la consigne précise de ne pas pénaliser les informations de contact.
- **Avis Answer Relevance** : La question porte sur la façon de répondre à un appel à projet. La réponse indique clairement à qui s'adresser (Caroline Vaslin) pour toute question relative aux AAP, ce qui répond directement à la demande de l'utilisateur.
- **Avis Context Precision** : Le contexte contient précisément le nom de la personne responsable des AAP ainsi que son rôle, ce qui permet de fournir la réponse demandée.

### Question : je suis en arrêt de travail, qui dois-je contacter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 87.38s, Eval: 17.90s, Total: 105.28s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse portent sur des contacts. Même si le nom Aurélie PETEREAU n’apparaît pas dans le contexte, il s’agit d’une information de contact et, selon les consignes, cela ne doit pas pénaliser la fidélité. Le reste de la réponse (Charlène BOIS et ses coordonnées) correspond exactement aux informations présentes dans le contexte.
- **Avis Answer Relevance** : La réponse répond à la question en indiquant des personnes à contacter pour un arrêt de travail. Elle fournit un contact supplémentaire qui n’est pas demandé, ce qui constitue un léger hors‑sujet, d’où la note 4.
- **Avis Context Precision** : Le contexte contient les coordonnées du secrétariat de la Médecine du Travail (Charlène BOIS) ainsi que de nombreux autres interlocuteurs. L’information nécessaire pour répondre à la question y est bien présente, donc la précision du contexte est maximale.

### Question : Combien de temps va prendre mon inscription ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 135.12s, Eval: 6.81s, Total: 141.93s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient aucune affirmation autre que le contact fourni. Les contacts sont explicitement exclus de la pénalité de fidélité, donc aucune hallucination n'est détectée.
- **Avis Answer Relevance** : La question porte sur la durée de l'inscription (« Combien de temps va prendre mon inscription ? »). La réponse ne fournit aucune information sur le délai, seulement un contact, ce qui ne répond pas du tout à la question.
- **Avis Context Precision** : Le contexte récupéré ne fournit pas de durée précise, mais il mentionne que les inscriptions sont ouvertes du 1 juin au 15 novembre et décrit le processus de transmission du dossier. Ces éléments sont vaguement liés à la question, mais ne donnent pas de réponse claire sur le temps nécessaire.

### Question : Comment avoir un email ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 143.82s, Eval: 10.11s, Total: 153.93s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte ou correspondent à des informations de contact. Le fait de mentionner que les doctorants reçoivent automatiquement un compte « étudiant établissement » (@etu.univ-tours.fr) ainsi que la nécessité de contacter la DRH pour les nouveaux agents se retrouve explicitement dans le texte. Les adresses e‑mail de la DSI (dsi@univ-tours.fr) et le rôle du service PJR sont des contacts ; selon la règle, les contacts absents du contexte ne sont pas considérés comme des hallucinations, donc aucune pénalité.
- **Avis Answer Relevance** : La question « Comment avoir un email ? » demande la procédure pour obtenir une adresse e‑mail institutionnelle. La réponse indique clairement les deux cas principaux (doctorants et nouveaux agents) et fournit les contacts utiles, répondant directement à la demande.
- **Avis Context Precision** : Le contexte fourni contient les informations nécessaires : description du compte « étudiant établissement », procédure de prise de contact avec la DRH, et les adresses e‑mail de la DSI. Ainsi le contexte est parfaitement ciblé.

### Question : - Je souhaite me procurer le formulaire de déclaration d’invention de l’université, à qui dois-je m’adresser ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 92.34s, Eval: 10.36s, Total: 102.70s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : le Pôle Juridique Recherche (PJR) gère les déclarations d’invention et le texte indique explicitement de privilégier l’adresse générique drv-pi@univ-tours.fr pour les questions de propriété intellectuelle. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond directement à la question « à qui dois‑je m’adresser ? » en indiquant le service et l’adresse e‑mail appropriés.
- **Avis Context Precision** : Le contexte fourni contient exactement les informations nécessaires (organisation du PJR, missions incluant l’instruction des déclarations d’invention, et l’adresse e‑mail générique).

### Question : Qui contacter pour toute demande d'ouvrages en service presse ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 3.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 141.23s, Eval: 12.53s, Total: 153.76s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient que l'adresse e‑mail drv-pi@univ-tours.fr, qui figure bien dans le contexte (adresse générique du PJR). Aucun élément inventé n'est ajouté, mais la réponse fait une inférence que cet e‑mail est le bon contact pour les "ouvrages en service presse", ce qui n'est pas explicitement indiqué dans le contexte.
- **Avis Answer Relevance** : La réponse fournit un contact, ce qui répond partiellement à la question, mais il n'est pas certain que ce soit le bon interlocuteur pour le service presse. Ainsi, la pertinence est partielle.
- **Avis Context Precision** : Le contexte ne mentionne pas spécifiquement le "service presse" ni un contact dédié à ce sujet. Le seul élément pertinent est l'adresse générique du PJR, qui n'est pas clairement liée à la demande d'ouvrages en service presse.

### Question : comment enregistrer ma demande de formation hors-catalogue et quels documents dois-je fournir ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 137.74s, Eval: 8.67s, Total: 146.41s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : la procédure d’accès à ADUM, la rubrique "Déclaration des formations hors catalogue" et la nécessité de fournir la fiche de validation des 50 crédits doctoraux ainsi que les justificatifs en un seul PDF. Aucun élément externe n’a été ajouté (les contacts sont exemptés de pénalité).
- **Avis Answer Relevance** : La réponse répond exactement à la question en expliquant comment enregistrer la demande et quels documents fournir, sans digression.
- **Avis Context Precision** : Le contexte récupéré contenait les informations nécessaires (rubrique ADUM, dépôt d’un PDF unique, fiche de validation, justificatifs). Ces informations ont été correctement exploitées.

### Question : Mon jury de thèse est-il valide ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 2.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 132.14s, Eval: 13.38s, Total: 145.52s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient pas d’affirmations factuelles contradictoires avec le contexte. Elle se contente de demander des informations supplémentaires et fournit un contact e‑mail qui n’apparaît pas dans le texte fourni (les contacts ajoutés ne sont pas pénalisés selon les règles). Aucun élément du contexte est falsifié, d’où une note élevée mais pas parfaite car la réponse introduit un élément (adresse e‑mail) qui n’est pas présent dans le contexte.
- **Avis Answer Relevance** : La question demande une évaluation de la validité du jury. La réponse indique simplement qu’il faut fournir les détails du jury pour pouvoir l’évaluer, sans donner d’analyse. Elle touche au sujet mais ne répond pas réellement à la question, d’où une note faible.
- **Avis Context Precision** : Le contexte fourni contient l’ensemble des règles nécessaires pour juger la validité d’un jury (nombre de membres, proportion de professeurs, exigences HDR, limites sur les membres émérites, parité, etc.). Ainsi le contexte est parfaitement pertinent.

### Question : quels types de financement de thèse existent ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 86.97s, Eval: 11.67s, Total: 98.64s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : contrats doctoraux ministériels, bourses régionales et départementales, CIFRE (industrielle), bourses associatives, financements par ANR, Europe, Labex, ERC, FUI, Bourses Rabelaisiennes, statut salarié et financement étranger. Aucun élément n’est inventé. Le contact ajouté n’est pas pénalisé selon la règle.
- **Avis Answer Relevance** : La réponse répond directement à la question en listant les différents types de financement de thèse, sans digression hors sujet.
- **Avis Context Precision** : Le contexte fourni contient une longue énumération des sources de financement (ANR, Europe, Labex, contrats de recherche, CIFRE, DGA, ADEME, gouvernements étrangers, salariés, etc.) qui permet de répondre à la question. Il est donc parfaitement pertinent.

### Question : - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autre CHRU?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 3.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 85.59s, Eval: 16.99s, Total: 102.58s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont soit directement tirées du contexte (ex. la distinction entre signature et dossiers réglementaires), soit concernent des coordonnées de contact qui, selon les règles, ne sont pas pénalisées même si elles n'apparaissent pas dans le contexte. Aucun élément inventé n'est présent.
- **Avis Answer Relevance** : La réponse adresse le sujet des échantillons du CHRU en proposant un contact et en rappelant les deux axes possibles (signature ou dossier CODECOH). Cependant, elle ne fournit pas de réponse concrète à la question initiale et se contente de demander des précisions, ce qui la rend partiellement pertinente.
- **Avis Context Precision** : Le contexte récupéré contient les informations nécessaires sur la manière de mentionner le CHRU dans les signatures et sur le dossier CODECOH relatif aux échantillons biologiques humains. Il est donc parfaitement adapté à la question.

### Question : Je souhaite monter un projet, comment faire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 90.51s, Eval: 16.24s, Total: 106.75s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes ou déductibles du contexte : le SPIV est mentionné comme service d’appui aux projets de recherche, les contacts sectoriels sont décrits, et l’adresse projets-etablissement@univ-tours.fr ainsi que le rôle du service SCRIPT sont explicités. Le seul élément de contact (Justine Gillet) n’est pas dans le contexte mais, selon la règle, les contacts ajoutés ne sont pas pénalisés.
- **Avis Answer Relevance** : La réponse répond directement à la question « comment monter un projet ? » en indiquant les deux grandes voies selon le type de projet (recherche ou transversal) et en fournissant les interlocuteurs à contacter, ce qui constitue une réponse ciblée et utile.
- **Avis Context Precision** : Le contexte récupéré contient toutes les informations nécessaires : description du SPIV, rôle du service SCRIPT, adresse e‑mail projets‑etablissement@univ-tours.fr, ainsi que les contacts par secteur. Il est donc parfaitement adapté.

### Question : - Comment protéger un savoir-faire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 85.02s, Eval: 9.62s, Total: 94.64s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement tirées du contexte : le besoin de distinguer les inventions brevetables des informations confidentielles, le dépôt de brevet ou la déclaration d'invention auprès de l'établissement, la signature d'accords ou de chartes de confidentialité, et le contact du Pôle Juridique Recherche. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond précisément à la question « Comment protéger un savoir‑faire ? » en proposant les deux voies principales (brevetage et confidentialité) et en indiquant le service à contacter pour plus d’informations.
- **Avis Context Precision** : Le contexte fourni contient les informations nécessaires (règles de confidentialité, conventions, droits de propriété intellectuelle, contacts du PJR). Il a été correctement exploité pour générer la réponse.

### Question : Je pars en mission, quelle pièce dois-je remplir ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 91.89s, Eval: 9.54s, Total: 101.43s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement soutenues par le contexte : le texte mentionne le « formulaire d’autorisation de déplacement » à remplir pour toute mission. Le contact ajouté (Ilona Moutoussamy) n’est pas considéré comme hallucination selon la règle d’exemption des contacts injectés.
- **Avis Answer Relevance** : La réponse répond exactement à la question « quelle pièce dois‑je remplir ? » en indiquant le formulaire d’autorisation de déplacement, sans digression hors sujet.
- **Avis Context Precision** : Le contexte contient explicitement l’information requise (le formulaire d’autorisation de déplacement) ainsi que le lien correspondant, ce qui est suffisant pour répondre à la question posée.

### Question : Quel est le délai moyen entre la soumission d’un manuscrit et sa publication ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 135.32s, Eval: 9.56s, Total: 144.88s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient aucune affirmation factuelle sur le délai de publication. Le seul élément fourni est une information de contact, qui n'est pas présent dans le contexte mais, selon les règles, les contacts ajoutés automatiquement ne sont pas pénalisés. Aucun autre contenu n'est halluciné.
- **Avis Answer Relevance** : La question porte sur le délai moyen entre la soumission d’un manuscrit et sa publication. La réponse se limite à un contact ("Contact a utiliser : PJR - Contact général : drv-pi@univ-tours.fr") et ne fournit aucune information relative au délai demandé, ce qui la rend hors‑sujet.
- **Avis Context Precision** : Le contexte récupéré mentionne un délai maximal de mise à disposition (6 mois pour les sciences, 12 mois pour les SHS) lié à la législation sur l’open‑access, mais il ne fournit pas le délai moyen entre soumission et publication. Ainsi, le contexte est vaguement lié au sujet (parle de délais) mais ne contient pas l'information recherchée.

## 09_premium_cross

### Question : C’est quoi les SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 59.59s, Eval: 9.99s, Total: 69.58s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (définition des SAPS, lien avec la loi LPR 2021, objectif de renforcer le dialogue entre chercheurs et citoyens, rôle de médiation scientifique) sont directement présentes dans le texte du contexte. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La question demande « C’est quoi les SAPS ? ». La réponse fournit une définition concise et pertinente, répondant exactement à la demande.
- **Avis Context Precision** : Le contexte contient une section intitulée « Les SAPS, qu'est-ce que c'est? » qui décrit les SAPS, leur cadre législatif (LPR 2021) et leurs objectifs. Le contexte est donc parfaitement ciblé.

### Question : Comment peut-on changer le budget d’un projet ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 107.80s, Eval: 8.50s, Total: 116.30s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations (contacter le SPIV, fournir un argumentaire scientifique, fournir un budget modifié validé par l'Antenne Financière, transmission au financeur) sont directement tirées du contexte. Le contact ajouté (Anne Galopin) est un élément de contact et, selon les règles, n'est pas pénalisé.
- **Avis Answer Relevance** : La réponse répond exactement à la question en expliquant la procédure pour modifier le budget d’un projet.
- **Avis Context Precision** : Le contexte contient la procédure détaillée de modification budgétaire via le SPIV, ainsi que les exigences de justification et de validation, ce qui est pleinement exploité.

### Question : Quelles sont les différentes démarches à effectuer ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 3.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 87.17s, Eval: 11.71s, Total: 98.88s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse reprend correctement les informations présentes dans le contexte (délai de 4 mois, saisie possible de la HATVP, procédure d’examen de l’éméritat, durée maximale de 5 ans renouvelable deux fois, cession du droit d’exploitation). Un seul élément n’est pas présent dans le contexte : le lien « https://www.univ-tours.fr/recherche/valorisation ». Il s’agit donc d’une petite hallucination, d’où la note 4.
- **Avis Answer Relevance** : La question demande les différentes démarches à effectuer. La réponse fournit trois séries de démarches (mobilité des chercheurs, obtention de l’éméritat, droit d’exploitation des œuvres). Elle répond partiellement à la question mais ne couvre pas l’ensemble des procédures décrites dans le contexte (ex. création d’une instance, composition, constitution du dossier, critères d’évaluation du conflit d’intérêts, options d’instances inter‑établissements). La pertinence est donc moyenne.
- **Avis Context Precision** : Le contexte retrouvé contient toutes les informations nécessaires pour répondre aux trois thématiques abordées dans la réponse (délais, instances, procédure d’éméritat, durée, droit d’exploitation). Il est donc très précis.

### Question : - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire extérieur? Est-ce gratuit?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 3.0/5, Context Precision: 4.0/5
- **Temps** : RAG: 141.86s, Eval: 8.75s, Total: 150.61s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : le besoin d'un contrat de recherche ou d'une convention de partenariat, le rôle du Service Partenariats, Innovations et Valorisation (SPIV), les procédures spécifiques pour les entreprises extérieures (visite, plan de prévention, permis de feu) et les coordonnées d'Hélène Jullien. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse décrit le cadre juridique et administratif pour réaliser des expérimentations avec un partenaire extérieur, ce qui répond à la première partie de la question. Cependant, elle ne répond pas à la seconde partie (« Est‑ce gratuit ? »), ce qui la rend partiellement pertinente.
- **Avis Context Precision** : Le contexte fourni contient les informations nécessaires sur le cadre de collaboration, les procédures et le service à contacter. Il ne mentionne toutefois aucune information sur la gratuité, ce qui explique l'absence de réponse à ce point.

### Question : A quelle adresse postale ou mail dois-je envoyer mon projet ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 189.74s, Eval: 7.66s, Total: 197.40s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient que l'adresse e‑mail drv-pi@univ-tours.fr, qui apparaît explicitement dans le contexte (section « Pour tous les sujets relatifs à la propriété intellectuelle … : contactez drv-pi@univ-tours.fr »). Aucun élément n'est inventé.
- **Avis Answer Relevance** : La question demande l'adresse postale ou mail pour envoyer un projet. La réponse fournit une adresse e‑mail utilisable, ce qui répond directement à la demande.
- **Avis Context Precision** : Le contexte fourni comprend bien l'e‑mail indiqué dans la réponse, ainsi que d’autres contacts. L'information requise était donc présente et correctement ciblée.

### Question : Comment m’inscrire / me réinscrire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 86.44s, Eval: 13.48s, Total: 99.92s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (mise à jour des informations, dépôt de la convention et des documents, clic sur « Je finalise la procédure », validation par les différentes instances et date limite du 15 novembre) sont directement présentes dans le contexte. Le contact ajouté (Marie Clermonte) n'est pas pénalisé selon la règle d'exemption des contacts.
- **Avis Answer Relevance** : La réponse répond précisément à la question « Comment m’inscrire / me réinscrire ? » en décrivant les étapes concrètes à suivre, sans digression.
- **Avis Context Precision** : Le contexte fourni contient l’ensemble des informations nécessaires pour répondre à la question, y compris les étapes détaillées, les validations requises et la date limite.

### Question : Quelles ressources le Pôle SAPS peut m’apporter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 58.21s, Eval: 9.34s, Total: 67.55s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (formations, accompagnements, événements, projets et contact) sont directement présentes dans le contexte. Aucun élément n’est inventé ; les contacts sont autorisés même s’ils ne figurent pas dans le texte principal.
- **Avis Answer Relevance** : La réponse répond exactement à la question en listant les ressources que le Pôle SAPS peut offrir, sans digression.
- **Avis Context Precision** : Le contexte fourni contient l’ensemble des informations nécessaires (formations, accompagnements, événements, projets, contacts) pour répondre à la question, il est donc parfaitement ciblé.

### Question : Y a-t-il des alumni ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 132.06s, Eval: 7.23s, Total: 139.29s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse indique que les documents fournis ne mentionnent pas explicitement d'alumni, ce qui correspond exactement à ce qui est observable dans le contexte (aucune occurrence du terme "alumni" ou d'un réseau d'anciens). Le contact proposé n'est pas présent dans le contexte, mais la règle autorise les contacts ajoutés automatiquement, donc aucune pénalité.
- **Avis Answer Relevance** : La question porte sur l'existence d'alumni. La réponse répond directement en précisant l'absence de mention et propose une démarche pour obtenir une réponse précise, ce qui est pleinement pertinent.
- **Avis Context Precision** : Le contexte récupéré contient les informations nécessaires pour conclure qu'aucune mention d'alumni n'est présente. Ainsi le contexte est adéquat pour répondre à la question.

### Question : Que propose le Pôle SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 57.05s, Eval: 14.56s, Total: 71.61s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : accompagnement des chercheurs (formations, dépôts de projets ANR/ APR‑IR, mise en relation, aide budgétaire), organisation d'événements (DéTours des sciences, Ma thèse en 180 s, Village des sciences, Fête de la science, Nocturnes de l'Histoire, festival (Re)Cherche et trouve), projets arts/sciences (Ma thèse en BD, Kaléidoscope, résidence d'artiste PieR Gajewski, Campement scientifique), actions de médiation (Apéro Sciences, interventions en classe, MeFILYA, concours Ma thèse en 180 s) et la Boutique des sciences. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question « Que propose le Pôle SAPS ? » en listant les services et activités proposés. Aucun contenu hors sujet n’est présent.
- **Avis Context Precision** : Le contexte fourni contient l’ensemble des informations utilisées : missions du pôle, formations, événements, projets arts/sciences, actions de médiation et la Boutique des sciences. Le contexte était donc parfaitement ciblé.

### Question : - Qu’est-ce qu’une invention ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 4.0/5, Context Precision: 3.0/5
- **Temps** : RAG: 133.97s, Eval: 8.93s, Total: 142.90s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse cite une définition précise d’une invention (solution technique nouvelle, activité inventive, application industrielle, article L.611-10). Cette formulation n’apparaît pas dans le contexte fourni, qui décrit surtout les décrets et les modalités de dévolution des droits, mais ne donne pas de définition juridique détaillée. Ainsi, l’information est partiellement inférée et constitue une hallucination, d’où la note 3.
- **Avis Answer Relevance** : La réponse répond directement à la question en donnant une définition d’invention et ajoute une information supplémentaire sur le décret applicable aux créateurs indépendants. Cette information supplémentaire n’est pas demandée mais reste liée au sujet, ce qui justifie une note élevée (4).
- **Avis Context Precision** : Le contexte récupéré porte sur les décrets relatifs aux inventeurs, les modalités de dévolution des droits, etc. Il ne contient pas la définition exacte de l’invention, mais il est tout de même pertinent pour le sujet général. L’absence de la définition précise conduit à une note moyenne (3).

### Question : - Je souhaite répondre à un Appel à projet?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 3.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 83.37s, Eval: 17.48s, Total: 100.85s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont soit neutres, soit des informations de contact. Bien que le nom et l'e‑mail de Caroline Vaslin n'apparaissent pas dans le contexte, la règle indique de ne pas pénaliser les contacts absents. Aucun autre élément de la réponse ne contredit le contexte.
- **Avis Answer Relevance** : La réponse propose un contact pour obtenir des informations, ce qui répond partiellement à la demande « Je souhaite répondre à un appel à projet ». Cependant, elle ne fournit aucune instruction concrète ni les étapes à suivre, ce qui limite sa pertinence.
- **Avis Context Precision** : Le contexte fourni porte principalement sur la procédure d’inscription doctorale, les pièces à fournir, les contacts de l’université et de l’INSA, etc. Il ne contient pas d’instructions précises sur la façon de répondre à un appel à projet, ni le contact de Caroline Vaslin. Le contexte est donc peu précis pour la question.

### Question : je suis en arrêt de travail, qui dois-je contacter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 3.0/5
- **Temps** : RAG: 88.12s, Eval: 16.54s, Total: 104.66s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont limitées à la donnée de contact. Bien que ce contact n'apparaisse pas dans le contexte, la règle d'exemption pour les informations de contact stipule de ne pas pénaliser la fidélité. Aucun autre élément n'est présent, donc aucune hallucination détectée.
- **Avis Answer Relevance** : La question demande explicitement « qui dois‑je contacter ? ». La réponse fournit un nom et une adresse e‑mail, répondant directement à la demande.
- **Avis Context Precision** : Le contexte fourni contient des informations générales sur le cadre de travail, les congés maladie et des liens vers l'organigramme de la DRH, mais il ne mentionne aucun contact précis. Ainsi, le contexte est partiellement utile pour orienter l'utilisateur, mais il ne fournit pas la réponse exacte attendue.

### Question : Combien de temps va prendre mon inscription ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 3.0/5, Context Precision: 4.0/5
- **Temps** : RAG: 83.55s, Eval: 12.25s, Total: 95.80s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (le délai d'instruction est rallongé pour les diplômes étrangers ou DEA) sont présentes dans le contexte. Les informations de contact ajoutées ne sont pas pénalisées selon la règle d'exemption des contacts.
- **Avis Answer Relevance** : La réponse traite du facteur qui influence la durée de l'inscription (délai rallongé), mais ne fournit pas de durée concrète demandée par l'utilisateur. Elle répond partiellement à la question.
- **Avis Context Precision** : Le contexte contient l'information clé sur le rallongement du délai pour les dossiers avec diplôme étranger ou DEA, mais il ne donne pas de durée précise. Le contexte est donc pertinent mais incomplet pour répondre à la question de façon chiffrée.

### Question : Comment avoir un email ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 2.0/5, Context Precision: 1.0/5
- **Temps** : RAG: 86.02s, Eval: 9.18s, Total: 95.20s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse introduit une affirmation selon laquelle il faut contacter le service à l'adresse drv-pi@univ-tours.fr pour toute demande liée à un email professionnel ou à une démarche administrative. Cette information n'est pas présente dans le contexte fourni. Le seul élément du texte qui correspond à une donnée de contact (l'adresse e‑mail) est exempté de pénalité selon la règle, mais le reste de la phrase (l'existence d'un tel service et son rôle) n'est pas traçable dans le contexte, d'où une faible fidélité.
- **Avis Answer Relevance** : La question « Comment avoir un email ? » attend probablement des instructions pour créer ou obtenir une adresse e‑mail. La réponse se contente de fournir un contact e‑mail d'un service, sans expliquer comment obtenir une adresse e‑mail. Elle ne répond donc pas réellement à la demande, ce qui rend la pertinence faible.
- **Avis Context Precision** : Le contexte récupéré porte sur le droit d'auteur, la propriété intellectuelle et les statuts des agents publics, sans aucune mention d'obtention d'une adresse e‑mail. Le contexte n'est donc pas du tout pertinent pour répondre à la question.

### Question : - Je souhaite me procurer le formulaire de déclaration d’invention de l’université, à qui dois-je m’adresser ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 84.20s, Eval: 7.05s, Total: 91.25s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les informations fournies (contact du PJR via l'adresse générique drv-pi@univ-tours.fr) sont présentes dans le contexte. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse indique précisément à qui s'adresser pour obtenir le formulaire, répondant exactement à la question posée.
- **Avis Context Precision** : Le contexte contient l'adresse générique pour les questions de propriété intellectuelle ainsi que la mission du PJR d'instruction des déclarations d'invention, ce qui est suffisant pour répondre.

### Question : Qui contacter pour toute demande d'ouvrages en service presse ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 2.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 89.75s, Eval: 10.57s, Total: 100.32s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse indique que le contact à utiliser est « PJR - Contact général : drv-pi@univ-tours.fr ». L'adresse e‑mail drv-pi@univ-tours.fr apparaît bien dans le contexte, mais le texte du contexte ne l’associe jamais à la prise en charge des « demandes d'ouvrages en service presse ». Lier cet e‑mail à cette fonction est une affirmation inventée, donc la réponse n’est pas entièrement fidèle au contexte.
- **Avis Answer Relevance** : La question porte sur le contact à solliciter pour toute demande d'ouvrages en service presse. La réponse fournit un contact générique du PJR, qui n’est pas présenté dans le contexte comme étant lié au service presse. Ainsi, la réponse ne répond pas correctement à la demande spécifique.
- **Avis Context Precision** : Le contexte ne contient aucune information explicite sur le service presse ou sur le contact dédié à ce type de demande. Les seules adresses présentes sont relatives à des services juridiques, à la relation membres, etc. Le contexte n’est donc pas précis pour répondre à la question.

### Question : comment enregistrer ma demande de formation hors-catalogue et quels documents dois-je fournir ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 1.0/5
- **Temps** : RAG: 85.73s, Eval: 10.19s, Total: 95.92s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (un seul contact e‑mail) sont autorisées à ne pas être présentes dans le contexte selon la règle spéciale sur les contacts injectés. Aucun autre contenu n'est présent, donc aucune hallucination n'est pénalisée.
- **Avis Answer Relevance** : La question porte sur la procédure d'enregistrement d'une demande de formation hors‑catalogue et les documents requis. La réponse ne fournit qu'un contact e‑mail et ne répond pas du tout à la demande.
- **Avis Context Precision** : Le contexte récupéré traite de droits d'auteur, de jurisprudence et de procédures administratives liées à la recherche, sans aucune information sur les demandes de formation hors‑catalogue. Il ne contient donc pas les informations nécessaires.

### Question : Mon jury de thèse est-il valide ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 82.78s, Eval: 11.07s, Total: 93.85s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient aucune affirmation factuelle autre que le contact fourni. Les contacts ne sont pas pénalisés même s'ils n'apparaissent pas dans le contexte, conformément à la règle. Aucun autre élément n'est présent, donc aucune hallucination n'est détectée.
- **Avis Answer Relevance** : La question porte sur la validité du jury de thèse. La réponse se limite à fournir un contact e‑mail, ce qui ne répond pas du tout à la demande. Aucun élément relatif aux critères d’éligibilité du jury n’est fourni.
- **Avis Context Precision** : Le contexte récupéré décrit précisément les critères d’éligibilité et les exclusions pour les membres d’un jury de thèse, ainsi que les règles de l’Ordonnance. Il contient donc toutes les informations nécessaires pour répondre à la question.

### Question : quels types de financement de thèse existent ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 85.31s, Eval: 8.85s, Total: 94.16s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les mentions de la réponse (contrats doctoraux établissement ou régionaux, bourses CIFRE, ANR, financements européens, Labex, contrats de recherche ou d'entreprise, financements étrangers, financements pour doctorants salariés) sont présentes textuellement dans le contexte. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond directement à la question en listant les différents types de financement de thèse. Elle fournit une réponse ciblée et utile sans digression.
- **Avis Context Precision** : Le contexte fourni contient une section détaillée sur les « Autres financements doctoraux » qui recense les sources de financement demandées. Le contexte est donc parfaitement adapté pour répondre à la question.

### Question : - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autre CHRU?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 135.96s, Eval: 9.34s, Total: 145.30s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations concernant la forme de la signature (première ligne avec le CHRU de Tours, seconde ligne avec l'Université de Tours) sont directement présentes dans le contexte. Le texte ajouté sur le contact (Claude‑Emmanuel Boudet) n'est pas dans le contexte, mais les consignes indiquent de ne pas pénaliser les contacts injectés pour la fidélité.
- **Avis Answer Relevance** : La question porte sur l'utilisation d'échantillons provenant du CHRU de Tours ou d'un autre CHRU, alors que la réponse traite uniquement de la rédaction d'une signature pour un personnel hospitalo‑universitaire. Aucun lien avec les échantillons n'est fourni, la réponse est donc hors sujet.
- **Avis Context Precision** : Le contexte fourni traite de la rédaction des signatures et des affiliations institutionnelles, pas de la gestion ou de l'utilisation d'échantillons. Il ne contient donc pas les informations nécessaires pour répondre à la question posée.

### Question : Je souhaite monter un projet, comment faire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 85.19s, Eval: 13.72s, Total: 98.91s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations concernant le rôle obligatoire du service SCRIPT, la validation par le COPIL et la nécessité de déposer le projet après validation sont directement présentes dans le contexte. Le seul élément supplémentaire est le contact de Justine Gillet (nom, e‑mail, téléphone) qui n’apparaît pas dans le contexte, mais les règles précisent de ne pas pénaliser les informations de contact ajoutées automatiquement.
- **Avis Answer Relevance** : La réponse répond à la question « comment monter un projet ? » en indiquant le premier point de contact et les étapes majeures (passer par le service SCRIPT, obtenir la validation du COPIL). Elle reste pertinente, même si elle ne détaille pas l’ensemble du processus décrit dans le contexte.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires pour répondre à la question : existence du service SCRIPT, son rôle obligatoire, le processus de validation par le COPIL, etc. Le contexte est donc très précis et complet pour la tâche demandée.

### Question : - Comment protéger un savoir-faire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 85.02s, Eval: 8.06s, Total: 93.08s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse se retrouvent dans le contexte : le besoin de conventions incluant des clauses de confidentialité et de propriété intellectuelle est explicitement mentionné, tout comme le fait que le Pôle Juridique Recherche (PJR) gère ces questions et que l'adresse drv-pi@univ-tours.fr est fournie. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond directement à la question « Comment protéger un savoir‑faire ? » en proposant la formalisation de conventions de confidentialité et de propriété intellectuelle et en indiquant le contact du PJR, ce qui constitue une réponse pertinente et ciblée.
- **Avis Context Precision** : Le contexte fourni contient les informations nécessaires (confidentialité, conventions, rôle du PJR, contacts) pour répondre à la question, et ces informations sont correctement exploitées.

### Question : Je pars en mission, quelle pièce dois-je remplir ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 86.32s, Eval: 7.13s, Total: 93.45s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse indique qu'il faut remplir le formulaire d'Autorisation de Déplacement, ce qui est explicitement présent dans le contexte. Elle ajoute également le délai de 15 jours, également présent. Le seul élément non présent dans le contexte est le lien URL vers l'Intranet ; il s'agit d'une information externe, d'où la note 4.
- **Avis Answer Relevance** : La réponse répond exactement à la question en indiquant la pièce à remplir (le formulaire d'Autorisation de Déplacement) et fournit la consigne de transmission, ce qui est pleinement pertinent.
- **Avis Context Precision** : Le contexte contient la mention du formulaire à remplir pour chaque mission ainsi que la procédure à suivre, donc il est parfaitement ciblé.

### Question : Quel est le délai moyen entre la soumission d’un manuscrit et sa publication ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 82.37s, Eval: 6.43s, Total: 88.80s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient aucune affirmation factuelle tirée du contexte, mais elle n'introduit aucune information erronée. Le seul élément ajouté est un contact, qui selon les règles ne doit pas être pénalisé. Ainsi, aucune hallucination n'est détectée.
- **Avis Answer Relevance** : La question porte sur le délai moyen entre la soumission d’un manuscrit et sa publication. La réponse fournie ne mentionne aucun délai, se limitant à un contact, ce qui ne répond pas du tout à la demande.
- **Avis Context Precision** : Le contexte fourni inclut clairement l'information pertinente : un délai maximal de six mois pour les sciences, techniques et médecine, et de douze mois pour les sciences humaines et sociales. Le contexte est donc parfaitement adapté à la question.

## 10_mid_draft

### Question : C’est quoi les SAPS ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 55.41s, Eval: 0.00s, Total: 55.41s
- **Tokens générés** : 0

### Question : Comment peut-on changer le budget d’un projet ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 106.71s, Eval: 0.00s, Total: 106.71s
- **Tokens générés** : 0

### Question : Quelles sont les différentes démarches à effectuer ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 79.65s, Eval: 0.00s, Total: 79.65s
- **Tokens générés** : 0

### Question : - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire extérieur? Est-ce gratuit?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 83.94s, Eval: 0.00s, Total: 83.94s
- **Tokens générés** : 0

### Question : A quelle adresse postale ou mail dois-je envoyer mon projet ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 80.06s, Eval: 0.00s, Total: 80.06s
- **Tokens générés** : 0

### Question : Comment m’inscrire / me réinscrire ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 85.97s, Eval: 0.00s, Total: 85.97s
- **Tokens générés** : 0

### Question : Quelles ressources le Pôle SAPS peut m’apporter ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 54.07s, Eval: 0.00s, Total: 54.07s
- **Tokens générés** : 0

### Question : Y a-t-il des alumni ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 87.66s, Eval: 0.00s, Total: 87.66s
- **Tokens générés** : 0

### Question : Que propose le Pôle SAPS ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 54.06s, Eval: 0.00s, Total: 54.06s
- **Tokens générés** : 0

### Question : - Qu’est-ce qu’une invention ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 84.52s, Eval: 6.41s, Total: 90.93s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient que le contact « drv-pi@univ-tours.fr », qui figure bien dans le contexte fourni. Aucun élément n’est ajouté qui ne provient pas du contexte, donc la réponse est totalement fidèle aux informations disponibles.
- **Avis Answer Relevance** : La question porte sur la définition d’une invention. La réponse fournit uniquement un contact et ne répond en rien à la demande, ce qui la rend hors sujet.
- **Avis Context Precision** : Le contexte récupéré traite largement de la législation autour des inventions, des dispositifs de valorisation et des droits de propriété intellectuelle, mais il ne fournit pas une définition claire et concise d’une invention. Ainsi, le contexte est seulement vaguement lié à la question.

### Question : - Je souhaite répondre à un Appel à projet?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 88.14s, Eval: 6.28s, Total: 94.42s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les informations fournies (contact de Caroline Vaslin, son rôle de gestion des AAP, y compris les colloques) sont présentes dans le contexte. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond directement à la demande de l'utilisateur qui veut savoir comment répondre à un appel à projet, en indiquant le contact approprié.
- **Avis Context Precision** : Le contexte contient le nom, l'adresse e‑mail et la fonction de Caroline Vaslin relative aux AAP, ce qui suffit pour répondre à la question.

### Question : je suis en arrêt de travail, qui dois-je contacter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 91.13s, Eval: 6.66s, Total: 97.79s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement tirées du contexte : les deux liens vers les pages « Congés maladie des agents titulaires » et « Congés maladie des agents contractuels » existent dans le texte fourni. Aucun élément n’a été inventé.
- **Avis Answer Relevance** : La réponse indique où trouver les procédures à suivre selon le statut de l’agent, ce qui répond en partie à la question « qui dois‑je contacter ? ». Elle ne donne pas un nom de contact précis, mais oriente l’utilisateur vers les ressources appropriées, ce qui reste pertinent.
- **Avis Context Precision** : Le contexte contient les informations nécessaires (liens spécifiques pour chaque statut) pour répondre à la question. Il ne manque aucune donnée essentielle au sein du texte fourni.

### Question : Combien de temps va prendre mon inscription ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 2.0/5, Context Precision: 3.0/5
- **Temps** : RAG: 141.79s, Eval: 11.98s, Total: 153.77s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse se base uniquement sur le contact présent dans le contexte (Christèle GAUDRON, adresse gaudron@univ-tours.fr). Aucun autre fait factuel n'est ajouté, à l'exception du suffixe «‑Bredif» au nom et de l'affirmation «référente administrative», qui ne figurent pas explicitement dans le contexte. Selon la règle, les informations de contact ne sont pas pénalisées, mais le titre ajouté constitue une légère invention, d'où un 4.
- **Avis Answer Relevance** : La question demande la durée de l'inscription. La réponse ne fournit pas de durée, mais indique de contacter une personne pour obtenir l'information. Cela ne répond pas directement à la question, seulement suggère une démarche, ce qui justifie un 2.
- **Avis Context Precision** : Le contexte contient des informations relatives aux étapes d’inscription, aux dates limites (ex. «au plus tard le 15 novembre») et aux contacts. Cependant, il ne donne pas de durée précise de la procédure, ce qui rend le contexte partiellement utile. Note de 3.

### Question : Comment avoir un email ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 84.51s, Eval: 6.93s, Total: 91.44s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes ou directement déductibles du contexte : le domaine @etu.univ-tours.fr, la création automatique du compte étudiant, le rôle du directeur de thèse ou de l'encadrant pour solliciter le service informatique, et le contact dsi@univ-tours.fr. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond précisément à la question « Comment avoir un email ? » en expliquant le processus d’obtention d’une adresse institutionnelle et les interlocuteurs à contacter.
- **Avis Context Precision** : Le contexte fourni contient les informations nécessaires (domaine de l’adresse, procédure de création via le service informatique, rôle du directeur de thèse). Il est donc parfaitement ciblé.

### Question : - Je souhaite me procurer le formulaire de déclaration d’invention de l’université, à qui dois-je m’adresser ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 86.73s, Eval: 7.21s, Total: 93.94s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les informations fournies (contact du PJR via l'adresse drv-pi@univ-tours.fr) sont présentes dans le contexte. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse indique clairement à qui s'adresser pour obtenir le formulaire de déclaration d’invention, répondant exactement à la question posée.
- **Avis Context Precision** : Le contexte contient l'adresse générique drv-pi@univ-tours.fr ainsi que la mention que le PJR gère les déclarations d'invention, ce qui est suffisant pour répondre à la question.

### Question : Qui contacter pour toute demande d'ouvrages en service presse ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 1.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 85.82s, Eval: 4.67s, Total: 90.49s
- **Tokens générés** : 0
- **Avis Faithfulness** : Aucune réponse n'est fournie, il n'est donc pas possible de vérifier la correspondance avec le contexte. L'absence de contenu implique que chaque affirmation (qui n'existe pas) ne peut pas être traçable, justifiant la note minimale.
- **Avis Answer Relevance** : La question demande le contact à joindre pour des demandes d'ouvrages en service presse. Aucun élément de réponse n'est présent, la question n'est donc pas du tout traitée.
- **Avis Context Precision** : Le contexte fourni ne contient pas d'information explicite sur le service presse ou son contact. Il ne comporte que des références génériques (adresse DSI, annuaire, etc.). Ainsi, le contexte est seulement vaguement lié au sujet, d'où la note 2.

### Question : comment enregistrer ma demande de formation hors-catalogue et quels documents dois-je fournir ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 93.52s, Eval: 6.45s, Total: 99.97s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (déposer la demande sur ADUM, rubrique 'Déclaration des formations hors catalogue', fichier PDF unique, inclusion de la fiche de validation et de tous les justificatifs, exigence d'une demande complète) sont directement présentes dans le contexte. Le contact ajouté n'est pas pénalisé selon la règle.
- **Avis Answer Relevance** : La réponse répond exactement à la question en expliquant comment enregistrer la demande et quels documents fournir, sans digression.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires pour répondre : procédure de dépôt, format du fichier, documents requis. Le système a utilisé ces éléments.

### Question : Mon jury de thèse est-il valide ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 2.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 88.96s, Eval: 11.53s, Total: 100.49s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient aucune affirmation factuelle qui ne soit pas présente dans le contexte. Elle se contente de demander des informations complémentaires et fournit un contact qui, bien que non présent dans le contexte, est exempté de pénalité selon les règles. Aucun élément halluciné n'est détecté.
- **Avis Answer Relevance** : La question demandait une évaluation de la validité du jury. La réponse ne fournit pas cette évaluation, mais se limite à demander des précisions supplémentaires, ce qui ne répond pas directement à la demande. Elle touche au sujet mais ne répond pas réellement à la question.
- **Avis Context Precision** : Le contexte fourni contient toutes les règles nécessaires (nombre de membres, proportion d'externes, présence d'un HDR, limites des membres invités, etc.) pour juger de la validité d'un jury. Ainsi le contexte est pleinement pertinent.

### Question : quels types de financement de thèse existent ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 87.80s, Eval: 11.13s, Total: 98.93s
- **Tokens générés** : 0
- **Avis Faithfulness** : Chaque élément de la réponse se retrouve textuellement dans le contexte : contrats doctoraux (ministériels, établissement, collectivités/région), bourses (régionales, départementales, industrielles, associatives, étrangères), financements ANR/Europe/Labex, contrats de recherche et contrats entreprise, CIFRE/DGA/ADEME, salariés (privé/public) et cotutelle internationale. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La question porte sur les types de financement de thèse. La réponse fournit une liste ciblée de ces types, répondant exactement à la demande sans digression.
- **Avis Context Precision** : Le contexte fourni contient toutes les catégories citées dans la réponse. Les informations sont pertinentes et directement exploitables pour répondre à la question.

### Question : - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autre CHRU?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 87.27s, Eval: 8.43s, Total: 95.70s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (structure en deux lignes, exemple d'affiliation « Université de Tours, INSERM, IC UMR U 930, 37032 Tours, France » et « CHRU de Tours, Service concerné, 37XXX Tours, France ») sont directement tirées du contexte fourni. Le contact ajouté n'est pas pénalisé selon la règle sur les contacts injectés.
- **Avis Answer Relevance** : La réponse répond précisément à la question en indiquant comment formuler les affiliations lorsqu'on utilise des échantillons du CHRU de Tours ou d'un autre CHRU, ce qui était l'objet de la demande.
- **Avis Context Precision** : Le contexte récupéré contient les règles détaillées de signature pour le personnel hospitalo‑universitaire du CHRU de Tours, y compris les exemples de lignes d'affiliation. Il est donc parfaitement adapté à la question.

### Question : Je souhaite monter un projet, comment faire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 3.0/5, Context Precision: 4.0/5
- **Temps** : RAG: 94.29s, Eval: 11.19s, Total: 105.48s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes ou compatibles avec le contexte. Le service SCRIPT et l'adresse projets-etablissement@univ-tours.fr figurent dans le texte. Les coordonnées de contact (nom, email, téléphone) ne sont pas dans le contexte, mais la consigne indique de ne pas pénaliser la fidélité pour les informations de contact ajoutées automatiquement.
- **Avis Answer Relevance** : La réponse indique un premier pas concret (contacter une personne et envoyer une saisine), ce qui répond partiellement à la question « comment monter un projet ? ». Cependant, elle ne décrit pas les étapes détaillées du montage (dossier, budget, comité de pilotage, etc.), ce qui limite sa pertinence.
- **Avis Context Precision** : Le contexte récupéré contient les informations nécessaires pour orienter l'utilisateur vers le service SCRIPT et l'adresse de saisine, ainsi que de nombreuses consignes détaillées sur le montage de projet. Il est donc pertinent, même s'il ne se limite pas à une simple procédure de contact.

### Question : - Comment protéger un savoir-faire ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 2.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 98.50s, Eval: 11.57s, Total: 110.07s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse mentionne le « Pôle Juridique Recherche » et l’adresse e‑mail drv-pi@univ-tours.fr ainsi que le fait qu’ils gèrent les conventions de confidentialité. Aucun de ces éléments n’apparaît dans le contexte fourni (le contexte parle de la DRV, de conventions ad hoc, etc.). Selon la règle, les contacts injectés ne sont pas pénalisés, mais l’affirmation sur leurs fonctions n’est pas justifiable à partir du texte, ce qui constitue une hallucination partielle. D’où la note 2.
- **Avis Answer Relevance** : La question demande comment protéger un savoir‑faire. La réponse se limite à indiquer un contact à joindre, sans expliquer les mécanismes (accords de confidentialité, conventions, cession de droits, etc.). Elle est donc peu pertinente, même si elle oriente vers une aide possible. Note 2.
- **Avis Context Precision** : Le contexte retrouvé contient de nombreuses informations pertinentes sur la protection du savoir‑faire (confidentialité, conventions, cessions de droits, outils juridiques, etc.). Il est donc très précis par rapport à la question. Note 5.

### Question : Je pars en mission, quelle pièce dois-je remplir ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 85.45s, Eval: 6.45s, Total: 91.90s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse indique exactement qu'il faut remplir le formulaire « Autorisation de Déplacement (AD) » et le transmettre 15 jours avant le départ. Ces deux informations sont présentes mot‑pour‑mot dans le contexte récupéré, aucune information supplémentaire n'est introduite.
- **Avis Answer Relevance** : La question demande « quelle pièce dois‑je remplir ? » La réponse fournit la pièce demandée (Autorisation de Déplacement) et précise le délai de transmission, répondant ainsi pleinement à la requête.
- **Avis Context Precision** : Le contexte contient la section « AUTORISATION DE DEPLACEMENT (à remplir pour chaque mission/déplacement…) » ainsi que la mention « A transmettre à votre gestionnaire ou antenne financière 15 jours minimum avant le départ en mission. ». Le contexte est donc parfaitement ciblé.

### Question : Quel est le délai moyen entre la soumission d’un manuscrit et sa publication ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 95.63s, Eval: 8.94s, Total: 104.57s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient aucune affirmation factuelle sur le délai de publication ; elle ne fournit qu'un contact. Les contacts ne sont pas pénalisés même s'ils n'apparaissent pas dans le contexte, donc aucune hallucination n'est comptée pour ce critère.
- **Avis Answer Relevance** : La question porte sur le délai moyen entre la soumission d’un manuscrit et sa publication. La réponse ne fournit aucun renseignement à ce sujet et se limite à un contact, ce qui la rend hors sujet.
- **Avis Context Precision** : Le contexte fourni ne mentionne pas le délai moyen entre soumission et publication. Il parle plutôt de délais maximaux (6 mois ou 12 mois) pour la mise à disposition en accès ouvert après la première publication, ce qui n’est pas directement la donnée recherchée.
