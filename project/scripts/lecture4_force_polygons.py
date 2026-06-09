#!/usr/bin/env python3
"""Figure: force-vector polygon closure for damped SDOF forced vibration."""

from __future__ import annotations

from plot_helpers import NAVY, OUT, RED, configure_matplotlib_cache


configure_matplotlib_cache()
import matplotlib.pyplot as plt


def draw_segment(ax, start, vec, label, color):
    x0, y0 = start
    dx, dy = vec
    ax.annotate("", xy=(x0 + dx, y0 + dy), xytext=(x0, y0), arrowprops=dict(arrowstyle="->", color=color, linewidth=2.2))
    ax.text(x0 + 0.55 * dx, y0 + 0.55 * dy, label, color=color, fontsize=11, ha="center", va="center")
    return (x0 + dx, y0 + dy)


fig, axes = plt.subplots(1, 2, figsize=(8.2, 3.7))

for ax, title in zip(axes, [r"Low frequency: $\Omega\ll\omega_n$", r"At resonance: $\Omega=\omega_n$"]):
    ax.set_title(title, color=NAVY, fontweight="bold")
    ax.axhline(0, color="#dddddd", linewidth=0.8)
    ax.axvline(0, color="#dddddd", linewidth=0.8)
    ax.set_aspect("equal")
    ax.set_xlim(-0.4, 2.3)
    ax.set_ylim(-1.05, 1.05)
    ax.axis("off")

p = (0.15, -0.65)
p = draw_segment(axes[0], p, (0.62, 0.92), r"$\bar{F}$", RED)
p = draw_segment(axes[0], p, (0.55, -0.15), r"$-k\bar{x}$", "#7b1fa2")
p = draw_segment(axes[0], p, (-0.34, -0.45), r"$-c\dot{\bar{x}}$", "#7b1fa2")
p = draw_segment(axes[0], p, (-0.83, -0.32), r"$-m\ddot{\bar{x}}$", "#7b1fa2")
axes[0].text(1.15, -0.88, "closed polygon: dynamic equilibrium", fontsize=9, color="#333333", ha="center")

p = (0.55, -0.65)
p = draw_segment(axes[1], p, (0.54, 0.54), r"$\bar{F}$", RED)
p = draw_segment(axes[1], p, (-0.54, 0.54), r"$-k\bar{x}$", "#7b1fa2")
p = draw_segment(axes[1], p, (-0.54, -0.54), r"$-c\dot{\bar{x}}$", "#7b1fa2")
p = draw_segment(axes[1], p, (0.54, -0.54), r"$-m\ddot{\bar{x}}$", "#7b1fa2")
axes[1].text(1.15, -0.88, "spring and inertia balance;\ndamping balances force", fontsize=9, color="#333333", ha="center")

fig.suptitle("Force Polygon Closure", color=NAVY, fontweight="bold")
fig.tight_layout()
fig.savefig(OUT / "lecture4_force_polygons.png", dpi=180)
plt.close(fig)
