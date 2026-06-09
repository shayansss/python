#!/usr/bin/env python3
"""Figure: forced SDOF model and free-body diagram."""

from __future__ import annotations

from plot_helpers import NAVY, RED, configure_matplotlib_cache


configure_matplotlib_cache()
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def draw_ground(ax, x0, x1, y):
    ax.plot([x0, x1], [y, y], color=NAVY, linewidth=2.2)
    for i in range(6):
        x = x0 + (x1 - x0) * i / 5
        ax.plot([x, x - 0.10], [y, y - 0.15], color=NAVY, linewidth=1.0)


def draw_vertical_spring(ax, x, y_top, y_bottom, width=0.22, turns=6):
    xs = [x, x]
    ys = [y_top, y_top - 0.14]
    coil_top = y_top - 0.14
    coil_bottom = y_bottom + 0.10
    for i in range(turns * 2 + 1):
        ys.append(coil_top - (i + 1) * (coil_top - coil_bottom) / (turns * 2 + 2))
        xs.append(x + width * (-1 if i % 2 == 0 else 1))
    xs.extend([x, x])
    ys.extend([coil_bottom, y_bottom])
    ax.plot(xs, ys, color=NAVY, linewidth=2.0)


fig, ax = plt.subplots(figsize=(7.6, 3.2))
ax.set_xlim(0, 10)
ax.set_ylim(0, 4.2)
ax.axis("off")

# Physical model measured from static equilibrium.
ax.add_patch(Rectangle((1.15, 2.15), 1.35, 0.62, facecolor="#eef4fb", edgecolor=NAVY, linewidth=2.0))
ax.text(1.83, 2.46, r"$m$", ha="center", va="center", fontsize=17)
draw_vertical_spring(ax, 1.83, 2.15, 0.85)
draw_ground(ax, 1.10, 2.60, 0.82)

ax.annotate("", xy=(1.83, 3.42), xytext=(1.83, 2.78), arrowprops=dict(arrowstyle="->", color=RED, linewidth=1.8))
ax.text(1.97, 3.28, r"$F(t)$", color=RED, fontsize=14, va="center")
ax.annotate("", xy=(1.02, 2.15), xytext=(1.02, 2.75), arrowprops=dict(arrowstyle="->", color=RED, linewidth=1.6))
ax.text(0.82, 2.45, r"$x$", color=RED, fontsize=14, ha="center", va="center")
ax.plot([0.70, 3.20], [2.96, 2.96], color=RED, linewidth=1.2)
ax.text(2.62, 2.82, "static equilibrium position", color=RED, fontsize=12, va="center")
ax.text(1.80, 0.34, "forced model", ha="center", fontsize=12, color="#333333")

# Free-body diagram.
ax.add_patch(Rectangle((6.05, 2.05), 1.35, 0.62, facecolor="#eef4fb", edgecolor=NAVY, linewidth=2.0))
ax.text(6.72, 2.36, r"$m$", ha="center", va="center", fontsize=17)
ax.annotate("", xy=(6.72, 3.43), xytext=(6.72, 2.68), arrowprops=dict(arrowstyle="->", color=RED, linewidth=1.8))
ax.text(6.88, 3.30, r"$F(t)$", color=RED, fontsize=14, va="center")
ax.annotate("", xy=(6.72, 1.32), xytext=(6.72, 2.05), arrowprops=dict(arrowstyle="->", color=RED, linewidth=1.8))
ax.text(6.92, 1.52, r"$kx$", color=RED, fontsize=14, va="center")
ax.annotate("", xy=(7.75, 2.90), xytext=(7.75, 2.25), arrowprops=dict(arrowstyle="->", color=RED, linewidth=1.6))
ax.text(7.93, 2.63, r"$\ddot{x}$", color=RED, fontsize=14, va="center")
ax.text(6.72, 0.34, "free-body diagram", ha="center", fontsize=12, color="#333333")

ax.text(5.0, 3.82, r"Newton's law:  $m\ddot{x}=F(t)-kx$", ha="center", fontsize=14, color=NAVY)
ax.text(5.0, 0.82, r"$m\ddot{x}+kx=F(t)$", ha="center", fontsize=15, color=NAVY)

fig.tight_layout(pad=0.4)
fig.savefig("scripts/lecture3_forced_fbd.png", dpi=180)
plt.close(fig)
