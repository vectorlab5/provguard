# Related Work Drafting Record

## Scope

Drafted the LaTeX Related Work section for:

**ProvGuard-RAG: Ledger-Anchored Provenance and Semantic Verification for Trustworthy Retrieval-Augmented LLMs in Cyber-Physical Incident Intelligence**

Target: MDPI AI Special Issue on trustworthy AI, LLMs, blockchain, data-centric intelligence, and secure smart environments.

## Data-Science-Paper Guidance Applied

- Used `references/writing-standards.md` for claim-evidence discipline, LaTeX citation style, and paragraph structure.
- Used `references/ai-patterns.md` to avoid generic literature-tour prose, unsupported broad claims, and citation bridges without mapping.
- Used `references/related-work.md` for theme-based organization, differentiation at the end of every theme, and concrete positioning.

## Theme Grouping

1. **Retrieval-Augmented Generation and Evaluation**
   - Citation keys: `chen2024benchmarkingrag`, `wang2023selfknowledge`, `louis2024legalrag`.
   - Role: motivates RAG failure modes, adaptive retrieval, and high-stakes domain-specific reference use.

2. **Data Provenance, Blockchain, and Trustworthy Distributed AI**
   - Citation keys: `werder2022dataprovenance`, `honarpajooh2021iotprovenance`, `yang2023trustworthyfl`, `wu2023bflsurvey`.
   - Role: motivates traceability, tamper-evident provenance records, and the practical limits of blockchain-style trust mechanisms.

3. **LLM Auditing and Application-Level Accountability**
   - Citation key: `mokander2023auditingllms`.
   - Role: motivates application-level audit artifacts for deployed RAG systems.

4. **Positioning of ProvGuard-RAG**
   - Synthesizes the three streams and states what the proposed framework adds: provenance-aware reranking, claim-level semantic verification, ledger-anchored audit manifests, and CPS incident intelligence evaluation.

## Critical Self-Review

The section now uses a theme-based structure instead of paper-by-paper summaries. Each subsection ends with a concrete differentiation from \textsc{ProvGuard-RAG}. The prose avoids reporting experimental performance and does not claim that the proposed system has already been validated.

The main weakness is citation coverage. The section currently relies on the eight verified sources already present in `references.bib`, which is acceptable for this drafting step but too thin for a journal submission. The final Related Work should add verified papers on CPS/IoT intrusion datasets, RAG poisoning or prompt injection, cybersecurity incident response, and semantic claim verification.

A second weakness is that the audit subsection depends primarily on one source. It is conceptually useful but should be expanded with additional verified work on AI audit logs, system accountability, or trustworthy AI governance once the literature curation phase is extended.

## Revision Plan

1. Add verified CPS/IoT security dataset citations once the benchmark is fixed.
2. Add verified RAG security papers on retrieval poisoning, indirect prompt injection, and adversarial context.
3. Add one or two verified semantic verification or entailment-based fact-checking references if semantic claim verification remains a core method component.
4. Consider a compact feature-comparison table after the method is finalized, comparing standard RAG, domain RAG, provenance systems, and \textsc{ProvGuard-RAG} by structural properties rather than performance.
5. Re-run style and citation checks after the placeholder Method and Experiments sections are replaced.

