#!/usr/bin/env python3
"""Figure: complex exponential force as a rotating vector."""

from __future__ import annotations

import math

from plot_helpers import NAVY, OUT, configure_matplotlib_cache


configure_matplotlib_cache()
import matplotlib.pyplot as plt


theta = math.radians(38)
F0 = 1.0
x = F0 * math.cos(theta)
y = F0 * math.sin(theta)

fig, ax = plt.subplots(figsize=(5.2, 5.2))
ax.axhline(0, color="#333333", linewidth=1.0)
ax.axvline(0, color="#333333", linewidth=1.0)
ax.annotate("", xy=(x, y), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color=NAVY, linewidth=2.4))
ax.plot([x, x], [0, y], color="#c62828", linestyle="--", linewidth=1.5)
ax.plot([0, x], [y, y], color="#c62828", linestyle="--", linewidth=1.5)
ax.text(x + 0.05, y + 0.04, r"$F_0e^{i\Omega t}$", color=NAVY, fontsize=15)
ax.text(x / 2, -0.10, r"$F_0\cos\Omega t$", color="#c62828", fontsize=13, ha="center")
ax.text(x + 0.05, y / 2, r"$F_0\sin\Omega t$", color="#c62828", fontsize=13, va="center")
arc = plt.matplotlib.patches.Arc((0, 0), 0.55, 0.55, theta1=0, theta2=math.degrees(theta), color="#555555")
ax.add_patch(arc)
ax.text(0.34, 0.10, r"$\Omega t$", fontsize=13)
ax.text(1.12, -0.05, "Re", fontsize=13)
ax.text(0.04, 1.10, "Im", fontsize=13)
ax.set_aspect("equal", adjustable="box")
ax.set_xlim(-0.25, 1.25)
ax.set_ylim(-0.25, 1.25)
ax.set_title("Complex Exponential Force", color=NAVY, fontweight="bold")
ax.axis("off")
fig.tight_layout()
fig.savefig(OUT / "lecture3_complex_force.png", dpi=180)
plt.close(fig)
