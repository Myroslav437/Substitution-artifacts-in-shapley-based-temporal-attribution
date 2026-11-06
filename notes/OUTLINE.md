# OUTLINE — revision 2 (authors' comments of 2026-11-05)

Structure of brief rev. 2 §3, with one change of order inside §6 (logged in CHANGELOG, C13): the principle of the evaluation (ground truth per background, ensemble divergence, test of the thesis) comes first, then the testbed, so that each DegradX result is stated where it motivates a choice (C11). Keys refer to `references.bib`; DX = degradx2026, DXR = degradxrepo, ACIIDS = mishchuk2026explaining. Terms: sequence (not unit), element (not cell), population (not fleet), state (not degradation state) outside the DegradX parts (C12).

The revision-1 outline is preserved in `notes/baseline_r1/notes_r1/OUTLINE_r1.md`; this file replaces it.

## Abstract (≤ 250 words, EAAI; no citations; no acronyms, since EAAI forbids undefined ones)
Most used family → removal by substitution → the background treats the data as mean-stationary although the model reads the state → off-support evaluation → six artifacts with instruments (introduced) → trend-aware backgrounds (state from the past, no generative model) → evaluation: models trained to reproduce a known function on a testbed calibrated to three battery datasets; distortion (introduced) separated from removed information → three result placeholders, each with "indicating that" → practical use (AI contribution vs engineering application, EAAI rule).

## 1 Introduction (1.5–2 pp.) — one argument
1. SHAP is the most used attribution family [cummins2024explainable: "by far" most used, 102 PdM studies; saarela2024recent: most common of 512 XAI applications, about a third; arabzadeh2025four: post hoc methods, SHAP in particular, dominate energy time-series forecasting]. TimeSHAP carries it to sequences [lundberg2017unified, bento2021timeshap]; importance by removal; removal = substitution by a background.
2. The background is left to the user [bento2021timeshap; nguyen2025tshap: understudied; kim2026groupsegment, papadeas2026empirical: sensitivity]. Beyond sensitivity, the background fixes which quantity is explained (efficiency) [sundararajan2020many; merrick2020explanation, mamalakis2023carefully].
3. Under mean-nonstationarity the substitution error is systematic (C6): substitution distance, its systematic part |m − b|, unconditional b constant while m moves with the state; coalitions combine values of different states → off support; the training data do not constrain f there; off-manifold Shapley values can be incorrect and differ between models that agree on the data [frye2021shapley]; trend → out-of-domain counterfactuals [tonekaboni2020went]. The response enters the attribution: artifact classes magnitude / meaning / propagation. The problem cannot be avoided: the mean component carries most target-relevant information [DX]; detrending as argument (different model; off-support again; removes the signal).
4. Thesis inline, \emph (C9): a single substitute is optimal only under mean-stationarity; the model reads the state. Stated formally and tested, not proven.
5. Characterization: to our knowledge not done (novelty record §3 of REFERENCES_AUDIT); six artifacts, each with signature and instrument.
6. Solution: TAB conditions the substitute on a low-dimensional state estimated from the past (TAB-state, TAB-traj), no generative model; learned imputer as established reference [frye2021shapley, chang2019explaining].
7. Evaluation in brief: ground truth must be known per background → models reproduce a known function; DegradX in one sentence [DX]. RQ1–RQ3 as tests of the thesis's consequences. Case study [ACIIDS]. Contributions (five: formal statement; characterization; TAB; evaluation design; case study). Scope; battery RUL flagship [severson2019data, ma2022real, cui2024data]; code release (% TODO URL).

