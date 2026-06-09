#!/usr/bin/env python3
"""Figure: complex-plane force equilibrium at low frequency and resonance."""

from __future__ import annotations

import math

from plot_helpers import NAVY, OUT, RED, configure_matplotlib_cache


configure_matplotlib_cache()
import matplotlib.pyplot as plt


def arrow(ax, angle, length, label, color=NAVY, rlabel=1.1, dx=0.0, dy=0.0):
    x = length * math.cos(angle)
    y = length * math.sin(angle)
    ax.annotate("", xy=(x, y), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color=color, linewidth=2.0))
    ax.text(rlabel * x + dx, rlabel * y + dy, label, color=color, fontsize=11, ha="center", va="center")


fig, axes = plt.subplots(1, 2, figsize=(8.2, 3.9))

for ax, title in zip(axes, [r"Low frequency: $\Omega\ll\omega_n$", r"At resonance: $\Omega=\omega_n$"]):
    ax.set_title(title, color=NAVY, fontweight="bold")
    ax.axhline(0, color="#333333", linewidth=0.9)
    ax.axvline(0, color="#333333", linewidth=0.9)
    ax.text(1.22, -0.08, "Re", fontsize=10)
    ax.text(0.07, 1.18, "Im", fontsize=10)
    ax.set_xlim(-1.35, 1.35)
    ax.set_ylim(-1.25, 1.25)
    ax.set_aspect("equal")
    ax.axis("off")

arrow(axes[0], math.radians(55), 0.95, r"$\bar{F}$", RED)
arrow(axes[0], math.radians(35), 0.62, r"$\bar{x}$", NAVY, 1.18, 0.04, -0.02)
arrow(axes[0], math.radians(125), 0.72, r"$\dot{\bar{x}}$", NAVY)
arrow(axes[0], math.radians(215), 0.72, r"$\ddot{\bar{x}}$", NAVY, 1.15, -0.04, -0.02)
arrow(axes[0], math.radians(225), 0.50, r"$c\dot{\bar{x}}$", "#7b1fa2", 1.55, -0.04, -0.05)
arrow(axes[0], math.radians(35), 0.46, r"$k\bar{x}$", "#7b1fa2", 1.55, 0.08, 0.08)
arrow(axes[0], math.radians(215), 0.34, r"$m\ddot{\bar{x}}$", "#7b1fa2", 2.05, -0.05, -0.11)

arrow(axes[1], math.radians(45), 0.90, r"$\bar{F}$", RED)
arrow(axes[1], math.radians(-45), 0.65, r"$\bar{x}$", NAVY, 1.12, 0.06, -0.02)
arrow(axes[1], math.radians(45), 0.65, r"$\dot{\bar{x}}$", NAVY, 1.10, -0.02, 0.04)
arrow(axes[1], math.radians(135), 0.65, r"$\ddot{\bar{x}}$", NAVY, 1.15, -0.06, 0.07)
arrow(axes[1], math.radians(225), 0.62, r"$c\dot{\bar{x}}$", "#7b1fa2", 1.42, -0.04, -0.04)
arrow(axes[1], math.radians(-45), 0.58, r"$k\bar{x}$", "#7b1fa2", 1.48, 0.10, -0.05)
arrow(axes[1], math.radians(135), 0.58, r"$m\ddot{\bar{x}}$", "#7b1fa2", 1.50, -0.12, 0.08)

fig.suptitle("Dynamic Equilibrium of Forces", color=NAVY, fontweight="bold")
fig.tight_layout()
fig.savefig(OUT / "lecture4_dynamic_equilibrium.png", dpi=180)
plt.close(fig)
