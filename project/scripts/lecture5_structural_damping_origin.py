#!/usr/bin/env python3
"""Figure: structural damping as internal material energy loss."""

from __future__ import annotations

import math

from plot_helpers import NAVY, OUT, RED, configure_matplotlib_cache


configure_matplotlib_cache()
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


fig, (ax_beam, ax_decay) = plt.subplots(1, 2, figsize=(8.0, 3.4))

ax_beam.set_xlim(0, 5)
ax_beam.set_ylim(0, 3)
ax_beam.axis("off")
ax_beam.set_title("Cantilever free vibration", color=NAVY, fontweight="bold")
ax_beam.add_patch(Rectangle((0.45, 0.55), 0.22, 1.9, facecolor="#d9dfe8", edgecolor=NAVY, linewidth=2.0))
ax_beam.plot([0.67, 4.35], [1.75, 1.75], color=NAVY, linewidth=4.0)
ax_beam.plot([0.67, 4.35], [1.75, 1.95], color=NAVY, linewidth=2.0, alpha=0.35)
ax_beam.annotate("", xy=(4.35, 2.15), xytext=(4.35, 1.34), arrowprops=dict(arrowstyle="<->", color=RED, linewidth=1.8))
ax_beam.text(2.5, 0.75, "energy lost inside material", ha="center", fontsize=11, color="#333333")

t = [7 * i / 900 for i in range(901)]
x = [math.exp(-0.28 * ti) * math.cos(6.5 * ti) for ti in t]
env = [math.exp(-0.28 * ti) for ti in t]
ax_decay.plot(t, x, color=NAVY, linewidth=2.0)
ax_decay.plot(t, env, color=RED, linestyle="--", linewidth=1.2)
ax_decay.plot(t, [-v for v in env], color=RED, linestyle="--", linewidth=1.2)
ax_decay.axhline(0, color="#333333", linewidth=0.8)
ax_decay.set_title("Decaying free response", color=NAVY, fontweight="bold")
ax_decay.set_xlabel("t")
ax_decay.set_ylabel("amplitude")
ax_decay.grid(True, alpha=0.25)

fig.tight_layout()
fig.savefig(OUT / "lecture5_structural_damping_origin.png", dpi=180)
plt.close(fig)
