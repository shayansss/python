#!/usr/bin/env python3
"""Figure: damped SDOF mass-spring-dashpot model."""

from __future__ import annotations

from plot_helpers import NAVY, OUT, configure_matplotlib_cache


configure_matplotlib_cache()
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


fig, ax = plt.subplots(figsize=(5.0, 4.8))
ax.set_xlim(-1.8, 1.8)
ax.set_ylim(0.0, 4.6)
ax.axis("off")

ax.annotate(r"$x(t)$", xy=(0.0, 4.35), xytext=(0.0, 3.92), ha="center", fontsize=16, arrowprops=dict(arrowstyle="->", color=NAVY, linewidth=1.8))
ax.add_patch(Rectangle((-0.82, 3.05), 1.64, 0.72, facecolor="#eef4fb", edgecolor=NAVY, linewidth=2.4))
ax.text(0.0, 3.41, r"$m$", ha="center", va="center", fontsize=22)

spring_x = -0.42
y_top = 3.05
y_bottom = 0.88
xs = [spring_x, spring_x]
ys = [y_top, y_top - 0.25]
turns = 7
height = y_top - 0.25 - y_bottom
for i in range(turns * 2 + 1):
    ys.append(y_top - 0.25 - (i + 1) * height / (turns * 2 + 2))
    xs.append(spring_x + 0.26 * (-1 if i % 2 == 0 else 1))
xs.append(spring_x)
ys.append(y_bottom)
ax.plot(xs, ys, color=NAVY, linewidth=2.2)
ax.text(-0.95, 1.9, r"$k$", fontsize=18)

damper_x = 0.48
ax.plot([damper_x, damper_x], [3.05, 2.45], color=NAVY, linewidth=2.2)
ax.add_patch(Rectangle((damper_x - 0.32, 1.62), 0.64, 0.86, fill=False, edgecolor=NAVY, linewidth=2.2))
ax.plot([damper_x, damper_x], [1.62, 0.88], color=NAVY, linewidth=2.2)
ax.plot([damper_x - 0.24, damper_x + 0.24], [2.05, 2.05], color=NAVY, linewidth=3.0)
ax.text(0.88, 1.9, r"$c$", fontsize=18)

ax.plot([-1.45, 1.45], [0.82, 0.82], color=NAVY, linewidth=2.4)
for gx in [i / 4 for i in range(-5, 6)]:
    ax.plot([gx, gx - 0.12], [0.82, 0.64], color=NAVY, linewidth=1.1)
ax.text(0.0, 0.35, "static equilibrium reference", ha="center", fontsize=10, color="#333333")

fig.savefig(OUT / "lecture4_damped_sdof_model.png", bbox_inches="tight", dpi=180)
plt.close(fig)
