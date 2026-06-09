#!/usr/bin/env python3
"""Figure: stress-strain hysteresis loop and ideal elastic response."""

from __future__ import annotations

import math

from plot_helpers import NAVY, OUT, RED, configure_matplotlib_cache


configure_matplotlib_cache()
import matplotlib.pyplot as plt


theta = [2 * math.pi * i / 500 for i in range(501)]
eps = [math.sin(th) for th in theta]
phase = math.radians(22)
stress = [1.15 * math.sin(th + phase) for th in theta]

fig, (ax_loop, ax_ideal) = plt.subplots(1, 2, figsize=(8.0, 3.6))

ax_loop.plot(eps, stress, color=NAVY, linewidth=2.3)
ax_loop.fill(eps, stress, color=NAVY, alpha=0.08)
ax_loop.annotate("loading", xy=(0.55, 0.88), xytext=(0.05, 1.15), arrowprops=dict(arrowstyle="->", color=RED), color=RED)
ax_loop.annotate("unloading", xy=(-0.55, -0.88), xytext=(-0.15, -1.15), arrowprops=dict(arrowstyle="->", color=RED), color=RED)
ax_loop.text(0.0, 0.0, "loop area\n= energy loss\nper unit volume", ha="center", va="center", fontsize=10)
ax_loop.set_title("Practical material", color=NAVY, fontweight="bold")

ax_ideal.plot([-1, 1], [-1, 1], color=NAVY, linewidth=2.3)
ax_ideal.annotate("same path", xy=(0.55, 0.55), xytext=(-0.55, 0.85), arrowprops=dict(arrowstyle="->", color=RED), color=RED)
ax_ideal.set_title("Ideal elastic case", color=NAVY, fontweight="bold")

for ax in (ax_loop, ax_ideal):
    ax.axhline(0, color="#333333", linewidth=0.8)
    ax.axvline(0, color="#333333", linewidth=0.8)
    ax.set_xlabel("strain")
    ax.set_ylabel("stress")
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.22)

fig.tight_layout()
fig.savefig(OUT / "lecture5_hysteresis_loop.png", dpi=180)
plt.close(fig)
