#!/usr/bin/env python3
"""Figure: logarithmic decrement from decaying free-vibration peaks."""

from __future__ import annotations

import math

from plot_helpers import NAVY, OUT, RED, configure_matplotlib_cache


configure_matplotlib_cache()
import matplotlib.pyplot as plt


zeta = 0.08
wn = 2 * math.pi
wd = wn * math.sqrt(1 - zeta**2)
t = [5.0 * i / 1000 for i in range(1001)]
x = [math.exp(-zeta * wn * ti) * math.cos(wd * ti) for ti in t]
tj = 1.0 * 2 * math.pi / wd
tn = 4.0 * 2 * math.pi / wd
xj = math.exp(-zeta * wn * tj)
xn = math.exp(-zeta * wn * tn)

fig, ax = plt.subplots(figsize=(7.2, 3.7))
ax.plot(t, x, color=NAVY, linewidth=2.0)
ax.plot(t, [math.exp(-zeta * wn * ti) for ti in t], color=RED, linestyle="--", linewidth=1.4)
ax.vlines([tj, tn], [0, 0], [xj, xn], color="#333333", linewidth=1.0)
ax.scatter([tj, tn], [xj, xn], color=RED, zorder=3)
ax.annotate(r"$x_j$", xy=(tj, xj), xytext=(tj - 0.55, xj + 0.13), arrowprops=dict(arrowstyle="->", color=RED), color=RED)
ax.annotate(r"$x_{j+n}$", xy=(tn, xn), xytext=(tn + 0.15, xn + 0.18), arrowprops=dict(arrowstyle="->", color=RED), color=RED)
ax.annotate(r"$nT_d$", xy=(tj, 0.78), xytext=(tn, 0.78), arrowprops=dict(arrowstyle="<->", color="#333333"), ha="center")
ax.axhline(0, color="#333333", linewidth=0.8)
ax.set_xlabel("t")
ax.set_ylabel("x(t)")
ax.set_title("Logarithmic Decrement", color=NAVY, fontweight="bold")
ax.text(2.6, -0.88, r"$\delta=\frac{1}{n}\ln\left(\frac{x_j}{x_{j+n}}\right)$", fontsize=15)
ax.grid(True, alpha=0.22)
fig.tight_layout()
fig.savefig(OUT / "lecture4_logarithmic_decrement.png", dpi=180)
plt.close(fig)
