# Benchmarks & Empirical Evaluation Report

## 1. Experimental Methodology and Scope

This empirical evaluation report analyzes the operational performance, routing accuracy, and retrieval characteristics of the VICTORIA RAG system across authentic user sessions collected within the university environment.

The test set reflects actual queries submitted by researchers, doctoral candidates, administrative directors, and project leaders to the Direction de la Recherche et de la Valorisation (DRV) at the University of Tours between June 11, 2026 and June 29, 2026. All raw telemetry is preserved in [`data/logs/rag_chat_logs.txt`](../../data/logs/rag_chat_logs.txt).

---

## 2. Quantitative Telemetry from Authentic Production Logs

Exhaustive extraction from the 57 validated interaction sessions:

| Performance Dimension | Measured Value | Methodology & Source Evidence |
|---|---|---|
| Total Validated Interaction Sessions | 57 sessions | Continuous production query trace in `rag_chat_logs.txt` |
| Query Length Spectrum | 7.8 words avg (min: 1, max: 22) | Spans raw acronyms (`LIFAT`, `HDR`) to multi-sentence procedural queries |
| Administrative Domain Routing | RED/Autre: 54.4% (31) · AFRV: 35.1% (20) · SPIV: 10.5% (6) | Automated classification mapped to corresponding university directorate units |
| HyDE Selective Bypass Rate | 91.2% (52 / 57 sessions) | Regex acronym capture and definition pattern bypass preventing semantic hallucination |
| HyDE Active Generation Rate | 8.8% (5 / 57 sessions) | Selective synthetic expansion for conceptual and exploratory queries |
| Expert Contact Resolution Rate | 57.9% (33 / 57 sessions) | Successful automated pairing with a certified institutional administrative officer |
| Transversal / General Queries | 42.1% (24 / 57 sessions) | High-level regulatory questions handled without specific individual officer needed |
| Agentic Reasoning Loop Depth | 1.05 iterations avg | 54 sessions resolved in 1 iteration (94.7%), 3 sessions in 2 iterations (5.3%) |
| Retrieved Documentary Context | 3.93 chunks avg (224 total) | Top-k bounded documentary passages injected into LLM context window |

---

## 3. Comparative Architectural Properties Matrix

To maintain absolute scientific integrity, rather than presenting unverified simulated retrieval scores for third-party systems on this private institutional dataset, the matrix below outlines the formal properties and qualitative trade-offs established in information retrieval literature:

| Architecture Configuration | Retrieval Paradigm | Handling of Local Acronyms | Resistance to Lexical Noise | Organizational Actionability | Theoretical Foundation |
|---|---|---|---|---|---|
| **Zero-Shot LLM (No RAG)** | Parametric internal weights | Fails (hallucinates local policies) | Zero (interpolates missing data) | None (no human contact) | Brown et al. (2020) |
| **Pure BM25 (Lexical Only)** | Sparse term-frequency (TF-IDF) | High on exact string match (`HDR`, `LIFAT`) | Low (vulnerable to synonyms / phrasing) | None (raw text only) | Robertson & Zaragoza (2009) |
| **Pure Dense Vector (E5)** | 1024-d cosine similarity | Moderate (semantic dilution on short codes) | Moderate (false positive vector drift) | None (unaware of org chart) | Wang et al. (2022) |
| **Hybrid RRF (BM25 + E5)** | Reciprocal Rank Fusion ($k=60$) | High (combines lexical & semantic signals) | Moderate (lexical traps may persist in top-k) | None (no officer routing) | Cormack et al. (2009) |
| **VICTORIA Pipeline** | Bi-modal RRF + Cross-Encoder | Maximal (automated HyDE bypass + regex) | Robust (`BAAI/bge-reranker-v2-m3` cross-attention) | Integrated (RAC router + contact cards) | Lewis et al. (2020) ; Xiao et al. (2023) |

---

## 4. Subsystem Pipeline Configuration and Runtime Specifications

The production pipeline components operate under verified configurations:

1. **Dual Candidate Retrieval (`BV/BV.py`)** :
   - Parallel prefetch in Qdrant: 20 dense candidate vectors (`intfloat/multilingual-e5-large`) and 20 sparse candidate vectors (`FastEmbed Qdrant/bm25`).
   - Merged using Reciprocal Rank Fusion (RRF) with standard smoothing factor $k=60$.
2. **Full Cross-Attention Reranking (`BV/BV.py`)** :
   - The Cross-Encoder `BAAI/bge-reranker-v2-m3` evaluates the query against all 20 retrieved candidates with a max sequence length of 512 tokens.
   - The candidates are sorted by cross-attention score, and only the top-$k$ passages ($k=5$ default) are passed forward to the generator.
3. **Automated Acronym Bypass Engine (`RAGilaas/RAGilaas.py`)** :
   - Syntactic regex filter `\b[A-Z][A-Z0-9-]{1,}\b` combined with definition query triggers (`c'est quoi`, `signifie`, `définition`).
   - Automatically bypasses hypothetical document generation for 91.2% of sessions, eliminating hallucinated acronym expansions while activating HyDE for complex exploratory questions.
4. **Calibrated Text Segmentation** :
   - Regulatory corpus (`BV/BV.py`): `max_chars = 3200`, `overlap_chars = 350` preserving integrity of legal articles and financial allowance tables.
   - Organizational directory (`RAC/qdrant.py`): `chunk_size = 900`, `chunk_overlap = 120` ensuring concise, atomic duty specifications.

