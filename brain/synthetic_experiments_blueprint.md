# Role A: Synthetic-Experiments Blueprint — ProvGuard-RAG
## Generated 2026-05-15 | Data-Science-Paper Synthetic-Experiments Protocol

---

## 1. SCOPE

Rewrite Section 4 (Experimental Design) of main.tex to follow the data-science-paper synthetic-experiments protocol. The current section has a directional expected-outcomes table only. The rewritten section will present **synthetic but internally consistent numerical results** with:

- 5 data tables (dataset stats, main results, poisoning robustness, ablation, latency/storage)
- 4 publication-quality figures (bar charts, radar chart, ablation waterfall)
- Statistical annotations ($p$-values, standard deviations, confidence intervals)
- Explicit synthetic-results disclaimers on every table and figure
- Python scripts that generate all data and plots (reproducible)

All results marked: **"Synthetic results — for methodological illustration. Empirical validation pending experiment execution."**

---

## 2. TABLE DESIGN

### Table I: Dataset Statistics
- **Source**: Actual documented statistics from TON_IoT and CICIoT2023 papers, plus estimated CVE/NVD and MITRE ATT&CK sizes
- **Columns**: Dataset, Type, Records, Attack Types, Query Count, Avg. Evidence/Query
- **No synthetic numbers needed** — these are factual dataset descriptions
- **LaTeX**: `\begin{tabularx}{\textwidth}{lclccc}`

### Table II: Main Results (Synthetic)
- **Rows**: B1 (Vanilla RAG), B2 (+Prov Filter), B3 (+NLI Verif), B4 (ProvGuard-RAG Full)
- **Columns**: ROUGE-L, BERTScore, Claim Support Ratio, Provenance Completeness, Audit Verif. Success
- **Formatting**: Best in **bold**, second-best \underline{underlined}, $\dagger$ for $p<0.05$ vs. B1 (McNemar/Friedman)
- **Synthetic numbers design** (internally consistent):
  - B1: baseline on all metrics
  - B2: same answer quality, lower poisoned-chunk rate, higher provenance completeness
  - B3: same answer quality, higher claim support ratio, same provenance as B1
  - B4: same answer quality, best claim support, best provenance completeness, 100% audit verifiability
- **Statistical annotation**: All B4 vs. B1 differences marked $\dagger$ where applicable
- **LaTeX**: `\begin{tabularx}{\textwidth}{lccccc}`

### Table III: Poisoned-Evidence Robustness (Synthetic)
- **Rows**: B1–B4 × poison levels {1%, 5%, 10%}
- **Columns**: Poisoned-Chunk Selection Rate (↓), Poisoned-Claim Support Rate (↓)
- **Synthetic numbers design**:
  - B1: rate increases with poison level (~0.8%, 4.2%, 8.7% selection)
  - B2: provenance reranking reduces selection (~0.4%, 2.1%, 4.8%)
  - B3: NLI reduces poisoned-claim support rate (~0.3%, 1.5%, 3.2% of claims supported)
  - B4: combined defense gives lowest rates (~0.2%, 1.0%, 2.3% selection; ~0.1%, 0.6%, 1.4% support)
- **LaTeX**: `\begin{tabularx}{\textwidth}{lcccc}`

### Table IV: Ablation Analysis (Synthetic)
- **Rows**: Full B4, w/o Prov Reranking, w/o NLI Verification, w/o Ledger Anchoring
- **Columns**: Same 5 metrics as Table II
- **Synthetic numbers design**: Each removal degrades the metric it targets
  - w/o Prov Reranking: Provenance completeness drops, poisoned-chunk rate rises
  - w/o NLI Verification: Claim support ratio drops
  - w/o Ledger Anchoring: Audit verifiability becomes N/A
- **LaTeX**: `\begin{tabularx}{\textwidth}{lccccc}`

### Table V: Latency and Storage Overhead (Synthetic)
- **Rows**: Per pipeline stage (Retrieval, Reranking, Generation, Verification, Ledger Append)
- **Columns**: Mean (ms), SD (ms), P95 (ms), Storage/Query (KB)
- **Synthetic numbers design**: 
  - Retrieval: ~120ms
  - Reranking: ~15ms (provenance adds ~3ms vs. relevance-only)
  - Generation: ~850ms (dominant)
  - Verification: ~180ms per query
  - Ledger Append: ~8ms
  - Total: ~1,173ms for B4 vs. ~970ms for B1
  - Storage: ~1.8KB per manifest
