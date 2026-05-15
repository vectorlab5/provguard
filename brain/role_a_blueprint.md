# Role A: Manuscript Blueprint — ProvGuard-RAG
## Generated 2026-05-15 | Target: MDPI AI journal

---

## 1. EXISTING DRAFT AUDIT (Introduction + Related Work)

### 1.1 Structural Assessment

**Introduction (lines 85–102 of main.tex): 7 paragraphs.** The data-science-paper skill targets 5–6 paragraphs for journal introductions. The current draft is slightly overlong. The blockchain paragraph (P4, line 91) overlaps with the provenance paragraph (P3, line 89) in its argumentative function — both argue that evidence traceability matters. Recommendation: merge P3 and P4 into a single "provenance and tamper-evidence" paragraph, reducing to 6 paragraphs total.

**Paragraph-by-paragraph evaluation:**

| Para | Function | Quality | Issue |
|------|----------|---------|-------|
| P1 (line 85) | Domain hook | Strong | Specific, domain-grounded. No generic opener. |
| P2 (line 87) | RAG gap | Strong | Cites Chen2024 and Wang2023 correctly. Establishes that retrieval alone is insufficient. |
| P3 (line 89) | Provenance gap | Good | Overlaps with P4. Could be sharper about what provenance means for RAG specifically (vs. general AI). |
| P4 (line 91) | Blockchain relevance | Good, but redundant | The restraint is correct, but the argument that "hashes not raw data go on-chain" can be folded into P3. |
| P5 (line 93) | Gap synthesis | Strong | The four-stream gap statement is the paper's strongest argumentative move. Preserve exactly. |
| P6 (line 95) | Method + contributions | Adequate | Contribution 4 ("reproducible experimental plan") is weak for a journal. See §3 below. |
| P7 (line 102) | Roadmap | Adequate | Fine, but references sections that don't exist yet. Will need updating. |

**Related Work (lines 104–133): 4 subsections.** The thematic structure is sound. The positioning subsection (§2.4) does excellent work. Missing categories: (a) RAG security and adversarial retrieval literature, (b) semantic claim verification / natural language inference methods, (c) CPS-specific incident-response systems with LLM components.

### 1.2 Critical Blocking Issues

**BLOCKING — Template mismatch:** `main.tex` uses `\documentclass[conference]{IEEEtran}`. MDPI AI journal requires the MDPI LaTeX class (`\documentclass[computerscience]{mdpi}` or similar). IEEE-specific environments (`IEEEkeywords`, `IEEEauthorblockN`, `\bibliographystyle{IEEEtran}`) are incompatible. **The template must be replaced before any further drafting.**

**BLOCKING — Citation insufficiency:** `references.bib` contains 8 entries. All 5 files in `refs/` are empty (0 bytes). The data-science-paper skill requires 30+ citations for journal papers. Missing categories:
- CPS/IoT security datasets (TON_IoT, CICIoT2023, Edge-IIoTset, etc.)
- RAG security: retrieval poisoning, prompt injection, adversarial context
- Semantic textual entailment / fact verification methods
- CPS incident response architectures
- Cryptographic provenance / Merkle-log systems
- MDPI AI journal exemplars (3+ needed)

**BLOCKING — Experiment status:** Design-only. Cannot claim empirical results. The synthetic-experiments approach from the data-science-paper skill must be used, with all claims explicitly marked as planned.

### 1.3 AI-Pattern Check

The existing prose passes the major AI-detection checks: no "In recent years," no "plays a crucial role," no "has attracted significant attention." The blockchain paragraph avoids overclaiming ("does not justify storing raw CPS logs on-chain" is well-calibrated). 

Minor risks:
- Some sentences in P5 exceed 35 words — break for readability
- "This paper therefore targets a gap between four research streams" is clear but could be sharper about *why* this gap exists (structural vs. accidental)

---

## 2. REFINED RESEARCH FRAMING

### 2.1 Research Gap (sharpened)

