#!/usr/bin/env python3
"""Figure: steady-state amplitude of viscously damped SDOF response."""

from __future__ import annotations

import math

from plot_helpers import NAVY, OUT, RED, configure_matplotlib_cache


configure_matplotlib_cache()
import matplotlib.pyplot as plt


r = [0.02 + 2.98 * i / 1000 for i in range(1001)]
zeta = 0.12
amp = [1.0 / math.sqrt((1 - ri**2) ** 2 + (2 * zeta * ri) ** 2) for ri in r]

fig, ax = plt.subplots(figsize=(6.8, 3.8))
ax.plot(r, amp, color=NAVY, linewidth=2.3)
ax.axvline(1.0, color=RED, linestyle="--", linewidth=1.4)
ax.axhline(1.0, color="#6b7280", linestyle=":", linewidth=1.2)
ax.text(1.03, max(amp) * 0.84, r"$\Omega\approx\omega_n$", color=RED, fontsize=11)
ax.text(0.06, 1.12, r"$X_{\mathrm{st}}$", color="#6b7280", fontsize=11)
ax.set_xlabel(r"$\Omega/\omega_n$")
ax.set_ylabel(r"$X_p/X_{\mathrm{st}}$")
ax.set_title("Steady-State Amplitude", color=NAVY, fontweight="bold")
ax.set_ylim(0, max(amp) * 1.08)
ax.grid(True, alpha=0.25)
fig.tight_layout()
fig.savefig(OUT / "lecture4_steady_state_response.png", dpi=180)
plt.close(fig)