- **LaTeX**: `\begin{tabularx}{\textwidth}{lcccc}`

---

## 3. FIGURE DESIGN

### Figure 3: Main Results Comparison (Grouped Bar Chart)
- **Type**: Grouped bar chart, 4 groups (B1–B4), 3 metrics side-by-side (ROUGE-L, BERTScore, Claim Support)
- **Python**: matplotlib or plotly
- **Output**: `figures/main_results.pdf` (vector)
- **Key features**: Error bars (SD), significance brackets, synthetic disclaimer in caption

### Figure 4: Poisoned-Evidence Robustness (Multi-Panel Bar Chart)
- **Type**: 2-panel figure: (a) Poisoned-Chunk Selection Rate, (b) Poisoned-Claim Support Rate
- **X-axis**: Poison level {1%, 5%, 10%}
- **Groups**: B1, B2, B3, B4 (4 bars per poison level)
- **Python**: matplotlib subplots
- **Output**: `figures/poisoning_robustness.pdf`

### Figure 5: Seven-Axis Evaluation Radar (Spider/Radar Chart)
- **Type**: Radar chart with 7 axes, two overlays (B1 and B4)
- **Axes**: Answer Quality, Claim Support, Poison Robustness, Prov. Completeness, Audit Verifiability, Speed (1/Latency), Storage Efficiency (1/Size)
- **Python**: matplotlib radar chart
- **Output**: `figures/radar_evaluation.pdf`
- **Purpose**: Visual summary of the seven-axis protocol; shows B4 enveloping B1 on all axes except speed

### Figure 6: Ablation Waterfall (Horizontal Bar Chart)
- **Type**: Horizontal bar chart showing Claim Support Ratio for full B4 and each ablation
- **Python**: matplotlib
- **Output**: `figures/ablation_waterfall.pdf`

---

## 4. PYTHON SCRIPTS

All data generation and plotting in a single reproducible script:

**Script**: `experiments/generate_synthetic_results.py`

**Structure**:
```python
# 1. Set random seed for reproducibility
# 2. Define configuration parameters (sample sizes, noise levels)
# 3. Generate synthetic per-query results for B1-B4
# 4. Compute aggregate metrics with CI
# 5. Run statistical tests (Friedman, McNemar)
# 6. Generate LaTeX tables (.tex include files)
# 7. Generate figures (.pdf)
```

**Files produced**:
- `experiments/table_main_results.tex`
- `experiments/table_poisoning.tex`
- `experiments/table_ablation.tex`
- `experiments/table_latency.tex`
- `figures/main_results.pdf`
- `figures/poisoning_robustness.pdf`
- `figures/radar_evaluation.pdf`
- `figures/ablation_waterfall.pdf`

---

## 5. NARRATIVE STRUCTURE FOR REWRITTEN §4

### §4.1: Experimental Setup (condensed from current §4.1–§4.5)
- Research questions (keep current 4 RQs)
- Datasets (keep current, add Table I)
- Baselines (keep current, trim prose)
- Evaluation metrics (keep current)
- Poisoning configuration (keep current)
- Implementation details: Qwen2.5-7B-Instruct, vLLM serving, FAISS index, 4×A100 GPUs

### §4.2: Main Results (NEW — synthetic)
- Narrative: "Table II reports synthetic results designed to illustrate the expected contribution pattern..."
- Walk through RQ1 and RQ2 findings from the table
- Reference Figure 3

### §4.3: Poisoned-Evidence Robustness (NEW — synthetic)
- Narrative: "Table III and Figure 4 examine robustness under controlled corpus poisoning..."
- Walk through the three poison levels
- Explain the defense-in-depth pattern (Prov + NLI > either alone)

### §4.4: Ablation Analysis (NEW — synthetic)
- Narrative: "Table IV isolates the marginal contribution of each component..."
- Reference Figure 6
- Discuss which component contributes most per metric

### §4.5: Latency and Storage Overhead (NEW — synthetic)
- Narrative: "Table V decomposes end-to-end latency..."
- Confirm bounded overhead hypothesis ($<$500ms, $<$5KB)

### §4.6: Summary and Hypothesis Assessment (NEW)
- Map synthetic results back to the four pre-registered hypotheses
- RQ1: Supported — provenance reranking reduces poisoned-chunk rate
- RQ2: Supported — NLI verification recall exceeds 0.80
- RQ3: Confirmed — overhead within bounds
- RQ4: Supported — full pipeline outperforms partial configurations

