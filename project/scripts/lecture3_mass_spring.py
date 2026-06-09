#!/usr/bin/env python3
"""Figure: undamped SDOF mass-spring schematic."""

from __future__ import annotations

from plot_helpers import NAVY, OUT, configure_matplotlib_cache


def setup_axis():
    configure_matplotlib_cache()
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(4.8, 5.4))
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(0.35, 4.55)
    ax.axis("off")
    return fig, ax


def draw_mass(ax, center=(0.0, 3.275), width=1.5, height=0.85, label=r"$m$") -> None:
    import matplotlib.pyplot as plt

    cx, cy = center
    ax.add_patch(
        plt.Rectangle(
            (cx - width / 2, cy - height / 2),
            width,
            height,
            facecolor="#eef4fb",
            edgecolor=NAVY,
            linewidth=2.4,
        )
    )
    ax.text(cx, cy, label, ha="center", va="center", fontsize=22)


def draw_spring(ax, x=0.0, y_top=2.85, y_bottom=0.78, width=0.48, turns=7, label=r"$k$") -> None:
    y_values = [y_top, y_top - 0.23]
    x_values = [x, x]
    coil_height = y_top - 0.23 - y_bottom

    for i in range(turns * 2 + 1):
        y_values.append(y_top - 0.23 - (i + 1) * (coil_height / (turns * 2 + 2)))
        x_values.append(x + width / 2 * (-1 if i % 2 == 0 else 1))

    y_values.append(y_bottom)
    x_values.append(x)
    ax.plot(x_values, y_values, color=NAVY, linewidth=2.3)
    ax.text(x + 0.42, (y_top + y_bottom) / 2, label, fontsize=20)


def draw_ground(ax, y=0.72, x_left=-1.25, x_right=1.25) -> None:
    ax.plot([x_left, x_right], [y, y], color=NAVY, linewidth=2.4)
    for gx in [i / 4 for i in range(-4, 5)]:
        ax.plot([gx, gx - 0.14], [y, y - 0.20], color=NAVY, linewidth=1.2)


def draw_displacement_arrow(ax) -> None:
    ax.annotate(
        r"$x(t)$",
        xy=(0, 4.35),
        xytext=(0, 3.9),
        ha="center",
        fontsize=16,
        arrowprops=dict(arrowstyle="->", color=NAVY, linewidth=1.8),
    )


configure_matplotlib_cache()
import matplotlib.pyplot as plt

fig, ax = setup_axis()
draw_displacement_arrow(ax)
draw_mass(ax)
draw_spring(ax)
draw_ground(ax)
fig.savefig(OUT / "lecture3_mass_spring.png", bbox_inches="tight", dpi=180)
plt.close(fig)
