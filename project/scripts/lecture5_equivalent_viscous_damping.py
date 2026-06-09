#!/usr/bin/env python3
"""Figure: frequency-dependent equivalent viscous damping ratio."""

from __future__ import annotations

from plot_helpers import NAVY, OUT, RED, configure_matplotlib_cache


configure_matplotlib_cache()
import matplotlib.pyplot as plt


eta = 0.12
r = [0.2 + 2.8 * i / 600 for i in range(601)]
zeta_eq = [eta / (2 * ri) for ri in r]

fig, ax = plt.subplots(figsize=(6.8, 3.8))
ax.plot(r, zeta_eq, color=NAVY, linewidth=2.3)
ax.axvline(1.0, color=RED, linestyle="--", linewidth=1.4)
ax.axhline(eta / 2, color=RED, linestyle=":", linewidth=1.4)
ax.text(1.03, eta / 2 + 0.012, r"at resonance: $\zeta_{\mathrm{eq}}=\eta/2$", color=RED, fontsize=10)
ax.set_xlabel(r"$\Omega/\omega_n$")
ax.set_ylabel(r"$\zeta_{\mathrm{eq}}$")
ax.set_title("Equivalent Viscous Damping Ratio", color=NAVY, fontweight="bold")
ax.grid(True, alpha=0.25)
ax.set_ylim(0, max(zeta_eq) * 1.05)
fig.tight_layout()
fig.savefig(OUT / "lecture5_equivalent_viscous_damping.png", dpi=180)
plt.close(fig)
