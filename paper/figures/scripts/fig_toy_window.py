"""Figure 2 (Section 5): one window under B1, B-pristine, B2* and B3*, and what each attribution of the reference model sums to.

Window: among DegradX's 120 evaluation windows of the HUST profile, the one whose final degradation state is largest.
(a) the observed values of one weighted channel and the substitute of each background over the window;
(b) the exact attribution of the affine reference model g under each background, sum_{u,c} w_{u,c} (x_{u,c} - b_c(u)),
    split into  w (phi(z) - b)  [mean component shared by the profile's sequences],
                w (m - phi(z))  [the sequence's departure from it: offsets and early-life reference],
                w (x - m)       [noise and inserted patterns].
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

import _common as C

PROFILE = "HUST"
CHANNEL = "mean_discharge_voltage"


def main() -> None:
    C.style.apply()
    L = C.window_length()
    spec = C.target_spec(PROFILE)
    w = spec.weights(C.WEIGHTING)                                  # (L, C)
    x0 = spec.x0                                                   # pristine reference point phi_c(0)
    b1 = C.b1(PROFILE)
    windows = C.evaluation_windows(PROFILE)
    unit, t = max(windows, key=lambda ut: ut[0].z[ut[1] - 1])      # largest final degradation state
    rows = np.arange(t - L, t)                                     # 0-based rows of positions t-L+1..t
    x, m, ms = unit.x[rows], unit.m[rows], unit.m_state[rows]
    pos = rows + 1
    c = spec.channels.index(CHANNEL)

    backgrounds = {                                                 # substitute windows (L, C)
        "B1": np.broadcast_to(b1, x.shape),
        "Bp": np.broadcast_to(x0, x.shape),
        "B2s": ms,
        "B3s": m,
    }
    # Parts of x - b that each background leaves to be explained: a constant background leaves all three; B2* removes
    # the shared mean component phi(z); B3* removes the unit's whole mean component m.
    shared, departure, noise = (w * (ms - 0)).sum(), (w * (m - ms)).sum(), (w * (x - m)).sum()
    parts = {
        "B1": ((w * (ms - backgrounds["B1"])).sum(), departure, noise),
        "Bp": ((w * (ms - backgrounds["Bp"])).sum(), departure, noise),
        "B2s": (0.0, departure, noise),
        "B3s": (0.0, 0.0, noise),
    }
    for k, b in backgrounds.items():                               # the parts add up to g(x) - g(b)
        assert np.isclose(sum(parts[k]), (w * (x - b)).sum())
    del shared

    fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(C.style.TEXTWIDTH_IN, 2.9), gridspec_kw={"width_ratios": [1.0, 1.15]})
    ax_a.plot(pos, x[:, c], color=C.style.GENERATED, lw=C.style.LW_THIN, marker="o", ms=2.2, label="observed")
    styles = {"B1": dict(ls="--"), "Bp": dict(ls=":"), "B2s": dict(ls="-", color="0.55"), "B3s": dict(ls="-.", color="0.35")}
    for k, b in backgrounds.items():
        ax_a.plot(pos, b[:, c], lw=C.style.LW_MAIN, color=styles[k].pop("color", "0.2"), **styles[k], label=C.LABEL[k])
    ax_a.set_xlabel("position $u$ in the window")
    ax_a.set_ylabel(f"{C.CHANNEL_LABEL[CHANNEL]} [{C.CHANNEL_UNIT[CHANNEL]}]")
    ax_a.set_title("(a) substitutes", loc="left")
    ax_a.legend(frameon=False, loc="upper left", bbox_to_anchor=(-0.02, -0.3), ncol=2, handlelength=2.2, columnspacing=1.0)
    C.style.despine(ax_a)

    names = ["Bp", "B1", "B2s", "B3s"]
    seg_labels = ["shared mean component", "departure of the sequence", "noise"]
    fills = ["0.25", "0.6", C.style.FILL]
    ypos = np.arange(len(names))[::-1]
    for yi, k in zip(ypos, names):
        left_pos, left_neg = 0.0, 0.0
        for j, v in enumerate(parts[k]):
            if v >= 0:
                ax_b.barh(yi, v, left=left_pos, color=fills[j], edgecolor="black", lw=0.4, height=0.6, label=seg_labels[j] if k == names[0] else None)
                left_pos += v
            else:
                ax_b.barh(yi, v, left=left_neg, color=fills[j], edgecolor="black", lw=0.4, height=0.6, label=seg_labels[j] if k == names[0] else None)
                left_neg += v
        total = sum(parts[k])
        ax_b.text(max(left_pos, 0) + 0.01 * max(abs(sum(p)) for p in parts.values()), yi, f"{total:.3f}", va="center", fontsize=7, color=C.style.GREY)
    ax_b.set_yticks(ypos, [C.LABEL[k].split(",")[0] for k in names])
    ax_b.axvline(0, color=C.style.REFERENCE, lw=C.style.LW_THIN)
    ax_b.set_xlabel(r"$g(x_W)-g(b)$  [units of the target variable]")
    ax_b.set_title("(b) sum of the exact attributions of $g$", loc="left")
    ax_b.legend(frameon=False, loc="upper left", bbox_to_anchor=(-0.02, -0.3), ncol=3, columnspacing=1.0)
    C.style.despine(ax_b)
    fig.subplots_adjust(left=0.085, right=0.98, top=0.9, bottom=0.36, wspace=0.42)
    print("window:", unit.index, "t =", t, "z_end =", round(float(unit.z[t - 1]), 4), "->", C.save(fig, "fig_toy_window"))
    for k in names:
        print(f"  {k:4s} parts={tuple(round(float(v), 4) for v in parts[k])} sum={sum(parts[k]):.4f}")


if __name__ == "__main__":
    main()
