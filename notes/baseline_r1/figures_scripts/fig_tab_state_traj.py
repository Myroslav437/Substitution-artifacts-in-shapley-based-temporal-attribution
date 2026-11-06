"""Figure 4: TAB-state against TAB-traj, drawn at their estimands on DegradX's HUST profile.

(a) TAB-state pools the population: one weighted channel of all training units against their exact degradation state,
    with the shared mapping phi_c(z), the value a fine-binned TAB-state with the exact state approaches (B2*).
    The band marks the states spanned by the window of Figure 1.
(b) TAB-traj follows the unit: the same channel of the unit of Figure 1 over its life, its own mean component m (B3*,
    the value a strictly-past fit approaches) and phi_c(z_t) (B2*). Their vertical gap is the unit's offset, which B2*
    leaves to be explained and B3* removes. The shaded positions are the window; the strict past of its last position
    is everything to its left.
The estimated backgrounds (state index, bins, fit family) are not drawn, since their constants are open (Notes box).
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
    P = C.profile(PROFILE)
    spec = C.target_spec(PROFILE)
    c = spec.channels.index(CHANNEL)
    unit, t = max(C.evaluation_windows(PROFILE), key=lambda ut: ut[0].z[ut[1] - 1])   # the window of Figure 1
    train = C.units(PROFILE)["train"]

    fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(C.style.TEXTWIDTH_IN, 2.5), gridspec_kw={"width_ratios": [1.0, 1.25]})
    z_all = np.concatenate([u.z for u in train])
    x_all = np.concatenate([u.x[:, c] for u in train])
    ax_a.scatter(z_all, x_all, s=0.3, color=C.style.MEASURED_BUNDLE, lw=0, rasterized=True, label="training units")
    zg = np.linspace(0.0, 1.0, 201)
    ax_a.plot(zg, P.mappings[CHANNEL](zg), color=C.style.GENERATED, lw=C.style.LW_MAIN, label=r"$\varphi_c(z)$, estimand of TAB-state")
    zw = unit.z[t - L:t]
    ax_a.axvspan(zw.min(), zw.max(), color="0.3", alpha=0.25, lw=0, label="states of the window")
    ax_a.set_xlabel("degradation state $z$")
    ax_a.set_ylabel(f"{C.CHANNEL_LABEL[CHANNEL]} [{C.CHANNEL_UNIT[CHANNEL]}]")
    ax_a.set_title("(a) TAB-state: the population at the same state", loc="left")
    ax_a.legend(frameon=True, framealpha=0.9, edgecolor="none", loc="lower left", markerscale=12)
    C.style.despine(ax_a)

    pos = np.arange(1, t + 1)
    ax_b.plot(pos, unit.x[:t, c], color=C.style.MEASURED, lw=C.style.LW_THIN, label="observed")
    ax_b.plot(pos, unit.m[:t, c], color=C.style.GENERATED, lw=C.style.LW_MAIN, label="$m$, estimand of TAB-traj")
    ax_b.plot(pos, unit.m_state[:t, c], color=C.style.GENERATED, ls="--", lw=C.style.LW_MAIN, label=r"$\varphi_c(z_t)$, estimand of TAB-state")
    ax_b.axvspan(t - L + 1, t, color="0.3", alpha=0.25, lw=0, label="window")
    ax_b.set_xlabel("position $t$")
    ax_b.set_title("(b) TAB-traj: the unit's own past", loc="left")
    ax_b.legend(frameon=False, loc="lower left")
    C.style.despine(ax_b)
    fig.subplots_adjust(left=0.085, right=0.99, top=0.9, bottom=0.18, wspace=0.25)
    print(C.save(fig, "fig_tab_state_traj"), "unit", unit.index, "t", t, "offset", round(float(unit.m[t - 1, c] - unit.m_state[t - 1, c]), 4))


if __name__ == "__main__":
    main()
