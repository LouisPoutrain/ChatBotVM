# Bilan des Évaluations (LLM as a Judge)

## Moyennes Globales

- **Faithfulness** : 4.45 / 5
- **Answer Relevance** : 4.32 / 5
- **Context Precision** : 4.09 / 5
- *Nombre de réponses évaluées avec succès : 22*
- **Temps moyen RAG** : 100.98s
- **Temps moyen Évaluation** : 7.19s
- **Temps moyen Total** : 108.17s
- **Tokens moyens générés** : 0
- *Nombre total de requêtes chronométrées : 22*

## Résultats par Fichier

### Fichier : rag_batch_trials.json
- Moyenne Faithfulness : 4.45 / 5
- Moyenne Answer Relevance : 4.32 / 5
- Moyenne Context Precision : 4.09 / 5
- *Évaluations réussies : 22*
- Temps moyen RAG : 100.98s
- Temps moyen Évaluation : 7.19s
- Temps moyen Total : 108.17s
- Tokens moyens générés : 0

---
## Détails des évaluations (Notes et Commentaires du Juge)

## rag_batch_trials.json

### Question : Je souhaite faire une demande d’aide à la mobilité. Quelles sont les pièces justificatives à transmettre ?
- **Notes** : Faithfulness: 3.0/5, Answer Relevance: 2.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 209.74s, Eval: 9.55s, Total: 219.29s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse mentionne que les pièces justificatives varient selon l'école doctorale, ce qui est cohérent avec le contexte (chaque ED a des exigences spécifiques). Cependant, elle n'exploite pas directement les informations du contexte pour lister les pièces. Le contact 'Julia Capdeville' n'est pas présent dans le contexte fourni, mais comme il s'agit d'un contact, il n'est pas considéré comme une hallucination selon les règles. La réponse reste vague et ne s'appuie pas sur des affirmations traçables dans le contexte.
- **Avis Answer Relevance** : La réponse aborde partiellement la question en indiquant que les pièces varient selon l'ED, mais elle ne fournit pas de détails concrets. Elle est donc peu utile et ne répond pas directement à la demande de l'utilisateur.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires pour répondre précisément à la question, avec des listes détaillées de pièces justificatives pour chaque école doctorale (EMSTU, H&L, MIPTIS, SSBCV, SSTED).

### Question : Quand recevrai-je mon diplôme ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 91.82s, Eval: 6.02s, Total: 97.84s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse s'appuie exclusivement sur le contexte fourni. L'affirmation selon laquelle la délivrance du diplôme est conditionnée au dépôt de la version finale de la thèse (électronique) et le délai de 3 mois pour les corrections sont explicitement mentionnés dans le contexte (Article 2, dernier paragraphe). Le contact Elysa Ragot est ignoré pour l'évaluation de la fidélité, conformément aux règles.
- **Avis Answer Relevance** : La réponse adresse directement la question 'Quand recevrai-je mon diplôme ?' en expliquant les conditions et délais liés à la délivrance du diplôme, ce qui est parfaitement pertinent.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires pour répondre à la question, notamment les conditions de dépôt de la thèse et le délai de 3 mois pour les corrections. Ces éléments sont bien ciblés et pertinents.

