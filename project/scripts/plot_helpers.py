"""Shared helpers for lecture-note figure generation."""

from __future__ import annotations

import os
from pathlib import Path


os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib")
OUT = Path(__file__).resolve().parent
OUT.mkdir(exist_ok=True)

NAVY = "#08255c"
GRID = "#d9dfe8"
PANEL_STROKE = "#c7ced8"
TEXT = "#333333"
INK = "#111111"
MUTED = "#333333"
FILL = "#eef4fb"
RED = "#c62828"


def configure_matplotlib_cache() -> None:
    os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib")


def polyline(points: list[tuple[float, float]], color: str = NAVY, width: float = 2.0) -> str:
    value = " ".join(f"{x:.2f},{y:.2f}" for x, y in points)
    return f'<polyline points="{value}" fill="none" stroke="{color}" stroke-width="{width}" />'


def map_points(xs: list[float], ys: list[float], box: tuple[int, int, int, int]) -> list[tuple[float, float]]:
    x0, y0, w, h = box
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    pad = 0.08 * (ymax - ymin or 1.0)
    ymin -= pad
    ymax += pad

    mapped = []
    for x, y in zip(xs, ys):
        px = x0 + (x - xmin) / (xmax - xmin) * w
        py = y0 + h - (y - ymin) / (ymax - ymin) * h
        mapped.append((px, py))
    return mapped


def svg_axes(x: int, y: int, w: int, h: int, title: str, ylabel: str = "x(t)") -> str:
    return f"""
    <rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#ffffff" stroke="{PANEL_STROKE}" />
    <line x1="{x}" y1="{y + h / 2}" x2="{x + w}" y2="{y + h / 2}" stroke="{GRID}" />
    <text x="{x + 8}" y="{y + 18}" font-size="14" font-weight="700" fill="{NAVY}">{title}</text>
    <text x="{x - 42}" y="{y + h / 2}" font-size="12" fill="{TEXT}">{ylabel}</text>
    """


def canvas(width=9, height=4.8, title=""):
    configure_matplotlib_cache()
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(width, height))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    if title:
        ax.text(5, 5.75, title, ha="center", va="center", color=NAVY, fontsize=16, fontweight="bold")
    return fig, ax


def save_figure(fig, name: str):
    import matplotlib.pyplot as plt

    fig.savefig(OUT / name, dpi=180, bbox_inches="tight")
    plt.close(fig)


def box(ax, xy, w, h, title, subtitle="", fc="white"):
    from matplotlib.patches import Rectangle

    x, y = xy
    ax.add_patch(Rectangle((x, y), w, h, facecolor=fc, edgecolor=NAVY, linewidth=1.8))
    ax.text(x + w / 2, y + h * 0.62, title, ha="center", va="center", color=NAVY, fontsize=10, fontweight="bold")
    if subtitle:
        ax.text(x + w / 2, y + h * 0.30, subtitle, ha="center", va="center", color=MUTED, fontsize=8)


def arrow(ax, start, end, dashed=False):
    from matplotlib.patches import FancyArrowPatch

    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=14,
            linewidth=1.7,
            color=NAVY,
            linestyle="--" if dashed else "-",
        )
    )


def draw_spring(ax, x0, x1, y, amp=0.25, turns=7):
    xs = [x0]
    ys = [y]
    lead = 0.35
    x = x0 + lead
    xs.append(x)
    ys.append(y)
    pitch = (x1 - x0 - 2 * lead) / (turns * 2)
    sign = 1
    for _ in range(turns * 2):
        x += pitch
        xs.append(x)
        ys.append(y + sign * amp)
        sign *= -1
    xs += [x1 - lead, x1]
    ys += [y, y]
    ax.plot(xs, ys, color=NAVY, linewidth=2)


def draw_damper(ax, x0, x1, y, scale=1.0):
    from matplotlib.patches import Rectangle

    mid = (x0 + x1) / 2
    h = 0.35 * scale
    ax.plot([x0, mid - 0.55], [y, y], color=NAVY, linewidth=2)
    ax.add_patch(Rectangle((mid - 0.55, y - h), 0.75, 2 * h, fill=False, edgecolor=NAVY, linewidth=2))
    ax.plot([mid - 0.10, mid - 0.10], [y - h * 0.8, y + h * 0.8], color=NAVY, linewidth=3)
    ax.plot([mid + 0.20, x1], [y, y], color=NAVY, linewidth=2)


def draw_ground(ax, x0, x1, y):
    ax.plot([x0, x1], [y, y], color=NAVY, linewidth=2)
    for i in range(8):
        x = x0 + (x1 - x0) * i / 7
        ax.plot([x, x - 0.18], [y, y - 0.25], color=NAVY, linewidth=1)


def draw_mass(ax, center, label, w=0.9, h=0.55):
    from matplotlib.patches import Rectangle

    x, y = center
    ax.add_patch(Rectangle((x - w / 2, y - h / 2), w, h, facecolor=FILL, edgecolor=NAVY, linewidth=1.8))
    ax.text(x, y, label, ha="center", va="center", fontsize=11, color=INK)
