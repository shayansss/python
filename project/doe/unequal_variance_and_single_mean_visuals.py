from pathlib import Path
from statistics import NormalDist

import os

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib")

import matplotlib.pyplot as plt
import numpy as np


OUTPUT_DIR = Path(__file__).resolve().parent / "images"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

NAVY = "#17324d"
TEAL = "#147d78"
ORANGE = "#e58b2a"
RED = "#bd3f43"
LIGHT_BLUE = "#dceaf2"
LIGHT_ORANGE = "#f8e7cf"
GRID = "#d9dee3"


def normal_pdf(x):
    return np.exp(-(x**2) / 2) / np.sqrt(2 * np.pi)


def save_welch_visual():
    nerve = np.array(
        [6625, 6000, 5450, 5200, 5175, 4900, 4750, 4500, 3985, 900, 450, 2800],
        dtype=float,
    )
    muscle = np.array(
        [3900, 3500, 3450, 3200, 2980, 2800, 2500, 2400, 2200, 1200, 1150, 1130],
        dtype=float,
    )

    n1, n2 = len(nerve), len(muscle)
    mean1, mean2 = nerve.mean(), muscle.mean()
    sd1, sd2 = nerve.std(ddof=1), muscle.std(ddof=1)
    difference = mean1 - mean2
    standard_error = np.sqrt(sd1**2 / n1 + sd2**2 / n2)
    t_value = difference / standard_error
    df = (sd1**2 / n1 + sd2**2 / n2) ** 2 / (
        (sd1**2 / n1) ** 2 / (n1 - 1) + (sd2**2 / n2) ** 2 / (n2 - 1)
    )

    fig = plt.figure(figsize=(14, 8.2), dpi=180, facecolor="white")
    grid = fig.add_gridspec(
        2,
        2,
        height_ratios=[1.2, 0.8],
        width_ratios=[1.2, 1],
        hspace=0.46,
        wspace=0.32,
    )

    ax_data = fig.add_subplot(grid[0, 0])
    rng = np.random.default_rng(21)
    positions = [1, 0]
    for values, position, color in [
        (nerve, positions[0], TEAL),
        (muscle, positions[1], ORANGE),
    ]:
        jitter = rng.normal(0, 0.045, len(values))
        ax_data.scatter(
            values,
            position + jitter,
            s=58,
            color=color,
            edgecolor="white",
            linewidth=0.8,
            zorder=3,
        )

    box = ax_data.boxplot(
        [muscle, nerve],
        positions=[0, 1],
        vert=False,
        widths=0.46,
        patch_artist=True,
        showfliers=False,
        medianprops={"color": NAVY, "linewidth": 2},
        boxprops={"linewidth": 1.2},
        whiskerprops={"linewidth": 1.2},
        capprops={"linewidth": 1.2},
    )
    for patch, color in zip(box["boxes"], [ORANGE, TEAL]):
        patch.set_facecolor(color)
        patch.set_alpha(0.18)

    ax_data.set_yticks([0, 1], ["Muscle", "Nerve"])
    ax_data.set_xlabel("Normalized fluorescence after two hours")
    ax_data.set_title("Observed values and spread", color=NAVY, fontweight="bold")
    ax_data.grid(axis="x", color=GRID, linewidth=0.8)
    ax_data.set_axisbelow(True)
    ax_data.text(
        0.99,
        0.97,
        f"Nerve: mean = {mean1:.0f}, s = {sd1:.0f}\n"
        f"Muscle: mean = {mean2:.0f}, s = {sd2:.0f}\n"
        f"SD ratio = {sd1 / sd2:.2f}",
        transform=ax_data.transAxes,
        ha="right",
        va="top",
        fontsize=10,
        color=NAVY,
        bbox={"facecolor": "white", "edgecolor": GRID, "boxstyle": "round,pad=0.4"},
    )

    ax_prob = fig.add_subplot(grid[0, 1])
    probabilities = (np.arange(1, n1 + 1) - 0.5) / n1
    normal_scores = np.array([NormalDist().inv_cdf(p) for p in probabilities])

    for values, color, label in [
        (nerve, TEAL, "Nerve"),
        (muscle, ORANGE, "Muscle"),
    ]:
        ordered = np.sort(values)
        slope, intercept = np.polyfit(normal_scores, ordered, 1)
        ax_prob.scatter(normal_scores, ordered, s=48, color=color, label=label, zorder=3)
        ax_prob.plot(
            normal_scores,
            intercept + slope * normal_scores,
            color=color,
            linewidth=2,
            alpha=0.85,
        )

    ax_prob.set_xlabel("Theoretical normal quantile")
    ax_prob.set_ylabel("Ordered fluorescence")
    ax_prob.set_title("Normal probability comparison", color=NAVY, fontweight="bold")
    ax_prob.grid(color=GRID, linewidth=0.8)
    ax_prob.set_axisbelow(True)
    ax_prob.legend(frameon=False, loc="upper left")
    ax_prob.text(
        0.03,
        0.03,
        "Both trends are roughly linear,\nbut their slopes differ strongly.",
        transform=ax_prob.transAxes,
        va="bottom",
        fontsize=10,
        color=NAVY,
        bbox={"facecolor": "white", "edgecolor": GRID, "boxstyle": "round,pad=0.4"},
    )

    ax_result = fig.add_subplot(grid[1, :])
    ax_result.axis("off")
    ax_result.add_patch(
        plt.Rectangle(
            (0.015, 0.08),
            0.97,
            0.82,
            transform=ax_result.transAxes,
            facecolor="#f7f9fa",
            edgecolor=GRID,
            linewidth=1.1,
        )
    )
    ax_result.text(
        0.04,
        0.77,
        "Welch's unequal-variance t-test",
        transform=ax_result.transAxes,
        fontsize=14,
        fontweight="bold",
        color=NAVY,
    )
    ax_result.text(
        0.04,
        0.51,
        "H0: mu_nerve = mu_muscle     H1: mu_nerve > mu_muscle",
        transform=ax_result.transAxes,
        fontsize=12,
        color=NAVY,
    )
    ax_result.text(
        0.04,
        0.25,
        f"Difference = {difference:.0f}     SE = {standard_error:.1f}     "
        f"t = {t_value:.3f}     df = {df:.2f}",
        transform=ax_result.transAxes,
        fontsize=12,
        color=NAVY,
    )
    ax_result.text(
        0.70,
        0.49,
        "One-sided P = 0.007",
        transform=ax_result.transAxes,
        fontsize=16,
        fontweight="bold",
        color=RED,
        ha="center",
    )
    ax_result.text(
        0.70,
        0.25,
        "Evidence that mean nerve fluorescence is greater",
        transform=ax_result.transAxes,
        fontsize=11,
        color=NAVY,
        ha="center",
    )

    fig.suptitle(
        "Nerve vs. Muscle Fluorescence: Why the Pooled t-Test Is Inappropriate",
        fontsize=17,
        fontweight="bold",
        color=NAVY,
        y=0.98,
    )
    fig.savefig(OUTPUT_DIR / "nerve_muscle_welch_test.png", bbox_inches="tight")
    plt.close(fig)


