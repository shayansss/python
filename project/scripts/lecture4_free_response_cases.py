#!/usr/bin/env python3
"""Figure: overdamped, critically damped, and underdamped free responses."""

from __future__ import annotations

import math

from plot_helpers import NAVY, OUT, RED, configure_matplotlib_cache


configure_matplotlib_cache()
import matplotlib.pyplot as plt


t = [6 * i / 700 for i in range(701)]
wn = 1.0
over = [math.exp(-0.45 * ti) * (1.0 + 0.12 * ti) for ti in t]
critical = [(1.0 + ti) * math.exp(-ti) for ti in t]
under_low = [math.exp(-0.10 * ti) * math.cos(math.sqrt(1 - 0.10**2) * ti) for ti in t]
under_high = [math.exp(-0.32 * ti) * math.cos(math.sqrt(1 - 0.32**2) * ti) for ti in t]

fig, ax = plt.subplots(figsize=(7.2, 4.0))
ax.plot(t, over, color="#6b7280", linewidth=2.1, label=r"overdamped, $\zeta>1$")
ax.plot(t, critical, color=RED, linewidth=2.1, label=r"critical, $\zeta=1$")
ax.plot(t, under_low, color=NAVY, linewidth=2.1, label=r"underdamped, low $\zeta$")
ax.plot(t, under_high, color="#2e7d32", linewidth=2.1, label=r"underdamped, higher $\zeta$")
ax.axhline(0, color="#333333", linewidth=0.8)
ax.set_xlabel("t")
ax.set_ylabel("x(t)")
ax.set_title("Free Response Types", color=NAVY, fontweight="bold")
ax.grid(True, alpha=0.25)
ax.legend(frameon=False, fontsize=9, loc="upper right")
fig.tight_layout()
fig.savefig(OUT / "lecture4_free_response_cases.png", dpi=180)
plt.close(fig)
