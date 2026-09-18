# Scientific Bibliography & Reference Literature

This catalogue indexes the foundational academic publications that underpin the theoretical and algorithmic architecture of the VICTORIA RAG system.

---

## 1. Core Literature Catalogue

| Title | Authors | Year | Venue | Primary Contribution | Reference Link |
|---|---|---|---|---|---|
| **Precise Zero-Shot Dense Retrieval without Relevance Labels** | L. Gao, X. Ma, J. Lin, J. Callan | 2022 | arXiv:2212.10496 | Introduces Hypothetical Document Embeddings (HyDE) for zero-shot query expansion without relevance labels. | [arXiv:2212.10496](https://arxiv.org/abs/2212.10496) |
| **Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks** | P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal, H. Küttler, M. Lewis, W. Yih, T. Rocktäschel, S. Riedel, D. Kiela | 2020 | NeurIPS 2020 | Foundational framework combining pre-trained parametric and non-parametric memory for verifiable generation. | [arXiv:2005.11401](https://arxiv.org/abs/2005.11401) |
| **The Probabilistic Relevance Framework: BM25 and Beyond** | S. Robertson, H. Zaragoza | 2009 | Foundations and Trends in Information Retrieval | Formal mathematical derivation of Okapi BM25 probabilistic relevance scoring and term frequency saturation. | [DOI: 10.1561/1500000019](https://doi.org/10.1561/1500000019) |
| **C-Pack: Packaged Resources to Advance General Chinese/Cross-lingual Information Retrieval** | S. Xiao, Z. Liu, P. Zhang, N. Muennighoff | 2023 | arXiv:2309.07597 | Introduces the BGE model suite, including BGE-M3 (multi-lingual, multi-functionality, multi-granularity) and state-of-the-art Cross-Encoders. | [arXiv:2309.07597](https://arxiv.org/abs/2309.07597) |
| **Text and Code Embeddings by Contrastive Pre-Training** | A. Neelakantan, T. Xu, R. Puri, A. Radford, J. M. Hesse, M. Patry, P. Tworek, J. Leike, I. Sutskever | 2022 | arXiv:2201.10005 | Asymmetric bi-encoder contrastive learning representations for passage and query embeddings. | [arXiv:2201.10005](https://arxiv.org/abs/2201.10005) |
| **Reciprocal Rank Fusion Outperforms Condorcet and Individual Rank Learning Methods** | G. V. Cormack, C. L. Clarke, S. Büttcher | 2009 | SIGIR 2009 | Standard unsupervised rank aggregation algorithm (RRF) for combining heterogeneous retrieval scores. | [SIGIR '09 Proceedings](https://doi.org/10.1145/1571941.1572114) |
| **Ragas: Automated Evaluation of Retrieval Augmented Generation** | S. Es, J. James, L. Espinosa-Anke, S. Schockaert | 2023 | arXiv:2309.15217 | Metric formulation for evaluating faithfulness, answer relevance, and context precision in RAG pipelines. | [arXiv:2309.15217](https://arxiv.org/abs/2309.15217) |

---

## 2. Theoretical Architecture Integration

### 2.1 Hypothetical Document Embeddings (HyDE) - Gao et al. (2022)
In VICTORIA, queries often lack lexical richness. Instead of directly embedding a short inquiry (e.g., *"frais de déplacement doctorant"*), the LLM synthesizes a hypothetical administrative excerpt. As established by Gao et al., embedding this synthetic document shifts the search vector closer to the latent space of formal administrative circulars, drastically improving semantic recall.

### 2.2 Hybrid Retrieval and RRF - Robertson et al. (2009), Cormack et al. (2009)
While dense bi-encoders capture semantic intent, they suffer from degradation on exact alphanumeric identifiers (e.g. `ED 549`, `LIFAT`, `AAP 2026`). BM25 preserves exact token matching. Using Reciprocal Rank Fusion ensures neither score range dominates, providing robust retrieval across both paraphrased questions and strict institutional acronyms.

### 2.3 Cross-Encoder Reranking - Xiao et al. (2023)
Bi-encoders map queries and passages into independent vectors, preventing token-level interaction during retrieval. BGE-Reranker processes the query and top candidate passages jointly across all self-attention layers, computing fine-grained token alignments that suppress false positives before context generation.
