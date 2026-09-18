# Documentation Index - VICTORIA System

Welcome to the technical documentation of **VICTORIA** (*Virtual Intelligent Conversational Tool for Organizational Research & Institutional Administration*), developed for the Direction de la Recherche et de la Valorisation (DRV) at the University of Tours.

---

## Documentation Structure

The documentation is divided into specialized modules:

1. **[Architecture Specification](architecture/architecture_overview.md)**
   - Theoretical principles of the multi-stage hybrid RAG pipeline.
   - Vector space mechanics (Dense `multilingual-e5-large` + Sparse `bm25` FastEmbed).
   - Reciprocal Rank Fusion (RRF) and Cross-Encoder neural reranker (`bge-reranker-v2-m3`).
   - Organizational routing sub-network (RAC) and HyDE expansion.

2. **[Corpus Ingestion & Diagnostic Report](reports/corpus_extraction_report.md)**
   - Complete extraction analysis across 120 institutional documents (904 pages).
   - Marker OCR processing, text density ratios, tabular markdown reconstruction.
   - Handling of scanned / low-layer PDFs (17.5% fallback).

3. **[Benchmarks & Empirical Evaluation Report](reports/benchmarks_and_evaluation.md)**
   - Measured quantitative performance across authentic user sessions (57 production queries).
   - Comparative baseline evaluation (Zero-shot vs BM25 vs Dense vs Hybrid vs Full VICTORIA).
   - Component latency profiling (p50: 1.78s).

4. **[Scientific Bibliography](references/bibliography.md)**
   - Comprehensive academic references cataloging foundational research papers (HyDE, RAG, Okapi BM25, BGE-M3, Contrastive Pre-training, Ragas).

5. **[Interactive Portal & Site Showcase](site/index.html)**
   - Web application demonstration and interactive simulator.
