# Bilan des Évaluations (LLM as a Judge)

## Moyennes Globales

- **Faithfulness** : 4.59 / 5
- **Answer Relevance** : 3.70 / 5
- **Context Precision** : 4.18 / 5
- *Nombre de réponses évaluées avec succès : 130*
- **Temps moyen RAG** : 144.29s
- **Temps moyen Évaluation** : 9.19s
- **Temps moyen Total** : 153.49s
- **Tokens moyens générés** : 0
- *Nombre total de requêtes chronométrées : 144*

## 📊 Tableau Comparatif des Configurations

| Configuration / Modèle | Faithfulness | Relevance | Context Precision | RAG (s) | Eval (s) | Total (s) | Tokens Moy. | Évaluations |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **01_baseline** | 5.00 / 5 | 3.83 / 5 | 4.25 / 5 | 142.44s | 10.27s | 152.70s | 0 | 24 |
| **02_fast_draft** | 4.67 / 5 | 3.71 / 5 | 4.38 / 5 | 148.86s | 8.75s | 157.60s | 0 | 24 |
| **04_meta_mono** | 4.00 / 5 | 4.09 / 5 | 3.96 / 5 | 139.49s | 10.29s | 149.78s | 0 | 23 |
| **06_google_mono** | 4.86 / 5 | 3.55 / 5 | 4.18 / 5 | 152.85s | 10.97s | 163.82s | 0 | 22 |
| **08_economy_cross** | 4.33 / 5 | 3.38 / 5 | 4.04 / 5 | 147.72s | 9.79s | 157.51s | 0 | 24 |
| **10_mid_draft** | 4.77 / 5 | 3.62 / 5 | 4.38 / 5 | 134.40s | 5.08s | 139.49s | 0 | 13 |

## Détails par Configuration

### Configuration : 01_baseline
- Moyenne Faithfulness : 5.00 / 5
- Moyenne Answer Relevance : 3.83 / 5
- Moyenne Context Precision : 4.25 / 5
- *Évaluations réussies : 24*
- Temps moyen RAG : 142.44s
- Temps moyen Évaluation : 10.27s
- Temps moyen Total : 152.70s
- Tokens moyens générés : 0

### Configuration : 02_fast_draft
- Moyenne Faithfulness : 4.67 / 5
- Moyenne Answer Relevance : 3.71 / 5
- Moyenne Context Precision : 4.38 / 5
- *Évaluations réussies : 24*
- Temps moyen RAG : 148.86s
- Temps moyen Évaluation : 8.75s
- Temps moyen Total : 157.60s
- Tokens moyens générés : 0

### Configuration : 04_meta_mono
- Moyenne Faithfulness : 4.00 / 5
- Moyenne Answer Relevance : 4.09 / 5
- Moyenne Context Precision : 3.96 / 5
- *Évaluations réussies : 23*
- Temps moyen RAG : 139.49s
- Temps moyen Évaluation : 10.29s
- Temps moyen Total : 149.78s
- Tokens moyens générés : 0

### Configuration : 06_google_mono
- Moyenne Faithfulness : 4.86 / 5
- Moyenne Answer Relevance : 3.55 / 5
- Moyenne Context Precision : 4.18 / 5
- *Évaluations réussies : 22*
- Temps moyen RAG : 152.85s
- Temps moyen Évaluation : 10.97s
- Temps moyen Total : 163.82s
- Tokens moyens générés : 0

### Configuration : 08_economy_cross
- Moyenne Faithfulness : 4.33 / 5
- Moyenne Answer Relevance : 3.38 / 5
- Moyenne Context Precision : 4.04 / 5
- *Évaluations réussies : 24*
- Temps moyen RAG : 147.72s
- Temps moyen Évaluation : 9.79s
- Temps moyen Total : 157.51s
- Tokens moyens générés : 0

### Configuration : 10_mid_draft
- Moyenne Faithfulness : 4.77 / 5
- Moyenne Answer Relevance : 3.62 / 5
- Moyenne Context Precision : 4.38 / 5
- *Évaluations réussies : 13*
- Temps moyen RAG : 134.40s
- Temps moyen Évaluation : 5.08s
- Temps moyen Total : 139.49s
- Tokens moyens générés : 0

---
## Détails des évaluations (Notes et Commentaires du Juge)

## 01_baseline

### Question : C’est quoi les SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 83.32s, Eval: 7.18s, Total: 90.50s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (définition de SAPS, lien avec la loi LPR 2021, objectif de rapprocher chercheurs et société, médiation, événements, projets participatifs, lien web) sont directement présentes dans le contexte fourni. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question « C’est quoi les SAPS ? » en donnant une définition claire et en précisant la mission du dispositif.
- **Avis Context Precision** : Le contexte récupéré contient la définition, le cadre législatif, les objectifs et le site web des SAPS, ce qui est suffisant pour répondre à la question.

### Question : Comment peut-on changer le budget d’un projet ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 159.97s, Eval: 9.09s, Total: 169.06s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (contacter le SPIV, fournir un argumentaire scientifique, soumettre un budget modifié validé par l'antenne financière, attendre le retour du financeur) sont directement tirées du texte du contexte. Le seul élément supplémentaire est le contact "Anne Galopin : af.polytech@univ-tours.fr", qui n'est pas présent dans le contexte, mais la règle d'exemption des contacts injectés indique de ne pas pénaliser la fidélité pour ce type d'information.
- **Avis Answer Relevance** : La réponse répond exactement à la question « Comment peut-on changer le budget d’un projet ? » en décrivant la procédure à suivre. Aucun élément hors sujet n'est ajouté.
- **Avis Context Precision** : Le contexte fourni contient une section dédiée aux demandes de modification budgétaire via le SPIV, incluant les étapes et les documents requis. Il est donc parfaitement adapté pour répondre à la question.

### Question : Quelles sont les différentes démarches à effectuer ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 133.03s, Eval: 8.64s, Total: 141.67s
- **Tokens générés** : 0
- **Avis Faithfulness** : Aucune affirmation n'est présente dans la réponse, il n'y a donc aucune information qui puisse être en contradiction avec le contexte fourni. Aucun élément n'est halluciné.
- **Avis Answer Relevance** : La question « Quelles sont les différentes démarches à effectuer ? » n'est pas du tout traitée par la réponse qui est vide ou inexistante, ce qui la rend hors sujet et inutile pour l'utilisateur.
- **Avis Context Precision** : Le contexte récupéré contient de nombreuses informations détaillées sur les démarches (pièces justificatives, dépôt PDF, lecture de la Charte du doctorat, transmission du dossier aux différentes directions, etc.). Le contexte est donc parfaitement pertinent et complet pour répondre à la question.

### Question : - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire extérieur? Est-ce gratuit?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 3.0/5, Context Precision: 4.0/5
- **Temps** : RAG: 227.70s, Eval: 7.99s, Total: 235.69s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations (nécessité d’un contrat, partage de la propriété intellectuelle, recours au SPIV) sont présentes dans le contexte fourni. Le contact Hélène Jullien est un contact injecté et, selon les règles, ne pénalise pas la fidélité.
- **Avis Answer Relevance** : La réponse indique le cadre contractuel requis, ce qui répond partiellement à la première partie de la question. Cependant, elle ne répond pas explicitement à la seconde partie (« Est‑ce gratuit ? »), ce qui rend la pertinence partielle.
- **Avis Context Precision** : Le contexte contient les informations sur le cadre contractuel et le service à contacter pour les aspects financiers, mais il ne précise pas si les expérimentations sont gratuites. Le contexte est donc pertinent mais incomplet pour la question de gratuité.

### Question : A quelle adresse postale ou mail dois-je envoyer mon projet ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 139.26s, Eval: 5.14s, Total: 144.40s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient que l'adresse e‑mail de Morgane Guibert, qui figure exactement dans le contexte fourni. Aucun élément n'est ajouté en dehors du contexte.
- **Avis Answer Relevance** : La question demande une adresse postale ou e‑mail pour envoyer le projet. La réponse fournit une adresse e‑mail pertinente, répondant directement à la demande.
- **Avis Context Precision** : Le contexte comprend l'e‑mail de la responsable du pôle (morgane.guibert@univ-tours.fr) ainsi que d'autres contacts. L'information nécessaire était donc bien présente.

### Question : Comment m’inscrire / me réinscrire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 131.82s, Eval: 16.19s, Total: 148.01s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement tirées du contexte : création d'un compte ADUM, dépôt des pièces justificatives en un seul PDF, validation de la Charte du doctorat, transmission du dossier aux différents validateurs, mise à jour des informations, dépôt de la Convention Individuelle de Formation, date limite du 15 novembre. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question « Comment m’inscrire / me réinscrire ? » en donnant les étapes concrètes pour l’inscription et la réinscription, sans digression.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires (procédure ADUM, documents requis, validation en chaîne, date limite) et celles‑ci sont utilisées dans la réponse.

### Question : Quelles ressources le Pôle SAPS peut m’apporter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 81.87s, Eval: 8.47s, Total: 90.34s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (accompagnement, formations, événements, projets arts/sciences, adresse e‑mail) sont directement présentes dans le contexte. Aucun élément n’est inventé ; les contacts sont explicitement listés dans le contexte, ce qui respecte la règle d’exemption des contacts.
- **Avis Answer Relevance** : La réponse répond exactement à la question « Quelles ressources le Pôle SAPS peut‑moi apporter ? » en présentant les principales catégories de ressources (accompagnement, formation, événements, projets arts/sciences) et en indiquant le contact. Aucun hors‑sujet n’est introduit.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires pour répondre : missions du pôle, types d’accompagnement, catalogue de formations, événements organisés, projets arts/sciences, etc. Le texte est donc parfaitement ciblé.

### Question : Y a-t-il des alumni ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 1.0/5
- **Temps** : RAG: 120.21s, Eval: 5.05s, Total: 125.26s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse fournie est vide, elle ne contient aucune affirmation. Ainsi, il n'y a aucune information qui puisse être en contradiction avec le contexte ; aucune hallucination n'est détectée.
- **Avis Answer Relevance** : La question porte sur l'existence d'alumni. La réponse ne fournit aucune information à ce sujet, donc elle ne répond pas du tout à la question.
- **Avis Context Precision** : Le contexte récupéré ne mentionne pas les alumni ; il porte sur l'encadrement de thèse, les services numériques, le programme PAUSE, etc. Le contexte n'est donc pas pertinent pour répondre à la question.

### Question : Que propose le Pôle SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 87.26s, Eval: 8.10s, Total: 95.36s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (médiation, événements comme DéTours des sciences, Ma thèse en 180 secondes, Fête de la science, formations mediatraining, accompagnement des chercheurs, conseils pour dépôts de projets ANR/ APR‑IR, projets arts‑sciences Kaléidoscope et Ma thèse en BD) sont directement présentes dans le contexte. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question « Que propose le Pôle SAPS ? » en listant les services et activités proposés. Aucun hors‑sujet n’est introduit.
- **Avis Context Precision** : Le contexte fourni contient l’ensemble des informations nécessaires (missions, événements, formations, accompagnement, projets collaboratifs) pour répondre à la question, et il a été correctement exploité.

### Question : - Qu’est-ce qu’une invention ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 128.04s, Eval: 10.00s, Total: 138.04s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les informations fournies dans la réponse (le contact drv-pi@univ-tours.fr) sont présentes dans le contexte. Aucun élément n'est inventé, donc la fidélité est maximale.
- **Avis Answer Relevance** : La question porte sur la définition d'une invention. La réponse ne fournit qu'un contact et ne répond en rien à la demande, ce qui la rend hors sujet.
- **Avis Context Precision** : Le contexte traite de la législation autour des inventions et des créateurs indépendants, mais il ne contient pas de définition explicite d'une invention. Le contexte est donc seulement vaguement lié à la question.

### Question : - Je souhaite répondre à un Appel à projet?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 217.03s, Eval: 10.83s, Total: 227.86s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (envoi du dossier en PDF, taille maximale 5 Mo, destinataire Caroline Vaslin, adresse e‑mail caroline.vaslin@univ‑tours.fr) sont directement présentes dans le contexte récupéré. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La question porte sur la manière de répondre à un appel à projets. La réponse indique clairement le format attendu et le contact à qui adresser le dossier, répondant ainsi directement à la demande.
- **Avis Context Precision** : Le contexte contient précisément les informations nécessaires (format PDF, taille maximale, nom et e‑mail du destinataire). Le système a extrait exactement ces données.

### Question : je suis en arrêt de travail, qui dois-je contacter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 2.0/5, Context Precision: 3.0/5
- **Temps** : RAG: 120.26s, Eval: 9.49s, Total: 129.75s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement tirées du contexte : les deux liens vers les pages « Congés maladie des agents titulaires » et « Congés maladie des agents contractuels » existent bien dans le texte fourni. Aucun élément inventé n’est présent.
- **Avis Answer Relevance** : La question demande explicitement « qui dois‑je contacter ? ». La réponse ne fournit aucun contact (nom, service, adresse mail, etc.) mais se contente d’orienter vers des pages de procédure. Elle est donc peu pertinente par rapport à la demande.
- **Avis Context Precision** : Le contexte contient des informations utiles sur les congés maladie (les deux liens) ainsi que d’autres indications (ex. : contacter un gestionnaire de la DRH, organigramme DRH) qui pourraient répondre à la question de contact. Le contexte est donc partiellement pertinent mais ne fournit pas directement le contact recherché.

### Question : Combien de temps va prendre mon inscription ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 4.0/5
- **Temps** : RAG: 126.12s, Eval: 16.40s, Total: 142.52s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes ou déduites directement du contexte : le délai dépend de la situation du dossier, les dossiers avec diplôme étranger/DEA ont un délai rallongé, et la procédure de validation successive est décrite. Les coordonnées fournies sont des contacts présents dans le contexte (même si la forme exacte diffère, les règles précisent de ne pas pénaliser les contacts). Aucun élément inventé n'est ajouté.
- **Avis Answer Relevance** : La réponse répond à la question « Combien de temps va prendre mon inscription ? » en expliquant que le délai varie selon le type de dossier et en conseillant de contacter le service pour obtenir un délai précis. Elle reste centrée sur la demande, même si elle ne donne pas de durée chiffrée précise, ce qui est cohérent avec le manque d'information exacte dans le contexte.
- **Avis Context Precision** : Le contexte fourni contient les informations nécessaires pour indiquer que le délai dépend du type de dossier et que les dossiers avec diplôme étranger sont plus longs. Ces éléments sont exploités dans la réponse. Le contexte ne donne pas de durée exacte, mais il fournit bien les éléments de variation du délai.

### Question : Comment avoir un email ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 119.95s, Eval: 10.02s, Total: 129.97s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : le texte indique que l'« Adresse électronique principale (identifiant de connexion ADUM) » est créée lors de la création du compte ADUM et sert à recevoir les mails liés au parcours doctoral. Aucun élément n’est ajouté de façon externe.
- **Avis Answer Relevance** : La réponse répond à la question « Comment avoir un email ? » en expliquant que l'email est obtenu en créant un compte ADUM. Elle est pertinente, bien que très concise et ne détaille pas les étapes exactes de création.
- **Avis Context Precision** : Le contexte fourni contient explicitement les informations sur l’adresse électronique principale liée à ADUM, ainsi que son rôle pour la réception des communications. Le contexte est donc parfaitement adapté à la question.

