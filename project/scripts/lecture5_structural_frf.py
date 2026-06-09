#!/usr/bin/env python3
"""Figure: FRF magnitude and phase for structural damping."""

from __future__ import annotations

import math

from plot_helpers import NAVY, OUT, RED, configure_matplotlib_cache


configure_matplotlib_cache()
import matplotlib.pyplot as plt


eta = 0.12
r = [0.02 + 2.48 * i / 1000 for i in range(1001)]
mag = [1.0 / math.sqrt((1 - ri**2) ** 2 + eta**2) for ri in r]
phase_lag = [math.degrees(math.atan2(eta, 1 - ri**2)) for ri in r]

fig, (ax_mag, ax_phase) = plt.subplots(2, 1, figsize=(7.2, 5.7), sharex=True, gridspec_kw={"height_ratios": [3, 1.5]})

ax_mag.plot(r, mag, color=NAVY, linewidth=2.3)
ax_mag.axvline(1.0, color=RED, linestyle="--", linewidth=1.4)
ax_mag.text(1.03, max(mag) * 0.88, r"$\Omega=\omega_n$", color=RED, fontsize=11)
ax_mag.set_ylabel(r"$|\alpha|/(1/k)$")
ax_mag.set_title("Structural-Damping FRF", color=NAVY, fontweight="bold")
ax_mag.grid(True, alpha=0.25)

ax_phase.plot(r, phase_lag, color=NAVY, linewidth=2.3)
ax_phase.axvline(1.0, color=RED, linestyle="--", linewidth=1.4)
ax_phase.set_yticks([0, 90, 180])
ax_phase.set_ylabel("phase lag")
ax_phase.set_xlabel(r"$\Omega/\omega_n$")
ax_phase.grid(True, alpha=0.25)

fig.tight_layout()
fig.savefig(OUT / "lecture5_structural_frf.png", dpi=180)
plt.close(fig)
