# Role B: Critical Self-Review and Revision Plan
## ProvGuard-RAG | Target: MDPI AI | Date: 2026-05-15

---

## Section 1: Introduction — Self-Review

### What works
- **Domain-grounded opening.** The first sentence immediately situates the paper in a concrete problem: evidence-control for CPS incident answers. No generic opener.
- **Merged provenance + blockchain paragraph (P3).** The audit recommendation to fold P3 and P4 is executed. The resulting paragraph moves from the provenance gap → why provenance matters for RAG → how ledger anchoring provides tamper-evidence without on-chain content. The argument flows, and the restraint on blockchain claims is preserved.
- **Gap statement (P4).** Explicitly calls the gap "structural rather than accidental" — this distinguishes the contribution from incremental work. Strongest sentence in the introduction.
- **Refined contribution list (C1–C4).** C4 is now framed as a benchmark infrastructure contribution, not a weak "experimental plan." Each contribution is specific enough to be verifiable.
- **Anti-AI compliance.** No "in recent years," "plays a crucial role," or "has attracted significant attention." Sentences vary in length. The prose is concrete.

### What needs revision
- **Paragraph 1 is too long (7 sentences, ~130 words).** The domain hook lists five sectors (industrial IoT, smart-city, transport, healthcare, energy) but the experiments target only IoT security datasets. This creates an evidence-domain mismatch. **Fix:** Trim the sector list to "industrial IoT and connected infrastructure" or add a sentence acknowledging the scope narrowing in experiments.
- **Roadmap paragraph (P6) references sections that may shift.** If §5 (Discussion) and §6 (Conclusion) are merged or reordered for MDPI format, the roadmap will be wrong. **Fix:** Defer final roadmap until all sections are stable.
- **Missing MDPI AI venue signal.** The introduction does not mention the MDPI AI journal's focus on trustworthy AI. **Fix:** Add one sentence in P1 or P5 connecting the work to trustworthy AI research.

### Revision actions
1. Trim P1 sector list or add scope-narrowing sentence
2. Add one-sentence MDPI AI venue alignment in P1 or P5
3. Update roadmap after all sections finalize

---

## Section 2: Related Work — Self-Review

### What works
- **Thematic structure.** Five subsections organized by research stream, not chronology. Each subsection ends with a sentence explaining what the stream does NOT address, creating forward momentum toward the positioning subsection.
- **Positioning subsection (§2.5).** Explicitly states what ProvGuard-RAG borrows from each stream and what it adds. This is the most important subsection in the related work and it delivers.
- **RAG security subsection (§2.4).** Now populated with three verified citations (PoisonedRAG, Xian et al., Ni et al. survey) instead of a placeholder paragraph. The defense-in-depth argument (provenance + verification as layered defenses) is articulated.

### What needs revision
- **Citation density is still below target.** 16 citations vs. the 35+ target. The RAG evaluation, provenance, and auditing subsections each have 2–4 citations; they need 5–8 each.
- **Missing subcategories.** The related work does not cover: (a) Retrieval-free or retrieval-light approaches for domain-specific QA, (b) CPS-specific incident response systems that use LLMs (SOAR platforms, threat intelligence automation), (c) Prompt engineering for evidence grounding.
- **RAG security subsection still marked as "in progress" at the end.** The final sentence says "A comprehensive review of additional RAG security literature is in progress and will be integrated before submission." This is honest but should be removed before submission.

### Revision actions
1. Add 12–15 more citations across all subsections via paper-search
2. Add CPS incident response paragraph to §2.3 or as new §2.6
3. Remove the "in progress" caveat before submission
4. Verify all 16 current citations via reference-validator skill

---

## Section 3: Method — Self-Review

### What works
- **Problem formulation (§3.1).** The four-property decomposition (correctness, faithfulness, traceability, auditability) is formal without being heavyweight. Each property is defined operationally, not just named.
- **Architecture description (§3.2).** Five-stage pipeline with clear boundaries. Each stage's input/output is specified. The design rationale choices (linear reranker, separate verifier, granular manifest) are justified in §3.3.
- **Equations are referenced and motivated.** The reranking score (Eq. 1), verification function (Eq. 2), and manifest structure (Eq. 3) each have a clear role in the argument. They are not decorative.
- **Algorithm pseudocode.** Concise, mirrors the architecture. The five-stage structure is visible in the comments.
- **Notation table.** Complete and consistent with the equations.