### Question : - Je souhaite me procurer le formulaire de déclaration d’invention de l’université, à qui dois-je m’adresser ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 127.61s, Eval: 9.18s, Total: 136.79s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les informations fournies dans la réponse (contact du PJR via l’adresse drv-pi@univ-tours.fr) sont présentes dans le contexte. Aucun élément n’a été inventé. Les contacts ajoutés automatiquement par le système ne sont pas pénalisés, mais ici ils ne sont pas présents dans la réponse.
- **Avis Answer Relevance** : La question demande à qui s’adresser pour obtenir le formulaire de déclaration d’invention. La réponse indique clairement le service (Pôle Juridique Recherche) et l’adresse e‑mail à utiliser, répondant directement à la demande.
- **Avis Context Precision** : Le contexte décrit le rôle du PJR dans l’instruction des déclarations d’invention et fournit l’adresse générique drv-pi@univ-tours.fr pour les questions de propriété intellectuelle. Ces informations sont exactement celles nécessaires pour répondre à la question.

### Question : Qui contacter pour toute demande d'ouvrages en service presse ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 1.0/5
- **Temps** : RAG: 125.99s, Eval: 7.73s, Total: 133.72s
- **Tokens générés** : 0
- **Avis Faithfulness** : Aucune affirmation n'est présentée dans la réponse, il n'y a donc aucune information qui puisse être en contradiction avec le contexte. Aucun élément halluciné n'est détecté, ce qui justifie le score maximal de 5.
- **Avis Answer Relevance** : La question demande "Qui contacter pour toute demande d'ouvrages en service presse ?" La réponse fournie est vide, ne mentionne aucun contact et ne répond donc pas du tout à la demande, d'où le score de 1.
- **Avis Context Precision** : Le contexte récupéré ne contient aucune information relative aux contacts du service presse ou aux demandes d'ouvrages. Ainsi, le contexte n'est pas pertinent pour répondre à la question, ce qui justifie le score de 1.

### Question : comment enregistrer ma demande de formation hors-catalogue et quels documents dois-je fournir ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 141.57s, Eval: 8.09s, Total: 149.66s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement tirées du contexte fourni : connexion à ADUM, navigation vers la rubrique « déclaration des formations hors-catalogue », champs à renseigner, nécessité d’envoyer un email préalable, et documents à joindre (fiche de validation et justificatifs). Le contact ajouté n’est pas pénalisé selon la règle sur les contacts injectés.
- **Avis Answer Relevance** : La réponse répond exactement à la question en expliquant comment enregistrer la demande et quels documents fournir, sans digression.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires (procédure ADUM, champs requis, documents obligatoires, email préalable) et celles‑ci sont utilisées dans la réponse.

### Question : Mon jury de thèse est-il valide ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 140.00s, Eval: 20.00s, Total: 160.00s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations du système (nombre de membres, proportion de professeurs, extérieurs, non‑impliqués, présence d’un HDR, équilibre femmes/hommes, règle du tiers à distance, présence du directeur de thèse et du candidat) sont directement tirées du contexte. Aucun élément factuel n’est inventé. Le seul ajout – les coordonnées de contact – est explicitement exempté par les consignes et n’est donc pas pénalisé.
- **Avis Answer Relevance** : La question demande de savoir si le jury est valide. La réponse fournit une checklist exhaustive des critères à vérifier, ce qui permet à l’utilisateur de juger de la validité de son jury. Elle répond donc pleinement à la demande sans digression.
- **Avis Context Precision** : Le contexte récupéré contient l’ensemble des règles de composition du jury (nombre de membres, proportions, HDR, émérite, distance, présence physique, etc.). Il est donc parfaitement adapté pour répondre à la question.

### Question : quels types de financement de thèse existent ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 141.52s, Eval: 10.81s, Total: 152.33s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte. Le contrat doctoral, les différentes bourses (régionale, départementale, industrielle, associative, étrangère), les financements publics (ANR, Europe, Labex, région Centre‑Val de Loire, bourses Rabelaisiennes), les contrats partenariaux (CIFRE, DGA, ADEME, contrats avec entreprises) et le statut salarié avec convention de formation sont explicitement mentionnés dans le texte fourni.
- **Avis Answer Relevance** : La question porte sur les types de financement de thèse. La réponse énumère précisément ces types, sans digression, répondant ainsi de façon exhaustive à la demande.
- **Avis Context Precision** : Le contexte récupéré contient l’ensemble des catégories de financement citées dans la réponse : contrats doctoraux, diverses bourses, financements publics (ANR, Europe, Labex, régionaux, universitaires), contrats CIFRE/DGA/ADEME et salariat. Il est donc parfaitement adapté.

### Question : - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autre CHRU?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 140.15s, Eval: 13.03s, Total: 153.18s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement tirées du contexte fourni : le texte décrit deux cas (unité tutelle de l'UT et du CHRU, ou unité non tutelle) et indique la forme de la signature en deux lignes avec les mentions « Université de Tours » et « CHRU de Tours, Service, 37XXX Tours, France ». Le contact ajouté est un contact injecté, qui selon les règles ne doit pas être pénalisé.
- **Avis Answer Relevance** : La question porte sur la manière de procéder avec des échantillons provenant du CHRU de Tours ou d'un autre CHRU. La réponse donne précisément les règles de signature à appliquer, répondant ainsi directement à la demande.
- **Avis Context Precision** : Le contexte retrouvé contient la section « Partenariat CHRU de Tours ou Hôpital » qui fournit les instructions exactes sur la rédaction des affiliations et signatures pour les auteurs hospitalo-universitaires. Le contexte est donc parfaitement pertinent.

### Question : Je souhaite monter un projet, comment faire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 148.12s, Eval: 17.87s, Total: 165.99s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : le besoin de saisir le service SCRIPT en amont est explicitement indiqué, ainsi que l’adresse e‑mail projets‑etablissement@univ‑tours.fr. Le nom et les coordonnées de Justine Gillet ne figurent pas dans le contexte, mais les consignes précisent de ne pas pénaliser les informations de contact absentes du contexte, donc la note reste maximale.
- **Avis Answer Relevance** : La réponse répond directement à la question « comment monter un projet ? » en indiquant la première démarche obligatoire (contacter le service SCRIPT). Elle fournit un contact concret, ce qui est pertinent, mais ne détaille pas les étapes suivantes du processus, d’où une petite perte de pertinence.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires pour répondre à la question, notamment l’obligation de saisir le service SCRIPT, l’adresse de saisine et le rôle du service dans le montage du projet. Le contexte est donc parfaitement ciblé.

### Question : - Comment protéger un savoir-faire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 143.28s, Eval: 13.13s, Total: 156.41s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse se retrouvent dans le contexte : le texte insiste sur la nécessité d’une convention/charte de confidentialité pour les collaborateurs bénévoles et les émérites, et indique que cela protège les informations confidentielles du laboratoire, ce qui inclut le savoir‑faire. Aucun élément externe n’est introduit. Le contact fourni est explicitement exempté de pénalité selon les règles d’évaluation.
- **Avis Answer Relevance** : La question porte sur la protection d’un savoir‑faire. La réponse propose la solution principale évoquée dans le contexte – la signature d’une convention de confidentialité – et précise son rôle dans les projets partenariaux, répondant ainsi directement à la demande.
- **Avis Context Precision** : Le contexte fourni contient les informations nécessaires : exigences de confidentialité, existence d’accords/charte, obligation pour les émérites, et importance de sécuriser les informations en recherche partenariale. Le système a correctement exploité ces éléments.

### Question : Je pars en mission, quelle pièce dois-je remplir ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 197.36s, Eval: 5.38s, Total: 202.74s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse indique uniquement qu'il faut remplir le formulaire « AUTORISATION DE DEPLACEMENT », information qui apparaît explicitement dans le contexte (section « AUTORISATION DE DEPLACEMENT »). Aucun autre fait n'est ajouté, le contact mentionné est exempté de pénalité selon la règle des contacts injectés.
- **Avis Answer Relevance** : La question demande quelle pièce remplir pour une mission. La réponse fournit exactement ce document, répondant ainsi de façon ciblée et complète.
- **Avis Context Precision** : Le contexte contient la section dédiée au formulaire d'autorisation de déplacement, incluant son titre et sa description. Cette information est suffisante pour répondre à la question.

### Question : Quel est le délai moyen entre la soumission d’un manuscrit et sa publication ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 237.00s, Eval: 8.55s, Total: 245.55s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient aucune affirmation qui contredit le contexte. Le seul élément fourni est une information de contact, qui selon les règles n'est pas considéré comme une hallucination. Aucun autre contenu n'est présent, donc aucune affirmation erronée n'est détectée.
- **Avis Answer Relevance** : La question porte sur le délai moyen entre la soumission d’un manuscrit et sa publication. La réponse fournie se limite à un contact (Morgane Guibert) et ne répond en rien à la question posée.
- **Avis Context Precision** : Le contexte récupéré mentionne des délais légaux (maximum de six mois pour les sciences, technique, médecine et douze mois pour les sciences humaines et sociales) relatifs à la mise à disposition ouverte d’un manuscrit après publication, mais il ne fournit pas le délai moyen entre soumission et publication. Ainsi, le contexte est seulement vaguement lié au sujet du délai, sans fournir l'information recherchée.

## 02_fast_draft

### Question : C’est quoi les SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 83.35s, Eval: 12.92s, Total: 96.27s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse se retrouvent dans le contexte : le sigle SAPS = Sciences Avec et Pour la Société, le lien avec la loi LPR 2021, l’objectif de renforcer le dialogue entre chercheurs et citoyens, la médiation scientifique, la co‑construction de projets et les exemples d’événements (Village des sciences, « Ma thèse en 180 secondes »). Le lien saps.univ‑tours.fr apparaît également dans le contexte. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond directement à la question « C’est quoi les SAPS ? » en donnant une définition claire et en précisant la mission principale du dispositif. Aucun hors‑sujet n’est présent.
- **Avis Context Precision** : Le contexte fourni contient la définition, les objectifs, le cadre législatif et des exemples d’activités des SAPS, ce qui est exactement ce qui est nécessaire pour répondre à la question.

### Question : Comment peut-on changer le budget d’un projet ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 173.16s, Eval: 8.57s, Total: 181.73s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (contacter le SPIV, fournir un argumentaire scientifique, soumettre un budget modifié validé par l'antenne financière, attendre l'accord écrit du financeur) sont directement présentes dans le contexte. Le seul élément supplémentaire est un contact nommé, mais les règles précisent de ne pas pénaliser la fidélité pour les contacts ajoutés.
- **Avis Answer Relevance** : La réponse répond exactement à la question « Comment peut-on changer le budget d’un projet ? » en décrivant la procédure à suivre, sans digression.
- **Avis Context Precision** : Le contexte contient la section « Gérer les aléas (demande d’avenant ou de modification) » qui fournit toutes les informations nécessaires pour répondre à la question, et ces informations sont correctement exploitées.

### Question : Quelles sont les différentes démarches à effectuer ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 117.19s, Eval: 6.08s, Total: 123.27s
- **Tokens générés** : 0
- **Avis Faithfulness** : Aucune affirmation n'est présentée dans la réponse du système, il n'y a donc aucune information qui puisse être en contradiction avec le contexte. Aucun élément inventé n'est détecté, ce qui justifie le score maximal de 5.
- **Avis Answer Relevance** : La question demandait « Quelles sont les différentes démarches à effectuer ? ». La réponse du système est vide (ou ne contient aucun texte), ne fournit donc aucune information utile et ne répond pas du tout à la demande, d'où le score de 1.
- **Avis Context Precision** : Le contexte récupéré contient de nombreuses informations sur les démarches liées au RGPD, aux demandes de mobilité, aux formalités administratives, aux contacts, etc. Il est donc pleinement pertinent et complet pour répondre à la question, ce qui mérite un 5.

### Question : - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire extérieur? Est-ce gratuit?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 3.0/5, Context Precision: 4.0/5
- **Temps** : RAG: 238.87s, Eval: 9.29s, Total: 248.16s
- **Tokens générés** : 0
- **Avis Faithfulness** : Les affirmations concernant l’obligation d’un contrat et la copropriété du brevet sont présentes dans le contexte. En revanche, le nom et le numéro de téléphone de Hélène Jullien ne figurent pas dans le texte fourni, ce qui constitue une hallucination. Le reste du texte reste fidèle au contexte.
- **Avis Answer Relevance** : La réponse indique qu’un contrat est nécessaire, ce qui répond partiellement à la première partie de la question. Cependant, elle ne répond pas clairement à la question « Est‑ce gratuit ? », se limitant à inviter à contacter quelqu’un pour les modalités financières, ce qui rend la réponse partiellement pertinente.
- **Avis Context Precision** : Le contexte contient les informations essentielles sur le besoin d’un contrat et la gestion de la propriété intellectuelle, ainsi que des indications que l’université n’exige pas de contrepartie financière dans certains cas. Il manque toutefois une mention explicite du caractère gratuit, ce qui rend le contexte légèrement incomplet pour répondre à la deuxième partie de la question.

### Question : A quelle adresse postale ou mail dois-je envoyer mon projet ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 120.16s, Eval: 6.25s, Total: 126.41s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les informations fournies dans la réponse (nom et adresse e‑mail de Morgane Guibert) sont présentes dans le contexte. Aucun élément n’a été inventé.
- **Avis Answer Relevance** : La réponse répond directement à la question en indiquant une adresse e‑mail où envoyer le projet. Aucun hors‑sujet n’est introduit.
- **Avis Context Precision** : Le contexte contient l’adresse e‑mail de la responsable du pôle (morgane.guibert@univ-tours.fr) ainsi que d’autres contacts pertinents, ce qui suffit pour répondre à la question.

### Question : Comment m’inscrire / me réinscrire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 221.21s, Eval: 11.83s, Total: 233.04s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (création d'un compte ADUM, période du 1 er juin au 15 novembre, dépôt de la Convention Individuelle de Formation et du rapport d'avancement, validation par la direction de thèse, laboratoire, école doctorale et établissement) sont directement présentes dans le contexte. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question « Comment m’inscrire / me réinscrire ? » en donnant les étapes essentielles à suivre, sans digression.
- **Avis Context Precision** : Le contexte fourni contient les informations nécessaires (création de compte ADUM, dates limites, documents à déposer, validation finale). Ces informations sont bien ciblées et suffisantes pour répondre à la question.

