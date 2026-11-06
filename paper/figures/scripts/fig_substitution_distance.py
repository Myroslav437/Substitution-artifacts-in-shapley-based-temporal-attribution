"""Figure 5 (descriptive, input data only): how far the unconditional backgrounds lie from the population at each state.

For every DegradX profile and weighted channel c, the training sequences of generation seed 0 are binned by their exact
degradation state z. In each bin, mu_c(z) and sigma_c(z) are the mean and standard deviation of the channel over the
positions in the bin (the state-conditional mean and spread of the paper's Equation for the stationarity assumption).
The figure shows the systematic substitution distance of an unconditional background b, |mu_c(z) - b_c|, in units of
sigma_c(z), for B1 (per-channel training mean) and B-pristine (the pristine reference point x0_c = phi_c(0)).

No attribution is computed: the figure describes the input data of the testbed.
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

import _common as C

N_BINS = 40           # equal-width bins of the exact degradation state on [0, 1]
MIN_COUNT = 50        # bins with fewer training positions are not drawn


def binned(name: str):
    P = C.profile(name)
    spec = C.target_spec(name)
    train = C.units(name)["train"]
    z = np.concatenate([u.z for u in train])
    x = np.concatenate([u.x for u in train], axis=0)                   # (N, C), all channels
    b1 = x.mean(axis=0)                                                 # B1 (decision D3: the mean); = C.b1(name)
    assert np.allclose(b1, C.b1(name))
    x0 = spec.x0                                                        # B-pristine
    edges = np.linspace(0.0, 1.0, N_BINS + 1)
    k = np.clip(np.digitize(z, edges) - 1, 0, N_BINS - 1)
    centres, out = [], {c: {"B1": [], "Bp": []} for c in P.weighted}
    for j in range(N_BINS):
        sel = k == j
        if sel.sum() < MIN_COUNT:
            continue
        centres.append(0.5 * (edges[j] + edges[j + 1]))
        for c in P.weighted:
            ci = spec.channels.index(c)
            mu, sd = x[sel, ci].mean(), x[sel, ci].std(ddof=1)
            out[c]["B1"].append(abs(mu - b1[ci]) / sd)
            out[c]["Bp"].append(abs(mu - x0[ci]) / sd)
    return np.array(centres), out, list(P.weighted)


def main() -> None:
    C.style.apply()
    fig, axes = plt.subplots(1, 3, figsize=(C.style.TEXTWIDTH_IN, 2.3), sharey=False)
    greys = ["black", "0.45", "0.7"]
    for ax, name in zip(axes, C.PROFILE_FILE):
        zc, out, chans = binned(name)
        for g, c in zip(greys, chans):
            ax.plot(zc, out[c]["B1"], color=g, lw=C.style.LW_MAIN, ls="-", label=f"{C.CHANNEL_LABEL[c]}, B1")
            ax.plot(zc, out[c]["Bp"], color=g, lw=C.style.LW_MAIN, ls="--", label=f"{C.CHANNEL_LABEL[c]}, {C.LABEL['Bp']}")
        ax.axhline(1.0, color=C.style.REFERENCE, lw=C.style.LW_THIN, ls=":")
        ax.set_yscale("log")
        ax.set_xlim(0, 1)
        ax.set_xlabel("degradation state $z$")
        ax.set_title(name, loc="left")
        C.style.despine(ax)
        print(name, {c: (round(float(np.min(out[c]["B1"])), 3), round(float(np.max(out[c]["B1"])), 2),
                         round(float(np.min(out[c]["Bp"])), 3), round(float(np.max(out[c]["Bp"])), 2)) for c in chans})
    axes[0].set_ylabel(r"$|\mu_c(z)-b_c|\,/\,\sigma_c(z)$")
    h, lab = axes[0].get_legend_handles_labels()
    fig.legend(h, lab, frameon=False, loc="lower center", ncol=3, bbox_to_anchor=(0.5, -0.01), columnspacing=1.2, handlelength=2.4)
    fig.subplots_adjust(left=0.08, right=0.99, top=0.9, bottom=0.37, wspace=0.28)
    print(C.save(fig, "fig_substitution_distance"))


if __name__ == "__main__":
    main()
