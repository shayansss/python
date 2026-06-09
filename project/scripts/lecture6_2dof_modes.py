#!/usr/bin/env python3
"""Figure: modal motion sketches of the equal 2-DOF example."""

from __future__ import annotations

from plot_helpers import NAVY, OUT, RED, configure_matplotlib_cache


configure_matplotlib_cache()
import matplotlib.pyplot as plt


fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.8), sharey=True)
xpos = [0.0, 1.0, 2.0]
snapshots = [-1.0, -0.55, 0.0, 0.55, 1.0]
modes = [
    ([1.0, 1.0], "1st mode of vibration", r"$\psi_1=[1,\ 1]^T,\quad \omega_{n1}=\sqrt{\frac{k}{m}}$"),
    ([1.0, -1.0], "2nd mode of vibration", r"$\psi_2=[1,\ -1]^T,\quad \omega_{n2}=\sqrt{\frac{3k}{m}}$"),
]

for ax, (shape, title, equation) in zip(axes, modes):
    ax.axhline(0, color="#333333", linewidth=0.9)
    ax.axvline(0, color="#333333", linewidth=0.9)

    for amp in snapshots:
        yvals = [0.0, amp * shape[0], amp * shape[1]]
        style = "-" if abs(amp) == 1.0 else "--"
        width = 2.2 if abs(amp) == 1.0 else 1.25
        alpha = 1.0 if abs(amp) == 1.0 else 0.55
        ax.plot(xpos, yvals, color=RED, linestyle=style, linewidth=width, alpha=alpha)
        ax.plot([1, 2], [yvals[1], yvals[2]], "o", color=RED, markersize=3.5, alpha=alpha)

    ax.text(1, 1.18, r"$x_1$", ha="center", color=RED, fontsize=11)
    ax.text(2, 1.18, r"$x_2$", ha="center", color=RED, fontsize=11)
    ax.text(1.0, -1.28, equation, ha="center", color=NAVY, fontsize=11)
    ax.set_title(title, color=NAVY, fontweight="bold", fontsize=13)
    ax.set_xlim(-0.12, 2.15)
    ax.set_ylim(-1.42, 1.42)
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(["reference", r"$m_1$", r"$m_2$"])
    ax.grid(True, alpha=0.18)

axes[0].set_ylabel("relative displacement")
fig.suptitle("Modal Motion Sketches for Equal Masses and Equal Springs", color=NAVY, fontweight="bold", fontsize=15)
fig.tight_layout()
fig.savefig(OUT / "lecture6_2dof_modes.png", dpi=180)
plt.close(fig)