### Question : Quel est le calendrier des inscriptions pour l’année universitaire 2025/2026 ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 3.0/5
- **Temps** : RAG: 88.90s, Eval: 7.09s, Total: 95.99s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ('La date limite pour finaliser et valider votre dossier de réinscription est le 15 novembre 2025.') est directement traçable dans le contexte fourni. Le contexte mentionne explicitement : 'votre dossier doit être finalisé et validé par tous les protagonistes au plus tard le 15 novembre de l'année universitaire en cours.' Aucune information hallucinée n'est présente.
- **Avis Answer Relevance** : La réponse adresse directement la question posée sur le calendrier des inscriptions pour l'année universitaire 2025/2026. Elle est ciblée et sans hors-sujet.
- **Avis Context Precision** : Le contexte contient des informations sur les réinscriptions et les délais, mais il est partiellement utile. La date limite du 15 novembre est bien présente, mais le contexte est très large (incluant des détails sur les comités de suivi, les dérogations, etc.) et ne se concentre pas uniquement sur le calendrier des inscriptions. Plusieurs informations clés sur les inscriptions (comme les étapes précises ou les dates d'ouverture) manquent.

### Question : Quels sont les délais à respecter pour ma soutenance ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 54.82s, Eval: 5.66s, Total: 60.48s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse cite textuellement et fidèlement l'information du contexte : 'La soutenance pourra intervenir, au minimum, trois semaines après la délivrance de l'autorisation de soutenance.' Aucune information inventée n'est présente. Le contact ajouté (Aurélie PETEREAU) est ignoré pour l'évaluation de la fidélité, conformément aux règles.
- **Avis Answer Relevance** : La réponse adresse directement et précisément la question posée sur les délais à respecter pour la soutenance. Aucune digression ou hors-sujet.
- **Avis Context Precision** : Le contexte contient explicitement l'information nécessaire pour répondre à la question : le délai minimal de trois semaines après l'autorisation de soutenance est clairement mentionné.

### Question : Qui se charge de créer le lien visioconférence pour ma soutenance ? Quand l’aurai-je ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 1.0/5, Context Precision: 1.0/5
- **Temps** : RAG: 92.32s, Eval: 5.11s, Total: 97.43s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient aucune information traçable dans le contexte fourni. Le contexte ne mentionne pas qui crée le lien de visioconférence ni quand il est communiqué. Le contact 'Christele Gaudron-Bredif' est ignoré pour la fidélité (règle des contacts injectés), mais la réponse ne répond pas à la question posée avec des éléments du contexte.
- **Avis Answer Relevance** : La réponse est totalement hors-sujet. Elle ne traite ni de la création du lien de visioconférence ni du moment où il est communiqué. Elle se limite à un contact sans lien avec la question.
- **Avis Context Precision** : Le contexte ne contient aucune information sur la création du lien de visioconférence ou son timing. Il traite uniquement des procédures administratives, de la composition du jury et des règles de soutenance.

### Question : Puis-je faire une césure ? Si oui, comment ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 85.62s, Eval: 5.09s, Total: 90.71s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse est entièrement basée sur le contexte fourni. Toutes les affirmations (durée maximale de 12 mois, non renouvelable, demande motivée, avis du directeur de thèse et de l'école doctorale, non-comptabilisation dans la durée de la thèse, étude par le bureau de l'école doctorale) sont explicitement mentionnées dans le contexte.
- **Avis Answer Relevance** : La réponse adresse directement et précisément la question posée ('Puis-je faire une césure ? Si oui, comment ?'). Elle fournit les conditions et la procédure sans hors-sujet.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires pour répondre à la question, notamment les conditions légales (arrêté du 25 mai 2016), la durée, la non-renouvelabilité, et la procédure de demande.

### Question : Pourquoi mon compte universitaire / ma carte étudiant a-t-elle été désactivée ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 4.0/5, Context Precision: 4.0/5
- **Temps** : RAG: 95.62s, Eval: 6.17s, Total: 101.79s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse mentionne que le compte universitaire des doctorants est valable pour l'année universitaire (1er septembre au 31 août) et qu'il est désactivé en cas de non-réinscription. Ces informations sont explicitement présentes dans le contexte (section 'Nouvel arrivant doctorant'). Aucune information hallucinée n'est détectée.
- **Avis Answer Relevance** : La réponse aborde directement la question de la désactivation du compte universitaire, mais elle est incomplète pour la carte étudiante (la réponse s'interrompt). La pertinence est donc bonne mais partielle.
- **Avis Context Precision** : Le contexte contient bien les informations nécessaires sur la validité du compte des doctorants (durée et condition de désactivation). Cependant, il manque des détails spécifiques sur la carte étudiante, ce qui limite la précision pour cette partie de la question.

### Question : Mon doctorant peut-il demander le prêt d’un ordinateur à l’Université ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 89.87s, Eval: 6.57s, Total: 96.44s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse est entièrement basée sur le contexte fourni. Chaque affirmation (bénéfice de droit d'un ordinateur portable, financement par la DSI ou le laboratoire, propriété de l'Université, restitution à l'issue de la thèse) est explicitement mentionnée dans le contexte. Aucun élément halluciné n'est présent.
- **Avis Answer Relevance** : La réponse adresse directement et précisément la question posée ('Mon doctorant peut-il demander le prêt d’un ordinateur à l’Université ?'). Elle est concise et pertinente, sans hors-sujet.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires pour répondre à la question, notamment la confirmation du droit à un ordinateur portable, les modalités de financement, et la propriété du matériel. Les informations sont bien ciblées et exploitables.

### Question : Quel est le processus de validation de mes démarches sur ADUM pour mon inscription / réinscription / soutenance ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 157.70s, Eval: 11.50s, Total: 169.20s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement traçables dans le contexte fourni. Par exemple : (1) Les étapes de finalisation du dossier (CIF, CV, photo, rapport d’avancement) sont explicitement mentionnées dans le contexte (e.g., 'Avoir déposé votre Convention Individuelle de Formation sur ADUM après validation de votre direction de thèse', 'Avoir déposé les documents à joindre (Photo, CV, Rapport d'activité/avancement)'). (2) La chaîne de validation (direction de thèse → codirection → laboratoire → école doctorale → établissement) est détaillée dans plusieurs extraits du contexte (e.g., 'Votre dossier devra ensuite être validé par votre codirection de thèse, le cas échéant, puis par votre direction de laboratoire, votre direction d'école doctorale puis par la personne représentant votre établissement'). (3) Les délais (15 novembre pour la réinscription, 2 mois avant la soutenance) sont également présents dans le contexte. (4) Le contact 'Christele Gaudron-Bredif' est un contact injecté automatiquement (règle spécifique) et ne pénalise pas la fidélité.
- **Avis Answer Relevance** : La réponse adresse directement et exhaustivement la question posée sur les processus de validation pour l'inscription, la réinscription et la soutenance sur ADUM. Chaque partie de la question est couverte sans hors-sujet : les étapes pour l'inscription/réinscription, la chaîne de validation, et les étapes pour la soutenance sont clairement détaillées.
- **Avis Context Precision** : Le contexte retrouvé contient toutes les informations nécessaires pour répondre correctement à la question. Les détails sur les démarches (documents à déposer, chaîne de validation, délais) sont explicitement présents dans les extraits fournis. Par exemple, les étapes de validation pour la réinscription et la soutenance sont décrites en détail dans plusieurs passages du contexte.

### Question : Combien de temps va prendre mon inscription ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 3.0/5
- **Temps** : RAG: 150.50s, Eval: 10.55s, Total: 161.05s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse mentionne correctement que les dossiers avec diplôme étranger ou DEA nécessitent un examen supplémentaire en bureau d'école doctorale, ce qui est explicitement indiqué dans le contexte (ex: 'Pour rappel, votre dossier doit être finalisé et validé par tous les protagonistes au plus tard le 15 novembre... Si votre dossier doit être étudié par le bureau de l'école doctorale, le délai de traitement de votre dossier sera plus long.'). Cependant, le nom 'Christele Gaudron-Bredif' et l'adresse 'gaudron@univ-tours.fr' ne sont pas présents dans le contexte (seul 'Christèle GAUDRON' et 'christele.gaudron@univ-tours.fr' apparaissent). Comme il s'agit d'informations de contact, cela ne pénalise pas la fidélité selon les règles.
- **Avis Answer Relevance** : La réponse adresse directement la question sur le délai d'inscription en fournissant une information pertinente (contact et mention du délai allongé pour les dossiers spécifiques).
- **Avis Context Precision** : Le contexte contient des informations sur les délais de traitement (ex: 'Si votre dossier doit être étudié par le bureau de l'école doctorale, le délai de traitement de votre dossier sera plus long.') et les étapes de validation, mais il manque une indication explicite du délai exact ou moyen pour une inscription standard. Les informations sur les contacts sont présentes mais pas sous la forme exacte utilisée dans la réponse.

### Question : Pourquoi mon manuscrit de thèse n’apparaît pas encore sur theses.fr ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 4.0/5
- **Temps** : RAG: 90.57s, Eval: 6.78s, Total: 97.35s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse est entièrement traçable dans le contexte. Elle mentionne explicitement que le manuscrit apparaîtra sur theses.fr après la soutenance, une fois que les services de bibliothèque auront traité le dossier (dépôt des documents de soutenance + version définitive sur ADUM). Ces éléments sont directement extraits du contexte, notamment des images 12_image_2.png et 12_image_3.png qui précisent que les résumés et la thèse apparaissent sur theses.fr après la soutenance et le traitement par les services de bibliothèque.
- **Avis Answer Relevance** : La réponse adresse directement la question posée ('Pourquoi mon manuscrit de thèse n’apparaît pas encore sur theses.fr ?') en expliquant les conditions nécessaires à son apparition. Elle est ciblée et sans hors-sujet.
- **Avis Context Precision** : Le contexte contient les informations nécessaires pour répondre à la question, notamment les étapes post-soutenance (traitement par les services de bibliothèque, dépôt sur ADUM). Cependant, il manque des détails sur les délais exacts ou les raisons spécifiques d'un retard éventuel, ce qui limite légèrement la précision.

### Question : Comment trouver un directeur de thèse ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 2.0/5, Context Precision: 1.0/5
- **Temps** : RAG: 86.36s, Eval: 9.46s, Total: 95.82s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse contient uniquement des informations de contact (Christele Gaudron-Bredif, gaudron@univ-tours.fr), qui sont explicitement exclues de l'évaluation de la fidélité selon les règles. Aucune autre information n'est présente, donc aucune hallucination n'est à signaler.
- **Avis Answer Relevance** : La réponse ne traite pas du tout de la question posée ('Comment trouver un directeur de thèse ?'). Elle se limite à une information de contact, ce qui est hors-sujet.
- **Avis Context Precision** : Le contexte retrouvé ne contient aucune information sur la manière de trouver un directeur de thèse. Il aborde plutôt les rôles, les procédures et les obligations liées à la direction de thèse, mais pas les démarches pour en trouver un.

### Question : Mon jury de thèse est-il valide ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 90.15s, Eval: 7.32s, Total: 97.47s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient que des informations directement issues du contexte. Toutes les règles énoncées (nombre de membres, proportions, HDR, émérite, invités) sont explicitement mentionnées dans le contexte. Le contact ajouté en fin de réponse est ignoré pour l'évaluation de ce critère, conformément aux règles.
- **Avis Answer Relevance** : La réponse adresse directement la question de la validité du jury en listant les critères à vérifier. Elle est utile et ciblée, sans hors-sujet.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires pour répondre à la question, notamment les règles de composition du jury, les exceptions (cotutelle, émérite, visioconférence), et les détails sur les invités. Les informations sont bien ciblées et pertinentes.

### Question : Comment déclarer ma soutenance ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 90.59s, Eval: 7.48s, Total: 98.07s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse est entièrement basée sur le contexte fourni. Les éléments clés (connexion à ADUM, clic sur 'Je souhaite effectuer ma demande de soutenance', délai de 2 mois, concertation préalable avec la direction de thèse) sont explicitement mentionnés dans le contexte. Aucune information externe ou hallucinée n'est présente.
- **Avis Answer Relevance** : La réponse adresse directement et de manière exhaustive la question 'Comment déclarer ma soutenance ?'. Elle fournit les étapes essentielles et pertinentes sans hors-sujet.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires pour répondre à la question, notamment les étapes de déclaration sur ADUM, le délai de 2 mois, et la concertation préalable. Les images et le texte du contexte confirment ces éléments.

### Question : Comment m’inscrire / me réinscrire ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 92.16s, Eval: 6.82s, Total: 98.98s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement traçables dans le contexte. Par exemple : l'utilisation d'ADUM, les documents à déposer (pièce d'identité, diplôme, justificatif de financement, Convention Individuelle de Formation, photo, CV, rapport d'avancement), la validation de la Charte du doctorat, la date limite du 15 novembre, et les contacts fournis (Elysa RAGOT, Christèle GAUDRON). Aucune information inventée n'est présente.
- **Avis Answer Relevance** : La réponse adresse directement et exhaustivement la question posée ('Comment m’inscrire / me réinscrire ?'). Elle distingue clairement les étapes pour l'inscription et la réinscription, sans hors-sujet.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires pour répondre correctement à la question. Les détails sur les documents à déposer, les étapes de validation, les contacts, et les spécificités des écoles doctorales (ex : projet de thèse pour l'ED Humanités et Langues) sont présents et bien ciblés.

### Question : Comment trouver un financement pour ma thèse ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 90.93s, Eval: 8.66s, Total: 99.59s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement traçables dans le contexte. Par exemple : les sources de financement (ANR, Europe, Labex, CIFRE, etc.), les liens vers les appels à projets (Conseil régional, financements nationaux/européens), et le montant minimum de 1 100 € nets/mois sont explicitement mentionnés dans le contexte. Les contacts fournis (ex. spiv@univ-tours.fr) sont exclus de l'évaluation de la fidélité car ils sont automatiquement injectés.
- **Avis Answer Relevance** : La réponse adresse directement et de manière exhaustive la question sur les moyens de financer une thèse. Elle liste les principales sources de financement et les démarches associées, sans hors-sujet.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires pour répondre à la question. Les sections 'Autres financements doctoraux' et 'Recherche de financement pour un projet/contrat de recherche' fournissent des détails précis sur les sources de financement, les montants, et les liens utiles.

### Question : Quels sont les critères de sélection d’un jury ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 54.44s, Eval: 4.92s, Total: 59.36s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement traçables dans le contexte. Par exemple : la taille minimale du jury (5 membres), la proportion de personnalités extérieures (au moins la moitié), la proportion de professeurs ou assimilés (au moins la moitié), la présence obligatoire d'un HDR de l'Université de Tours, les limites sur les liens scientifiques avec le candidat, et l'équilibre femmes-hommes. Les informations de contact (Aurélie PETEREAU) sont exclues de l'évaluation de fidélité conformément aux règles.
- **Avis Answer Relevance** : La réponse adresse directement et exhaustivement la question posée sur les critères de sélection d’un jury. Aucun élément hors-sujet n'est présent.
- **Avis Context Precision** : Le contexte retrouvé contient toutes les informations nécessaires pour répondre correctement à la question. Les règles de composition du jury sont clairement détaillées dans la section 'Règles de composition du jury' du contexte.

### Question : Quand recevrai-je ma carte étudiante / mon certificat de scolarité ?
- **Notes** : Faithfulness: 1.0/5, Answer Relevance: 1.0/5, Context Precision: 1.0/5
- **Temps** : RAG: 87.55s, Eval: 5.86s, Total: 93.41s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse du système est vide (aucune information fournie), ce qui signifie qu'aucune affirmation ne peut être tracée dans le contexte. La question porte sur la réception de la carte étudiante ou du certificat de scolarité, mais le contexte fourni ne contient aucune information sur ces sujets. La réponse vide est donc équivalente à une absence totale de fidélité.
- **Avis Answer Relevance** : La réponse ne traite absolument pas la question posée. La question demande des informations sur la réception de documents administratifs (carte étudiante, certificat de scolarité), mais la réponse est vide, donc hors-sujet.
- **Avis Context Precision** : Le contexte retrouvé ne contient aucune information pertinente pour répondre à la question. Il traite exclusivement des procédures de soutenance de thèse, des pièces justificatives pour l'inscription en doctorat, et des processus administratifs liés à la thèse, mais rien sur les cartes étudiantes ou certificats de scolarité.

### Question : Qui envoie mon manuscrit de thèse aux rapporteurs et au jury ? Quand ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 94.59s, Eval: 6.32s, Total: 100.91s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse indique que la gestionnaire de l'école doctorale envoie le lien de consultation du manuscrit aux rapporteurs et au jury après validation du chef d'établissement et finalisation de la procédure sur ADUM. Cette information est explicitement mentionnée dans le contexte (section 6 : 'La gestionnaire de votre école doctorale, une fois la composition de votre jury validé par le chef d'établissement et la finalisation de votre procédure, peut indiquer la date de retour des pré-rapports de soutenance ce qui déclenche l'envoi : [...] du lien utile pour consultation du manuscrit de thèse'). Aucune information externe ou hallucinée n'est présente.
- **Avis Answer Relevance** : La réponse adresse directement et précisément la question posée ('Qui envoie mon manuscrit de thèse aux rapporteurs et au jury ? Quand ?'). Elle identifie l'acteur (gestionnaire de l'école doctorale) et le moment (après validation du chef d'établissement et finalisation sur ADUM), sans hors-sujet.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires pour répondre à la question. La section 6 décrit clairement le processus d'envoi du manuscrit par la gestionnaire de l'école doctorale, y compris les conditions préalables (validation du chef d'établissement et finalisation sur ADUM).

