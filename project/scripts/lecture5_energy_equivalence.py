#!/usr/bin/env python3
"""Figure: equivalent viscous damping from energy equivalence."""

from __future__ import annotations

from plot_helpers import NAVY, OUT, RED, configure_matplotlib_cache


configure_matplotlib_cache()
import matplotlib.pyplot as plt


omega = [0.15 + 3.0 * i / 500 for i in range(501)]
alpha_a2 = 1.0
c = 0.35
edh = [alpha_a2 for _ in omega]
edv = [3.14159 * c * om for om in omega]
ceq = [alpha_a2 / (3.14159 * om) for om in omega]

fig, (ax_e, ax_c) = plt.subplots(1, 2, figsize=(8.2, 3.6))

ax_e.plot(omega, edh, color=NAVY, linewidth=2.2, label=r"structural: $E_{dh}=\alpha A^2$")
ax_e.plot(omega, edv, color=RED, linewidth=2.2, label=r"viscous: $E_{dv}=\pi c\Omega A^2$")
ax_e.set_xlabel(r"$\Omega$")
ax_e.set_ylabel("energy per cycle")
ax_e.set_title("Energy loss per cycle", color=NAVY, fontweight="bold")
ax_e.grid(True, alpha=0.25)
ax_e.legend(frameon=False, fontsize=8)

ax_c.plot(omega, ceq, color=NAVY, linewidth=2.2)
ax_c.set_xlabel(r"$\Omega$")
ax_c.set_ylabel(r"$c_{\mathrm{eq}}$")
ax_c.set_title(r"$c_{\mathrm{eq}}=h/\Omega$", color=NAVY, fontweight="bold")
ax_c.grid(True, alpha=0.25)
ax_c.text(1.45, 1.65, "equivalence changes\nwith frequency", fontsize=10, color="#333333")

fig.tight_layout()
fig.savefig(OUT / "lecture5_energy_equivalence.png", dpi=180)
plt.close(fig)