## 2 Related Work (2–2.5 pp.) — revision-1 threads, revised
2.1 Value-function problem — kept; Hooker sentence rewritten to his claim (forced extrapolation, misleading) [hooker2021unrestricted]; Frye's equivalence-class result added (supports ensemble divergence); "as we argue" removed (C8); "unit" → "sequence". [frye2021shapley, aas2021explaining, chen2020true, janzing2020feature, sundararajan2020many, hooker2021unrestricted, yeh2022threading]
2.2 What a background explains — kept; Sturmfels's blindness to the baseline value added (prior report of A2). [covert2021explaining, merrick2020explanation, sundararajan2020many, mamalakis2023carefully, sundararajan2017axiomatic, sturmfels2020visualizing, haug2021baselines, zhang2026baselines, chen2022explaining]
2.3 Masking artifacts in images — Jain's specific findings (skew toward unrelated classes; reliance on the masking pattern) and Fong's network artifacts added (prior reports of A3, A4). [jain2022missingness, fong2017interpretable, chang2019explaining, agarwal2021explaining, sridhar2026missingness]
2.4 Realistic perturbations for time series — kept; D6 written plainly. [tonekaboni2020went, crabbe2021explaining, enguehard2023learning, liu2024explaining, kim2026deltaxai, menadjiev2026grail, DX]
2.5 Temporal Shapley methods — kept; TimeSHAP's "cells" anchored to elements; TSHAP unverified detail as % TODO. [bento2021timeshap, nayebi2023windowshap, nguyen2025tshap, kim2026groupsegment, papadeas2026empirical, zhao2026tempshap]
2.6 XAI in prognostics and its evaluation — opening replaced: SHAP most used in predictive maintenance [cummins2024explainable] (Moosavi's common statement dropped, C3); DegradX results qualitative only (numbers moved to §6.1, C11). [ACIIDS, qu2026explainable, turbe2023evaluation, simic2025comprehensive, baer2026class, ismail2020benchmarking, queen2023encoding, baer2026xaitimesynth, DX, esteban2017real, DXR]
2.7 The gap — kept; neutral terms; "cheap" replaced.

## 3 Problem setup and notation (≈1.5 pp.) — no common knowledge (C13)
1. Data, windows, elements (TimeSHAP's cells), players. [bento2021timeshap]
2. Masking operator (Eq. 1), value function; Shapley values cited, not restated [shapley1953value]; A_b(f) as the estimator's map.
3. Explained quantity: efficiency (Eq. 2) [sundararajan2020many]; Baseline Shapley; explained mass (introduced).
4. Requirements R1–R3 [DX for the length leakage].
5. Mean component, state, state-conditional mean μ_c(s), state index h_u (Eq.).
6. Substitution distance and the stationarity assumption: Eq. (risk decomposition); constant optimum = population mean; state-wise optimum μ_c(s); coincide only under mean-stationarity; excess = squared systematic distance (C9 a). The model reads the state.
7. Ground truth for b relative to a function g, distortion, difference game (Eqs.) [sundararajan2020many for linearity] — formal items needed by §4.
8. Notation table (Table 1).

## 4 Substitution artifacts (≈2 pp.) — hypotheses
0. Opening: under an unconditional b the excess substitution error is located in the bands of the mean component far from b; the model's response there enters D_b; none of the artifacts needs a monotone mean component.
1. A1 inflation: description + monotone instance; prior: extrapolation-induced inflation [hooker2021unrestricted], trend → noisy perturbation methods [tonekaboni2020went]; M1.
2. A2 blindness: description; the part shared by the ground truth (Sturmfels) vs the artifact; prior [sturmfels2020visualizing]; M2 with pattern-free counterpart [DX].
3. Bands geometry, Fig. 1 (schematic).
4. A3 spurious pattern: prior [jain2022missingness, fong2017interpretable]; M3.
5. A4 directional offset: prior [jain2022missingness]; M4 (with and without known function).
6. A5 carry-over: none reported to our knowledge; M5.
7. A6 compounding: none reported as such; M6.

## 5 Trend-aware backgrounds (≈2.5–3 pp.) — the proposed solution
1. What each background explains (Table 2) and the toy window (Fig. 2, DegradX HUST) [DX].
2. B0, B1 (mean; TimeSHAP's median variant), B-pristine; B1 is the best constant (link to §3's equation). [bento2021timeshap, DX] (% TODO ACIIDS Eq. 3)
3. TAB-state: Eq.; estimand μ_c; index from x_{1:u−1}; merging; index-channel screen; robust variant. K changes the question. S1–S4, limitations.
4. TAB-traj: Eq.; strict past; T1–T4; shift in meaning. Both shift what is explained.
5. Oracles B2*, B3*; Fig. 3 (DegradX HUST).
6. B2c (D1 default). B4 (learned imputer, established reference) [frye2021shapley].
7. Selection guide (Table 3).

## 6 Evaluation methodology (≈4–4.5 pp.)
6.1 Ground truth per background — why not a common ground truth (DegradX numbers, the only place they appear) [DX]; known function → exact ϕ*_b; D_b; non-circularity [DXR]; normalization and explained mass; ensemble divergence (introduced) [frye2021shapley, DX]; how the thesis is tested (consequences i–iii, outcomes that contradict it, RQ mapping) (C9 d). Fig. 4 (design).
6.2 Testbed — DegradX as used (DegradX's terms named once) [DX, DXR, severson2019data, ma2022real, cui2024data]; reference model g; the premise in the testbed (Fig. 5, descriptive, judgment call); declared extensions, with DegradX implications 2 and 3 where they motivate the trended null channel and the event-driven target [DX, DXR]; longer L (D2; % TODO ACIIDS); P-GEN.
6.3 Models — families, function-identity check (D8 open), control [friedman2001greedy]; ground truth per family; verdict.
6.4 Instruments, predictions and statistics — Table 4; E1–E5 [DX]; statistics [DX, DXR].
6.5 Measured data and case study — TSTR ratios [DX]; appended null channels; ensemble divergence; PCoE case study [saha2007battery, ACIIDS] (% TODO ×4).
6.6 Implementation — TimeSHAP 1.0.4 settings [bento2021timeshap, DXR]; background sequence; modified masking step; estimator-family argument; TSHAP check [nguyen2025tshap] (% TODO).
