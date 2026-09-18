# Corpus Ingestion & Extraction Diagnostic Report

## 1. Corpus Overview and Scope

This diagnostic report evaluates the automated document ingestion and extraction pipeline executed on the institutional corpus of the Direction de la Recherche et de la Valorisation (DRV) at the University of Tours.

The corpus comprises official administrative acts, internal regulations, procedure workflows, call-for-project guidelines, and financial templates spanning four main administrative departments:
- **AFRV** : Antenne Financière de la Recherche et de la Valorisation
- **RED / Doctorat** : Recherche et Écoles Doctorales
- **SPIV** : Service du Partenariat et de l'Ingénierie de Valorisation
- **PJR** : Pôle Juridique Recherche

---

## 2. Quantitative Summary Statistics

Data extracted and validated from the systematic batch run logs (`TestExtraction/logs/marker_test_report.json`):

| Diagnostic Metric | Quantitative Value | Standard Reference |
|---|---|---|
| Total Documents Processed | 120 PDF files | Full institutional set |
| Total Cumulated Pages | 904 pages | Average: 7.53 pages/doc |
| Total Corpus Disk Volume | 100.44 MB | Average: 0.84 MB/doc |
| Total Extracted Characters | 2,268,697 characters | Markdown textual payload |
| Total Extracted Words | 243,396 words | Clean lexical tokens |
| Mean Alpha Ratio | 0.6438 | Alphabetical / Total char density |
| Non-searchable / Scanned Documents | 21 documents (17.5%) | OCR Fallback Triggered |
| Pipeline Conversion Success Rate | 100.0% (120 / 120) | Zero catastrophic failures |

---

## 3. Departmental Distribution

```
Corpus Breakdown by Administrative Service:
├── RED (Doctoral Studies & Regulations) : 58 documents (48.3%)
├── AFRV (Financial Management & Claims)  : 24 documents (20.0%)
├── SPIV (Partnerships, Tech Transfer)   : 20 documents (16.7%)
└── PJR (Legal, IP, Ethics)              : 18 documents (15.0%)
```

---

## 4. Technical Challenges and Mitigation

### 4.1 Scanned and Low-Text-Layer Documents (17.5%)
- **Problem** : 21 documents were scanned administrative circulars or signed presidential decrees with missing or corrupt font maps.
- **Diagnostics** : Identified by pre-check analyzer when `sample_text_chars < 50` or `sample_alpha_ratio == 0.0`.
- **Resolution** : Automatic trigger of the `marker` dual-engine pipeline with Tesseract OCR backend (`fra` language package, 300 DPI page rasterization), restoring full textual searchability.

### 4.2 Tabular Data Preservation
- **Problem** : Administrative budget tables and expense ceiling charts frequently break during conventional PDF text dumps (e.g. `pdftotext`).
- **Resolution** : Structural analysis reconstructed merged cells into clean GitHub-Flavored Markdown tables, ensuring accurate vector retrieval for threshold questions (e.g. daily allowance limits, funding percentages).

### 4.3 Acronym Disambiguation
- **Problem** : High recurrence of condensed institutional acronyms (ED 549, SSBCV, MIPTIS, EMSTU, SPIV, AFRV, CAC, CS).
- **Resolution** : Preservation of exact typographic tokens in sparse BM25 index and chunk metadata domain tagging.
