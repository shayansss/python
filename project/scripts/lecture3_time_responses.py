#!/usr/bin/env python3
"""Figure: undamped SDOF time responses."""

from __future__ import annotations

import math

from plot_helpers import NAVY, OUT, map_points, polyline, svg_axes


m = 1.0
k = 100.0
f0 = 1.0
wn = math.sqrt(k / m)
n = 1200
t = [8.0 * i / (n - 1) for i in range(n)]


def zero_ic_response(omega: float) -> list[float]:
    return [f0 / (k - m * omega**2) * (math.cos(omega * ti) - math.cos(wn * ti)) for ti in t]


panels = [
    ("Off resonance", zero_ic_response(0.60 * wn)),
    ("Near resonance: beating", zero_ic_response(0.92 * wn)),
    ("Exact resonance: growing envelope", [f0 / (2 * m * wn) * ti * math.sin(wn * ti) for ti in t]),
]

svg = [
    '<svg xmlns="http://www.w3.org/2000/svg" width="900" height="640" viewBox="0 0 900 640">',
    '<rect width="900" height="640" fill="#fbfcfd"/>',
    f'<text x="450" y="34" text-anchor="middle" font-size="22" font-weight="700" fill="{NAVY}">Undamped SDOF Time Responses</text>',
]

for i, (title, yvals) in enumerate(panels):
    box = (90, 70 + i * 175, 760, 125)
    svg.append(svg_axes(*box, title=title))
    svg.append(polyline(map_points(t, yvals, box)))

svg.append('<text x="450" y="620" text-anchor="middle" font-size="14" fill="#333">t</text>')
svg.append("</svg>")
(OUT / "lecture3_time_responses.svg").write_text("\n".join(svg), encoding="utf-8")
