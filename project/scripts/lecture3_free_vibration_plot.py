#!/usr/bin/env python3
"""Figure: undamped free vibration amplitude and period."""

from __future__ import annotations

import math

import numpy as np

from plot_helpers import NAVY, RED, configure_matplotlib_cache


configure_matplotlib_cache()
import matplotlib.pyplot as plt


wn = 2 * math.pi
T = 2 * math.pi / wn
t = np.linspace(0, 3.4 * T, 800)
x0 = 1.0
v0 = 0.35 * wn
x = x0 * np.cos(wn * t) + (v0 / wn) * np.sin(wn * t)
amp = math.sqrt(x0**2 + (v0 / wn) ** 2)

fig, ax = plt.subplots(figsize=(7.2, 3.0))
ax.plot(t, x, color=RED, linewidth=2.3)
ax.axhline(0.0, color="#333333", linewidth=0.9)

first_peak_t = math.atan2(v0 / wn, x0) / wn
if first_peak_t < 0:
    first_peak_t += T
second_peak_t = first_peak_t + T

ax.annotate(
    "",
    xy=(first_peak_t, amp),
    xytext=(first_peak_t, 0.0),
    arrowprops=dict(arrowstyle="<->", color=RED, linewidth=1.5),
)
ax.text(first_peak_t + 0.05, 0.55 * amp, "amplitude", color=RED, fontsize=12, va="center")

y_period = -1.22 * amp
ax.annotate(
    "",
    xy=(first_peak_t, y_period),
    xytext=(second_peak_t, y_period),
    arrowprops=dict(arrowstyle="<->", color=RED, linewidth=1.5),
)
ax.text(
    0.5 * (first_peak_t + second_peak_t),
    y_period - 0.15,
    r"$T=\frac{2\pi}{\omega_n}$",
    color=RED,
    fontsize=13,
    ha="center",
    va="top",
)

ax.text(0.03, 0.93, r"$x(t)=x_0\cos\omega_n t+\frac{v_0}{\omega_n}\sin\omega_n t$", transform=ax.transAxes, fontsize=14)
ax.set_xlabel("t")
ax.set_ylabel("x(t)")
ax.set_xlim(t.min(), t.max())
ax.set_ylim(-1.55 * amp, 1.45 * amp)
ax.spines[["top", "right"]].set_visible(False)
ax.grid(True, alpha=0.22)
fig.tight_layout()
fig.savefig("scripts/lecture3_free_vibration_plot.png", dpi=180)
plt.close(fig)
