from pathlib import Path

import os

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib")

import matplotlib.pyplot as plt
import numpy as np


OUTPUT_DIR = Path(__file__).resolve().parent / "images"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

POWER_LEVELS = np.array([160, 180, 200, 220])
ETCH_RATES = np.array(
    [
        [575, 542, 530, 539, 570],
        [565, 593, 590, 579, 610],
        [600, 651, 610, 637, 629],
        [725, 700, 715, 685, 710],
    ],
    dtype=float,
)

NAVY = "#17324d"
TEAL = "#147d78"
ORANGE = "#e58b2a"
GRID = "#d9dee3"


def save_plasma_etch_visual() -> None:
    means = ETCH_RATES.mean(axis=1)

    fig, axes = plt.subplots(1, 2, figsize=(13, 5.8), dpi=180, facecolor="white")

    box = axes[0].boxplot(
        [row for row in ETCH_RATES],
        tick_labels=[str(level) for level in POWER_LEVELS],
        patch_artist=True,
        widths=0.55,
        medianprops={"color": NAVY, "linewidth": 2},
        whiskerprops={"color": NAVY, "linewidth": 1.2},
        capprops={"color": NAVY, "linewidth": 1.2},
        boxprops={"color": TEAL, "linewidth": 1.2},
    )
    for patch in box["boxes"]:
        patch.set_facecolor(TEAL)
        patch.set_alpha(0.2)

    axes[0].set_title("Comparative box plots", color=NAVY, fontweight="bold")
    axes[0].set_xlabel("RF power (W)")
    axes[0].set_ylabel("Etch rate (Å/min)")
    axes[0].grid(axis="y", color=GRID, linewidth=0.8)
    axes[0].set_axisbelow(True)

    offsets = np.linspace(-2.8, 2.8, ETCH_RATES.shape[1])
    for power, values in zip(POWER_LEVELS, ETCH_RATES):
        axes[1].scatter(
            power + offsets,
            values,
            s=54,
            color=TEAL,
            edgecolor="white",
            linewidth=0.8,
            zorder=3,
        )

    axes[1].plot(
        POWER_LEVELS,
        means,
        color=ORANGE,
        marker="D",
        markersize=6,
        linewidth=2.2,
        label="Treatment mean",
        zorder=4,
    )
    for power, mean in zip(POWER_LEVELS, means):
        axes[1].annotate(
            f"{mean:.1f}",
            (power, mean),
            xytext=(0, 10),
            textcoords="offset points",
            ha="center",
            color=NAVY,
            fontsize=9,
        )

    axes[1].set_title("Individual observations and means", color=NAVY, fontweight="bold")
    axes[1].set_xlabel("RF power (W)")
    axes[1].set_ylabel("Etch rate (Å/min)")
    axes[1].set_xticks(POWER_LEVELS)
    axes[1].grid(color=GRID, linewidth=0.8)
    axes[1].set_axisbelow(True)
    axes[1].legend(frameon=False, loc="upper left")

    fig.suptitle(
        "Plasma Etching Experiment: Etch Rate by RF Power",
        fontsize=16,
        fontweight="bold",
        color=NAVY,
        y=1.01,
    )
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "plasma_etch_anova.png", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    save_plasma_etch_visual()