def save_single_mean_visual():
    mu0 = 200
    sample_mean = 214
    variance = 100
    sigma = np.sqrt(variance)
    sample_size = 4
    standard_error = sigma / np.sqrt(sample_size)
    z_value = (sample_mean - mu0) / standard_error
    critical = 1.645
    p_value = 1 - NormalDist().cdf(z_value)

    fig = plt.figure(figsize=(14, 7.8), dpi=180, facecolor="white")
    grid = fig.add_gridspec(
        2,
        2,
        height_ratios=[1, 0.78],
        width_ratios=[1.08, 1],
        hspace=0.4,
        wspace=0.28,
    )

    ax_choice = fig.add_subplot(grid[0, 0])
    ax_choice.axis("off")
    ax_choice.set_title("Choose the reference distribution", color=NAVY, fontweight="bold", pad=12)

    rows = [
        ["Population SD", "Known", "Unknown"],
        ["Statistic", "z = difference\n/ known SE", "t = difference\n/ estimated SE"],
        ["Reference", "Standard normal", "t with n - 1 df"],
        ["Two-sided CI", "ybar +/- z* SE", "ybar +/- t* SE"],
    ]
    table = ax_choice.table(
        cellText=rows,
        cellLoc="left",
        colWidths=[0.25, 0.36, 0.39],
        loc="center",
        bbox=[0.0, 0.02, 1.0, 0.87],
    )
    table.auto_set_font_size(False)
    table.set_fontsize(9.5)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("white")
        cell.set_linewidth(2)
        cell.set_facecolor(LIGHT_BLUE if col == 1 else LIGHT_ORANGE if col == 2 else "#eef1f3")
        if col == 0:
            cell.set_text_props(weight="bold", color=NAVY)

    ax_curve = fig.add_subplot(grid[0, 1])
    x = np.linspace(-3.8, 3.8, 900)
    density = normal_pdf(x)
    ax_curve.plot(x, density, color=NAVY, linewidth=2.2)
    ax_curve.fill_between(
        x,
        0,
        density,
        where=x >= critical,
        color=RED,
        alpha=0.28,
        label="Reject H0 at alpha = 0.05",
    )
    ax_curve.axvline(critical, color=RED, linestyle="--", linewidth=1.8)
    ax_curve.axvline(z_value, color=TEAL, linewidth=2.5)
    ax_curve.annotate(
        f"Observed z = {z_value:.2f}",
        xy=(z_value, normal_pdf(z_value)),
        xytext=(1.35, 0.22),
        arrowprops={"arrowstyle": "->", "color": TEAL, "linewidth": 1.5},
        color=TEAL,
        fontsize=11,
        fontweight="bold",
    )
    ax_curve.set_xlim(-3.8, 3.8)
    ax_curve.set_ylim(0, 0.43)
    ax_curve.set_yticks([])
    ax_curve.set_xticks(
        [-3, -2, -1, 0, 1, critical, z_value],
        ["-3", "-2", "-1", "0", "1", "1.645", "2.80"],
    )
    ax_curve.set_xlabel("Standard normal test statistic")
    ax_curve.set_title("Fabric example: upper-tail Z-test", color=NAVY, fontweight="bold")
    ax_curve.spines[["left", "right", "top"]].set_visible(False)
    ax_curve.legend(frameon=False, loc="upper left")

    ax_result = fig.add_subplot(grid[1, :])
    ax_result.axis("off")
    ax_result.add_patch(
        plt.Rectangle(
            (0.015, 0.08),
            0.97,
            0.82,
            transform=ax_result.transAxes,
            facecolor="#f7f9fa",
            edgecolor=GRID,
            linewidth=1.1,
        )
    )
    ax_result.text(
        0.04,
        0.75,
        "Breaking-strength acceptance test",
        transform=ax_result.transAxes,
        fontsize=14,
        fontweight="bold",
        color=NAVY,
    )
    ax_result.text(
        0.04,
        0.47,
        "H0: mu = 200 psi     H1: mu > 200 psi",
        transform=ax_result.transAxes,
        fontsize=12,
        color=NAVY,
    )
    ax_result.text(
        0.04,
        0.22,
        f"n = {sample_size}     ybar = {sample_mean}     sigma = {sigma:.0f}     "
        f"SE = {standard_error:.0f}     z = ({sample_mean} - {mu0})/{standard_error:.0f} = {z_value:.2f}",
        transform=ax_result.transAxes,
        fontsize=12,
        color=NAVY,
    )
    ax_result.text(
        0.76,
        0.48,
        f"P = {p_value:.5f}",
        transform=ax_result.transAxes,
        fontsize=16,
        fontweight="bold",
        color=RED,
        ha="center",
    )
    ax_result.text(
        0.76,
        0.23,
        "Reject H0: mean strength exceeds 200 psi",
        transform=ax_result.transAxes,
        fontsize=11,
        color=NAVY,
        ha="center",
    )

    fig.suptitle(
        "Inference on a Single Population Mean",
        fontsize=17,
        fontweight="bold",
        color=NAVY,
        y=0.98,
    )
    fig.savefig(OUTPUT_DIR / "single_mean_inference.png", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    save_welch_visual()
    save_single_mean_visual()
