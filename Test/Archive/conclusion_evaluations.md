# Bilan des Évaluations (LLM as a Judge)

## Moyennes Globales

- **Faithfulness** : 3.54 / 5
- **Answer Relevance** : 4.13 / 5
- **Context Precision** : 4.01 / 5
- *Nombre de réponses évaluées avec succès : 336*

## Résultats par Fichier

### Fichier : Query_Mix_05_mistral_stack_trials.json
- Moyenne Faithfulness : 2.96 / 5
- Moyenne Answer Relevance : 4.04 / 5
- Moyenne Context Precision : 4.17 / 5
- *Évaluations réussies : 24*

### Fichier : Query4_rag_batch_trials.json
- Moyenne Faithfulness : 4.00 / 5
- Moyenne Answer Relevance : 4.50 / 5
- Moyenne Context Precision : 4.14 / 5
- *Évaluations réussies : 14*

### Fichier : Query_rag_batch_trials.json
- Moyenne Faithfulness : 4.61 / 5
- Moyenne Answer Relevance : 4.89 / 5
- Moyenne Context Precision : 4.50 / 5
- *Évaluations réussies : 18*

### Fichier : Query6_rag_batch_trials.json
- Moyenne Faithfulness : 4.33 / 5
- Moyenne Answer Relevance : 4.83 / 5
- Moyenne Context Precision : 4.50 / 5
- *Évaluations réussies : 6*

### Fichier : Query_Mix_04_meta_stack_trials.json
- Moyenne Faithfulness : 3.14 / 5
- Moyenne Answer Relevance : 4.29 / 5
- Moyenne Context Precision : 4.07 / 5
- *Évaluations réussies : 14*

### Fichier : Query8_rag_batch_trials.json
- Moyenne Faithfulness : 2.38 / 5
- Moyenne Answer Relevance : 3.38 / 5
- Moyenne Context Precision : 3.38 / 5
- *Évaluations réussies : 8*

### Fichier : Query_Mix_02_fast_draft_trials.json
- Moyenne Faithfulness : 3.00 / 5
- Moyenne Answer Relevance : 4.14 / 5
- Moyenne Context Precision : 4.00 / 5
- *Évaluations réussies : 21*

### Fichier : Query2_rag_batch_trials.json
- Moyenne Faithfulness : 4.23 / 5
- Moyenne Answer Relevance : 4.62 / 5
- Moyenne Context Precision : 3.15 / 5
- *Évaluations réussies : 26*

### Fichier : Query_Mix_08_economy_cross_trials.json
- Moyenne Faithfulness : 2.96 / 5
- Moyenne Answer Relevance : 3.70 / 5
- Moyenne Context Precision : 4.04 / 5
- *Évaluations réussies : 23*

### Fichier : Query5_rag_batch_trials.json
- Moyenne Faithfulness : 3.56 / 5
- Moyenne Answer Relevance : 3.89 / 5
- Moyenne Context Precision : 2.89 / 5
- *Évaluations réussies : 9*

### Fichier : Query_Mix_07_qwen_mono_trials.json
- Moyenne Faithfulness : 3.38 / 5
- Moyenne Answer Relevance : 3.79 / 5
- Moyenne Context Precision : 4.25 / 5
- *Évaluations réussies : 24*

### Fichier : Query_Mix_01_baseline_trials.json
- Moyenne Faithfulness : 3.61 / 5
- Moyenne Answer Relevance : 4.30 / 5
- Moyenne Context Precision : 4.52 / 5
- *Évaluations réussies : 23*

### Fichier : Query7_rag_batch_trials.json
- Moyenne Faithfulness : 4.11 / 5
- Moyenne Answer Relevance : 4.53 / 5
- Moyenne Context Precision : 4.37 / 5
- *Évaluations réussies : 19*

### Fichier : Query_Mix_10_big_draft_trials.json
- Moyenne Faithfulness : 3.67 / 5
- Moyenne Answer Relevance : 4.29 / 5
- Moyenne Context Precision : 3.92 / 5
- *Évaluations réussies : 24*

### Fichier : Query_Mix_03_max_quality_trials.json
- Moyenne Faithfulness : 3.00 / 5
- Moyenne Answer Relevance : 3.54 / 5
- Moyenne Context Precision : 4.00 / 5
- *Évaluations réussies : 24*

### Fichier : Query_Mix_06_google_mono_trials.json
- Moyenne Faithfulness : 3.46 / 5
- Moyenne Answer Relevance : 3.71 / 5
- Moyenne Context Precision : 4.29 / 5
- *Évaluations réussies : 24*

### Fichier : Query_Mix_09_premium_cross_trials.json
- Moyenne Faithfulness : 3.54 / 5
- Moyenne Answer Relevance : 4.04 / 5
- Moyenne Context Precision : 4.25 / 5
- *Évaluations réussies : 24*

### Fichier : Query3_rag_batch_trials.json
- Moyenne Faithfulness : 4.18 / 5
- Moyenne Answer Relevance : 4.27 / 5
- Moyenne Context Precision : 2.55 / 5
- *Évaluations réussies : 11*

---
## Détails des évaluations (Notes et Commentaires du Juge)

## Query_Mix_05_mistral_stack_trials.json

### Question : C’est quoi les SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : la définition « Sciences Avec et Pour la Société », le lien avec la loi LPR 2021, le rôle du Ministère, les objectifs de renforcer la confiance et le dialogue, la reconnaissance de la médiation scientifique, les exemples d’activités (Boutique des sciences, DéTours des sciences, Finale « Ma thèse en 180 secondes ») et le contact d’Alice NUÉ. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question « C’est quoi les SAPS ? » en donnant une définition claire, les objectifs et des exemples concrets, ce qui la rend pleinement pertinente.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires pour répondre à la question : définition, cadre législatif, missions, exemples d’événements et contacts. Le système a utilisé ces éléments de façon appropriée.

### Question : Comment peut-on changer le budget d’un projet ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La majorité des étapes décrites (préparer un argumentaire scientifique, établir un budget modifié, transmettre la demande au SPIV, attendre l’accord du financeur) sont directement présentes dans le contexte. Cependant, le contact "Anne Galopin : af.polytech@univ-tours.fr" n’apparaît nulle part dans le texte fourni, ce qui constitue une hallucination.
- **Avis Answer Relevance** : La réponse répond précisément à la question « Comment peut-on changer le budget d’un projet ? » en détaillant la procédure à suivre, ce qui la rend très pertinente.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires : procédure de modification budgétaire, rôle du SPIV/SPV, nécessité d’un argumentaire scientifique, validation par l’antenne financière et attente de l’accord du financeur. Le système a correctement exploité ces éléments.

### Question : Quelles sont les différentes démarches à effectuer ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 3.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend la plupart des documents listés dans le contexte (pièce d'identité, diplôme, justificatif de financement, projet de thèse pour l'ED Humanités & Langues). Cependant, l'affirmation « les exigences sont similaires, mais sans projet de thèse spécifique » n’est pas explicitement présente dans le contexte et constitue une inférence non justifiée, ce qui diminue la fidélité.
- **Avis Answer Relevance** : La question demande les différentes démarches à effectuer. La réponse ne couvre qu’une partie du processus (inscription en doctorat) et ignore les nombreuses autres étapes décrites dans le contexte (déclaration de dépôt de thèse, validations par le directeur, le laboratoire, l’école doctorale, constitution du dossier de soutenance, formulaires de dérogation, etc.). Elle est donc partiellement pertinente.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires pour répondre à la question : il décrit les étapes de dépôt, de validation, les pièces justificatives, les exigences spécifiques selon les écoles, etc. Le contexte est donc très précis et complet.

### Question : - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire extérieur? Est-ce gratuit?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 2.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse indique que les expérimentations avec un partenaire extérieur relèvent du « LIFAT » et propose de contacter Justine Gillet. Aucun de ces éléments n’apparaît dans le contexte fourni : la question est associée à Hélène Jullien (secteur Santé) et le contexte ne mentionne pas LIFAT ni Justine Gillet comme interlocuteur pour ce sujet. Ainsi la plupart des affirmations sont hallucinations.
- **Avis Answer Relevance** : La réponse ne répond pas réellement à la question posée : elle ne décrit pas le cadre juridique (convention d’accueil, contrat, etc.) et ne précise pas si l’activité est gratuite. Elle fournit seulement un contact erroné, ce qui ne satisfait que partiellement la demande.
- **Avis Context Precision** : Le contexte contient la question exacte ainsi que les coordonnées d’Hélène Jullien et des informations sur la nécessité d’une convention d’accueil de collaborateur bénévole et l’encadrement contractuel des collaborations. Le contexte est donc très pertinent pour répondre à la question.

### Question : A quelle adresse postale ou mail dois-je envoyer mon projet ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 4.0/5, Context Precision: 4.0/5
- **Avis Faithfulness** : La réponse cite deux adresses e‑mail (aurelie.petereau@univ-tours.fr et projets-etablissement@univ-tours.fr) qui figurent bien dans le contexte. Le lien fourni vers la page "Suivi d'un projet/contrat de recherche" n’apparaît pas dans le texte source (c’est une URL localhost), ce qui constitue une hallucination. Le reste du contenu (type de projet, consignes) est cohérent avec le contexte, mais aucune information n’est inventée au‑delà de ce lien.
- **Avis Answer Relevance** : La réponse répond à la question en proposant des adresses e‑mail où envoyer le projet, en précisant que le choix dépend du type de projet. Elle ne donne pas une adresse postale unique, mais fournit des options pertinentes, ce qui reste largement pertinent pour la demande.
- **Avis Context Precision** : Le contexte contient plusieurs adresses e‑mail utiles (spiv@univ-tours.fr, fsd@univ-tours.fr, aurelie.petereau@univ-tours.fr, projets-etablissement@univ-tours.fr). Le système a exploité deux de ces adresses et a fait référence à la page de suivi de projet, donc le contexte était globalement pertinent, même s’il n’a pas utilisé toutes les adresses disponibles.

### Question : Comment m’inscrire / me réinscrire ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La plupart des étapes (validation par la direction de thèse, délai du 15 novembre, documents à fournir, utilisation d’ADUM) sont présentes dans le contexte. Cependant la réponse introduit des informations qui n’apparaissent pas dans le texte fourni : le nom « Christèle Gaudron‑Bredif », l’adresse e‑mail « gaudron@univ‑tours.fr » (le contexte donne « christele.gaudron@univ‑tours.fr »), ainsi qu’un lien explicite vers un tutoriel ADUM. Ces ajouts constituent des hallucinations, d’où la note 3.
- **Avis Answer Relevance** : La question porte sur les modalités d’inscription ou de réinscription. La réponse décrit clairement les deux procédures, les documents requis, les validations nécessaires et indique un contact, répondant ainsi parfaitement à la demande.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires (délais, pièces justificatives, validation par les différentes instances, contacts). Il a donc été exploité de façon pertinente.

### Question : Quelles ressources le Pôle SAPS peut m’apporter ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend les quatre axes de la stratégie SAPS (valorisation, formation, implication de la société civile, création de dispositifs) qui sont bien présents dans le contexte. En revanche, elle introduit des éléments qui n’apparaissent pas dans le texte fourni : la mention du laboratoire LIFAT, le nom « Anne Galopin » et l’adresse e‑mail af.polytech@univ‑tours.fr. Ces informations sont donc des hallucinations.
- **Avis Answer Relevance** : La réponse répond à la question en listant les types de ressources que le Pôle SAPS peut offrir (formation, valorisation, etc.). Malgré la présence d’informations superflues (LIFAT, contact inventé), le cœur de la réponse reste pertinent pour la demande.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires pour répondre : description de la stratégie SAPS, les missions du pôle, et un contact générique saps@univ‑tours.fr. Le système a donc pu s’appuyer sur un contexte pertinent et complet.

### Question : Y a-t-il des alumni ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse indique qu'aucune information sur les alumni n'a été trouvée, ce qui correspond au fait que le contexte ne mentionne pas d'alumni. Cependant, elle ajoute un contact (Marie Clermonte et son e‑mail) qui n'apparaît nulle part dans le contexte, constituant une hallucination.
- **Avis Answer Relevance** : La question porte sur l'existence d'alumni. La réponse répond directement en indiquant l'absence d'information et propose une démarche de suivi, ce qui est pleinement pertinent.
- **Avis Context Precision** : Le contexte fourni ne contient aucune information relative aux alumni ou à un réseau d'anciens étudiants. Ainsi, le contexte n'est pas réellement pertinent pour répondre à la question.

### Question : Que propose le Pôle SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Chaque affirmation de la réponse se retrouve textuellement ou de façon très proche dans le contexte fourni. Par exemple, l’accompagnement des chercheurs (déposés ANR, APR‑IR, projets européens, aide au montage budgétaire) est décrit dans la partie « Accompagnement / conseil » du contexte. Les formations listées (vulgarisation, médiatraining, préparation à *Ma Thèse en 180 s*, gestion des fausses informations) sont présentes dans la diapositive « Formations ». Tous les événements cités (DéTours des sciences, Finale régionale « Ma Thèse en 180 s », Village des sciences, Semaine du cerveau, Nocturnes de l’Histoire) apparaissent dans les slides correspondantes. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La question demandait « Que propose le Pôle SAPS ? ». La réponse décrit précisément les missions, les dispositifs, les formations, les événements, les projets arts‑sciences, le label et les ressources proposées, répondant ainsi de façon exhaustive à la demande.
- **Avis Context Precision** : Le contexte récupéré contient l’ensemble des informations nécessaires : missions du pôle, catalogue de formations, description des événements, projets régionaux, label SAPS, site web, etc. Aucun besoin d’information supplémentaire n’est requis.

### Question : - Qu’est-ce qu’une invention ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 5.0/5, Context Precision: 3.0/5
- **Avis Faithfulness** : La réponse cite une définition précise d’une invention (solution technique nouvelle, activité inventive, application industrielle, articles L. 611-10) qui n’apparaît pas dans le contexte fourni. Le contexte mentionne seulement des articles L. 611-7, R. 611-21 et des notions de titularité, mais pas la définition exacte. Le seul élément présent dans le contexte est l’adresse e‑mail drv-pi@univ-tours.fr, qui est correctement reprise.
- **Avis Answer Relevance** : La question porte sur la définition d’une invention. La réponse fournit directement une définition et, en plus, propose un contact utile. Elle répond donc pleinement à la demande.
- **Avis Context Precision** : Le contexte traite de la législation autour des inventions, des dispositifs de valorisation et des contacts du PJR, mais il ne contient pas la définition exacte donnée par la réponse. Le contexte est donc partiellement pertinent, mais il manque l’information recherchée.

### Question : - Je souhaite répondre à un Appel à projet?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse utilise majoritairement les contacts et le rôle du SPIV présents dans le contexte, mais elle invente le numéro de téléphone de Juliette Piquard (02 47 36 79 74) qui n’apparaît nulle part dans le contexte fourni. Cette information non‑documentée fait baisser la note de fidélité.
- **Avis Answer Relevance** : La réponse répond à la demande en proposant des interlocuteurs pour aider à répondre à un appel à projet, ce qui est pertinent. Elle fournit toutefois deux contacts différents, ce qui crée une légère confusion mais reste globalement en lien avec la question.
- **Avis Context Precision** : Le contexte contient les coordonnées de Juliette Piquard (email) et de Justine Gillet, ainsi que la description du SPIV et de son rôle dans le montage de projets. Le système a donc pu puiser les informations nécessaires.

### Question : je suis en arrêt de travail, qui dois-je contacter ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 5.0/5, Context Precision: 3.0/5
- **Avis Faithfulness** : La réponse indique de contacter la DRH, ce qui est cohérent avec le contexte qui mentionne la DRH, mais elle ajoute le nom et l'e‑mail d'Aurélie PETEREAU qui n'apparaissent nulle part dans le texte fourni. Cette information est donc une hallucination, ce qui fait baisser la note de fidélité.
- **Avis Answer Relevance** : La question porte sur le contact à joindre en cas d'arrêt de travail. La réponse fournit un interlocuteur (DRH) et un contact précis, répondant ainsi directement à la demande.
- **Avis Context Precision** : Le contexte mentionne la DRH, un organigramme et un numéro de téléphone général, mais il ne fournit pas explicitement de procédure ou de contact dédié à un arrêt de travail. Le contexte est donc partiellement pertinent, mais incomplet pour la question.

### Question : Combien de temps va prendre mon inscription ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 4.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse indique que le délai exact n'est pas précisé, ce qui correspond au contexte où aucune durée d'inscription n'est mentionnée. Le processus de transmission via ADUM et la réception d'un mail sont bien présents dans le texte. En revanche, le contact "Guillaume Fialeix : guillaume.fialeix@univ-tours.fr" n'apparaît pas dans le contexte, constituant une hallucination.
- **Avis Answer Relevance** : La réponse répond à la question en expliquant que le délai n'est pas indiqué dans les documents et en donnant des informations utiles sur le suivi du dossier, ce qui est pertinent même si la réponse ne fournit pas de durée précise.
- **Avis Context Precision** : Le contexte fourni porte sur les pièces à fournir, le déroulement administratif et les contacts, mais ne contient aucune information sur la durée de l'inscription. Ainsi le contexte est seulement vaguement lié à la question de durée.

### Question : Comment avoir un email ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement soutenues par le contexte : le compte étudiant est fourni aux doctorants, il inclut une messagerie, le directeur de thèse doit anticiper la demande auprès du service informatique lors des vagues d'achats, et le doctorant reçoit ses identifiants et son matériel à son arrivée. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond précisément à la question « Comment avoir un email ? » en expliquant le processus d'obtention d'un compte de messagerie pour un doctorant, ce qui est exactement ce qui était demandé.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires (existence du compte, rôle du service informatique, procédure d'activation, adresse générique du service). Il a donc été exploité de façon pertinente.

### Question : - Je souhaite me procurer le formulaire de déclaration d’invention de l’université, à qui dois-je m’adresser ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 2.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse indique que le formulaire doit être demandé à Justine Gillet (adresse e‑mail justine.gillet@univ‑tours.fr). Aucun élément du contexte ne mentionne ce nom, cette adresse ou ce rôle. Il s’agit donc d’une hallucination complète. Toutes les affirmations de la réponse ne sont pas traçables dans le contexte.
- **Avis Answer Relevance** : La réponse tente de répondre à la question en donnant un interlocuteur, mais l’interlocuteur fourni est erroné et n’est pas présent dans le contexte. Elle ne répond donc pas correctement à la demande.
- **Avis Context Precision** : Le contexte fournit le nom et les coordonnées de Morgane Guibert ainsi qu’une référence au formulaire (disponible sur l’intranet). Aucun contact spécifique n’est indiqué pour le formulaire, ce qui rend le contexte insuffisant pour répondre précisément à la question.

### Question : Qui contacter pour toute demande d'ouvrages en service presse ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 2.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse indique qu'il faut contacter « Jeanne Hélouis » (jeanne.helouis@univ-tours.fr). Aucun nom, adresse e‑mail ou numéro de téléphone de ce type n’apparaît dans le contexte fourni. Ainsi l’information est une hallucination complète.
- **Avis Answer Relevance** : La réponse répond à la question en proposant un contact, mais comme le contact est inventé, la réponse n’est pas réellement utile. Elle reste néanmoins centrée sur la demande, d’où un faible score.
- **Avis Context Precision** : Le contexte ne contient aucune information de contact relative aux « ouvrages en service presse ». Le tableau présent ne fournit qu’un intitulé de question sans réponse. Le contexte n’est donc pas pertinent pour fournir un contact, ce qui justifie un score bas.

