#!/usr/bin/env python3
"""Figure: two-degree-of-freedom undamped mass-spring system."""

from __future__ import annotations

from plot_helpers import NAVY, OUT, configure_matplotlib_cache


configure_matplotlib_cache()
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def spring(ax, x0, x1, y, amp=0.12, turns=6):
    xs = [x0, x0 + 0.18]
    ys = [y, y]
    pitch = (x1 - x0 - 0.36) / (turns * 2)
    x = x0 + 0.18
    sign = 1
    for _ in range(turns * 2):
        x += pitch
        xs.append(x)
        ys.append(y + sign * amp)
        sign *= -1
    xs += [x1 - 0.18, x1]
    ys += [y, y]
    ax.plot(xs, ys, color=NAVY, linewidth=2.0)


fig, ax = plt.subplots(figsize=(8.0, 3.2))
ax.set_xlim(0, 10)
ax.set_ylim(0, 4)
ax.axis("off")

ax.add_patch(Rectangle((0.35, 1.0), 0.22, 2.0, facecolor="#d9dfe8", edgecolor=NAVY, linewidth=2.0))
spring(ax, 0.57, 2.55, 2.0)
ax.text(1.55, 2.38, r"$k_1$", fontsize=14)

ax.add_patch(Rectangle((2.55, 1.55), 1.05, 0.9, facecolor="#eef4fb", edgecolor=NAVY, linewidth=2.2))
ax.text(3.08, 2.0, r"$m_1$", ha="center", va="center", fontsize=16)
spring(ax, 3.6, 6.35, 2.0)
ax.text(4.95, 2.38, r"$k_2$", fontsize=14)

ax.add_patch(Rectangle((6.35, 1.55), 1.05, 0.9, facecolor="#eef4fb", edgecolor=NAVY, linewidth=2.2))
ax.text(6.88, 2.0, r"$m_2$", ha="center", va="center", fontsize=16)
spring(ax, 7.4, 9.3, 2.0)
ax.text(8.35, 2.38, r"$k_3$", fontsize=14)
ax.add_patch(Rectangle((9.3, 1.0), 0.22, 2.0, facecolor="#d9dfe8", edgecolor=NAVY, linewidth=2.0))

ax.annotate(r"$x_1(t)$", xy=(3.08, 2.8), xytext=(3.08, 3.45), ha="center", fontsize=13, arrowprops=dict(arrowstyle="->", color=NAVY, linewidth=1.6))
ax.annotate(r"$x_2(t)$", xy=(6.88, 2.8), xytext=(6.88, 3.45), ha="center", fontsize=13, arrowprops=dict(arrowstyle="->", color=NAVY, linewidth=1.6))
ax.text(5, 0.45, "free vibration: no continuing external force", ha="center", fontsize=11, color="#333333")

fig.savefig(OUT / "lecture6_2dof_system.png", bbox_inches="tight", dpi=180)
plt.close(fig)
