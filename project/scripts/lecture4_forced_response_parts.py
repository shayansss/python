#!/usr/bin/env python3
"""Figure: transient, steady-state, and total response under harmonic force."""

from __future__ import annotations

import math

from plot_helpers import NAVY, OUT, RED, configure_matplotlib_cache


configure_matplotlib_cache()
import matplotlib.pyplot as plt


t = [12 * i / 1200 for i in range(1201)]
xc = [1.0 * math.exp(-0.28 * ti) * math.cos(2.7 * ti - 0.35) for ti in t]
xp = [0.45 * math.cos(1.55 * ti - 0.65) for ti in t]
x = [a + b for a, b in zip(xc, xp)]

fig, axes = plt.subplots(3, 1, figsize=(7.6, 6.2), sharex=True)
for ax, y, title, color in [
    (axes[0], xc, r"transient part $x_c(t)$", RED),
    (axes[1], xp, r"steady-state part $x_p(t)$", NAVY),
    (axes[2], x, r"total response $x(t)=x_c(t)+x_p(t)$", "#2e7d32"),
]:
    ax.plot(t, y, color=color, linewidth=2.0)
    ax.axhline(0, color="#333333", linewidth=0.8)
    ax.set_ylabel("x(t)")
    ax.set_title(title, color=NAVY, fontsize=11)
    ax.grid(True, alpha=0.23)

axes[2].set_xlabel("t")
fig.suptitle("Forced Response Components", color=NAVY, fontweight="bold")
fig.tight_layout()
fig.savefig(OUT / "lecture4_forced_response_parts.png", dpi=180)
plt.close(fig)
