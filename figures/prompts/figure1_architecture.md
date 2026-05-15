# Figure 1 Generation Prompt — ProvGuard-RAG Architecture

Target: `figures/architecture.pdf` (Figure~\ref{fig:architecture}, §3.2 of `main.tex`)
Skill: `data-science-paper/references/figure-generation-prompts.md`
Template: Type 1 (Method Overview / Pipeline) with one external system block (transparency log)
Generator: Google Gemini image generation (or Imagen / DALL·E with the same prompt)
Reviewer question this figure must answer: *"How does ProvGuard-RAG attach provenance, claim verification, and tamper-evident audit logging to a standard RAG query, and which components are new versus borrowed?"*

---

## Pre-flight checklist (per skill §"Visual Richness Rules")

- [x] Data representations at input (user query text snippet) and output (answer + manifest + inclusion proof)
- [x] At least 2–3 feature-map / data visualizations between stages (candidate-set ranking bars, claim list, manifest tuple, Merkle tree)
- [x] At least 2–3 mathematical/operation symbols on connections (∑ in reranker, σ on verification gate, H(·) on hashing edges, ⊕ at manifest construction)
- [x] Novel component (provenance reranker + claim verifier + ledger anchor) gets accent color and most internal detail
- [x] Dimension/cardinality annotations: `|R_q^cand|=N_cand`, `|R_q|=k`, `|A|=K`, `|L|=N`
- [x] Color palette: Cool Academic (palette A) — gray for standard, light orange for novel, light purple for external log

---

## COPY-PASTE-READY PROMPT (paste into Gemini / Imagen)

