"""Figure 2 (schematic): state bands of A1 and A2 for an unconditional background b.

The curves are analytic shapes drawn for illustration only (no data, no tick values): (a) a monotone mean component,
(b) the same component with a slow periodic part added, so that it is not monotone in position. The near band is where
the mean component lies close to b, the far band where it lies far from it; shading on the position axis shows where
each band falls.
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

import _common as C


def bands(ax, u, m, b, near, far, title):
    ax.plot(u, m, color=C.style.GENERATED, lw=C.style.LW_MAIN, label="mean component $m(u)$")
    ax.axhline(b, color="0.2", ls="--", lw=C.style.LW_THIN, label="background $b$")
    ax.axhspan(b - near, b + near, color=C.style.FILL, alpha=0.8, lw=0)
    d = np.abs(m - b)
    y0 = m.min() - 0.18 * (m.max() - m.min())       # strip below the curve that marks the bands on the position axis
    ax.fill_between(u, y0, y0 + 0.06 * (m.max() - m.min()), where=d <= near, color="0.55", lw=0, step="mid", label="near band")
    ax.fill_between(u, y0, y0 + 0.06 * (m.max() - m.min()), where=d >= far, color="0.15", lw=0, step="mid", label="far band")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel("position $u$")
    ax.set_title(title, loc="left")
    C.style.despine(ax)


def main() -> None:
    C.style.apply()
    u = np.linspace(0.0, 1.0, 600)
    mono = 1.0 - u ** 1.6                       # schematic monotone shape
    nonmono = mono + 0.22 * np.sin(2 * np.pi * 2.5 * u)
    b = mono.mean()
    near, far = 0.06, 0.30
    fig, axes = plt.subplots(1, 2, figsize=(C.style.TEXTWIDTH_IN, 2.0), sharey=True)
    bands(axes[0], u, mono, b, near, far, "(a) monotone mean component")
    bands(axes[1], u, nonmono, b, near, far, "(b) non-monotone mean component")
    axes[0].set_ylabel("value (schematic)")
    h, lab = axes[0].get_legend_handles_labels()
    fig.legend(h, lab, frameon=False, loc="lower center", ncol=4, bbox_to_anchor=(0.5, -0.02))
    fig.subplots_adjust(left=0.06, right=0.99, top=0.88, bottom=0.27, wspace=0.08)
    print(C.save(fig, "fig_state_bands"))


if __name__ == "__main__":
    main()