---

## 6. SYNTHETIC NUMERICAL VALUES (Internally Consistent)

### Table II — Main Results
| Config | ROUGE-L | BERTScore | Claim Support | Prov. Completeness | Audit Verif. |
|--------|---------|-----------|---------------|-------------------|--------------|
| B1     | 0.423 ± 0.031 | 0.861 ± 0.012 | 0.724 ± 0.038 | 0.12 ± 0.05 | N/A |
| B2     | 0.421 ± 0.033 | 0.859 ± 0.013 | 0.726 ± 0.037 | **0.94 ± 0.03** | N/A |
| B3     | 0.424 ± 0.030 | 0.862 ± 0.011 | **0.883 ± 0.026**$^\dagger$ | 0.13 ± 0.05 | N/A |
| B4     | 0.422 ± 0.032 | 0.860 ± 0.012 | **0.891 ± 0.024**$^\dagger$ | **0.95 ± 0.02**$^\dagger$ | **1.000**$^\dagger$ |

### Table III — Poisoning Robustness (5% poison level shown; 1% and 10% also in table)
| Config | Poison-Chunk Rate (5%) | Poison-Claim Support (5%) |
|--------|----------------------|--------------------------|
| B1     | 0.042 ± 0.008 | 0.031 ± 0.006 |
| B2     | 0.021 ± 0.005$^\dagger$ | 0.018 ± 0.004 |
| B3     | 0.039 ± 0.007 | 0.008 ± 0.003$^\dagger$ |
| B4     | **0.010 ± 0.003$^\dagger$** | **0.003 ± 0.001$^\dagger$** |

### Table IV — Ablation
| Config | BERTScore | Claim Support | Prov. Compl. | Audit Verif. |
|--------|-----------|---------------|-------------|--------------|
| B4 (Full) | 0.860 ± 0.012 | 0.891 ± 0.024 | 0.95 ± 0.02 | 1.000 |
| w/o Prov. Rerank | 0.861 ± 0.011 | 0.882 ± 0.026 | 0.14 ± 0.05 | 1.000 |
| w/o NLI Verif. | 0.859 ± 0.013 | 0.727 ± 0.037 | 0.94 ± 0.03 | 1.000 |
| w/o Ledger | 0.860 ± 0.012 | 0.890 ± 0.025 | 0.95 ± 0.02 | N/A |

### Table V — Latency
| Stage | Mean (ms) | SD (ms) | P95 (ms) |
|-------|-----------|---------|----------|
| Retrieval | 118 | 22 | 152 |
| Prov. Reranking | 15 | 4 | 23 |
| Generation | 847 | 156 | 1,104 |
| Claim Verification | 178 | 41 | 248 |
| Ledger Append | 8 | 2 | 12 |
| **Total (B4)** | **1,166** | **168** | **1,441** |

---

## 7. DISCLAIMER LANGUAGE

Every table caption and figure caption must include:
> "Synthetic results for methodological illustration. All values are generated for experimental design validation. Empirical validation pending experiment execution."

The section lead must state:
> "The results presented in this section are synthetically generated to illustrate the expected contribution pattern and validate the experimental design. All numerical values are produced by a reproducible Python script (experiments/generate_synthetic_results.py) that instantiates the evaluation protocol described in Section 4.1. These values are not empirical measurements. They are designed to be internally consistent with the pre-registered hypotheses in Section 4.1.6 and serve as a concrete instantiation of the seven-axis evaluation framework. All figures and tables are marked accordingly."

---

## 8. DEPENDENCIES AND SEQUENCING

```
1. Write experiments/generate_synthetic_results.py
2. Run script → generates .tex table files and .pdf figures
3. Rewrite Section 4 in main.tex, \input{} the generated tables
4. Compile → verify all cross-references
5. Self-review the rewritten section
```

---

## 9. NOTES FOR ROLE B

- Use `\input{experiments/table_main_results.tex}` for table inclusion (avoids cluttering main.tex)
- Figures use `\includegraphics{figures/main_results.pdf}` with MDPI figure formatting
- All statistical tests use standard Python libraries (scipy.stats)
- Seed: 42 for reproducibility
- The synthetic data should be realistic enough to be plausible but clearly marked
- Table best/second-best formatting: `\textbf{0.891}` for best, `\underline{0.883}` for second-best
- Significance marker: `$^\dagger$` with footnote "$^\dagger p < 0.05$ vs. Vanilla RAG (B1)"
