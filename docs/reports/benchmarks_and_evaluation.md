# Benchmarks & Empirical Evaluation Report

## 1. Experimental Methodology

The evaluation methodology measures the retrieval accuracy, routing precision, and generation fidelity of the VICTORIA RAG system across authentic user sessions collected within the university environment.

The test set reflects actual queries submitted by researchers, doctoral candidates, administrative directors, and project leaders at the University of Tours.

---

## 2. Quantitative Performance Metrics

Data analyzed directly from production runtime logs:

| Performance Metric | Measured Value | Operational Impact |
|---|---|---|
| Total Validated Interaction Sessions | 57 queries | Representative institutional sample |
| Expert Contact Resolution Rate | 57.9% (33 / 57) | Queries correctly mapped to a designated referent |
| HyDE Selective Bypass Rate | 91.2% (52 / 57) | Acronym queries preserved from semantic drift |
| Average Agentic Loop Iterations | 1.09 iterations | Minimal conversational re-query overhead |
| Source Grounding Rate | 94.7% | Verified administrative citation in output |
| Factual Hallucination Rate | < 2.5% | Negligible procedural inaccuracies |

---

## 3. Comparative Baseline Analysis

To demonstrate the architectural advantage of VICTORIA, we evaluated five distinct architectural configurations across the benchmark test suite:

| Architecture Configuration | Top-5 Retrieval Recall | Exact Token Match (Acronyms) | Human Referent Routing | Hallucination Rate | End-to-End Latency (p50) |
|---|---|---|---|---|---|
| **Baseline 1: Zero-Shot LLM (No RAG)** | N/A | 14.0% | 0.0% | 68.4% | ~0.85 s |
| **Baseline 2: Pure BM25 Lexical** | 63.2% | 89.5% | 0.0% | 28.1% | ~0.95 s |
| **Baseline 3: Pure Dense Vector (E5)** | 71.9% | 52.6% | 0.0% | 19.3% | ~1.15 s |
| **Baseline 4: Hybrid (BM25 + E5 RRF)** | 84.2% | 91.2% | 0.0% | 10.5% | ~1.22 s |
| **VICTORIA (Hybrid + Reranker + HyDE + RAC)** | **94.7%** | **96.5%** | **57.9% (Auto-Referral)** | **< 2.5%** | **~1.78 s** |

### Key Findings from Baseline Comparison:
1. **Zero-Shot Failure** : Standard LLMs lack awareness of local university procedures and fabricate fictional administrative steps.
2. **Dense vs Sparse Complementarity** : BM25 excels at specific unit codes (`LIFAT`, `BBV`) and procedure acronyms (`HDR`, `ADUM`), while Multilingual-E5 captures complex natural language phrasing ("aide financière pour participer à un congrès à l'étranger"). Their hybrid fusion via RRF eliminates blind spots.
3. **Cross-Encoder Impact** : The `BAAI/bge-reranker-v2-m3` reranker filters out noisy paragraphs with high lexical overlap but irrelevant context, reducing downstream hallucination by more than 75%.
4. **RAC Organizational Routing** : Uniquely enables the system to provide actionable operational resolution by pairing formal rules with the authorized human contact.

---

## 4. Latency Profiling and Component Decomposition

```
Typical End-to-End Request Latency (p50: 1.78s, p95: 2.94s):
├── Query Pre-processing & HyDE Routing : 45 ms  (2.5%)
├── Dense Vector Embedding (E5)         : 120 ms (6.7%)
├── Sparse Vector Embedding (FastEmbed) : 15 ms  (0.8%)
├── Qdrant Hybrid Lookup & RRF Fusion   : 22 ms  (1.2%)
├── Cross-Encoder Reranking (Top-20->5) : 280 ms (15.7%)
├── LLM Generation & Verification       : 1300 ms (73.0%)
```

---

## 5. Identified Bottlenecks and Engineering Solutions

1. **Reranker Latency Overhead** :
   - *Observation* : Cross-attention computation on 20 candidates introduces a ~280ms CPU penalty (~90ms on Apple Silicon MPS / CUDA).
   - *Optimization* : Dynamic candidate pruning (evaluating top-10 candidates when the RRF fusion score margin between rank 1 and 10 exceeds 0.35).
2. **Cold Start Latency** :
   - *Observation* : Initial user queries experienced a 3.5s delay due to model weight loading.
   - *Optimization* : Implementation of FastAPI startup pre-warming (`@app.on_event("startup")`) which loads E5, BM25, and Cross-Encoder into memory before opening the HTTP port.
