# Introduction Drafting Record

## Scope

Drafted the LaTeX Introduction for:

**ProvGuard-RAG: Ledger-Anchored Provenance and Semantic Verification for Trustworthy Retrieval-Augmented LLMs in Cyber-Physical Incident Intelligence**

Target: MDPI AI Special Issue on trustworthy AI, LLMs, blockchain, data-centric intelligence, and secure smart environments.

## Data-Science-Paper Guidance Applied

- Used the Introduction section structure from `references/introduction.md`.
- Used `references/writing-standards.md` for claim-evidence discipline, LaTeX conventions, and contribution formatting.
- Used `references/ai-patterns.md` to avoid generic opening, literature-tour structure, unsupported deployment claims, and broad hype.

## Central Argument

Standard RAG is useful for cyber--physical incident intelligence, but it is insufficient unless retrieval relevance is joined with source provenance, semantic claim support, and post-hoc auditability.

## Critical Self-Review

The current Introduction is aligned with the central argument and avoids claiming completed experiments. It frames blockchain narrowly as ledger or Merkle-log anchoring for audit manifests, not as a general-purpose decentralization solution. The contribution list is specific enough for a planning-stage manuscript and does not report unsupported numerical results.

The main weakness is that the application setting remains broader than a final submission should allow. The text refers to cyber--physical incident intelligence across industrial IoT, smart cities, transportation, healthcare, and energy, but the empirical section will likely need to narrow this to one or two public CPS/IoT cybersecurity datasets. The Introduction should be revised once the exact benchmark tasks are fixed.

A second weakness is citation coverage. The current citations are verified and relevant, but the final paper still needs dataset and cybersecurity incident-response references. It also needs direct references on RAG security, retrieval poisoning, and prompt injection once those papers are verified.

A third weakness is that the manuscript template still contains placeholder material outside the Introduction. The Introduction itself avoids placeholder claims, but the full `main.tex` is not yet submission-clean.

## Revision Plan

1. Add verified citations for the selected CPS/IoT datasets, likely TON_IoT and CICIoT2023 if those become the main benchmarks.
2. Add verified RAG-security citations on retrieval poisoning, prompt injection, and adversarial context injection.
3. Replace the planning-stage contribution item about a reproducible experimental plan with an empirical contribution only after real experiments are completed.
4. Align the roadmap with the final section structure after the Method and Experiments sections are drafted.
5. Remove or replace all remaining template placeholder text in `main.tex` before any manuscript-level quality check.