```
You are a technical diagram creator for peer-reviewed scientific papers (MDPI AI / TPAMI level).

## TASK
Create a detailed method overview figure for the paper
"ProvGuard-RAG: Ledger-Anchored Provenance and Semantic Verification for
Trustworthy Retrieval-Augmented LLMs in Cyber-Physical Incident Intelligence."

The figure shows a five-stage retrieval-augmented-generation pipeline plus an external
append-only Merkle transparency log. Four of the five stages are novel additions to a
standard RAG pipeline; one stage (LLM generation) is a borrowed standard component.

## ARCHITECTURE
Pipeline (left to right, horizontal flow):
  [Query q] -> [Stage 1: Evidence Registration]
            -> [Stage 2: Hybrid Retrieval + Provenance-Aware Reranker]
            -> [Stage 3: LLM Generation + Claim Decomposition]
            -> [Stage 4: Semantic Claim Verification (NLI)]
            -> [Stage 5: Audit Manifest + Ledger Anchoring]
            -> [Output: answer a + manifest M_q + audit path]

External system (drawn ABOVE Stage 5, connected by an upward arrow labelled "append h_M"):
  [Transparency Log L]: append-only Merkle tree, returns log position pi(h_M),
  audit path ap(h_M), and current root r'.

Off-pipeline input (drawn ABOVE Stage 1, connected by a downward arrow):
  [Evidence Corpus C]: a small stack of document icons each carrying a provenance tag
  with the four fields (src, tau, parser, h). Stage 1 is OFF the query critical path
  (annotate this with a small "off-line" label).

## DETAILED CONTENT FOR EACH STAGE

INPUT (left edge):
- Show a small text snippet inside a rounded rectangle styled as a chat bubble:
  "q: Was device D17 compromised in the window 14:00 - 14:30?"
- Below it, a tiny clock-icon to suggest temporal scoping.

[Stage 1: Evidence Registration]  (NOVEL, accent color)
- Inside the box, draw 3 small document icons stacked with slight offset.
- Each document carries a small provenance tag below it showing four mini-pills:
  "src", "tau", "parser", "h". Use alternating shades of the neutral color for the pills.
- A small SHA-256 hash icon (open lock with "H" inside) sits next to the tags to
  indicate cryptographic hashing.
- Annotation under the box: "p_i = (src_i, tau_i, parser_i, h_i)".

[Stage 2: Hybrid Retrieval + Provenance-Aware Reranker]  (NOVEL, accent color, LARGEST module)
- Internally split into TWO sub-blocks side by side:
  (a) "Hybrid Retrieval" sub-block:
      - Show a small inverted-index grid (BM25) on top
      - Show a small dense vector grid (BGE-M3 embeddings, 6 colored vertical bars) below
      - Their outputs converge with a "+ lambda" symbol into the candidate set
  (b) "Provenance-Aware Reranker" sub-block:
      - Show four small horizontal bars labelled s_rel, s_trust, s_recency, s_ver
      - Show their weighted sum with a Sigma symbol producing s(d)
      - Equation beside this sub-block (small typeset):
        "s(d) = alpha s_rel + beta s_trust + gamma s_recency + delta s_ver"
- Between (a) and (b), label the intermediate set "R_q^cand  (|.|=N_cand)".
- Output of the box: a TopK selector icon (small bar chart with the top three bars
  highlighted) producing the final evidence set R_q with cardinality k.
- Annotation under the box: "Eqs. (1)-(5)".

[Stage 3: LLM Generation + Claim Decomposition]  (BORROWED, neutral gray color)
- Internally show two stacked sub-blocks:
  (a) "Generator G" (Qwen2.5-7B-Instruct): small block with a transformer-like
      stack of three thin horizontal bars indicating layers
  (b) "Claim Decomposer": small block with a text snippet on the left and three
      bullet-point claims c_1, c_2, c_3 on the right
- Output: a small list "A = {c_1, ..., c_K}" with three example bullets.
- Use the NEUTRAL color to mark this as standard / borrowed.

[Stage 4: Semantic Claim Verification]  (NOVEL, accent color)
- Inside the box show a small entailment matrix: rows are claims c_1, c_2, c_3,
  columns are retrieved evidence d_1, d_2 from R_q. Cells show small
  probability-bar glyphs (warm-to-cool 2-cell bars).
- To the right of the matrix, show three colored chips for the three labels:
  GREEN = supported, RED = unsupported, AMBER = insufficient.
- Place a small sigma symbol on the threshold gate where the chips are decided.
- Annotation under the box: "thresholds theta_entail, theta_contra  (Eq. 6)".

[Stage 5: Audit Manifest + Ledger Anchoring]  (NOVEL, accent color)
- Inside the box show the manifest tuple as a labelled record:
  "M_q = (h_q, {(h_i, src_i, tau_i)}, model_id, prompt_v, {(c_j, v(c_j))}, h_a)"
  Render this as a stacked field list with thin dividers.
- A small ⊕ icon shows the manifest construction step.
- An H(.) box hashes M_q to produce h_M (small hash glyph).
- An upward arrow leaves the box, labelled "append h_M", going to the
  External Transparency Log L drawn ABOVE the pipeline.

[Transparency Log L]  (EXTERNAL, secondary color = light purple)
- Draw a small Merkle tree icon: a triangle made of seven tiny circles
  (4 leaves on bottom, 2 internal, 1 root) connected by thin lines.
- Highlight the leaf where h_M lands (small accent dot).
- Show three labelled outputs returning DOWN to Stage 5: pi(h_M), ap(h_M), r'.
- Annotation beside the log: "append-only Merkle tree (Eq. 7)".

OUTPUT (right edge):
- A small "answer + manifest" envelope icon labelled
  "(a, A, v, M_q, h_M, pi(h_M), ap(h_M))"
- Below it, a tiny magnifying-glass icon and the label "to auditor"
  to indicate the inclusion proof can be re-verified independently.

## CONNECTIONS AND OPERATIONS
- Main flow: solid dark gray arrows left-to-right between Stages 1-2-3-4-5.
- Off-line ingestion: dashed dark gray arrow from "Evidence Corpus C" DOWN to Stage 1.
- Manifest anchoring: solid arrow UP from Stage 5 to Transparency Log L,
  labelled "append h_M" with a small H(.) glyph.
- Audit return: dashed arrow DOWN from Transparency Log L back to Stage 5,
  labelled "(pi, ap, r')".
- Hash flows: thin dashed arrows from each evidence document into the manifest record,
  labelled with H(d_i) symbols.
- Verification gate: a small sigma symbol on the arrow leaving Stage 4.
- Final delivery: solid arrow from Stage 5 to the output envelope on the right.

## COLOR CODING (Palette A, low-saturation)
- Stages 1, 2, 4, 5 (ProvGuard-RAG additions): light orange #FFE0B2 fill,
  dark gray #333333 outline.
- Stage 3 (standard RAG component): light gray #E8E8E8 fill,
  dark gray #333333 outline.
- Transparency Log L (external system): light purple #E8DAEF fill,
  dark gray outline.
- Feature/data tensor sub-blocks (BM25 grid, dense vector bars, attention matrix,
  manifest record): very light blue #D6E4F0 fill.
- Background: pure white #FFFFFF.
- Text: near-black #1A1A1A.

## LAYOUT
- Single horizontal pipeline row, left to right, vertically centered.
- Aspect ratio approximately 3:1 (wide and short, fits MDPI single-column at full width).
- Equal vertical centering of all five stages; Stage 2 is the largest box (it has the
  most internal detail), Stages 1, 3, 4, 5 are slightly smaller and uniform in size.
- Transparency Log L sits ABOVE Stage 5, with a clearly visible up-arrow connection.
- Evidence Corpus C sits ABOVE Stage 1, with a clearly visible down-arrow connection.
- Generous whitespace (at least 15-20% empty space) on all four sides.
- All boxes aligned on a strict invisible grid.
- A small legend in the bottom-left corner with three swatches:
    [orange] ProvGuard-RAG addition
    [gray]   Standard RAG component
    [purple] External transparency log

## CRITICAL STYLE CONSTRAINTS

This figure will appear in a peer-reviewed scientific paper (MDPI AI / TPAMI level).
It must look like a human researcher created it in PowerPoint or Adobe Illustrator.
The figure should be VISUALLY RICH and DETAILED — not just labeled boxes with arrows.

AESTHETIC RULES:
- FLAT 2D layout for all module containers (rectangles, rounded rectangles)
- THIN outlines (0.5-1pt) in dark gray or black
- WHITE or very light gray (#F5F5F5) background for module containers
- MAXIMUM 3 accent colors, all low saturation and high brightness
- CLEAN sans-serif font (Helvetica/Arial), all text 8-11pt and fully legible
- SIMPLE straight arrows with small arrowheads, mathematical symbols on key connections
- All shapes ALIGNED on a clean grid layout
- GENEROUS whitespace between modules

VISUAL RICHNESS RULES:
- Each module box contains VISUAL CONTENT showing what happens inside (mini sub-blocks,
  data representations, small matrices, tuples), not just a text label
- Show data representations at input (the chat-bubble query) and at output
  (the answer + manifest envelope)
- Include cardinality annotations (|R_q^cand|=N_cand, |R_q|=k, |A|=K) on key connections
- Use mathematical symbols (Sigma in reranker, sigma on verification gate, H(.) on hash
  edges, +lambda for hybrid mixing, ⊕ at manifest construction) to show operations
- The novel components (Stages 1, 2, 4, 5) have the most internal detail
- The reranker (Stage 2) is the largest box and shows two parallel sub-blocks plus the
  weighted-sum equation in small typeset

FORBIDDEN:
- NO gradient fills (solid flat colors only)
- NO drop shadows or shadow effects
- NO glow, bloom, light ray, or luminous effects
- NO 3D perspective on module containers
- NO glossy, bubbly, or rounded-pillow shapes
- NO saturated or vivid colors (nothing brighter than HSB saturation 25%)
- NO background patterns or textures
- NO caption or title text inside the figure (the LaTeX caption supplies this)
- NO infographic or poster aesthetic
- NO thick outlines or heavy borders
- NO photorealistic elements or photographs
- NO emoji-style or clip-art icons (use simple monochrome line-art only)
- NO blockchain or coin imagery — the transparency log is a Merkle tree, NOT a
  cryptocurrency

## OUTPUT
- Size: 3200 x 1100 pixels
- Background: pure white
- Format: PNG with transparent background acceptable; PDF preferred if available
- The image should remain legible at 50% zoom
```