Existing RAG evaluation frameworks test retrieval relevance and answer correctness. Existing provenance systems record data lineage at rest. Existing LLM audit frameworks distinguish governance, model, and application layers. But **no existing framework simultaneously operationalizes retrieval relevance, source provenance, semantic claim support, and post-hoc auditability as jointly measurable properties of a single RAG interaction in a cyber-physical incident context.** The gap is structural — these concerns are addressed in separate literatures that do not intersect at the retrieval-generation loop.

### 2.2 Research Question

*Can a RAG system for cyber-physical incident intelligence be designed so that provenance-aware evidence ranking, semantic claim verification, and ledger-anchored audit manifests jointly reduce unsupported or poisoned-evidence-grounded answers while enabling post-hoc verifiability with bounded overhead?*

Sub-questions:
1. Does provenance-aware reranking (source trust, recency, verification status) reduce poisoned-evidence selection compared to relevance-only reranking?
2. Can semantic claim verification detect unsupported claims without requiring ground-truth answer labels?
3. What is the storage and latency overhead of ledger-anchored audit manifests in a CPS incident-intelligence pipeline?
4. Does the combination of provenance-aware retrieval and semantic verification improve auditability beyond what either mechanism achieves alone?

### 2.3 Core Argument

A trustworthy RAG system for cyber-physical incident intelligence cannot be built by stacking retrieval, generation, and provenance as independent modules. Instead, provenance metadata must enter the retrieval-and-ranking loop, generated claims must be verified against retrieved evidence before presentation, and the entire evidence-to-answer chain must be recorded in a tamper-evident manifest. This coupling creates measurable auditability properties that standard RAG pipelines do not expose.

### 2.4 Theoretical Framework

The paper operationalizes three concepts:
- **Evidence faithfulness** (from RAG evaluation): a generated claim is faithful if it is semantically entailed by the retrieved evidence set.
- **Provenance traceability** (from data provenance): every retrieved chunk is linked to a source identifier, ingestion timestamp, parser version, and cryptographic hash.
- **Audit verifiability** (from LLM auditing): a third party can reconstruct the evidence-to-answer chain and verify that the evidence was not altered post-retrieval, without accessing the raw corpus.

These are not novel concepts individually. The contribution is their joint operationalization inside a single RAG architecture.

### 2.5 Assumptions (explicit)
1. The retrieval corpus is pre-registered with provenance metadata (source ID, timestamp, hash). We assume this registration step is feasible and not the system's bottleneck.
2. The ledger/Merkle-log component is used only for hash anchoring, not for content storage. We assume a lightweight append-only log (e.g., Trillian, Merkle tree) with negligible write cost per query.
3. Semantic verification uses an off-the-shelf NLI model fine-tuned on domain data. We assume NLI accuracy is sufficient to flag unsupported claims as a screening tool, not as a definitive truth oracle.
4. The CPS incident intelligence setting is scoped to textual evidence (logs, alerts, policies, vulnerability records), not real-time sensor streams or video.

---

## 3. REFINED CONTRIBUTION SET

The Introduction draft proposes four contributions. Below is the refined set with sharper specificity:

**C1. Problem formulation.** A formal definition of trustworthy cyber-physical RAG that decomposes system trustworthiness into four jointly measured properties: answer correctness, evidence faithfulness, provenance traceability, and audit verifiability. This formulation extends standard RAG evaluation (which tests correctness and relevance) by making provenance and auditability first-class evaluation targets.

**C2. ProvGuard-RAG architecture.** A modular framework with five connected components: (i) provenance-registered evidence indexing, (ii) hybrid retrieval with provenance-aware reranking, (iii) claim decomposition from generated responses, (iv) semantic claim-evidence verification, (v) ledger-anchored audit manifest construction. The architecture is designed so that components (iii)–(v) can be added to an existing RAG pipeline without retraining the generator.

**C3. Evaluation protocol for trustworthy CPS RAG.** A multi-metric evaluation framework covering seven axes: answer quality (ROUGE, BERTScore, human judgment), claim support (NLI entailment ratio), poisoned-evidence robustness (selection rate under adversarial injection), provenance completeness (metadata coverage ratio), audit verification (tamper-detection success), retrieval latency, and manifest storage overhead. This protocol operationalizes the joint measurement described in C1.

