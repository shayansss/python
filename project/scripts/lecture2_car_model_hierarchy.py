#!/usr/bin/env python3
"""Figure: one compact car model hierarchy with sketches."""

from __future__ import annotations

from plot_helpers import FILL, NAVY, OUT, configure_matplotlib_cache


configure_matplotlib_cache()
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, FancyArrowPatch, Rectangle


fig, ax = plt.subplots(figsize=(11.0, 6.2))
ax.set_xlim(0, 12)
ax.set_ylim(0, 7)
ax.axis("off")


def panel(x, title, subtitle):
    ax.add_patch(Rectangle((x, 1.2), 2.05, 4.45, facecolor="#fbfcfd", edgecolor="#c7ced8", linewidth=1.1))
    ax.text(x + 1.025, 5.35, title, ha="center", va="center", color=NAVY, fontsize=12, fontweight="bold")
    ax.text(x + 1.025, 5.0, subtitle, ha="center", va="center", fontsize=8.8, color="#333333")


def arrow(x0, y0, x1, y1):
    ax.add_patch(
        FancyArrowPatch(
            (x0, y0),
            (x1, y1),
            arrowstyle="-|>",
            mutation_scale=13,
            linewidth=1.5,
            color=NAVY,
        )
    )


def spring_vertical(x, y0, y1, amp=0.08, turns=5):
    ys = [y0]
    xs = [x]
    step = (y1 - y0) / (turns * 2)
    side = 1
    y = y0
    for _ in range(turns * 2):
        y += step
        xs.append(x + side * amp)
        ys.append(y)
        side *= -1
    xs.append(x)
    ys.append(y1)
    ax.plot(xs, ys, color=NAVY, linewidth=1.5)


def damper_vertical(x, y0, y1):
    mid = (y0 + y1) / 2
    ax.plot([x, x], [y0, mid - 0.22], color=NAVY, linewidth=1.4)
    ax.add_patch(Rectangle((x - 0.12, mid - 0.22), 0.24, 0.34, fill=False, edgecolor=NAVY, linewidth=1.3))
    ax.plot([x - 0.11, x + 0.11], [mid + 0.02, mid + 0.02], color=NAVY, linewidth=2)
    ax.plot([x, x], [mid + 0.12, y1], color=NAVY, linewidth=1.4)


def ground(x0, x1, y):
    ax.plot([x0, x1], [y, y], color=NAVY, linewidth=1.4)
    for i in range(5):
        x = x0 + (x1 - x0) * i / 4
        ax.plot([x, x - 0.08], [y, y - 0.12], color=NAVY, linewidth=1.0)


def mass(x, y, label, w=0.55, h=0.34):
    ax.add_patch(Rectangle((x - w / 2, y - h / 2), w, h, facecolor=FILL, edgecolor=NAVY, linewidth=1.4))
    ax.text(x, y, label, ha="center", va="center", fontsize=8.5)


def wheel(x, y):
    ax.add_patch(Circle((x, y), 0.09, fill=False, edgecolor=NAVY, linewidth=1.3))


def sketch_1dof(x):
    cx = x + 1.025
    mass(cx, 3.75, r"$M$", w=0.72, h=0.42)
    spring_vertical(cx - 0.18, 2.55, 3.54)
    damper_vertical(cx + 0.18, 2.55, 3.54)
    ground(cx - 0.55, cx + 0.55, 2.55)
    ax.annotate(r"$x(t)$", xy=(cx + 0.42, 3.82), xytext=(cx + 0.72, 4.25), fontsize=8.5, arrowprops=dict(arrowstyle="->", color=NAVY))
    ax.text(cx, 1.65, "body bounce", ha="center", fontsize=8.5)


def sketch_2dof(x):
    cx = x + 1.025
    mass(cx, 4.0, r"$M_1$", w=0.66, h=0.36)
    mass(cx, 2.75, r"$M_2$", w=0.58, h=0.32)
    spring_vertical(cx - 0.18, 2.94, 3.82)
    damper_vertical(cx + 0.18, 2.94, 3.82)
    spring_vertical(cx - 0.18, 2.0, 2.59)
    damper_vertical(cx + 0.18, 2.0, 2.59)
    ground(cx - 0.55, cx + 0.55, 2.0)
    ax.text(cx - 0.55, 4.18, r"$x_1$", fontsize=8.5)
    ax.text(cx - 0.55, 2.92, r"$x_2$", fontsize=8.5)
    ax.text(cx, 1.65, "body + wheel", ha="center", fontsize=8.5)


def sketch_4dof(x):
    cx = x + 1.025
    ax.add_patch(Rectangle((cx - 0.65, 3.68), 1.3, 0.38, facecolor=FILL, edgecolor=NAVY, linewidth=1.4))
    ax.text(cx, 3.87, r"$M_1,I$", ha="center", va="center", fontsize=8.5)
    for wx in [cx - 0.45, cx + 0.45]:
        mass(wx, 2.72, r"$M$", w=0.36, h=0.27)
        spring_vertical(wx, 2.88, 3.68, amp=0.055)
        spring_vertical(wx, 2.0, 2.58, amp=0.055)
    ground(cx - 0.75, cx + 0.75, 2.0)
    ax.text(cx - 0.75, 4.22, r"$x_1$", fontsize=8.5)
    ax.text(cx + 0.35, 4.22, r"$\theta$", fontsize=8.5)
    ax.text(cx, 1.65, "bounce + pitch", ha="center", fontsize=8.5)


