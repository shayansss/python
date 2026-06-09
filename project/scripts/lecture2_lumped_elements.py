#!/usr/bin/env python3
from plot_helpers import MUTED, NAVY, canvas, draw_damper, draw_mass, draw_spring, save_figure

fig, ax = canvas(8.6, 2.9)
ax.set_xlim(0.45, 9.45)
ax.set_ylim(1.45, 5.25)
ax.text(1.8, 4.9, "Rigid mass", ha="center", color=NAVY, fontsize=14, fontweight="bold")
ax.text(5.0, 4.9, "Spring", ha="center", color=NAVY, fontsize=14, fontweight="bold")
ax.text(8.1, 4.9, "Viscous damper", ha="center", color=NAVY, fontsize=14, fontweight="bold")
draw_mass(ax, (1.8, 3.5), r"$m$", 1.5, 0.85)
ax.plot([0.65, 1.05], [3.5, 3.5], color=NAVY, linewidth=2)
ax.plot([2.55, 3.0], [3.5, 3.5], color=NAVY, linewidth=2)
draw_spring(ax, 4.05, 5.95, 3.5)
ax.text(5, 4.12, r"$k$", ha="center", fontsize=16)
draw_damper(ax, 7.15, 9.1, 3.5)
ax.text(8.1, 4.12, r"$c$", ha="center", fontsize=16)
for x, lines in [(1.8, ["mass only", "no stiffness", "no damping"]), (5.0, ["stiffness only", "no mass", "no damping"]), (8.1, ["damping only", "no mass", "no stiffness"])]:
    for i, line in enumerate(lines):
        ax.text(x, 2.45 - 0.38 * i, line, ha="center", fontsize=10, color=MUTED)
save_figure(fig, "lecture2_lumped_elements.png")
