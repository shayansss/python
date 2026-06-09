#!/usr/bin/env python3
"""Figure: free-body diagrams for the two-DOF undamped example."""

from __future__ import annotations

from plot_helpers import FILL, NAVY, OUT, configure_matplotlib_cache


configure_matplotlib_cache()
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


fig, ax = plt.subplots(figsize=(8.4, 3.2))
ax.set_xlim(0, 10)
ax.set_ylim(0, 4)
ax.axis("off")


def mass_box(x, y, label):
    ax.add_patch(Rectangle((x - 0.55, y - 0.38), 1.1, 0.76, facecolor=FILL, edgecolor=NAVY, linewidth=2))
    ax.text(x, y, label, ha="center", va="center", fontsize=15)


def force_arrow(start, end, label, label_offset=(0, 0)):
    ax.annotate("", xy=end, xytext=start, arrowprops=dict(arrowstyle="->", color=NAVY, linewidth=1.8))
    lx = (start[0] + end[0]) / 2 + label_offset[0]
    ly = (start[1] + end[1]) / 2 + label_offset[1]
    ax.text(lx, ly, label, ha="center", va="center", fontsize=12)


mass_box(2.7, 2.0, r"$m_1$")
force_arrow((2.15, 2.0), (1.15, 2.0), r"$k_1x_1$", (0, 0.35))
force_arrow((3.25, 2.0), (4.55, 2.0), r"$k_2(x_2-x_1)$", (0, 0.35))
force_arrow((2.7, 2.55), (3.55, 2.55), r"$\ddot{x}_1$", (0, 0.22))
ax.text(2.7, 0.95, r"$m_1\ddot{x}_1=-k_1x_1+k_2(x_2-x_1)$", ha="center", fontsize=12)

mass_box(7.3, 2.0, r"$m_2$")
force_arrow((7.85, 2.0), (8.85, 2.0), r"$k_3x_2$", (0, 0.35))
force_arrow((6.75, 2.0), (5.45, 2.0), r"$k_2(x_2-x_1)$", (0, 0.35))
force_arrow((7.3, 2.55), (8.15, 2.55), r"$\ddot{x}_2$", (0, 0.22))
ax.text(7.3, 0.95, r"$m_2\ddot{x}_2=-k_2(x_2-x_1)-k_3x_2$", ha="center", fontsize=12)

ax.text(
    5,
    3.55,
    r"Assume $x_2>x_1$: spring $k_2$ is stretched and pulls the two masses together",
    ha="center",
    fontsize=11,
    color="#333333",
)

fig.savefig(OUT / "lecture6_free_body_diagrams.png", bbox_inches="tight", dpi=180)
plt.close(fig)
