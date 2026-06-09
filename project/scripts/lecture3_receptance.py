#!/usr/bin/env python3
"""Figure: undamped SDOF receptance magnitude and phase."""

from __future__ import annotations

from plot_helpers import NAVY, OUT, configure_matplotlib_cache


configure_matplotlib_cache()
import matplotlib.pyplot as plt


m = 1.0
k = 100.0
wn = (k / m) ** 0.5
ratios_left = [0.02 + (0.96 - 0.02) * i / 700 for i in range(701)]
ratios_right = [1.04 + (2.20 - 1.04) * i / 900 for i in range(901)]


def receptance(r: float) -> float:
    omega = r * wn
    return 1.0 / (k - m * omega**2)


mag_left = [abs(receptance(r)) for r in ratios_left]
mag_right = [abs(receptance(r)) for r in ratios_right]
clip = 0.12
mag_left = [min(v, clip) for v in mag_left]
mag_right = [min(v, clip) for v in mag_right]

fig, (ax_mag, ax_phase) = plt.subplots(
    2,
    1,
    figsize=(7.2, 6.0),
    sharex=True,
    gridspec_kw={"height_ratios": [3, 1.4]},
)

ax_mag.plot(ratios_left, mag_left, color=NAVY, linewidth=2.2)
ax_mag.plot(ratios_right, mag_right, color=NAVY, linewidth=2.2)
ax_mag.axvline(1.0, color="#c62828", linestyle="--", linewidth=1.5)
ax_mag.text(1.03, 0.105, r"$\Omega=\omega_n$", color="#c62828", fontsize=12)
ax_mag.set_ylabel(r"$|\alpha(\Omega)|$")
ax_mag.set_title("Undamped SDOF Frequency Response Function", color=NAVY, fontweight="bold")
ax_mag.grid(True, alpha=0.25)
ax_mag.set_ylim(0, clip)

ax_phase.plot([0.0, 1.0], [0, 0], color=NAVY, linewidth=2.2)
ax_phase.plot([1.0, 2.2], [180, 180], color=NAVY, linewidth=2.2)
ax_phase.axvline(1.0, color="#c62828", linestyle="--", linewidth=1.5)
ax_phase.set_yticks([0, 180])
ax_phase.set_ylabel("phase")
ax_phase.set_xlabel(r"frequency ratio, $\Omega/\omega_n$")
ax_phase.grid(True, alpha=0.25)
ax_phase.set_xlim(0, 2.2)
ax_phase.set_ylim(-25, 205)

fig.tight_layout()
fig.savefig(OUT / "lecture3_receptance.png", dpi=180)
plt.close(fig)