---

## Iteration prompts (use only if the first generation falls short)

### If output is too simple (just text boxes with arrows):
> The figure is too simple — it looks like a rough flowchart, not a publication figure. Please add visual content INSIDE Stages 2, 4, and 5: in Stage 2 add the two parallel sub-blocks (BM25 inverted-index grid + dense vector bars) and the four reranker score bars with their Sigma; in Stage 4 add the small claim-by-evidence entailment matrix with three colored chips for supported / unsupported / insufficient; in Stage 5 add the manifest tuple as a stacked field list and the H(.) hash glyph. Add cardinality labels |R_q^cand|=N_cand, |R_q|=k, |A|=K on the connecting arrows. Add a Merkle-tree icon (seven small circles) inside the Transparency Log block.

### If the log looks like cryptocurrency / blockchain art:
> Remove all coin, chain-link, and blockchain imagery. The transparency log is a Merkle tree (a triangle of seven small circles connected by lines), not a cryptocurrency. Use the light purple #E8DAEF fill and a thin dark-gray outline only. No glow, no metallic effects, no chain links.

### If colors are too saturated / too "AI-generated":
> Reduce all color saturation to at most HSB 25%. Replace any vivid orange with #FFE0B2; replace any vivid purple with #E8DAEF; replace any vivid blue with #D6E4F0. All outlines must be a single dark-gray hue #333333. Remove any rainbow gradient or color transition.

