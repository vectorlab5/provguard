"""
Generate the ProvGuard-RAG architecture figure (Figure 1) as a vector PDF.
Five-stage block diagram with annotated data flow and external transparency log.

Output: figures/architecture.pdf
"""
import os
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.lines import Line2D

OUT = os.path.join(os.path.dirname(__file__), "..", "architecture.pdf")

# Color palette: muted, print-friendly
COLOR_STD = "#E6EEF6"   # standard RAG components
COLOR_NEW = "#FCE4D6"   # ProvGuard-RAG additions
COLOR_LOG = "#E2D9F3"   # external log
COLOR_EDGE = "#1F2A44"
COLOR_TXT = "#1F2A44"

fig, ax = plt.subplots(figsize=(9.5, 4.6))
ax.set_xlim(0, 100)
ax.set_ylim(0, 50)
ax.axis("off")


def block(x, y, w, h, text, color, lw=1.2):
    box = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.4,rounding_size=1.2",
        linewidth=lw,
        edgecolor=COLOR_EDGE,
        facecolor=color,
    )
    ax.add_patch(box)
    ax.text(x + w / 2, y + h / 2, text,
            ha="center", va="center",
            fontsize=9, color=COLOR_TXT, wrap=True)


def arrow(x1, y1, x2, y2, label=None, label_offset=(0, 1.5)):
    a = FancyArrowPatch((x1, y1), (x2, y2),
                        arrowstyle="-|>", mutation_scale=12,
                        linewidth=1.0, color=COLOR_EDGE)
    ax.add_patch(a)
    if label:
        ax.text((x1 + x2) / 2 + label_offset[0],
                (y1 + y2) / 2 + label_offset[1],
                label, ha="center", va="center",
                fontsize=7.5, color=COLOR_TXT, style="italic")


# Layout: two-row pipeline with stages 1-2-3 on top, 4-5 on bottom
# Stage 1: Evidence Registration
block(2, 32, 16, 12,
      "Stage 1\nEvidence\nRegistration\n$(\\mathrm{src},\\tau,h)$",
      COLOR_NEW)

# Stage 2: Hybrid Retrieval + Provenance Reranking
block(22, 32, 18, 12,
      "Stage 2\nHybrid Retrieval +\nProvenance Reranker",
      COLOR_NEW)

# Stage 3: LLM Generation + Claim Decomposition
block(44, 32, 18, 12,
      "Stage 3\nLLM Generation +\nClaim Decomposition",
      COLOR_STD)

# Stage 4: Semantic Claim Verification
block(44, 10, 18, 12,
      "Stage 4\nSemantic Claim\nVerification (NLI)",
      COLOR_NEW)

# Stage 5: Audit Manifest + Ledger Anchoring
block(22, 10, 18, 12,
      "Stage 5\nAudit Manifest\nConstruction",
      COLOR_NEW)

# External transparency log
block(66, 10, 18, 12,
      "Transparency Log $\\mathcal{L}$\n(append-only,\nMerkle tree)",
      COLOR_LOG)

# Arrows: top row left-to-right
arrow(18, 38, 22, 38, "evidence index")
arrow(40, 38, 44, 38, "$\\mathcal{R}_q$")

# Stage 3 -> Stage 4 (down)
arrow(53, 32, 53, 22, "claims $A$")

# Stage 4 -> Stage 5 (left)
arrow(44, 16, 40, 16, "labels $v$")

# Stage 5 -> Log (right)
arrow(40, 16, 66, 16, "$h_M$ append")

# Output arrow from Stage 4
arrow(62, 16, 78, 5, "answer + manifest")

# Legend
ax.add_patch(FancyBboxPatch((2, 2), 4, 3.5,
                            boxstyle="round,pad=0.2,rounding_size=0.5",
                            linewidth=0.8, edgecolor=COLOR_EDGE,
                            facecolor=COLOR_NEW))
ax.text(7, 3.75, "ProvGuard-RAG addition", fontsize=8, va="center")

ax.add_patch(FancyBboxPatch((28, 2), 4, 3.5,
                            boxstyle="round,pad=0.2,rounding_size=0.5",
                            linewidth=0.8, edgecolor=COLOR_EDGE,
                            facecolor=COLOR_STD))
ax.text(33, 3.75, "Standard RAG component", fontsize=8, va="center")

ax.add_patch(FancyBboxPatch((54, 2), 4, 3.5,
                            boxstyle="round,pad=0.2,rounding_size=0.5",
                            linewidth=0.8, edgecolor=COLOR_EDGE,
                            facecolor=COLOR_LOG))
ax.text(59, 3.75, "External transparency log", fontsize=8, va="center")

# Query input on the left, output on the right (annotations)
ax.text(0.5, 38, "query $q$",
        fontsize=9, ha="left", va="center", color=COLOR_TXT)
arrow(0.5, 36.5, 2, 36.5)

ax.text(94, 5, "answer $a$\n+ manifest $M_q$",
        fontsize=8.5, ha="left", va="center", color=COLOR_TXT)

plt.tight_layout()
plt.savefig(OUT, format="pdf", bbox_inches="tight")
print(f"Wrote {OUT}")