### Question : Quelles ressources le Pôle SAPS peut m’apporter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 80.98s, Eval: 15.00s, Total: 95.98s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : accompagnement (conseil, montage de projets, aide budgétaire, mise en relation avec médiateurs, journalistes), formations (médiation, mediatraining, préparation à « Ma Thèse en 180 secondes », éthique), organisation d'événements (Fête de la science, DéTours des sciences, etc.), projets arts/sciences (Ma thèse en BD, Kaléidoscope) et la Boutique des sciences. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question « Quelles ressources le Pôle SAPS peut‑moi apporter ? » en listant les principales ressources disponibles, sans digression.
- **Avis Context Precision** : Le contexte fourni contient l’ensemble des informations nécessaires (missions du pôle, types de formations, accompagnement, événements, projets arts/sciences, boutique des sciences, lien web). Il est donc parfaitement ciblé.

### Question : Y a-t-il des alumni ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 129.11s, Eval: 8.86s, Total: 137.97s
- **Tokens générés** : 0
- **Avis Faithfulness** : Aucune affirmation n'est présentée dans la réponse ; par conséquent, il n'y a aucune information qui puisse être en contradiction avec le contexte. L'absence d'énoncés signifie que la réponse est entièrement fidèle aux données fournies.
- **Avis Answer Relevance** : La question porte sur l'existence d'alumni. La réponse ne fournit aucune information, ne répond donc pas du tout à la question.
- **Avis Context Precision** : Le contexte récupéré contient principalement des liens vers des pages relatives aux rémunérations, campagnes de carrière, écoles doctorales, etc. Aucun de ces éléments ne mentionne les alumni, ce qui rend le contexte peu pertinent pour la question posée.

### Question : Que propose le Pôle SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 93.41s, Eval: 8.87s, Total: 102.28s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement tirées du contexte fourni : médiation et dialogue (événements, formations, accompagnement), recherche participative (Boutique des sciences), projets arts/sciences (Ma thèse en BD, Kaléidoscope), soutien aux projets (conseil, montage budgétaire, partenaires). Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond précisément à la question « Que propose le Pôle SAPS ? » en listant les services et activités proposés, sans digression.
- **Avis Context Precision** : Le contexte retrouvé contient l’ensemble des informations nécessaires : missions du pôle, types d’événements, formations, accompagnement, projets arts/sciences, etc. Il est donc parfaitement ciblé.

### Question : - Qu’est-ce qu’une invention ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 3.0/5
- **Temps** : RAG: 224.22s, Eval: 9.74s, Total: 233.96s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse décrit l'invention comme une création technique nouvelle, inventive et susceptible d'application industrielle, ce qui correspond à la notion générale d'invention brevetable évoquée dans le contexte. Le texte ne fournit pas explicitement ces trois critères, ils sont donc déduits du contexte. Aucun élément n'est manifestement inventé, d'où une note élevée mais pas parfaite.
- **Avis Answer Relevance** : La question porte sur la définition d'une invention. La réponse fournit directement cette définition, ce qui la rend pleinement pertinente.
- **Avis Context Precision** : Le contexte récupéré traite largement des inventions dans le cadre juridique (décrets, déclarations, régime de dévolution). Il ne contient toutefois pas de définition concise de l'invention, ce qui rend le contexte partiellement adéquat pour répondre à la question.

### Question : - Je souhaite répondre à un Appel à projet?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 138.57s, Eval: 6.22s, Total: 144.79s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte. Le nom Caroline Vaslin et son rôle lié aux appels à projets (AAP) sont explicitement mentionnés. L'adresse e‑mail, bien qu'absente du contexte, est une information de contact et ne doit pas être pénalisée selon les règles.
- **Avis Answer Relevance** : La question demande comment répondre à un appel à projet. La réponse fournit directement le contact approprié pour le faire, répondant ainsi pleinement à la demande.
- **Avis Context Precision** : Le contexte contient les informations nécessaires : le nom de la personne responsable des AAP et son rôle. Aucun autre élément du contexte n'est requis pour répondre à la question.

### Question : je suis en arrêt de travail, qui dois-je contacter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 134.12s, Eval: 6.41s, Total: 140.53s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse indique qu'il faut informer le médecin du travail du Service Prévention Protection Santé Sécurité, localisation Plat d'Etain. Cette information se trouve explicitement dans le contexte (section « Le médecin du travail » et mention que le médecin du travail doit être informé des congés maladie). Aucun élément n'est ajouté hors du contexte.
- **Avis Answer Relevance** : La question demande qui contacter en cas d'arrêt de travail. La réponse fournit exactement le contact requis, répondant ainsi pleinement à la demande.
- **Avis Context Precision** : Le contexte récupéré contient la description du rôle du médecin du travail, son rattachement au service concerné et son lieu, ce qui est exactement ce qui est nécessaire pour répondre à la question.

### Question : Combien de temps va prendre mon inscription ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 2.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 228.82s, Eval: 8.01s, Total: 236.83s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les informations fournies (adresse e‑mail et le fait de contacter la personne) sont présentes dans le contexte. Le nom légèrement différent ("Christele Gaudron‑Bredif") n'est pas pénalisé car il s'agit d'une information de contact, et la règle indique de ne pas pénaliser les contacts absents du contexte.
- **Avis Answer Relevance** : La réponse ne donne pas directement le délai demandé, elle indique seulement de contacter quelqu'un pour l'obtenir. Elle touche au sujet mais ne répond pas réellement à la question du temps d'inscription.
- **Avis Context Precision** : Le contexte ne contient aucune indication chiffrée ou temporelle sur la durée de traitement de l'inscription. Il ne fournit donc pas les informations nécessaires pour répondre précisément à la question.

### Question : Comment avoir un email ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 124.40s, Eval: 6.48s, Total: 130.88s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : le texte indique que tout doctorant dispose d’un compte « étudiant établissement » avec une adresse email sur le domaine etu.univ-tours.fr et que la validité du compte est à l'année universitaire. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond à la question « Comment avoir un email ? » en indiquant que les doctorants en obtiennent automatiquement un compte. C’est pertinent, mais la réponse ne décrit pas les démarches éventuelles pour obtenir ou activer ce compte, ce qui aurait pu être attendu.
- **Avis Context Precision** : Le contexte fourni contient exactement l’information nécessaire sur l’existence d’un compte email pour les doctorants, ainsi que son domaine et sa durée de validité. Le contexte est donc parfaitement ciblé.

### Question : - Je souhaite me procurer le formulaire de déclaration d’invention de l’université, à qui dois-je m’adresser ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 143.06s, Eval: 4.85s, Total: 147.91s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les informations fournies dans la réponse (contacter le PJR via l'adresse drv-pi@univ-tours.fr) sont présentes dans le contexte. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond directement à la question en indiquant à qui s'adresser pour obtenir le formulaire de déclaration d’invention, en précisant le service et l'adresse e‑mail.
- **Avis Context Precision** : Le contexte contient explicitement l'adresse e‑mail générique du PJR (drv-pi@univ-tours.fr) ainsi que la mention que le PJR pilote les déclarations d'invention. Le contexte est donc parfaitement adapté.

### Question : Qui contacter pour toute demande d'ouvrages en service presse ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 1.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 134.81s, Eval: 3.00s, Total: 137.81s
- **Tokens générés** : 0
- **Avis Faithfulness** : Aucune réponse du système n'est fournie dans les données d'évaluation. Par conséquent, aucune affirmation ne peut être vérifiée par rapport au contexte, ce qui constitue une absence totale d'information et donc une très faible fidélité.
- **Avis Answer Relevance** : La question "Qui contacter pour toute demande d'ouvrages en service presse ?" n'est pas du tout traitée, car aucune réponse n'est présentée. La pertinence est donc nulle.
- **Avis Context Precision** : Le contexte récupéré porte principalement sur le RGPD, les contacts du DPO, et divers services administratifs de l'Université de Tours. Il ne contient aucune information explicite concernant un "service presse" ou les contacts associés. Le contexte est donc très peu pertinent pour la question, justifiant un score faible.

### Question : comment enregistrer ma demande de formation hors-catalogue et quels documents dois-je fournir ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 2.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 139.53s, Eval: 9.64s, Total: 149.17s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient aucune information factuelle qui ne provient pas du contexte, à l'exception du contact fourni. Selon la règle, les contacts injectés ne sont pas pénalisés. Aucun autre élément n'est halluciné.
- **Avis Answer Relevance** : La question porte sur la procédure d'enregistrement d'une demande de formation hors-catalogue et les documents à fournir. La réponse ne donne que le nom et l'e‑mail d'un contact, sans expliquer la démarche ni les pièces à fournir, ce qui ne répond pas directement à la demande.
- **Avis Context Precision** : Le contexte retrouvé comprend une liste détaillée des documents requis ainsi que des indications sur la soumission d'une demande d'inscription. Ces informations sont exactement ce qui est nécessaire pour répondre à la question.

### Question : Mon jury de thèse est-il valide ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 3.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 133.86s, Eval: 10.57s, Total: 144.43s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient aucune affirmation factuelle qui ne provient pas du contexte. Elle se limite à demander des informations complémentaires et à fournir un contact qui, bien que non présent dans le contexte, est un contact injecté et ne doit pas être pénalisé. Aucun élément halluciné n'est présenté comme factuel.
- **Avis Answer Relevance** : La réponse est partiellement pertinente : elle indique qu’il faut davantage de précisions pour juger la validité du jury, ce qui est lié à la question, mais elle ne fournit pas d’évaluation concrète du jury actuel.
- **Avis Context Precision** : Le contexte récupéré comporte l’ensemble des règles de composition d’un jury de thèse (nombre de membres, répartition des grades, exigences d’indépendance, etc.). Il est donc parfaitement adapté pour répondre à la question.

### Question : quels types de financement de thèse existent ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 135.80s, Eval: 9.31s, Total: 145.11s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les catégories mentionnées dans la réponse (contrats doctoraux, financements ANR/Europe/Labex, contrats de recherche et entreprise dont CIFRE/DGA/ADEME, bourses gouvernementales/associatives/étrangères, financement salarié, bourses Rabelaisiennes et présidentielles) sont présentes textuellement dans le contexte fourni. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond directement à la question en listant les différents types de financement de thèse, sans digression ni information hors sujet.
- **Avis Context Precision** : Le contexte récupéré contient une section intitulée « Autres financements doctoraux » qui énumère précisément les mêmes sources de financement que celles reprises dans la réponse, ainsi que des mentions de contrats doctoraux « Établissement » et « Collectivités », et des bourses spécifiques (Rabelaisiennes, présidentielles). Le contexte est donc parfaitement adapté.

### Question : - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autre CHRU?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 131.87s, Eval: 8.19s, Total: 140.06s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : le besoin d'un dossier CODECOH pour les échantillons biologiques humains, y compris ceux provenant du CHRU de Tours ou d'un autre CHRU, ainsi que les contacts du Référent Dossier CODECOH et du Conseiller de prévention. Le contact ajouté (Claude‑Emmanuel Boudet) n'est pas pénalisé selon la règle sur les contacts injectés.
- **Avis Answer Relevance** : La réponse répond précisément à la question en indiquant la procédure obligatoire (dossier CODECOH) et les interlocuteurs à contacter pour les échantillons du CHRU de Tours ou d'un autre CHRU.
- **Avis Context Precision** : Le contexte récupéré contient les informations nécessaires sur le dossier CODECOH et les contacts associés, ainsi que la mention explicite du CHRU de Tours, ce qui est exactement ce qui est requis pour répondre à la question.

### Question : Je souhaite monter un projet, comment faire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 3.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 128.80s, Eval: 13.67s, Total: 142.47s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont compatibles avec le contexte. Le seul élément qui n’apparaît pas dans le texte fourni est le contact Justine Gillet, mais la règle d’exemption des contacts injectés indique de ne pas pénaliser la fidélité pour ce type d’information. Aucun autre fait n’est halluciné.
- **Avis Answer Relevance** : La réponse propose un contact pour obtenir de l’aide, ce qui répond partiellement à la question « comment monter un projet ? ». Cependant, elle ne décrit aucune des étapes du montage ni ne mentionne les services réellement présentés dans le contexte, ce qui limite sa pertinence.
- **Avis Context Precision** : Le contexte récupéré contient de nombreuses informations utiles (description du SPIV, rôle du service, contacts, procédure de validation, documents requis, etc.) qui permettent de répondre à la question. Le contexte est donc très précis et pertinent.

### Question : - Comment protéger un savoir-faire ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 3.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 133.98s, Eval: 9.71s, Total: 143.69s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse se limite à indiquer le contact du Pôle Juridique Recherche (PJR) et l'adresse e‑mail drv-pi@univ‑tours.fr, informations qui figurent explicitement dans le contexte. Aucun élément n’est inventé ; la recommandation de contacter le PJR est une inférence raisonnable à partir du rôle décrit du PJR (pilotage du portefeuille de propriété intellectuelle, expertise juridique).
- **Avis Answer Relevance** : La question porte sur les moyens de protéger un savoir‑faire. La réponse indique uniquement de contacter le PJR, ce qui est une piste pertinente mais très partielle ; elle ne décrit pas les mécanismes concrets (confidentialité, conventions, dépôt de brevet, déclaration d’invention, etc.).
- **Avis Context Precision** : Le contexte fourni contient de nombreuses informations relatives à la protection de la propriété intellectuelle, aux conventions de confidentialité, aux obligations des émérites et des bénévoles, ainsi que les coordonnées du PJR. Il est donc pleinement pertinent pour répondre à la question.

### Question : Je pars en mission, quelle pièce dois-je remplir ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 254.17s, Eval: 10.12s, Total: 264.29s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (remplir le formulaire « Autorisation de déplacement » et le lien fourni) sont directement présentes dans le contexte. Aucun élément inventé n'est ajouté, et les contacts éventuels ne sont pas pénalisés selon la règle d'exemption.
- **Avis Answer Relevance** : La question demande la pièce à remplir pour une mission. La réponse indique précisément le formulaire requis, ce qui répond exactement à la demande.
- **Avis Context Precision** : Le contexte contient la section « Autorisation de déplacement » avec le lien vers le formulaire PDF, ce qui fournit l'information nécessaire pour répondre à la question.

### Question : Quel est le délai moyen entre la soumission d’un manuscrit et sa publication ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 129.08s, Eval: 6.39s, Total: 135.47s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient aucune affirmation qui ne provient pas du contexte. Le seul élément ajouté est un contact, qui selon les règles ne doit pas être pénalisé. Aucun contenu halluciné n'est présent.
- **Avis Answer Relevance** : La question porte sur le délai moyen entre la soumission d’un manuscrit et sa publication. La réponse fournie ne donne aucune information à ce sujet, se limitant à un contact, ce qui la rend hors sujet.
- **Avis Context Precision** : Le contexte récupéré parle d’un délai légal (maximum de 6 mois ou 12 mois selon le domaine) concernant la mise à disposition gratuite du manuscrit après publication, mais il ne fournit pas le délai moyen entre soumission et publication. Ainsi le contexte est seulement vaguement lié à la notion de délai, mais ne répond pas à la question demandée.

## 04_meta_mono

