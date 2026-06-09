#!/usr/bin/env python3
"""Figure: physical-space system compared with modal-space SDOF equations."""

from __future__ import annotations

from plot_helpers import FILL, NAVY, OUT, configure_matplotlib_cache, draw_spring


configure_matplotlib_cache()
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


fig, ax = plt.subplots(figsize=(9.2, 4.7))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis("off")

ax.text(2.4, 5.55, "Physical space", ha="center", color=NAVY, fontsize=15, fontweight="bold")
ax.text(7.4, 5.55, "Modal space", ha="center", color=NAVY, fontsize=15, fontweight="bold")

# Physical 3-DOF chain.
wall_x = 0.45
ax.add_patch(Rectangle((wall_x, 2.1), 0.14, 2.0, facecolor="#d9dfe8", edgecolor=NAVY, linewidth=1.8))
centers = [1.7, 2.95, 4.2]
for i, x in enumerate(centers, start=1):
    ax.add_patch(Rectangle((x - 0.32, 2.55), 0.64, 0.54, facecolor=FILL, edgecolor=NAVY, linewidth=1.7))
    ax.text(x, 2.82, rf"$m_{i}$", ha="center", va="center", fontsize=11)
    ax.annotate(rf"$x_{i}$", xy=(x, 3.25), xytext=(x + 0.32, 3.75), fontsize=10, arrowprops=dict(arrowstyle="->", color=NAVY))
    ax.annotate(rf"$F_{i}$", xy=(x + 0.34, 2.25), xytext=(x + 0.82, 2.25), fontsize=10, arrowprops=dict(arrowstyle="<-", color=NAVY))

draw_spring(ax, wall_x + 0.14, centers[0] - 0.32, 2.82, amp=0.10, turns=5)
draw_spring(ax, centers[0] + 0.32, centers[1] - 0.32, 2.82, amp=0.10, turns=5)
draw_spring(ax, centers[1] + 0.32, centers[2] - 0.32, 2.82, amp=0.10, turns=5)
draw_spring(ax, centers[2] + 0.32, 5.05, 2.82, amp=0.10, turns=5)
ax.add_patch(Rectangle((5.05, 2.1), 0.14, 2.0, facecolor="#d9dfe8", edgecolor=NAVY, linewidth=1.8))
for label, x in zip([r"$k_1$", r"$k_2$", r"$k_3$", r"$k_4$"], [1.05, 2.35, 3.6, 4.72]):
    ax.text(x, 3.08, label, fontsize=10)

ax.text(2.75, 1.35, r"coordinates: $x_1,\ x_2,\ x_3$", ha="center", fontsize=11)
ax.text(2.75, 0.95, "equations are generally coupled", ha="center", fontsize=10, color="#333333")

# Modal systems.
ys = [4.25, 3.05, 1.85]
for idx, y in enumerate(ys, start=1):
    ax.plot([6.15, 8.85], [y, y], color="#d9dfe8", linewidth=1.0)
    ax.add_patch(Rectangle((6.35, y - 0.28), 0.58, 0.56, facecolor=FILL, edgecolor=NAVY, linewidth=1.6))
    ax.text(6.64, y, rf"$m_{{r{idx}}}$", ha="center", va="center", fontsize=10)
    draw_spring(ax, 6.93, 8.15, y, amp=0.08, turns=5)
    ax.add_patch(Rectangle((8.15, y - 0.5), 0.12, 1.0, facecolor="#d9dfe8", edgecolor=NAVY, linewidth=1.5))
    ax.annotate(rf"$f_{{r{idx}}}$", xy=(6.32, y + 0.43), xytext=(5.75, y + 0.43), fontsize=10, arrowprops=dict(arrowstyle="->", color=NAVY))
    ax.text(7.55, y + 0.22, rf"$k_{{r{idx}}}$", fontsize=10)
    ax.text(8.55, y, rf"mode {idx}", fontsize=10, va="center")

ax.text(7.35, 0.95, r"coordinates: $y_1,\ y_2,\ y_3$", ha="center", fontsize=11)
ax.text(7.35, 0.55, "modal equations are uncoupled", ha="center", fontsize=10, color="#333333")

fig.savefig(OUT / "lecture7_physical_modal_space.png", dpi=180, bbox_inches="tight")
plt.close(fig)