### Question : Pourquoi l’accès à ma réinscription à distance est-il bloqué ?
- **Notes** : Faithfulness: 4.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 90.65s, Eval: 7.48s, Total: 98.13s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse mentionne des étapes préalables non validées (Convention Individuelle de Formation, documents manquants, validation en attente) qui sont explicitement citées dans le contexte (ex. : 'Avoir déposé votre Convention Individuelle de Formation sur ADUM', 'Avoir déposé les documents à joindre'). Cependant, l'adresse e-mail 'elysat.ragot@univ-tours.fr' contient une faute de frappe (manque un 'a' dans 'elysa') par rapport au contexte ('elysa.ragot@univ-tours.fr'). Cette erreur est mineure et ne constitue pas une hallucination majeure, mais elle affecte légèrement la fidélité.
- **Avis Answer Relevance** : La réponse adresse directement la question en expliquant les raisons possibles du blocage (étapes non validées) et propose une solution (contacter un responsable). Elle est donc parfaitement pertinente.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires pour répondre à la question : les étapes obligatoires pour la réinscription (Convention Individuelle de Formation, documents à joindre, validation par la direction de thèse/laboratoire) sont clairement détaillées. Aucune information clé ne manque.

### Question : Qui doit renseigner les membres de mon CSI sur ADUM ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 3.0/5
- **Temps** : RAG: 142.00s, Eval: 8.68s, Total: 150.68s
- **Tokens générés** : 0
- **Avis Faithfulness** : La réponse ne contient aucune information hallucinée. Le contact 'Caroline Vaslin' est explicitement exclu de l'évaluation de la fidélité selon les règles (contacts injectés automatiquement). Aucune autre affirmation n'est présente dans la réponse.
- **Avis Answer Relevance** : La réponse adresse directement la question posée ('Qui doit renseigner les membres de mon CSI sur ADUM ?') en fournissant un contact précis pour cette tâche. Elle est donc parfaitement pertinente.
- **Avis Context Precision** : Le contexte retrouvé contient des informations sur le CSI (composition, réunions, rapports) et sur ADUM (déclaration de soutenance, gestion des données), mais il ne mentionne pas explicitement qui est responsable de la saisie des membres du CSI dans ADUM. Le contexte est donc partiellement utile mais manque de cette information clé.