### If text is illegible at print scale:
> All text labels must be at least 8pt clean sans-serif (Helvetica or Arial). The four reranker score-component labels (s_rel, s_trust, s_recency, s_ver), the three verification labels (supported / unsupported / insufficient), the manifest field names, and the cardinality annotations must be clearly readable when the image is viewed at 50% zoom.

### If Stage 2 is the same size as the other stages:
> Stage 2 must be the LARGEST box because it contains the most internal sub-blocks (Hybrid Retrieval + Provenance Reranker). Make it about 1.4x the width of Stages 1, 3, 4, 5. The other four stages should be uniform in size.

---

## Post-generation human polish workflow (per skill §"Post-Generation")

1. Open the AI output in PowerPoint, Illustrator, or draw.io as a layout reference.
2. Redraw cleanly using vector tools (the current `figures/architecture.pdf` was generated by `figures/scripts/draw_architecture.py` and may serve as a starting block-layout that you replace with the richer Gemini-derived content).
3. Standardize colors to the four palette hexcodes above.
4. Re-type all text in Helvetica/Arial, no smaller than 8pt.
5. Verify visual content accuracy:
   - reranker equation matches Eq. (5) of `main.tex`,
   - verification labels match the three-way branch in Eq. (6),
   - manifest tuple matches Eq. (3),
   - the Merkle inclusion proof terms match Eq. (7).
6. Export as PDF, save as `figures/architecture.pdf` (replacing the current programmatic placeholder).
7. Print test at 50% zoom — every label and every annotation must remain legible.

## Quality checklist for the final figure (per skill §"Quality Checklist")

Visual richness
- [ ] Input shows the chat-bubble query
- [ ] Stage 2 shows two parallel sub-blocks (BM25 + dense) and four weighted score bars
- [ ] Stage 4 shows the claim-by-evidence entailment matrix and three-color label chips
- [ ] Stage 5 shows the manifest tuple as a labelled record
- [ ] Transparency Log L shows a Merkle-tree icon
- [ ] Mathematical symbols Sigma, sigma, H(.), +lambda, ⊕ appear on the relevant connections
- [ ] Cardinality annotations |R_q^cand|=N_cand, |R_q|=k, |A|=K appear
- [ ] Output envelope shows the full output tuple

Anti-AI aesthetics
- [ ] No gradient fills
- [ ] No drop shadows or glow
- [ ] All colors below HSB saturation 25%
- [ ] At most three accent colors (orange, purple, blue) plus neutral gray
- [ ] All icons are simple monochrome line-art

Technical correctness
- [ ] Stages 1, 2, 4, 5 are accent-colored (additions); Stage 3 is gray (standard)
- [ ] Transparency Log L is purple (external)
- [ ] Off-line ingestion arrow from C to Stage 1 is dashed
- [ ] Audit-return arrow from L to Stage 5 is dashed
- [ ] No "Placeholder:" or "to be generated" text inside the rendered figure
- [ ] Equation numbers in annotations match `main.tex` (Eqs. 1-5 in Stage 2, Eq. 6 in
      Stage 4, Eqs. 3 and 7 around Stage 5)

Publication readiness
- [ ] Renders crisp at 3200x1100 pixels
- [ ] All labels legible at 50% zoom
- [ ] Fits MDPI single-column page width without cropping
- [ ] Style consistent with `figures/main_results.pdf`, `figures/poisoning_robustness.pdf`,
      `figures/radar_evaluation.pdf`, `figures/ablation_waterfall.pdf` (same palette,
      same font family, same outline weight)
