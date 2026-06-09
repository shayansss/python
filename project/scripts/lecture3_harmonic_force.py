#!/usr/bin/env python3
"""Figure: harmonic excitation used in forced vibration."""

from __future__ import annotations

import math

from plot_helpers import NAVY, OUT, configure_matplotlib_cache


configure_matplotlib_cache()
import matplotlib.pyplot as plt


F0 = 1.0
Omega = 2 * math.pi
t = [2.5 * i / 500 for i in range(501)]
f = [F0 * math.cos(Omega * ti) for ti in t]

fig, ax = plt.subplots(figsize=(7.0, 3.2))
ax.plot(t, f, color=NAVY, linewidth=2.2)
ax.axhline(0.0, color="#333333", linewidth=0.9)
ax.annotate(
    "",
    xy=(0.0, F0),
    xytext=(0.0, 0.0),
    arrowprops=dict(arrowstyle="<->", color="#c62828", linewidth=1.6),
)
ax.text(-0.06, 0.55 * F0, r"$F_0$", color="#c62828", fontsize=15, ha="right")
ax.text(1.22, -1.20, r"$F(t)=F_0\cos\Omega t$", fontsize=15)
ax.set_xlabel("t")
ax.set_ylabel("force, F(t)")
ax.set_title("Harmonic Excitation", color=NAVY, fontweight="bold")
ax.set_ylim(-1.35, 1.35)
ax.grid(True, alpha=0.25)
fig.tight_layout()
fig.savefig(OUT / "lecture3_harmonic_force.png", dpi=180)
plt.close(fig)
