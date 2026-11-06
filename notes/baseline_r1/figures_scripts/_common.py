"""Shared access to DegradX for the figure scripts of Sections 1-3.

Every number in a figure comes from DegradX (declarations, fitted profiles, generator, committed split tables)
or from the definitions in the paper; nothing is typed by hand.

DegradX must be available as a clone of github.com/Myroslav437/degradx at commit f5bba50; its path is read from the
environment variable DEGRADX_REPO. Figures are written to the paper's media/ folder.
"""
from __future__ import annotations

import os
import sys
from functools import lru_cache
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
PAPER_DIR = HERE.parents[1] / "_arXiv__Substitution_Artifacts_in_Shapley_Based_Temporal_Attribution"
MEDIA = PAPER_DIR / "media"
DEGRADX_COMMIT = "f5bba50"

REPO = Path(os.environ.get("DEGRADX_REPO", "")).resolve() if os.environ.get("DEGRADX_REPO") else None
if REPO is None or not (REPO / "src" / "degradx").is_dir():
    sys.exit("Set DEGRADX_REPO to a clone of github.com/Myroslav437/degradx at commit f5bba50.")
sys.path.insert(0, str(REPO / "src"))

import yaml  # noqa: E402
import pandas as pd  # noqa: E402

from degradx.generator.generate import Profile, generate_unit  # noqa: E402
from degradx.targets.decomposable import TargetSpec  # noqa: E402
from degradx.utils.seeding import rng  # noqa: E402
from degradx.viz import style  # noqa: E402

# Profile names of the paper and of the DegradX artifacts
PROFILE_FILE = {"MATR": "MATR", "HUST": "HUST", "FORM": "TRI_FORMATION"}
GENERATION_SEED = 0          # the generation seed of DegradX's models (DegradX §4)
WEIGHTING = "recency"        # DegradX's primary weighting

# Labels used in the text (Section 3.4, Table 2); figures use exactly these strings.
LABEL = {
    "B0": "B0", "B1": "B1", "Bp": "B-pristine",
    "B2": "B2, TAB-state", "B3": "B3, TAB-traj", "B2c": "B2c", "B4": "B4",
    "B2s": r"B2$^\star$, TAB-state with exact state", "B3s": r"B3$^\star$, TAB-traj with exact mean component",
}
CHANNEL_LABEL = {"capacity": "capacity", "charge_time": "charge time", "mean_discharge_voltage": "mean discharge voltage"}
CHANNEL_UNIT = {"capacity": "Ah", "charge_time": "min", "mean_discharge_voltage": "V"}


@lru_cache(maxsize=None)
def declarations() -> dict:
    with open(REPO / "configs" / "declarations.yaml", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def declared(dotted: str):
    node = declarations()["declared_by_design"]
    for part in dotted.split("."):
        node = node[part]
    return node


def window_length() -> int:
    return int(declared("target.window_length_L.value"))


def base_seed() -> int:
    """DegradX's base seed: the default of its stage command line, from which every random stream derives."""
    import inspect
    from degradx.utils import cli
    return int(inspect.signature(cli.stage_parser).parameters["default_seed"].default)


@lru_cache(maxsize=None)
def profile(name: str) -> Profile:
    """Fitted profile with offsets (stage s09). The null_permuted channel needs measured charge-time readings, which
    DegradX does not commit; a placeholder pool is passed. It changes only that null channel: every other channel draws
    from its own seeded stream, so the measured channels of the units are those DegradX generates."""
    import json
    prof = json.loads((REPO / "artifacts" / "s09_fit_profiles" / "profiles" / f"{PROFILE_FILE[name]}.json").read_text())
    return Profile.from_json(prof, np.array([0.0]))


@lru_cache(maxsize=None)
def split_table(name: str) -> pd.DataFrame:
    return pd.read_csv(REPO / "artifacts" / "s10_generate_units" / "tables" / f"generated_units_{PROFILE_FILE[name]}_seed{GENERATION_SEED}.csv")


@lru_cache(maxsize=None)
def units(name: str) -> dict:
    """Generated units of the profile at DegradX's generation seed, keyed by split, in DegradX's unit order."""
    P, tab = profile(name), split_table(name)
    out = {"train": [], "validation": [], "test": []}
    for idx, sp in zip(tab["index"], tab["split"]):
        u = generate_unit(P, GENERATION_SEED, int(idx))
        assert u is not None and u.T == int(tab.loc[tab["index"] == idx, "T"].iloc[0]), "unit differs from DegradX's table"
        out[sp].append(u)
    return out


def target_spec(name: str) -> TargetSpec:
    beta = declared("target.weights.beta.value")
    L = window_length()
    return TargetSpec.build(profile(name), beta, L, L / 4)   # half-life h := L/4 (DegradX §3.2.1)


def evaluation_windows(name: str) -> list[tuple]:
    """DegradX's reference-value window rule (scripts/s15_reference_values.py, select_windows): stratified across
    test units, drawn with the evaluation stream of the base seed. Returns (unit, end position t)."""
    L = window_length()
    n = int(declared("attribution.windows_scored_per_profile"))
    g = rng(base_seed(), "evaluation", "s8", PROFILE_FILE[name])
    eligible = [u for u in units(name)["test"] if u.T >= L]
    per = int(np.ceil(n / len(eligible)))
    picks = []
    for ui, u in enumerate(eligible):
        ends = np.arange(L, u.T + 1)
        for e in np.sort(g.choice(ends, size=min(per, len(ends)), replace=False)):
            picks.append((ui, int(e)))
    idx = np.sort(g.choice(len(picks), size=min(n, len(picks)), replace=False))
    return [(eligible[picks[i][0]], picks[i][1]) for i in idx]


def b1(name: str) -> np.ndarray:
    """B1: per-channel mean over all positions of the training units (decision D3: the mean)."""
    tr = units(name)["train"]
    return np.concatenate([u.x for u in tr], axis=0).mean(axis=0)


def save(fig, stem: str) -> Path:
    MEDIA.mkdir(parents=True, exist_ok=True)
    path = MEDIA / f"{stem}.pdf"
    fig.savefig(path)
    return path