### Question : C’est quoi les SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 71.95s, Eval: 9.28s, Total: 81.23s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : le sigle SAPS signifie Sciences Avec et Pour la Société, il s’agit d’un pôle de l'Université de Tours, il vise à rapprocher chercheurs et société, à favoriser le dialogue et la médiation scientifique, et ses trois missions principales (répondre aux sollicitations extérieures, organiser des points de rencontre, accompagner les chercheurs) sont explicitement décrites dans le texte. L’adresse e‑mail fournie figure également dans la partie contacts du contexte. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La question demande une définition des SAPS. La réponse fournit exactement cette définition ainsi que leurs objectifs principaux, répondant ainsi pleinement à la demande.
- **Avis Context Precision** : Le contexte récupéré contient la définition du sigle, le cadre institutionnel, les missions et même les coordonnées de contact. Il est donc parfaitement adapté pour répondre à la question.

### Question : Comment peut-on changer le budget d’un projet ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 144.72s, Eval: 10.95s, Total: 155.67s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations concernant la procédure (contacter le SPIV, fournir un argumentaire scientifique, fournir un budget modifié conforme au financeur, analyse par le SPIV en interaction avec l'Antenne Financière) sont directement tirées du contexte. Le seul élément ajouté est un contact nommé (Anne Galopin), mais les règles précisent de ne pas pénaliser les informations de contact absentes du contexte.
- **Avis Answer Relevance** : La réponse répond exactement à la question « Comment peut-on changer le budget d’un projet ? » en indiquant les étapes à suivre et le service à contacter, sans digression.
- **Avis Context Precision** : Le contexte contient la section « Gérer les aléas (demande d’avenant ou de modification) » qui décrit précisément la procédure de modification budgétaire, ce qui est exactement ce dont la réponse a besoin.

### Question : Quelles sont les différentes démarches à effectuer ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 2.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 335.55s, Eval: 7.41s, Total: 342.96s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les informations fournies (contact du Service RED, nom d'Aurélie Pétereau, numéro de téléphone et adresse e‑mail) sont présentes dans le contexte. Aucun élément inventé n’est ajouté, à l’exception d’une suggestion générique de consulter le site web, qui n’est pas une hallucination grave. Le score est donc 4.
- **Avis Answer Relevance** : La question demande « les différentes démarches à effectuer ». La réponse ne décrit aucune démarche concrète (ex. constitution du dossier, pièces à fournir, étapes de dépôt, validation par la commission, etc.) et se limite à indiquer un point de contact. Elle ne répond donc pas réellement à la demande, d’où un score de 2.
- **Avis Context Precision** : Le contexte récupéré contient de nombreuses informations détaillées sur les démarches liées à l’HDR, à la mobilité, aux dossiers de candidature, aux pièces à fournir, etc. Il est donc parfaitement pertinent pour répondre à la question. Score = 5.

### Question : - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire extérieur? Est-ce gratuit?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 3.0/5, Context Precision: 3.0/5
- **Temps** : RAG: 133.05s, Eval: 9.10s, Total: 142.15s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse cite le document "Guide du DU/La propriété intellectuelle.md" qui n’apparaît pas dans le contexte fourni. Le contexte mentionne plutôt un guide des projets et contrats de recherche, mais pas ce titre précis. Le reste (contact du SPIV, mention du Service Partenariats Innovations Valorisation) est présent dans le contexte. La présence d’une information inventée fait baisser la note.
- **Avis Answer Relevance** : La réponse indique où chercher le cadre juridique (un guide) et propose de contacter le SPIV, ce qui répond partiellement à la première partie de la question. Cependant, elle ne répond pas du tout à la seconde partie (est‑ce gratuit ?), ce qui limite la pertinence globale.
- **Avis Context Precision** : Le contexte contient des informations sur les conventions de partenariat, la propriété intellectuelle et le rôle du SPIV, mais il ne fournit pas de réponse explicite sur la gratuité des expérimentations. Ainsi le contexte est partiellement utile, mais incomplet pour répondre à la question dans son intégralité.

### Question : A quelle adresse postale ou mail dois-je envoyer mon projet ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 125.82s, Eval: 8.28s, Total: 134.10s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les informations fournies dans la réponse (drv-pi@univ-tours.fr et morgane.guibert@univ-tours.fr) sont présentes textuellement dans le contexte. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La question demande une adresse postale ou mail pour envoyer un projet. La réponse propose deux adresses e‑mail appropriées, ce qui répond directement à la demande.
- **Avis Context Precision** : Le contexte contient les adresses e‑mail mentionnées dans la réponse ainsi que l’indication de privilégier l’adresse générique drv-pi@univ-tours.fr. Le contexte ne fournit aucune adresse postale, mais il fournit suffisamment d’informations e‑mail pour répondre.

### Question : Comment m’inscrire / me réinscrire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 142.93s, Eval: 8.97s, Total: 151.90s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement tirées du contexte : connexion à ADUM, suivi du tutoriel, dépôt de la Convention Individuelle de Formation et des documents, envoi du dossier à la direction de thèse, validation avant le 15 novembre. Aucun élément n’est inventé, y compris les coordonnées de contact qui figurent bien dans le contexte.
- **Avis Answer Relevance** : La réponse répond précisément à la question « Comment m’inscrire / me réinscrire ? » en décrivant la procédure à suivre, les pièces à déposer et les échéances, ce qui correspond exactement à ce qui était demandé.
- **Avis Context Precision** : Le contexte fourni contient l’ensemble des informations nécessaires (procédure ADUM, documents requis, dates limites, contacts). Il a été correctement exploité pour générer la réponse.

### Question : Quelles ressources le Pôle SAPS peut m’apporter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 95.72s, Eval: 8.33s, Total: 104.05s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (faciliter les échanges, former à la médiation, organiser des événements/animations, accompagner aux événements nationaux) sont directement présentes dans le contexte. Les coordonnées fournies figurent également dans le texte. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond à la question en listant les principales catégories de ressources offertes par le Pôle SAPS. Elle reste pertinente, même si elle ne détaille pas l’ensemble des services disponibles.
- **Avis Context Precision** : Le contexte fourni contient une description exhaustive des missions, formations, accompagnements, projets et événements du Pôle SAPS, suffisante pour répondre à la question.

### Question : Y a-t-il des alumni ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 5.0/5, Context Precision: 1.0/5
- **Temps** : RAG: 143.56s, Eval: 7.65s, Total: 151.21s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse affirme l'existence d'un réseau d'alumni, fournit un lien et une adresse e‑mail qui ne figurent pas du tout dans le contexte fourni. Ces informations sont donc des hallucinations. Les contacts injectés sont exemptés de pénalité, mais le reste de l'affirmation n'est pas traçable dans le texte.
- **Avis Answer Relevance** : La question porte sur l'existence d'alumni. La réponse répond directement en indiquant qu'il y en a, en donnant un lien et un contact, ce qui correspond exactement à la demande.
- **Avis Context Precision** : Le contexte récupéré parle de libertés, d'associations étudiantes, de procédures de domiciliation, etc., et ne mentionne aucune information relative aux alumni. Le contexte n'est donc pas du tout pertinent pour répondre à la question.

### Question : Que propose le Pôle SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 89.38s, Eval: 13.41s, Total: 102.79s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte fourni : le Pôle SAPS propose des formations (médiation scientifique, éthique, vulgarisation, préparation au concours "Ma Thèse en 180 secondes"), des événements (Fête de la Science, Nocturnes de l'Histoire, festival (Re)Cherche et Trouve, finale régionale) et des projets (Boutique des sciences, Label SAPS, projets arts/sciences, partenariats scientifiques pour la classe). Aucun élément n’est inventé, y compris les coordonnées qui figurent déjà dans le contexte.
- **Avis Answer Relevance** : La réponse répond directement à la question « Que propose le Pôle SAPS ? » en listant les principales offres (formations, événements, projets) avec des exemples concrets. Aucun hors‑sujet n’est présent.
- **Avis Context Precision** : Le contexte récupéré contient l’ensemble des informations nécessaires : description des missions, des formations, des événements et des projets du Pôle SAPS. Il est donc parfaitement adapté à la question.

### Question : - Qu’est-ce qu’une invention ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 3.0/5, Context Precision: 3.0/5
- **Temps** : RAG: 121.98s, Eval: 9.42s, Total: 131.40s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse affirme que « une invention est un résultat brevetable obtenu par un Créateur Indépendant, qui est un inventeur non‑salarié ni agent public, accueilli par une personne morale réalisant de la recherche ». Cette définition n’apparaît nulle part dans le contexte fourni ; le texte parle d’inventeurs, de créateurs indépendants et de la dévolution des droits, mais ne définit pas l’invention de cette façon. Ainsi plusieurs affirmations sont hallucinations.
- **Avis Answer Relevance** : La réponse tente de répondre à la question « Qu’est‑ce qu’une invention ? » en proposant une définition, ce qui est pertinent. Cependant, la définition est inexacte par rapport au contexte, et la réponse ne couvre pas d’autres aspects possibles (ex. critères de brevetabilité). Elle reste donc partiellement pertinente.
- **Avis Context Precision** : Le contexte fourni traite du régime juridique des inventions, des inventeurs et des créateurs indépendants, mais ne contient pas de définition claire de l’invention. Le contexte est donc partiellement utile, mais il manque les éléments nécessaires pour fournir une définition précise.

### Question : - Je souhaite répondre à un Appel à projet?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 156.36s, Eval: 0.00s, Total: 156.36s
- **Tokens générés** : 0

### Question : je suis en arrêt de travail, qui dois-je contacter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 132.83s, Eval: 8.04s, Total: 140.87s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : le médecin du travail est le contact indiqué et il est rattaché au Service Prévention Protection Santé Sécurité, situé au Plat d'Etain (Relais Santé au Travail). Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question « qui dois‑je contacter ? » en indiquant le médecin du travail, ce qui est la réponse attendue pour un arrêt de travail.
- **Avis Context Precision** : Le contexte fourni contient la description du médecin du travail, son rattachement et son lieu, ce qui suffit pleinement à répondre à la question.

### Question : Combien de temps va prendre mon inscription ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 4.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 136.41s, Eval: 15.29s, Total: 151.70s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse mentionne que la durée de traitement peut varier et donne une estimation vague. Cette information n'apparaît pas dans le contexte fourni, qui ne contient aucune indication sur les délais d'inscription. Le reste de la réponse (référence à la Charte du doctorat) est présent dans le contexte. Ainsi, la réponse comporte à la fois des éléments fondés et des éléments non‑supportés, justifiant une note moyenne.
- **Avis Answer Relevance** : La réponse s'adresse directement à la question du temps d'inscription en expliquant qu'il est difficile de donner une durée précise et en proposant des pistes (consultation de la charte, contact d'un responsable). Elle reste pertinente, même si elle ne fournit pas de chiffre concret.
- **Avis Context Precision** : Le contexte fourni décrit les documents à fournir, les étapes de dépôt et la nécessité de lire la Charte du doctorat, mais il ne mentionne aucun délai de traitement. Le contexte est donc seulement partiellement lié à la question de durée.

### Question : Comment avoir un email ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 3.0/5, Context Precision: 3.0/5
- **Temps** : RAG: 136.12s, Eval: 13.00s, Total: 149.12s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse indique qu'il faut se rendre sur https://pal.univ-tours.fr pour demander un compte email. Le contexte mentionne ce lien uniquement pour le prêt de matériel non chiffré, pas pour la création d'un compte de messagerie. Ainsi, cette information n'est pas supportée par le texte fourni, ce qui constitue une hallucination. Le reste de la phrase (demander un compte « étudiant établissement » ou « personnel ») est présent dans le contexte, mais l'association avec le lien est erronée.
- **Avis Answer Relevance** : La réponse tente de répondre à la question « Comment avoir un email ? » en proposant une procédure, mais la procédure proposée est incorrecte. Elle reste néanmoins centrée sur le sujet de l'obtention d'un compte email, ce qui lui vaut une note moyenne.
- **Avis Context Precision** : Le contexte contient des informations pertinentes sur les comptes email (ex. chaque doctorant possède un compte « étudiant établissement », possibilité de demander un compte « personnel », contacts DSI). Cependant, il ne fournit pas de lien direct ou d'instructions précises pour créer le compte, ce qui rend le contexte partiellement adéquat.

### Question : - Je souhaite me procurer le formulaire de déclaration d’invention de l’université, à qui dois-je m’adresser ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 137.61s, Eval: 11.93s, Total: 149.54s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (adresse du PJR, contact de Morgane Guibert, adresse générique drv-pi@univ-tours.fr) sont présentes textuellement dans le contexte fourni. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond directement à la question en indiquant à qui s’adresser pour obtenir le formulaire de déclaration d’invention, en proposant le PJR et un contact précis.
- **Avis Context Precision** : Le contexte contient les informations nécessaires : le Pôle Juridique Recherche, son rôle d’instruction des déclarations d’invention, et les adresses e‑mail des responsables. Le contexte est donc parfaitement adapté.

### Question : Qui contacter pour toute demande d'ouvrages en service presse ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 3.0/5
- **Temps** : RAG: 128.38s, Eval: 11.27s, Total: 139.65s
- **Tokens générés** : 0
- **Avis Faithfulness** : L'email spiv@univ-tours.fr figure bien dans le contexte, mais le contexte ne précise pas qu'il s'agit du "service presse". L'attribution du rôle de service presse à cet email n'est pas explicitement supportée, ce qui constitue une légère hallucination.
- **Avis Answer Relevance** : La réponse fournit directement un contact pour les demandes d'ouvrages en service presse, répondant ainsi pleinement à la question posée.
- **Avis Context Precision** : Le contexte contient des informations de contact (spiv@univ-tours.fr) mais ne mentionne pas explicitement le service presse. Le contexte est donc partiellement pertinent, mais il manque la désignation précise recherchée.

### Question : comment enregistrer ma demande de formation hors-catalogue et quels documents dois-je fournir ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 4.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 139.70s, Eval: 13.37s, Total: 153.07s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse introduit plusieurs informations qui ne figurent pas dans le contexte fourni : il n’est jamais fait mention d’un « service de la formation continue », ni d’une liste précise de documents (CV, projet de formation, etc.) à fournir, ni de l’adresse e‑mail lucie.primault@univ‑tours.fr. Ces éléments sont donc des hallucinations. Seules les références au "Guide des DU (Vademecum des DU)" et au "Conseiller Mobilité Carrière" sont présentes dans le contexte.
- **Avis Answer Relevance** : La réponse répond globalement à la question en indiquant où se renseigner et quels types de documents pourraient être attendus. Elle reste donc pertinente, même si les détails fournis ne sont pas justifiés par le contexte.
- **Avis Context Precision** : Le contexte récupéré ne contient pas d’instructions précises sur la procédure d’enregistrement d’une formation hors‑catalogue ni sur les pièces à fournir. Il ne fournit que des liens généraux (Guide des DU, Conseiller Mobilité Carrière) qui ne suffisent pas à répondre complètement à la question.

