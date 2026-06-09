#!/usr/bin/env python3
"""Figure: equivalent spatial, modal, and response models for forced response."""

from __future__ import annotations

from plot_helpers import FILL, NAVY, OUT, configure_matplotlib_cache


configure_matplotlib_cache()
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle


fig, ax = plt.subplots(figsize=(9.6, 4.8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis("off")


def box(x, y, w, h, title, body):
    ax.add_patch(Rectangle((x, y), w, h, facecolor=FILL, edgecolor=NAVY, linewidth=1.8))
    ax.text(x + w / 2, y + h - 0.35, title, ha="center", va="center", color=NAVY, fontsize=12, fontweight="bold")
    ax.text(x + w / 2, y + h / 2 - 0.12, body, ha="center", va="center", fontsize=10)


def arrow(start, end, label):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=14, linewidth=1.6, color=NAVY))
    ax.text((start[0] + end[0]) / 2, (start[1] + end[1]) / 2 + 0.18, label, ha="center", fontsize=8.5)


box(0.45, 3.45, 2.25, 1.25, "Spatial model", r"$M,\ K$")
box(3.9, 3.45, 2.20, 1.25, "Modal model", r"$\Lambda,\ \Phi$")
box(7.3, 3.45, 2.25, 1.25, "Response model", r"$\alpha(\omega)$")

box(3.85, 0.75, 2.55, 1.2, "Forced response", r"$X_0=\alpha(\omega)F_0$")

arrow((2.7, 4.08), (3.9, 4.08), "EVP")
arrow((6.1, 4.08), (7.3, 4.08), "modal sum")
arrow((1.55, 3.45), (4.35, 1.95), "physical equations")
arrow((5.0, 3.45), (5.0, 1.95), "modal equations")
arrow((8.42, 3.45), (6.05, 1.95), "FRF matrix")

ax.text(5, 5.55, "Equivalent Models for Harmonic Response", ha="center", color=NAVY, fontsize=14, fontweight="bold")
ax.text(5, 0.25, "Any one model can be used to compute harmonic steady-state response.", ha="center", fontsize=11, color="#333333")

fig.savefig(OUT / "lecture7_model_representations.png", dpi=180, bbox_inches="tight")
plt.close(fig)
