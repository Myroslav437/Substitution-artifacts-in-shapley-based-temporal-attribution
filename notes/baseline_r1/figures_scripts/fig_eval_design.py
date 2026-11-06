"""Figure 3 (diagram): the evaluation design of Section 3.5 and the measured arms and case study of Section 3.6.

All labels are the terms and symbols of the text; profile names and window lengths come from DegradX's declarations
through _common.
"""
from __future__ import annotations

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

import _common as C

TITLE_PT, BODY_PT = 7.0, 6.2


def box(ax, x, y, w, h, title, lines):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.01", fc="white", ec="black", lw=0.7))
    ax.text(x + 0.01, y + h - 0.018, title, ha="left", va="top", fontsize=TITLE_PT, fontweight="bold")
    ax.text(x + 0.01, y + h - 0.068, "\n".join(lines), ha="left", va="top", fontsize=BODY_PT, linespacing=1.3)


def arrow(ax, p, q, label=None):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=7, lw=0.7, color="black", shrinkA=0, shrinkB=0))
    if label:
        ax.text((p[0] + q[0]) / 2, (p[1] + q[1]) / 2 + 0.015, label, fontsize=BODY_PT, color=C.style.GREY, ha="center")


def main() -> None:
    C.style.apply()
    profiles = ", ".join(C.PROFILE_FILE)
    L = C.window_length()
    L_long = max(C.declared("responsiveness.generator_settings.window_length_L"))   # D2 default
    fig, ax = plt.subplots(figsize=(C.style.TEXTWIDTH_IN, 4.1))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.set_position([0, 0, 1, 1])

    W, H = 0.2, 0.24          # synthetic boxes
    xs = (0.0, 0.225, 0.45)
    y1, y2, y3 = 0.70, 0.385, 0.03
    ax.text(0.0, 0.985, "synthetic arms: ground truth exact", fontsize=7.5, va="top", color=C.style.GREY)
    ax.text(0.69, 0.985, "measured arms and case study", fontsize=7.5, va="top", color=C.style.GREY)

    box(ax, xs[0], y1, W, H, "DegradX units", [f"profiles {profiles}", r"exact $z$, $m$, $p$, $\varepsilon$, $\varphi_c(z)$", f"$L:={L}$, 120 windows"])
    box(ax, xs[1], y1, W, H, "declared extensions", [r"$y_{\mathrm{obs}}$, $\psi(y_{\mathrm{obs}})$, $y_{\mathrm{ev}}$", "trended null channel", f"stress variants, $L:={L_long}$", "P-GEN"])
    box(ax, xs[2], y1, W, H, "model families", [r"M-obs, M-$\psi$, M-ev", "M-y, M-R", "control: boosted trees"])
    arrow(ax, (xs[0] + W, y1 + H / 2), (xs[1], y1 + H / 2))
    arrow(ax, (xs[1] + W, y1 + H / 2), (xs[2], y1 + H / 2))

    box(ax, xs[0], y2, W, H, "known function $g$", [r"$\phi^\star_b=\phi(v^g_b)$", "closed form for affine $g$", "and coalition-", "independent $b$"])
    box(ax, xs[1], y2, W, H, "backgrounds $b$", ["B0, B1, B-pristine", "B2 TAB-state", "B3 TAB-traj", r"B2c, B4; B2$^\star$, B3$^\star$"])
    box(ax, xs[2], y2, W, H, "trained models $f$", ["$A_b(f)$, TimeSHAP", "cell level, same", "coalition samples"])
    arrow(ax, (xs[1], y2 + H / 2), (xs[0] + W, y2 + H / 2))
    arrow(ax, (xs[1] + W, y2 + H / 2), (xs[2], y2 + H / 2))
    arrow(ax, (xs[2] + W / 2, y1), (xs[2] + W / 2, y2 + H))

    box(ax, xs[0], y3, 0.31, H + 0.06, "distortion and explained mass",
        [r"$D_b=A_b(f)-\phi^\star_b$", r"$\Delta_b(S)=v^f_b(S)-v^g_b(S)$", r"$\mathrm{EM}_b=|v^f_b(W)-v^f_b(\emptyset)|$", r"ensemble divergence $\mathrm{ED}_b$"])
    box(ax, 0.34, y3, 0.31, H + 0.06, "instruments",
        ["M1 null channels (A1)", "M2 retrieval by state band (A2)", "M3 pattern-free windows (A3)", "M4 signed shift against $z$ (A4)",
         "M5 carry-over vs control (A5)", "M6 coalition size (A6)", r"$\rightarrow$ RQ1, RQ2"])
    arrow(ax, (xs[0] + W / 2, y2), (xs[0] + W / 2, y3 + H + 0.06))
    arrow(ax, (xs[2] + W / 2, y2), (0.28, y3 + H + 0.06))
    arrow(ax, (0.31, y3 + 0.15), (0.34, y3 + 0.15))

    xm, wm = 0.69, 0.31
    box(ax, xm, y1, wm, H, "measured cells", [f"{profiles}", "calibrated and validated profiles", "+ two appended null channels", "M-R ensembles"])
    box(ax, xm, y2, wm, H, "without ground truth", [r"M4 centring of $f(\mathrm{mask})-f(x_W)$", "mass on null channels", r"ensemble divergence $\mathrm{ED}_b$",
                                                    r"$\rightarrow$ RQ3: generated vs measured"])
    box(ax, xm, y3, wm, H + 0.06, "case study", ["NASA PCoE", "corrected pipeline", "attention LSTM", "step 1: B1 vs published", "step 2: each background"])
    arrow(ax, (xm + wm / 2, y1), (xm + wm / 2, y2 + H))
    arrow(ax, (xs[2] + W, y1 + H * 0.3), (xm, y2 + H * 0.7), "M-R")
    ax.plot([0.67, 0.67], [0.02, 0.98], color=C.style.REFERENCE, lw=C.style.LW_THIN, ls=":")
    print(C.save(fig, "fig_eval_design"))


if __name__ == "__main__":
    main()