### Question : comment enregistrer ma demande de formation hors-catalogue et quels documents dois-je fournir ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend presque intégralement les informations du contexte : connexion à ADUM, sélection de la rubrique, champs à renseigner et documents à joindre. Le seul élément qui n'apparaît pas dans le contexte est le lien externe « https://adum.fr » et la mention « pour plus de détails, consultez la procédure officielle », qui constitue une hallucination mineure.
- **Avis Answer Relevance** : La réponse répond exactement à la question en expliquant comment enregistrer la demande hors-catalogue et quels documents fournir, sans digression.
- **Avis Context Precision** : Le contexte fourni contient toutes les instructions nécessaires (accès ADUM, champs à remplir, documents à joindre, nécessité d'un email préalable). Le système a correctement exploité ces informations.

### Question : Mon jury de thèse est-il valide ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend la plupart des critères présents dans le contexte (nombre de membres, proportion de professeurs, extérieurs, HDR, représentation hommes/femmes, membres invités, membre émérite, indépendance). Cependant, elle introduit la mention « procédures en vigueur à l'Université de Tours » qui n’apparaît nulle part dans le contexte fourni. Cette information est donc une hallucination, ce qui empêche d’attribuer le score maximal.
- **Avis Answer Relevance** : La question porte sur la validité du jury. La réponse fournit une liste claire de critères à vérifier, ce qui répond directement à la demande de l’utilisateur. Aucun élément hors sujet n’est ajouté.
- **Avis Context Precision** : Le contexte contient toutes les règles nécessaires pour juger de la validité d’un jury (nombre de membres, répartition, HDR, président, membres invités, etc.). Le système a correctement extrait ces informations.

### Question : quels types de financement de thèse existent ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La plupart des affirmations (types de financement, montant minimum de 1 100 € nets/mois, distinction entre contrats doctoraux « Établissement »/« Collectivités » et autres financements) sont directement présentes dans le contexte. Cependant, le contact "Louis Lantier : louis.lantier@univ-tours.fr" n’apparaît nulle part dans le texte fourni, ce qui constitue une hallucination. Cette présence d’une information inventée empêche d’attribuer le score maximal.
- **Avis Answer Relevance** : La réponse répond clairement à la question en listant les différents types de financement de thèse, ce qui correspond exactement à la demande.
- **Avis Context Precision** : Le contexte récupéré contient toutes les informations nécessaires sur les catégories de financement (contrats doctoraux, ANR, Europe, Labex, CIFRE, etc.) et le montant requis, ce qui rend le contexte très précis pour la question.

### Question : - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autre CHRU?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les informations fournies (adresse e‑mail, numéro de téléphone de Claude‑Emmanuel BOUDET et le contact de Justine Gillet) figurent exactement dans le contexte. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse indique clairement que Claude‑Emmanuel BOUDET est le chargé d’affaires à contacter pour les projets avec des échantillons du CHRU, ce qui répond à la question. L’ajout du contact de Justine Gillet n’est pas demandé, ce qui diminue légèrement la pertinence.
- **Avis Context Precision** : Le contexte contient la question précise sur les échantillons du CHRU ainsi que les coordonnées de Claude‑Emmanuel BOUDET, ce qui est exactement ce dont la réponse a besoin.

### Question : Je souhaite monter un projet, comment faire ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend correctement les étapes décrites dans le contexte (contact du service SCRIPT, composition du dossier, désignation d'un coordinateur/chef de projet, validation par le COPIL). Cependant, elle introduit un interlocuteur nommé Justine Gillet avec son e‑mail et son téléphone, qui n’apparaît nulle part dans le contexte fourni. Cette information est donc une hallucination, ce qui empêche d’attribuer la note maximale.
- **Avis Answer Relevance** : La réponse répond directement à la question « Je souhaite monter un projet, comment faire ? » en donnant les étapes concrètes à suivre. Aucun élément hors sujet n’est présent.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires pour répondre à la question : procédure de montage, contacts, pièces du dossier, rôle du COPIL, etc. Le contexte est donc parfaitement pertinent.

### Question : - Comment protéger un savoir-faire ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend correctement les notions de confidentialité, d’accords de confidentialité, d’utilisation du cahier de laboratoire électronique et du rôle du SPIV, qui sont toutes présentes dans le contexte. Cependant, elle introduit deux informations qui n’apparaissent pas du tout dans le contexte : le laboratoire "LIFAT" et le contact "Justine Gillet" avec son adresse e‑mail. Ces ajouts constituent des hallucinations, ce qui fait baisser la note de fidélité.
- **Avis Answer Relevance** : La réponse répond directement à la question « Comment protéger un savoir‑faire ? » en proposant des étapes concrètes (confidentialité, NDA, cahier électronique, recours au SPIV, bonnes pratiques de sécurité). Aucun élément hors sujet n’est présent.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires pour répondre à la question : exigences de confidentialité, rôle du SPIV, utilisation du cahier de laboratoire électronique, recommandations de sécurité numérique. Le contexte est donc très précis.

### Question : Je pars en mission, quelle pièce dois-je remplir ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 2.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse mentionne « Anne Galopin » et l’adresse e‑mail af.polytech@univ‑tours.fr, qui n’apparaissent nulle part dans le contexte fourni. Aucun de ces éléments n’est traçable, ce qui constitue une hallucination majeure. De plus, la réponse ne cite aucune des pièces listées dans le contexte (accord de confidentialité, dossier scientifique, etc.).
- **Avis Answer Relevance** : La réponse tente de répondre à la question en proposant un contact, mais le contact est inventé et ne fournit pas la pièce à remplir. Elle ne répond donc pas réellement à la demande de savoir quelle pièce remplir.
- **Avis Context Precision** : Le contexte contient des informations sur les documents requis pour les projets de recherche (accord de confidentialité, dossier scientifique, email de validation du SPV, dossier complet) ainsi que des contacts universitaires. Cependant, il ne mentionne pas explicitement une « pièce » pour une mission, et la réponse ne s’appuie pas sur les documents réellement listés.

### Question : Quel est le délai moyen entre la soumission d’un manuscrit et sa publication ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 1.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse fournit un contact (Jeanne Hélouis, jeanne.helouis@univ-tours.fr) qui n'apparaît nulle part dans le contexte fourni. Aucun élément de la réponse n'est traçable dans le texte, donc la fidélité est très faible.
- **Avis Answer Relevance** : La question porte sur le délai moyen entre la soumission d’un manuscrit et sa publication. La réponse ne mentionne aucun délai, mais donne uniquement un contact, ce qui ne répond pas du tout à la question.
- **Avis Context Precision** : Le contexte contient des informations pertinentes sur les délais légaux (maximum de six mois pour les sciences, douze mois pour les sciences humaines et sociales) qui pourraient être utilisées pour répondre à la question. Le contexte est donc très précis et pertinent.

## Query4_rag_batch_trials.json

### Question : combien de crédits doctoraux dois-je valider pour être autorisé à soutenir ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)

### Question : quelles formations dois-je suivre pour être autorisées à soutenir ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 3.0/5
- **Avis Faithfulness** : La réponse s'appuie majoritairement sur le contexte fourni (exigences des ED, formations, dossier ADUM, délais). Cependant, elle mentionne un contact spécifique ('Guillaume Fialeix') qui n'est pas explicitement cité dans le contexte, bien que plausible dans un cadre universitaire. Cela justifie une note de 4 plutôt que 5.
- **Avis Answer Relevance** : La réponse est directement utile et exhaustive : elle détaille les exigences par ED, les formations, les délais administratifs et les étapes concrètes à suivre. Elle reformule clairement les attentes du contexte (ex : productions scientifiques, ADUM) en les organisant pour le doctorant.
- **Avis Context Precision** : Le contexte est partiel et désorganisé : les informations clés (comme les exigences des ED ou les formations obligatoires) sont noyées dans des extraits disparates (images, procédures administratives, RGPD). La réponse a dû synthétiser des éléments épars, ce qui limite la précision du contexte à **3**. Les détails sur les formations transversales ou les contacts manquent de clarté dans les sources.

### Question : comment faire valider ma participation à un colloque ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)

### Question : comment enregistrer ma demande de formation hors-catalogue et quels documents dois-je fournir ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5

### Question : les frais de déplacement sont-ils pris en charge pour suivre une formation ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 3.0/5
- **Avis Faithfulness** : {'score': 4, 'explanation': "La réponse s'appuie majoritairement sur le contexte fourni (ex. : référence au décret 2006-781 pour les avances sur frais de déplacement, mention des formations SST et du partage DRH/structure). Cependant, elle introduit des éléments non vérifiables dans le contexte, comme la recommandation de contacter *Anne Galopin* (non mentionnée) ou le *LIFAT* (laboratoire non cité). Ces ajouts, bien que plausibles, ne sont pas strictement sourcés."}
- **Avis Answer Relevance** : {'score': 5, 'explanation': "La réponse aborde directement la question des frais de déplacement pour les formations, en distinguant les cas (SST vs autres) et en proposant des pistes concrètes (contacts, liens utiles). Elle est claire, structurée et utile pour l'utilisateur."}
- **Avis Context Precision** : {'score': 3, 'explanation': 'Le contexte contient des informations pertinentes (ex. : liste des dépenses éligibles aux avances, mention des formations SST), mais il est **fragmenté et incomplet** : rien ne précise explicitement les règles de prise en charge des frais de déplacement *spécifiquement pour les formations* (hors cas des chercheurs invités ou collaborateurs bénévoles, non applicables ici). Les éléments clés sont dispersés (ex. : décret 2006-781 dans une liste générique, formations SST dans une autre section).'}

### Question : dois-je suivre un CSI pour me réinscrire ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse s'appuie sur le contexte fourni (obligation du CSI pour la réinscription dès la 2ᵉ année, rôle du comité, et échéances). Cependant, une légère imprécision est présente : **le nom et l'email de contact (Marie Clermonte) ne figurent pas dans le contexte**, ce qui constitue une information externe non vérifiée. Le reste est strictement fidèle (ex. : réunion obligatoire avant réinscription, composition du CSI).
- **Avis Answer Relevance** : La réponse est **directement pertinente** : elle confirme l'obligation du CSI pour la réinscription (question posée), explique son rôle, et mentionne les étapes clés (réunion annuelle, transmission du rapport). L'ajout d'un contact administratif, bien que non sourcé, renforce l'utilité pratique pour l'usager.
- **Avis Context Precision** : Le contexte contient **toutes les informations nécessaires** pour répondre : obligation du CSI pour la réinscription (cf. section *Réunions du CSI*), son rôle (détection de conflits, validation par l'ED), et les échéances (réunion avant chaque réinscription dès la 2ᵉ année). Les détails sur la composition du comité et les étapes de réunion (*présentation des travaux, entretien sans le directeur, etc.*) sont également présents.

### Question : je rencontre une difficulté avec mon directeur de thèse, qui puis-je contacter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 4.0/5

### Question : je souhaite mettre en place une convention de cotutelle, qui dois-je contacter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Reasoning global** : [{'criterion': 'faithfulness', 'explanation': "La réponse s'appuie strictement sur le contexte fourni (ex. : contact de Lucie PRIMAULT, étapes 1 à 4, délais, et lien vers le règlement des écoles doctorales). Aucune information externe ou hallucinée n'est ajoutée. Les détails comme l'email, le numéro de téléphone, et les ressources sont extraits fidèlement du texte source."}, {'criterion': 'answer_relevance', 'explanation': "La réponse adresse **directement** la question ('qui contacter ?') en priorisant le contact clé (Lucie PRIMAULT) et en résumant la procédure en 2 étapes claires. Les éléments complémentaires (délais, ressources) sont pertinents pour guider l'utilisateur sans surcharge. L'ajout du Pôle Juridique est un bonus utile mais mineure, justifié par le contexte (négociation DAJP mentionnée)."}, {'criterion': 'context_precision', 'explanation': "Le contexte fourni contient **toutes les informations nécessaires** pour répondre : nom/coordonnées du contact (Etape 1), procédure détaillée (Etapes 1-4), délais (18 mois), et lien vers le règlement. Les images et sections juridiques (Art. 21-23) confirment la validité des éléments cités. Aucune lacune n'empêche une réponse complète."}]

### Question : quelle est la différence entre une cotutelle et une codirection ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5

### Question : je souhaite mettre en place une convention de codirection, qui dois-je contacter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 4.0/5

### Question : quels financements nécessitent une audition par l’école doctorale ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 4.0/5

### Question : je souhaite faire une mission d’enseignement, quelle est la procédure ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 2.0/5, Context Precision: 3.0/5
- **Reasoning global** : [{'faithfulness': "La réponse mentionne un contact ('Marie Clermonte') et des détails procéduraux (autorisations, documents) **absents du contexte fourni**. Cela relève d'une **hallucination** (informations non sourcées). Le contexte évoque uniquement des procédures pour missions *générales* (recherche, colloques, déplacements), mais **rien sur l'enseignement spécifique** ou ce contact."}, {'answer_relevance': "La réponse aborde *partiellement* la question (procédure pour une mission), mais **ne cite aucune source valide** du contexte (ex : formulaire 'autorisation de déplacement', règles pour zones à risque, ou lien vers les démarches en ligne). Les conseils donnés (préciser nature/destination/durée) sont génériques et **peuvent s'appliquer à n'importe quel type de mission**, sans valeur ajoutée spécifique à l'enseignement."}, {'context_precision': "Le contexte contient des **éléments utiles mais dispersés** : procédures pour missions à l'étranger (formulaire AD, ARIANE, FSD), exclusions (colloques, co-rédaction), et liens vers des démarches en ligne. Cependant, **rien ne concerne explicitement les missions d'enseignement**, ni ne détaille une procédure dédiée. Le contexte est **insuffisant pour une réponse précise** sur ce cas spécifique."}]

### Question : je suis en arrêt de travail, qui dois-je contacter ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 3.0/5, Context Precision: 4.0/5

### Question : peut-on cumuler un contrat doctoral avec un autre contrat ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 3.0/5, Context Precision: 4.0/5

### Question : quel est le statut d’un doctorant ?
- **Erreur d'évaluation** : HTTPSConnectionPool(host='llm.ilaas.fr', port=443): Read timed out. (read timeout=30)

### Question : quels types de financement de thèse existent ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Reasoning global** : La réponse est **strictement fidèle** au contexte fourni, sans ajout d'informations externes (faithfulness: 5). Elle **répond précisément** à la question en listant exhaustivement les types de financement (contrats doctoraux, CIFRE, ANR, Europe, etc.) et leurs spécificités (answer_relevance: 5). Enfin, le contexte contenait **toutes les informations nécessaires** pour produire cette réponse, avec des détails sur les montants, procédures et acteurs impliqués (context_precision: 5).

### Question : comment s’inscrire aux formations ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 4.0/5
- **Reasoning global** : {'faithfulness': "La réponse s'appuie strictement sur le contexte fourni (ex. : ADUM, formations obligatoires, crédits doctoraux, désistement, etc.), sans ajouter d'informations externes non vérifiables. Les détails comme les 5 formations max/année, les 50 crédits requis, ou les règles de désistement sont directement extraits du contexte.", 'answer_relevance': "La réponse adresse **précisément** la question posée ('comment s’inscrire aux formations') en structurant les étapes clés (candidature → obligations → validation → crédits). Elle inclut même des exemples concrets (motivation type) et des liens utiles (catalogue du Collège Doctoral).", 'context_precision': "Le contexte contenait **la majorité** des informations nécessaires (ex. : processus ADUM, crédits, formations obligatoires), mais certaines précisions (comme l'URL exacte du catalogue ou des détails sur les écoles doctorales spécifiques) auraient pu être plus explicites. D'où un 4/5."}

## Query_rag_batch_trials.json

### Question : Je souhaite faire une demande d’aide à la mobilité. Quelles sont les pièces justificatives à transmettre ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 2.0/5
- **Reasoning global** : {'faithfulness': "La réponse reste fidèle au contexte en ne mentionnant que les informations présentes (contacts, absence de détails sur les pièces justificatives) et en évitant d'inventer des éléments. Cependant, l'ajout de l'adresse *af.polytech@univ-tours.fr* (Anne Galopin) **n'est pas présente dans le contexte fourni**, ce qui justifie un 4/5 plutôt que 5/5.", 'answer_relevance': "La réponse est parfaitement pertinente : elle oriente clairement vers les interlocuteurs compétents (École Doctorale et contacts par discipline) et explique l'absence d'informations précises dans le contexte. Elle propose une solution concrète (contacter les références fournies).", 'context_precision': 'Le contexte **ne contient aucune information explicite sur les pièces justificatives** pour une demande d’aide à la mobilité. Il liste seulement des dispositifs (ED, Erasmus, etc.) et des contacts, sans détail administratif. D’où un 2/5 pour ce critère.'}

### Question : Quand recevrai-je mon diplôme ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 3.0/5
- **Avis Faithfulness** : {'score': 4, 'explanation': "La réponse s'appuie sur le contexte fourni (délai de 15 jours pour les documents post-soutenance, rôle d'ADUM, mention de l'Université de Tours). Cependant, **le nom et l'email du contact (M. Guillaume Fialeix)** ne figurent pas dans le contexte partagé (images et texte extraits). Cela relève d'une **inférence plausible** (basée sur des connaissances externes ou une source non affichée), mais non strictement *faithful* au contexte donné. D'où un 4/5 plutôt que 5/5."}
- **Avis Answer Relevance** : {'score': 5, 'explanation': 'La réponse est **directement utile** : elle explique les étapes post-soutenance, mentionne le délai administratif (15 jours), et oriente vers un contact pour obtenir le délai exact du diplôme physique. Elle couvre à la fois le processus immédiat (documents) et la question sous-jacente (réception du diplôme).'}
- **Avis Context Precision** : {'score': 3, 'explanation': "Le contexte contient des informations **partielles** sur la procédure de soutenance (étapes 1 à 9, délai de 15 jours pour les documents), mais **rien sur** : (1) le délai de fabrication/envoi du diplôme physique, (2) les coordonnées de M. Fialeix, (3) les modalités de retrait/envoi. Ces éléments clés pour répondre précisément à la question manquent, d'où un 3/5. Le contexte permet une réponse *partielle* (étapes administratives), mais pas *complète* (diplôme physique)."}

### Question : Quel est le calendrier des inscriptions pour l’année universitaire 2025/2026 ?
- **Erreur d'évaluation** : Expecting ',' delimiter: line 9 column 16 (char 638)

### Question : Quels sont les délais à respecter pour ma soutenance ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5

### Question : Qui se charge de créer le lien visioconférence pour ma soutenance ? Quand l’aurai-je ?
- **Erreur d'évaluation** : Expecting ',' delimiter: line 9 column 24 (char 580)

### Question : Puis-je faire une césure ? Si oui, comment ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Reasoning global** : La réponse est **strictement fidèle** au contexte fourni : elle cite textuellement les conditions (durée, non-renouvellement, exclusion du travail de thèse) et la procédure (demande motivée, avis du directeur de thèse/ED, décision du chef d'établissement) sans ajouter d'informations externes. Elle est **pertinente** car elle répond précisément à la question sur la possibilité et les modalités d'une césure, en synthétisant clairement les éléments clés du contexte. Enfin, le contexte **contenait bien toutes les informations nécessaires** (article 14 de l'arrêté de 2022, règles de l'ED, procédure administrative), confirmant une précision contextuelle maximale.

### Question : Pourquoi mon compte universitaire / ma carte étudiant a-t-elle été désactivée ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 4.0/5
- **Reasoning global** : <<Faithfulness>> : La réponse s'appuie strictement sur le contexte fourni (ex. : validité annuelle du compte, réinscription via ADUM, blocage en cas de non-réinscription, contacts DSI/DRV-RED). Aucune information externe ou hallucinée n'est introduite, et les détails techniques (dates, services comme UTBox/Office365) sont extraits du contexte ou des sections connexes (ex. *Nouvel arrivant doctorant* et *Charte du poste de travail*). La mention des 'ressources rendues indisponibles' et du 'blocage à distance' est directement issue du contexte (paragraphe sur les services numériques et la sécurité informatique).

<<Answer Relevance>> : La réponse aborde **directement** la cause probable (défaut de réinscription) et propose des **actions concrètes et hiérarchisées** (vérification ADUM → contact DSI/DRV-RED → déclaration en cas de perte). Elle couvre aussi des cas secondaires (ex. : vol/perte de carte) mentionnés dans le contexte, tout en restant centrée sur la question initiale. Les liens vers les services utiles (ADUM, FAQ doctorale) sont pertinents et extraits du contexte.

<<Context Precision>> : Le contexte contient **l'essentiel** des informations pour répondre (ex. : durée de validité du compte, processus de réinscription, contacts DSI), mais manque de détails **explicites** sur les motifs précis de désactivation (ex. : retard de paiement, suspension administrative, etc.), ce qui limite la précision de la réponse sur les causes alternatives. La note 4 reflète cette légère imprécision, bien que les éléments clés soient présents pour une réponse globale satisfaisante.

### Question : Mon doctorant peut-il demander le prêt d’un ordinateur à l’Université ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5

### Question : Quel est le processus de validation de mes démarches sur ADUM pour mon inscription / réinscription / soutenance ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 4.0/5

### Question : Combien de temps va prendre mon inscription ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 4.0/5

### Question : Pourquoi mon manuscrit de thèse n’apparaît pas encore sur theses.fr ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 4.0/5

### Question : Comment trouver un directeur de thèse ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Reasoning global** : "Faithfulness" = 5 : La réponse s'appuie strictement sur le contexte fourni (procédure exacte, contacts, documents requis) sans ajouter d'éléments externes ou hallucinés. "Answer Relevance" = 5 : La réponse est claire, structurée et adresse directement la question en détaillant les étapes concrètes pour trouver un directeur de thèse, spécifiques aux SHS et à l'Université de Tours. "Context Precision" = 5 : Le contexte contenait toutes les informations nécessaires (procédure administrative, emails de contact, exigences documentaires), bien organisées et exploitables pour une réponse complète.

### Question : Mon jury de thèse est-il valide ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5

### Question : Comment déclarer ma soutenance ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5

### Question : Comment m’inscrire / me réinscrire ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5

### Question : Comment trouver un financement pour ma thèse ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)

### Question : Quels sont les critères de sélection d’un jury ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5

### Question : Qui envoie mon manuscrit de thèse aux rapporteurs et au jury ? Quand ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5

### Question : Pourquoi l’accès à ma réinscription à distance est-il bloqué ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5

### Question : Qui doit renseigner les membres de mon CSI sur ADUM ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 3.0/5, Context Precision: 5.0/5

### Question : Comment obtenir le label européen ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5

## Query6_rag_batch_trials.json

### Question : C’est quoi les SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5

### Question : Quels dispositifs SAPS existent pour les doctorants ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)

### Question : À qui adresser une demande pour monter un projet de médiation ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 4.0/5, Context Precision: 3.0/5

### Question : Quels événements sont proposés par le Pôle SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Reasoning global** : {'faithfulness': "La réponse s'appuie strictement sur le contexte fourni (slides 5, 6, 8, 9, 10, 11, 13) sans ajouter d'informations externes ou non vérifiables. Les événements cités (DéTours des sciences, MT180, Festival (Re)Cherche et trouve, etc.) et les détails (dates, liens, formats) correspondent exactement aux données du contexte.", 'answer_relevance': "La réponse couvre de manière exhaustive et organisée la question posée ('Quels événements sont proposés par le Pôle SAPS ?'). Elle distingue clairement les événements récurrents, exceptionnels et projets arts/sciences, tout en incluant des liens utiles et des contacts pertinents.", 'context_precision': "Le contexte fourni contient toutes les informations nécessaires pour répondre précisément : noms des événements (slides 5, 8, 11), dates (slide 8 : '25 avril 2025', slide 11 : '5-6-7 juin 2026'), formats (slide 10 : 'Ma thèse en BD', slide 9 : 'Fête de la science'), et détails pratiques (liens, contacts en slide 25). Aucune information manquante n’est nécessaire pour une réponse complète."}

### Question : Où puis-je trouver les appels à projets en cours ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5

### Question : C’est quoi TEEPEE ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5

### Question : Existe-t-il une boutique des sciences à l’Université ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 4.0/5

## Query_Mix_04_meta_stack_trials.json

### Question : C’est quoi les SAPS ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend correctement la définition « Sciences Avec et Pour la Société », les objectifs de la stratégie (inciter, former, impliquer, inspirer) et les contacts saps@univ‑tours.fr et juliette.piquard@univ‑tours.fr qui figurent dans le contexte. Cependant, elle introduit un contact qui n’apparaît pas dans le contexte (Anne Galopin : af.polytech@univ‑tours.fr), ce qui constitue une hallucination.
- **Avis Answer Relevance** : La réponse répond directement à la question « C’est quoi les SAPS ? » en donnant la signification et en décrivant la stratégie associée. Les informations supplémentaires (contacts, site web) restent pertinentes au sujet.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires pour répondre à la question : définition, objectifs, structure du pôle, contacts. Le système a pu extraire ces éléments.

### Question : Comment peut-on changer le budget d’un projet ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend les informations présentes dans le contexte (contact du SPV et de l'antenne financière, rôle du SPV dans les modifications budgétaires). Cependant, elle mentionne un contact nommé « Anne Galopin » avec l'adresse af.polytech@univ-tours.fr, qui n'apparaît nulle part dans le contexte fourni. Cette information constitue une hallucination, d'où la note 4.
- **Avis Answer Relevance** : La réponse répond directement à la question « Comment peut-on changer le budget d’un projet ? » en indiquant les interlocuteurs et la procédure à suivre. Aucun élément hors sujet n'est introduit.
- **Avis Context Precision** : Le contexte contient les sections « Modifications budgétaires : contacter le SPV et l'antenne financière » et les détails sur la procédure de modification, ce qui est exactement ce dont la réponse a besoin. Le contexte est donc parfaitement ciblé.

### Question : Quelles sont les différentes démarches à effectuer ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 4.0/5, Context Precision: 4.0/5
- **Avis Faithfulness** : La plupart des affirmations de la réponse sont présentes dans le contexte : contacts de Juliette Piquard, référence au Guide des achats, rôle du SPIV, formulaire de saisine du référent déontologue. Cependant, la réponse ajoute un contact "Anne Galopin : af.polytech@univ-tours.fr" qui n’apparaît nulle part dans le contexte, constituant une hallucination.
- **Avis Answer Relevance** : La réponse répond à la question en listant plusieurs démarches (contact du responsable, consultation du guide, recours au SPIV, formulaire déontologique). Elle reste pertinente mais ne couvre pas l’ensemble des démarches possibles évoquées dans le contexte.
- **Avis Context Precision** : Le contexte fourni contient les informations nécessaires (contacts, guides, procédures, formulaires) et celles‑ci sont correctement exploitées dans la réponse. Le contexte est donc pertinent, même si la réponse n’en utilise qu’une partie.

### Question : - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire extérieur? Est-ce gratuit?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend correctement le besoin d’un contrat et le rôle du SPIV, ainsi que les coordonnées d’Hélène Jullien, qui figurent dans le contexte. En revanche, l’affirmation « il n'est pas toujours gratuit » n’est pas mentionnée dans le contexte, tout comme la suggestion de contacter Justine Gillet et la référence au « Laboratoire LIFAT », qui ne sont pas présentes dans le texte fourni. Ces éléments constituent des hallucinations.
- **Avis Answer Relevance** : La réponse répond globalement à la question en indiquant le cadre contractuel et en précisant que les expérimentations ne sont pas systématiquement gratuites. Un contact supplémentaire (Justine Gillet) est toutefois hors sujet, ce qui empêche d’attribuer le score maximal.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires : la question exacte, les coordonnées d’Hélène Jullien, les exigences contractuelles et le rôle du SPIV. Le système a donc pu s’appuyer sur un contexte pertinent.

### Question : A quelle adresse postale ou mail dois-je envoyer mon projet ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse cite correctement les adresses e‑mail présentes dans le contexte (juliette.piquard@univ‑tours.fr, spiv@univ‑tours.fr). Cependant, elle ajoute un contact qui n’apparaît pas du tout dans le contexte : « Anne Galopin : af.polytech@univ‑tours.fr ». Cette information est donc une hallucination, ce qui empêche d’attribuer la note maximale.
- **Avis Answer Relevance** : La réponse répond directement à la question en indiquant des adresses e‑mail où envoyer le projet, ce qui correspond exactement à la demande de l’utilisateur.
- **Avis Context Precision** : Le contexte fourni contient les adresses e‑mail nécessaires (Juliette Piquard, adresse générique du service). Il n’y a donc aucune lacune du côté du contexte.

### Question : Comment m’inscrire / me réinscrire ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La plupart des affirmations de la réponse sont présentes dans le contexte (création du compte ADUM, validation en 24 h, connexion à l'espace personnel, validation du dossier par les directions, réception d'un mail, modèles de rapport). Cependant, le contact fourni (Christèle Gaudron‑Bredif à l'adresse gaudron@univ‑tours.fr) n’apparaît pas dans le contexte ; le nom et l'email sont inventés, ce qui constitue une hallucination.
- **Avis Answer Relevance** : La réponse répond directement à la question « Comment m’inscrire / me réinscrire ? » en décrivant les étapes à suivre, les validations requises et les contacts éventuels. Aucun élément hors sujet n’est introduit.
- **Avis Context Precision** : Le contexte récupéré contient toutes les informations nécessaires pour répondre à la question : procédure ADUM, validation du dossier, modèles de rapport, contacts, lien du site web, etc. Il est donc très précis.

### Question : Quelles ressources le Pôle SAPS peut m’apporter ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend correctement le rôle général du Pôle SAPS et l'adresse e‑mail saps@univ‑tours.fr, qui figurent dans le contexte. En revanche, elle introduit des éléments inexistants : le contact "Anne Galopin : af.polytech@univ-tours.fr" et la mention de "ressources disponibles pour le laboratoire LIFAT". Ces informations ne sont pas présentes dans le contexte, ce qui constitue des hallucinations.
- **Avis Answer Relevance** : La réponse répond à la question en indiquant que le Pôle SAPS peut fournir des ressources et en proposant un contact. Elle reste globalement pertinente, même si elle ajoute des informations hors sujet (lab LIFAT, contact Anne Galopin) qui ne sont pas demandées.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires pour répondre : description de la stratégie SAPS, rôle du pôle, et l'adresse e‑mail de contact. Le système a donc pu s’appuyer sur un contexte pertinent et complet.

### Question : Y a-t-il des alumni ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)

### Question : Que propose le Pôle SAPS ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)

### Question : - Qu’est-ce qu’une invention ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)

### Question : - Je souhaite répondre à un Appel à projet?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)

### Question : je suis en arrêt de travail, qui dois-je contacter ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)

### Question : Combien de temps va prendre mon inscription ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 3.0/5, Context Precision: 3.0/5
- **Avis Faithfulness** : La réponse mentionne « Christèle Gaudron‑Bredif » et l’adresse e‑mail gaudron@univ‑tours.fr, qui n’apparaissent pas dans le contexte. Le contexte ne cite que Christèle Gaudron (sans Bredif) avec l’e‑mail christele.gaudron@univ‑tours.fr. Cette information est donc hallucination. Le reste de la phrase (conseil de contacter) n’est pas présent dans le texte source.
- **Avis Answer Relevance** : La réponse répond indirectement à la question en suggérant de contacter une personne pour obtenir le délai, mais elle ne fournit pas la durée demandée. Elle est donc partiellement pertinente mais ne répond pas directement à la question.
- **Avis Context Precision** : Le contexte contient une FAQ « Combien de temps va prendre mon inscription ? » ainsi que les coordonnées de Christèle Gaudron, mais il ne fournit pas de réponse chiffrée. Le contexte est donc partiellement utile, mais il manque l’information précise recherchée.

### Question : Comment avoir un email ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 4.0/5, Context Precision: 1.0/5
- **Avis Faithfulness** : La réponse mentionne un contact (Morgane Guibert) et une adresse e‑mail (morgane.guibert@univ-tours.fr) ainsi que le service informatique de l'Université de Tours. Aucun de ces éléments n'apparaît dans le contexte fourni, qui traite de confidentialité, de cahiers de laboratoire, de droits d'auteur, etc. Il s'agit donc d'hallucinations majeures.
- **Avis Answer Relevance** : La réponse répond à la question « Comment avoir un email ? » en proposant de contacter le service informatique et une personne précise. Elle est donc pertinente par rapport à la demande, même si les informations ne proviennent pas du contexte.
- **Avis Context Precision** : Le contexte ne contient aucune information relative à l'obtention d'un e‑mail, ni à l'Université de Tours, ni à des contacts. Le contexte est donc totalement inapproprié pour répondre à la question.

### Question : - Je souhaite me procurer le formulaire de déclaration d’invention de l’université, à qui dois-je m’adresser ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les informations fournies dans la réponse (adresse e‑mail drv-pi@univ-tours.fr et son rôle pour les questions générales de propriété intellectuelle) sont présentes textuellement dans le contexte. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question « à qui dois‑je m’adresser ? » en indiquant le contact approprié.
- **Avis Context Precision** : Le contexte contient l’adresse générique drv-pi@univ-tours.fr ainsi que l’instruction de l’utiliser pour les questions de propriété intellectuelle, ce qui est précisément ce qui est demandé.

### Question : Qui contacter pour toute demande d'ouvrages en service presse ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)

### Question : comment enregistrer ma demande de formation hors-catalogue et quels documents dois-je fournir ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 3.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse introduit des informations qui n’apparaissent pas dans le contexte, notamment le contact « Anne Galopin : af.polytech@univ-tours.fr » et la mention du laboratoire LIFAT. Ces éléments sont donc des hallucinations. Le reste du texte (absence d’information précise dans le contexte) est correct, mais la présence d’éléments non‑trouvés diminue fortement la fidélité.
- **Avis Answer Relevance** : La réponse répond partiellement à la question en indiquant que les détails ne sont pas fournis et en suggérant de contacter un service. Cependant, le contact proposé est erroné et aucune procédure concrète ni liste de documents n’est donnée, ce qui rend la pertinence limitée.
- **Avis Context Precision** : Le contexte récupéré ne contient aucune information sur la procédure d’enregistrement d’une formation hors‑catalogue ni sur les documents requis. Il porte plutôt sur l’accueil, l’accompagnement et des liens généraux (organigramme DRH, messagerie, etc.). Le contexte est donc peu pertinent pour la question posée.

### Question : Mon jury de thèse est-il valide ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)

### Question : quels types de financement de thèse existent ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)

### Question : - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autre CHRU?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend les adresses e‑mail et numéros de téléphone de Claude‑Emmanuel Boudet et d'Hélène Jullien exactement comme ils apparaissent dans le contexte, ainsi que les informations sur le SPIV qui sont présentes plus bas. Cependant, elle ajoute une recommandation de contacter Justine Gillet, ce qui n’est pas indiqué dans le contexte comme pertinent pour une question de santé, constituant ainsi une légère hallucination.
- **Avis Answer Relevance** : La réponse répond directement à la question en indiquant les personnes à contacter pour un projet clinique ou avec des échantillons du CHRU, ce qui correspond à la demande de l'utilisateur. Aucun élément hors sujet majeur n’est présent.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires (contacts, domaine santé, question précise sur les échantillons du CHRU). La réponse s’appuie sur ces données.

### Question : Je souhaite monter un projet, comment faire ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend correctement le rôle du SPIV, le conseil de le contacter deux semaines avant la clôture, les adresses e‑mail de Juliette Piquard et du service SPIV, qui figurent toutes dans le contexte. En revanche, elle ajoute un contact « Anne Galopin : af.polytech@univ-tours.fr » qui n’apparaît nulle part dans le texte fourni, ce qui constitue une hallucination.
- **Avis Answer Relevance** : La réponse répond à la question en indiquant comment procéder (contacter le SPIV, prendre contact tôt, utiliser les adresses e‑mail). Le conseil supplémentaire sur Anne Galopin n’est pas demandé et constitue une digression, d’où une légère perte de pertinence.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires pour répondre : rôle du SPIV, contacts, délai recommandé, etc. Le texte récupéré est donc très pertinent pour la question.

### Question : - Comment protéger un savoir-faire ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)

### Question : Je pars en mission, quelle pièce dois-je remplir ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)

### Question : Quel est le délai moyen entre la soumission d’un manuscrit et sa publication ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 4.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse indique correctement que le contexte ne contient pas d'information sur le délai moyen entre soumission et publication. Cependant, elle ajoute un contact (Christele Gaudron-Bredif, gaudron@univ-tours.fr) qui n'apparaît nulle part dans le contexte fourni, constituant une hallucination.
- **Avis Answer Relevance** : La réponse traite directement la question en signalant l'absence d'information pertinente dans le contexte et en demandant plus de contexte, ce qui est pertinent même si elle ne fournit pas la donnée recherchée.
- **Avis Context Precision** : Le contexte récupéré porte sur les procédures de soutenance de thèse et la gestion administrative des manuscrits de thèse, sans aucune mention du délai moyen entre soumission d'un manuscrit et sa publication. Il est donc peu pertinent pour répondre à la question.

## Query8_rag_batch_trials.json

### Question : - Puis-je directement signer un contrat qui engage mon laboratoire ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : {'score': 3, 'explanation': 'La réponse est globalement fidèle au contexte, car elle confirme que le PJR doit être consulté pour signer un contrat engageant le laboratoire (présent dans la liste des questions récurrentes du contexte : *« Puis-je directement signer un contrat qui engage mon laboratoire ? »*). **Cependant**, elle introduit des éléments **non présents dans le contexte** (ex. : nom et email de *Justine Gillet*, adresse générique *drv-pi@univ-tours.fr*), ce qui constitue une **hallucination mineure** (d’où un score de 3/5). Le contexte ne fournit aucune information sur les contacts spécifiques du PJR, seulement la mention de son existence et de sa compétence.'}
- **Avis Answer Relevance** : {'score': 5, 'explanation': 'La réponse est **parfaitement pertinente** : elle répond directement à la question (*« Non, vous ne pouvez pas signer directement »*), explique clairement la procédure (validation par le PJR), et propose une action concrète (*contacter le PJR*). Aucune digression ou information superflue.'}
- **Avis Context Precision** : {'score': 5, 'explanation': 'Le contexte est **suffisant et précis** pour répondre à la question. Il inclut explicitement la question *« Puis-je directement signer un contrat qui engage mon laboratoire ? »* dans la liste des sujets relevant du PJR (section *II. Liste des questions récurrentes*), et détaille les risques juridiques liés aux engagements contractuels (ex. : responsabilité de l’établissement, clauses de confidentialité). Aucune information manquante pour une réponse complète.'}

### Question : - Qu’est-ce qu’un auteur ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 4.0/5

### Question : - Qu’est-ce qu’une invention ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 4.0/5, Context Precision: 1.0/5
- **Avis Faithfulness** : La réponse du système **hallucine** des critères techniques (nouveauté, activité inventive, application industrielle) qui **ne figurent pas dans le contexte fourni**. Celui-ci traite exclusivement de la **dévolution des droits de propriété intellectuelle** pour des créateurs indépendants accueillis par des structures de recherche, sans jamais définir explicitement ce qu'est une *invention* au sens juridique ou technique. Les seuls éléments pertinents dans le contexte concernent les **inventions de mission** (réalisées dans le cadre d'une convention ou d'études confiées) et les **inventions hors-mission attribuables**, mais sans en donner une définition générique. La mention des *brevets* est accessoire et ne justifie pas une généralisation non sourcée.
- **Avis Answer Relevance** : La réponse est **globalement pertinente** pour un utilisateur cherchant une définition basique d'une invention, même si elle ne s'appuie pas sur le contexte. Elle aborde bien la dimension *propriété intellectuelle* (mentionnée dans la question) et les critères classiques de brevetabilité, qui sont une attente légitime face à cette question. Cependant, elle ignore totalement le **contexte spécifique des créateurs indépendants** (central dans les documents fournis), ce qui limite sa pertinence pour un public ciblé (ex: chercheurs, juristes en PI).
- **Avis Context Precision** : Le contexte fourni est **totalement imprécis** pour répondre à la question posée. Il détaille des **cas particuliers** (dévolution des droits pour des non-salariés, distinctions logiciels/inventions, statuts des émérites, etc.) sans jamais offrir de définition générique ou des critères juridiques/techniques d'une invention. Les extraits pertinents (ex: *inventions de mission* dans la table comparative en fin de document) sont noyés dans des discussions procédurales et ne suffisent pas à construire une réponse complète. Un contexte idéal aurait inclus des articles du **Code de la Propriété Intellectuelle (CPI)** définissant une invention (ex: [Art. L611-10](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006734000/)) ou des références à l'**INPI**.

### Question : - Quelles sont les conditions de brevetabilité ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 2.0/5, Context Precision: 4.0/5
- **Reasoning global** : [{'criterion': 'faithfulness', 'explanation': "La réponse du système **hallucine des informations** non présentes dans le contexte fourni : aucune mention d'**Anouk Martinet**, de son email (**anouk.martinet@univ-tours.fr**), ou d'une procédure de contact spécifique à l'Université de Tours. Le contexte évoque uniquement le **Pôle Juridique Recherche (PJR)** comme point de référence, sans coordonnées précises."}, {'criterion': 'answer_relevance', 'explanation': 'La réponse **redirige vers un contact** plutôt que de fournir les **conditions de brevetabilité** (nouveauté, activité inventive, application industrielle), qui sont pourtant **explicitement listées dans la question récurrente** du contexte (section *II. Liste des questions récurrentes*). Une réponse directe était possible en citant les **3 critères classiques** (même si non détaillés dans le contexte).'}, {'criterion': 'context_precision', 'explanation': 'Le contexte **contient bien les éléments** pour une réponse partielle : la question *« Quelles sont les conditions de brevetabilité ? »* est **explicitement référencée** dans la liste des sujets du PJR (section II), et des décrets (ex: R.611-1 à -141 CPI) sont cités. Cependant, **aucune définition claire des critères** (nouveauté, etc.) n’y est développée, limitant la précision possible.'}]

### Question : - Comment protéger un savoir-faire ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 2.0/5, Context Precision: 4.0/5

### Question : - Je souhaite me procurer le formulaire de déclaration d’invention de l’université, à qui dois-je m’adresser ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 2.0/5, Context Precision: 3.0/5

### Question : - Ma/mon doctorant(e) doit soutenir sa thèse prochainement et le manuscrit contient des informations confidentielles faisant l’objet d’un dépôt de demande en brevet en cours, que dois-je faire ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : {'score': 2, 'explanation': 'La réponse mentionne des noms et contacts spécifiques (ex. *Justine Gillet*, *drv-pi@univ-tours.fr*) **absents du contexte fourni**, ce qui constitue une **hallucination claire** (informations non sourcées). Le contexte ne cite ni personnes ni adresses e-mail, mais évoque uniquement le *Pôle Juridique Recherche (PJR)* de manière générique. La suggestion de préciser le *laboratoire LIFAT* est également une **inférence non justifiée** par le texte source.'}
- **Avis Answer Relevance** : {'score': 4, 'explanation': 'La réponse est **globalement pertinente** : elle oriente vers le PJR (mentionné dans le contexte comme compétent pour les questions de propriété intellectuelle et brevets, cf. *Liste de sujets pour lesquels les chercheurs doivent être dirigés vers le PJR*), et évoque des mesures types (restrictions d’accès, conventions de confidentialité) **alignées avec les enjeux du contexte** (ex. *sécurisation de la confidentialité*, *accords ad hoc*). Le ton est direct et utile.'}
- **Avis Context Precision** : {'score': 5, 'explanation': 'Le contexte contient **toutes les informations nécessaires** pour répondre : (1) la question exacte est listée dans les *questions récurrentes* du PJR (*Ma/mon doctorant(e) doit soutenir sa thèse...*), (2) des sections détaillent la gestion de la confidentialité (ex. *conventions de collaborateur bénévole*, *responsabilité de l’établissement*), et (3) le PJR est clairement identifié comme interlocuteur pour les brevets et la propriété intellectuelle. Aucune information manquante.'}

### Question : - Où puis-je me procurer des cahiers de laboratoire papier ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 3.0/5, Context Precision: 1.0/5

## Query_Mix_02_fast_draft_trials.json

### Question : C’est quoi les SAPS ?
- **Erreur d'évaluation** : 'choices'

### Question : Comment peut-on changer le budget d’un projet ?
- **Erreur d'évaluation** : 'choices'

### Question : Quelles sont les différentes démarches à effectuer ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La plupart des informations (contacts Juliette Piquard, spiv@univ-tours.fr, usage du CLE, formulaire animaux) sont présentes dans le contexte. Cependant, le système a ajouté le contact « Anne Galopin : af.polytech@univ-tours.fr », qui n’apparaît nulle part dans le texte fourni, ainsi qu’un lien vers https://www.univ-tours.fr/fr/services-directions/recherche.html qui n’est pas présent. Ces ajouts constituent des hallucinations, d’où la note moyenne.
- **Avis Answer Relevance** : La réponse propose des étapes concrètes (« démarches ») en lien avec la question, en se focalisant sur le laboratoire LIFAT. Elle répond donc à la demande, même si elle se spécialise sur un cas particulier qui n’est pas explicitement demandé. La pertinence reste élevée.
- **Avis Context Precision** : Le contexte récupéré contient toutes les informations nécessaires pour répondre : contacts, services (SPIV), outils (CLE), formulaires, etc. Le système a pu s’appuyer sur ces éléments, justifiant la note maximale.

### Question : - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire extérieur? Est-ce gratuit?
- **Erreur d'évaluation** : 'choices'

### Question : A quelle adresse postale ou mail dois-je envoyer mon projet ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse utilise les adresses e‑mail présentes dans le contexte (juliette.piquard@univ‑tours.fr, spiv@univ‑tours.fr) et reprend des consignes du texte (contact 2 semaines avant la clôture). Cependant elle introduit un contact qui n’apparaît pas dans le contexte : Anne Galopin (af.polytech@univ‑tours.fr). Cette hallucination empêche d’attribuer le score maximal.
- **Avis Answer Relevance** : La réponse indique clairement à quelle adresse e‑mail envoyer le projet, ce qui répond à la question. Elle ajoute toutefois des informations superflues (procédure détaillée, lien vers des ressources, contact supplémentaire non demandé) qui diminuent légèrement la pertinence.
- **Avis Context Precision** : Le contexte contient les adresses e‑mail nécessaires (Juliette Piquard, spiv, etc.) et aucune adresse postale. Ainsi le contexte est parfaitement adapté pour répondre à la question.

### Question : Comment m’inscrire / me réinscrire ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La plupart des étapes, dates, documents requis et procédures sont directement tirés du contexte. Cependant le nom et l'e‑mail du contact fourni (« Christele Gaudron‑Bredif », gaudron@univ‑tours.fr) n’apparaissent pas dans le texte source (le contexte donne Christèle Gaudron et christele.gaudron@univ‑tours.fr). Cette inexactitude constitue une hallucination, d’où la note 4.
- **Avis Answer Relevance** : La réponse répond précisément à la question « Comment m’inscrire / me réinscrire ? » en détaillant la création de compte ADUM, les pièces à fournir, les délais et les contacts. Aucun élément hors sujet n’est présent.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires (procédure ADUM, dates, documents, contacts, validation par la direction). Le système les a exploitées de façon pertinente.

### Question : Quelles ressources le Pôle SAPS peut m’apporter ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La plupart des affirmations (incitation, formation, implication de la société civile, réseau inter‑services, contact e‑mail) sont directement tirées du contexte. Cependant, la réponse introduit des éléments qui n’apparaissent pas dans le texte, comme la mention du laboratoire « LIFAT », ainsi que des exemples précis (visibilité, soutiens institutionnels, supports multimédias, expositions virtuelles, projets artistiques interactifs, vulgarisation créative) qui ne sont pas présents dans le contexte. Ces ajouts constituent des hallucinations, d’où la note 4.
- **Avis Answer Relevance** : La réponse répond exactement à la question en listant les différentes ressources que le Pôle SAPS peut offrir, sans digression hors sujet.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires (stratégie SAPS, services rattachés, missions de formation, implication sociétale, contact) pour répondre à la question, ce qui justifie la note maximale.

### Question : Y a-t-il des alumni ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse indique qu'aucune information sur un réseau d'alumni n'a été trouvée, ce qui correspond exactement au contenu du contexte. Cependant, elle suggère de contacter le "Service Communication" et la "Direction des Relations Extérieures", entités qui n'apparaissent pas dans le contexte fourni, constituant ainsi une petite hallucination.
- **Avis Answer Relevance** : La réponse répond directement à la question "Y a-t-il des alumni ?" en indiquant l'absence d'information et en proposant une démarche supplémentaire, ce qui est pleinement pertinent.
- **Avis Context Precision** : Le contexte récupéré ne contient aucune information relative aux alumni ou à un réseau d'anciens étudiants. Il porte sur la science ouverte, les mobilités Erasmus+, etc., donc il n'est pas pertinent pour répondre à la question.

### Question : Que propose le Pôle SAPS ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend correctement les quatre axes de la stratégie (inciter, former/informer, impliquer, inspirer) et le pilotage du pôle tel que décrits dans le contexte. Cependant, elle introduit des informations qui n’apparaissent pas dans le contexte : un contact « Anne Galopin : af.polytech@univ-tours.fr » et la mention d’une unité de recherche spécifique (LIFAT) comme exemple, qui ne sont pas présentes dans le texte fourni. Ces ajouts constituent des hallucinations, ce qui fait baisser la note de fidélité.
- **Avis Answer Relevance** : La réponse répond directement à la question « Que propose le Pôle SAPS ? » en détaillant les quatre axes de proposition du pôle ainsi que les acteurs et le contact principal. Le contenu est donc très pertinent pour la question posée.
- **Avis Context Precision** : Le contexte retrouvé contient toutes les informations nécessaires pour répondre à la question : description de la stratégie en quatre points, organigramme du pôle, services rattachés et le contact saps@univ‑tours.fr. Le contexte est donc parfaitement adapté.

### Question : - Qu’est-ce qu’une invention ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 4.0/5, Context Precision: 3.0/5
- **Avis Faithfulness** : La réponse introduit plusieurs informations qui ne figurent pas dans le contexte fourni : la définition précise de l'invention comme "solution technique nouvelle à un problème technique, susceptible d'application industrielle et protégée par un brevet" ainsi que le nom et l'adresse e‑mail de Morgane Guibert du PJR. Aucun de ces éléments n'est présent dans le texte de référence, ce qui constitue une hallucination majeure.
- **Avis Answer Relevance** : La réponse répond à la question posée en donnant une définition de l'invention, ce qui est pertinent. L'ajout du contact est superflu mais ne rend pas la réponse hors sujet.
- **Avis Context Precision** : Le contexte mentionne la notion d'invention et propose des questions liées, mais il ne fournit pas de définition explicite. Le contexte est donc partiellement utile, mais il manque les détails nécessaires pour répondre directement.

### Question : - Je souhaite répondre à un Appel à projet?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend correctement les coordonnées de Justine Gillet et les liens de financement qui figurent dans le contexte. Cependant, l’affirmation « dans le cadre du laboratoire LIFAT » n’est pas présente dans le contexte (LIFAT apparaît seulement dans la description du secteur de Juliette Piquard, pas comme laboratoire). Cette information est donc une hallucination, ce qui empêche d’attribuer la note maximale.
- **Avis Answer Relevance** : La question porte sur la façon de répondre à un appel à projet. La réponse indique clairement quel chargé d’affaires contacter, fournit ses coordonnées et rappelle les principaux guichets de financement, répondant ainsi directement à la demande.
- **Avis Context Precision** : Le contexte récupéré contient les contacts des chargés d’affaires, les questions associées et les liens vers les sources de financement. Toutes ces informations sont pertinentes pour répondre à la question.

### Question : je suis en arrêt de travail, qui dois-je contacter ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse cite correctement Juliette Piquard et son adresse e‑mail, qui figurent dans le contexte, ainsi que les liens vers les pages de congés maladie présents dans le texte. Cependant, elle introduit un contact qui n’existe pas dans le contexte : « Anne Galopin : af.polytech@univ-tours.fr ». Cette information est donc une hallucination, ce qui empêche d’attribuer la note maximale.
- **Avis Answer Relevance** : La réponse répond à la question en indiquant un interlocuteur (Juliette Piquard) à contacter pour déclarer un arrêt de travail. Elle ajoute toutefois un second contact erroné et des détails supplémentaires qui ne sont pas demandés, ce qui diminue légèrement la pertinence.
- **Avis Context Precision** : Le contexte fourni contient les coordonnées de Juliette Piquard, ainsi que les liens vers les pages de congés maladie. Ces éléments sont suffisants pour répondre à la question, d’où la note maximale.

### Question : Combien de temps va prendre mon inscription ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 2.0/5, Context Precision: 3.0/5
- **Avis Faithfulness** : La réponse cite un contact qui apparaît dans le contexte (christele.gaudron@univ-tours.fr), mais le nom complet « Christele Gaudron‑Bredif » n’est pas présent dans le texte fourni, ce qui constitue une hallucination. De plus, l’affirmation selon laquelle la durée dépend de plusieurs étapes et peut varier n’est pas explicitement mentionnée dans le contexte ; il n’y a aucune indication chiffrée sur le délai. Ainsi, plusieurs éléments ne sont pas directement traçables.
- **Avis Answer Relevance** : La question demande une estimation du temps nécessaire à l’inscription. La réponse ne fournit aucune estimation, se contentant de dire que le délai varie et d’inviter l’utilisateur à contacter un gestionnaire. Elle ne répond donc pas réellement à la demande de durée.
- **Avis Context Precision** : Le contexte contient de nombreuses informations sur la procédure d’inscription, les pièces à fournir, les contacts et les dates d’ouverture des inscriptions, mais il ne fournit pas de durée précise. Le contexte est donc partiellement utile, mais il manque l’information recherchée (délai).

### Question : Comment avoir un email ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 4.0/5, Context Precision: 1.0/5
- **Avis Faithfulness** : La réponse mentionne un contact (Morgane Guibert) et une adresse e‑mail (morgane.guibert@univ-tours.fr) qui n’apparaissent nulle part dans le contexte fourni. Toutes les affirmations de la réponse ne sont donc pas traçables dans le texte, ce qui constitue une hallucination majeure.
- **Avis Answer Relevance** : La réponse répond à la question « Comment avoir un email ? » en proposant de contacter une personne précise, ce qui est pertinent pour l’utilisateur même si l’information n’est pas issue du contexte.
- **Avis Context Precision** : Le contexte récupéré ne contient aucune information relative à la création ou à l’obtention d’une adresse e‑mail, ni à un interlocuteur à contacter. Il est donc hors sujet par rapport à la question posée.

### Question : - Je souhaite me procurer le formulaire de déclaration d’invention de l’université, à qui dois-je m’adresser ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : le Pôle Juridique Recherche (PJR) est mentionné comme l'entité compétente, et l'adresse e‑mail drv-pi@univ-tours.fr figure dans la section Contacts comme adresse générique pour les questions de propriété intellectuelle. Aucun élément n’a été inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question en indiquant à qui s’adresser (PJR) et en fournissant l’adresse e‑mail appropriée, sans digression.
- **Avis Context Precision** : Le contexte contient les informations nécessaires : le nom du service (PJR) et l’adresse e‑mail (drv-pi@univ-tours.fr). Ces éléments sont directement exploités dans la réponse.

### Question : Qui contacter pour toute demande d'ouvrages en service presse ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 2.0/5, Context Precision: 3.0/5
- **Avis Faithfulness** : La réponse mentionne que Juliette Piquard est à contacter pour les demandes d'ouvrages en service presse et ajoute « liée au laboratoire LIFAT ». Aucun de ces éléments (rôle de presse, lien avec LIFAT) n’apparaît dans le contexte. Seul l’adresse e‑mail de Juliette Piquard est présente, mais l’attribution du rôle de contact presse est une hallucination.
- **Avis Answer Relevance** : La réponse tente de répondre à la question mais fournit un contact qui n’est pas justifié par le contexte. Elle ne répond donc pas correctement à la demande de contact pour le service presse.
- **Avis Context Precision** : Le contexte contient plusieurs contacts (Morgane Guibert, Juliette Piquard, etc.) mais aucune indication claire sur le « service presse ». Le contexte est donc partiellement utile, mais il manque l’information précise recherchée.

### Question : comment enregistrer ma demande de formation hors-catalogue et quels documents dois-je fournir ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 2.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse introduit de nombreuses informations qui ne figurent pas dans le contexte fourni : le laboratoire LIFAT, le contact « Anne Galopin » avec son adresse e‑mail, ainsi que des documents précis (formulaire de demande, accord hiérarchique, devis) qui ne sont jamais mentionnés. Aucun de ces éléments ne peut être tracé dans le texte source, ce qui constitue une hallucination majeure.
- **Avis Answer Relevance** : La réponse tente de répondre à la question en proposant de contacter la DRH ou le service formation, mais elle ne fournit pas de procédure concrète ni la liste exacte des documents demandés. Elle reste donc très partielle et peu utile pour l'utilisateur.
- **Avis Context Precision** : Le contexte récupéré ne contient pas d’instructions spécifiques sur la demande de formation hors‑catalogue. Il ne fournit que des informations générales sur l’accueil, la formation et des contacts DRH, ce qui n’est pas suffisant pour répondre précisément à la question.

### Question : Mon jury de thèse est-il valide ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend la plupart des critères de composition du jury présents dans le contexte (nombre de membres, proportion de professeurs, extériorité, limitation des émérites, équilibre hommes‑femmes, absence de conflit d’intérêts, présence d’un HDR). Cependant, elle introduit un contact « Anouk Martinet : anouk.martinet@univ-tours.fr » qui n’apparaît nulle part dans le contexte, ainsi qu’un lien URL légèrement différent (cvl au lieu de cyl). Ces éléments constituent des hallucinations, ce qui empêche d’attribuer la note maximale.
- **Avis Answer Relevance** : La réponse répond directement à la question « Mon jury de thèse est‑il valide ? » en listant les critères à vérifier et en demandant les informations nécessaires pour juger la validité du jury. Elle fournit également des ressources utiles.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires sur la composition du jury, les règles d’émérite, le nombre de membres, les exigences d’équilibre et de HDR, etc. Le système a correctement exploité ces données.

### Question : quels types de financement de thèse existent ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La plupart des éléments de la réponse sont directement tirés du contexte (contrats doctoraux, bourses régionales, bourses Rabelaisiennes, CIFRE, ANR, Europe, Labex, contrats entreprise, bourses industrielles, cotutelles, doctorants salariés, etc.). Deux exemples précis ("Horizon Europe" et "Fondation pour la Recherche Médicale") ne figurent pas dans le texte fourni, ce qui constitue une petite hallucination.
- **Avis Answer Relevance** : La réponse répond exactement à la question en listant les différents types de financement de thèse, sans digression hors sujet.
- **Avis Context Precision** : Le contexte fourni contient toutes les catégories de financement mentionnées dans la réponse ; il est donc très pertinent et complet pour répondre à la question.

### Question : - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autre CHRU?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les informations fournies (nom, email, téléphone de Claude‑Emmanuel BOUDET, ainsi que la suggestion de Justine Gillet) figurent exactement dans le contexte. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse indique clairement le contact approprié pour les échantillons du CHRU, répondant directement à la question. L’ajout de Justine Gillet est une information supplémentaire mais reste pertinente.
- **Avis Context Precision** : Le contexte contient la ligne de Claude‑Emmanuel BOUDET avec son domaine Santé et ses coordonnées, qui sont exactement les informations nécessaires pour répondre à la question.

### Question : Je souhaite monter un projet, comment faire ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend la plupart des étapes et contacts présents dans le contexte (SPV, Juliette Piquard, spiv@univ‑tours.fr, délai de 2 semaines, documents à fournir). Cependant, elle introduit des éléments qui n’apparaissent pas dans le contexte : le nom « Anne Galopin » et l’adresse e‑mail af.polytech@univ‑tours.fr, ainsi que la mention « laboratoire LIFAT » comme entité précise alors que LIFAT n’est mentionné que comme secteur. Ces ajouts constituent des hallucinations, ce qui empêche d’attribuer la note maximale.
- **Avis Answer Relevance** : La réponse répond directement à la question « comment monter un projet ? » en proposant les étapes clés, les documents requis, les contacts utiles et des ressources complémentaires. Aucun élément hors sujet n’est présent.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires pour répondre : rôle du SPV, procédure de montage, documents attendus, contacts (Juliette Piquard, spiv@univ‑tours.fr), délai de prise de contact, etc. Le contexte est donc très précis et complet.

### Question : - Comment protéger un savoir-faire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : le PJR est bien l'entité compétente, Anouk Martinet est bien la juriste chargée de la valorisation avec l'adresse anouk.martinet@univ-tours.fr, et l'adresse générique drv-pi@univ-tours.fr figure également dans le texte. Aucun élément n’a été inventé.
- **Avis Answer Relevance** : La réponse répond directement à la question « Comment protéger un savoir‑faire ? » en indiquant le service à contacter et les types d’outils juridiques pertinents (accords de confidentialité, conventions). Aucun hors‑sujet n’est présent.
- **Avis Context Precision** : Le contexte contient la question récurrente « Comment protéger un savoir‑fait ? », ainsi que les coordonnées du PJR et de ses membres. Le système a extrait exactement ces informations, donc le contexte était parfaitement adapté.

### Question : Je pars en mission, quelle pièce dois-je remplir ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 2.0/5, Context Precision: 3.0/5
- **Avis Faithfulness** : La réponse mentionne un contact qui n’apparaît pas dans le contexte (Anne Galopin : af.polytech@univ-tours.fr). Cette information est donc une hallucination. Le reste du texte (absence de procédure détaillée) est cohérent avec le contexte, mais la présence d’une donnée non‑présente diminue fortement la fidélité.
- **Avis Answer Relevance** : La question demande « quelle pièce doit‑je remplir ? ». La réponse ne fournit aucune pièce ou formulaire, se contentant de dire que les procédures ne sont pas détaillées et de proposer un contact. Elle ne répond donc pas directement à la demande.
- **Avis Context Precision** : Le contexte contient des informations utiles (liste des documents à fournir, contacts du SPV) mais ne précise pas de formulaire spécifique pour une « mission ». Ainsi le contexte est partiellement pertinent, mais il manque le détail exact recherché.

### Question : Quel est le délai moyen entre la soumission d’un manuscrit et sa publication ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 4.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse indique que le contexte ne fournit pas l'information demandée, ce qui est correct. Cependant, elle invente un contact (Christele Gaudron‑Bredif, gaudron@univ‑tours.fr) qui n'apparaît nulle part dans le texte fourni, constituant une hallucination. Ainsi la fidélité est affectée.
- **Avis Answer Relevance** : La réponse répond à la question en précisant l'absence d'information dans le contexte et propose des pistes de contact, ce qui reste pertinent même si elle ne fournit pas le délai demandé.
- **Avis Context Precision** : Le contexte récupéré ne contient aucune donnée sur le délai moyen entre soumission et publication. Il est donc peu pertinent pour la question, ce qui justifie une note basse.

## Query2_rag_batch_trials.json

### Question : Quels documents faut-il fournir pour l’inscription ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Reasoning global** : {'faithfulness': "La réponse du système se base strictement sur le contexte fourni (exigences pour l'inscription en doctorat, incluant pièces d'identité, diplômes, justificatifs de financement et spécificités pour les diplômes étrangers ou dispenses). Aucune information externe ou hallucinée n'est ajoutée. Les détails comme la traduction certifiée ou le regroupement en un seul PDF sont directement tirés du contexte.", 'answer_relevance': "La réponse adresse **précisément** la question posée ('documents pour l’inscription') en listant de manière claire et organisée les éléments requis, sans digression. Elle distingue même les cas particuliers (dispenses, ED 'Humanités et Langues'), ce qui renforce son utilité.", 'context_precision': 'Le contexte fourni contient **toutes les informations nécessaires** pour répondre à la question, y compris les nuances (ex: documents supplémentaires pour les diplômes étrangers ou les écoles doctorales spécifiques). Les images et répétitions dans le contexte (ex: doubles mentions des justificatifs) confirment la exhaustivité des données sources.'}

### Question : Quelles sont les dates limites d’inscription ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 4.0/5, Context Precision: 1.0/5

### Question : Qui contacter pour avoir des informations sur la gestion de l’inscription et du contrat doctoral ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 3.0/5, Context Precision: 2.0/5

### Question : Quelle est mon école doctorale de rattachement ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 4.0/5

### Question : Y a-t-il une journée de rentrée ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 1.0/5
- **Reasoning global** : {'faithfulness': "La réponse ne contient aucune information non sourcée ou inventée. Elle reste strictement dans les limites du contexte fourni (ou son absence) et propose une alternative crédible (contact direct). L'erreur mineure sur l'email ('.f' au lieu de '.fr') est un détail technique, non une hallucination.", 'answer_relevance': 'La réponse aborde directement la question en : (1) confirmant l’absence d’information dans le contexte, (2) suggérant des pistes concrètes pour obtenir la réponse (contacts/services). Elle évite les hors-sujet et guide l’utilisateur vers une résolution.', 'context_precision': 'Le contexte fourni ne contient **aucune** mention de journée de rentrée, d’événements d’accueil, ou de calendrier universitaire. Il se limite à des procédures administratives (formations, soutenances, inscriptions). Le score reflète l’**incapacité du contexte** à répondre à la question, non un défaut de la réponse.'}

### Question : Y a-t-il une association de doctorants ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 4.0/5

### Question : Comment avoir un email ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 4.0/5

### Question : Qui gère mon contrat doctoral ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 1.0/5
- **Avis Faithfulness** : La réponse du système est strictement fidèle : elle ne contient **aucune** information issue du contexte (qui ne traitait pas des contrats doctoraux mais des collaborateurs bénévoles, de la propriété intellectuelle et des risques juridiques). Elle se limite à une absence d'information et à une redirection vers des contacts génériques (école doctorale, RH, PJR), sans inventer de détails. Note maximale (5/5).
- **Avis Answer Relevance** : La réponse est **pertinente** car elle oriente l'utilisateur vers les acteurs habituellement compétents pour gérer un contrat doctoral (école doctorale, RH). Cependant, elle manque de précision sur *qui exactement* gère le contrat (ex: l'école doctorale est-elle l'autorité signataire ? Le laboratoire a-t-il un rôle ?). La mention du PJR (Pôle Juridique Recherche) est moins pertinente ici, car ce pôle gère surtout la propriété intellectuelle et les contrats de recherche, pas les contrats doctoraux. Note légèrement réduite (4/5).
- **Avis Context Precision** : Le contexte fourni est **totalement non pertinent** pour répondre à la question. Il aborde des sujets juridiques liés aux collaborateurs bénévoles, à la propriété intellectuelle et aux risques de requalification en contrat de travail, mais **rien** sur les contrats doctoraux, leur gestion administrative ou les acteurs responsables. Il ne contenait aucune information utile pour construire une réponse. Note minimale (1/5).

### Question : Comment obtenir ma carte étudiante ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 3.0/5

### Question : Y a-t-il des questions spécifiques pour les étudiants étrangers ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 4.0/5

### Question : Où trouver la charte du doctorat ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 1.0/5
- **Reasoning global** : {'faithfulness': 'La réponse ne contient aucune information non sourcée du contexte fourni. Elle reconnaît explicitement l’absence de la charte dans les documents et propose une solution externe *sans l’affirmer comme une certitude* (formulation prudente : *« je vous invite à contacter »*).', 'answer_relevance': 'La réponse est utile car elle oriente l’utilisateur vers une action concrète (contacter un service dédié), bien que le contexte ne contienne pas la réponse directe. Note légèrement inférieure à 5 car une mention générique du *site du collège doctoral* (présent dans le contexte : *https://collegedoctoral-cvl.fr/*) aurait pu être ajoutée comme piste complémentaire.', 'context_precision': 'Le contexte fourni ne mentionne **ni le terme « charte du doctorat »**, ni un lien ou une procédure pour y accéder. Il se limite aux démarches administratives (ADUM, soutenance, inscriptions), aux pièces justificatives, et à des liens partiels (ex : calendrier des soutenances). Aucune information pertinente n’était disponible pour répondre à la question.'}

### Question : Qui contacter en cas de conflit ou de VSS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Reasoning global** : La réponse est **strictement fidèle** au contexte fourni : elle cite uniquement les contacts présents dans le document (cellules d'écoute de l'Université de Tours pour conflits, VSS et discriminations), sans ajouter d'informations externes ou erronées. **Pertinence maximale** : elle répond directement à la question en segmentant les cas (conflit vs VSS) et en fournissant les adresses e-mail exactes. Le **contexte était précis** : il contenait bien les données nécessaires (adresses des cellules VSS, conflits, discriminations pour l'Université de Tours), reproduites sans distorsion. L'ajout du lien vers la Mission Égalité et le SSU renforce l'utilité sans sortir du cadre source.

### Question : Comment gérer mes formations dans le temps ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 3.0/5
- **Reasoning global** : [{'faithfulness': "La réponse s'appuie majoritairement sur le contexte fourni (ex: formations obligatoires, crédits doctoraux, Adum, désistement 15 jours avant). Cependant, elle introduit une **information non vérifiable dans le contexte** : le contact 'Marie Clermonte' (marie.clermonte@univ-tours.f) qui n’apparaît nulle part. Cela justifie un **4/5** plutôt que 5."}, {'answer_relevance': 'La réponse est **exhaustive et directement utile** : elle structure clairement les étapes (planification, inscription, validation, soutenance) et extrait les règles critiques (ex: 50 crédits, formations obligatoires). Elle reformule aussi les contraintes (ex: absence = refus futur) de manière actionnable. **5/5**.'}, {'context_precision': 'Le contexte est **partiellement précis** : il contient des informations clés (ex: règles de validation, formations obligatoires, Adum), mais manque de détails concrets sur la **gestion temporelle** (ex: comment prioriser les formations sur 3 ans, outils de suivi du temps). Les éléments sur les crédits et le portfolio sont dispersés dans des sections peu structurées. **3/5**.'}]

### Question : Quelles sont les formations obligatoires et quand faut-il les suivre ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 4.0/5

### Question : Les formations externes sont-elles prises en compte ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5

### Question : Comment financer les missions d’enseignement ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5

### Question : Quand faut-il faire les CSI et combien faut-il en faire ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 4.0/5, Context Precision: 1.0/5

### Question : Le CSI est-il nécessaire pour la réinscription ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5

### Question : Comment fonctionne le CSI ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)

### Question : Que faire si le CSI donne un avis défavorable ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 4.0/5
- **Avis Faithfulness** : {'score': 4, 'explanation': "La réponse s’appuie majoritairement sur le contexte fourni (rôle du CSI, alerte à l’ED, solutions proposées). Cependant, certains éléments ne sont pas explicitement mentionnés dans le contexte, comme le nom et l’email de la référente ('Marie Clermonte'), ce qui introduit une légère *hallucination mineure* (ou une inférence non justifiée). Le reste est fidèle : processus d’alerte, rôle de l’ED, et types de solutions envisagées (médiation, soutien)."}
- **Avis Answer Relevance** : {'score': 5, 'explanation': 'La réponse est **directement utile et complète** : elle explique clairement (1) la signification d’un avis défavorable du CSI, (2) les étapes déclenchées (alerte à l’ED, réunion de bureau), (3) les actions concrètes pour le doctorant (contact référent, solutions proposées). Aucune digression.'}
- **Avis Context Precision** : {'score': 4, 'explanation': "Le contexte contient **toutes les informations essentielles** pour répondre (rôle du CSI, processus d’alerte, actions de l’ED en cas de difficultés). Cependant, il manque des détails pratiques comme un **contact spécifique** (ex. : email d’un référent), ce qui justifie un 4 plutôt qu’un 5. La réponse aurait pu se limiter strictement aux éléments du contexte (ex. : omettre 'Marie Clermonte' ou préciser que ce détail n’est pas sourcé)."}

### Question : Comment préparer un dépôt de thèse (attendus du manuscrit, langue, etc.) ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 3.0/5
- **Avis Faithfulness** : La réponse s'appuie majoritairement sur le contexte fourni (exigences ADUM, résumés, délais, pièces justificatives). Cependant, elle extrapole légèrement en mentionnant la possibilité de rédiger le manuscrit en anglais (non explicitement confirmée dans le contexte, mais plausible dans le cadre académique français).
- **Avis Answer Relevance** : La réponse couvre exhaustivement la question : format du manuscrit, langue, délais, procédures administratives, et contacts utiles. Elle reformule clairement les exigences du contexte pour une compréhension immédiate.
- **Avis Context Precision** : Le contexte contient les informations essentielles (délais, résumés, pièces à fournir), mais il est désorganisé (images, répétitions, fragments de phrases) et manque de détails sur des aspects critiques comme la langue du manuscrit ou les spécificités des écoles doctorales. Exemple : les règles pour SSBCV/EMSTU/MIPTIS sont mentionnées, mais sans explication claire des différences.

### Question : Comment préparer un jury de thèse et quelle est sa composition ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 4.0/5

### Question : Comment préparer une soutenance (délais, etc.) ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 4.0/5

### Question : Quelles sont les différentes démarches à effectuer ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Reasoning global** : {'faithfulness': "La réponse s'appuie strictement sur le contexte fourni, sans ajouter d'informations externes ou non vérifiables. Tous les éléments mentionnés (documents requis, processus ADUM, spécificités par école doctorale, etc.) sont directement extraits du contexte.", 'answer_relevance': "La réponse adresse **précisément** la question sur les 'démarches à effectuer' en structurant les étapes clés (préparation des documents, dépôt via ADUM, validation hiérarchique) et en ciblant les particularités (ex: ED Humanités et Langues). Aucune digression.", 'context_precision': 'Le contexte contenait **toutes les informations nécessaires** pour répondre de manière exhaustive : liste des documents, détails sur ADUM, processus de validation, exigences linguistiques, et cas spécifiques (dispense de Master, écoles doctorales). Aucune lacune n’empêchait une réponse complète.'}

### Question : Quand et où récupérer mon diplôme après la soutenance ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 3.0/5, Context Precision: 1.0/5

### Question : Y a-t-il des alumni ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 1.0/5

### Question : Comment rester en contact avec l’UT après la thèse ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 3.0/5, Context Precision: 2.0/5
- **Reasoning global** : <<1. **Fidélité (1/5)** : La réponse mentionne un contact (*claire.mirebeau@univ-tours.fr*) **absent du contexte**, et suggère des options (réseaux alumni, newsletters) **non documentées** dans les extraits fournis. Hallucination claire.

2. **Pertinence (3/5)** : La réponse oriente vers le *SRED* (mentionné indirectement dans le contexte via les contacts administratifs), mais manque de précisions actionnables (ex. : liens vers des pages dédiées aux anciens doctorants, si elles existent dans le contexte).

3. **Précision du contexte (2/5)** : Le contexte contient des **coordonnées générales** (ex. : *dsi@univ-tours.fr*, contacts des écoles doctorales) et des **liens intranet** (ex. : [annuaire](https://utnet.univ-tours.fr/fr/annuaire.html)), mais **aucune information explicite** sur les dispositifs post-thèse. Les images et extraits se concentrent sur la *période de thèse* (matériel, soutenance, mobilité), sans aborder l’*after-thèse*.>>

## Query_Mix_08_economy_cross_trials.json

### Question : C’est quoi les SAPS ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend correctement la définition des SAPS et les quatre axes de la stratégie tels que décrits dans le contexte. Cependant, elle introduit un contact (Anne Galopin, af.polytech@univ-tours.fr) qui n’apparaît nulle part dans le contexte fourni, constituant une hallucination. Ainsi, la fidélité n’est pas parfaite.
- **Avis Answer Relevance** : La réponse répond directement à la question « C’est quoi les SAPS ? » en donnant une définition claire et en détaillant les axes de la stratégie, ce qui la rend très pertinente.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires pour répondre à la question : définition, objectifs, axes, et même le lien vers le portail. Le contexte est donc parfaitement ciblé.

### Question : Comment peut-on changer le budget d’un projet ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La majorité des affirmations (contacter le SPIV, l'antenne financière, fournir un argumentaire scientifique et un budget modifié, la condition que l'avenant n'est pas un accord) sont directement présentes dans le contexte. Cependant, le nom « Anne Galopin » et l'adresse e‑mail « af.polytech@univ-tours.fr » n’apparaissent nulle part dans le texte fourni, ce qui constitue une hallucination.
- **Avis Answer Relevance** : La réponse répond précisément à la question « Comment changer le budget d’un projet ? » en décrivant la procédure à suivre, les documents requis et les interlocuteurs, sans digression.
- **Avis Context Precision** : Le contexte récupéré contient toutes les informations nécessaires : mention du SPIV/SPV, de l'antenne financière, des documents à fournir et de la règle sur l'avenant. Ainsi le contexte est parfaitement adapté.

### Question : Quelles sont les différentes démarches à effectuer ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La plupart des informations fournies (contacts de Juliette Piquard, rôle du SPIV, confidentialité, usage du CLE, service de la Commande publique, procédure de sourcing, formulaires d'animaux et de déontologie, liens d'annuaire et de démarches) sont directement présentes dans le contexte. Cependant, le contact "Anne Galopin : af.polytech@univ-tours.fr" n'apparaît pas dans le texte fourni, ce qui constitue une hallucination.
- **Avis Answer Relevance** : La réponse répond clairement à la question en listant les différentes démarches possibles (suivi de projet, protection des résultats, achats/sourcing, éthique/animaux) et en indiquant les interlocuteurs et ressources correspondantes, ce qui correspond exactement à ce qui était demandé.
- **Avis Context Precision** : Le contexte récupéré contient toutes les informations nécessaires pour répondre : contacts, services, procédures, formulaires, liens, etc. Il est donc très précis et complet par rapport à la question.

### Question : - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire extérieur? Est-ce gratuit?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 2.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse indique que Justine Gillet est l’interlocuteur principal pour la question posée. Le contexte ne mentionne jamais que Justine Gillet soit la personne à contacter pour les expérimentations avec un partenaire extérieur ; la ligne correspondante associe cette question à Hélène Jullien. Ainsi, l’affirmation est une hallucination. De plus, la réponse ne mentionne aucune information sur la gratuité, ce qui n’est pas présent dans le contexte.
- **Avis Answer Relevance** : La réponse propose de contacter une chargée d’affaires, mais indique la mauvaise personne et ne répond pas à la partie « Est‑ce gratuit ? ». Elle ne fournit donc pas une réponse adéquate à la question posée.
- **Avis Context Precision** : Le contexte retrouvé contient la question exacte ainsi que les coordonnées de la bonne interlocutrice (Hélène Jullien) et des informations générales sur l’encadrement contractuel des collaborations. Le contexte est donc pleinement pertinent.

### Question : A quelle adresse postale ou mail dois-je envoyer mon projet ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les informations fournies (Anne Galopin, l’adresse e‑mail af.polytech@univ‑tours.fr et Juliette Piquard avec son e‑mail) sont présentes textuellement dans le contexte. Aucun élément n’a été inventé.
- **Avis Answer Relevance** : La question demande l’adresse postale ou e‑mail pour envoyer le projet. La réponse propose deux adresses e‑mail pertinentes, ce qui répond directement à la demande. La mention du laboratoire LIFAT ajoute une précision mais ne rend pas la réponse hors sujet.
- **Avis Context Precision** : Le contexte contient les contacts demandés : Anne Galopin (associée à af.polytech@univ‑tours.fr) et Juliette Piquard (juliette.piquard@univ‑tours.fr). Le contexte fournit également d’autres adresses génériques, mais les informations essentielles sont bien présentes.

### Question : Comment m’inscrire / me réinscrire ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La plupart des étapes décrites (utilisation d'ADUM, création du compte, validation du dossier, date limite du 15 novembre, validation hiérarchique et réception d'un mail) sont directement présentes dans le contexte. Cependant, le contact fourni ("Christele Gaudron-Bredif" et l'email "gaudron@univ-tours.fr") n'apparaît pas dans le texte fourni ; le contexte ne mentionne que "Christèle GAUDRON" sans adresse e‑mail. Cette information est donc hallucination.
- **Avis Answer Relevance** : La réponse répond précisément à la question « Comment m’inscrire / me réinscrire ? » en détaillant la procédure à suivre sur la plateforme ADUM, les étapes de validation et le délai, ce qui correspond exactement à la demande.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires : création et activation du compte ADUM, remplissage du dossier, validation par les différentes instances, date limite du 15 novembre, et mention d'un mail de confirmation. Le texte fourni est donc très pertinent.

### Question : Quelles ressources le Pôle SAPS peut m’apporter ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Les quatre axes présentés (incitation, formation, implication, inspiration) sont directement tirés du contexte. En revanche, la réponse mentionne le laboratoire LIFAT et un interlocuteur nommé Anne Galopin (af.polytech@univ-tours.fr) qui n’apparaissent nulle part dans le contexte fourni. Ces informations sont donc des hallucinations, ce qui fait baisser la note de fidélité.
- **Avis Answer Relevance** : La réponse répond globalement à la question en listant les ressources que le Pôle SAPS peut offrir. Le contenu est pertinent, même si des éléments supplémentaires (LIFAT, Anne Galopin) sont hors sujet.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires pour répondre à la question : la stratégie SAPS et le rôle du Pôle. Le contexte est donc très précis et complet pour la tâche.

### Question : Y a-t-il des alumni ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 1.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement vérifiables dans le contexte : le texte ne mentionne aucun réseau alumni ou association d'anciens diplômés. La réponse ne crée donc aucune information inventée.
- **Avis Answer Relevance** : La réponse répond directement à la question « Y a-t-il des alumni ? » en indiquant que le contexte fourni ne contient aucune information à ce sujet, ce qui est la réponse la plus pertinente compte tenu des données disponibles.
- **Avis Context Precision** : Le contexte récupéré ne comporte aucune information relative aux alumni. Ainsi, il ne fournit pas les données nécessaires pour répondre positivement ou négativement à la question.

### Question : Que propose le Pôle SAPS ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Les quatre axes (Inciter, Former et Informer, Impliquer, Inspirer) sont exactement repris du contexte, ce qui montre une bonne correspondance. En revanche, la réponse ajoute un interlocuteur nommé « Anne Galopin » avec l'adresse e‑mail « af.polytech@univ-tours.fr », qui n'apparaît nulle part dans le contexte fourni. Cette information est donc une hallucination, ce qui empêche d’attribuer le score maximal.
- **Avis Answer Relevance** : La réponse répond directement à la question « Que propose le Pôle SAPS ? » en décrivant les quatre axes de la stratégie du pôle. Aucun élément hors sujet n’est introduit, hormis le contact erroné qui n’affecte pas la pertinence de la partie principale.
- **Avis Context Precision** : Le contexte contient précisément les informations nécessaires (les quatre axes de la stratégie du pôle). Le système a pu les extraire correctement, montrant que le contexte était très pertinent.

### Question : - Qu’est-ce qu’une invention ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 1.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse fournit uniquement un contact (Morgane Guibert, morgane.guibert@univ-tours.fr) qui n'apparaît nulle part dans le contexte fourni. Aucun élément de la réponse n'est traçable dans le texte, ce qui constitue une hallucination complète.
- **Avis Answer Relevance** : La question porte sur la définition d'une invention. La réponse ne donne aucune définition, ni explication, ni information pertinente ; elle se limite à un contact, donc elle ne répond pas du tout à la question.
- **Avis Context Precision** : Le contexte contient plusieurs passages relatifs aux inventions (définition, conditions de brevetabilité, procédure de déclaration, etc.). Ainsi, le contexte était pleinement adéquat pour répondre à la question.

### Question : - Je souhaite répondre à un Appel à projet?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les informations fournies (nom, e‑mail, téléphone de Justine Gillet et Juliette Piquard, ainsi que l’appartenance du laboratoire LIFAT au secteur Sciences et technologies) sont présentes dans le contexte. Aucun élément n’a été inventé.
- **Avis Answer Relevance** : La réponse répond directement à la demande « Je souhaite répondre à un Appel à projet ? » en indiquant les interlocuteurs à contacter pour être accompagné dans la démarche, ce qui est exactement ce que l’utilisateur recherche.
- **Avis Context Precision** : Le contexte récupéré contient les contacts Justine Gillet et Juliette Piquard, leurs coordonnées, ainsi que la mention du laboratoire LIFAT dans le secteur Sciences et technologies. Il fournit donc toutes les informations nécessaires pour répondre à la question.

### Question : je suis en arrêt de travail, qui dois-je contacter ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 2.0/5, Context Precision: 4.0/5
- **Avis Faithfulness** : La réponse mentionne « Anne Galopin » et l’adresse e‑mail af.polytech@univ‑tours.fr ainsi que le « laboratoire LIFAT ». Aucun de ces éléments n’apparaît dans le contexte fourni. Toutes les autres affirmations (liens vers les pages de congés maladie, organigramme DRH) sont présentes, mais la partie principale de la réponse est hallucination.
- **Avis Answer Relevance** : La réponse tente de répondre à la question en indiquant un contact, mais le contact fourni est erroné et n’est pas présent dans le contexte. Elle touche donc le sujet sans fournir l’information correcte, ce qui la rend peu pertinente.
- **Avis Context Precision** : Le contexte contient plusieurs contacts pertinents (Juliette Piquard, Mélanie Fauconnier, spiv@univ‑tours.fr, fsd@univ‑tours.fr) ainsi que des liens vers les procédures de congés maladie. Le contexte est donc pertinent, mais il ne fournit pas le contact indiqué par la réponse.

### Question : Combien de temps va prendre mon inscription ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse indique que le contexte ne précise pas la durée, ce qui est exact. Cependant, elle fournit une adresse e‑mail « gaudron@univ-tours.fr » qui n’apparaît pas dans le contexte (l’adresse correcte est christele.gaudron@univ-tours.fr). Cette information inventée diminue la fidélité.
- **Avis Answer Relevance** : La question porte sur le temps nécessaire à l’inscription. La réponse indique clairement que le délai n’est pas précisé dans le contexte et conseille de contacter le gestionnaire, ce qui répond directement à la demande.
- **Avis Context Precision** : Le contexte contient des informations sur la procédure d’inscription et les contacts, mais aucune indication sur la durée du traitement. Ainsi le contexte est seulement vaguement lié à la question de durée.

### Question : Comment avoir un email ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 2.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : le texte indique bien que le contexte ne contient pas d'information sur la procédure d'obtention d'un email, et l'adresse drv-pi@univ-tours.fr figure dans le contexte. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La question porte sur la façon d'obtenir une adresse email. La réponse indique seulement que le contexte ne le couvre pas et fournit un contact. Elle ne décrit aucune procédure pour créer ou obtenir une adresse email, ce qui la rend peu pertinente.
- **Avis Context Precision** : Le contexte ne fournit pas les informations nécessaires pour répondre à la question « Comment avoir un email ? ». Il ne contient que des informations juridiques et administratives ainsi qu'une adresse de contact, donc il est seulement vaguement lié au sujet.

### Question : - Je souhaite me procurer le formulaire de déclaration d’invention de l’université, à qui dois-je m’adresser ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les informations fournies (Pôle Juridique Recherche et l'adresse email drv-pi@univ-tours.fr) sont présentes dans le contexte. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question en indiquant à qui s'adresser et quel contact utiliser.
- **Avis Context Precision** : Le contexte contient la question identique ainsi que les coordonnées génériques du PJR, ce qui permet de répondre correctement.

### Question : Qui contacter pour toute demande d'ouvrages en service presse ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 2.0/5, Context Precision: 3.0/5
- **Avis Faithfulness** : La réponse introduit des informations qui ne figurent pas dans le contexte : le contact "Anne Galopin" et l'adresse e‑mail af.polytech@univ‑tours.fr sont absents du texte fourni. De plus, l'affirmation que le SPIV gère spécifiquement les "ouvrages en service presse" n'est pas mentionnée dans le contexte. Ainsi, plusieurs affirmations ne sont pas traçables.
- **Avis Answer Relevance** : La réponse tente de répondre à la question en proposant des contacts, mais les contacts fournis sont partiellement erronés et ne correspondent pas exactement à la demande. Elle ne répond donc que partiellement à la question.
- **Avis Context Precision** : Le contexte contient plusieurs contacts pertinents (Morgane Guibert, Juliette Piquard, adresse générique spiv@univ‑tours.fr) ainsi que la mention du Service Partenariats Innovations Valorisation. Cependant, il ne précise pas explicitement le service pour les "ouvrages en service presse", ce qui rend le contexte seulement partiellement précis pour la question.

### Question : comment enregistrer ma demande de formation hors-catalogue et quels documents dois-je fournir ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 2.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse mentionne des éléments qui n’apparaissent nulle part dans le contexte : le nom « Anne Galopin », l’adresse e‑mail « af.polytech@univ‑tours.fr » et le laboratoire « LIFAT ». Aucun de ces contacts n’est présent dans le texte fourni, donc ces informations sont des hallucinations.
- **Avis Answer Relevance** : La réponse tente de répondre à la question en indiquant de contacter les RH, mais elle fournit un contact erroné et ne répond pas à la partie concernant les documents à fournir. Elle est donc peu pertinente.
- **Avis Context Precision** : Le contexte ne contient pas d’instructions précises sur la procédure d’enregistrement d’une formation hors‑catalogue, ni la liste des documents requis. Il ne fournit que des indications générales sur le contact avec la DRH, ce qui montre que le contexte était insuffisant pour répondre correctement.

### Question : Mon jury de thèse est-il valide ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse s’appuie largement sur le contexte (règles de composition du jury, nombre de membres, exigences HDR, rôle des émérites). Cependant, deux éléments ne figurent pas dans le contexte : le contact « Anouk Martinet » (nom et adresse e‑mail) et l’affirmation que l’émérite ne peut jamais être rapporteur, alors que le texte source indique qu’il peut l’être. Ces inventions font baisser la note.
- **Avis Answer Relevance** : La question porte sur la validité du jury de thèse. La réponse fournit les critères précis à vérifier, ce qui répond directement à la demande. Aucun hors‑sujet n’est présent.
- **Avis Context Precision** : Le contexte récupéré contient toutes les informations nécessaires sur la composition du jury, les exigences HDR, la présence d’un émérite, la représentation équilibrée, etc. Il est donc parfaitement ciblé.

### Question : quels types de financement de thèse existent ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)

### Question : - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autre CHRU?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 2.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse introduit des informations qui ne figurent pas dans le contexte : elle mentionne le « laboratoire LIFAT », indique que Justine Gillet (chargée d’affaires Sciences & Matériaux) est la personne à contacter pour des échantillons cliniques, alors que le contexte désigne Claude‑Emmanuel BOUDET (domaine Santé) comme interlocuteur pertinent. Ces affirmations sont donc des hallucinations.
- **Avis Answer Relevance** : La réponse tente de répondre à la question sur les échantillons du CHRU, mais elle oriente l’utilisateur vers la mauvaise personne et le mauvais domaine, ce qui rend la réponse peu pertinente pour le besoin exprimé.
- **Avis Context Precision** : Le contexte récupéré contient bien les informations nécessaires : le tableau indique clairement que Claude‑Emmanuel BOUDET, chargé d’affaires Santé, traite les questions relatives aux projets cliniques et aux échantillons du CHRU. Le contexte est donc très précis.

### Question : Je souhaite monter un projet, comment faire ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend correctement plusieurs éléments du contexte (délai de deux semaines, rôle du SPIV, étapes de prise de contact, validation, documents à fournir, contact Juliette Piquard). Cependant, elle introduit un contact qui n’apparaît pas dans le contexte : « Anne Galopin » avec l’adresse e‑mail af.polytech@univ‑tours.fr. Cette information est donc une hallucination, ce qui fait baisser la note de fidélité.
- **Avis Answer Relevance** : La réponse répond directement à la question « comment monter un projet ? » en décrivant les étapes à suivre et en indiquant les interlocuteurs pertinents. Aucun élément hors sujet n’est présent.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires pour répondre : description du SPIV, procédure en plusieurs étapes, contacts, documents requis, délais, etc. Le système a donc pu s’appuyer sur un contexte très précis.

### Question : - Comment protéger un savoir-faire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les informations fournies (Pôle Juridique Recherche, le nom d'Anouk Martinet et son adresse e‑mail) figurent exactement dans le contexte. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse indique clairement à qui s'adresser pour protéger un savoir‑faire, ce qui répond à la demande de l'utilisateur. Elle ne donne pas de procédure détaillée, mais oriente correctement l'utilisateur vers le service compétent.
- **Avis Context Precision** : Le contexte contient la question « Comment protéger un savoir‑faire ? », la liste des contacts du PJR et le rôle d'Anouk Martinet. Ces éléments sont pleinement exploités.

### Question : Je pars en mission, quelle pièce dois-je remplir ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 3.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse mentionne le contact « Anne Galopin » (af.polytech@univ-tours.fr) qui n’apparaît nulle part dans le contexte fourni. Aucun autre élément de la réponse (par ex. « conformément à nos procédures ») n’est présent dans le texte source. Ainsi, la réponse contient des informations hallucinated, ce qui la pénalise fortement sur ce critère.
- **Avis Answer Relevance** : La question porte sur la pièce à remplir pour une mission. La réponse indique qu’aucune information n’a été trouvée et oriente l’utilisateur vers un contact. Cette orientation est partiellement pertinente, mais le contact fourni est erroné, ce qui diminue la pertinence globale.
- **Avis Context Precision** : Le contexte contient des listes de documents requis pour les soumissions de projets (accord de confidentialité, dossier scientifique, etc.) et plusieurs contacts universitaires, mais aucune indication précise sur le formulaire ou la pièce à fournir pour une « mission ». Le contexte est donc seulement vaguement lié à la question.

### Question : Quel est le délai moyen entre la soumission d’un manuscrit et sa publication ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 1.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse fournit un contact (Christele Gaudron-Bredif : gaudron@univ-tours.fr) qui n’apparaît pas dans le contexte fourni. De plus, aucune information du contexte n’est utilisée pour répondre à la question, ce qui constitue une hallucination majeure.
- **Avis Answer Relevance** : La question porte sur le délai moyen entre la soumission d’un manuscrit et sa publication. La réponse ne mentionne aucun délai, mais donne uniquement un contact, donc elle ne répond pas du tout à la question.
- **Avis Context Precision** : Le contexte traite principalement des procédures de dépôt de thèse, des délais de dépôt avant la soutenance (ex. : dépôt au moins 7 semaines avant la soutenance) et des formalités administratives. Aucun élément du contexte ne fournit le délai moyen entre soumission d’un manuscrit et publication, ce qui rend le contexte peu pertinent pour la question.

## Query5_rag_batch_trials.json

### Question : Que faire dès que mon projet a été accepté ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5

### Question : Comment se passe l’ouverture des crédits ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 4.0/5, Context Precision: 2.0/5

### Question : Je souhaite demander la prolongation de mon projet. Commet dois-je faire ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 4.0/5
- **Avis Faithfulness** : {'score': 4, 'explanation': "La réponse s'appuie majoritairement sur le contexte fourni (procédure SPIV, rôle de Juliette Piquard, nécessité d'un argumentaire scientifique, etc.). Cependant, elle mentionne *LIFAT* (laboratoire non cité dans le contexte) et *Anne Galopin* (contact absent du contexte), ce qui introduit des éléments non vérifiables dans les sources. Ces ajouts minimes justifient un **4/5** plutôt qu'un 5/5."}
- **Avis Answer Relevance** : {'score': 5, 'explanation': "La réponse est **directement utile** : elle détaille la procédure exacte pour une prolongation (contact SPIV, argumentaire, attente de validation), avec des étapes claires et des contacts précis. Elle couvre parfaitement la question posée (*'Comment demander une prolongation ?'*)."}
- **Avis Context Precision** : {'score': 4, 'explanation': "Le contexte contient **toutes les informations critiques** pour répondre (rôle du SPIV, procédure d'avenant, contacts par secteur, besoin d'un argumentaire). Cependant, il est dispersé sur plusieurs pages (ex. : règles SPIV en page 27, contacts en page 28), ce qui rend l'extraction moins immédiate. D'où un **4/5** plutôt que 5/5."}

### Question : Comment peut-on changer le budget d’un projet ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5

### Question : Je suis nouveau MCF, à quelle date aurais-je les crédits ? A quoi puis-je utiliser les crédits ? Qu’est ce que j’ai le droit de faire avec ces crédits ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 1.0/5
- **Avis Faithfulness** : {'score': 5, 'explanation': 'La réponse ne contient aucune information non sourcée ou inventée. Elle reconnaît explicitement l’absence de données dans le contexte fourni et oriente vers des contacts institutionnels pertinents (service financier, PJR). Aucune hallucination ou extrapolation non justifiée.'}
- **Avis Answer Relevance** : {'score': 4, 'explanation': 'La réponse est globalement pertinente : elle identifie correctement l’absence de réponse dans le contexte et propose une démarche proactive (contacter les services compétents). Cependant, elle ne reformule pas explicitement les 3 sous-questions de l’utilisateur (date, usages, droits), ce qui aurait pu améliorer la clarté. D’où un 4/5 plutôt que 5/5.'}
- **Avis Context Precision** : {'score': 1, 'explanation': 'Le contexte fourni ne contient **aucune information** sur les crédits des MCF (dates, usages, règles). Il traite uniquement de propriété intellectuelle, contrats, et éméritat – des sujets sans lien avec la question posée. Le score est donc minimal (1/5), car le contexte était *totalement inapproprié* pour répondre.'}

### Question : Je dois justifier scientifiquement mon projet, quelle est la trame à utiliser ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 2.0/5, Context Precision: 1.0/5
- **Reasoning global** : "faithfulness" = 1 : La réponse invente une personne (Marie PERAULT) et une adresse email non présentes dans le contexte, ce qui constitue une **hallucination claire** et une infidélité totale aux sources fournies.

"answer_relevance" = 2 : La réponse tente d’adresser la question (demande de trame), mais la solution proposée (contacter une personne fictive) est **inutile et trompeuse**, même si le ton est orienté vers l’action.

"context_precision" = 1 : Le contexte **ne contient aucune information** sur la trame de justification scientifique ou un contact dédié. Il liste seulement des questions fréquentes sans réponses associées, rendant impossible une réponse fidèle basée sur ces données.

### Question : Je souhaite monter un projet, comment faire ?
- **Erreur d'évaluation** : Parsing JSON / Evaluation failed: Expecting value: line 1 column 1 (char 0)

### Question : Je souhaite recruter un CDD, comment dois-je faire ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 3.0/5, Context Precision: 3.0/5
- **Avis Faithfulness** : {'score': 2, 'explanation': 'La réponse contient des **informations non présentes dans le contexte** (ex: mention de *Juliette Piquard* comme contact pour le LIFAT, alors que le contexte associe son secteur aux *Sciences et Technologies* sans préciser le LIFAT. L’email *af.polytech@univ-tours.fr* et le nom *Anne Galopin* sont **absents du contexte**. La référence à un document *règles CDD BIATSS 2026* est **inventée** (le contexte cite des règles de 2019/2020).'}
- **Avis Answer Relevance** : {'score': 3, 'explanation': 'La réponse aborde **partiellement** la question en citant des étapes utiles (contact DRH, niveaux de diplôme, documents), mais **manque de précision** sur les spécificités du CDD (durée, motifs légaux, grilles indiciaires PPCR 2019 mentionnées dans le contexte). Les liens vers des ressources génériques (*nouveaux arrivants*, *carte multiservices*) sont **peu pertinents** pour une question ciblée sur le *processus de recrutement*.'}
- **Avis Context Precision** : {'score': 3, 'explanation': "Le contexte contient des **éléments utiles** (niveaux de diplôme par catégorie, mention des grilles PPCR 2019, lien vers *'Je recrute un nouvel agent'*), mais il est **incomplet** : aucune procédure détaillée pour un CDD n’y est décrite (ex: motifs de recours, durée maximale, formalités administratives). Les informations sont **éparpillées** (ex: règles de 2020 mélangées à des mises à jour de 2024 sans cohérence). Les contacts mentionnés (Juliette Piquard, Mélanie Fauconnier) sont **limités à l’accompagnement carrière**, pas au recrutement."}

### Question : Je souhaite organiser un colloque, comment dois-je faire ?
- **Erreur d'évaluation** : HTTPSConnectionPool(host='llm.ilaas.fr', port=443): Read timed out. (read timeout=30)

### Question : Je pars en mission, quelle pièce dois-je remplir ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 2.0/5, Context Precision: 1.0/5

### Question : Je souhaite demander une aide à la commission recherche pour un appel à projet, quand dois-je demander et quelles pièces fournir ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 4.0/5

## Query_Mix_07_qwen_mono_trials.json

### Question : C’est quoi les SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : définition des SAPS, lien avec la loi LPR 2021, objectifs de rapprochement chercheurs‑citoyens, reconnaissance de la dimension science‑société, collaboration avec la CSTI, site saps.univ‑tours.fr et le contact Alice NUÉ avec son e‑mail. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question « C’est quoi les SAPS ? » en donnant une définition claire, les objectifs et le cadre institutionnel, ce qui constitue une réponse pleinement pertinente.
- **Avis Context Precision** : Le contexte fourni contenait toutes les informations nécessaires (définition, cadre légal, objectifs, lien avec l’Université de Tours, site web et contacts). Il était donc parfaitement ciblé.

### Question : Comment peut-on changer le budget d’un projet ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La plupart des affirmations (contacter le SPIV, passer par l'Antenne Financière, fournir un argumentaire scientifique et un budget modifié) sont directement présentes dans le contexte. Cependant, le nom "Anne Galopin" et l'adresse e‑mail "af.polytech@univ-tours.fr" n’apparaissent nulle part dans le texte fourni, ce qui constitue une hallucination.
- **Avis Answer Relevance** : La réponse répond précisément à la question « Comment changer le budget d’un projet ? » en décrivant la procédure, les documents requis et les interlocuteurs, sans digression.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires pour répondre : procédure de modification budgétaire, rôle du SPIV/SPV, rôle de l'Antenne Financière, documents à fournir. Ainsi le contexte est très pertinent.

### Question : Quelles sont les différentes démarches à effectuer ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 1.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse mentionne un contact (Guillaume Fialeix, guillaume.fialeix@univ-tours.fr) qui n’apparaît nulle part dans le contexte fourni. Aucun autre élément de la réponse ne peut être rattaché au texte source, ce qui constitue une hallucination totale.
- **Avis Answer Relevance** : La question demande les différentes démarches à effectuer. La réponse ne fournit qu’un seul contact et ne décrit aucune démarche (envoi de dossier, pièces à fournir, etc.). Elle ne répond donc pas du tout à la question.
- **Avis Context Precision** : Le contexte récupéré contient plusieurs sections détaillant les démarches à suivre (ex. envoi du dossier par mail, lettres de demande et d’appui, tableau budgétaire, programme du colloque, choix entre réservation par le laboratoire ou versement direct, etc.). Le contexte est donc très pertinent et complet pour répondre à la question.

### Question : - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire extérieur? Est-ce gratuit?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 3.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse indique que l’interlocuteur est Justine Gillet (email justine.gillet@univ-tours.fr). Or, le contexte associe la question « Dans quel cadre puis-je réaliser des expérimentations avec un partenaire extérieur? Est‑ce gratuit? » à Hélène Jullien, dont les coordonnées sont helene.jullien@univ-tours.fr et 0247367993. Aucun élément du contexte ne mentionne Justine Gillet comme contact pour ce sujet, donc cette information est hallucination. De plus, la réponse ne mentionne pas le caractère gratuit ou non de la démarche, information qui figure implicitement dans le contexte (exigence d’un cadre contractuel).
- **Avis Answer Relevance** : La réponse répond partiellement à la question en indiquant qu’il faut contacter une Chargée d’Affaires, mais elle ne répond pas à la partie concernant la gratuité et fournit un contact erroné. Elle est donc seulement partiellement pertinente.
- **Avis Context Precision** : Le contexte récupéré contient la question exacte, les coordonnées d’Hélène Jullien ainsi que des informations générales sur l’encadrement contractuel des collaborations. Le contexte est donc pleinement pertinent et complet pour répondre à la question.

### Question : A quelle adresse postale ou mail dois-je envoyer mon projet ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 3.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse mentionne Anne Galopin et l'adresse e‑mail af.polytech@univ‑tours.fr, qui n’apparaissent nulle part dans le contexte fourni. Seul le mail de Juliette Piquard est présent dans le contexte. La présence d’informations non‑documentées constitue une hallucination, ce qui réduit fortement la fidélité.
- **Avis Answer Relevance** : La réponse fournit bien des adresses e‑mail, ce qui répond partiellement à la question « à quelle adresse postale ou mail ». Cependant, elle inclut un contact erroné et ne mentionne pas l’adresse générique du service, ce qui rend la pertinence moyenne.
- **Avis Context Precision** : Le contexte contient plusieurs adresses e‑mail pertinentes (juliette.piquard@univ‑tours.fr, melanie.fauconnier@univ‑tours.fr, spiv@univ‑tours.fr, etc.). Il est donc très précis et fournit les informations nécessaires pour répondre à la question.

### Question : Comment m’inscrire / me réinscrire ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend la plupart des informations présentes dans le contexte (utilisation d'ADUM, dépôt d'un PDF unique, validation séquentielle, réception d'un mail, date limite du 15 novembre). Cependant le nom et l'adresse e‑mail du contact sont erronés : le contexte cite « Christèle Gaudron » avec l’adresse « christele.gaudron@univ-tours.fr », alors que la réponse indique « Christele Gaudron‑Bredif » et « gaudron@univ-tours.fr ». Ces éléments n’apparaissent pas dans le contexte, ce qui constitue une hallucination.
- **Avis Answer Relevance** : La réponse répond directement à la question « Comment m’inscrire / me réinscrire ? » en décrivant la procédure à suivre, les étapes de validation et le délai, ce qui correspond exactement à la demande.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires pour répondre : procédure ADUM, dépôt d’un PDF unique, validation par les différentes instances, date limite, et contacts. Le système a pu extraire ces éléments, donc le contexte est très précis.

### Question : Quelles ressources le Pôle SAPS peut m’apporter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : missions d’accompagnement, formations, événements, projets arts/sciences, contacts (Alice NUE) et le lien du site. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond précisément à la question « Quelles ressources le Pôle SAPS peut‑moi apporter ? » en listant les services et ressources disponibles, sans digression.
- **Avis Context Precision** : Le contexte fourni contient l’ensemble des informations nécessaires (missions, formations, événements, projets, contacts). Il a été correctement exploité pour générer la réponse.

### Question : Y a-t-il des alumni ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse se contente d'affirmer que le contexte fourni ne mentionne aucune information sur un réseau d'anciens étudiants ou une association "alumni". Cette affirmation est directement vérifiable dans le texte fourni, qui ne contient aucun passage relatif aux alumni. Aucun élément n'est ajouté de façon inventée.
- **Avis Answer Relevance** : La question porte sur l'existence d'alumni. La réponse répond directement en indiquant que le contexte ne fournit aucune information à ce sujet, ce qui correspond exactement à ce qui est demandé.
- **Avis Context Precision** : Le contexte récupéré porte sur les libertés, les procédures d'association, la sécurité, etc., et ne contient aucune donnée concernant les alumni. Ainsi, le contexte n'est pas pertinent pour répondre à la question, ce qui justifie un faible score.

### Question : Que propose le Pôle SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : les trois missions du Pôle SAPS (répondre aux sollicitations, organiser des rencontres, accompagner les chercheurs), les exemples d'événements (DéTours des sciences, Ma thèse en 180 s, Village des sciences, festival (Re)Cherche et trouve), les services de conseil (dépôt de projets ANR, APR‑IR, projets européens) et les formations, ainsi que le contact d'Alice NUÉ et le site saps.univ-tours.fr. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question « Que propose le Pôle SAPS ? » en listant les offres et services du pôle, avec des détails pertinents et utiles.
- **Avis Context Precision** : Le contexte fourni contient l’ensemble des informations nécessaires (missions, événements, formations, contacts, site web). Il a été correctement exploité.

### Question : - Qu’est-ce qu’une invention ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 2.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : le PJR est bien indiqué comme le service compétent et l'adresse e‑mail drv-pi@univ-tours.fr figure dans la section des contacts. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La question demande la définition d’une invention. La réponse ne fournit pas cette définition, elle se contente de rediriger vers un contact, ce qui ne répond pas directement à la demande.
- **Avis Context Precision** : Le contexte contient la question « Qu’est‑ce qu’une invention ? » mais ne fournit pas la réponse attendue (définition, critères, etc.). Le contexte est donc seulement vaguement lié, sans les informations nécessaires pour répondre.

### Question : - Je souhaite répondre à un Appel à projet?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte. Juliette Piquard et Justine Gillet ainsi que leurs adresses e‑mail apparaissent dans le texte fourni, de même que le lien avec le laboratoire LIFAT et le rôle du SPIV.
- **Avis Answer Relevance** : La réponse répond directement à la demande « Je souhaite répondre à un Appel à projet ? » en indiquant les interlocuteurs à contacter, ce qui constitue une réponse pertinente et utile.
- **Avis Context Precision** : Le contexte récupéré contient les informations nécessaires (contacts, secteurs, laboratoire LIFAT) pour répondre à la question, et la réponse les utilise exactement.

### Question : je suis en arrêt de travail, qui dois-je contacter ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 3.0/5, Context Precision: 4.0/5
- **Avis Faithfulness** : La réponse mentionne un contact nommé « Aurélie PETEREAU » avec l'adresse e‑mail aurelie.petereau@univ‑tours.fr. Aucun de ces éléments n'apparaît dans le contexte fourni, qui ne cite aucun nom ni adresse e‑mail. Ainsi, la plupart des affirmations de la réponse sont hallucinations.
- **Avis Answer Relevance** : La réponse répond à la question en proposant un interlocuteur, mais comme cet interlocuteur n'est pas présent dans le contexte, la pertinence est partielle. Elle ne fournit pas les informations génériques présentes dans le contexte (gestionnaire DRH, organigramme, etc.).
- **Avis Context Precision** : Le contexte contient bien l'information générale selon laquelle il faut prendre contact avec un gestionnaire de la DRH et consulter l’organigramme. Il ne fournit pas de contact précis, mais il est pertinent pour la question. Il manque toutefois le détail d’un nom ou d’une adresse e‑mail, d’où la note 4.

### Question : Combien de temps va prendre mon inscription ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse indique que le contexte ne précise pas la durée de traitement, ce qui est exact. Cependant, elle ajoute un contact (Guillaume Fialeix, guillaume.fialeix@univ-tours.fr) qui n'apparaît pas dans le contexte fourni, constituant une hallucination.
- **Avis Answer Relevance** : La réponse répond directement à la question en expliquant l'absence d'information sur la durée et en proposant une démarche pour obtenir la réponse, ce qui est pleinement pertinent.
- **Avis Context Precision** : Le contexte fourni ne contient aucune indication sur le temps nécessaire à l'inscription, il ne permet donc pas de répondre précisément à la question. Le contexte est donc peu pertinent pour la durée demandée.

### Question : Comment avoir un email ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 3.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse se retrouvent dans le contexte : l'existence d'un compte mail Zimbra pour chaque usager, la nécessité de se connecter via les services numériques de l'université, et le contact d'assistance dsi@univ-tours.fr. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond partiellement à la question « Comment avoir un email ? ». Elle indique que l'utilisateur possède déjà un compte Zimbra et indique où obtenir de l'aide, mais ne décrit pas les étapes concrètes pour créer ou récupérer une adresse mail, ce qui était attendu.
- **Avis Context Precision** : Le contexte fourni contient les informations nécessaires : chaque usager bénéficie d'un compte Zimbra, il existe une rubrique dédiée à la messagerie Zimbra, et le contact dsi@univ-tours.fr est indiqué. Le contexte est donc très pertinent.

### Question : - Je souhaite me procurer le formulaire de déclaration d’invention de l’université, à qui dois-je m’adresser ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend correctement le rôle du SPIV et la présence de Morgane Guibert dans le contexte. Cependant, elle introduit un interlocuteur nommé Justine Gillet avec son adresse e‑mail, qui n’apparaît nulle part dans le contexte fourni, constituant une hallucination. Le reste des informations (formulaire sur l’intranet, recommandation du cahier de laboratoire) est présent dans le contexte.
- **Avis Answer Relevance** : La réponse répond à la question en indiquant à qui s’adresser pour le formulaire, en mentionnant le SPIV et un contact. Elle ajoute des informations supplémentaires (cahier de laboratoire) qui ne sont pas demandées mais ne nuisent pas à la pertinence globale.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires : le rôle du SPIV dans les déclarations d’invention, le formulaire à venir sur l’intranet, et les coordonnées de Morgane Guibert. Ainsi le contexte est pleinement pertinent.

### Question : Qui contacter pour toute demande d'ouvrages en service presse ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 2.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse mentionne un contact (Jeanne Hélouis, jeanne.helouis@univ-tours.fr) qui n'apparaît nulle part dans le contexte fourni. Aucun élément du contexte ne justifie cette information, donc la réponse hallucine ces données.
- **Avis Answer Relevance** : La question porte sur le contact à joindre pour des demandes d'ouvrages en service presse. La réponse donne un contact, mais comme il n'est pas présent dans le contexte et n'est pas clairement lié à la notion de "service presse", la pertinence est très faible.
- **Avis Context Precision** : Le contexte ne contient aucune information sur un contact spécifique pour le service presse, ni même sur le service presse lui‑même. Le contexte fourni porte sur des dispositions légales, le Pôle Juridique Recherche, etc., qui ne répondent pas directement à la question.

### Question : comment enregistrer ma demande de formation hors-catalogue et quels documents dois-je fournir ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement tirées du contexte : la procédure via ADUM, la rubrique "déclaration des formations hors-catalogue", les informations à renseigner, la nécessité de joindre la fiche de validation et les justificatifs, le format PDF unique, ainsi que le contact Guillaume Fialeix avec son e‑mail. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question en expliquant comment enregistrer la demande de formation hors‑catalogue et quels documents fournir, sans digression.
- **Avis Context Precision** : Le contexte fourni contient les instructions détaillées pour la déclaration hors‑catalogue, la liste des pièces à joindre et le contact de Guillaume Fialeix. Il est donc parfaitement ciblé.

### Question : Mon jury de thèse est-il valide ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement tirées du contexte fourni : nombre de membres (4‑8), moitié de professeurs/HDR, moitié extérieurs, présence d’au moins un HDR, limite de deux membres invités, rôle des membres invités, limitation d’un seul membre émérite, procédure de désignation et d’autorisation, évaluation au cas‑par‑cas par le directeur/adjoint de l’ED. Aucun élément n’est ajouté ou inventé.
- **Avis Answer Relevance** : La question « Mon jury de thèse est‑il valide ? » demande les critères de validité. La réponse décrit précisément ces critères et la procédure de validation, permettant à l’utilisateur de vérifier la validité de son jury. Elle répond donc pleinement à la demande.
- **Avis Context Precision** : Le contexte contient l’ensemble des règles nécessaires (composition, nombre, statut, extériorité, invités, émérites, procédure de désignation, rôle du président, etc.). Le système a récupéré ces informations de façon exacte.

### Question : quels types de financement de thèse existent ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend correctement les trois grands types de financement présents dans le contexte (financement interne, sur projet, sur contrat de recherche/CIFRE). Cependant, elle introduit un contact qui n’apparaît pas dans le contexte : Anne Galopin (af.polytech@univ-tours.fr). Cette information est donc une hallucination, ce qui empêche d’attribuer la note maximale.
- **Avis Answer Relevance** : La question porte sur les types de financement de thèse. La réponse liste les trois catégories attendues et fournit même des exemples concrets (CIFRE, appels régionaux, nationaux, européens). Elle répond donc de façon ciblée et exhaustive, même si elle ajoute des contacts non demandés.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires : financement interne (mentionné même si le détail est absent), financement sur projet avec les trois guichets, et financement sur contrat de recherche incluant les thèses CIFRE. Le texte récupéré est donc parfaitement pertinent.

### Question : - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autre CHRU?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 2.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse indique que Justine Gillet est l’interlocutrice à contacter pour les échantillons du CHRU. Dans le contexte, Justine Gillet apparaît dans la catégorie Sciences et matériaux avec des questions différentes, mais aucune mention n’est faite qu’elle gère les projets cliniques ou les échantillons du CHRU. Cette affirmation n’est donc pas traçable dans le contexte, ce qui constitue une hallucination. Les coordonnées de Justine sont présentes dans le contexte, mais leur utilisation pour ce sujet est erronée.
- **Avis Answer Relevance** : La question porte spécifiquement sur l’utilisation d’échantillons provenant du CHRU de Tours ou d’un autre CHRU. La réponse propose un contact qui n’est pas pertinent pour ce type de demande, ne répond donc pas réellement à la question posée.
- **Avis Context Precision** : Le contexte récupéré contient la ligne de Claude‑Emmanuel BOUDET, qui inclut exactement la question sur les échantillons du CHRU, ainsi que ses coordonnées. Le contexte est donc parfaitement pertinent et complet pour répondre à la question.

### Question : Je souhaite monter un projet, comment faire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement tirées du contexte fourni : contact du service SCRIPT, contenu du dossier de soumission, délai de 15 jours avant la commission, disponibilité du coordonnateur/chef de projet, transmission de l'avis du COPIL sous 48 h, et l’adresse e‑mail de Mme Caroline Vaslin. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond précisément à la question « Je souhaite monter un projet, comment faire ? » en décrivant les étapes concrètes à suivre. Aucun hors‑sujet n’est introduit, à l’exception d’une note optionnelle sur l’appel 2026 qui reste pertinente.
- **Avis Context Precision** : Le contexte récupéré contenait l’ensemble des informations nécessaires (procédure de validation, rôle du service SCRIPT, pièces du dossier, délais, présentation au COPIL). Il était donc parfaitement ciblé.

### Question : - Comment protéger un savoir-faire ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La majorité des affirmations (confidentialité, rôle du SPIV, utilisation du cahier de laboratoire, mesures PPST) sont directement tirées du contexte. Cependant, la réponse introduit le "laboratoire LIFAT" et le contact "Justine Gillet" avec son e‑mail, qui n’apparaissent nulle part dans le texte fourni. Ces éléments constituent des hallucinations, ce qui empêche d’attribuer la note maximale.
- **Avis Answer Relevance** : La réponse répond clairement à la question « Comment protéger un savoir‑faire ? » en proposant des mesures concrètes (confidentialité, accords NDA, accompagnement SPIV, PPST, bonnes pratiques numériques et physiques). Aucun hors‑sujet n’est présent.
- **Avis Context Precision** : Le contexte récupéré contient toutes les informations nécessaires pour répondre à la question : exigences de confidentialité, rôle du SPIV, importance du cahier de laboratoire, cadre PPST, etc. Le texte est donc très pertinent.

### Question : Je pars en mission, quelle pièce dois-je remplir ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 2.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse indique qu'aucune information sur le formulaire de mission n'est présente, ce qui est correct. Cependant, elle ajoute un contact nommé Anne Galopin avec l'email af.polytech@univ-tours.fr, qui n'apparaît pas du tout dans le contexte fourni. Cette information est donc hallucination, ce qui fait baisser la note de fidélité.
- **Avis Answer Relevance** : La réponse tente de répondre à la question en indiquant l'absence d'information et en proposant un contact. Le contact étant erroné, la réponse n'apporte pas réellement la solution recherchée, ce qui la rend peu pertinente.
- **Avis Context Precision** : Le contexte fourni ne contient pas de formulaire spécifique pour une mission, mais il comporte des contacts (Juliette Piquard, Mélanie Fauconnier, spiv@univ-tours.fr, fsd@univ-tours.fr) et une liste de documents liés aux projets de recherche. Le contexte est donc seulement vaguement lié à la question.

### Question : Quel est le délai moyen entre la soumission d’un manuscrit et sa publication ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 1.0/5, Context Precision: 3.0/5
- **Avis Faithfulness** : La réponse fournit uniquement un contact (Jeanne Hélouis, jeanne.helouis@univ-tours.fr) qui n’apparaît nulle part dans le contexte fourni. Aucun élément de la réponse ne peut être retracé dans le texte source, ce qui constitue une hallucination complète.
- **Avis Answer Relevance** : La question porte sur le délai moyen entre la soumission d’un manuscrit et sa publication. La réponse ne mentionne aucun délai, mais donne un contact, ce qui ne répond pas du tout à la question.
- **Avis Context Precision** : Le contexte contient des informations sur les délais légaux d’accès ouvert (maximum 6 mois pour les sciences, 12 mois pour les SHS) et d’autres sections relatives à la soumission, mais il ne fournit pas explicitement le « délai moyen » demandé. Le contexte est donc partiellement utile, mais ne répond pas directement à la question.

## Query_Mix_01_baseline_trials.json

### Question : C’est quoi les SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement soutenues par le texte fourni : définition des SAPS, cadre législatif (loi LPR 2021), rôle du ministère, objectifs de rapprochement et de dialogue, reconnaissance de la médiation scientifique, exemples de co‑construction avec des acteurs non académiques, formations, événements (DéTours des sciences, Ma thèse en 180 s, festival (Re)Cherche et trouve) et le site web. Le contact d'Alice NUÉ et son e‑mail figurent également dans le contexte. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond précisément à la question « C’est quoi les SAPS ? » en donnant une définition claire et en illustrant le fonctionnement du dispositif, notamment à l'Université de Tours. Aucun hors‑sujet n’est présent.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires pour définir les SAPS : leur sigle, leur ancrage législatif, leurs objectifs, leurs missions et leurs actions concrètes. Le texte récupéré est donc parfaitement ciblé.

### Question : Comment peut-on changer le budget d’un projet ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse introduit des éléments qui n’apparaissent pas dans le contexte : le nom « Anne Galopin », l’adresse e‑mail af.polytech@univ‑tours.fr et la mention du laboratoire LIFAT sont absents du texte fourni. Ces informations sont donc des hallucinations. Le reste du processus (argumentaire scientifique, budget modifié, contact du SPV/SPIV et de l’antenne financière, attente de validation du financeur) est bien présent dans le contexte.
- **Avis Answer Relevance** : La réponse répond à la question en décrivant les étapes pour modifier le budget d’un projet : préparation des documents, transmission de la demande, validation du financeur. Elle reste globalement pertinente même si elle ajoute un contact précis qui n’est pas demandé.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires : il indique qu’il faut contacter le SPV et l’antenne financière, fournir un argumentaire scientifique et un budget modifié, et attendre l’accord du financeur. Le contexte est donc très précis pour répondre à la question.

### Question : Quelles sont les différentes démarches à effectuer ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 2.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse ne cite aucune information précise du contexte. Elle se contente d’une phrase d’introduction générique « Voici les démarches à effectuer… » qui n’apparaît pas dans le texte fourni. Aucun détail des étapes n’est présenté, donc la plupart des affirmations ne sont pas traçables dans le contexte.
- **Avis Answer Relevance** : La question demande les différentes démarches à effectuer. La réponse ne fournit aucune démarche concrète, se limitant à une introduction vide. Elle ne répond donc pas réellement à la demande.
- **Avis Context Precision** : Le contexte contient une description détaillée de la procédure d’inscription (création de compte ADUM, pièces à fournir, assemblage en PDF, validation par les différentes directions, contacts, etc.). Ainsi le contexte était très pertinent et complet pour répondre à la question.

### Question : - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire extérieur? Est-ce gratuit?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse introduit des éléments qui ne figurent pas dans le contexte : la mention du LIFAT (absent du texte) et la recommandation de contacter Justine Gillet, alors que le contexte indique que la question relève de Hélène Jullien et fournit ses coordonnées. Ces informations sont donc hallucinées. Le reste du contenu (SPIV, besoin d’un contrat) est présent dans le contexte.
- **Avis Answer Relevance** : La réponse traite bien de la nécessité d’un encadrement contractuel et de la question de gratuité, ce qui correspond à la demande. Cependant, le mauvais interlocuteur proposé diminue légèrement la pertinence globale.
- **Avis Context Precision** : Le contexte récupéré contient la question exacte, les coordonnées de Hélène Jullien ainsi que des informations sur le SPIV et les exigences contractuelles. Il est donc pleinement pertinent pour répondre à la question.

### Question : A quelle adresse postale ou mail dois-je envoyer mon projet ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les informations fournies (adresse e‑mail de Juliette Piquard, son rôle pour le secteur Sciences et Technologies incluant LIFAT, le contact de Justine Gillet, la procédure du "Starter Pack") sont présentes textuellement dans le contexte. Aucun élément n’a été inventé.
- **Avis Answer Relevance** : La réponse indique clairement l’adresse e‑mail à laquelle envoyer le projet, ce qui répond directement à la question. Les informations supplémentaires (procédure, autre contact) restent pertinentes au sujet du dépôt de projet.
- **Avis Context Precision** : Le contexte contient l’e‑mail juliette.piquard@univ-tours.fr ainsi que son domaine d’intervention, ainsi que d’autres contacts utiles. Le système a donc exploité le bon extrait du contexte.

### Question : Comment m’inscrire / me réinscrire ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La plupart des étapes décrites (accord du directeur, création de compte ADUM, dépôt d’un PDF, validation par la direction, réception d’un mail) sont présentes dans le contexte. Cependant, le nom "Christele Gaudron-Bredif" et l’adresse e‑mail "gaudron@univ-tours.fr" n’apparaissent pas dans le texte fourni (l’e‑mail correct est christele.gaudron@univ-tours.fr). Ces légères inexactitudes constituent une hallucination, d’où la note 4.
- **Avis Answer Relevance** : La réponse répond directement à la question « Comment m’inscrire / me réinscrire ? » en détaillant la procédure d’inscription en première année et la réinscription en années suivantes, ainsi que les contacts utiles. Aucun élément hors sujet n’est ajouté.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires : procédures ADUM, pièces à fournir, dates limites, validation par les directions, et contacts. Le système a pu extraire ces données, justifiant la note maximale.

### Question : Quelles ressources le Pôle SAPS peut m’apporter ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La plupart des affirmations de la réponse sont directement présentes dans le contexte (accompagnement de projets, formations, événements, ressources en ligne, liens). Un seul élément n’est pas mentionné dans le texte fourni : le « prêt de matériel » pour animations et expositions, ce qui constitue une hallucination mineure.
- **Avis Answer Relevance** : La réponse répond précisément à la question en listant les différentes ressources que le Pôle SAPS peut offrir (accompagnement, formations, événements, outils en ligne). Aucun hors‑sujet n’est introduit.
- **Avis Context Precision** : Le contexte récupéré contient toutes les informations nécessaires : missions du pôle, description des formations, des événements, des projets arts/sciences, des contacts et des liens web. Il est donc parfaitement ciblé.

### Question : Y a-t-il des alumni ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse affirme ne pas avoir trouvé d'information sur les alumni, ce qui correspond au fait que le contexte ne mentionne aucun alumni. Cependant, elle suggère de contacter le "service de la communication" et la "Direction des Relations Internationales", contacts qui n'apparaissent pas dans le contexte fourni, constituant ainsi des informations inventées.
- **Avis Answer Relevance** : La réponse répond directement à la question "Y a-t-il des alumni ?" en indiquant l'absence d'information et en proposant des pistes de recherche, ce qui est pleinement pertinent.
- **Avis Context Precision** : Le contexte récupéré ne contient aucune information relative aux alumni ou à un réseau d'anciens étudiants. Il porte sur des services, des contacts et des programmes internes, donc il n'est pas pertinent pour répondre à la question.

### Question : Que propose le Pôle SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte ou sont des reformulations directes. Les missions, les événements (DéTours des sciences, Ma thèse en 180s, Fête de la science, etc.), les formations, le label Teepee, les contacts et les liens web figurent exactement dans le texte fourni. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond précisément à la question « Que propose le Pôle SAPS ? » en listant les services, les événements, les formations, les accompagnements et les ressources proposées. Aucun hors‑sujet n’est introduit.
- **Avis Context Precision** : Le contexte récupéré contient l’ensemble des informations nécessaires : missions du pôle, description des activités, exemples d’événements, formations, projets arts/sciences, label Teepee, contacts et site web. Il est donc parfaitement ciblé.

### Question : - Qu’est-ce qu’une invention ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 4.0/5, Context Precision: 3.0/5
- **Avis Faithfulness** : La réponse introduit une définition de l'invention (solution technique nouvelle, critères de nouveauté, activité inventive, brevetabilité, référence au CPI) qui n'apparaît nulle part dans le contexte fourni. Ces informations sont donc des hallucinations. En revanche, le contact e‑mail drv-pi@univ-tours.fr est bien présent dans le contexte, ce qui montre que la réponse n'est pas totalement hors sujet, d'où une note de 2.
- **Avis Answer Relevance** : La question porte sur la définition d’une invention. La réponse fournit une définition générique et indique un point de contact pour plus de précision, ce qui répond directement à la demande. Quelques éléments supplémentaires (invitation à contacter le PJR) sont présents mais restent pertinents, justifiant une note de 4.
- **Avis Context Precision** : Le contexte traite principalement du régime juridique des créateurs indépendants, des structures d’accueil et des dispositions légales relatives aux inventions, mais il ne contient pas de définition claire d’une invention. Le contexte est donc partiellement utile, d'où une note de 3.

### Question : - Je souhaite répondre à un Appel à projet?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les informations fournies dans la réponse (nom, fonction, secteur, adresse e‑mail) sont présentes dans le contexte. Aucun élément n’a été inventé.
- **Avis Answer Relevance** : La réponse propose un interlocuteur pour aider à répondre à un appel à projet, ce qui correspond à la demande. Cependant, elle introduit une hypothèse non mentionnée (être membre du laboratoire LIFAT) qui n’est pas requise par la question, d’où une légère perte de pertinence.
- **Avis Context Precision** : Le contexte contient les coordonnées de Juliette Piquard ainsi que son rattachement au secteur « Sciences et technologies », qui inclut le LIFAT. Le contexte est donc parfaitement adapté pour répondre à la question.

### Question : je suis en arrêt de travail, qui dois-je contacter ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 4.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse indique qu'il faut contacter « Aurélie PETEREAU » (Direction des Ressources Humaines) à une adresse e‑mail précise. Aucun de ces éléments (nom, adresse e‑mail) n’apparaît dans le contexte fourni. Seul le lien vers le cadre de travail est présent dans le texte. Ainsi, la majorité de l’affirmation n’est pas traçable dans le contexte, ce qui justifie une note faible.
- **Avis Answer Relevance** : La réponse répond directement à la question en proposant un interlocuteur et un moyen de contact, ce qui est pertinent pour la demande « qui dois‑je contacter ? ». Même si le contact est inventé, la forme de la réponse reste ciblée, d’où une note élevée.
- **Avis Context Precision** : Le contexte parle de la gestion des congés, du cadre de travail et fournit des contacts (David SAVY, Adrien LEMONNIER, Caroline Jacques, Katia Bouaza) ainsi que l’organigramme de la DRH, mais il ne mentionne aucun nom ou e‑mail correspondant à la réponse donnée. Le contexte est donc seulement vaguement lié à la question et ne fournit pas l’information recherchée.

### Question : Combien de temps va prendre mon inscription ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 4.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : le processus de validation (direction de thèse, laboratoire, école doctorale), la variabilité des délais et les coordonnées de Guillaume Fialeix. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond à la question en expliquant que la durée dépend des étapes de validation et en proposant de contacter le responsable pour une estimation précise. Elle ne fournit pas de durée exacte, ce qui reflète l'absence d'information précise dans le contexte, mais reste pertinente.
- **Avis Context Precision** : Le contexte contient les informations nécessaires (délais de validation, contacts, étapes du processus) qui permettent de formuler une réponse. Il manque toutefois une indication explicite du temps moyen, ce qui rend le contexte partiellement complet pour la question.

### Question : Comment avoir un email ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes ou directement déductibles du contexte fourni. Le fait que chaque doctorant dispose d’un compte email sur le domaine etu.univ‑tours.fr, les contacts du service informatique (dsi@univ‑tours.fr, liste des informaticiens de proximité), la plateforme PAL, le rôle du gestionnaire d’école doctorale et les services associés (Office 365, ENT, VPN, UTBox) sont explicitement mentionnés dans le texte. Aucun élément n’est inventé ; même la forme « prenom.nom@etu.univ‑tours.fr » est une reformulation raisonnable du domaine indiqué.
- **Avis Answer Relevance** : La réponse répond précisément à la question « Comment avoir un email ? » en décrivant la procédure d’obtention, les interlocuteurs à contacter, les étapes d’activation et de renouvellement, ainsi que les services liés à l’adresse email.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires : existence d’un compte email pour les doctorants, procédure d’attribution via le service informatique, contacts (dsi@, liste des informaticiens, PAL), et détails sur les services numériques. Le système a exploité ces éléments de façon pertinente.

### Question : - Je souhaite me procurer le formulaire de déclaration d’invention de l’université, à qui dois-je m’adresser ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les informations fournies (Justine Gillet, son rôle, email, téléphone, le fait que le formulaire est "à venir sur intranet", le lien vers le SPIV et les articles du code) sont présentes dans le contexte. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond directement à la question en indiquant le contact à qui s'adresser pour obtenir le formulaire de déclaration d’invention, avec les coordonnées demandées.
- **Avis Context Precision** : Le contexte contient le nom, le rôle, les coordonnées de Justine Gillet ainsi que la mention du SPIV comme service chargé des déclarations d’invention, ce qui suffit pour répondre à la question.

### Question : Qui contacter pour toute demande d'ouvrages en service presse ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 2.0/5, Context Precision: 3.0/5
- **Avis Faithfulness** : La réponse introduit un contact (Aurélie PETEREAU, aurelie.petereau@univ-tours.fr) qui n’apparaît nulle part dans le contexte fourni, constituant une hallucination. Le reste du texte (absence d’information, liens vers des pages) est compatible avec le contexte, mais la présence de cet élément non‑documenté diminue fortement la fidélité.
- **Avis Answer Relevance** : La question demande explicitement le contact à joindre pour les demandes d’ouvrages du service presse. La réponse indique qu’aucune information n’a été trouvée et propose des pages génériques ainsi qu’un contact halluciné, ne répondant donc pas directement à la demande.
- **Avis Context Precision** : Le contexte contient une « Adresse générique du service » (spiv@univ-tours.fr) qui pourrait correspondre au service presse, ainsi que d’autres adresses e‑mail. Cependant, le texte ne précise pas que ces adresses sont liées au service presse, rendant le contexte partiellement pertinent mais incomplet pour répondre précisément.

### Question : comment enregistrer ma demande de formation hors-catalogue et quels documents dois-je fournir ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend presque intégralement les informations du contexte : procédure d’envoi d’un email préalable, déclaration sur ADUM, champs à remplir et documents à joindre. Le seul élément ajouté qui n’apparaît pas dans le contexte est le lien URL « https://www.adum.fr/ » vers le compte ADUM, ce qui constitue une légère hallucination.
- **Avis Answer Relevance** : La réponse répond exactement à la question en expliquant comment enregistrer la demande hors‑catalogue et quels documents fournir, sans digression.
- **Avis Context Precision** : Le contexte fourni contient toutes les instructions nécessaires (email préalable, déclaration ADUM, pièces à joindre, rappel sur l’incomplétude). Il est donc parfaitement pertinent.

### Question : Mon jury de thèse est-il valide ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend la plupart des règles présentes dans le contexte (nombre de membres, proportions, HDR, rapporteurs, membre émérite, équilibre de genre, rôle du directeur d'école et du président). Cependant, elle introduit des informations qui ne figurent pas dans le texte fourni : un nombre maximal de 2 membres invités, des liens URL (legifrance, ADUM, site du Collège Doctoral), la mention « procédures de l'Université de Tours » et des coordonnées spécifiques. Ces éléments sont donc des hallucinations, ce qui empêche d’attribuer la note maximale.
- **Avis Answer Relevance** : La réponse répond à la question « Mon jury de thèse est‑il valide ? » en proposant un checklist des critères de validité et les étapes de vérification. Elle ne donne pas de jugement sur un jury concret (impossible sans les données), mais fournit les informations nécessaires pour que l'utilisateur puisse vérifier lui‑même. La pertinence est donc élevée.
- **Avis Context Precision** : Le contexte récupéré contient toutes les règles nécessaires pour juger de la validité d’un jury (nombre de membres, proportions, HDR, rapporteurs, membres extérieurs, genre, membres invités, etc.). Le système a donc pu s’appuyer sur un contexte très précis.

### Question : quels types de financement de thèse existent ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La plupart des éléments de la réponse sont directement tirés du contexte (ex. contrats « Établissement », contrats régionaux, ANR, Europe, Labex, ANRS, Handicap, CIFRE, DGA/ADEME, financements étrangers, salariés, cotutelle, bourses de fondations). Cependant, la réponse ajoute des précisions non présentes dans le texte, comme les "programmes-cadre" et les "bourses Marie Skłodowska‑Curie" ainsi que les "missions d’enseignement rémunérées", qui ne sont pas mentionnées dans le contexte. Ces ajouts constituent des hallucinations légères, d'où la note 4.
- **Avis Answer Relevance** : La réponse répond exactement à la question en listant les différents types de financement de thèse, sans digression hors sujet. Elle fournit une vue d'ensemble claire et structurée, ce qui justifie la note maximale de 5.
- **Avis Context Precision** : Le contexte fourni contient une liste détaillée des sources de financement (ANR, Europe, Labex, contrats de recherche, CIFRE, DGA, ADEME, gouvernements, associations, salariés, etc.). Il est donc parfaitement adapté pour répondre à la question, d'où la note 5.

### Question : - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autre CHRU?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend correctement le nom, l'e‑mail et le téléphone de Claude‑Emmanuel BOUDET tels qu'ils figurent dans le contexte. Cependant, elle ajoute une information non présente dans le contexte : « Contact à utiliser : Justine Gillet », ce qui constitue une hallucination. Le reste du texte (rôle d’accompagnement, sécurisation des échantillons) est une reformulation raisonnable mais pas explicitement mentionné, d'où une note intermédiaire.
- **Avis Answer Relevance** : La réponse cible la question en indiquant le chargé d’affaires à contacter pour les échantillons du CHRU. Elle fournit les coordonnées demandées, ce qui répond directement à la demande. L'ajout de Justine Gillet est hors sujet mais n'empêche pas la pertinence principale.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires : le nom, l'e‑mail, le téléphone de Claude‑Emmanuel BOUDET ainsi que la question relative aux échantillons du CHRU. Le système a donc pu extraire les bonnes données.

### Question : Je souhaite monter un projet, comment faire ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 3.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse ne contient aucune information manifestement inventée ; elle se contente d’affirmer qu’une procédure spécifique existe, ce qui est cohérent avec le contexte. Cependant, elle ne cite aucun détail présent dans le texte (ex. contacts, étapes, exigences), ce qui constitue une légère inférence plutôt qu’une restitution exacte.
- **Avis Answer Relevance** : La réponse répond globalement à la question « comment monter un projet ? » en indiquant qu’il faut suivre une procédure et en promettant des étapes et contacts. Néanmoins, elle ne fournit aucune des étapes concrètes attendues, restant donc partiellement pertinente.
- **Avis Context Precision** : Le contexte fourni contient de nombreuses informations précises sur le montage d’un projet (exigences de partenariat, budget, durée, contacts e‑mail, pièces à fournir, calendrier, rôle du SCRIPT, etc.). Ces informations sont pleinement pertinentes pour répondre à la question.

### Question : - Comment protéger un savoir-faire ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La plupart des affirmations (confidentialité stricte, usage du cahier de laboratoire, rôle du SPIV, vérification PPST, consignes de sécurité numérique) sont directement présentes dans le contexte. Cependant, le système a inventé le contact « Justine Gillet (justine.gillet@univ-tours.fr) » qui n’apparaît nulle part dans le texte fourni. Cette hallucination fait baisser la note de fidélité.
- **Avis Answer Relevance** : La réponse traite précisément de la manière de protéger un savoir‑faire : confidentialité, accords NDA, traçabilité, accompagnement du SPIV, vérifications PPST et mesures de sécurité numérique. Elle répond donc pleinement à la question posée.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires (confidentialité, SPIV, cahier de laboratoire, PPST, consignes de sécurité) pour répondre à la question. Aucun élément essentiel n’est absent du contexte.

### Question : Je pars en mission, quelle pièce dois-je remplir ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend les éléments présents dans le contexte (Ordre de mission, état liquidatif, pièces justificatives, règle de non‑remboursement kilométrique). Un seul élément n’est pas présent dans le contexte : le lien vers le barème officiel du service public (https://www.service-public.fr/particuliers/actualites/A15564). Cette petite addition constitue une hallucination, d’où la note 4.
- **Avis Answer Relevance** : La question demande la pièce à remplir pour une mission. La réponse indique clairement l’Ordre de mission (et, en complément, l’État liquidatif après la mission), ce qui répond directement à la demande. Aucun hors‑sujet n’est introduit.
- **Avis Context Precision** : Le contexte contient les mentions d’« Ordre de mission », d’« État liquidatif », ainsi que les listes de pièces justificatives et la règle de non‑remboursement kilométrique. Ces informations sont suffisantes pour répondre à la question, d’où la note maximale.

### Question : Quel est le délai moyen entre la soumission d’un manuscrit et sa publication ?
- **Erreur d'évaluation** : 'choices'

## Query7_rag_batch_trials.json

### Question : - Est-ce que je dois faire un contrat avec mon partenaire même si on n'échange pas d'argent?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 3.0/5
- **Avis Faithfulness** : {'score': 4, 'explanation': "La réponse s'appuie majoritairement sur le contexte fourni (ex. : risques juridiques, propriété intellectuelle, rôle du PJR, statut des collaborateurs bénévoles). Cependant, certaines précisions (comme les exemples concrets de litiges ou les références à des articles de loi non cités dans le contexte, ex. L.122-7 CPI) ne sont pas explicitement mentionnées dans le texte source, bien qu'elles soient cohérentes avec le domaine. D'où un 4/5 pour une fidélité *presque* parfaite."}
- **Avis Answer Relevance** : {'score': 5, 'explanation': 'La réponse est **exactement alignée** avec la question : elle explique *pourquoi* un contrat est nécessaire (même sans échange financier), *quels* risques sont évités, et *comment* procéder (avec contacts PJR). Elle couvre aussi des aspects implicites comme la confidentialité ou les collaborateurs non rémunérés, ce qui enrichit utilement la réponse.'}
- **Avis Context Precision** : {'score': 3, 'explanation': "Le contexte fourni contient des **éléments pertinents** (ex. : risques liés aux collaborateurs bénévoles, rôle du PJR, propriété intellectuelle), mais il est **fragmenté et incomplet** pour une réponse exhaustive. Par exemple, il n’explique pas clairement *les types de contrats possibles* (convention de collaboration, accord de consortium) ni les *procédures précises* de signature, que la réponse mentionne pourtant. Ces lacunes obligent à une inférence partielle, d'où un 3/5."}

### Question : - J'aimerais présenter certains de mes résultats à un partenaire afin de lui proposer une collaboration, est-ce qu'il faut encadrer cela?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5

### Question : - J'ai obtenu une subvention pour mon projet, pourquoi je ne peux pas commencer le projet dès maintenant?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 2.0/5, Context Precision: 4.0/5
- **Avis Faithfulness** : {'score': 3, 'explanation': "La réponse s'appuie partiellement sur le contexte (mention d'un contact pertinent : Justine Gillet), mais elle **hallucine** une attribution de domaine incorrecte pour la question posée. En réalité, la question est listée sous **Laurine DRUGAT** (Sciences de la vie/SHS), et non Justine Gillet (Sciences et matériaux). De plus, la réponse suggère des 'étapes administratives ou juridiques' sans preuve dans le contexte, qui ne mentionne que des redirections vers d'autres services (ex: AFRV, DRH) pour des questions spécifiques (recrutement, achats, etc.)."}
- **Avis Answer Relevance** : {'score': 2, 'explanation': "La réponse est **partiellement utile** en orientant vers un contact, mais elle **ne répond pas directement** à la question ('pourquoi je ne peux pas commencer ?'). Le contexte révèle que la raison dépend souvent de **démarches préalables** (ex: validation budgétaire, recrutement, achats) gérées par d'autres services (AFRV, DRH), non mentionnés dans la réponse. Une réponse optimale aurait listé ces blocages concrets (ex: 'attente de la validation du budget par l’AFRV' ou 'recrutement en cours via la DRH')."}
- **Avis Context Precision** : {'score': 4, 'explanation': "Le contexte contient **toutes les informations nécessaires** pour une réponse précise : la question est explicitement listée sous Laurine DRUGAT, et les tableaux détaillent les services responsables des étapes post-subvention (AFRV pour les dépenses, DRH pour les recrutements, etc.). Cependant, ces informations sont **éparpillées** dans des sections différentes (ex: 'Montage de Projet' vs 'Questions récurrentes'), ce qui peut rendre leur extraction moins immédiate."}

### Question : - J'ai été contacté en tant qu'expert pour parler de mon domaine de recherche, est-ce que je peux le faire gratuitement?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Reasoning global** : {'faithfulness': "La réponse s'appuie strictement sur le contexte fourni (tableau des chargés d'affaires et recommandations générales sur les démarches administratives). Aucune information externe ou hallucinée n'est introduite. La mention de la consultation obligatoire de la chargée d'affaires et les coordonnées de Justine Gillet (pour le LIFAT) sont directement extraites du contexte.", 'answer_relevance': "La réponse adresse **directement** la question posée ('est-ce que je peux le faire gratuitement?') en soulignant la nécessité d'un **encadrement préalable** (même pour une intervention gratuite), ce qui est implicite dans le contexte (ex: 'présenter des résultats à un partenaire' ou 'collaboration' nécessite un accord). Elle oriente vers le bon interlocuteur, ce qui est utile et concret.", 'context_precision': "Le contexte contient **toutes les informations nécessaires** pour répondre : (1) la question exacte est listée dans les 'Questions récurrentes' du tableau, (2) les coordonnées des chargés d'affaires sont fournies, (3) les sections sur la propriété intellectuelle et la confidentialité (ex: 'accord de confidentialité') justifient la nécessité d'un encadrement, même pour une intervention non rémunérée. Le contexte couvre à la fois les aspects **administratifs** (qui contacter) et **juridiques** (pourquoi encadrer)."}

### Question : - Je souhaite répondre à un Appel à projet?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5

### Question : - Faire valider mon budget pour un projet de recherche?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Reasoning global** : <<Faithfulness>> : La réponse s'appuie strictement sur le contexte fourni (ex. : références à Justine Gillet, SPIV, et la procédure de 'Starter Pack' extraites des tableaux et paragraphes du contexte. Aucune information externe ou hallucinée n'est ajoutée. **5/5**

<<Answer Relevance>> : La réponse adresse *directement* la question ('faire valider mon budget') en fournissant une marche à suivre claire, des contacts précis (Justine Gillet pour le LIFAT), et des liens utiles. **5/5**

<<Context Precision>> : Le contexte contenait *toutes* les informations nécessaires : (1) les chargés d'affaires par domaine (tableau avec Justine Gillet pour Sciences et matériaux/LIFAT), (2) la procédure de validation budgétaire (section 'Montage de Projet'), et (3) les coordonnées. Aucune lacune n'empêchait une réponse complète. **5/5**

### Question : - Je souhaite engager des discussions avec un partenaire extérieur?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5

### Question : - Je souhaite collaborer (prestation, collaboration, expertise, etc) avec un partenaire tout en protégeant mes travaux de recherche?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : {'score': 5, 'explanation': "La réponse s'appuie strictement sur le contexte fourni (ex: référence à Justine Gillet pour *Sciences et matériaux*, mention du SPIV, accord de confidentialité, cahier de laboratoire, et lien vers le guide des contrats). Aucune information externe ou hallucinée n'est introduite. Les éléments comme les coordonnées, les procédures (brevet, confidentialité), et les outils (CLE) sont directement tirés du contexte."}
- **Avis Answer Relevance** : {'score': 5, 'explanation': 'La réponse adresse **directement** la question en 3 points clés : (1) *qui contacter* (Justine Gillet, avec coordonnées), (2) *pourquoi* (encadrement juridique, protection des résultats, outils comme le CLE), et (3) *risques à éviter* (divulgation sans accord de confidentialité). Elle inclut même un avertissement proactif (⚠️) et un lien utile vers le guide des contrats, ce qui dépasse une simple réponse basique.'}
- **Avis Context Precision** : {'score': 5, 'explanation': "Le contexte contenait **toutes les informations nécessaires** pour répondre : (a) la table identifie Justine Gillet comme la chargée d’affaires pour *Sciences et matériaux* avec la question exacte posée par l'utilisateur (*collaboration + protection des travaux*), (b) les sections sur le SPIV, les accords de confidentialité, le CLE, et les brevets fournissent des détails concrets pour construire la réponse. Aucune lacune n’est observable."}

### Question : - Je souhaite construire un projet avec un volet clinique (RIPH/RNIPH)?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5

### Question : - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autre CHRU?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 3.0/5, Context Precision: 5.0/5

### Question : - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire extérieur? Est-ce gratuit?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : {'score': 4, 'explanation': 'La réponse s’appuie majoritairement sur le contexte fourni (ex : nécessité d’un contrat, rôle du SPIV, contact de Justine Gillet pour les Sciences et matériaux). Cependant, une légère imprécision est présente : le contexte ne mentionne pas explicitement le **laboratoire LIFAT** comme relevant de Justine Gillet (il est listé sous Juliette Piquard pour les *Sciences et technologies*). Cela constitue une extrapolation mineure, mais non critique, car le reste des informations (obligation de contrat, gratuité conditionnelle, rôle du SPIV) est fidèle au contexte.'}
- **Avis Answer Relevance** : {'score': 5, 'explanation': 'La réponse adresse **directement et exhaustivement** la question : (1) elle précise le cadre contractuel obligatoire pour les expérimentations avec un partenaire extérieur, (2) aborde la question de la gratuité en distinguant les cas (prestation vs collaboration équilibrée), et (3) fournit des contacts et ressources utiles (SPIV, cahier de laboratoire, lien vers les contrats de recherche). Aucune information superflue ou hors-sujet.'}
- **Avis Context Precision** : {'score': 5, 'explanation': 'Le contexte contient **toutes les informations nécessaires** pour répondre : (1) la question exacte (*"Dans quel cadre puis-je réaliser des expérimentations avec un partenaire extérieur? Est-ce gratuit?"*) est listée sous Hélène Jullien (Santé) **et** correspond aux missions générales du SPIV décrites dans les paragraphes suivants ; (2) les modalités de collaboration (contrats, confidentialité, propriété intellectuelle) sont détaillées ; (3) les contacts par domaine (incluant Justine Gillet pour les Sciences et matériaux) sont fournis. Le contexte permet une réponse complète et sourcée.'}

### Question : - Comment puis-je envoyer ou recevoir des échantillons biologiques ou chimiques pour mener ma recherche?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5

### Question : - Comment construire le budget pour ma demande de financement?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5

### Question : - Je souhaite présenter certains de mes résultats à un partenaire en vue de proposer une collaboration: cette démarche doit-elle faire l'objet d'un encadrement particulier?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Reasoning global** : [{'criterion': 'faithfulness', 'explanation': "La réponse s'appuie strictement sur le contexte fourni, sans ajouter d'informations externes non vérifiables. Elle cite explicitement des éléments du tableau (ex: Justine Gillet, SPIV) et des extraits textuels (ex: confidentialité, brevets). Aucune hallucination détectée."}, {'criterion': 'answer_relevance', 'explanation': "La réponse adresse **directement** la question en : 1) confirmant la nécessité d'un encadrement, 2) précisant les outils (accords de confidentialité, contrats), 3) orientant vers le contact adéquat (Justine Gillet) et 4) mentionnant les risques (divulgation de brevets). L'utilisateur obtient une réponse **actionnable** et complète."}, {'criterion': 'context_precision', 'explanation': "Le contexte contenait **toutes les informations nécessaires** pour répondre : la question exacte était listée dans le tableau (colonne 'Questions récurrentes') pour Justine Gillet, et les paragraphs sur la confidentialité/brevets/SPIV fournissaient les détails juridiques et procéduraux. Aucune information manquante pour une réponse robuste."}]

### Question : - Est-il nécessaire de mettre en place un contrat lorsqu'un projet de recherche est mené uniquement avec des partenaires académiques?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 4.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : {'score': 3, 'explanation': "La réponse mentionne des éléments plausibles (ex: 'propriété intellectuelle, confidentialité, engagements réciproques') qui pourraient être déduits du contexte, mais **aucune source directe dans le contexte fourni** ne confirme explicitement ces points pour des collaborations *uniquement académiques*. Le contexte aborde surtout les **collaborateurs bénévoles**, les **émérites**, et les **contrats avec des tiers industriels** (marchés publics, brevets, etc.), mais pas explicitement les partenariats inter-laboratoires publics. La référence à 'Justine Gillet' et au PJR est une extrapolation utile mais non justifiée par le contexte donné (le PJR est cité pour des cas précis comme les brevets ou les conventions d'accueil, pas pour des collaborations académiques pures)."}
- **Avis Answer Relevance** : {'score': 4, 'explanation': 'La réponse est **utile et adaptée** à la question** : elle souligne à juste titre que même entre académiques, des risques juridiques (PI, confidentialité) peuvent exister et recommande de consulter le PJR. La suggestion de préciser les détails du projet (laboratoires, résultats attendus) est pertinente. Cependant, elle aurait pu insister davantage sur l’**absence de mention explicite** dans le contexte des collaborations 100% académiques (ce qui aurait pu mener à une note de 5).'}
- **Avis Context Precision** : {'score': 2, 'explanation': "Le contexte fourni est **peu précis** pour répondre à la question. Il traite surtout de : 1) **collaborateurs bénévoles/émérites** (risques de confidentialité, PI, responsabilité), 2) **contrats avec des tiers externes** (marchés publics, brevets), et 3) **procédures internes du PJR** (déclarations d’invention, licences). **Aucun passage ne discute spécifiquement des partenariats entre laboratoires publics**, ni ne précise si des contrats sont obligatoires dans ce cas. Les éléments sur les 'conventions d'accueil' ou 'accords de consortium' (cités dans la réponse) ne sont pas détaillés dans le contexte. La note aurait pu être 1, mais le contexte évoque indirectement des **risques généraux** (confidentialité, PI) qui *pourraient* s’appliquer, d’où un 2."}

### Question : - Je souhaite répondre à projet – comment monter mon budget et projet?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5

### Question : - J'ai obtenu la subvention pour mon projet, quel INM de recrutement je peux prévoir avec la somme que j'ai obtenue?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 3.0/5
- **Avis Faithfulness** : {'score': 4, 'explanation': "La réponse s'appuie majoritairement sur le contexte fourni (ex: INM minimum de 366, catégories A/B/C, PPCR 2019, contact RH). Cependant, elle mentionne des éléments non explicitement présents dans le contexte (ex: 'grilles indiciaires pour 2026', 'laboratoire LIFAT', 'Anne Galopin' comme contact spécifique). Ces ajouts, bien que plausibles, ne sont pas strictement sourcés dans le texte fourni, d'où une légère déduction."}
- **Avis Answer Relevance** : {'score': 5, 'explanation': "La réponse est parfaitement alignée avec la question : elle aborde directement l'INM en fonction du budget, des catégories de postes, et des contraintes administratives. Elle propose même une marche à suivre concrète (contacter les RH), ce qui dépasse une simple réponse factuelle."}
- **Avis Context Precision** : {'score': 3, 'explanation': "Le contexte contient des informations utiles (INM minimum, catégories de recrutement, procédures RH), mais il est **incomplet** pour une réponse exhaustive : (1) absence de grilles indiciaires détaillées par catégorie en 2020/2024, (2) pas de mention des fourchettes salariales ou des charges patronales précises, (3) références floues aux 'nouvelles règles PPCR' sans détails. Le contexte permet une réponse partielle, mais nécessite des inférences ou des compléments externes pour être complet."}

### Question : - Il me reste une marge de crédits sur mon projet, jusqu'à quand puis-je l'utiliser et pour quel type de dépense?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 4.0/5, Context Precision: 3.0/5

### Question : - Comment procéder pour réaliser les achats (consommables ou prestation) financés par une subvention?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 3.0/5
- **Avis Faithfulness** : {'score': 4, 'explanation': "La réponse s'appuie majoritairement sur le contexte fourni (ex : rôle de l'Antenne Financière, seuils de 25 000 € HT, dérogations pour paiement avant 'service fait', frais de structure). Cependant, quelques éléments ne sont pas explicitement mentionnés dans le contexte, comme l'exemple de contact 'Anne Galopin' ou la précision sur les '50% pour l’établissement/50% pour le labo' (le contexte évoque des répartitions variables selon les financeurs, mais pas cette formule exacte). Ces ajouts, bien que plausibles, ne sont pas strictement sourcés."}
- **Avis Answer Relevance** : {'score': 5, 'explanation': "La réponse couvre de manière exhaustive et structurée la question initiale : vérification de l'éligibilité, choix de la procédure (avec distinction par seuil), engagement/paiement, et contact dédié. Les étapes sont claires et directement actionnables pour un chercheur ou gestionnaire. L’inclusion d’exemples concrets (abonnements, logiciels) et de cas particuliers (indemnités aux panelistes) renforce la pertinence."}
- **Avis Context Precision** : {'score': 3, 'explanation': "Le contexte fourni est fragmenté et parfois redondant (ex : répétitions sur le rôle de l’AF), avec des informations éparses sur plusieurs pages. Les éléments clés pour répondre à la question y sont présents (rôle de l’AF, seuils, dérogations, frais de structure), mais leur dispersion et le manque de synthèse initiale rendent leur extraction moins immédiate. Par exemple, la procédure pour les achats > 25 000 € HT est implicite (nécessité de passer par le SCoP), mais non explicitement détaillée en une seule section. Les tableaux sur les types de financement ou les frais de structure apportent des précisions utiles, mais leur lien avec la procédure d'achat n'est pas directement établi dans le contexte."}

## Query_Mix_10_big_draft_trials.json

### Question : C’est quoi les SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes ou clairement déduites du contexte : définition des SAPS, lien avec la loi LPR 2021, rôle du ministère, objectifs de rapprochement chercheurs‑citoyens, reconnaissance de la médiation scientifique, exemples d’actions (événements, formations, accompagnement) et le contact d'Alice NUÉ. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La question porte sur la définition des SAPS. La réponse fournit une définition précise, les objectifs, les actions concrètes et le cadre institutionnel, répondant pleinement à la demande.
- **Avis Context Precision** : Le contexte récupéré contient la définition, les objectifs, les missions et les contacts relatifs aux SAPS, ce qui est exactement ce qui est nécessaire pour répondre à la question.

### Question : Comment peut-on changer le budget d’un projet ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend correctement les étapes décrites dans le contexte (contacter le SPIV, fournir un argumentaire scientifique et un budget révisé, attendre l’accord du financeur). Cependant, elle introduit des éléments qui n’apparaissent pas dans le contexte : le nom « Anne Galopin », l’adresse e‑mail af.polytech@univ‑tours.fr, le service « Service d’Appui à la Recherche » et la mention du laboratoire « LIFAT ». Ces informations sont donc des hallucinations, ce qui empêche d’attribuer la note maximale.
- **Avis Answer Relevance** : La réponse répond directement à la question « Comment changer le budget d’un projet ? » en décrivant la procédure à suivre, les interlocuteurs et les documents requis. Aucun élément hors sujet n’est présent.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires pour répondre : procédure de modification budgétaire, rôle du SPIV/SPV, documents à fournir, nécessité de l’accord du financeur, etc. Le contexte est donc parfaitement pertinent.

### Question : Quelles sont les différentes démarches à effectuer ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 1.0/5, Context Precision: 1.0/5
- **Avis Faithfulness** : La réponse ne contient aucune information erronée ou inventée ; elle se limite à annoncer qu'elle va lister les démarches. Aucun élément du texte n’est en contradiction avec le contexte, mais aucune donnée concrète n’est non plus fournie.
- **Avis Answer Relevance** : La question demande les différentes démarches à effectuer. La réponse ne fournit aucune démarche concrète, se contentant d’une phrase introductive vide. Elle ne répond donc pas à la demande.
- **Avis Context Precision** : Le contexte fourni décrit en détail les étapes du dossier HDR (formulaires, pièces à fournir, dépôt, examen par la commission, autorisation d’inscription, composition du jury, etc.) ainsi que les contacts. Aucun de ces éléments n’est exploité dans la réponse, ce qui montre que le contexte n’a pas été utilisé de façon pertinente.

### Question : - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire extérieur? Est-ce gratuit?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 4.0/5, Context Precision: 4.0/5
- **Avis Faithfulness** : La réponse contient plusieurs affirmations qui ne figurent pas dans le contexte fourni : mention du « laboratoire LIFAT », indication que la gratuité ne s’applique qu’aux partenariats académiques, référence à un tarif fixé par le SPIV, et attribution de contacts (Juliette Piquard, Justine Gillet) spécifiques à LIFAT. Ces éléments sont donc des hallucinations. Les parties concernant la nécessité d’un contrat et le rôle du SPIV sont bien présentes dans le contexte, mais la proportion d’informations non‑supportées est élevée, d’où la note 2.
- **Avis Answer Relevance** : La réponse répond globalement à la question en expliquant qu’un contrat est requis et en abordant la question de la gratuité. Cependant, elle introduit des informations hors sujet (LIFAT, contacts non pertinents) qui diminuent légèrement la pertinence, justifiant un 4.
- **Avis Context Precision** : Le contexte fourni contient les informations essentielles (question de Hélène Jullien, besoin d’encadrer contractuellement, rôle du SPIV, exigences de confidentialité). Le système a pu s’appuyer sur ces éléments, même s’il a ajouté du superflu. Le contexte était donc pertinent, d’où un 4.

### Question : A quelle adresse postale ou mail dois-je envoyer mon projet ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les informations fournies dans la réponse sont présentes dans le contexte : l'adresse e‑mail drv-pi@univ-tours.fr apparaît plusieurs fois, ainsi que l'absence d'adresse postale. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond directement à la question en indiquant l'e‑mail à utiliser et en précisant qu'aucune adresse postale n'est disponible, ce qui correspond exactement à la demande.
- **Avis Context Precision** : Le contexte contient l'e‑mail générique drv-pi@univ-tours.fr ainsi que l'information qu'aucune adresse postale n'est fournie. Le contexte est donc parfaitement adapté.

### Question : Comment m’inscrire / me réinscrire ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La plupart des étapes, documents requis, validations et dates sont directement tirés du contexte. Cependant, le nom "Christele Gaudron-Bredif" et l'adresse e‑mail "gaudron@univ-tours.fr" n’apparaissent pas dans le texte fourni (le contexte donne "Christèle GAUDRON" et l'e‑mail "christele.gaudron@univ-tours.fr"). Cette information inventée fait baisser la note de fidélité.
- **Avis Answer Relevance** : La réponse répond précisément à la question « Comment m’inscrire / me réinscrire ? » en décrivant la procédure, les pièces à fournir, les validations nécessaires et les contacts utiles. Aucun élément hors sujet n’est présent.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires (plateforme ADUM, pièces à fournir, validations, dates limites, contacts, liens). Le système a pu extraire ces données, donc la précision du contexte est maximale.

### Question : Quelles ressources le Pôle SAPS peut m’apporter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : formations (Médiatraining, Jeudis des SAPS), accompagnement de projets (conseil, mise en relation, aide budgétaire, ANR, APR‑IR, projets européens), exemples d’appels (Kaléidoscope, Ma thèse en BD), événements (DéTours des sciences, Fête de la science, Festival (Re)Cherche et trouve), boutique des sciences, label SAPS TEEPEE, contacts (Audrey Richard, Caroline Didier) et URLs. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question « Quelles ressources le Pôle SAPS peut‑moi apporter ? » en listant les différentes ressources (formations, accompagnement, événements, réseau, ressources en ligne) de façon détaillée et pertinente.
- **Avis Context Precision** : Le contexte fourni contient l’ensemble des informations nécessaires : description des missions, listes de formations, accompagnement, événements, contacts et sites web. Le système a correctement exploité ces éléments.

### Question : Y a-t-il des alumni ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont vérifiables dans le contexte : le texte indique qu'aucune information sur un réseau d'alumni n'est présente. La suggestion de consulter d'autres sources n'est pas une affirmation factuelle et ne constitue pas une hallucination.
- **Avis Answer Relevance** : La réponse répond directement à la question « Y a-t-il des alumni ? » en indiquant l'absence d'information dans les ressources consultées et en proposant des pistes pour obtenir une réponse, ce qui est pleinement pertinent.
- **Avis Context Precision** : Le contexte fourni porte sur les campagnes de carrière du personnel, les contacts internes, la réglementation interne, etc., et ne contient aucune mention d'alumni ou d'association d'anciens. Ainsi, le contexte n'est pas précis pour répondre à la question.

### Question : Que propose le Pôle SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte fourni, parfois reformulées mais sans invention. Par exemple, les missions, les événements (DéTours des sciences, Ma thèse en 180 s, Festival (Re)Cherche et trouve), les formations (Médiatraining, Jeudis des SAPS, CERCIP), les projets arts‑sciences (Ma thèse en BD, Kaléidoscope, résidence d’artiste Pier Gajewski) et le label SAPS Teepee sont tous mentionnés dans le texte source.
- **Avis Answer Relevance** : La question porte sur ce que propose le Pôle SAPS. La réponse décrit précisément les offres du pôle (missions, formations, événements, projets, dispositifs structurants, publics cibles), répondant ainsi de façon exhaustive à la demande.
- **Avis Context Precision** : Le contexte récupéré contient l’ensemble des informations exploitées : missions, événements, formations, projets, label, boutique des sciences, publics, etc. Aucun élément requis n’est absent du contexte.

### Question : - Qu’est-ce qu’une invention ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 4.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse inclut une définition de l'invention (« création technique nouvelle qui apporte une solution à un problème spécifique et qui peut faire l'objet d'une protection par un brevet ») qui n'apparaît nulle part dans le contexte fourni. Seule la partie indiquant de contacter le PJR et l'adresse e‑mail est présente dans le contexte. Ainsi, plusieurs affirmations sont hallucinations, justifiant une note faible.
- **Avis Answer Relevance** : La réponse répond directement à la question en proposant une définition et en orientant l'utilisateur vers le PJR pour plus de précision. Elle reste pertinente, même si elle ajoute une suggestion de contact qui n'était pas demandée explicitement.
- **Avis Context Precision** : Le contexte contient la question « Qu'est-ce qu'une invention ? » ainsi que les coordonnées du PJR, mais il ne fournit aucune définition de l'invention. Le contexte est donc seulement vaguement lié à la réponse attendue, d'où une note basse.

### Question : - Je souhaite répondre à un Appel à projet?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les informations fournies (nom, e‑mail, téléphone de Justine Gillet, référence à Juliette Piquard, liens vers les appels à projets régionaux, nationaux et le dispositif CIFRE) sont présentes dans le contexte. Les fonctions attribuées à Justine (montage administratif, validation du budget, aspects juridiques) découlent des questions récurrentes listées pour elle et ne constituent pas des inventions.
- **Avis Answer Relevance** : La réponse cible directement la demande « Je souhaite répondre à un Appel à projet » en indiquant le chargé d’affaires à contacter et en proposant des ressources utiles pour la candidature.
- **Avis Context Precision** : Le contexte contient les contacts pertinents (Justine Gillet, Juliette Piquard) ainsi que les liens vers les guichets de financement et le dispositif CIFRE, ce qui permet de répondre à la question sans chercher d’autres sources.

### Question : je suis en arrêt de travail, qui dois-je contacter ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 4.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse cite un contact précis – Aurélie PETEREAU et son adresse e‑mail – qui n’apparaît nulle part dans le contexte fourni. Cette information est donc une hallucination. Les liens vers les pages « Congés maladie des agents titulaires/contractuels » sont présents dans le contexte, mais la partie principale (nom et e‑mail) n’est pas justifiable.
- **Avis Answer Relevance** : La réponse répond directement à la question « qui dois‑je contacter ? » en proposant un interlocuteur, ce qui la rend pertinente. Les informations supplémentaires (liens) sont utiles mais ne nuisent pas à la pertinence.
- **Avis Context Precision** : Le contexte ne fournit pas le nom ni l’e‑mail du référent. Il indique seulement qu’il faut prendre contact avec un gestionnaire de la DRH et renvoie à l’organigramme. Ainsi le contexte est seulement vaguement lié à la demande de contact.

### Question : Combien de temps va prendre mon inscription ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 3.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse mentionne un contact qui n'existe pas dans le contexte : « Christèle Gaudron‑Bredif » et l'adresse e‑mail « gaudron@univ‑tours.fr ». Le contexte ne contient que « Christèle Gaudron » avec l'e‑mail « christele.gaudron@univ‑tours.fr ». Cette différence constitue une hallucination. Le reste de la réponse (les étapes de validation) est cohérent avec le contexte, mais la présence d'informations inventées réduit la note.
- **Avis Answer Relevance** : La question porte sur la durée de l'inscription. La réponse indique que la durée dépend de plusieurs étapes et invite à contacter un gestionnaire pour obtenir une estimation, sans fournir de durée concrète. Elle répond partiellement à la question mais ne fournit pas l'information demandée.
- **Avis Context Precision** : Le contexte décrit la procédure d’inscription, les étapes de validation et la période d’ouverture (du 1ᵉʳ juin au 15 novembre), mais ne donne pas de durée précise. Ainsi le contexte est vaguement lié à la question de durée, mais il manque les informations chiffrées attendues.

### Question : Comment avoir un email ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement soutenues par le contexte. Le texte indique que le gestionnaire DRH doit être contacté (organigramme DRH), que l’adresse mail se crée via la messagerie Zimbra, que le service informatique de proximité crée les comptes pour les doctorants, et fournit l’adresse générique dsi@univ-tours.fr. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La question « Comment avoir un email ? » reçoit une réponse précise expliquant les démarches à suivre, tant pour les personnels que pour les doctorants, ce qui répond exactement à la demande.
- **Avis Context Precision** : Le contexte récupéré contient toutes les informations nécessaires : procédure DRH, lien vers l’organigramme, référence à la messagerie Zimbra, rôle du service informatique de proximité et adresse générique dsi@univ-tours.fr. Il est donc parfaitement ciblé.

### Question : - Je souhaite me procurer le formulaire de déclaration d’invention de l’université, à qui dois-je m’adresser ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les informations fournies dans la réponse (contact du PJR via l'adresse drv-pi@univ-tours.fr) sont présentes textuellement dans le contexte. Aucun élément n’a été inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question : elle indique à qui s’adresser pour obtenir le formulaire de déclaration d’invention.
- **Avis Context Precision** : Le contexte contient plusieurs adresses e‑mail, dont celle indiquée (drv-pi@univ-tours.fr) qui est explicitement présentée comme le point de contact pour les questions de propriété intellectuelle et les déclarations d’invention.

### Question : Qui contacter pour toute demande d'ouvrages en service presse ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 2.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse introduit des informations qui ne figurent pas dans le contexte fourni : elle propose de contacter le "Service Communication" de l'Université, fournit un lien vers l'annuaire en ligne et indique le numéro de téléphone "02 47 36 60 00". Aucun de ces éléments n'est présent dans le texte du contexte, ce qui constitue une hallucination. Le reste de la réponse (absence d'information dans le contexte) est correct.
- **Avis Answer Relevance** : La question demande explicitement qui contacter pour les demandes d'ouvrages en service presse. La réponse indique qu'aucune information n'est disponible et suggère de contacter le Service Communication, ce qui n'est pas une réponse directe à la question et ne repose pas sur le contexte. Elle touche au sujet mais ne fournit pas la réponse attendue.
- **Avis Context Precision** : Le contexte fourni ne contient aucune mention d'un "service presse" ni d'un contact dédié à ce service. Les contacts listés (directeur, assistante, service de la commande publique, etc.) ne répondent pas à la demande. Ainsi le contexte est très peu pertinent pour la question posée.

### Question : comment enregistrer ma demande de formation hors-catalogue et quels documents dois-je fournir ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La plupart des étapes et des documents demandés sont exactement tirés du contexte (envoi d'un email préalable, dépôt sur ADUM, champs à remplir, fiche de validation, justificatifs, accord du directeur). Cependant la réponse ajoute des URLs (https://www.adum.fr/ et https://www.adum.fr/aide) et mentionne un « guide utilisateur ADUM » qui n’apparaissent pas dans le contexte, ce qui constitue une petite hallucination.
- **Avis Answer Relevance** : La réponse répond directement à la question en expliquant comment enregistrer la demande hors‑catalogue et quels documents joindre, sans digression hors sujet.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires (procédure ADUM, champs du formulaire, documents obligatoires, besoin d’accord du directeur). La réponse s’appuie sur ces éléments.

### Question : Mon jury de thèse est-il valide ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend les critères de validité du jury tels qu’ils figurent dans le contexte (nombre de membres, moitié professeurs/assimilés, moitié extérieurs, deux rapporteurs HDR, un HDR de l’établissement, équilibre femmes‑hommes, limite d’un membre émérite et de deux membres invités). Aucun de ces éléments n’est inventé. Le seul élément non présent dans le contexte est le lien hypothétique « [lien_hypothétique_à_remplacer_si_disponible_dans_le_contexte] », qui constitue une hallucination mineure.
- **Avis Answer Relevance** : La réponse répond à la demande en expliquant que, pour juger de la validité du jury, il faut connaître sa composition et en rappelant les critères applicables. Elle ne donne pas de verdict définitif (impossible sans les données du jury), mais fournit les informations nécessaires et demande les précisions manquantes, ce qui est pertinent pour la question.
- **Avis Context Precision** : Le contexte fourni contient toutes les règles nécessaires pour évaluer la validité d’un jury de thèse (nombre de membres, répartition, exigences HDR, rôle du président, limites des membres invités, etc.). Le système a pu extraire ces informations, donc le contexte est parfaitement précis.

### Question : quels types de financement de thèse existent ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les catégories de financement mentionnées dans la réponse (contrats doctoraux Établissement et Collectivités, ANR, programmes européens, Labex, contrats de recherche, CIFRE/DGA/ADEME, bourses étrangères, statut salarié) sont présentes dans le contexte. Aucun élément n’est inventé, à l’exception de la précision « pour les doctorants du laboratoire LIFAT », qui n’est pas explicitement liée aux types de financement dans le texte source.
- **Avis Answer Relevance** : La réponse répond directement à la question « quels types de financement de thèse existent ? » en listant les différentes sources de financement, ce qui correspond exactement à la demande.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires (liste des sources de financement, distinction entre contrats doctoraux Établissement/Collectivités, montant minimum requis). Le système a correctement exploité ces éléments.

### Question : - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autre CHRU?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse utilise les coordonnées de Claude‑Emmanuel BOUDET et d’Hélène JULLIEN qui figurent dans le contexte. Le numéro de téléphone est correctement reproduit (même chiffres, format différent). Cependant, l’affirmation selon laquelle ces chargés d’affaires appartiennent au Service Partenariats Innovations Valorisation (SPIV) et qu’ils « accompagnent spécifiquement les projets impliquant des échantillons biologiques/cliniques » n’est pas explicitement mentionnée dans le contexte, ce qui constitue une légère hallucination.
- **Avis Answer Relevance** : La question porte sur la prise en charge d’échantillons du CHRU. La réponse indique clairement les contacts pertinents (Claude‑Emmanuel BOUDET, puis Hélène JULLIEN) et fournit leurs coordonnées, répondant ainsi directement à la demande.
- **Avis Context Precision** : Le contexte contient exactement les informations nécessaires (nom, email, téléphone) pour répondre à la question. Aucun élément essentiel n’est absent du contexte.

### Question : Je souhaite monter un projet, comment faire ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend les étapes du montage de projet (préparer le Starter Pack, l’envoyer au chargé d’affaires, vérification, dépôt) qui figurent dans le contexte. Cependant, elle introduit le terme « laboratoire LIFAT », qui n’apparaît nulle part dans le texte fourni – il n’est mentionné que comme secteur dans la liste des interlocuteurs. Cette mention constitue une hallucination, d’où la note 3.
- **Avis Answer Relevance** : La question porte sur la manière de monter un projet. La réponse fournit une procédure claire en quatre étapes, répondant directement à la demande. Aucun élément hors sujet n’est ajouté, justifiant la note maximale de 5.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires : les étapes du montage, la notion de « Starter Pack », le rôle du chargé d’affaires, ainsi que les coordonnées des interlocuteurs. Le texte récupéré est donc parfaitement pertinent, d’où la note 5.

### Question : - Comment protéger un savoir-faire ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend correctement les notions de confidentialité, d’accords de confidentialité, d’utilisation du cahier de laboratoire et du rôle du SPIV, qui sont toutes présentes dans le contexte. Cependant, elle introduit des informations qui n’apparaissent nulle part dans le contexte : le nom du laboratoire « LIFAT » et le contact « Justine Gillet » avec son adresse e‑mail. Ces éléments constituent des hallucinations, ce qui fait baisser la note de fidélité à 2.
- **Avis Answer Relevance** : La réponse répond directement à la question « Comment protéger un savoir‑faire ? » en proposant des mesures concrètes (confidentialité, NDA, cahier de laboratoire, recours au SPIV) et en ajoutant un contact pour un accompagnement. Aucun élément n’est hors sujet, donc la pertinence est maximale.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires pour répondre à la question : exigences de confidentialité, importance du cahier de laboratoire, rôle du Service Partenariats Innovations Valorisation, etc. Le contexte est donc parfaitement ciblé.

### Question : Je pars en mission, quelle pièce dois-je remplir ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 2.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse introduit des informations qui n’apparaissent pas dans le contexte : le nom « Anne Galopin », l’adresse e‑mail af.polytech@univ‑tours.fr, ainsi que la liste précise des pièces (ordre de mission, autorisation de déplacement, justificatifs de frais). Aucun de ces éléments n’est présent dans le texte fourni, ce qui constitue une hallucination majeure. Seul le laboratoire LIFAT est mentionné dans le contexte, mais le reste de la réponse n’est pas traçable.
- **Avis Answer Relevance** : La question demande « quelle pièce » remplir pour une mission. La réponse ne fournit pas la pièce demandée, mais oriente vers un contact qui, selon elle, indiquera la liste des pièces. Ainsi, la réponse ne répond pas directement à la question et reste partiellement pertinente.
- **Avis Context Precision** : Le contexte fourni ne contient pas d’information explicite sur les pièces à remplir pour une mission, mais il liste des contacts (Juliette Piquard, Mélanie Fauconnier, spiv@univ‑tours.fr) et des documents liés aux projets de recherche. Le contexte est donc seulement vaguement lié au sujet de la mission.

### Question : Quel est le délai moyen entre la soumission d’un manuscrit et sa publication ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : le texte indique que les documents décrivent les étapes avant la soutenance, qu'aucun délai de publication n'est précisé, et le numéro de téléphone 02 47 36 64 12 figure bien dans le contexte. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond à la question en expliquant que le délai moyen demandé n’est pas indiqué dans les documents et propose de contacter le Service RED pour l’obtenir. Elle ne fournit pas le délai demandé (car il n’est pas disponible), mais elle reste pertinente et utile.
- **Avis Context Precision** : Le contexte fourni ne contient pas l’information recherchée (délai moyen entre soumission du manuscrit et publication). Il ne fournit que des délais liés au dépôt du manuscrit avant la soutenance (7 semaines), ce qui n’est pas la même donnée. Ainsi le contexte est peu pertinent pour la question.

## Query_Mix_03_max_quality_trials.json

### Question : C’est quoi les SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : la définition « Sciences Avec et Pour la Société », le rôle de rapprochement entre chercheurs et société, les activités d’événements (DéTours des sciences, Ma thèse en 180 secondes), les formations à la médiation scientifique, l’accompagnement de projets, le contact d’Alice NUÉ avec son e‑mail, et le site saps.univ‑tours.fr. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question « C’est quoi les SAPS ? » en donnant une définition claire, les objectifs et les principales actions du dispositif, ce qui constitue une réponse pleinement pertinente.
- **Avis Context Precision** : Le contexte fourni contient la définition, les objectifs, les missions, les événements, les formations et les coordonnées du pôle SAPS. Il est donc parfaitement adapté pour répondre à la question.

### Question : Comment peut-on changer le budget d’un projet ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La majorité des étapes décrites (argumentaire scientifique, budget révisé, contact du SPV et de l'antenne financière, validation par le financeur) sont présentes dans le contexte. Cependant, le nom et l'adresse e‑mail "Anne Galopin – af.polytech@univ‑tours.fr" n'apparaissent nulle part dans le texte fourni, constituant une hallucination claire.
- **Avis Answer Relevance** : La réponse répond directement à la question en expliquant comment modifier le budget d’un projet, en détaillant les étapes et les interlocuteurs pertinents.
- **Avis Context Precision** : Le contexte contient les informations nécessaires sur les procédures de modification budgétaire, le rôle du SPV, de l'antenne financière et les documents à fournir, ce qui permet de répondre correctement à la question.

### Question : Quelles sont les différentes démarches à effectuer ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La plupart des informations fournies sont directement tirées du contexte (documents d’inscription, procédure de connexion, remplissage de la Convention Individuelle de Formation, étapes de validation, dossier de soutenance, label européen). Cependant, le nom et l’adresse e‑mail « Guillaume Fialeix – guillaume.fialeix@univ-tours.fr » n’apparaissent nulle part dans le contexte, constituant une hallucination. Un petit nombre d’inférences (ex. notifications automatiques) sont présentes mais restent plausibles. Ainsi la fidélité est évaluée à 3.
- **Avis Answer Relevance** : La réponse répond clairement à la question « Quelles sont les différentes démarches à effectuer ? » en listant les étapes majeures du parcours doctoral, de l’inscription à la soutenance, en incluant le label européen et un contact. Aucun élément hors sujet n’est présent, d’où la note maximale de 5.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires pour répondre à la question : listes de pièces à fournir, procédure d’accès à l’espace ADUM, détails de la convention, validation par les différentes instances, exigences du dossier de soutenance et modalités du label européen. La précision du contexte est donc évaluée à 5.

### Question : - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire extérieur? Est-ce gratuit?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 3.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse introduit plusieurs informations qui ne figurent pas dans le contexte : le contact de Justine Gillet (nom, e‑mail, téléphone) alors que la question est associée à Hélène Jullien, ainsi que des affirmations sur la gratuité selon le type de partenariat qui ne sont pas mentionnées dans le texte fourni. Seules les parties concernant la nécessité d’un encadrement contractuel et le rôle du SPIV sont présentes dans le contexte.
- **Avis Answer Relevance** : La réponse traite du cadre contractuel et de la gratuité, ce qui correspond à la question, mais elle fournit des informations erronées (contact inapproprié) et des précisions non présentes dans le contexte, ce qui diminue sa pertinence globale.
- **Avis Context Precision** : Le contexte contient la question exacte, le contact d'Hélène Jullien, ainsi que les consignes sur l’encadrement contractuel et le rôle du SPIV. Il est donc pleinement pertinent pour répondre à la demande.

### Question : A quelle adresse postale ou mail dois-je envoyer mon projet ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 2.0/5, Context Precision: 3.0/5
- **Avis Faithfulness** : La réponse indique « Anne Galopin – af.polytech@univ-tours.fr » comme contact. Aucun nom ni adresse e‑mail de ce type n’apparaît dans le contexte fourni. Toutes les adresses présentes dans le contexte sont différentes (juliette.piquard@univ‑tours.fr, melanie.fauconnier@univ‑tours.fr, spiv@univ‑tours.fr, etc.). La réponse invente donc un contact, ce qui constitue une hallucination majeure.
- **Avis Answer Relevance** : La réponse tente de répondre à la question en donnant une adresse e‑mail, mais l’adresse fournie est incorrecte. Elle ne répond donc pas réellement à la demande de l’utilisateur, ce qui la rend peu pertinente.
- **Avis Context Precision** : Le contexte contient plusieurs adresses e‑mail pertinentes (ex. juliette.piquard@univ‑tours.fr, melanie.fauconnier@univ‑tours.fr, spiv@univ‑tours.fr, etc.) qui pourraient être utilisées pour l’envoi du projet. Cependant, aucune de ces adresses n’est mentionnée dans la réponse, et le contexte ne fournit pas d’adresse postale. Le contexte est donc partiellement utile mais ne couvre pas la réponse donnée.

### Question : Comment m’inscrire / me réinscrire ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La plupart des étapes décrites (création du compte ADUM, rassemblement des pièces, validation par la direction de thèse et du laboratoire, réception d'un mail) sont directement tirées du contexte. Cependant, le nom "Christele Gaudron‑Bredif" et l'adresse e‑mail "gaudron@univ-tours.fr" n'apparaissent pas dans le texte fourni (le contexte mentionne "Christèle GAUDRON" et l'e‑mail "christele.gaudron@univ-tours.fr"). Ces éléments sont donc des hallucinations.
- **Avis Answer Relevance** : La réponse répond précisément à la question « Comment m’inscrire / me réinscrire ? » en proposant des procédures distinctes pour l’inscription initiale et la réinscription, ce qui correspond exactement à la demande.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires : procédure d’inscription via ADUM, documents requis, validation par les différentes instances, réception d’un mail, ainsi que les contacts des gestionnaires d’écoles doctorales. Le système a pu s’appuyer sur ces éléments.

### Question : Quelles ressources le Pôle SAPS peut m’apporter ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La plupart des affirmations (incitation, formation, mobilisation, inspiration, services supports) sont directement tirées du contexte. Cependant, le système a ajouté un contact nommé « Anne Galopin – af.polytech@univ-tours.fr », qui n’apparaît nulle part dans le texte fourni, constituant une hallucination.
- **Avis Answer Relevance** : La réponse répond précisément à la question en listant les différentes ressources que le Pôle SAPS peut offrir (médiation, formation, mobilisation, inspiration, services supports) et propose un moyen de contact, ce qui est pertinent pour l’interrogation.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires : description de la stratégie SAPS, les services rattachés, le rôle du pôle et l’adresse e‑mail générique saps@univ‑tours.fr. Le système a donc pu s’appuyer sur un contexte très pertinent.

### Question : Y a-t-il des alumni ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 1.0/5
- **Avis Faithfulness** : La réponse ne contient aucune affirmation ; il n'y a donc aucune information qui puisse être en contradiction avec le contexte fourni. Aucun élément n'est halluciné.
- **Avis Answer Relevance** : La question porte sur l'existence d'alumni. La réponse est vide et ne fournit aucune information relative à la présence ou l'absence d'alumni, ne répond donc pas du tout à la question.
- **Avis Context Precision** : Le contexte récupéré porte sur les libertés d'expression, d'association, les procédures de domiciliation et d'hébergement des associations étudiantes, etc. Aucun de ces éléments ne traite des alumni, le contexte n'est donc pas pertinent pour répondre à la question.

### Question : Que propose le Pôle SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : missions du Pôle SAPS (répondre aux sollicitations extérieures, organiser des rencontres, accompagner les chercheurs, formations, boutique des sciences, label Teepee, valorisation des projets). Les contacts, les URLs et les événements cités figurent également dans le texte fourni. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond précisément à la question « Que propose le Pôle SAPS ? » en listant les services, les événements, les accompagnements et les ressources offerts par le pôle. Aucun hors‑sujet n’est introduit.
- **Avis Context Precision** : Le contexte récupéré contient l’ensemble des informations nécessaires : missions, événements, formations, accompagnement, contacts, sites web, etc. Il est donc parfaitement adapté pour répondre à la question.

### Question : - Qu’est-ce qu’une invention ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 3.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse indique qu'aucune définition d'invention n'est présente dans le contexte, ce qui est correct. Cependant, elle ajoute un contact e‑mail (drv-pi@univ-tours.fr) et fait référence à des documents "DOC 1 à DOC 5" qui n'apparaissent pas dans le contexte fourni. Ces éléments sont donc des hallucinations, ce qui fait baisser la note.
- **Avis Answer Relevance** : La réponse répond partiellement à la question en signalant l'absence de définition et en demandant plus de contexte. Elle ne fournit pas la définition recherchée, mais elle reste liée à la demande, d'où une note moyenne.
- **Avis Context Precision** : Le contexte fourni porte sur des décrets, des litiges et des modalités de dévolution des droits de propriété intellectuelle, mais ne contient aucune définition explicite d'une "invention". Le contexte est donc seulement vaguement lié au sujet.

### Question : - Je souhaite répondre à un Appel à projet?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 4.0/5
- **Avis Faithfulness** : La réponse utilise les contacts Justine Gillet et Juliette Piquard qui figurent bien dans le contexte, ainsi que la référence au laboratoire LIFAT qui apparaît dans la description du secteur de Juliette Piquard. Les étapes proposées (identifier l’appel, préparer le dossier, faire valider le budget, déposer la candidature, suivi) sont des inférences raisonnables à partir du texte sur le financement par appel à projet, mais ne sont pas explicitement énoncées dans le contexte. Le seul élément clairement halluciné est la mention « RAC obligatoire », qui n’apparaît nulle part dans le contexte.
- **Avis Answer Relevance** : La réponse répond directement à la question « Je souhaite répondre à un Appel à projet ? » en détaillant les étapes à suivre, les contacts utiles et des ressources complémentaires. Aucun hors‑sujet n’est présent.
- **Avis Context Precision** : Le contexte fourni contient les contacts pertinents, la description des appels à projet et les liens vers les plateformes de financement. Il ne donne pas de procédure pas à pas, mais fournit suffisamment d’informations pour élaborer une réponse. Il manque toutefois quelques détails explicites (ex. : liste complète des plateformes nationales et européennes) qui auraient pu être cités.

### Question : je suis en arrêt de travail, qui dois-je contacter ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 4.0/5
- **Avis Faithfulness** : La réponse indique que le médecin du travail doit être prévenu et que la DRH doit recevoir l’arrêt, ce qui est soutenu par le contexte (section « Le médecin du travail » et mentions de la DRH). En revanche, l’instruction d’informer son responsable hiérarchique et le lien URL proposé vers la page du SSU ne figurent pas dans le texte fourni, ce qui constitue une hallucination partielle.
- **Avis Answer Relevance** : La question porte sur les interlocuteurs à contacter en cas d’arrêt de travail. La réponse fournit une liste claire de trois interlocuteurs (responsable hiérarchique, médecin du travail/SSU, DRH), répondant directement à la demande.
- **Avis Context Precision** : Le contexte contient des informations sur le médecin du travail, le Service de Santé Universitaire et la DRH, suffisantes pour identifier les personnes à contacter, même si le rôle du responsable hiérarchique n’est pas explicitement mentionné.

### Question : Combien de temps va prendre mon inscription ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 4.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : le texte indique qu'aucun délai précis n’est fourni, que la durée dépend de plusieurs étapes (création du compte ADUM, dépôt du dossier, validation, prise de RDV) et le contact Guillaume Fialeix avec son e‑mail apparaît exactement dans le contexte. Aucun élément n’a été inventé.
- **Avis Answer Relevance** : La réponse répond directement à la question en expliquant qu’aucun délai exact n’est indiqué et en proposant de contacter le gestionnaire d’école doctorale pour obtenir une estimation, ce qui est la meilleure réponse possible compte tenu du manque d’information précise.
- **Avis Context Precision** : Le contexte récupéré contient la procédure d’inscription, les étapes à suivre et les contacts, mais il ne fournit pas de durée chiffrée. Il est donc pertinent mais ne comporte pas l’information temporelle recherchée, d’où une note légèrement inférieure.

### Question : Comment avoir un email ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse s’appuie majoritairement sur le contexte : l’adresse générique du service informatique (dsi@univ-tours.fr), le lien PAL, le fait que les doctorants reçoivent automatiquement un compte sur le domaine etu.univ-tours.fr, et que le service informatique de proximité gère les demandes. Le seul élément non présent dans le texte source est l’exemple d’adresse « prenom.nom@etu.univ-tours.fr », qui constitue une reformulation inventée.
- **Avis Answer Relevance** : La réponse répond directement à la question « Comment avoir un email ? » en expliquant la procédure à suivre, les contacts à utiliser et le domaine de l’adresse e‑mail universitaire.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires (adresse e‑mail du service, plateforme PAL, création automatique de comptes doctorants, domaine etu.univ‑tours.fr). La réponse exploite ces éléments.

### Question : - Je souhaite me procurer le formulaire de déclaration d’invention de l’université, à qui dois-je m’adresser ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 4.0/5, Context Precision: 3.0/5
- **Avis Faithfulness** : La réponse cite un contact qui n’apparaît pas dans le contexte (Justine Gillet, son adresse e‑mail et son rôle de responsable du service des déclarations d’invention). De plus, elle ajoute des précisions (référente en propriété intellectuelle, mention du laboratoire LIFAT) qui ne sont pas présentes dans le texte fourni. Seul le contact de Morgane Guibert est présent dans le contexte. Cette présence d’éléments inventés entraîne une faible fidélité.
- **Avis Answer Relevance** : La réponse répond à la question en indiquant à qui s’adresser pour obtenir le formulaire. Même si un des contacts est erroné, l’information principale (un interlocuteur) est fournie, ce qui rend la réponse globalement pertinente.
- **Avis Context Precision** : Le contexte fournit le nom et les coordonnées de Morgane Guibert ainsi qu’une référence au formulaire (disponible « à venir sur intranet »). Il ne mentionne toutefois aucun responsable nommé Justine Gillet. Le contexte est donc partiellement utile mais ne contient pas toutes les informations nécessaires pour répondre précisément.

### Question : Qui contacter pour toute demande d'ouvrages en service presse ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 1.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Aucune réponse n'a été fournie par le système, il n'y a donc aucune affirmation à vérifier par rapport au contexte. L'absence de contenu signifie qu'aucune information n'est confirmée comme fidèle au contexte.
- **Avis Answer Relevance** : La question demandait "Qui contacter pour toute demande d'ouvrages en service presse ?". Le système n'a fourni aucune information, donc il ne répond pas du tout à la question.
- **Avis Context Precision** : Le contexte récupéré contient une section "Vos interlocuteurs" avec le nom, l'e‑mail et le téléphone de Morgane Guibert, qui est clairement la personne à contacter pour les demandes d'ouvrages. Le contexte est donc parfaitement pertinent et complet pour répondre à la question.

### Question : comment enregistrer ma demande de formation hors-catalogue et quels documents dois-je fournir ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 1.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse ne s’appuie sur aucune information présente dans le contexte. Le nom « Anne Galopin » et l’adresse e‑mail « af.polytech@univ-tours.fr » n’apparaissent nulle part dans le texte fourni, ce qui constitue une hallucination complète.
- **Avis Answer Relevance** : La question porte sur la procédure d’enregistrement d’une demande de formation hors‑catalogue et les documents à fournir. La réponse ne mentionne ni la procédure, ni les documents requis, se limitant à un contact qui n’est pas lié à la demande. Elle est donc hors‑sujet.
- **Avis Context Precision** : Le contexte contient des informations générales sur les démarches administratives (contact d’un gestionnaire DRH, liste des pièces à fournir, organigramme DRH, cadre de travail, etc.) qui pourraient répondre à la question, mais il ne fournit pas de détail spécifique sur la formation hors‑catalogue. Le contexte est donc vaguement lié, justifiant un score de 2.

### Question : Mon jury de thèse est-il valide ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 1.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Aucune réponse n'a été fournie par le système. Par conséquent, il n'y a aucune affirmation à vérifier par rapport au contexte, ce qui conduit à la note minimale. Aucun élément n'est traçable dans le contexte car rien n'est présent.
- **Avis Answer Relevance** : La question « Mon jury de thèse est-il valide ? » n'a reçu aucune réponse. La pertinence est donc nulle, d'où la note 1.
- **Avis Context Precision** : Le contexte récupéré contient de nombreuses informations détaillées sur les exigences de validité d'un jury de thèse (nombre de membres, proportion d'extérieurs, HDR, équilibre hommes‑femmes, etc.). Le contexte est donc complet et parfaitement pertinent pour répondre à la question, justifiant la note maximale de 5.

### Question : quels types de financement de thèse existent ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte fourni : contrat doctoral ministériel, bourses régionale, départementale, industrielle, associative, bourses Campus France, convention CIFRE, contrats de recherche avec entreprises/associations/collectivités, appels à projets régionaux, nationaux et européens, programmes ANR, Labex, CIFRE/DGA/ADEME, financements étrangers, et le salaire des doctorants salariés. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question « quels types de financement de thèse existent ? » en listant les différentes catégories de financement de manière exhaustive et structurée.
- **Avis Context Precision** : Le contexte récupéré contenait toutes les informations nécessaires : il mentionnait les différents types de bourses, contrats, conventions, appels à projets et sources externes, ainsi que les spécificités pour les doctorants salariés. Le contexte était donc parfaitement ciblé.

### Question : - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autre CHRU?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 2.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse indique que l'utilisateur doit contacter Justine Gillet pour les questions d'échantillons du CHRU. Or, le contexte montre que la question concernant les échantillons du CHRU est associée à Claude‑Emmanuel BOUDET (ligne Santé). Aucun élément du contexte ne soutient que Justine Gillet soit le contact approprié pour ce sujet. Ainsi, plusieurs affirmations ne sont pas traçables dans le contexte, justifiant une note faible.
- **Avis Answer Relevance** : La réponse fournit un contact, mais ce contact n'est pas pertinent pour la question posée. Elle ne répond donc pas correctement à la demande de l'utilisateur, ce qui la rend peu pertinente.
- **Avis Context Precision** : Le contexte récupéré contient toutes les informations nécessaires : le nom, l'email et le téléphone de Claude‑Emmanuel BOUDET, ainsi que la description de la question liée aux échantillons du CHRU. Le contexte est donc très précis.

### Question : Je souhaite monter un projet, comment faire ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La plupart des informations (étapes du montage, le « Starter Pack », les contacts Justine Gillet et Juliette Piquard, l’adresse projets-etablissement@univ-tours.fr, le lien SPIV) sont directement présentes dans le contexte. Cependant, l’affirmation que Justine Gillet est le « contact principal (obligatoire) » pour le laboratoire LIFAT n’est pas mentionnée dans le contexte ; le contexte associe Justine Gillet au secteur Sciences et matériaux, tandis que LIFAT relève du secteur Sciences et technologies (contact Juliette Piquard). De plus, la référence « source : Guide du DU » n’apparaît pas. Ces éléments constituent des hallucinations, ce qui empêche d’attribuer la note maximale.
- **Avis Answer Relevance** : La réponse répond clairement à la question « comment monter un projet ? » en détaillant les étapes à suivre, les documents à préparer et les interlocuteurs à contacter. Même si elle se focalise sur le laboratoire LIFAT, elle fournit une procédure applicable à tout projet, ce qui la rend très pertinente.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires : les étapes du montage, la notion de « Starter Pack », les contacts des chargés d’affaires, l’adresse de saisine et le lien vers le service SPIV. Ainsi le contexte est parfaitement adapté.

### Question : - Comment protéger un savoir-faire ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La plupart des affirmations (confidentialité, NDA, usage du cahier de laboratoire, rôle du SPIV, inscription des inventeurs, régime de rémunération, références PPST) sont directement présentes dans le contexte. Cependant, le contact "Justine Gillet – justine.gillet@univ-tours.fr" n’apparaît nulle part dans le contexte fourni (il ne figure que dans le brouillon interne, qui ne fait pas partie du contexte). Cette information est donc une hallucination, ce qui empêche d’attribuer la note maximale.
- **Avis Answer Relevance** : La réponse répond précisément à la question « Comment protéger un savoir‑faire ? » en proposant des étapes concrètes (confidentialité, documentation, déclaration, formalisation, suivi). Aucun élément hors sujet n’est introduit.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires : exigences de confidentialité, NDA, cahier de laboratoire (papier et électronique), rôle du SPIV, procédure de déclaration d’invention, exigences d’inscription des inventeurs, régime de rémunération, et les mesures PPST. Le système a donc pu puiser dans un contexte très pertinent.

### Question : Je pars en mission, quelle pièce dois-je remplir ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 1.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse mentionne « Anne Galopin » et l'adresse e‑mail af.polytech@univ‑tours.fr, qui n'apparaissent nulle part dans le contexte fourni. Aucun élément de la réponse n'est traçable dans le texte, ce qui constitue une hallucination totale.
- **Avis Answer Relevance** : La question demande « quelle pièce dois‑je remplir ? » pour une mission. La réponse fournit uniquement un contact, sans indiquer de formulaire ou de document à remplir, ne répond donc pas du tout à la demande.
- **Avis Context Precision** : Le contexte contient des informations sur les documents à fournir pour les projets de recherche (accord de confidentialité, dossier scientifique, email de validation, dossier complet) ainsi que des consignes de prise de contact avec le SPV. Ces éléments sont pertinents pour identifier la « pièce » à remplir, mais le contexte ne mentionne pas explicitement le formulaire pour une mission. Ainsi, le contexte est vaguement lié mais incomplet.

### Question : Quel est le délai moyen entre la soumission d’un manuscrit et sa publication ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 1.0/5, Context Precision: 1.0/5
- **Avis Faithfulness** : La réponse fournie est vide ; il n'y a aucune affirmation à vérifier. Par conséquent, aucune information n'est en contradiction avec le contexte, ce qui correspond à une fidélité maximale.
- **Avis Answer Relevance** : Aucune réponse n'est donnée à la question « Quel est le délai moyen entre la soumission d’un manuscrit et sa publication ? ». La réponse ne traite pas du tout du sujet demandé.
- **Avis Context Precision** : Le contexte récupéré porte sur les procédures d'HDR, les exigences de dépôt de thèse, etc., et ne contient aucune donnée concernant le délai moyen entre soumission et publication. Le contexte n'est donc pas pertinent pour la question.

## Query_Mix_06_google_mono_trials.json

### Question : C’est quoi les SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : la signification de SAPS, le lien avec la loi LPR 2021, les objectifs de renforcer le pacte entre chercheurs et citoyens, la reconnaissance de la dimension science‑société, le rôle des pôles SAPS et les coordonnées d'Alice NUÉ. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La question porte uniquement sur la définition des SAPS. La réponse fournit cette définition ainsi que le cadre législatif et les objectifs associés, répondant pleinement à la demande.
- **Avis Context Precision** : Le contexte récupéré contient la définition exacte de SAPS, le cadre de la loi LPR, les objectifs et le contact d'Alice NUÉ. Il est donc parfaitement ciblé.

### Question : Comment peut-on changer le budget d’un projet ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend correctement le principe indiqué dans le contexte : toute modification budgétaire doit passer par le SPIV/SPV et nécessite un argumentaire scientifique ainsi qu’un budget révisé. Cependant, le nom « Mme Anne Galopin » et l’adresse e‑mail « af.polytech@univ-tours.fr » n’apparaissent nulle part dans le contexte fourni, ce qui constitue une hallucination. Le reste du contenu est bien ancré dans le texte source.
- **Avis Answer Relevance** : La réponse répond directement à la question « Comment changer le budget d’un projet ? » en décrivant la procédure à suivre et les documents à fournir. Aucun élément hors sujet n’est introduit.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires : la nécessité de passer par le SPIV/SPV, le rôle de l’antenne financière, les pièces à fournir, et la mention que la demande d’avenant n’est pas un accord définitif. Le texte récupéré est donc très pertinent.

### Question : Quelles sont les différentes démarches à effectuer ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement tirées du contexte fourni. Les éléments tels que le destinataire du dossier (Monsieur le Vice‑Président en charge de la Recherche), la transmission à la DRV‑RED, la liste des pièces (demande motivée, projet, avis, accords, liste des doctorants, ressources financières, engagements juridiques, cahier de laboratoire) ainsi que les procédures pour un nouvel agent (contact DRH, organigramme, pièces à fournir) et la procédure de soutenance de thèse (documents à déposer sur ADUM, circuit de validation) figurent bien dans le texte source. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La question demande les différentes démarches à effectuer. La réponse propose trois catégories de démarches (changement d’affectation recherche, accueil d’un nouvel agent, demande de soutenance de thèse) et décrit les étapes requises pour chacune, ce qui répond de façon ciblée et exhaustive à la demande.
- **Avis Context Precision** : Le contexte récupéré contient l’ensemble des informations nécessaires : la liste détaillée des pièces pour la mobilité, les consignes relatives à l’accueil d’un agent via la DRH, et les exigences pour la soutenance de thèse. Le système a donc exploité un contexte très pertinent.

### Question : - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire extérieur? Est-ce gratuit?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 3.0/5, Context Precision: 3.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : le besoin d’un encadrement contractuel est mentionné dans le texte, et l’adresse e‑mail de Justine Gillet figure dans le tableau. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse traite du cadre contractuel demandé, mais ne répond pas à la seconde partie de la question (« Est‑ce gratuit ? »). Elle ne fournit donc qu’une réponse partielle à la question posée.
- **Avis Context Precision** : Le contexte contient les informations nécessaires sur l’obligation d’un contrat et les coordonnées de Justine Gillet, mais il ne précise pas si les expérimentations sont gratuites. Le contexte est donc partiellement utile, mais incomplet pour répondre entièrement à la question.

### Question : A quelle adresse postale ou mail dois-je envoyer mon projet ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les informations fournies dans la réponse (l'adresse email projets-es-etablissement@univ-tours.fr) apparaissent explicitement dans le contexte (slide 4). Aucun élément n'est inventé.
- **Avis Answer Relevance** : La question demande l'adresse postale ou mail pour envoyer le projet. La réponse donne une adresse mail précise, ce qui répond directement à la demande.
- **Avis Context Precision** : Le contexte contient l'adresse email requise ainsi que d'autres contacts. L'information nécessaire était clairement présente, donc le contexte est parfaitement pertinent.

### Question : Comment m’inscrire / me réinscrire ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La plupart des étapes décrites (création du compte ADUM, lien, période d’inscription, documents requis, validation par les directions) sont présentes dans le contexte. Cependant le système a inventé un contact nommé « Christele Gaudron‑Bredif » avec l’e‑mail gaudron@univ‑tours.fr, qui n’apparaît pas dans le contexte (le contact réel est Christèle Gaudron, christele.gaudron@univ‑tours.fr). Cette hallucination empêche le score d’être maximal.
- **Avis Answer Relevance** : La réponse répond directement à la question « Comment m’inscrire / me réinscrire ? » en détaillant les procédures pour une première inscription et pour une réinscription, ce qui correspond exactement à la demande.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires (procédure ADUM, dates, documents, validation, lien, contacts). Le système a pu extraire ces éléments, donc le contexte est très précis.

### Question : Quelles ressources le Pôle SAPS peut m’apporter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : accompagnement aux dépôts de projets (conseil, montage budgétaire, identification de partenaires, lieux de diffusion, valorisation), les formations (vulgarisation, mediatraining, éthique, publics scolaires, préparation au concours « Ma Thèse en 180 s »), l’appui événementiel (participation à la Fête de la science, Semaine du cerveau, Nocturnes de l'Histoire, création d'animations, prêt de matériel) ainsi que le contact d'Alice NUÉ et le site saps.univ‑tours.fr. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question en listant les ressources que le Pôle SAPS peut fournir, sans digression.
- **Avis Context Precision** : Le contexte récupéré contient l’ensemble des informations nécessaires : missions du pôle, description des formations, accompagnement aux projets, soutien événementiel, contacts et site web. Il est donc parfaitement ciblé.

### Question : Y a-t-il des alumni ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 1.0/5, Context Precision: 1.0/5
- **Avis Faithfulness** : La réponse du système est vide. Aucun énoncé n'est présent, il n'est donc pas possible de vérifier la fidélité à un contexte. En l'absence de contenu, on considère que la réponse ne respecte pas le critère de fidélité.
- **Avis Answer Relevance** : La question porte sur l'existence d'alumni. Le système n'a fourni aucune information, ne répond donc pas du tout à la question.
- **Avis Context Precision** : Le contexte fourni ne contient aucune mention d'alumni ou d'un réseau d'anciens étudiants. Ainsi, même si le système avait répondu, le contexte ne serait pas pertinent pour la question. Le critère est donc noté au minimum.

### Question : Que propose le Pôle SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : accompagnement des chercheurs (montage de projets, mise en relation, formations), organisation d'événements (DéTours des sciences, Village des sciences, finale « Ma thèse en 180 secondes », festivals, participation à la Fête de la science, Semaine du cerveau, Nocturnes de l'Histoire), projets arts‑sciences (Ma thèse en BD, Kaléidoscope) et la Boutique des sciences. Le contact d'Alice NUE et son e‑mail figurent également dans le contexte. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question « Que propose le Pôle SAPS ? » en listant les services, formations, événements et accompagnements proposés. Aucun hors‑sujet n’est présent.
- **Avis Context Precision** : Le contexte fourni contient l’ensemble des informations nécessaires : missions du pôle, types d’accompagnement, catalogue de formations, exemples d’événements, projets interdisciplinaires et coordonnées. Il est donc parfaitement ciblé.

### Question : - Qu’est-ce qu’une invention ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 1.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse indique une adresse e‑mail (drv-pi@univ-tours.fr) qui n’apparaît nulle part dans le contexte fourni. Aucun élément du texte ne fournit une définition de l’invention, alors que la réponse prétend offrir une définition précise. Ainsi, la plupart des affirmations sont hallucinations.
- **Avis Answer Relevance** : La question demande « Qu’est‑ce qu’une invention ? ». La réponse ne fournit aucune définition et se contente de rediriger vers un contact, ce qui ne répond pas à la demande de l’utilisateur.
- **Avis Context Precision** : Le contexte contient la question « Qu’est‑ce qu’une invention ? » mais ne fournit pas la réponse attendue. Le contexte est donc seulement vaguement lié à la question, sans les informations nécessaires pour y répondre.

### Question : - Je souhaite répondre à un Appel à projet?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse cite les contacts Justine Gillet et Juliette Piquard avec leurs adresses e‑mail, qui figurent bien dans le contexte. Cependant, elle ajoute la mention « pour le laboratoire LIFAT », une précision qui n’est pas explicitement présente dans le contexte (LIFAT apparaît seulement comme un secteur, pas comme le laboratoire de l’utilisateur). Cette légère extrapolation empêche d’attribuer le score maximal.
- **Avis Answer Relevance** : La réponse répond à la demande en proposant des interlocuteurs pour aider à répondre à un appel à projet, ce qui est pertinent. L’ajout du laboratoire LIFAT n’est pas demandé et constitue un léger hors‑sujet, d’où un score de 4.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires : les questions récurrentes liées aux appels à projet et les coordonnées des chargés d’affaires, ainsi que la liste des interlocuteurs du SPIV. Le contexte est donc très précis pour répondre à la question.

### Question : je suis en arrêt de travail, qui dois-je contacter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte. Le texte indique que la gestion administrative et le versement du traitement sont assurés par la DRH et conseille de consulter l’organigramme de la DRH pour identifier le gestionnaire, exactement comme le contexte le mentionne. Les deux liens vers les pages « Congés maladie des agents titulaires » et « Congés maladie des agents contractuels » figurent également dans le contexte. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La question demande qui contacter en cas d’arrêt de travail. La réponse indique de prendre contact avec le gestionnaire de la DRH (via l’organigramme) et fournit les liens pertinents selon le statut de l’agent, répondant ainsi directement à la demande.
- **Avis Context Precision** : Le contexte fourni contient les informations nécessaires : les liens vers les pages de congés maladie pour titulaires et contractuels, ainsi que l’instruction de consulter l’organigramme de la DRH pour identifier le gestionnaire. Le contexte est donc parfaitement ciblé.

### Question : Combien de temps va prendre mon inscription ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 3.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte : le texte indique qu'aucune durée précise n'est fournie, décrit le circuit de validation et mentionne le contact Guillaume Fialeix avec son adresse e‑mail, qui figure bien dans le contexte. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond directement à la question « Combien de temps va prendre mon inscription ? » en précisant que la durée exacte n’est pas indiquée et en proposant de contacter le gestionnaire concerné. Aucun hors‑sujet n’est introduit.
- **Avis Context Precision** : Le contexte contient des informations sur la procédure d’inscription et les contacts, mais il ne fournit pas de durée chiffrée. Ainsi, le contexte est partiellement utile mais ne possède pas la donnée recherchée, d’où la note moyenne.

### Question : Comment avoir un email ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 3.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse (existence d'un compte étudiant sur le domaine etu.univ-tours.fr, validité à l'année universitaire et prolongation après réinscription) sont directement tirées du contexte. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse indique que le doctorant possède une messagerie grâce à son compte, ce qui répond partiellement à la question « Comment avoir un email ? ». Cependant, elle ne décrit pas les étapes concrètes pour obtenir ce compte ou créer l'adresse email, ce qui limite la pertinence.
- **Avis Context Precision** : Le contexte fourni contient les informations nécessaires sur le compte informatique du doctorant, le domaine de messagerie et la validité du compte. Ces informations sont exactement celles utilisées dans la réponse.

### Question : - Je souhaite me procurer le formulaire de déclaration d’invention de l’université, à qui dois-je m’adresser ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 2.0/5, Context Precision: 4.0/5
- **Avis Faithfulness** : La réponse mentionne un contact nommé Justine Gillet (justine.gillet@univ-tours.fr) qui n’apparaît nulle part dans le contexte fourni. C’est donc une hallucination. Le reste de la réponse (le rôle du SPIV) est présent dans le contexte, mais la présence d’une information erronée diminue fortement la fidélité.
- **Avis Answer Relevance** : La réponse tente de répondre à la question en donnant un interlocuteur, mais l’interlocuteur proposé est faux. Ainsi, la réponse ne satisfait pas réellement la demande de l’utilisateur, ce qui la rend peu pertinente.
- **Avis Context Precision** : Le contexte contient des informations utiles : la présence de Morgane Guibert comme interlocuteur et la mention du Service Partenariats Innovations Valorisation (SPIV) chargé des déclarations d’invention. Le contexte est donc pertinent, même s’il ne donne pas explicitement le nom d’un interlocuteur dédié au formulaire.

### Question : Qui contacter pour toute demande d'ouvrages en service presse ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 1.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Aucune réponse n'a été fournie, il est donc impossible de vérifier que les affirmations proviennent du contexte. Aucun élément n'est traçable, ce qui conduit à la note la plus basse.
- **Avis Answer Relevance** : La question n'a reçu aucune réponse, donc elle n'est pas du tout pertinente par rapport à la demande de savoir qui contacter pour les ouvrages en service presse.
- **Avis Context Precision** : Le contexte contient les informations nécessaires (Service de la Commande Publique avec son adresse e‑mail, Service Technique de l’Immobilier, etc.) pour répondre à la question. Ainsi, le contexte est très précis et complet pour le besoin.

### Question : comment enregistrer ma demande de formation hors-catalogue et quels documents dois-je fournir ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement tirées du contexte : connexion à ADUM, navigation vers l'espace personnel → rubrique formations → déclaration des formations hors-catalogue, les informations à renseigner (intitulé, catégorie, année, dates, organisateur, heures, compétences, programme) et les documents obligatoires (fiche de demande complétée et justificatifs). La contrainte du PDF unique, la non‑traitement des dossiers incomplets, la fréquence de traitement mensuelle et la notification par e‑mail sont également présentes dans le texte source. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question posée en expliquant comment enregistrer la demande hors‑catalogue et quels documents fournir, sans digression.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires (procédure d’enregistrement, champs à remplir, documents à joindre, format du dépôt, modalités de traitement). Le système les a correctement exploitées.

### Question : Mon jury de thèse est-il valide ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement tirées du texte fourni : nombre de membres (4‑8), répartition moitié/mi‑moitié (professeurs, extérieurs à l’unité, extérieurs à l’établissement, non impliqués), présence d’au moins un HDR, limitation des membres émérites, nombre maximal de membres invités, objectif de parité, et évaluation au cas‑par‑cas par le directeur de l’École Doctorale. Aucun élément n’est ajouté en dehors du contexte.
- **Avis Answer Relevance** : La réponse répond exactement à la question « Mon jury de thèse est‑il valide ? » en listant les critères qui déterminent la validité d’un jury. Elle fournit les informations nécessaires pour que l’utilisateur puisse vérifier la conformité de son jury.
- **Avis Context Precision** : Le contexte fourni contient l’ensemble des règles citées dans la réponse. Les informations recherchées (composition, exigences, limites, parité, rôle des membres émérites et invités) sont toutes présentes dans le texte du contexte.

### Question : quels types de financement de thèse existent ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Les quatre types de financement (contrat doctoral, financement ANRT/CIFRE, contrat de travail ou attestation de l'employeur, attestation de bourse) sont exactement présents dans le contexte, ce qui est correct. En revanche, le système a inventé un contact nommé « Christele Gaudron-Bredif » avec l'e‑mail « gaudron@univ-tours.fr », qui ne figurent pas dans le contexte (le nom réel est Christèle Gaudron et l'e‑mail est christele.gaudron@univ-tours.fr). Cette information erronée constitue une hallucination, d'où la note moyenne.
- **Avis Answer Relevance** : La réponse répond directement à la question en listant les types de financement de thèse demandés. Le supplément d'information de contact, bien que non requis, ne nuit pas à la pertinence de la réponse.
- **Avis Context Precision** : Le contexte contient précisément la liste des justificatifs de financement, qui suffit pour répondre à la question. Aucun élément essentiel n’est absent du contexte.

### Question : - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autre CHRU?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 2.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse indique de contacter Justine Gillet (justine.gillet@univ-tours.fr). Or, dans le contexte, la question sur le volet clinique ou les échantillons du CHRU est associée à Claude‑Emmanuel BOUDET, pas à Justine Gillet. Cette information n’est donc pas présente dans le contexte et constitue une hallucination.
- **Avis Answer Relevance** : La réponse tente de répondre à la question en proposant un contact, mais le contact fourni est incorrect. Elle reste donc partiellement pertinente, mais ne répond pas correctement à la demande.
- **Avis Context Precision** : Le contexte récupéré contient exactement la question posée ainsi que le nom, l'email et le téléphone du chargé d’affaires approprié (Claude‑Emmanuel BOUDET). Le contexte est donc parfaitement pertinent.

### Question : Je souhaite monter un projet, comment faire ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend les étapes du "Starter Pack" et le rôle du SPIV qui sont décrits dans le contexte. Le contact Justine Gillet et son adresse e‑mail sont bien présents dans le contexte. En revanche, l’affirmation "au sein du laboratoire LIFAT" n’est pas mentionnée dans le contexte (LIFAT apparaît seulement dans une liste de secteurs) et le qualificatif "interlocutrice principale" n’est pas explicitement indiqué. Ces éléments constituent de légères hallucinations, d’où la note 4.
- **Avis Answer Relevance** : La réponse répond directement à la question « comment monter un projet ? » en proposant les étapes concrètes et le contact à solliciter. Aucun hors‑sujet n’est présent, justifiant la note maximale.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires (étapes du montage, contacts, rôle du SPIV). La réponse s’appuie entièrement sur ces éléments, d’où la note 5.

### Question : - Comment protéger un savoir-faire ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend correctement les notions de secret, d’accord de confidentialité et le rôle du SPIV, qui sont présentes dans le contexte. Cependant, elle introduit un contact nommé « Justine Gillet » avec une adresse e‑mail qui n’apparaît nulle part dans le contexte fourni, constituant une hallucination.
- **Avis Answer Relevance** : La réponse répond directement à la question en expliquant que le secret et les accords de confidentialité sont essentiels pour protéger un savoir‑faire, et indique le service SPIV comme interlocuteur, ce qui est pertinent et utile.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires pour répondre à la question : exigences de confidentialité, NDA, rôle du SPIV, et outils comme le cahier de laboratoire. Le contexte est donc très précis.

### Question : Je pars en mission, quelle pièce dois-je remplir ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 1.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse mentionne un contact (Anne Galopin, af.polytech@univ-tours.fr) qui n’apparaît nulle part dans le contexte fourni. Aucun élément de la réponse ne peut être retracé dans le texte source, ce qui constitue une hallucination totale.
- **Avis Answer Relevance** : La question demande « quelle pièce dois-je remplir ? » en vue d’une mission. La réponse fournit uniquement un contact, ne répondant pas du tout à la demande de formulaire ou de pièce à remplir.
- **Avis Context Precision** : Le contexte contient des informations sur les documents requis pour les soumissions de projets (accord de confidentialité, dossier scientifique, email de validation, dossier complet) ainsi que plusieurs contacts universitaires, mais aucune indication précise sur une « pièce » liée à une mission. Le contexte est donc seulement vaguement lié au sujet de la question.

### Question : Quel est le délai moyen entre la soumission d’un manuscrit et sa publication ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 1.0/5, Context Precision: 3.0/5
- **Avis Faithfulness** : La réponse ne cite aucun élément présent dans le contexte. Le contact "Jeanne Hélouis" et son adresse e‑mail n’apparaissent nulle part dans le texte fourni, il s’agit donc d’une hallucination complète.
- **Avis Answer Relevance** : La question porte sur le délai moyen entre la soumission d’un manuscrit et sa publication. La réponse ne fournit aucune information à ce sujet, se limitant à un contact hors sujet.
- **Avis Context Precision** : Le contexte contient des informations pertinentes sur les délais légaux (maximum de six mois pour les sciences, douze mois pour les SHS). Cependant, il ne donne pas de délai moyen. Le contexte est donc partiellement utile, mais incomplet pour répondre à la question.

## Query_Mix_09_premium_cross_trials.json

### Question : C’est quoi les SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement tirées du contexte : la définition « Sciences Avec et Pour la Société », le lien avec la loi LPR 2021, le rôle du Ministère de l'Enseignement supérieur et de la Recherche, et les objectifs de rapprochement et de dialogue. Le contact indiqué (Alice NUE / alice.nue@univ-tours.fr) correspond exactement à la personne listée dans la section CONTACTS (Alice NUÉ). Aucun élément n’est inventé.
- **Avis Answer Relevance** : La question porte uniquement sur la définition des SAPS. La réponse fournit une définition claire, les objectifs concrets et même un contact utile, répondant ainsi pleinement à la demande.
- **Avis Context Precision** : Le contexte récupéré (Slide 2) contient la définition, le cadre législatif (loi LPR 2021) et les objectifs des SAPS. Il était donc parfaitement adapté pour répondre à la question.

### Question : Comment peut-on changer le budget d’un projet ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend correctement les étapes décrites dans le contexte (argumentaire scientifique, budget modifié, transmission au SPIV, attente de l’accord du financeur, variabilité des délais). Cependant, elle introduit des éléments qui n’apparaissent pas dans le contexte : le laboratoire « LIFAT », le nom « Anne Galopin » et l’adresse e‑mail « af.polytech@univ-tours.fr ». Ces informations sont donc des hallucinations, ce qui empêche d’attribuer la note maximale.
- **Avis Answer Relevance** : La réponse répond directement à la question « Comment changer le budget d’un projet ? » en décrivant la procédure à suivre. Aucun élément hors sujet n’est présent.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires (rôle du SPIV, de l’antenne financière, besoin d’un argumentaire, budget modifié, attente de l’accord du financeur, délais). Il est donc parfaitement pertinent.

### Question : Quelles sont les différentes démarches à effectuer ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement tirées du contexte fourni : la liste des pièces (demande motivée, projet de recherche, avis du directeur, accord du directeur d'arrivée, liste des doctorants, ressources financières, engagements juridiques, matériel expérimental, cahier de laboratoire) ainsi que les étapes de transmission à la DRV‑RED, l’avis de la commission recherche, le conseil académique et la procédure en cas de refus sont présentes dans le texte. Aucun élément n’a été inventé.
- **Avis Answer Relevance** : La question demande les différentes démarches à effectuer. La réponse décrit précisément les démarches (constitution du dossier, pièces à fournir, transmission, instruction, avis, décision, recours) et répond donc de façon ciblée et exhaustive à la demande.
- **Avis Context Precision** : Le contexte récupéré contient l’ensemble des informations nécessaires : la liste détaillée des documents et accords requis ainsi que la procédure de soumission et de décision. Le modèle a pu s’appuyer entièrement sur ce contexte.

### Question : - Dans quel cadre puis-je réaliser des expérimentations avec un partenaire extérieur? Est-ce gratuit?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 3.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse mentionne correctement qu’une collaboration doit être encadrée par un contrat et un accord de confidentialité, ce qui figure dans le contexte. En revanche, elle indique que les expérimentations se font « dans le cadre du laboratoire LIFAT » et propose de contacter Justine Gillet. Aucun élément du contexte ne lie LIFAT à la question ni ne désigne Justine Gillet comme interlocuteur pour ce sujet (c’est Hélène Jullien qui est listée). Ces affirmations sont donc inventées ou mal attribuées.
- **Avis Answer Relevance** : La réponse répond partiellement à la question : elle indique qu’un contrat et un accord de confidentialité sont nécessaires et propose un interlocuteur, mais l’interlocuteur est erroné et la réponse ne précise pas clairement si les expérimentations peuvent être gratuites. Ainsi, la pertinence est moyenne.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires : la question exacte, la nécessité d’un contrat/confidentialité, et les coordonnées d’Hélène Jullien. Le contexte est donc très précis pour répondre à la question.

### Question : A quelle adresse postale ou mail dois-je envoyer mon projet ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les informations fournies dans la réponse (l'adresse e‑mail guillaume.fialeix@univ-tours.fr) apparaissent textuellement dans le contexte. Aucun élément n'est inventé.
- **Avis Answer Relevance** : La réponse répond à la question en donnant une adresse e‑mail valide, mais elle ne mentionne pas les autres adresses possibles (ex. celle de l'Université d'Orléans) ni d'éventuelles adresses postales, ce qui la rend partiellement pertinente.
- **Avis Context Precision** : Le contexte contient plusieurs adresses e‑mail (pour Orléans, Tours, etc.) qui permettent de répondre à la question. Le contexte est donc pleinement pertinent.

### Question : Comment m’inscrire / me réinscrire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte : création du compte ADUM avec le lien fourni, période d’inscription (1 juin‑15 novembre), documents à fournir, exigences de validation (direction de thèse, laboratoire, école doctorale, représentant du chef), réception d’un mail de confirmation, suivi sur l’espace ADUM, et procédure de dérogation pour la 4ᵉ/5ᵉ année. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question « Comment m’inscrire / me réinscrire ? » en décrivant la procédure pas à pas, les conditions et les étapes de suivi, sans digression hors sujet.
- **Avis Context Precision** : Le contexte récupéré contient toutes les informations nécessaires : lien ADUM, dates limites, pièces à fournir, validation par les différentes instances, notifications par mail, suivi du dossier, et spécificités pour les années supérieures. Le système a donc utilisé un contexte très pertinent.

### Question : Quelles ressources le Pôle SAPS peut m’apporter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement présentes dans le contexte fourni : accompagnement de projets, formations (médiatraining, Ma Thèse en 180s, gestion des fake news, CERCIP, Maison pour la Science), événements (DéTours des sciences, Finale régionale, Village des sciences, Fête de la science, etc.), projets arts‑sciences, boutique des sciences, label SAPS Teepee, festival (Re)Cherche et trouve, identification de prestataires et soutien aux publics éloignés. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond exactement à la question « Quelles ressources le Pôle SAPS peut‑moi apporter ? » en listant les différentes formes d’accompagnement, de formation, d’événements, d’outils et de financements disponibles.
- **Avis Context Precision** : Le contexte récupéré contient l’ensemble des informations nécessaires : missions du pôle, catalogue de formations, description des événements, détails sur le label et la boutique, contacts, etc. Il est donc parfaitement ciblé.

### Question : Y a-t-il des alumni ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse indique qu'aucune information sur un réseau d'alumni n'est présente dans les documents consultés, ce qui correspond au contenu du contexte (aucune mention d'alumni). Cependant, elle propose de contacter le "service des Relations avec les Anciens", service qui n'apparaît pas dans le contexte, constituant une petite hallucination.
- **Avis Answer Relevance** : La question porte sur l'existence d'alumni. La réponse répond directement en indiquant l'absence d'information et en suggérant des interlocuteurs potentiels, ce qui est pleinement pertinent.
- **Avis Context Precision** : Le contexte fourni ne contient aucune information relative aux alumni ou à un réseau d'anciens. Il est donc peu précis pour répondre à la question, se limitant à des sections administratives et de services divers.

### Question : Que propose le Pôle SAPS ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont présentes dans le contexte fourni : missions du pôle, exemples d'événements (DéTours des sciences, Ma thèse en 180 s, Festival (Re)Cherche et trouve), formations (Jeudis des SAPS, médiatraining, CERCIP), projets (Label SAPS Teepee, boutique des sciences), contacts (Alice NUE, etc.) et le site saps.univ‑tours.fr. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond directement à la question « Que propose le Pôle SAPS ? » en listant les services, formations, événements et accompagnements offerts, ce qui correspond exactement à ce qui était demandé.
- **Avis Context Precision** : Le contexte récupéré contient l’ensemble des informations nécessaires : missions, activités, projets, contacts, URLs, etc. Il est donc parfaitement ciblé.

### Question : - Qu’est-ce qu’une invention ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 2.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse mentionne une adresse e‑mail (drv-pi@univ-tours.fr) et indique qu'il faut contacter le PJR pour obtenir la définition d'une invention. Aucun de ces éléments n’apparaît dans le contexte fourni ; le contexte ne contient aucune adresse de contact. Ainsi la réponse introduit des informations non présentes dans le texte source, ce qui la rend peu fidèle.
- **Avis Answer Relevance** : La question demande la définition d’une invention. La réponse ne fournit aucune définition, se limitant à rediriger l’interlocuteur vers le PJR. Elle ne répond donc pas directement à la demande, ce qui la rend peu pertinente.
- **Avis Context Precision** : Le contexte récupéré ne comporte pas de définition d’une invention, seulement la mention de la question « Qu’est‑ce qu’une invention ? ». Le texte ne fournit donc pas les informations nécessaires pour répondre à la question, ce qui rend le contexte insuffisant.

### Question : - Je souhaite répondre à un Appel à projet?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse utilise les contacts présents dans le contexte (Juliette Piquard, Justine Gillet, SPIV). Cependant, le numéro de téléphone attribué à Juliette Piquard (02 47 36 79 74) n’apparaît nulle part dans le contexte fourni, ce qui constitue une hallucination. De plus, l’affirmation « dans le cadre du laboratoire LIFAT » n’est pas explicitement mentionnée, mais reste une inférence raisonnable.
- **Avis Answer Relevance** : La réponse répond directement à la question en indiquant quels interlocuteurs contacter pour répondre à un appel à projet, ce qui correspond exactement à la demande.
- **Avis Context Precision** : Le contexte contient les informations nécessaires : contacts des chargés d’affaires, description du service SPIV et la mention que plusieurs d’entre eux (dont Justine Gillet) traitent des appels à projet. Le contexte est donc pleinement pertinent.

### Question : je suis en arrêt de travail, qui dois-je contacter ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 3.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement tirées du contexte : les deux liens vers les pages « congés maladie des agents titulaires » et « congés maladie des agents contractuels » existent bien dans le texte fourni. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse indique où trouver les procédures, mais la question demandait explicitement « qui dois‑je contacter ? ». La réponse ne fournit pas de contact (nom, e‑mail, service) et se contente de rediriger vers des pages, ce qui ne répond pas pleinement à la demande.
- **Avis Context Precision** : Le contexte contient précisément les deux liens mentionnés dans la réponse, ainsi que des informations sur les congés maladie. Le système a donc utilisé les bonnes parties du contexte.

### Question : Combien de temps va prendre mon inscription ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 3.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse indique que le délai d’instruction « peut prendre quelques jours à quelques semaines » et propose de contacter Guillaume Fialeix (guillaume.fialeix@univ-tours.fr). Aucun de ces éléments n’apparaît dans le contexte fourni ; le contexte décrit les étapes de validation mais ne donne aucune estimation de durée ni le nom de Guillaume Fialeix. Ces affirmations sont donc des hallucinations.
- **Avis Answer Relevance** : La question porte sur la durée de l’inscription. La réponse tente de répondre en donnant une estimation de durée, mais cette estimation n’est pas tirée du contexte et reste vague. Elle reste donc partiellement pertinente, mais repose sur des informations non fondées.
- **Avis Context Precision** : Le contexte décrit le processus d’inscription (validation par la direction de thèse, laboratoire, école doctorale, etc.) mais ne fournit pas d’information chiffrée sur le temps nécessaire. Le contexte est donc seulement vaguement lié à la question de durée.

### Question : Comment avoir un email ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement tirées du contexte : le compte « étudiant établissement » sur le domaine etu.univ-tours.fr, l’accès à la messagerie et aux services numériques, la nécessité de contacter le service informatique de proximité et le lien fourni vers la liste des informaticiens. Aucun élément n’est inventé.
- **Avis Answer Relevance** : La réponse répond précisément à la question « Comment avoir un email ? » en expliquant les étapes à suivre (activer le compte, contacter le service informatique) et en fournissant le lien utile. Aucun hors‑sujet n’est présent.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires : existence du compte étudiant, domaine etu.univ-tours.fr, services associés, et le lien vers le service informatique de proximité. Il est donc parfaitement ciblé.

### Question : - Je souhaite me procurer le formulaire de déclaration d’invention de l’université, à qui dois-je m’adresser ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 2.0/5, Context Precision: 3.0/5
- **Avis Faithfulness** : La réponse indique que le formulaire doit être demandé à Justine Gillet (nom et adresse e‑mail). Aucun de ces éléments n’apparaît dans le contexte fourni ; le seul interlocuteur présent est Morgane Guibert. Ainsi la réponse introduit des informations inventées, ce qui la rend non fidèle au contexte.
- **Avis Answer Relevance** : La réponse tente de répondre à la question en donnant un contact, mais le contact fourni est erroné. Elle ne répond donc que partiellement à la demande de l’utilisateur.
- **Avis Context Precision** : Le contexte contient des contacts (Morgane Guibert) et mentionne le formulaire (disponible sur l’intranet), mais il ne précise pas explicitement qui contacter. Le contexte est donc partiellement utile, mais il manque le lien direct vers le formulaire ou le responsable indiqué.

### Question : Qui contacter pour toute demande d'ouvrages en service presse ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 2.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse indique qu'aucune information n'a été trouvée, puis propose de contacter le Service Communication avec un lien vers son annuaire. Aucun élément du contexte ne mentionne un Service Communication ni l'URL fournie, ce qui constitue une hallucination. Toutes les affirmations ne sont donc pas traçables dans le contexte.
- **Avis Answer Relevance** : La question demande le contact pour les demandes d'ouvrages en service presse. La réponse ne fournit pas le contact recherché et propose un service qui n'est pas mentionné dans le contexte, ce qui ne répond pas correctement à la question.
- **Avis Context Precision** : Le contexte fourni ne contient pas d'information explicite sur un service presse ou un contact dédié. Il comporte d'autres contacts (ex. Aurélie PETEREAU, Service de la Commande Publique) qui ne répondent pas à la demande, d'où une pertinence limitée du contexte pour la question.

### Question : comment enregistrer ma demande de formation hors-catalogue et quels documents dois-je fournir ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement tirées du contexte fourni. Les étapes (connexion ADUM, rubrique Formations, sélection de 'déclaration des formations hors-catalogue'), les champs à renseigner et les documents à joindre (fiche de demande de validation des crédits doctoraux et justificatifs) sont exactement décrits dans le texte. Aucun élément n'est ajouté ou modifié.
- **Avis Answer Relevance** : La réponse répond précisément à la question en expliquant comment enregistrer la demande hors-catalogue et quels documents fournir, sans digression.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires : procédure d’enregistrement, champs requis, documents à joindre, et mention de l’envoi préalable par email. Le système a utilisé ces informations de façon ciblée.

### Question : Mon jury de thèse est-il valide ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 4.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend presque intégralement les critères décrits dans le contexte (nombre de membres, répartition des profils, HDR, équilibre de genre, membres invités, rapporteurs). Le seul élément qui ne figure pas dans le contexte est la mention « procédures en vigueur à l'Université de Tours », qui est une information ajoutée et donc une hallucination. Aucun autre détail n'est inventé.
- **Avis Answer Relevance** : La question porte sur la validité du jury. La réponse fournit les critères à vérifier pour juger de la validité, ce qui est pertinent et utile, même si elle ne donne pas de réponse définitive « oui / non » pour le jury spécifique de l'utilisateur.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires sur la composition du jury, les exigences de genre, les membres invités, les rapporteurs HDR, etc. La réponse utilise correctement ces informations.

### Question : quels types de financement de thèse existent ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse reprend correctement les quatre types de financement mentionnés dans le contexte (contrat doctoral, CIFRE, contrat de travail/attestation employeur, bourse). Cependant, le nom et l'adresse e‑mail du contact fourni ("Christele Gaudron-Bredif" et "gaudron@univ-tours.fr") n'apparaissent pas dans le contexte, qui cite "Christèle Gaudron" et "christele.gaudron@univ-tours.fr". Ces éléments sont donc des hallucinations, ce qui empêche d'attribuer le score maximal.
- **Avis Answer Relevance** : La réponse répond directement à la question en listant les types de financement de thèse. L'ajout d'un contact est supplémentaire mais reste lié au sujet, donc la pertinence est maximale.
- **Avis Context Precision** : Le contexte contient exactement les informations nécessaires (la liste des justificatifs de financement). Il est donc parfaitement pertinent pour répondre à la question.

### Question : - ou bien avec des échantillons en provenance du CHRU de Tours ou d'un autre CHRU?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 2.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La réponse indique que l’interlocuteur est Justine Gillet (Sciences et matériaux) et mentionne le laboratoire LIFAT, aucune de ces informations n’apparaît dans le contexte fourni pour la question sur les échantillons du CHRU. Le contexte désigne Claude‑Emmanuel BOUDET comme la personne concernée. Ainsi la majorité des affirmations sont hallucinations.
- **Avis Answer Relevance** : La réponse tente de répondre à la question en proposant un contact, mais le contact proposé est incorrect. Elle ne répond donc pas réellement à la demande de l’utilisateur.
- **Avis Context Precision** : Le contexte contient la bonne information : la question sur les échantillons du CHRU figure sous Claude‑Emmanuel BOUDET, avec ses coordonnées. Le contexte est donc pleinement pertinent.

### Question : Je souhaite monter un projet, comment faire ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La plupart des étapes (préparer le Starter Pack, l’envoyer au chargé d’affaires, vérification & signature, dépôt) sont directement tirées du contexte. Cependant, l’affirmation que Justine Gillet est l’interlocutrice dédiée pour le LIFAT n’apparaît pas dans le texte fourni ; Justine Gillet est associée aux Sciences et matériaux, tandis que LIFAT est mentionné sous le secteur Sciences et technologies. Cette association constitue une hallucination.
- **Avis Answer Relevance** : La réponse répond clairement à la question « comment monter un projet ? » en décrivant les étapes concrètes et en proposant un contact, ce qui la rend très pertinente.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires : les étapes du montage, la notion de Starter Pack, le rôle du chargé d’affaires et plusieurs contacts. Le système a pu extraire ces éléments.

### Question : - Comment protéger un savoir-faire ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : La plupart des affirmations sont directement tirées du contexte (confidentialité, rôle du SPIV, usage du cahier électronique, mesures PPST, bonnes pratiques de déplacement). Cependant, la réponse introduit deux éléments qui n’apparaissent pas dans le contexte : le nom du laboratoire « LIFAT » et l’adresse e‑mail « justine.gillet@univ-tours.fr ». Ces informations sont donc des hallucinations.
- **Avis Answer Relevance** : La réponse répond clairement à la question « Comment protéger un savoir‑faire ? » en proposant des actions concrètes (confidentialité, cahier électronique, mesures PPST, sécurisation des déplacements) et en indiquant le service d’accompagnement. Aucun élément hors sujet n’est présent.
- **Avis Context Precision** : Le contexte fourni contient toutes les informations nécessaires pour répondre : exigences de confidentialité, rôle du SPIV, existence du cahier de laboratoire électronique, cadre PPST et consignes de sécurité lors de déplacements. Le système a correctement exploité ces sources.

### Question : Je pars en mission, quelle pièce dois-je remplir ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 3.0/5, Context Precision: 4.0/5
- **Avis Faithfulness** : La réponse mentionne l’Ordre de Mission et l’État liquidatif, qui sont bien présents dans le contexte. Cependant, elle ajoute un contact (Anne Galopin : af.polytech@univ‑tours.fr) et un lien avec un paramètre ID_FICHE=XXXXXX qui n’apparaissent nulle part dans le texte fourni. Ces éléments sont donc des hallucinations.
- **Avis Answer Relevance** : La question porte sur la pièce à remplir pour une mission. La réponse indique deux pièces (OM et état liquidatif), ce qui répond partiellement à la demande, mais le contexte indique également d’autres documents (accord de confidentialité, dossier scientifique, email de validation, dossier complet) qui ne sont pas mentionnés. La réponse est donc partiellement pertinente.
- **Avis Context Precision** : Le contexte contient bien les informations nécessaires (liste des documents, mentions de l’Ordre de Mission et de l’État liquidatif). Il est donc pertinent, même s’il offre davantage de détails que la réponse ne les exploite.

### Question : Quel est le délai moyen entre la soumission d’un manuscrit et sa publication ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 4.0/5, Context Precision: 2.0/5
- **Avis Faithfulness** : La réponse indique correctement que le contexte ne fournit pas de délai moyen entre soumission et publication. Cependant, elle ajoute un contact (Jeanne Hélouis, jeanne.helouis@univ-tours.fr) qui n’apparaît nulle part dans le contexte, constituant une hallucination.
- **Avis Answer Relevance** : La réponse répond à la question en expliquant qu’elle ne peut pas fournir le délai demandé parce qu’il n’est pas présent dans le contexte, ce qui est pertinent et utile.
- **Avis Context Precision** : Le contexte ne contient pas l’information recherchée (délai moyen entre soumission et publication). Il ne fournit que des délais de mise à disposition en open‑access (6 mois / 12 mois), qui ne répondent pas directement à la question.

## Query3_rag_batch_trials.json

### Question : Quelles sont les étapes pour soumettre un manuscrit ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 4.0/5

### Question : A qui puis-je adresser mon projet de publication ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Reasoning global** : {'faithfulness': "La réponse s'appuie strictement sur le contexte fourni (ex. : mention explicite du PJR, de la mission 'conventions d'aide à publication', et des contacts comme Anouk Martinet). Aucune information externe ou hallucinée n'est introduite.", 'answer_relevance': "La réponse est directement utile et ciblée : elle identifie le service compétent (PJR), précise le type de convention concerné (aide à publication), et fournit un contact dédié avec des détails pratiques (email, rôle). L'ajout d'informations complémentaires (droits d'auteur, contrats d'édition) est pertinent car lié au sujet.", 'context_precision': "Le contexte contient toutes les informations nécessaires pour répondre : la section **B. Sur les contrats** liste explicitement les 'conventions d'aide à publication' comme relevant du PJR, et les contacts (y compris Anouk Martinet) sont clairement indiqués. Les détails sur les missions du PJR (droit d'auteur, contrats d'édition) confirment la précision du contexte."}

### Question : A quelle adresse postale ou mail dois-je envoyer mon projet ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Avis Faithfulness** : {'score': 4, 'explanation': "La réponse s'appuie majoritairement sur le contexte fourni (adresses de Juliette Piquard et du SPIV, mention des 2 semaines avant clôture). Cependant, elle introduit une information non présente dans le contexte : *« Contact à utiliser : Anne Galopin : af.polytech@univ-tours.fr »*, ce qui constitue une **hallucination mineure** (d'où un 4/5 au lieu de 5)."}
- **Avis Answer Relevance** : {'score': 5, 'explanation': "La réponse est **directement utile** : elle identifie le bon interlocuteur (Juliette Piquard pour le LIFAT), fournit les adresses pertinentes (individuelle + générique SPIV), et rappelle une règle clé (délai de 2 semaines). Elle guide clairement l'utilisateur sur les prochaines étapes."}
- **Avis Context Precision** : {'score': 5, 'explanation': 'Le contexte contient **toutes les informations nécessaires** pour répondre : adresses emails des interlocuteurs par secteur (incluant Juliette Piquard pour le LIFAT et le SPIV), ainsi que les règles de soumission (délai de 2 semaines). Aucune information manquante pour une réponse complète.'}

### Question : Quels sont les critères d’évaluation des manuscrits ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 4.0/5

### Question : Où trouver les consignes de rédaction destinées aux auteurs ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 1.0/5, Context Precision: 1.0/5
- **Avis Faithfulness** : La réponse du système **hallucine totalement** des informations absentes du contexte fourni. Aucune mention de *Jeanne Hélouis* ou de *l'Université de Tours* n'apparaît dans le document source. Le système invente un contact et une institution sans fondement, ce qui constitue une **violation flagrante** du critère de fidélité (note minimale : **1/5**).
- **Avis Answer Relevance** : Bien que la question porte sur des *consignes de rédaction pour les auteurs*, la réponse proposée (un contact fictif) est **inutile et hors-sujet**. Le contexte fourni ne contient aucune information sur des consignes éditoriales, mais le système aurait pu le signaler explicitement plutôt que de fabriquer une réponse. Pertinence **nulle (1/5)**.
- **Avis Context Precision** : Le contexte fourni est un extrait juridique sur le **droit d'auteur** (CPI, jurisprudence, exceptions, etc.) et **ne traite absolument pas** des consignes de rédaction pour les auteurs. Il est donc **impossible** d'y répondre avec les éléments disponibles. Précision du contexte : **1/5** (le contexte est inadapté à la question).

### Question : Quel est le délai moyen entre la soumission d’un manuscrit et sa publication ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 1.0/5
- **Reasoning global** : {'faithfulness': "La réponse ne contient aucune information non sourcée et reste strictement dans les limites des connaissances disponibles (absence d'hallucination). Elle indique clairement l'absence de données dans le contexte fourni.", 'answer_relevance': "La réponse est pertinente : elle explique pourquoi elle ne peut répondre (manque d'informations dans le contexte) et oriente vers des sources utiles (école doctorale, éditeurs, ADUM). Cela répond indirectement mais utilement à la question en guidant l'utilisateur vers des solutions concrètes.", 'context_precision': 'Le contexte fourni ne contient **aucune** information sur les délais de soumission/publication de manuscrits (thèses ou articles). Il aborde uniquement des procédures administratives (soutenances, HDR, crédits, etc.), sans mention de timing éditorial. Le score est donc minimal (1/5).'}

### Question : Quels sont les droits cédés à l’éditeur ? Puis-je publier une version préprint ou en accès ouvert ?
- **Erreur d'évaluation** : HTTPSConnectionPool(host='llm.ilaas.fr', port=443): Read timed out. (read timeout=30)

### Question : Quels sont les domaines constitutifs du catalogue et le type de publication des PUFR ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 1.0/5

### Question : A quel public s’adressent les publications ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 4.0/5

### Question : A qui puis-je m'adresser pour toute commande d'ouvrages publiés aux Presses universitaires François-Rabelais (PUFR) ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 1.0/5

### Question : Comment accéder aux ouvrages des PUFR ? Sont-ils disponibles en accès ouvert ou payant ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 1.0/5

### Question : Qui contacter pour toute demande d'ouvrages en service presse ?
- **Notes** : Faithfulness: 2.0/5, Answer Relevance: 3.0/5, Context Precision: 1.0/5
