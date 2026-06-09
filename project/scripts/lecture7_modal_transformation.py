#!/usr/bin/env python3
"""Figure: modal transformation as an expansion in mode-shape basis vectors."""

from __future__ import annotations

import numpy as np

from plot_helpers import NAVY, OUT, RED, configure_matplotlib_cache


configure_matplotlib_cache()
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection


fig = plt.figure(figsize=(7.2, 5.2))
ax = fig.add_subplot(111, projection="3d")

origin = np.zeros(3)
basis = np.array(
    [
        [1.0, 0.15, 0.05],
        [0.1, 0.95, 0.2],
        [0.05, 0.15, 1.05],
    ]
)
y = np.array([1.4, 0.9, 0.75])
x = y @ basis

for idx, vec in enumerate(basis, start=1):
    ax.quiver(*origin, *vec, color=NAVY, linewidth=2.0, arrow_length_ratio=0.08)
    ax.text(*(vec * 1.08), rf"$\psi_{idx}$", color=NAVY, fontsize=12)

ax.quiver(*origin, *x, color=RED, linewidth=2.6, arrow_length_ratio=0.06)
ax.text(*(x * 1.05), r"$x=\Psi y$", color=RED, fontsize=12)

segments = []
point = origin.copy()
for coeff, vec in zip(y, basis):
    new = point + coeff * vec
    segments.append([point, new])
    point = new
ax.add_collection3d(Line3DCollection(segments, colors="#777777", linewidths=1.4, linestyles="dashed"))

ax.text2D(0.05, 0.93, "Modal transformation", transform=ax.transAxes, color=NAVY, fontsize=15, fontweight="bold")
ax.text2D(0.05, 0.86, r"$x=y_1\psi_1+y_2\psi_2+\cdots+y_n\psi_n$", transform=ax.transAxes, fontsize=12)
ax.text2D(0.05, 0.79, r"$y_r$: participation of mode $r$", transform=ax.transAxes, fontsize=11)

ax.set_xlim(0, 2.3)
ax.set_ylim(0, 1.7)
ax.set_zlim(0, 1.6)
ax.set_xlabel("coordinate 1")
ax.set_ylabel("coordinate 2")
ax.set_zlabel("coordinate 3")
ax.view_init(elev=23, azim=-54)
ax.grid(True, alpha=0.25)

fig.savefig(OUT / "lecture7_modal_transformation.png", dpi=180, bbox_inches="tight")
plt.close(fig)
