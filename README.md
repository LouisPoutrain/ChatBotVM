# VICTORIA : Systeme RAG Hybride et Routage Organisationnel pour la Recherche Universitaire

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-FastAPI%20%7C%20Gradio-009688.svg?style=flat-square)](https://fastapi.tiangolo.com/)
[![Vector Engine](https://img.shields.io/badge/Vector%20DB-Qdrant-dc2626.svg?style=flat-square)](https://qdrant.tech/)
[![Embeddings](https://img.shields.io/badge/Embeddings-Multilingual--E5--Large%20%2B%20BM25-4f46e5.svg?style=flat-square)](https://huggingface.co/intfloat/multilingual-e5-large)
[![Reranker](https://img.shields.io/badge/Reranker-BAAI%2Fbge--reranker--v2--m3-059669.svg?style=flat-square)](https://huggingface.co/BAAI/bge-reranker-v2-m3)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production--Ready-success.svg?style=flat-square)]()

---

## Demonstration Visuelle d'Execution

L'illustration ci-dessous presente une execution reelle du pipeline d'inference VICTORIA traitant une requete reglementaire complexe avec expansion selective, filtrage neuronal et resolution automatique du referent administratif :

![Demonstration d'Execution VICTORIA](docs/site/assets/demo_execution.svg)

---

## Motivation Scientifique et Resume Executif

Dans les environnements institutionnels et de recherche academique, les systemes de Question-Reponse naifs fondes sur des modeles de langage generatifs autonomes souffrent de limites fondamentales :
1. **Hallucinations reglementaires** : Tendance a inventer des procedures administratives, des delais ou des seuils financiers inexistants en comblant les lacunes par interpolation probabiliste.
2. **Desalignement lexical** : Discordance entre le vocabulaire informel des chercheurs ou doctorants et les formulations juridiques codifiees des decrets, chartes et arretes.
3. **Disparite de precision des acronymes** : Defaillance des representations vectorielles denses sur les codes d'unites de recherche, les numeros d'ecoles doctorales ou les acronymes de procedures (ex. HDR, SPIV, AFRV, LIFAT, BBV, ED 549).
4. **Absence d'actionnabilite** : Une reponse purement textuelle demeure sterile si l'usager n'est pas mis en relation avec le gestionnaire ou charge d'affaires specifiquement habilite a instruire la demarche.

Le projet **VICTORIA** (*Virtual Intelligent Conversational Tool for Organizational Research & Institutional Administration*) repond a cette quadruple problematique par une architecture hybride en etapes successives :
- **Espace vectoriel bi-modal dense et creux** : Couplage du modele semantique multilingue dense `intfloat/multilingual-e5-large` (1024 dimensions) et de l'indexation lexicale creuse `BM25` via FastEmbed, fusionnes par l'algorithme *Reciprocal Rank Fusion* (RRF).
- **Reranking neuronal a attention croisee** : Reclassement des passages candidats via le Cross-Encoder `BAAI/bge-reranker-v2-m3` eliminant les faux positifs lexicaux.
- **Routage organisationnel RAC (*Reseau d'Accompagnement et de Competences*)** : Module d'affectation automatique appariant l'unite de recherche de l'usager aux referents metiers institutionnels (Antenne Financiere, Partenariats, Ecoles Doctorales, Pole Juridique).
- **Expansion contextuelle HyDE avec contournement d'acronymes** : Generation d'un document hypothetique pour densifier la requete, desactivee algorithmiquement sur detection d'acronymes normalises afin d'eviter toute derivation semantique.

---

## Architecture des Modules et Flux de Donnees

```
+---------------------------------------------------------------------------------------------------+
|                                 ARCHITECTURE DU SYSTEME VICTORIA                                  |
+---------------------------------------------------------------------------------------------------+

  [ UTBOX Cloud Univ-Tours ] --- Synchronisation WebDAV differentielle (Utbox.py)
              |
              v
  [ Ingestion Marker OCR ] ----- Conversion haute fidelite PDF vers Markdown structure (PDF2/)
              |
              v
  [ Decoupage Chunking ] ------- RecursiveCharacterTextSplitter (800 car., chevauchement 150)
              |
      +-------+-------+
      |               |
      v               v
  [ Dense E5 ]   [ Sparse BM25 ]
      |               |
      +-------+-------+
              v
  [ Base Vectorielle Qdrant ] -- Collection hybride 'pdf2_documents' (Metadonnees domaines)
              ^
              | Requete Hybride RRF (k=60)
              |
  [ Prompt Utilisateur ] ------> [ Module HyDE ] (Expansion selective si absence d'acronymes)
              |
              +----------------> [ Routeur RAC ] --> Extraction d'entites et referents metiers
                                       |
                                       v
  [ Candidats Top-20 ] --------> [ Cross-Encoder Reranker BAAI/bge-reranker-v2-m3 ]
                                       |
                                       v Top-5 Passages filtres
                                 [ Boucle Agentique & Garde-fous ]
                                 [ Moteur LLM (Mistral / ILaaS) ]
                                       |
                                       v
                     [ Reponse Sourcée + Contact Institutionnel ]
                                       |
       +-------------------------------+-------------------------------+
       |                               |                               |
       v                               v                               v
[ API FastAPI :8600 ]       [ Interface Gradio ]           [ Widget Web Intranet ]
```

---

## Resultats Experimentaux et Benchmarks Authentiques

L'ensemble des metriques ci-apres provient de l'analyse instrumentee des 120 documents sources du corpus et des 57 sessions d'interaction reelles executees en environnement universitaire (rapports detailles consultables dans [`docs/reports/`](docs/reports/)).

### 1. Metriques Globales du Corpus Institutionnel

| Indicateur Technique | Valeur Mesuree | Observation Methodologique |
|---|---|---|
| Documents PDF traites | 120 fichiers | Couverture exhaustive AFRV, SPIV, RED, PJR |
| Volume cumule de pages | 904 pages | Moyenne de 7,53 pages par document |
| Volume source sur disque | 100,44 Mo | Moyenne de 0,84 Mo par fichier |
| Volume textuel extrait | 2 268 697 caracteres | Payload Markdown propre indexe dans `PDF2/` |
| Lexique utile normalise | 243 396 mots | Tokens exploitables pour l'indexation dense/creuse |
| Ratio de densite alphabetique | 0,6438 | Taux de caracteres alphabetiques valides |
| Documents scannes traites | 21 documents (17,5%) | Detection automatique et bascule OCR Tesseract 300 DPI |
| Taux de succes de conversion | 100,0% | Zero plantage ou echec sur la suite de conversion |

### 2. Comparaison Objective avec les Architectures Baselines

Les tests ont ete menes sur le banc d'essai standard de 57 requetes administratives reelles issues des journaux de production :

| Configuration Architecturale | Rappel Top-5 | Correspondance Acronymes | Routage Referent RAC | Taux d'Hallucination | Latence Moyenne (p50) |
|---|---|---|---|---|---|
| **Baseline 1 : LLM Zero-Shot (Sans RAG)** | N/A | 14,0% | 0,0% | 68,4% | 0,85 s |
| **Baseline 2 : Recherche Lexicale (BM25 seul)** | 63,2% | 89,5% | 0,0% | 28,1% | 0,95 s |
| **Baseline 3 : Recherche Dense (Multilingual-E5)** | 71,9% | 52,6% | 0,0% | 19,3% | 1,15 s |
| **Baseline 4 : Hybride RRF (BM25 + Dense E5)** | 84,2% | 91,2% | 0,0% | 10,5% | 1,22 s |
| **VICTORIA (Hybride + Reranker + RAC + HyDE)** | **94,7%** | **96,5%** | **57,9%** | **< 2,5%** | **1,78 s** |

### 3. Analyse des Goulots d'Etranglement et Optimisations

1. **Latence du Cross-Encoder** :
   - *Constat* : Le calcul de l'attention croisee sur 20 candidats entraine une charge de 280 ms sur CPU (~90 ms sur GPU / MPS).
   - *Optimisation appliquee* : Pruning dynamique des candidats reduisant l'evaluation a 10 passages lorsque l'ecart de score RRF entre le rang 1 et le rang 10 depasse le seuil empirique de 0,35.
2. **Preservation des Acronymes par Contournement HyDE** :
   - *Constat* : L'expansion HyDE diluait les sigles courts (ex. *BBV*, *LIFAT*, *HDR*) en inventant des definitions non institutionnelles.
   - *Optimisation appliquee* : Algorithme de bypass automatique sur detection d'acronymes, activant un ciblage direct du filtre de fichier et de domaine (91,2% des requetes acronymes preservees).

---

## Arborescence du Projet

```
ChatBotVM/
├── BV/                                  # Module de gestion de la Base Vectorielle
│   └── BV.py                            # Moteur Qdrant, embeddings E5/BM25 et fusion RRF
├── Interface/                           # Couches d'exposition de l'interface
│   ├── README.md                        # Documentation specifique du module d'interface
│   ├── fastapi_rag_wrapper.py           # Serveur API REST asynchrone (FastAPI / APScheduler)
│   ├── gradio_rag_wrapper.py            # Interface interactive Gradio pour validation experte
│   └── static/                          # Fichiers statiques web
│       ├── Chat.png                     # Mascotte visuelle du projet
│       ├── admin.html                   # Console d'administration et d'audit des journaux
│       ├── demo.html                    # Page de banc d'essai et d'integration locale
│       └── widget.js                    # Widget client leger integrateur pour intranet
├── PDF2/                                # Corpus structure extrait des documents institutionnels
│   ├── AFRV/                            # Documents financiers et gestion des depenses
│   ├── Autre/                           # Reglements ecoles doctorales, soutenances et HDR
│   ├── Guide du DU/                     # Directives et guides des directeurs d'unites
│   ├── PJR/                             # Fiches juridiques, propriete intellectuelle, deontologie
│   └── SPIV/                            # Conventions de recherche, valorisation et partenariats
├── RAC/                                 # Reseau d'Accompagnement et de Competences
│   ├── ContactRole.txt                  # Repertoire textuel des fonctions administratives
│   ├── Data/                            # Fiches de cadrage des missions par service
│   ├── RAC.py                           # Moteur d'affectation et de filtrage organisationnel
│   ├── organigramme.json                # Arborescence hierarchique structuree de la DRV
│   └── qdrant.py                        # Indexation vectorielle du repertoire de contacts
├── RAGilaas/                            # Orchestration du pipeline RAG
│   ├── Prompt.py                        # Templates de prompts et garde-fous d'inference
│   └── RAGilaas.py                      # Boucle de raisonnement agentique et inference LLM
├── TestExtraction/                      # Outils d'evaluation et de diagnostic d'extraction
│   └── logs/                            # Rapports d'analyse du corpus
│       └── marker_test_report.json      # Rapport d'audit unitaire sur les 120 documents
├── Utilitaire/                          # Scripts utilitaires et chaine d'automatisation
│   ├── Contacts.py                      # Extracteur et parseur des fiches contacts
│   ├── Marker.py                        # Pipeline d'OCR et conversion PDF vers Markdown
│   ├── Utbox.py                         # Client de synchronisation WebDAV UTBOX
│   ├── antenne_financiere_table.py      # Parseur de repartition des antennes financieres
│   ├── auto_update_pipeline.py          # Orchestrateur de mise a jour continue hebdomadaire
│   ├── spiv_charges_affaires.py         # Table d'affectation des charges d'affaires SPIV
│   └── toPDF.py                         # Utilitaires de conversion documentaire
├── docs/                                # Documentation formelle du projet
│   ├── README.md                        # Sommaire et index de la documentation
│   ├── architecture/                    # Specifications architecturales detaillees
│   │   └── architecture_overview.md     # Document d'architecture de reference
│   ├── references/                      # Bibliographie et etat de l'art
│   │   └── bibliography.md              # References scientifiques commenteess
│   ├── reports/                         # Rapports empiriques et etudes scientifiques
│   │   ├── benchmarks_and_evaluation.md # Rapport de benchmarks comparatifs
│   │   └── corpus_extraction_report.md  # Rapport de diagnostic de l'extraction documentaire
│   └── site/                            # Portail documentaire deployable
│       ├── assets/                      # Assets visuels du projet
│       │   └── demo_execution.svg       # Demonstration vectorielle d'inference
│       └── index.html                   # Portail web interactif miroir
├── .dockerignore                        # Exclusions de construction conteneur Docker
├── .gitignore                           # Exclusions standardisees Git (PEP 517 / Caches)
├── Dockerfile                           # Construction de l'image de production Python 3.10
├── docker-compose.yml                   # Orchestration conjointe Qdrant + FastAPI
├── index.html                           # Portail web d'accueil GitHub Pages a la racine
├── LICENSE                              # Licence MIT officielle (Louis Poutrain)
├── pyproject.toml                       # Configuration packaging moderne PEP 517 / PEP 621
└── requirements.txt                     # Dependances figees d'execution et de service
```

---

## Guide de Demarrage Reproductible (Quickstart)

### 1. Prerequis Systeme

- Python 3.10 ou superieur
- Git et Git LFS
- Moteur d'execution Docker (optionnel mais recommande pour la production)
- Accès reseau au serveur Qdrant (ou execution locale sur le port 6333)

### 2. Installation de l'Environnement

```bash
# 1. Cloner le depot
git clone https://github.com/LouisPoutrain/ChatBotVM.git
cd ChatBotVM

# 2. Creer et activer l'environnement virtuel
python3 -m venv .venv
source .venv/bin/activate

# 3. Installer l'ensemble des dependances
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Configuration de l'Environnement

Creer un fichier `.env` a la racine du projet avec vos identifiants d'API :

```ini
LLM_API_KEY=votre_cle_api_secrete
LLM_BASE_URL=https://llm.ilaas.fr/v1
QDRANT_URL=http://localhost:6333
```

### 4. Indexation et Initialisation des Donnees

Si vous disposez de nouveaux documents bruts ou souhaitez reinitialiser les index vectoriels :

```bash
# Indexer le repertoire des contacts administratifs (RAC)
python RAC/qdrant.py

# Indexer le corpus Markdown dans la collection Qdrant (BV)
python BV/BV.py --markdown-dir ./PDF2
```

### 5. Lancement des Services Applicatifs

#### Option A : Serveur d'API REST de Production (FastAPI)

```bash
uvicorn Interface.fastapi_rag_wrapper:app --host 0.0.0.0 --port 8600 --reload
```
Le serveur expose :
- Documentation interactive OpenAPI : `http://localhost:8600/docs`
- Endpoint de requete conversationnelle : `POST http://localhost:8600/api/chat`
- Console d'administration et telemetrie : `http://localhost:8600/static/admin.html`

#### Option B : Interface d'Evaluation Experte (Gradio)

```bash
python Interface/gradio_rag_wrapper.py
```
L'interface Web est accessible directement a l'adresse `http://localhost:7860`.

#### Option C : Deploiement Conteneurise (Docker Compose)

```bash
docker-compose up -d --build
```

---

## References et Bibliographie Scientifique

Le tableau ci-dessous resume les articles fondateurs sur lesquels repose la conception algorithmique de VICTORIA :

| Reference Scientifique | Auteurs | Annee | Publication / Venue | Impact sur VICTORIA |
|---|---|---|---|---|
| **Precise Zero-Shot Dense Retrieval without Relevance Labels** | L. Gao, X. Ma, J. Lin, J. Callan | 2022 | arXiv:2212.10496 | Mecanisme HyDE d'expansion hypothetique des requetes |
| **Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks** | P. Lewis et al. | 2020 | NeurIPS 2020 | Paradigme RAG de memoire parametrique et non parametrique |
| **The Probabilistic Relevance Framework: BM25 and Beyond** | S. Robertson, H. Zaragoza | 2009 | FnTIR | Fondement probabiliste de l'indexation lexicale BM25 |
| **C-Pack: Packaged Resources to Advance General Information Retrieval** | S. Xiao, Z. Liu, P. Zhang, N. Muennighoff | 2023 | arXiv:2309.07597 | Architecture du Cross-Encoder Reranker BGE-M3 |
| **Reciprocal Rank Fusion Outperforms Condorcet Methods** | G. V. Cormack, C. L. Clarke, S. Büttcher | 2009 | SIGIR 2009 | Formule de fusion RRF reliant les rangs denses et creux |
| **Ragas: Automated Evaluation of Retrieval Augmented Generation** | S. Es, J. James, L. Espinosa-Anke, S. Schockaert | 2023 | arXiv:2309.15217 | Cadre methodologique d'evaluation de fidelite et precision |

---

## Auteur et Licence

- **Auteur & Developpeur Principal** : Louis Poutrain ([louispoutrain337@gmail.com](mailto:louispoutrain337@gmail.com))
- **Institution** : Direction de la Recherche et de la Valorisation (DRV), Universite de Tours
- **Licence** : Projet distribue sous licence open-source **MIT**. Voir le fichier [`LICENSE`](LICENSE) pour l'integralite des termes juridiques.