### Question : Mon jury de thèse est-il valide ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 140.57s, Eval: 13.16s, Total: 153.73s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations concernant les règles de composition du jury (4‑8 membres, moitié professeurs ou rang A, moitié extérieurs, présence d'au moins un HDR, etc.) sont directement présentes dans le contexte. Le contact mentionné (Christele Gaudron‑Bredif) n'est pas dans le contexte, mais la consigne indique de ne pas pénaliser les informations de contact ajoutées automatiquement.
- **Avis Answer Relevance** : La réponse fournit les critères à vérifier pour juger de la validité du jury, ce qui répond à la demande de l'utilisateur. Elle ne donne pas de verdict direct sur le jury spécifique de l'utilisateur, mais indique les étapes à suivre, ce qui reste pertinent bien que partiellement complet.
- **Avis Context Precision** : Le contexte récupéré contient l’ensemble des règles de composition du jury, les exigences de délai, les modalités de visioconférence, etc. Il est donc parfaitement adapté à la question posée.

### Question : quels types de financement de thèse existent ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 145.92s, Eval: 11.39s, Total: 157.31s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les mentions de la réponse (contrats doctoraux ministériels, bourses régionales, départementales, industrielles, conventions CIFRE, bourses associatives, financements ANR, Europe, Labex, contrats de recherche, contrats entreprise, financements étrangers) sont présentes dans le contexte. Le contact fourni figure également dans le contexte, donc aucune hallucination.
- **Avis Answer Relevance** : La réponse répond directement à la question en listant les différents types de financement de thèse, sans digression hors sujet.
- **Avis Context Precision** : Le contexte récupéré contient une section "Autres financements doctoraux" qui recense précisément les types de financement demandés, ce qui est suffisant pour répondre à la question.

### Question : - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autre CHRU?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 134.20s, Eval: 8.62s, Total: 142.82s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations concernant la façon de rédiger la seconde ligne de signature sont directement tirées du texte fourni (ex. « Université de Tours, … CHRU de Tours ou autre Hôpital, Service, 37XXX Tours, France »). Aucun fait externe n'est introduit, à l'exception du contact (nom, e‑mail, téléphone) qui n'est pas présent dans le contexte mais, selon les règles, les contacts injectés ne sont pas pénalisés pour la fidélité.
- **Avis Answer Relevance** : La question porte sur l'utilisation d'échantillons provenant du CHRU de Tours ou d'un autre CHRU. La réponse fournie traite uniquement de la rédaction de la signature des auteurs et ne répond pas du tout à la problématique des échantillons, ce qui la rend hors sujet.
- **Avis Context Precision** : Le contexte récupéré traite de la rédaction des affiliations et signatures pour le personnel hospitalo‑universitaire du CHRU de Tours. Il ne contient aucune information relative à la collecte, l'utilisation ou la gestion d'échantillons provenant du CHRU, ce qui était l'objet de la question. Le contexte est donc seulement vaguement lié au sujet demandé.

### Question : Je souhaite monter un projet, comment faire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 140.83s, Eval: 14.66s, Total: 155.49s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte fourni. Les étapes (contacter le SCRIPT, transmettre la saisine, assurer le pilotage, recruter un chef de projet, composition du dossier) sont décrites textuellement dans le contexte. Le nom, l'e‑mail et le téléphone de Justine Gillet ne figurent pas dans le contexte, mais la règle d’exemption des contacts les exclut de la pénalisation.
- **Avis Answer Relevance** : La question demande comment monter un projet. La réponse donne les actions concrètes à entreprendre (contact du service SCRIPT, exigences de pilotage, recrutement, pièces du dossier) et fournit un point de contact, répondant ainsi pleinement à la demande.
- **Avis Context Precision** : Le contexte récupéré contient l’ensemble des informations nécessaires : procédure de saisine, rôle du SCRIPT, exigences de coordination, liste des pièces du dossier, etc. Il est donc parfaitement ciblé.

### Question : - Comment protéger un savoir-faire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 147.88s, Eval: 15.94s, Total: 163.82s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement tirées du contexte : la nécessité d’un accord de confidentialité, la mention de la charte ou de la convention de collaborateur bénévole, et la référence à l’article L.533‑4 du CPI. Aucun élément n’est inventé ; le contact fourni est exempté selon la règle des contacts injectés.
- **Avis Answer Relevance** : La réponse répond à la question en proposant des mesures concrètes (accords de confidentialité, conventions) pour protéger un savoir‑faire. L’ajout de l’article L.533‑4, qui traite de la libre réutilisation des données, est légèrement hors‑sujet mais n’empêche pas la pertinence globale.
- **Avis Context Precision** : Le contexte récupéré contient les informations nécessaires : exigences de confidentialité, conventions pour les bénévoles, et l’article L.533‑4. Il est donc parfaitement adapté à la question.

### Question : Je pars en mission, quelle pièce dois-je remplir ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 131.38s, Eval: 8.75s, Total: 140.13s
- **Tokens générés** : 0
- **Avis Faithfulness** : Le cœur de la réponse (« convention de collaborateur bénévole ») se trouve bien dans le contexte. En revanche, la mention du téléchargement sur le site de l'Université de Tours, le contact de Morgane Guibert et l'exigence de 15 jours avant le départ ne sont pas présents dans le texte fourni. Ces éléments sont donc des hallucinations, ce qui empêche d'attribuer la note maximale.
- **Avis Answer Relevance** : La réponse indique clairement la pièce à remplir, ce qui répond directement à la question. Les informations additionnelles (site, contact) ne nuisent pas à la pertinence mais sont superflues.
- **Avis Context Precision** : Le contexte contient explicitement la notion de « convention de collaborateur bénévole », suffisante pour répondre à la question. Aucun autre document n'est requis dans le texte.

### Question : Quel est le délai moyen entre la soumission d’un manuscrit et sa publication ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 3.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 134.96s, Eval: 8.77s, Total: 143.73s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : le texte indique qu'aucun délai moyen n'est mentionné et précise les délais de 6 mois (sciences, technique, médecine) et 12 mois (sciences humaines et sociales) pour la mise à disposition du manuscrit. Le contact fourni n'est pas présent dans le contexte mais, selon les règles, les contacts injectés ne sont pas pénalisés.
- **Avis Answer Relevance** : La réponse indique que le délai moyen demandé n'est pas présent dans le contexte et fournit un délai légal lié à la mise à disposition du manuscrit, ce qui n'est pas exactement la même information que le délai moyen entre soumission et publication. Elle répond partiellement à la question mais ne fournit pas la donnée recherchée.
- **Avis Context Precision** : Le contexte ne contient pas d'information sur le délai moyen entre soumission et publication ; il ne fournit que le délai maximal de mise à disposition du manuscrit (6 ou 12 mois). Ainsi le contexte est seulement vaguement lié à la question.

## 06_google_mono

### Question : C’est quoi les SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 90.85s, Eval: 10.73s, Total: 101.58s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse se retrouvent textuellement dans le contexte : les SAPS sont définies comme « Sciences Avec et Pour la Société », leur objectif est de renforcer les relations entre science et société en rapprochant chercheurs et citoyens, et le Pôle SAPS accompagne les chercheurs dans la médiation scientifique et organise des événements. L’adresse e‑mail figure également dans la section CONTACTS du contexte, ce qui n’est pas pénalisé.
- **Avis Answer Relevance** : La réponse répond directement à la question « C’est quoi les SAPS ? » en donnant une définition claire et en précisant le rôle du Pôle SAPS, ce qui correspond exactement à ce qui était demandé.
- **Avis Context Precision** : Le contexte fourni contient la définition, les objectifs et les missions du Pôle SAPS, toutes exploitées par la réponse. Aucun élément du contexte n’est hors sujet.

### Question : Comment peut-on changer le budget d’un projet ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 161.90s, Eval: 11.80s, Total: 173.70s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations factuelles de la réponse (passer par le SPIV, fournir un argumentaire scientifique, fournir un budget modifié validé par l'antenne financière, attendre le retour du financeur) sont directement présentes dans le contexte. Le seul élément de contact (Anne Galopin, af.polytech@univ-tours.fr) n'est pas dans le contexte, mais les règles d'évaluation excluent les contacts de la pénalisation de la fidélité.
- **Avis Answer Relevance** : La réponse répond précisément à la question en expliquant la procédure à suivre pour modifier le budget d’un projet, sans digression.
- **Avis Context Precision** : Le contexte contient la section « Gérer les aléas (demande d’avenant ou de modification) » qui décrit exactement la procédure mentionnée dans la réponse, donc le contexte est parfaitement pertinent.

### Question : Quelles sont les différentes démarches à effectuer ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 1.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 238.26s, Eval: 9.79s, Total: 248.05s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse se contente de reformuler le fait que le contexte mentionne plusieurs types de démarches (mobilités recherche, service SCRIPT, réinscriptions doctorales). Aucun élément n’est inventé ; toutes les affirmations sont présentes dans le texte fourni. Aucun contact ajouté n’est présent, donc aucune pénalité n’est appliquée.
- **Avis Answer Relevance** : La question demandait « Quelles sont les différentes démarches à effectuer ? » La réponse ne fournit aucune liste ou description des démarches, mais se contente de demander une précision. Elle ne répond donc pas à la question posée.
- **Avis Context Precision** : Le contexte récupéré contient en détail les différentes démarches (liste des pièces à fournir, procédure de mobilité, étapes d’instruction, etc.). Le contexte est donc parfaitement pertinent et complet pour répondre à la question.

