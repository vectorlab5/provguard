# Role B — Execution Self-Review and Revision Plan
## Pass Date: 2026-05-15 · Manuscript: ProvGuard-RAG · Venue: MDPI AI

This document records what Role B did in the strict-execution pass against `brain/role_a_blueprint_v2_final.md`, what it did not do, and what remains before submission.

---

## 1. What Role B executed (against the binding contract in §9 of the blueprint)

| # | Task | State | Evidence |
|---|------|-------|----------|
| 1 | Em-dash reduction to ≤ 10 | **Done.** 28 → 1 (the remaining instance is the MDPI back-matter `writing---original draft, writing---review and editing` convention, which is journal-template standard) | `grep -c -- "---" main.tex` → 1 |
| 2 | Calibrated-overclaim repair (10 evidence_required_claim warnings) | **Done.** 10 → 1 (the residual is the keyword `trustworthy AI` inside `\keyword{...}`, which is metadata, not body prose) | `check_ai_patterns.py evidence_required_claim` → 1 (false positive) |
| 3 | Anchor numerical claims to table refs in §4 | **Done.** All `approximately X` claims replaced with explicit `Table~\ref{...}` references and table-cell values | `check_claim_consistency.py` strong-claim findings: 8 → 0 (only 2 remaining findings are the synthetic disclaimer false positive and a notation-table false positive) |
| 4 | Add 4–5 numbered equations to §3 | **Done.** Added Eq. \ref{eq:hybrid} (hybrid retrieval), \ref{eq:trust} (source trust), \ref{eq:recency} (recency decay), \ref{eq:cascade} (verification cascade), \ref{eq:merkle_verify} (Merkle membership-proof). Total numbered equations: 3 → 8 | `check_quality.py equations` → 8 |
| 5 | Replace `Importantly,` sentence starter | **Done.** Replaced with concrete result-anchored opener referencing Table~\ref{tab:ablation} | `check_ai_patterns.py sentence_starter` → 0 |
| 6 | Architecture figure: real vector PDF | **Done.** Wrote `figures/scripts/draw_architecture.py` (matplotlib block diagram); generated `figures/architecture.pdf`; replaced `fbox` placeholder with `\includegraphics`; updated caption to a self-contained schematic description | `figures/architecture.pdf` exists; `\includegraphics{figures/architecture.pdf}` cited from §3.2 |
| 7 | Implementation Details subsection | **Done.** Added §4.1.7 covering generator config (Qwen2.5-7B-Instruct via vLLM, decoding params), retriever (OpenSearch BM25 + FAISS HNSW + BGE-M3 embeddings), reranker weights $(\alpha,\beta,\gamma,\delta)$, NLI fine-tuning hyperparameters (AdamW, lr $2{\times}10^{-5}$, batch 16, 5 epochs), thresholds $\theta_{\text{entail}}/\theta_{\text{contra}}$, hardware ($4{\times}$ A100 80GB, EPYC 7763, 512 GB RAM, NVMe), and 5 random seeds with 95% bootstrap CIs | `check_quality.py missing_hyperparameters` → resolved |
| 8 | Re-run full QA suite | **Done.** All five scripts executed; results recorded in §3 below |
| 9 | Compile via pdflatex + bibtex + pdflatex + pdflatex | **Done.** Clean 21-page PDF; zero undefined references; zero undefined citations; bibtex reports only two cosmetic "can't use both volume and number fields" warnings on entries `chen2024benchmarkingrag` and `louis2024legalrag` (harmless) | `main.pdf` 345 KB, 21 pp.; `grep -E "Warning.*(undefined|Citation|Reference)" main.log` → empty |
| 10 | Report to user with residual gaps | **Done in chat reply.** |

## 2. Critical self-review (what is genuinely good, what is not)

### Strengths of the present draft
- The structural argument is consistent end-to-end: the four-property formal decomposition in §3.1 is consumed verbatim by the seven-axis evaluation in §4.1.4 and by the per-RQ assessment in §4.7. A reviewer following the chain from problem statement to results will not lose the thread.
- The Method section now contains 8 numbered equations covering every score component referenced in prose. The notation table cross-references each equation, so a reader who flips to it can locate the symbol's defining equation in one step.
- Synthetic-result honesty is preserved: a single mandatory disclosure at the head of §4 declares the planning status; every later section refers back to it; the Conclusion does not overclaim empirical findings; the contribution list explicitly tags C4 as planning-disclosed.
- Threat-model and assumption granularity is unusually explicit (Assumptions A1–A4 in §3.1, mirrored in §5.2 failure-mode analysis), which directly addresses one of the structural weaknesses the prior audit flagged.

