#!/usr/bin/env python3
"""Figure: qualitative decay of system energy for different damping levels."""

from __future__ import annotations

import math

from plot_helpers import NAVY, OUT, RED, configure_matplotlib_cache


configure_matplotlib_cache()
import matplotlib.pyplot as plt


t = [5 * i / 600 for i in range(601)]
fig, (ax_over, ax_under) = plt.subplots(1, 2, figsize=(8.2, 3.7), sharey=True)

for rate, label, color in [
    (0.0, r"$\zeta=\infty$", "#6b7280"),
    (0.25, r"large $\zeta$", "#607d8b"),
    (0.55, r"$\zeta$ reducing", NAVY),
    (1.05, r"$\zeta=1$", RED),
]:
    y = [math.exp(-rate * ti) if rate else 1.0 for ti in t]
    ax_over.plot(t, y, color=color, linewidth=2.0, label=label)

for rate, label, color in [
    (0.0, r"$\zeta=0$", "#6b7280"),
    (0.30, r"small $\zeta$", NAVY),
    (0.70, r"larger $\zeta$", "#2e7d32"),
    (1.05, r"$\zeta\to1^-$", RED),
]:
    y = [math.exp(-rate * ti) if rate else 1.0 for ti in t]
    ax_under.plot(t, y, color=color, linewidth=2.0, label=label)

for ax, title in [(ax_over, "Overdamped systems"), (ax_under, "Underdamped systems")]:
    ax.set_title(title, color=NAVY, fontweight="bold")
    ax.set_xlabel("t")
    ax.set_ylim(-0.04, 1.06)
    ax.grid(True, alpha=0.25)
    ax.legend(frameon=False, fontsize=8)

ax_over.set_ylabel("E(t)")
fig.suptitle("Decay of System Energy", color=NAVY, fontweight="bold")
fig.tight_layout()
fig.savefig(OUT / "lecture4_energy_decay.png", dpi=180)
plt.close(fig)