def sketch_7dof(x):
    cx = x + 1.025
    ax.add_patch(Rectangle((cx - 0.48, 2.85), 0.96, 1.12, facecolor=FILL, edgecolor=NAVY, linewidth=1.4))
    ax.text(cx - 0.10, 3.41, "body", ha="center", va="center", fontsize=8.5)

    wheel_positions = [
        (cx - 0.68, 3.82, r"$x_2$", cx - 0.68, 3.56),
        (cx + 0.68, 3.82, r"$x_3$", cx + 0.82, 4.02),
        (cx - 0.68, 3.00, r"$x_4$", cx - 0.88, 2.90),
        (cx + 0.68, 3.00, r"$x_5$", cx + 0.88, 2.90),
    ]
    for wx, wy, label, lx, ly in wheel_positions:
        ax.add_patch(Circle((wx, wy), 0.12, facecolor="#fbfcfd", edgecolor=NAVY, linewidth=1.3))
        ax.plot([wx, cx + 0.48 * (1 if wx > cx else -1)], [wy, wy], color=NAVY, linewidth=1.1)
        ax.text(lx, ly, label, ha="center", fontsize=7.8)

    ax.annotate(r"$x_1$", xy=(cx, 4.05), xytext=(cx, 4.45), ha="center", fontsize=8.2, arrowprops=dict(arrowstyle="->", color=NAVY))
    ax.add_patch(
        FancyArrowPatch(
            (cx + 0.31, 4.04),
            (cx - 0.31, 4.04),
            connectionstyle="arc3,rad=0.34",
            arrowstyle="-|>",
            mutation_scale=10,
            linewidth=1.2,
            color=NAVY,
        )
    )
    ax.text(cx - 0.61, 4.14, r"$\phi$", fontsize=8.2)
    ax.add_patch(
        FancyArrowPatch(
            (cx + 0.60, 3.64),
            (cx + 0.60, 3.18),
            connectionstyle="arc3,rad=-0.34",
            arrowstyle="-|>",
            mutation_scale=10,
            linewidth=1.2,
            color=NAVY,
        )
    )
    ax.text(cx + 0.76, 3.40, r"$\theta$", ha="left", va="center", fontsize=8.2)
    ax.text(cx, 2.20, "body + four wheels", ha="center", fontsize=8.4)
    ax.text(cx, 1.65, "bounce, pitch, roll", ha="center", fontsize=8.5)


def sketch_fem(x):
    cx = x + 1.025
    ax.add_patch(Rectangle((cx - 0.7, 2.75), 1.4, 0.95, facecolor=FILL, edgecolor=NAVY, linewidth=1.4))
    for i in range(1, 4):
        ax.plot([cx - 0.7 + i * 0.35, cx - 0.7 + i * 0.35], [2.75, 3.7], color=NAVY, linewidth=0.7, alpha=0.7)
    for j in range(1, 3):
        ax.plot([cx - 0.7, cx + 0.7], [2.75 + j * 0.32, 2.75 + j * 0.32], color=NAVY, linewidth=0.7, alpha=0.7)
    ax.text(cx, 4.05, "flexible body", ha="center", fontsize=8.5)
    ax.text(cx, 2.25, "many nodal DOFs", ha="center", fontsize=8.5)
    ax.text(cx, 1.65, "distributed model", ha="center", fontsize=8.5)


ax.text(6, 6.55, "Car Model Hierarchy", ha="center", color=NAVY, fontsize=16, fontweight="bold")
ax.text(6, 6.15, r"Inputs: engine/transmission force $F(t)$ and road displacement $y(t)$", ha="center", fontsize=10.5, color="#333333")

xs = [0.35, 2.65, 4.95, 7.25, 9.55]
titles = [
    ("1 DOF", "bounce only"),
    ("2 DOF", "body + wheel"),
    ("4 DOF", "pitch included"),
    ("7 DOF", "roll included"),
    ("FEM", "flexibility"),
]
sketches = [sketch_1dof, sketch_2dof, sketch_4dof, sketch_7dof, sketch_fem]

for x, (title, subtitle), draw in zip(xs, titles, sketches):
    panel(x, title, subtitle)
    draw(x)

for a, b in zip(xs[:-1], xs[1:]):
    arrow(a + 2.08, 3.4, b - 0.05, 3.4)

ax.text(2.4, 0.55, "simpler, lower effort", ha="center", fontsize=10, color="#333333")
arrow(4.35, 0.6, 7.4, 0.6)
ax.text(9.0, 0.55, "more detailed, higher effort", ha="center", fontsize=10, color="#333333")

fig.savefig(OUT / "lecture2_car_model_hierarchy.png", dpi=180, bbox_inches="tight")
plt.close(fig)