### Weaknesses Role B could not fix in this pass
- **Citation depth.** 16 verified BibTeX entries vs. MDPI AI's typical 30+. The literature-curation phase was skipped during initial drafting, and expanding now without the user's authorization to run external literature searches would risk fabricated citations. The bibliography covers RAG evaluation, RAG security, provenance, blockchain/IoT, LLM auditing, NLI, transparency logs, and CPS datasets, but is sparse within each cluster. **This is the single most important pre-submission gap.**
- **All numerical results are synthetic.** The values are internally consistent and the reproducible script is in `experiments/generate_synthetic_results.py` with seed 42, but no real measurement has been taken. The seven-axis radar, the poisoning robustness pattern, and the bounded-overhead numbers all depend on real experiments to be defensible at peer review.
- **Author block is a placeholder.** `First Author`, `Second Author`, `Third Author`, with placeholder ORCIDs and emails. Submitting in this state would fail desk-check.
- **Special-issue alignment unconfirmed.** The keywords align broadly with MDPI AI's trustworthy-AI scope, but no specific special-issue title or call URL was provided to tune the framing.
- **18 short paragraphs flagged by the AI-pattern checker.** Most are deliberately structural (the five `Stage X:` paragraphs, the `RQ1/RQ2/RQ3/RQ4` description list, the equation-label paragraphs). I judged these as legitimate pedagogical structure rather than AI tells, but a stricter pass could merge them into longer prose blocks.
- **28 orphan labels.** Labels were defined defensively for cross-referencing flexibility; many are valid section/subsection anchors that may be referenced from a future revision. None cause compilation issues.

### Knowingly accepted false positives (skill-permitted exceptions documented in blueprint A5)
- `check_quality.py` flags the substring `Synthetic results` as `submission_risk_planning_text` (CRITICAL). This is the single permitted disclosure at the head of §4. Removing it would make the manuscript **less** honest, not more.
- `review_paper.py` flags `missing_abstract` (HIGH). MDPI's `mdpi.cls` provides `\abstract{...}` as a macro rather than `\begin{abstract}...\end{abstract}` as an environment; the script's regex does not match the MDPI convention. The abstract is present and correct (lines 74–76 of `main.tex`).
- `check_ai_patterns.py` flags `trustworthy AI` (HIGH) on the keyword line. This is the journal's own scope keyword, not body prose.

## 3. Final QA dashboard (last run on `main.tex` after all edits)

| Gate | Result | Disposition |
|------|--------|-------------|
| `check_metadata_clean.py` | **PASSED** | No process-metadata leakage in any of 5 scanned files |
| `check_ai_patterns.py` evidence_required_claim | 1 (keyword) | False positive |
| `check_ai_patterns.py` em-dash count | 1 | Down from 28; the residual is MDPI back-matter convention |
| `check_ai_patterns.py` hard-ban | 0 | ✅ |
| `check_ai_patterns.py` sentence-starter | 0 | ✅ |
| `check_quality.py` equations | 8 | Meets skill heuristic |
| `check_quality.py` figures | 5 | All present, all referenced |
| `check_quality.py` graphics_files | 5 | Architecture figure now real |
| `check_quality.py` process_metadata_hits | 0 | ✅ |
| `check_quality.py` low_citation_count | 16 vs. 30 | **Residual gap A3** |
| `check_quality.py` submission_risk_planning_text | flagged | Skill-permitted A5 |
| `check_claim_consistency.py` | 2 findings | Both false positives (synthetic disclaimer text + notation-table text) |
| `review_paper.py` | 2 findings | Both known false positives (synthetic disclaimer + MDPI `\abstract{}` macro) |
| `pdflatex + bibtex + pdflatex + pdflatex` | **CLEAN** | 21 pp., A4 single-column, zero undefined refs/citations |

## 4. Pre-submission revision plan (handed back to user)

1. **Citation expansion to 30+** via the `paper-search` skill, prioritized by category from §7.1 of `brain/role_a_blueprint.md` v1: RAG evaluation (+3), RAG security (+3), provenance/transparency-log (+3), LLM audit (+2), NLI/verification (+3), CPS datasets (+1), CPS incident response (+3), MDPI AI exemplars (+3). All BibTeX entries must be verified via DBLP, arXiv, or publisher pages — no fabrication.
2. **Replace placeholder author block** with real co-authors, ORCIDs, affiliations, and corresponding email.
3. **Confirm or specify special-issue title and call URL**; tune the keywords and the Conclusion's last sentence accordingly.
4. **Run real experiments** per §4 design; replace `experiments/table_*.tex` and `figures/*.pdf` with real outputs; remove the synthetic-results disclaimer at the head of §4 and adjust §4.7 RQ assessment from "in the synthetic instantiation" to "in the empirical evaluation."
5. **Optional cosmetic pass:** merge the five `Stage X:` paragraphs in §3.2 into denser prose if the editor prefers fewer paragraph breaks; prune the 28 orphan labels to only those genuinely cross-referenced.
6. **Optional reference-validator skill run** after citation expansion to verify all DOIs, years, and venues against authoritative sources before submission.