**C4. Reproducible benchmark instantiation.** A concrete instantiation of the ProvGuard-RAG pipeline and evaluation protocol on public CPS/IoT security datasets (nominated: TON_IoT, CICIoT2023), public vulnerability knowledge bases (CVE/NVD, MITRE ATT&CK), and open-weight LLMs. All dataset preprocessing scripts, evaluation code, and configuration files will be released. This contribution is methodological — we provide the first reproducible benchmark for provenance-aware CPS RAG — and empirical claims are explicitly marked as planned until experiments are executed.

*Note: C4 replaces the weaker "reproducible experimental plan" language from the Introduction draft. The new framing positions the contribution as a benchmark infrastructure contribution, which is publishable even without experimental results, provided the benchmark design is rigorous.*

---

## 4. MDPI AI VENUE-FIT ANALYSIS

### 4.1 Journal Scope Alignment

MDPI AI (ISSN 2673-2688) publishes on: machine learning, deep learning, NLP, computer vision, robotics, AI ethics, explainable AI, trustworthy AI, AI applications, and AI systems. The ProvGuard-RAG paper aligns with:
- **Trustworthy AI**: provenance, auditability, verifiability are core trustworthy-AI concerns.
- **NLP / LLMs**: RAG, claim verification, semantic entailment.
- **AI systems**: the architecture is a systems contribution connecting retrieval, verification, and audit logging.
- **AI applications**: cyber-physical incident intelligence is an application domain.

### 4.2 Required Template Changes

MDPI AI uses the MDPI LaTeX class. The current IEEEtran template must be replaced. Actions:
1. Download MDPI LaTeX template from https://www.mdpi.com/authors/latex
2. Replace `\documentclass[conference]{IEEEtran}` with MDPI class
3. Replace `IEEEkeywords` with MDPI `\keyword{}` macro
4. Replace IEEE author block with MDPI author format
5. Replace `\bibliographystyle{IEEEtran}` with MDPI bibliography style
6. Switch from double-column to single-column
7. Adjust figure/table formatting to MDPI standards

### 4.3 Length Expectations

MDPI AI allows 15–25 pages in the published template (single-column). Our target: ~18 pages including figures, tables, and references. Current draft (Introduction + Related Work) is approximately 2,500 words. Extrapolating to full paper: ~8,000–10,000 words of body text.

---

## 5. SECTION-BY-SECTION WRITING PLAN

### Section 1: Introduction (revised from existing draft)
- **Target length**: 6 paragraphs, ~1,500 words
- **Changes needed**:
  1. Merge P3 (provenance) and P4 (blockchain) into single paragraph
  2. Replace C4 with the benchmark-instantiation framing (§3 above)
  3. Add one sentence aligning with MDPI AI's trustworthy-AI scope
  4. Break long sentences (>30 words) in P5
- **Template action**: Adapt to MDPI class after template migration

### Section 2: Related Work (revised from existing draft)
- **Target length**: 5 subsections, ~2,500 words
- **Changes needed**:
  1. Add §2.5: RAG Security and Adversarial Retrieval (new subsection covering retrieval poisoning, prompt injection, adversarial context injection)
  2. Add to §2.1: semantic claim verification / NLI methods for fact-checking
  3. Add to §2.3: CPS-specific incident-response systems
  4. Increase citation count: current 8 → target 35+
- **Citations to add (minimum)**:
  - RAG security: retrieval poisoning attacks, corpus poisoning defenses
  - NLI/verification: FEVER, FactCC, SummaC, AlignScore
  - CPS incident response: IDS/IPS with LLM components, SOAR platforms
  - Datasets: TON_IoT, CICIoT2023, Edge-IIoTset
  - Merkle/transparency logs: Certificate Transparency, Trillian, Sigstore

### Section 3: Proposed Method — ProvGuard-RAG
- **Target length**: ~3,000 words, 5 subsections
- **Structure**:
  - §3.1: Problem Formulation (formal notation, trustworthy RAG decomposition)
  - §3.2: System Architecture Overview (pipeline figure)
  - §3.3: Provenance-Registered Evidence Indexing (source registration, chunking, hashing)
  - §3.4: Hybrid Retrieval with Provenance-Aware Reranking (BM25 + dense, multi-factor scoring)
  - §3.5: Claim Decomposition and Semantic Verification (claim extraction, NLI-based support check)
  - §3.6: Ledger-Anchored Audit Manifest (what goes in the manifest, hash chaining)
  - §3.7: Algorithm (pseudocode for end-to-end query flow)
