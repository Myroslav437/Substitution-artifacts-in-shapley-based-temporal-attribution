#!/bin/sh
# Regenerates every figure of the paper. Requires DEGRADX_REPO (DegradX at f5bba50).
set -e
cd "$(dirname "$0")"
PY=${PYTHON:-python}
for s in fig_state_bands.py fig_toy_window.py fig_tab_state_traj.py fig_eval_design.py fig_substitution_distance.py; do
  echo "== $s"; "$PY" "$s"
done