### Question : Comment obtenir le label européen ?
- **Notes** : Faithfulness: 5.0/5, Answer Relevance: 5.0/5, Context Precision: 5.0/5
- **Temps** : RAG: 94.56s, Eval: 5.12s, Total: 99.68s
- **Tokens générés** : 0
- **Avis Faithfulness** : Toutes les affirmations de la réponse sont directement traçables dans le contexte. Les 4 conditions pour obtenir le label européen sont explicitement listées dans le contexte (ex: 'L'autorisation de soutenance accordée au vu de rapports rédigés par au moins deux professeurs...', 'Un membre au moins du jury doit appartenir à un établissement...', etc.). Les contacts fournis (Guillaume Fialeix, Christèle Gaudron) sont exclus de l'évaluation de fidélité car ils sont automatiquement injectés.
- **Avis Answer Relevance** : La réponse adresse directement et exhaustivement la question 'Comment obtenir le label européen ?' en listant les 4 conditions obligatoires et en fournissant des ressources utiles (liens, contacts). Aucun élément hors-sujet n'est présent.
- **Avis Context Precision** : Le contexte contient toutes les informations nécessaires pour répondre à la question, notamment les 4 conditions détaillées pour l'obtention du label européen, ainsi que des liens vers des ressources officielles. Aucune information clé ne manque.