- **Key deliverables**: 5–7 numbered equations, 1 algorithm (algorithm2e), 1 architecture figure, notation table

### Section 4: Experimental Design (synthetic-experiments approach)
- **Target length**: ~2,500 words
- **Structure**:
  - §4.1: Research Questions (map to RQ1–RQ4 from §2.2)
  - §4.2: Datasets (TON_IoT, CICIoT2023, CVE/NVD, MITRE ATT&CK)
  - §4.3: Baselines (standard RAG, RAG + provenance filter, RAG + NLI verification)
  - §4.4: Evaluation Metrics (7-axis protocol from C3)
  - §4.5: Experimental Configuration (model versions, hyperparameters, hardware)
  - §4.6: Expected Outcomes and Hypothesis Tests (per-RQ predictions, statistical tests)
- **Critical rule**: All result tables contain "Planned" or "Expected" labeling. No fabricated numbers. The section reports experimental *design*, not results.

### Section 5: Discussion (planned)
- **Target length**: ~1,200 words
- **Structure**:
  - Interpretation framework for expected results
  - Failure mode analysis (when provenance reranking might hurt, NLI verification limits)
  - Generalizability beyond CPS (legal, medical, financial RAG)
  - Threat to validity: dataset representativeness, NLI model limitations, ledger trust assumptions

### Section 6: Conclusion
- **Target length**: ~400 words
- **Structure**: Summary of contributions, limitations (explicit), future work (poisoning-robust reranking, multi-modal CPS evidence, real deployment evaluation)

### Section 7: Abstract
- **Target length**: 200 words
- **Written last** (per skill guidance)
- **Structure**: Problem → Approach → Contributions → Significance

---

## 6. SYNTHETIC-EXPERIMENT PROTOCOL

Following `references/synthetic-experiments.md` from the data-science-paper skill:

### 6.1 Dataset Configuration
| Dataset | Type | Size | Use |
|---------|------|------|-----|
| TON_IoT | Network/telemetry | ~22M records | Primary benchmark: incident queries with ground-truth evidence |
| CICIoT2023 | IoT attack traffic | ~33 types | Diversity test: attack-type coverage |
| CVE/NVD | Vulnerability DB | ~200K entries | Knowledge base: vulnerability evidence |
| MITRE ATT&CK | Attack taxonomy | ~600 techniques | Knowledge base: attack-pattern evidence |

### 6.2 Baseline Grid
| Baseline | Retrieval | Reranking | Verification | Audit |
|----------|-----------|-----------|--------------|-------|
| B1: Vanilla RAG | BM25 + dense | Relevance only | None | None |
| B2: RAG + ProvFilter | BM25 + dense | Relevance + source trust | None | None |
| B3: RAG + NLI | BM25 + dense | Relevance only | NLI entailment | None |
| B4: ProvGuard-RAG (full) | BM25 + dense | Relevance + provenance | NLI entailment | Ledger manifest |

### 6.3 Hypothesis Table
| RQ | Hypothesis | Metric | Expected Direction |
|----|-----------|--------|--------------------|
| RQ1 | ProvGuard-RAG selects fewer poisoned chunks than B1 | Poisoned-chunk selection rate | ProvGuard-RAG < B1 (p<0.05) |
| RQ2 | NLI verification flags >80% of unsupported claims | Claim-support recall | >0.80 |
| RQ3 | Manifest overhead <200ms per query, <2KB storage per query | Latency, storage | Bounded |
| RQ4 | ProvGuard-RAG manifest verification succeeds where B1 has no audit artifacts | Manifest verifiability (binary) | ProvGuard-RAG = 1.0, B1 = N/A |

