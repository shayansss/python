#!/usr/bin/env python3
"""Figure: viscous dashpot model and linear force-velocity relation."""

from __future__ import annotations

from plot_helpers import NAVY, OUT, RED, configure_matplotlib_cache


configure_matplotlib_cache()
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


fig, (ax_damper, ax_curve) = plt.subplots(1, 2, figsize=(8.0, 3.4))

ax_damper.set_xlim(0, 5)
ax_damper.set_ylim(0, 4)
ax_damper.axis("off")
ax_damper.set_title("Viscous dashpot", color=NAVY, fontweight="bold")
ax_damper.plot([2.5, 2.5], [3.6, 2.85], color=NAVY, linewidth=2.4)
ax_damper.plot([2.5, 2.5], [1.15, 0.4], color=NAVY, linewidth=2.4)
ax_damper.add_patch(Rectangle((1.9, 1.15), 1.2, 1.7, fill=False, edgecolor=NAVY, linewidth=2.4))
ax_damper.plot([2.15, 2.85], [2.0, 2.0], color=NAVY, linewidth=3.2)
ax_damper.plot([2.15, 2.85], [2.45, 2.45], color=NAVY, linewidth=1.5, alpha=0.5)
ax_damper.plot([2.15, 2.85], [1.55, 1.55], color=NAVY, linewidth=1.5, alpha=0.5)
ax_damper.plot(2.5, 3.7, marker="o", color=NAVY, markersize=5)
ax_damper.plot(2.5, 0.3, marker="o", color=NAVY, markersize=5)
ax_damper.text(3.35, 2.0, r"$f_d=c\dot{x}$", fontsize=16, va="center")

ax_curve.set_title("Force proportional to velocity", color=NAVY, fontweight="bold")
ax_curve.spines[["top", "right"]].set_visible(False)
ax_curve.set_xlim(-1.1, 1.1)
ax_curve.set_ylim(-1.1, 1.1)
ax_curve.axhline(0, color="#333333", linewidth=1)
ax_curve.axvline(0, color="#333333", linewidth=1)
ax_curve.plot([-1, 1], [-1, 1], color=NAVY, linewidth=2.5)
ax_curve.text(0.62, 0.78, r"slope $c$", color=RED, fontsize=12)
ax_curve.set_xlabel(r"$\dot{x}$")
ax_curve.set_ylabel(r"$F$")
ax_curve.grid(True, alpha=0.2)

fig.tight_layout()
fig.savefig(OUT / "lecture4_viscous_damping_model.png", dpi=180)
plt.close(fig)