### What needs revision
- **The verification equation (Eq. 2) is a simplification.** Real NLI entailment is more nuanced than the max-over-documents formulation suggests. The SummaC paper shows that sentence-level aggregation matters. **Fix:** Add a sentence acknowledging this simplification and citing SummaC's chunking approach as the implementation strategy.
- **No ablation design in the method section.** The method should foreshadow which components are most likely to fail and why. The Discussion section handles failure modes, but the Method section could plant the seeds. **Fix:** Add one sentence per component identifying its primary fragility (e.g., "The source trust scores require domain calibration; mis-calibrated scores could penalize relevant evidence from novel sources").
- **The architecture figure is a placeholder.** MDPI AI requires publication-quality figures. **Fix:** Generate a TikZ or vector figure before submission.
- **Assumptions from the blueprint are not stated.** The blueprint lists four assumptions (pre-registration feasibility, lightweight log, NLI screening role, textual-only scope). These should appear in §3.1 or a dedicated assumptions paragraph. **Fix:** Add an explicit assumptions paragraph.
- **LLM choice (Qwen2.5-7B) is mentioned only in §3.2 but should be justified.** Why this model over Llama-3 or Mistral? **Fix:** Add a one-sentence justification (e.g., strong multilingual technical reasoning, Apache 2.0 license for reproducibility).

### Revision actions
1. Add explicit assumptions paragraph after problem formulation
2. Cite SummaC chunking approach for Eq. 2 implementation
3. Add component fragility sentences
4. Justify Qwen2.5-7B choice
5. Generate architecture figure (deferred to figure-generation phase)

---

## Section 4: Experimental Design — Self-Review

### What works
- **Pre-registered hypothesis structure.** Each RQ has a null hypothesis, alternative hypothesis, statistical test, and expected direction. This is publication-quality experimental design.
- **Explicit "planned" labeling.** The section leads with a disclaimer and every table/claim is marked as planned. No fabricated results.
- **Baseline grid is well-structured.** B1–B4 incrementally activate components, enabling clean ablation analysis.
- **Seven-axis evaluation protocol.** Directly operationalizes the four-property problem formulation from §3.1. Each metric maps to a property.
- **Expected outcome table.** Communicates the hypotheses visually without claiming results.

### What needs revision
- **Table I (dataset statistics) is placeholdered.** Need actual statistics: number of records, query types, evidence sources per dataset.
- **No gold-standard annotation plan for claim verification evaluation.** RQ2 requires expert-annotated ground truth for unsupported claims. The protocol should specify annotation guidelines, annotator qualifications, and inter-annotator agreement metric. **Fix:** Add an annotation methodology paragraph.
- **Poisoning attack parameters ($p_{\text{poison}}$) are not specified.** The poisoning experiment needs concrete parameters: what fraction of corpus is poisoned, what attack generation method, what target queries. **Fix:** Specify attack configuration.
- **BERTScore is used as an answer quality metric but may not capture CPS-domain correctness.** CPS incident answers require factual precision (was device D17 compromised at 14:17, not 14:18). BERTScore measures semantic similarity, not factual accuracy. **Fix:** Add a note that BERTScore is a proxy and that human expert judgment is the primary answer-quality metric.

### Revision actions
1. Populate dataset statistics with actual numbers from TON_IoT and CICIoT2023 documentation
2. Add annotation methodology for claim verification ground truth
3. Specify poisoning attack parameters
4. Add caveat about BERTScore as proxy metric
5. Remove placeholder figure references or mark them clearly

---

## Section 5: Discussion — Self-Review

### What works
- **Interpretation-first structure.** The section leads with how to interpret expected results, not with a re-summary of findings.
- **Failure mode analysis.** Anticipates four specific failure modes with root causes: mis-calibrated source trust, NLI domain shift, evidence corpus deletion, log trust assumption.
- **Limitations subsection.** Covers the five key limitations honestly: planning-stage status, text-only scope, entailment proxy limitation, dataset coverage, tamper-evidence vs. tamper-prevention.