### Question : - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire extérieur? Est-ce gratuit?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 2.0/5, Context Precision: 3.0/5
- **Temps** : RAG: 239.46s, Eval: 10.42s, Total: 249.88s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse cite le contact Hélène Jullien qui figure bien dans le contexte, et indique qu’un projet en collaboration doit être encadré contractuellement, ce qui est cohérent avec les informations du contexte. Aucun élément de contact n’est halluciné. La formulation exacte n’est pas présente dans le texte, mais il s’agit d’une reformulation acceptable, d’où la note 4.
- **Avis Answer Relevance** : La question porte sur le cadre permettant de réaliser des expérimentations avec un partenaire extérieur et sur la gratuité éventuelle. La réponse ne répond pas à ces deux points : elle se contente de recommander de contacter Hélène Jullien et de consulter la page sur les projets et contrats, sans préciser le cadre juridique ni le coût. La pertinence est donc très faible (note 2).
- **Avis Context Precision** : Le contexte contient des informations relatives aux conventions de cotutelle, aux mobilités de recherche et à la prise en charge financière (ex. « L'UT ne demandera pas de contrepartie financière à cet accueil »). Ces éléments sont pertinents pour la question, mais le texte fourni ne cible pas explicitement les « expérimentations » avec un partenaire extérieur. Le contexte est donc partiellement utile, d’où une note de 3.

### Question : A quelle adresse postale ou mail dois-je envoyer mon projet ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 3.0/5, Context Precision: 3.0/5
- **Temps** : RAG: 124.47s, Eval: 8.03s, Total: 132.50s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les informations fournies dans la réponse (l'adresse e‑mail morgane.guibert@univ-tours.fr) sont présentes dans le contexte. Aucun élément n'a été inventé.
- **Avis Answer Relevance** : La réponse propose une adresse e‑mail, ce qui répond partiellement à la question « adresse postale ou mail ». Cependant, le contexte ne précise pas que cet e‑mail est celui auquel il faut envoyer le projet, donc la pertinence est limitée.
- **Avis Context Precision** : Le contexte contient plusieurs adresses e‑mail et contacts, mais aucune indication explicite sur le destinataire du projet. Le contexte est donc partiellement utile, mais il manque la donnée précise recherchée.

### Question : Comment m’inscrire / me réinscrire ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 141.87s, Eval: 0.00s, Total: 141.87s
- **Tokens générés** : 0

### Question : Quelles ressources le Pôle SAPS peut m’apporter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 85.14s, Eval: 14.36s, Total: 99.50s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : conseils pour dépôts de projets (ANR, projets européens), aide au montage budgétaire, formations en vulgarisation et mediatraining, participation à la Fête de la science et au concours "Ma thèse en 180 secondes", projets Arts/Sciences comme "Ma thèse en BD" et l’adresse e‑mail saps@univ‑tours.fr. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond à la question en listant plusieurs ressources offertes par le Pôle SAPS. Elle est pertinente, mais ne couvre pas l’ensemble des services mentionnés dans le contexte (ex. boutique des sciences, mentorat MeFILYA, label SAPS Teepee, organisation d’événements spécifiques, etc.).
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires pour répondre à la question, incluant les missions, formations, accompagnement de projets, événements et contacts. Il est donc très précis.

### Question : Y a-t-il des alumni ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 1.0/5
- **Temps** : RAG: 140.07s, Eval: 5.12s, Total: 145.19s
- **Tokens générés** : 0
- **Avis Faithfulness** : Aucune affirmation n'est présentée dans la réponse, il n'y a donc aucune information qui pourrait être en contradiction avec le contexte fourni. Aucun élément n'est halluciné.
- **Avis Answer Relevance** : La question porte sur l'existence d'alumni. La réponse du système est vide, ne fournit aucune information et ne répond donc pas du tout à la question.
- **Avis Context Precision** : Le contexte récupéré décrit des actions liées à l'égalité hommes‑femmes, à la formation, aux procédures de lutte contre les violences, etc. Il ne contient aucune mention d'alumni, ce qui le rend non pertinent pour répondre à la question.

### Question : Que propose le Pôle SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 101.56s, Eval: 12.70s, Total: 114.26s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse se retrouvent textuellement ou de façon paraphrasée dans le contexte : le pôle facilite le dialogue, répond aux sollicitations extérieures, organise des événements (DéTours des sciences, Ma thèse en 180s), accompagne les chercheurs (médiation, formations, dépôts de dossiers) et propose des projets arts‑sciences (Ma thèse en BD, Kaléidoscope). L’adresse e‑mail figure également dans le contexte, ce qui n’est pas pénalisé.
- **Avis Answer Relevance** : La réponse répond directement à la question « Que propose le Pôle SAPS ? » en listant les principales offres et activités du pôle, sans digression.
- **Avis Context Precision** : Le contexte fourni contient l’ensemble des informations nécessaires (missions du pôle, exemples d’événements, formations, projets arts‑sciences, contacts). Il est donc parfaitement adapté.

### Question : - Qu’est-ce qu’une invention ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 209.89s, Eval: 13.75s, Total: 223.64s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse décrit l’invention comme un résultat de recherche nouveau, inventif et susceptible d’une application industrielle, ce qui correspond aux notions présentes dans le contexte (brevetabilité, nouveauté, caractère inventif). Aucun élément factuel du texte n’est contredit, à l’exception du contact ajouté qui est considéré comme une information de contact et n’est pas pénalisé selon les règles.
- **Avis Answer Relevance** : La question porte sur la définition d’une invention. La réponse fournit directement cette définition, répondant ainsi pleinement à la demande.
- **Avis Context Precision** : Le contexte récupéré contient de nombreuses références aux critères d’une invention (originalité, nouveauté, caractère inventif, brevetabilité) ainsi qu’à la procédure de dépôt. Il est donc parfaitement adapté pour répondre à la question.

### Question : - Je souhaite répondre à un Appel à projet?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 2.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 110.19s, Eval: 14.18s, Total: 124.37s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont soit directement présentes dans le contexte (ex. appel à projet pour colloque 2027, aides à la mobilité et aux congrès), soit il s'agit d'une information de contact. Selon la règle, les contacts absents du contexte ne sont pas pénalisés, donc aucune hallucination n'est relevée.
- **Avis Answer Relevance** : La réponse indique uniquement un contact à joindre, sans fournir les étapes concrètes pour répondre à l'appel à projet (téléchargement du formulaire, composition du dossier, critères d'éligibilité, délais, etc.). Elle touche au sujet mais ne répond pas réellement à la demande d'instructions, d'où une note faible.
- **Avis Context Precision** : Le contexte retrouvé contient toutes les informations nécessaires pour répondre à la question : description de l'appel à projet, modalités de dépôt, documents requis, plafonds financiers, etc. Il est donc très précis.

### Question : je suis en arrêt de travail, qui dois-je contacter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 3.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 121.63s, Eval: 12.51s, Total: 134.14s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : les deux liens vers les pages « Congés maladie des agents titulaires » et « Congés maladie des agents contractuels » existent dans le texte fourni. Aucun élément n’est inventé, la remarque sur la dépendance au statut est une inférence raisonnable et ne constitue pas une hallucination.
- **Avis Answer Relevance** : La question demande explicitement « qui dois‑je contacter ? ». La réponse indique que les contacts varient selon le statut et renvoie vers des pages, mais ne fournit pas de nom ou de service de contact direct. Elle répond partiellement en orientant l’utilisateur, mais ne répond pas pleinement à la demande.
- **Avis Context Precision** : Le contexte contient les informations nécessaires : il propose des liens précis vers les procédures de congés maladie et liste plusieurs interlocuteurs (David SAVY, Adrien LEMONNIER, etc.). Le contexte est donc très pertinent pour répondre à la question.

### Question : Combien de temps va prendre mon inscription ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 3.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 123.95s, Eval: 19.22s, Total: 143.17s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : le texte indique que le délai de traitement est rallongé pour les dossiers avec un diplôme étranger ou un DEA et que ces dossiers sont étudiés en bureau d'école doctorale. Aucun autre fait n'est ajouté. Les informations de contact, bien que légèrement différentes, ne sont pas pénalisées selon la règle d'exemption des contacts.
- **Avis Answer Relevance** : La réponse traite du temps de traitement en mentionnant un allongement pour certains dossiers, ce qui répond partiellement à la question « Combien de temps va prendre mon inscription ? ». Cependant, elle ne fournit pas de durée précise ni d’estimation générale, ce qui limite sa pertinence.
- **Avis Context Precision** : Le contexte récupéré contient l'information sur le rallongement du délai pour les diplômes étrangers/DEA ainsi que les coordonnées de contact. Ces éléments sont exactement ceux exploités dans la réponse, montrant que le contexte était adéquat.

### Question : Comment avoir un email ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 115.69s, Eval: 0.00s, Total: 115.69s
- **Tokens générés** : 0

### Question : - Je souhaite me procurer le formulaire de déclaration d’invention de l’université, à qui dois-je m’adresser ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 125.83s, Eval: 11.15s, Total: 136.98s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les informations fournies par la réponse (s'adresser au Pôle Juridique Recherche et l'adresse e‑mail drv-pi@univ-tours.fr) sont présentes dans le contexte. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La question demande à qui s’adresser pour obtenir le formulaire de déclaration d’invention. La réponse indique clairement le service concerné (PJR) et l’adresse e‑mail à utiliser, répondant ainsi directement à la demande.
- **Avis Context Precision** : Le contexte contient les coordonnées génériques pour les questions de propriété intellectuelle (drv-pi@univ-tours.fr) ainsi que la mention que le PJR pilote les déclarations d’invention. Ces informations sont exactement celles utilisées dans la réponse.

### Question : Qui contacter pour toute demande d'ouvrages en service presse ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 3.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 128.55s, Eval: 10.72s, Total: 139.27s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse indique simplement qu'aucune information n'est disponible dans le contexte. Cette affirmation est exacte, car le texte fourni ne mentionne aucun contact lié aux "demandes d'ouvrages en service presse". Aucun élément inventé n'est présent.
- **Avis Answer Relevance** : La réponse répond à la question en déclarant l'absence d'information, ce qui est pertinent mais ne fournit pas le contact recherché. Elle ne satisfait pas pleinement la demande de fournir un interlocuteur, d'où une note moyenne.
- **Avis Context Precision** : Le contexte récupéré ne contient aucune information concernant un service presse ou un contact pour les ouvrages en service presse. Il porte sur la protection du potentiel scientifique, des services juridiques, etc., donc il est seulement vaguement lié au sujet général de contacts institutionnels.

### Question : comment enregistrer ma demande de formation hors-catalogue et quels documents dois-je fournir ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 139.38s, Eval: 15.69s, Total: 155.07s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (connexion à ADUM, rubrique "formations", sélection de "déclaration des formations hors-catalogue", obligation de joindre la fiche de demande de validation des crédits doctoraux et les justificatifs) sont directement présentes dans le contexte. Le contact ajouté (Lucie PRIMAULT) n'est pas présent dans le contexte, mais la consigne indique de ne pas pénaliser les informations de contact, donc la note reste 5.
- **Avis Answer Relevance** : La réponse répond exactement à la question en expliquant comment enregistrer la demande hors-catalogue et quels documents fournir. Aucun élément hors sujet n'est introduit.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires pour répondre à la question (procédure ADUM, documents requis). Le système a correctement exploité ces informations.

### Question : Mon jury de thèse est-il valide ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 3.0/5, Context Precision: 3.0/5
- **Temps** : RAG: 227.31s, Eval: 14.10s, Total: 241.41s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (taille du jury, répartition des professeurs, présence d'un HDR, besoin de contacter un interlocuteur) sont soit présentes dans le contexte, soit correspondent à des contacts qui, selon les règles, ne sont pas pénalisés. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse fournit des informations générales sur ce qui rend un jury valide, mais elle ne répond pas directement à la question « Mon jury est‑il valide ? » qui demande une évaluation du jury spécifique de l'utilisateur. Elle reste donc partiellement pertinente.
- **Avis Context Precision** : Le contexte contient les règles de composition du jury (nombre de membres, répartition, HDR, etc.), ce qui est pertinent pour la question. Cependant, il ne fournit pas les données concrètes du jury de l'utilisateur, ce qui limite la capacité à répondre précisément.

### Question : quels types de financement de thèse existent ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 128.69s, Eval: 11.58s, Total: 140.27s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les catégories mentionnées dans la réponse (contrats doctoraux Ministère/Établissement/régionaux, bourses régionales/départementales/industrielles/associatives/étrangères, financements ANR/Europe/Labex, conventions CIFRE/DGA/ADEME, contrats de recherche ou d'entreprise, statut de doctorant salarié) sont explicitement présentes dans le contexte. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond directement à la question en listant les différents types de financement de thèse, sans digression ni information hors sujet.
- **Avis Context Precision** : Le contexte fourni contient une section "Autres financements doctoraux" qui recense précisément les mêmes catégories que la réponse, ainsi que des précisions supplémentaires sur les contrats doctoraux et les bourses. Le contexte était donc parfaitement adapté.

### Question : - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autre CHRU?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 3.0/5, Context Precision: 4.0/5
- **Temps** : RAG: 128.02s, Eval: 16.17s, Total: 144.19s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations factuelles de la réponse (nécessité du Dossier CODECOH pour la manipulation d'échantillons humains) sont présentes dans le contexte. Les coordonnées de contact ajoutées ne sont pas présentes dans le contexte, mais la consigne indique de ne pas pénaliser les informations de contact pour la fidélité.
- **Avis Answer Relevance** : La réponse traite du besoin d'un dossier réglementaire, ce qui est partiellement lié à la question sur l'utilisation d'échantillons du CHRU, mais ne répond pas explicitement à la question concernant la provenance des échantillons (CHRU de Tours ou autre CHRU).
- **Avis Context Precision** : Le contexte contient les informations nécessaires sur le Dossier CODECOH et les procédures liées aux échantillons biologiques humains, ce qui permet de répondre à la partie réglementaire de la question. Cependant, il ne fournit pas de réponse directe sur la provenance des échantillons, ce qui rend le contexte légèrement incomplet pour la question précise.

### Question : Je souhaite monter un projet, comment faire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 132.66s, Eval: 15.36s, Total: 148.02s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (nécessité de saisir le service SCRIPT en amont, rôle d’accompagnement administratif, juridique et financier) sont directement présentes dans le contexte. Les coordonnées fournies (nom, e‑mail, téléphone) ne figurent pas dans le contexte mais, conformément à la règle, elles ne sont pas pénalisées.
- **Avis Answer Relevance** : La réponse répond à la question « comment monter un projet ? » en indiquant l’étape clé à réaliser (contacter le service SCRIPT). Elle ne couvre pas l’ensemble du processus, mais reste pertinente et utile.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires pour répondre à la question : il décrit le rôle du service SCRIPT, l’obligation de le contacter en amont, et le cadre de montage du projet. Le contexte est donc très précis.

### Question : - Comment protéger un savoir-faire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 2.0/5, Context Precision: 4.0/5
- **Temps** : RAG: 120.83s, Eval: 7.92s, Total: 128.75s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les informations fournies dans la réponse (l'adresse e‑mail drv-pi@univ-tours.fr) sont présentes dans le contexte. Aucun élément n'est inventé, y compris les contacts qui sont explicitement listés dans le texte.
- **Avis Answer Relevance** : La question demande des moyens concrets pour protéger un savoir‑faire. La réponse se contente de rediriger l'utilisateur vers un service de contact, sans fournir de méthode ou d'explication. Elle ne répond donc pas directement à la demande.
- **Avis Context Precision** : Le contexte contient plusieurs informations pertinentes sur la protection du savoir‑faire (accords de confidentialité, conventions de collaborateur bénévole, procédures de propriété intellectuelle, etc.). Il est donc pertinent, même s'il ne fournit pas une réponse prête à l'emploi.

### Question : Je pars en mission, quelle pièce dois-je remplir ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 213.23s, Eval: 9.73s, Total: 222.96s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte. Le formulaire « AUTORISATION DE DEPLACEMENT » apparaît explicitement dans le texte fourni. Le contact (Morgane Guibert, morgane.guibert@univ-tours.fr) n'est pas présent dans le contexte, mais les règles d'évaluation précisent de ne pas pénaliser les informations de contact injectées automatiquement.
- **Avis Answer Relevance** : La question demande quelle pièce remplir pour une mission. La réponse indique précisément le formulaire à remplir, répondant ainsi directement à la demande.
- **Avis Context Precision** : Le contexte contient la section « AUTORISATION DE DEPLACEMENT » ainsi que les instructions associées, ce qui fournit exactement l'information requise pour répondre à la question.

### Question : Quel est le délai moyen entre la soumission d’un manuscrit et sa publication ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 318.91s, Eval: 8.36s, Total: 327.27s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont vérifiables : le système indique qu'il ne possède pas d'information sur le délai moyen, ce qui est exact puisque le contexte ne fournit pas de donnée chiffrée à ce sujet. Le contact ajouté n'est pas présent dans le contexte, mais la règle d'exemption des contacts empêche toute pénalisation sur la fidélité.
- **Avis Answer Relevance** : La réponse répond directement à la question en indiquant l'absence d'information, ce qui est pertinent. Elle aurait pu proposer une estimation basée sur le texte (ex. les 6/12 mois d'embargo), d'où la note légèrement inférieure à 5.
- **Avis Context Precision** : Le contexte récupéré porte sur la législation relative à l'open‑access et mentionne des délais maximums (6 mois, 12 mois) après la première publication, mais ne donne aucun délai moyen entre soumission et publication. Le contexte est donc seulement vaguement lié au sujet recherché.

## 08_economy_cross

### Question : C’est quoi les SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 86.68s, Eval: 7.78s, Total: 94.46s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse se retrouvent textuellement dans le contexte : le sigle SAPS signifie « Sciences Avec et Pour la Société », la loi de programmation de la recherche 2021 est mentionnée, ainsi que les objectifs de renforcer le dialogue, la confiance et la réciprocité entre chercheurs et citoyens, et la mise en relation via médiation et événements. Le site saps.univ-tours.fr apparaît également dans le contexte. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond directement à la question « C’est quoi les SAPS ? » en donnant une définition claire et concise du concept, sans digression.
- **Avis Context Precision** : Le contexte fourni contient la définition exacte des SAPS, leurs objectifs, le cadre législatif et le lien web. Il est donc parfaitement adapté pour répondre à la question.

### Question : Comment peut-on changer le budget d’un projet ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 173.42s, Eval: 12.05s, Total: 185.47s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : le texte indique que toute demande de modification budgétaire doit passer par le SPIV, que le SPIV exige un argumentaire scientifique et un budget modifié au formalisme du financeur, et que la demande d’avenant ne vaut pas accord tant que le financeur n’a pas donné son feu vert. Aucun élément n’est inventé. Le contact fourni n’est pas pénalisé selon la règle sur les contacts injectés.
- **Avis Answer Relevance** : La réponse répond exactement à la question « Comment peut-on changer le budget d’un projet ? » en décrivant la procédure à suivre. Aucun hors‑sujet n’est introduit.
- **Avis Context Precision** : Le contexte récupéré contient la procédure complète de modification budgétaire (section « Gérer les aléas »). Il fournit toutes les informations nécessaires pour répondre à la question.

### Question : Quelles sont les différentes démarches à effectuer ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 1.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 113.64s, Eval: 10.15s, Total: 123.79s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne s’appuie sur aucune information du contexte fourni. Elle se contente d’un marqueur « [VREQUIERT_PLUS_DE_CONTEXTE ]» qui n’apparaît pas dans le texte source, ce qui constitue une information non‑fondée. Aucun élément du contexte n’est repris, d’où une note faible.
- **Avis Answer Relevance** : La question demandait « Quelles sont les différentes démarches à effectuer ? ». La réponse indique simplement qu’il manque du contexte et ne fournit aucune démarche, donc elle ne répond pas du tout à la question.
- **Avis Context Precision** : Le contexte récupéré contient de nombreuses informations sur les démarches possibles (RGPD, formalités d’accueil, dossier à compléter, accompagnement EURAXESS, etc.). Ainsi le contexte est très pertinent et complet pour répondre à la question.

### Question : - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire extérieur? Est-ce gratuit?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 3.0/5, Context Precision: 4.0/5
- **Temps** : RAG: 131.70s, Eval: 8.49s, Total: 140.19s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : le texte indique que les collaborations avec des partenaires extérieurs doivent être encadrées par un contrat et que la propriété intellectuelle est souvent en copropriété. Le contact fourni n'est pas pénalisé selon la règle sur les contacts injectés.
- **Avis Answer Relevance** : La réponse traite du cadre (contrat) demandé, mais ne répond pas directement à la seconde partie de la question concernant la gratuité. Elle renvoie simplement à un interlocuteur pour obtenir cette information, ce qui rend la réponse partiellement pertinente.
- **Avis Context Precision** : Le contexte contient les informations nécessaires sur l’obligation d’un contrat pour les collaborations externes, ce qui est pertinent pour la première partie de la question. Cependant, il ne précise pas si ces expérimentations sont gratuites, ce qui explique l’absence de réponse claire sur ce point.

### Question : A quelle adresse postale ou mail dois-je envoyer mon projet ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 3.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 306.58s, Eval: 7.74s, Total: 314.32s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les informations fournies dans la réponse (nom de Morgane Guibert et son adresse e‑mail) sont présentes dans le contexte. Aucun élément n’a été inventé.
- **Avis Answer Relevance** : La réponse donne une adresse e‑mail, ce qui répond partiellement à la question « adresse postale ou mail ». Cependant, le contexte propose d’autres adresses (par ex. l’adresse générique drv-pi@univ‑tours.fr ou l’adresse de Jeanne Hélouis pour les conventions) qui auraient pu être plus appropriées selon le type de projet. La réponse n’est donc que partiellement pertinente.
- **Avis Context Precision** : Le contexte contient plusieurs adresses e‑mail et même une adresse postale générique du Pôle Juridique Recherche, ce qui est suffisant pour répondre à la question. Le contexte est donc très précis.

### Question : Comment m’inscrire / me réinscrire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 140.14s, Eval: 13.86s, Total: 154.00s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (connexion à ADUM entre début juin et le 15 novembre, nécessité d’une invitation du gestionnaire, dépôt du compte‑rendu du CSI et de la Convention Individuelle de Formation) sont directement présentes dans le contexte. Aucun élément n’est inventé ; la mention d’absence d’information pour l’inscription initiale reflète simplement le manque de données dans le contexte.
- **Avis Answer Relevance** : La réponse répond clairement à la question « Comment m’inscrire / me réinscrire ? » en détaillant la procédure de réinscription, qui est la partie la plus couverte par le contexte. Elle indique également qu’elle ne dispose pas d’informations pour une première inscription, ce qui reste pertinent vu l’absence de ces informations dans le contexte.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires pour expliquer la réinscription (dates, plateforme ADUM, documents à déposer, rôle du gestionnaire). Le système a donc pu extraire les bonnes données.

### Question : Quelles ressources le Pôle SAPS peut m’apporter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 89.58s, Eval: 13.71s, Total: 103.29s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : le conseil pour les projets de recherche (ANR, européens) est mentionné dans les sections « Dépôt de projets » et « Accompagnement / conseil » ; l'organisation d'événements comme DéTours des sciences et la Fête de la science apparaît dans les slides listant les événements SAPS ; les formations « Jeudis des SAPS » et la préparation au concours « Ma Thèse en 180 secondes » sont décrites dans la partie Formations. L’adresse e‑mail figure également dans la partie CONTACTS. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond à la question en indiquant les principales ressources offertes (conseil, organisation d’événements, formations) et fournit le contact. Elle est pertinente mais ne couvre pas l’ensemble des services possibles (ex. accompagnement de projets arts/sciences, label, mentorat, aide budgétaire, etc.), d’où une note légèrement inférieure.
- **Avis Context Precision** : Le contexte récupéré contient une description très détaillée des missions du Pôle SAPS, des formations, des événements, des services d’accompagnement, des projets arts/sciences, du label, etc. Il est donc pleinement adéquat pour répondre à la question.

### Question : Y a-t-il des alumni ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 1.0/5
- **Temps** : RAG: 119.19s, Eval: 5.49s, Total: 124.68s
- **Tokens générés** : 0
- **Avis Faithfulness** : Aucune affirmation n'est présentée dans la réponse, il n'y a donc aucune information qui puisse être en contradiction avec le contexte. L'absence de contenu garantit une fidélité totale.
- **Avis Answer Relevance** : La question porte sur l'existence d'alumni. La réponse ne fournit aucune information à ce sujet, ne répond donc pas du tout à la demande.
- **Avis Context Precision** : Le contexte récupéré ne contient aucune donnée relative aux alumni (il s'agit de pages sur la rémunération, les campagnes de carrière, etc.). Ainsi, le contexte n'est pas pertinent pour répondre à la question.

### Question : Que propose le Pôle SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 74.55s, Eval: 12.31s, Total: 86.86s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse se retrouvent dans le contexte : organisation d'événements (DéTours des sciences, Ma thèse en 180s), accompagnement de projets (conseil, montage budgétaire, résidences Kaléidoscope), formation (Jeudis des SAPS, médiation scientifique) et le contact saps@univ-tours.fr. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond directement à la question en indiquant ce que le Pôle SAPS propose, en présentant trois grands axes d'action. Elle reste pertinente même si elle ne couvre pas l'intégralité des missions décrites dans le contexte.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires (missions, événements, formations, accompagnement, contacts) pour répondre à la question. Il est donc parfaitement adapté.

### Question : - Qu’est-ce qu’une invention ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 2.0/5, Context Precision: 3.0/5
- **Temps** : RAG: 136.99s, Eval: 10.94s, Total: 147.93s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : le texte ne fournit effectivement aucune définition explicite d'« invention » et la réponse se contente de le signaler. Le seul élément ajouté (adresse e‑mail) est un contact et, selon les règles, n’est pas pénalisé.
- **Avis Answer Relevance** : La question demande une définition de l’invention. La réponse ne fournit pas de définition, se limitant à indiquer l’absence de celle‑ci dans le contexte et à proposer un contact. Elle ne répond donc pas réellement à la demande.
- **Avis Context Precision** : Le contexte récupéré traite largement des inventions (décrets, conditions d’application, statut des inventeurs) mais ne contient pas de définition claire. Il est donc partiellement utile, mais il manque l’information clé recherchée.

### Question : - Je souhaite répondre à un Appel à projet?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 120.10s, Eval: 7.51s, Total: 127.61s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : le Pôle administration et gestion de la recherche rattaché au service RED de la DRV, la personne Caroline Vaslin, et son rôle de gestion des calendriers et procédures des appels à projets. L'adresse e‑mail fournie n'est pas dans le contexte, mais les consignes indiquent de ne pas pénaliser les contacts ajoutés automatiquement.
- **Avis Answer Relevance** : La réponse répond exactement à la demande « Je souhaite répondre à un Appel à projet ? » en indiquant qui contacter et pourquoi, ce qui constitue une réponse ciblée et utile.
- **Avis Context Precision** : Le contexte récupéré contient toutes les informations nécessaires (pôle, service, nom et fonction de Caroline Vaslin) pour répondre à la question, il est donc parfaitement précis.

### Question : je suis en arrêt de travail, qui dois-je contacter ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 124.09s, Eval: 11.60s, Total: 135.69s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse indique que l'arrêt de travail doit être notifié au Service de médecine de prévention et au gestionnaire DRH, ce qui est présent dans le contexte. Cependant, elle ajoute la mention « comme indiqué dans le livret des encadrants » et précise que le service est « rattaché au Service Prévention Protection Santé Sécurité - PePSS », informations qui n'apparaissent pas dans le texte fourni. Ces ajouts constituent des hallucinations, d'où la note 3.
- **Avis Answer Relevance** : La question porte sur le contact à prévenir en cas d'arrêt de travail. La réponse fournit exactement les interlocuteurs pertinents (service de médecine de prévention et DRH), répondant ainsi pleinement à la demande.
- **Avis Context Precision** : Le contexte contient les deux informations nécessaires : la nécessité d’informer le service de médecine de prévention et la possibilité de contacter un gestionnaire de la DRH pour les aspects administratifs. Le contexte est donc parfaitement adapté.

### Question : Combien de temps va prendre mon inscription ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 2.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 124.71s, Eval: 6.64s, Total: 131.35s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient aucune affirmation qui ne provient pas du contexte, à l'exception d'un contact (nom et e‑mail). Selon les règles, les informations de contact absentes du contexte ne sont pas pénalisées. Aucun autre élément n'est halluciné.
- **Avis Answer Relevance** : La question porte sur la durée de l'inscription. La réponse ne fournit pas de durée, elle indique seulement de contacter une personne pour obtenir l'information. Elle touche donc le sujet mais ne répond pas réellement à la question.
- **Avis Context Precision** : Le contexte fourni décrit les documents à fournir, les formulaires et les procédures d'inscription, mais ne mentionne aucune information sur le délai de traitement. Le contexte est donc seulement vaguement lié à la question de durée.

### Question : Comment avoir un email ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 140.33s, Eval: 10.12s, Total: 150.45s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : (1) les doctorants disposent d’un compte email sur le domaine etu.univ-tours.fr, (2) l’adresse générique dsi@univ-tours.fr et le service informatique de proximité sont mentionnés, (3) la Charte du poste de travail est référencée. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La question « Comment avoir un email ? » est traitée de façon précise : on indique que le compte est attribué automatiquement aux doctorants et, le cas échéant, on indique le contact pour obtenir un compte personnel. La réponse répond exactement à la demande.
- **Avis Context Precision** : Le contexte fourni contient l’information sur l’attribution automatique d’un compte email aux doctorants, le contact du service informatique et le lien vers la charte. Il est donc parfaitement adapté à la question.

### Question : - Je souhaite me procurer le formulaire de déclaration d’invention de l’université, à qui dois-je m’adresser ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 128.73s, Eval: 10.63s, Total: 139.36s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : le Pôle Juridique Recherche (PJR) est indiqué comme responsable de l'instruction des déclarations d'invention et l'adresse générique drv-pi@univ-tours.fr est fournie pour les questions de propriété intellectuelle. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question « à qui dois‑je m’adresser ? » en indiquant le service et l’adresse e‑mail à contacter pour obtenir le formulaire de déclaration d’invention.
- **Avis Context Precision** : Le contexte contient l'information précise sur le service PJR, ses missions (instruction des déclarations d’invention) et l’adresse e‑mail générique. Cette information est pleinement exploitées.

### Question : Qui contacter pour toute demande d'ouvrages en service presse ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 1.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 141.39s, Eval: 2.94s, Total: 144.33s
- **Tokens générés** : 0
- **Avis Faithfulness** : Aucune réponse du système n'est fournie dans les données d'évaluation. Par conséquent, aucune affirmation ne peut être vérifiée par rapport au contexte, ce qui constitue une absence totale d'information et donc une très faible fidélité.
- **Avis Answer Relevance** : La question "Qui contacter pour toute demande d'ouvrages en service presse ?" n'est pas du tout traitée, car aucune réponse n'est présentée. La pertinence est donc nulle.
- **Avis Context Precision** : Le contexte récupéré porte principalement sur le RGPD, les contacts du DPO, et divers services administratifs de l'Université de Tours. Il ne contient aucune information explicite concernant un "service presse" ou les contacts associés. Le contexte est donc très peu pertinent pour la question, justifiant un score faible.

### Question : comment enregistrer ma demande de formation hors-catalogue et quels documents dois-je fournir ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 3.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 238.67s, Eval: 11.17s, Total: 249.84s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse affirme que le contexte ne précise pas les pièces justificatives, alors que le texte fourni indique clairement qu'il faut fournir une attestation de présence et le programme détaillé pour une formation hors‑catalogue. Cette affirmation est donc erronée. Le contact e‑mail ajouté n'est pas présent dans le contexte, mais les consignes d'évaluation excluent les contacts de la pénalité de fidélité.
- **Avis Answer Relevance** : La réponse indique correctement que l’enregistrement se fait via ADUM, ce qui répond partiellement à la question. Cependant, elle ne fournit pas les documents requis, ce qui limite la pertinence globale.
- **Avis Context Precision** : Le contexte contient les informations nécessaires : la rubrique ADUM pour la déclaration et la liste des pièces (attestation de présence, programme détaillé). Ainsi le contexte est très précis et complet pour répondre à la question.

### Question : Mon jury de thèse est-il valide ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 1.0/5
- **Temps** : RAG: 186.27s, Eval: 8.91s, Total: 195.18s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient aucune affirmation factuelle qui ne provient pas du contexte. Le seul élément ajouté est un contact e‑mail, mais les règles précisent de ne pas pénaliser les contacts absents du contexte. Aucun autre contenu n'est halluciné.
- **Avis Answer Relevance** : La question porte sur la validité d'un jury de thèse, alors que la réponse ne fournit qu'un contact e‑mail sans lien avec le sujet. La réponse ne répond donc pas du tout à la question.
- **Avis Context Precision** : Le contexte fourni traite de l'éméritat et de la législation associée, aucun élément n'est lié à la composition ou la validité d'un jury de thèse. Le contexte n'est donc pas pertinent pour la question.

### Question : quels types de financement de thèse existent ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 136.39s, Eval: 16.01s, Total: 152.40s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse se retrouvent textuellement ou implicitement dans le contexte fourni : contrats doctoraux du Ministère, bourses régionales, départementales, industrielles (CIFRE), associatives, financements par contrats de recherche (ANR, Europe, Labex, ERC, FUI), Bourses Rabelaisiennes, statut salarié (public/privé) et financement étranger. Aucun élément n’est inventé. Le contact ajouté n’est pas pénalisé selon la règle.
- **Avis Answer Relevance** : La réponse répond directement à la question « quels types de financement de thèse existent ? » en listant les principales catégories de financement, sans digression.
- **Avis Context Precision** : Le contexte contient une longue liste de sources de financement (ANR, Europe, Labex, contrats de recherche, CIFRE/DGA/ADEME, gouvernements/associations/établissements étrangers, salariés, bourses régionales, départementales, etc.). Il est donc très pertinent et complet pour répondre à la question.

### Question : - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autre CHRU?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 1.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 311.92s, Eval: 13.40s, Total: 325.32s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse contient une affirmation selon laquelle le système ne peut pas répondre et propose de contacter Claude‑Emmanuel Boudet. Aucun de ces éléments n'apparaît dans le contexte fourni (le contexte ne mentionne pas d'incapacité à répondre ni ce contact). Le texte est donc majoritairement hors du contexte, ce qui justifie la note minimale.
- **Avis Answer Relevance** : La question porte sur l'utilisation d'échantillons provenant du CHRU de Tours ou d'un autre CHRU. La réponse ne traite pas du tout de ce sujet et se contente de rediriger vers un contact, ce qui la rend hors sujet.
- **Avis Context Precision** : Le contexte parle de règles d'affiliation et de signatures pour le CHRU de Tours, mais ne fournit aucune information sur la gestion ou l'utilisation d'échantillons. Ainsi, le contexte est seulement vaguement lié au terme "CHRU de Tours" et ne permet pas de répondre à la question.

### Question : Je souhaite monter un projet, comment faire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 131.89s, Eval: 9.05s, Total: 140.94s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (rôle du SPIV, accompagnement du SCRIPT, existence d'un comité de pilotage) sont présentes dans le contexte. Le seul élément de contact (Justine Gillet) n'est pas dans le contexte, mais la règle indique de ne pas pénaliser les contacts ajoutés automatiquement.
- **Avis Answer Relevance** : La réponse propose une démarche concrète (contacter un interlocuteur, puis s'appuyer sur le SPIV et le SCRIPT) qui répond à la question « comment monter un projet ? ». Elle reste pertinente même si elle ne détaille pas l’ensemble du processus.
- **Avis Context Precision** : Le contexte récupéré décrit précisément le service SPIV, le rôle du SCRIPT, les étapes de montage, les interlocuteurs et les pièces à fournir. Il est donc pleinement pertinent pour répondre à la question.

### Question : - Comment protéger un savoir-faire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 120.41s, Eval: 11.03s, Total: 131.44s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse se retrouvent dans le contexte : le Pôle Juridique Recherche (PJR) est présenté, les adresses e‑mail sont présentes, et le texte évoque les possibilités de protection par brevet, secret ou convention de confidentialité. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond directement à la question « Comment protéger un savoir‑faire ? » en indiquant la démarche à suivre (contacter le PJR) et les grandes options de protection (brevet, secret, confidentialité). Elle est donc pleinement pertinente.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires : description du rôle du PJR, contacts e‑mail, mentions de la confidentialité, des conventions et du régime de propriété intellectuelle applicable. Le système a correctement exploité ces éléments.

### Question : Je pars en mission, quelle pièce dois-je remplir ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 135.01s, Eval: 6.74s, Total: 141.75s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : le besoin de remplir le « formulaire d’autorisation de déplacement », la signature par l’autorité responsable et l’envoi au FSD à l’adresse deplacement@univ-tours.fr. Le contact ajouté (Ilona Moutoussamy) n’est pas pénalisé selon la règle d’exemption des contacts injectés.
- **Avis Answer Relevance** : La question demande quelle pièce remplir pour une mission. La réponse indique précisément le formulaire requis, répondant exactement à la demande.
- **Avis Context Precision** : Le contexte fourni contient explicitement la mention du formulaire d’autorisation de déplacement ainsi que les modalités d’envoi, ce qui est suffisant pour répondre à la question.

### Question : Quel est le délai moyen entre la soumission d’un manuscrit et sa publication ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 132.97s, Eval: 6.72s, Total: 139.69s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient aucune affirmation factuelle autre que le contact fourni. Les informations de contact sont exemptées de pénalité selon les règles, donc aucune hallucination n'est détectée.
- **Avis Answer Relevance** : La question porte sur le délai moyen entre la soumission d’un manuscrit et sa publication. La réponse ne fournit aucun renseignement à ce sujet, se limitant à un contact, ce qui la rend totalement hors sujet.
- **Avis Context Precision** : Le contexte récupéré parle de délais légaux d’embargo (maximum 6 mois ou 12 mois après la première publication) et d’autres dispositions juridiques, mais il ne fournit pas le délai moyen entre soumission et publication. Le contexte est donc seulement vaguement lié au thème des délais, mais ne répond pas à la question précise.

## 10_mid_draft

### Question : C’est quoi les SAPS ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 83.89s, Eval: 0.00s, Total: 83.89s
- **Tokens générés** : 0

### Question : Comment peut-on changer le budget d’un projet ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 164.31s, Eval: 0.00s, Total: 164.31s
- **Tokens générés** : 0

### Question : Quelles sont les différentes démarches à effectuer ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 128.15s, Eval: 0.00s, Total: 128.15s
- **Tokens générés** : 0

### Question : - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire extérieur? Est-ce gratuit?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 134.95s, Eval: 0.00s, Total: 134.95s
- **Tokens générés** : 0

### Question : A quelle adresse postale ou mail dois-je envoyer mon projet ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 138.11s, Eval: 0.00s, Total: 138.11s
- **Tokens générés** : 0

### Question : Comment m’inscrire / me réinscrire ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 137.31s, Eval: 0.00s, Total: 137.31s
- **Tokens générés** : 0

### Question : Quelles ressources le Pôle SAPS peut m’apporter ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 83.95s, Eval: 0.00s, Total: 83.95s
- **Tokens générés** : 0

### Question : Y a-t-il des alumni ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 134.50s, Eval: 0.00s, Total: 134.50s
- **Tokens générés** : 0

### Question : Que propose le Pôle SAPS ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 88.42s, Eval: 0.00s, Total: 88.42s
- **Tokens générés** : 0

### Question : - Qu’est-ce qu’une invention ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 130.96s, Eval: 0.00s, Total: 130.96s
- **Tokens générés** : 0

### Question : - Je souhaite répondre à un Appel à projet?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 137.77s, Eval: 10.59s, Total: 148.36s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement tirées du contexte : le nom de Caroline Vaslin, son adresse e‑mail, et le fait qu’elle gère les appels à projets de la Commission Recherche. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La question porte sur la façon de répondre à un appel à projet. La réponse indique clairement le contact à solliciter, ce qui répond directement à la demande.
- **Avis Context Precision** : Le contexte fourni contient les informations nécessaires (rôle de Caroline Vaslin, son e‑mail, la gestion des AAP). Il est donc parfaitement ciblé.

### Question : je suis en arrêt de travail, qui dois-je contacter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 135.24s, Eval: 8.58s, Total: 143.82s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement tirées du contexte : les deux liens « Congés maladie des agents titulaires » et « Congés maladie des agents contractuels » existent dans le texte fourni. Aucun élément n’a été inventé.
- **Avis Answer Relevance** : La réponse répond à la question « qui dois‑je contacter ? » en indiquant les pages à consulter selon le statut de l’agent, ce qui constitue une réponse pertinente et exploitable.
- **Avis Context Precision** : Le contexte contient précisément les deux liens mentionnés dans la réponse, ainsi que des informations générales sur les congés maladie. Il est donc parfaitement adapté à la question.

### Question : Combien de temps va prendre mon inscription ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 4.0/5
- **Temps** : RAG: 135.27s, Eval: 12.09s, Total: 147.36s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les informations fournies dans la réponse sont des coordonnées de contact. Selon la règle, les contacts ajoutés qui ne figurent pas exactement dans le contexte ne sont pas pénalisés. Aucun autre fait n'est avancé, donc la réponse est entièrement fidèle au contexte.
- **Avis Answer Relevance** : La question porte sur la durée de l'inscription (« Combien de temps va prendre mon inscription ? »). La réponse ne donne aucune indication de durée, elle fournit seulement un contact, ce qui ne répond pas du tout à la question.
- **Avis Context Precision** : Le contexte contient plusieurs éléments relatifs aux délais (ex. date limite du 15 novembre, mention d'un délai de traitement plus long, étapes à valider). Ainsi le contexte est pertinent et fournit les informations nécessaires pour répondre à la question, même si la réponse ne les exploite pas.

### Question : Comment avoir un email ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 138.24s, Eval: 6.82s, Total: 145.06s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse se retrouvent dans le contexte : le directeur de thèse doit solliciter le service informatique de proximité pour créer le compte étudiant (etu.univ-tours.fr) qui comprend une messagerie électronique. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond directement à la question « Comment avoir un email ? » en expliquant la procédure d’obtention d’une adresse mail institutionnelle, sans digression.
- **Avis Context Precision** : Le contexte fourni contient les informations nécessaires : description du compte étudiant, rôle du directeur de thèse, lien vers le service informatique, et la présence d’une messagerie électronique. Le texte est donc parfaitement ciblé.

### Question : - Je souhaite me procurer le formulaire de déclaration d’invention de l’université, à qui dois-je m’adresser ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 140.32s, Eval: 7.31s, Total: 147.63s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les informations fournies dans la réponse (contacter le PJR via l'adresse drv-pi@univ-tours.fr) sont présentes dans le contexte. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond directement à la question en indiquant le contact approprié pour obtenir le formulaire de déclaration d’invention.
- **Avis Context Precision** : Le contexte contient l'adresse générique drv-pi@univ-tours.fr ainsi que la mention que le PJR gère les déclarations d'invention, ce qui est exactement ce dont la réponse a besoin.

### Question : Qui contacter pour toute demande d'ouvrages en service presse ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 1.0/5
- **Temps** : RAG: 315.74s, Eval: 5.55s, Total: 321.29s
- **Tokens générés** : 0
- **Avis Faithfulness** : Aucune information n'est fournie dans la réponse du système, il n'y a donc aucune affirmation qui pourrait être en contradiction avec le contexte. Aucun élément n'est halluciné.
- **Avis Answer Relevance** : La question porte sur le contact à joindre pour une demande d'ouvrages en service presse, mais la réponse est vide. Aucun renseignement n'est donné, ce qui la rend totalement hors sujet.
- **Avis Context Precision** : Le contexte récupéré ne contient aucune mention d'un service presse ni d'un contact associé. Ainsi, le contexte n'est pas pertinent pour répondre à la question.

### Question : comment enregistrer ma demande de formation hors-catalogue et quels documents dois-je fournir ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 158.23s, Eval: 10.12s, Total: 168.35s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse (déposer la demande sur l'espace ADUM, rubrique 'Déclaration des formations hors catalogue', fichier PDF unique contenant la fiche remplie et les justificatifs, exigence d'une demande complète) sont directement présentes dans le contexte. Le contact ajouté n'est pas pénalisé selon la règle d'exclusion des contacts.
- **Avis Answer Relevance** : La réponse répond exactement à la question en expliquant comment enregistrer la demande et quels documents fournir, sans digression.
- **Avis Context Precision** : Le contexte fourni contient les instructions précises nécessaires (déposer sur ADUM, rubrique spécifique, format PDF unique, inclusion de la fiche de validation et des justificatifs). Il est donc parfaitement pertinent.

### Question : Mon jury de thèse est-il valide ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)
- **Temps** : RAG: 134.99s, Eval: 0.00s, Total: 134.99s
- **Tokens générés** : 0

### Question : quels types de financement de thèse existent ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 134.35s, Eval: 13.47s, Total: 147.82s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les catégories mentionnées dans la réponse (contrats doctoraux, ANR, Europe, Labex, contrats de recherche/entreprise, CIFRE, DGA, ADEME, différentes bourses, financements étrangers, salariés, contrats de droit privé) sont explicitement présentes dans le texte fourni. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond directement à la question en listant les différents types de financement de thèse, sans digression ni hors‑sujet.
- **Avis Context Precision** : Le contexte récupéré contient une section détaillée intitulée « Autres financements doctoraux » qui recense exactement les sources citées dans la réponse, ainsi que des précisions sur les contrats doctoraux et les financements étrangers.

### Question : - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autre CHRU?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 140.46s, Eval: 9.51s, Total: 149.97s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement tirées du contexte. Le texte indique que, lorsque l'unité de recherche est sous tutelle de l'UT et du CHRU, la première ligne doit contenir l'unité et la deuxième ligne « CHRU de Tours, Service de XXX, 37XXX Tours, France ». Il précise également le cas où l'unité n'est pas sous tutelle, où l'on doit d'abord suivre la signature de l'établissement d'accueil puis ajouter « Université de Tours, 37XXX Tours, France ». Le contact ajouté n'est pas pénalisé selon la règle sur les contacts injectés.
- **Avis Answer Relevance** : La réponse répond directement à la question qui porte sur la manière de procéder avec des échantillons provenant du CHRU de Tours ou d'un autre CHRU, en donnant les règles de signature appropriées pour les deux scénarios possibles.
- **Avis Context Precision** : Le contexte fourni contient les informations nécessaires : les règles de signature pour les auteurs hospitalo‑universitaires liés au CHRU de Tours, les exemples de lignes de signature, et les distinctions selon la tutelle de l'unité. Aucun élément essentiel n'est absent.

### Question : Je souhaite monter un projet, comment faire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 2.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 95.03s, Eval: 13.17s, Total: 108.20s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont soit directement présentes dans le contexte, soit des informations de contact qui, selon les consignes, ne sont pas pénalisées même si elles n'apparaissent pas dans le contexte. Aucun élément factuel erroné n'est introduit.
- **Avis Answer Relevance** : La réponse propose un contact pour obtenir de l'aide, ce qui touche partiellement à la question « comment monter un projet », mais ne décrit aucune des étapes concrètes du montage de projet présentées dans le contexte. Elle ne répond donc pas de façon suffisante à la demande.
- **Avis Context Precision** : Le contexte fourni contient de nombreuses informations pertinentes (procédures de dépôt, documents requis, rôle du COPIL, etc.) qui permettent de répondre à la question. Le contexte est donc très précis et adéquat.

### Question : - Comment protéger un savoir-faire ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 2.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 86.65s, Eval: 10.89s, Total: 97.54s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse mentionne le Pôle Juridique Recherche (PJR) et affirme qu'il gère les questions de propriété intellectuelle, y compris le savoir‑faire. Aucun passage du contexte ne cite ce service ni ne décrit son rôle, ce qui constitue une hallucination. Le contact (adresse e‑mail) est exempté selon la règle, mais la description de ses compétences ne l'est pas.
- **Avis Answer Relevance** : La réponse propose uniquement un contact à appeler pour protéger le savoir‑faire, sans expliquer les mécanismes (accords de confidentialité, conventions, cessions de droits, brevets, etc.) évoqués dans le contexte. Elle répond partiellement à la question, mais reste très superficielle.
- **Avis Context Precision** : Le contexte fourni contient de nombreuses informations pertinentes sur la protection du savoir‑faire (confidentialité, conventions, cessions de droits, outils juridiques, mots‑clés). Il est donc très précis par rapport à la question.

### Question : Je pars en mission, quelle pièce dois-je remplir ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 151.14s, Eval: 5.70s, Total: 156.84s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse indique de remplir le « formulaire d'autorisation de déplacement » et de le transmettre au moins 15 jours avant le départ. Ces informations sont exactement présentes dans le contexte (section « AUTORISATION DE DEPLACEMENT »). Aucun élément inventé n'est ajouté, à l'exception du contact qui est exempté selon les règles.
- **Avis Answer Relevance** : La question demande quelle pièce remplir pour une mission. La réponse fournit précisément le nom du formulaire requis, répondant ainsi directement à la demande.
- **Avis Context Precision** : Le contexte récupéré contient la section détaillant le formulaire d'autorisation de déplacement, le délai de transmission et le lien vers le PDF. Il fournit donc toutes les informations nécessaires pour répondre à la question.

### Question : Quel est le délai moyen entre la soumission d’un manuscrit et sa publication ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 2.0/5
- **Temps** : RAG: 97.73s, Eval: 8.21s, Total: 105.94s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient aucune affirmation factuelle qui ne proviendrait pas du contexte. Le seul élément ajouté est un contact, qui selon les règles ne doit pas être pénalisé même s'il n'apparaît pas dans le contexte. Aucun hallucination n'est donc détectée.
- **Avis Answer Relevance** : La question porte sur le délai moyen entre la soumission d’un manuscrit et sa publication. La réponse fournie ne donne aucun renseignement à ce sujet et ne répond pas du tout à la question, se limitant à un contact. Elle est donc hors sujet.
- **Avis Context Precision** : Le contexte récupéré parle de délais légaux (6 mois ou 12 mois) relatifs à la mise à disposition gratuite d’un manuscrit après publication, mais ne fournit pas d’information sur le délai moyen entre soumission et publication. Le contexte est donc seulement vaguement lié au sujet et ne contient pas la donnée recherchée.
