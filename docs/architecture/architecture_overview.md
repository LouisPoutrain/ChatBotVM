# Architecture System Overview - VICTORIA RAG

## Executive Summary

VICTORIA (*Virtual Intelligent Conversational Tool for Organizational Research & Institutional Administration*) is a multi-stage, high-precision Retrieval-Augmented Generation (RAG) system engineered for the Direction de la Recherche et de la Valorisation (DRV) at the University of Tours.

Institutional environments present unique information retrieval challenges:
- Extensive heterogeneous corpora (doctoral rules, financial guidelines, partnership frameworks, intellectual property devolution notes).
- High density of domain-specific acronyms (AFRV, SPIV, RED, PJR, SAPS, HDR, ADUM, EMSTU, MIPTIS, SSBCV, BBV, LIFAT).
- Mission-critical factual precision where inaccurate administrative guidance leads to procedural non-compliance.
- The dual requirement of delivering both verified documentary excerpts and directing users to the designated human administrative officer (*Référent Métier*).

To address these constraints, VICTORIA integrates a dual-route architecture combining hybrid dense-sparse vector search, cross-encoder neural reranking, hypothetical document query expansion (HyDE), and an organizational routing sub-network (RAC).

---

## High-Level Architecture Diagram

```
[ Institutional Data Source (UTBOX / WebDAV Cloud) ]
                        │
                        ▼ (Differential Sync: Utbox.py)
[ Ingestion & OCR Pipeline (Marker.py / PyMuPDF / Tesseract) ]
                        │
                        ▼ (Structured Markdown Corpus: PDF2/)
[ Document Chunking (RecursiveCharacterTextSplitter: 800c / 150o) ]
                        │
       ┌────────────────┴────────────────┐
       ▼                                 ▼
[ Dense Vector Embedding ]       [ Sparse Lexical Embedding ]
(intfloat/multilingual-e5-large)  (Qdrant/bm25 via FastEmbed)
       │                                 │
       └────────────────┬────────────────┘
                        ▼
    [ Vector Database: Qdrant Engine (univ-qdrant) ]
         Collection: pdf2_documents (1024-dim, HNSW)
                        ▲
                        │  Hybrid Retrieval (Reciprocal Rank Fusion - RRF)
                        │
════════════════════════╪═════════════════════════════════════════════════
                 QUERY PROCESSING & INFERENCE ENGINE
════════════════════════╪═════════════════════════════════════════════════
                        │
         [ User Prompt / REST API Request ]
                        │
       ┌────────────────┴────────────────┐
       ▼                                 ▼
[ RAC Module Router ]             [ Query Expansion: HyDE ]
- Domain Tagging (AFRV/SPIV/RED)  - Zero-shot Document Generation
- Lab & Entity Disambiguation     - Automated Acronym Detection Bypass
- Human Referent Resolution       - Dynamic Query Rewriting
       │                                 │
       └────────────────┬────────────────┘
                        ▼
         [ Hybrid Document Retrieval ]
                        │
                        ▼
         [ Cross-Encoder Neural Reranker ]
         (BAAI/bge-reranker-v2-m3, len=512)
                        │
                        ▼
         [ Agentic State Machine & Guardrails ]
         - Multi-iteration Thought/Action loop
         - Hidden Context & RAC Contact Mandatory Enforcer
         - Hallucination suppression & citation verification
                        │
                        ▼
         [ LLM Generation (Mistral / ILaaS) ]
                        │
                        ▼
[ Client Interfaces: Web Widget / FastAPI REST / Gradio Evaluation ]
```

---

## Detailed Pipeline Subsystems

### 1. Ingestion and Document Transformation Subsystem

- **Automated Differential Synchronizer (`Utilitaire/Utbox.py`, `auto_update_pipeline.py`)** :
  Connects to the university Nextcloud/UTBOX instance via authenticated WebDAV or secure share endpoint. Downloads modified archives and performs incremental synchronization.
- **Structural OCR & Document Reconstruction (`Utilitaire/Marker.py`)** :
  Converts complex, multi-column administrative PDFs into semantic Markdown. It extracts hierarchical headers (`#`, `##`, `###`), detects embedded tables into standard GitHub-Flavored Markdown tables, and preserves document metadata. For scanned documents, it triggers OCR via Tesseract (`fra` model).

### 2. Indexation and Hybrid Vector Engine (`BV/BV.py`)

- **Chunking Strategy** :
  `RecursiveCharacterTextSplitter` configured with chunk size of 800 characters and overlap of 150 characters, splitting hierarchically along paragraph boundaries (`\n\n`), sentence boundaries (`\n`), and punctuation marks.
- **Dense Representation** :
  `intfloat/multilingual-e5-large` (1024-dimensional dense vectors). Asymmetric encoding protocol:
  - Document passages prefixed with: `passage: `
  - Search queries prefixed with: `query: `
- **Sparse Representation** :
  `Qdrant/bm25` model executed via FastEmbed, computing on-the-fly IDF-modified term-frequency vectors stored within Qdrant sparse indexes.
- **Rank Fusion** :
  Hybrid queries execute both vector lookups concurrently. Candidates are merged using Reciprocal Rank Fusion (RRF) with default parameter $k=60$:
  $$RRF(d) = \sum_{m \in \{\text{dense}, \text{sparse}\}} \frac{1}{k + r_m(d)}$$

### 3. Neural Reranking Subsystem

Top-20 fused candidates retrieved from Qdrant are passed to a Cross-Encoder reranker:
- **Model** : `BAAI/bge-reranker-v2-m3`
- **Context Length** : 512 tokens
- **Operation** : Evaluates full cross-attention between query and candidate passage, computing a calibrated relevance score in $[-10, +10]$ that eliminates false positives induced by superficial keyword overlap.

### 4. Semantic Organizational Router (RAC: Réseau d'Accompagnement & Contacts)

Administrative users rarely require generic information alone; they require the exact contact person responsible for validating their administrative act.
- **Domain Tagging** : Identifies institutional domains (`AFRV`: Finance/Invoicing, `SPIV`: Contracts/Partnerships, `RED`: Doctoral Studies/HDR, `PJR`: Legal/IP, `SAPS`: Scientific Outreach).
- **Directory Vectorization (`RAC/qdrant.py`)** : Stores institutional organigrams and contact roles into a specialized collection (`infocontact`).
- **Entity Matching (`Utilitaire/Contacts.py`, `RAC/RAC.py`)** : Maps user questions to specific financial managers (by research unit code), business developers (by scientific domain), or doctoral school referents.

### 5. Query Reformulation: Hypothetical Document Embeddings (HyDE)

- Standard queries often exhibit vocabulary mismatch with official administrative texts.
- HyDE leverages a prompt to synthesize a hypothetical administrative passage that would answer the question.
- **Acronym Bypass Rule** : If a question contains known entity acronyms (e.g., `HDR`, `LIFAT`, `BBV`, `EMSTU`), the system bypasses HyDE to prevent semantic drift and ensure precise keyword matching.

### 6. Production Serving & Deployment Subsystem

- **FastAPI Core (`Interface/fastapi_rag_wrapper.py`)** :
  - Asynchronous non-blocking endpoints.
  - CORS security configured for authorized academic intranet origins (`utnet.univ-tours.fr`).
  - Pre-warmed model instances initialized during the FastAPI lifecycle startup event.
- **Automated Scheduling** :
  - Embedded `APScheduler` executing background differential sync jobs weekly on Sundays at 03:00 AM.
- **Containerization (`Dockerfile`, `docker-compose.yml`)** :
  - Multi-container orchestration linking the FastAPI application with a dedicated Qdrant vector database container.