### What needs revision
- **The generalizability argument (§5.3) is under-evidenced.** Claims that the framework generalizes to legal, medical, and financial domains without citing domain-specific RAG work in those areas. **Fix:** Add citations to legal RAG, medical RAG, and financial compliance RAG papers.
- **No connection back to the four-property formulation.** The Discussion should explicitly map each failure mode back to which property it threatens (e.g., NLI domain shift threatens evidence faithfulness; log trust assumption threatens audit verifiability). **Fix:** Add property-to-failure-mode mapping.

### Revision actions
1. Add domain-specific RAG citations for generalizability claim
2. Map failure modes to the four-property decomposition
3. Consider adding a "Broader Implications" paragraph connecting to MDPI AI's trustworthy AI scope

---

## Section 6: Conclusion — Self-Review

### What works
- **Contribution summary.** Each of the four contributions is reflected.
- **Explicit limitations.** Not buried in hedging language.
- **Future work directions.** Specific and actionable (multi-hop entailment, multi-modal CPS, deployment studies).

### What needs revision
- **The Conclusion is slightly generic in its first two sentences.** "We identified a structural gap... To address this gap, we proposed..." follows a template pattern. **Fix:** Rephrase the opening sentence to be more specific to what ProvGuard-RAG uniquely does.
- **Missing connection to MDPI AI scope.** The Conclusion does not explicitly state why this work matters for the trustworthy AI community. **Fix:** Add one sentence.

### Revision actions
1. Rephrase opening for specificity
2. Add MDPI AI scope connection

---

## Section: Abstract — Self-Review

### What works
- **Structure:** Problem (2 sentences) → Approach (2 sentences) → Method specification (2 sentences) → Significance (1 sentence). ~190 words, within the 200-word target.
- **Concrete details.** Names Qwen2.5-7B, specifies the four-property decomposition, mentions the seven-axis evaluation protocol.
- **Honest about experiment status.** "with empirical evaluation planned as subsequent work" — does not claim results.

### What needs revision
- **The abstract may be slightly dense.** Seven technical concepts (provenance metadata, semantic entailment, ledger-anchored manifest, Merkle log, answer correctness, evidence faithfulness, provenance traceability, audit verifiability) appear in ~190 words. **Fix:** Consider whether all seven evaluation axes need to be named in the abstract or whether "a multi-axis evaluation protocol" suffices.

### Revision actions
1. Reduce concept density if possible without losing specificity
2. Update after full manuscript is stable

---

## Cross-Section Consistency Check

| Element | §1 (Intro) | §2 (Related) | §3 (Method) | §4 (Experiments) | §5 (Discussion) | §6 (Conclusion) |
|---------|-----------|-------------|-------------|-------------------|-----------------|-----------------|
| Four-property decomposition | Introduced as C1 | N/A | Formally defined (§3.1) | Mapped to 7 metrics | Mapped back in failure analysis | Summarized |
| ProvGuard-RAG stages | Listed in P5 | N/A | Detailed in §3.2 | Ablated in §4.3 | N/A | Summarized |
| C1–C4 contributions | Listed | N/A | C2 in §3.2 | C3 in §4.4, C4 in §4.2 | N/A | Reflected |
| Qwen2.5-7B | Not mentioned | N/A | §3.2 Stage 3 | §4.3 | N/A | Not mentioned |
| "Planned" status | Implicit in C4 | N/A | N/A | Explicit disclaimer | Explicit in §5.4 | Implicit in abstract |

**Issue:** Qwen2.5-7B is not mentioned in Introduction or Conclusion. Should be mentioned in Introduction (as part of C4 specification) or removed from Introduction and kept only in Method/Experiments.

---

## Revision Priority Ranking

1. **BLOCKING:** Add explicit assumptions paragraph to §3.1
2. **BLOCKING:** Specify poisoning attack parameters in §4
3. **HIGH:** Add 15+ more citations (target: 35 total)
4. **HIGH:** Add annotation methodology for RQ2 ground truth
5. **HIGH:** Trim Introduction P1 sector list or add scope-narrowing
6. **MEDIUM:** Add MDPI AI venue signal in Introduction and Conclusion
7. **MEDIUM:** Map failure modes to four-property decomposition in Discussion
8. **MEDIUM:** Add domain-specific RAG citations for generalizability claim
9. **LOW:** Generate architecture figure
10. **LOW:** Run check_ai_patterns.py and check_quality.py