### 6.4 Planned Tables and Figures
- **Table I**: Dataset statistics
- **Table II**: Main results (answer quality + claim support + provenance completeness)
- **Table III**: Poisoned-evidence robustness
- **Table IV**: Ablation (remove provenance reranking, remove NLI verification, remove ledger anchoring)
- **Table V**: Latency and storage overhead
- **Figure 1**: ProvGuard-RAG architecture diagram
- **Figure 2**: Audit manifest structure (schematic)
- **Figure 3**: Expected performance radar chart (7-axis evaluation)

---

## 7. CITATION EXPANSION PLAN

### 7.1 Categories to Populate (minimum counts)

| Category | Min. Citations | Candidate Sources |
|----------|---------------|-------------------|
| RAG evaluation & methods | 6 | Keep existing + add Self-RAG, CRAG, ARES |
| RAG security / adversarial | 4 | Retrieval poisoning, corpus poisoning, prompt injection |
| Provenance & blockchain | 5 | Keep existing + add Merkle/transparency log papers |
| LLM auditing & governance | 3 | Keep Mökander + add 2 more |
| Semantic verification / NLI | 5 | FEVER, FactCC, SummaC, AlignScore, ANLI |
| CPS/IoT datasets | 4 | TON_IoT, CICIoT2023, Edge-IIoTset, UNSW-NB15 |
| CPS incident response | 3 | SOAR, IDS with LLM, threat intelligence platforms |
| MDPI AI exemplars | 3 | Recent MDPI AI papers on trustworthy AI / RAG |
| Domain-specific RAG | 2 | Keep Louis2024 + add 1 more |
| **Total** | **35+** | |

### 7.2 Immediate Action
Run `paper-search` skill to populate the empty `refs/*.bib` files. Priority order: datasets → RAG security → semantic verification → CPS incident response.

---

## 8. WRITING CONSTRAINTS (FROM SKILL + VENUE)

1. **Paragraph discipline**: 4–8 sentences per paragraph. No bullet lists in body text (except contribution list).
2. **No AI-filler phrases**: See forbidden-phrases.md. Specifically prohibited: "In recent years," "plays a crucial role," "has attracted significant attention," "state-of-the-art," "demonstrates the effectiveness."
3. **Claim-evidence discipline**: Every non-obvious claim cites a source or is marked as an assumption/hypothesis.
4. **No fabricated results**: All experimental claims labeled "planned," "expected," or "hypothesized."
5. **Citation prose**: Integrate citations into sentences (e.g., "Chen et al. [X] showed that..."), not parenthetical lists.
6. **Equation discipline**: All equations numbered and referenced in text. Notation table in Method section.
7. **MDPI formatting**: Single-column, MDPI bibliography style, MDPI author format, MDPI section numbering.

---

## 9. SEQUENCING AND DEPENDENCIES

```
Phase A: Template Migration → MDPI class replacement
Phase B: Literature Expansion → paper-search skill → populate refs/*.bib (BLOCKS all writing)
Phase C: Section Revision → Introduction + Related Work (revise per audit)
Phase D: New Drafting → Method → Experiments → Discussion → Conclusion → Abstract
Phase E: Quality Assurance → check_ai_patterns.py → check_quality.py → manual audit
```

**Dependency note**: Phase D (Method drafting) can begin in parallel with Phase B (literature search) for the architectural description, but citation-heavy parts of Method (§3.4–§3.5 on NLI and reranking) require literature completion.

---

## 10. OPEN QUESTIONS FOR USER

1. **MDPI AI template**: Should I download and install the MDPI LaTeX template now, or defer template migration until after all sections are drafted in the current IEEE format?
2. **Benchmark datasets**: TON_IoT and CICIoT2023 are nominated. Are these acceptable, or do you have preferred alternatives?
3. **LLM choice for experiments**: The method is LLM-agnostic. Which open-weight model should the experiment plan target (e.g., Llama-3-8B, Mistral-7B, Qwen2.5-7B)?
4. **Ledger implementation**: The audit manifest uses "ledger or Merkle-log." Should the paper commit to a specific implementation (e.g., Trillian, Sigstore/Rekor) or keep it abstract?
5. **Co-authors**: The author block in main.tex is placeholder. Who are the co-authors and affiliations?
