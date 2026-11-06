# Masking backgrounds on DegradX: readiness check and methodology review

*2026-11-03. Inputs: the final DegradX arXiv paper; repository `Myroslav437/degradx` at `f5bba50` (main); `Masking_Backgrounds_Methodology_v5.1.md`; the project reviews of 2026-10-07 and 2026-10-08.*

## Verdict

**Go, with one redesign.**

- DegradX as released is a usable substrate for the masking paper: generator, profiles, exact decomposition, trained ensembles and scoring code. Nothing in the DegradX paper needs to change.
- DegradX's own results show that the way v5.1 planned to use it cannot decide between backgrounds. v5.1 scores each background's attribution on a trained model against the generating function's ground truth.
- The masking paper therefore needs a different reference: models trained on the observation-level target, for which every background has a known correct answer (§2.2).

---

## 1. Can the DegradX results be used?

### 1.1 What carries over as is

| DegradX asset | Use in the masking paper |
|---|---|
| Exact degradation state z at every position | True level index for stratifying M1, M2 and M4; a check on TAB-state's estimated index |
| `m` (the unit's own mean component, with offsets) and `m_state` = φ_c(z) (population, no offsets) on every generated unit | Oracle backgrounds B3\* := m and B2\* := m_state. They separate the TAB concept from its estimation error |
| Reference model g, and ϕ\*(b) = w(m + p − b) for any baseline (`ground_truth_from_baseline`) | Implementation gate: on g, every background implementation must return w(x − b) |
| Null channels (flat, permuted), the null-leakage gate, the conditional-permutation channel-use check | Zero-attribution truth for A1; the acceptance test for new trap channels |
| 60 trained LSTMs: 3 profiles × 2 weightings × 10 members (Git LFS) | Continuity arm, read with ground-truth-free instruments |
| Profiles validated against MATR, HUST and FORM (TSTR 1.49, 1.17, 1.54) | Paired real arms, each with a measured fidelity |
| Temporal profile error, channel allocation error, degraded-map responsiveness | Companion scores. Rank agreement alone is known to miss smoothing and end shifts |
| Full-scale TimeSHAP pipeline: 5,760 explanations in 1.71 h on 12 CPU workers (v2 evaluation) | Cost basis |
| Generator overrides: noise-variance multiplier, transition sharpness (z → z^s), pattern-amplitude multiplier | v5.1's sharp-knee and noise stress variants without new generator code |
| Finding: switching TimeSHAP from the pristine window to the average event reorders methods in rank agreement in HUST and FORM | Citable motivation in the introduction. Not artifact evidence: it is scored against ground truth that is not identifiable on trained models |

### 1.2 What DegradX's results rule out

**F1. On trained models, scores against ϕ\* cannot rank backgrounds.**
- Methods differ by at most 0.073 in rank agreement. Each method's range over ten equally accurate models is at least 0.099, and 0.32–0.34 in FORM.
- TimeSHAP's own background switch moved rank agreement by at most 0.04, which is below that range.
- A background comparison scored this way is therefore expected to drown in model-to-model variation.
- The same evidence falsifies v5.1 §3.7.2(i): "ground truth transfers to the model only if the model learned the generating function, enforced by the accuracy gate". Ten models that pass the gate learned different functions.

**F2. ϕ\* is measured from the pristine point x⁰, and TAB changes what is explained.**
- On g, a background b returns w(x − b).
  - TAB-state, with fine bins: b ≈ φ_c(z_t), so the attribution ≈ w(δ + p + ε).
  - TAB-traj: b ≈ m, so the attribution ≈ w(p + ε).
- Both discard the graded field, which is the bulk of ϕ\*.
  - Against the common ϕ\*, TAB is wrong by construction.
  - Against its own ϕ\*(b), TAB is exact by construction, as is every other background on g.
- Neither comparison measures a masking artifact, because that requires a model that is nonlinear off its support.
- DegradX's declarations anticipated this (`attribution.baseline.not_adopted`): a background conditioned on the local mean component "would make trend-conditional backgrounds correct by construction and any later evaluation of them circular".

**F3. Channels with zero weight that carry z are not traps.**
- MATR's internal resistance and temperature have conditional importance 0.0026 [0.0014, 0.0046] and 0.0043 [0.0028, 0.0073] (`table4_usability.json`). The model reads them.
- This breaks v5.1's Design 3. A trap channel is meant to carry the trend without entering the label, so that its correct attribution is about 0. A channel that carries the state predicts the target, so a model may legitimately use it.
- The null channels are clean but stationary, so they offer no mean-component structure for M1.

**F4. No localized structure is learnable under y.**
- MATR and HUST carry no inserted patterns.
- In FORM the pattern term holds 1.7 × 10⁻⁵ of the mean term's variance, and removing it leaves the error unchanged.
- M2 and M3 are therefore infeasible on models trained on y.

**F5. DegradX windows are almost flat in their mean component.**

Computed here from the committed fitted profiles with the library generator: generation seed 0, 300 units, windows every 6 positions, B1 taken as the mean over all generated positions. All values are medians, in units of the channel's noise SD.

| Profile | Channel | Change within the window (L := 24) | Distance of the window from B1 |
|---|---|---|---|
| MATR | capacity | 1.05 | 16.9 |
| MATR | charge time | 0.13 | 3.4 |
| MATR | mean discharge voltage | 0.12 | 2.0 |
| HUST | capacity | 2.54 | 62.5 |
| HUST | charge time | 0.11 | 2.3 |
| HUST | mean discharge voltage | 0.12 | 5.6 |
| FORM | capacity | 0.79 | 8.3 |
| FORM | charge time | 0.00 | 1.1 |
| FORM | mean discharge voltage | 0.14 | 2.3 |

- The change within a window is at most 10 % of the window's distance from B1.
- Under B1 the substitution distance is therefore nearly constant inside a window. Class I artifacts will appear between windows, indexed by z, not as a temporal profile inside a window.
- v5.1's time-domain views (edge inflation, A5 carry-over profiles) need longer windows.
- Capacity is far off the manifold under B1 (8–63 noise SD); the other channels are mildly so (1–6). Artifacts should therefore concentrate on capacity.

### 1.3 To finalize before starting (repository only, no paper changes)

1. **Retag the release.**
   - Tag `v1` points to `c7737c9`; main is `f5bba50`.
   - Main restores the S04 seed-stream name that produced the committed artifacts (renaming it changes the draws) and fixes the bundle loader's memory use. Code at `v1` therefore does not reproduce the committed FORM protocol-share permutation.
   - Tag `v1.0.1` on main and build the release bundle from it.
   - I could not check from this session whether the bundle is attached to the release.
2. **Fill the arXiv footnote,** which still reads "[PLACEHOLDER: repository and DOI]".
3. **Recover the X9 pilot** (observation-level target, HUST).
   - Its code and record are not in the public repository: the remote has only `main`.
   - §2.2 builds on it, so recover it from the v2 branch if it is kept locally.
4. **Retrain or recompute what was not committed:** the TSTR models (target R) and the S15 attribution maps. Both are cheap.
5. **Check the generator overrides before using them.** They were declared but not run with offsets (D25), so run the construction checks once before any stress variant.
6. **Freeze DegradX v1.** Put the masking-paper extensions (trended null channel, y_obs target, per-window backgrounds) in a versioned layer on top, so the released numbers never move.

---

## 2. Methodology review: how the masking paper should use DegradX

### 2.1 The core problem: each background asks its own question

Attributions sum to f(x) − f(b(x)), so the background fixes what is being explained.

| Background | When all cells are masked, f is evaluated on | Attributions sum to | Question answered |
|---|---|---|---|
| B0, B1, pristine (unconditional) | a constant window | f(x) − f(b) | Why does this prediction differ from a fixed reference? |
| B2 TAB-state (R2, fine bins) | the population at this window's states | f(x) − f(b_state(x)) | Why does it differ from a typical unit at the same state? |
| B3 TAB-traj (R2) | the unit's own extrapolated trajectory | f(x) − f(b_traj(x)) | What do the observations add beyond the unit's own trajectory? |
| B4 imputer (depends on the coalition) | the population marginal | ≈ f(x) − E f | The B1 question, with coalitions that stay on the manifold |

**Consequences for v5.1:**

1. **Read distortion per question.** "TAB reduces distortion" must be read against the question each background answers, and the explained mass |f(x) − f(b)| must be reported beside it. Otherwise a reviewer reads the result as "TAB explains less, so it errs less".
2. **The semantic shift applies to B2 as well.** v5.1 states it for B3 only (§3.5.3a). With fine bins, b_state sits on the observed level.
   - In HUST, the offsets carry 0.343 of Var(y). B2 still explains them and B3 does not, so HUST is where the two methods differ most.
3. **One selection-guide row is wrong.** §3.5.3b routes "does the absolute level here matter?" to B2. Only backgrounds whose explained quantity keeps the level can answer that: the unconditional ones, or B4.
4. **K in B2 changes the question.** It is not only a bias–variance setting (§3.5.2): K = 1 explains the level, while a large K removes it.
5. **B4 against TAB compares two different games.**
   - A cheap analogue of B4 keeps the B1 question: a coalition-conditional TAB. It substitutes each masked cell with the level of the same channel's unmasked cells in the window. The windows are nearly flat (F5), so this is a closed-form mean.
   - R2 excludes this variant partly on cost. The cost argument holds for a model-based imputer, but not for a mean. Worth adding as an arm, or else R2 should be kept with the narrower question stated explicitly.

### 2.2 Proposed design: give the trained model a known function

**The idea, taken from the X9 pilot.**
- Train the LSTM on y_obs := Σ w (x − x⁰), the reference model g applied to the observed window.
- f then reproduces g on the data support. In X9 (HUST; IG and occlusion only), the models fit to 1–2 % of the noise term's SD. In temporal profile error, the ten models spanned 0.45–0.47, against a method gap of 0.035.
- Off the support nothing constrains f, and that is exactly where unconditional backgrounds query it.

**Reference and distortion.** For every background b, the correct attribution of the learned function is the exact attribution of g from b, ϕ_b^ref := w(x − b). The distortion is

  D_b := A_b(f) − w(x − b).

- **It separates the two parts the thesis names (v5.1 §1.1).** These are (a) genuine information loss, which equals w(x − b), and (b) the model's reaction to an impossible input, which equals D_b.
- **It is not circular.** TAB is not correct by construction: it passes only if its coalitions keep f on its support. Noise-free substitutes over large coalitions are a real way for it to fail (A6).
- **It asks every background the same question.** Did the background make f leave the region where it equals g? The comparison is therefore fair even though the explained quantities differ.
- **Normalisation.** Report D_b in target units and relative to |w(x − b)|, both declared before running.

**Model families, all trained on DegradX units:**

| Family | Training target | Correct attribution | Role |
|---|---|---|---|
| M-obs | y_obs (affine) | w(x − b), for every b | Tier 1 headline |
| M-ψ (conditional) | ψ(y_obs), with a declared monotone nonlinear ψ | Exact Shapley of ψ∘g from b, by permutation sampling on the analytic function (cheap, any precision) | Run if M-obs distortion stays within fit error for every background. The risk it covers: an LSTM fitted to an affine map may stay nearly linear off the support |
| M-y (released) | y | Ground-truth-free instruments only | Continuity with DegradX |
| M-R | R, on generated units (TSTR models) and on measured cells | Ground-truth-free instruments | Tier 2 bridge (RQ3) |

**Two further instruments that this design enables:**
- **Ensemble divergence.**
  - The ten M-obs members agree on the support, so their attributions under b can differ only through off-support behaviour. The spread of A_b across members therefore measures, without ground truth, how much an explanation depends on behaviour no training data constrain.
  - It runs unchanged on measured data with M-R ensembles. This gives Tier 2 a third necessary-condition instrument and turns DegradX's central finding into a tool.
- **Paired contrasts.** Compare backgrounds within a model, on the same windows with the same TimeSHAP seed. Report each contrast with its interval and the number of members that agree in sign, not unpaired scores against ϕ\* (F1).

### 2.3 Backgrounds on DegradX

- **B0.**
  - Attributions run in raw input space: `RawSpaceModel` wraps the standardiser.
  - Zero in the standardised space is the training mean, i.e. B1. B0 therefore means raw zeros (0 Ah, 0 min, 0 V), a pure floor.
  - Declare which reading is used.
- **B1.**
  - v5.1 takes ACIIDS's feature-wise mean (Eq. 3). DegradX's secondary baseline is TimeSHAP's average event, which is the per-channel median.
  - Pick one; the other costs one extra run.
- **B-pristine (new incumbent).**
  - x⁰ at every position. This is DegradX's primary baseline: unconditional, and farthest from late-life windows.
  - Its TimeSHAP maps already come out of the DegradX pipeline (`data/attributions`, not committed).
- **B2\* := φ_c(z_t) and B3\* := m_t (oracle arms).** They bound what TAB can reach with a perfect level index. The gap from B2 to B2\* is the estimation error of the index.
- **B2's index.**
  - v5.1 computes ĥ_t from x_{1:t}, so the masked value feeds its own substitute.
  - v5.1 gives the substitution-integrity argument against exactly this for B3 (§3.5.3), so B2 should use x_{1:t−1} as well.
- **Interface.**
  - The TimeSHAP 1.0.4 kernel accepts a background sequence of the explained length (`timeshap_kernel.py`). Per-window TAB backgrounds (L × C) therefore go through the existing interface. DegradX's wrapper reshapes the background to (1, C) and needs that one change.
  - B4 and the coalition-conditional TAB do not fit a single background. They need a modified masking step in the kernel, which v5.1 §3.6 does not mention.
- **Elapsed position t in M-R.** The R models take t as an input. Declare it as unmasked context rather than a player: masking age with a fleet mean is its own A1 case and would dominate.

### 2.4 A1–A6 on DegradX

| Artifact | Instrument | Feasible on DegradX? | What is needed |
|---|---|---|---|
| A1 | M1 | Partly: the null channels have zero truth but no mean-nonstationarity | A trended null channel: a mapping applied to another unit's state trajectory at a random phase. Accept it only if it passes the null-leakage gate and the conditional-use check |
| A2 | M2 | FORM only, under M-obs. Patterns enter y_obs linearly, so the model reproduces them; bands come from the exact z | Nothing further |
| A3 | M3 | No. It needs a model that reacts to the shape of an excursion. At fitted amplitudes the pattern term is 1.7 × 10⁻⁵ of the mean term's variance, and under y_obs the response is linear | A declared event-driven target on FORM, which depends on p and so must be detected. Add amplitude stress if it is not learnable. Synthetic only, labelled as not calibrated |
| A4 | M4 | Yes, on every model. Under M-obs the reference shift is g(mask(x)) − g(x) = Σ_masked w(b − x) | Nothing further |
| A5 | M5 | No: DegradX has no non-recurrent control, and L = 24 is too short for carry-over profiles (F5) | A GBT on flattened windows, plus one longer L from DegradX's declared grid (48 or 96) |
| A6 | M6 | Yes | Stratification by coalition size |

### 2.5 Real arms and RQ3

- **Paired real arms:** MATR, HUST and FORM. Their TSTR ratios state how far each synthetic arm stands for its dataset. HUST is the anchor, since its interval [0.94, 1.34] contains 1.
- **PCoE** remains only for the ACIIDS case study, unpaired. A profile is not possible: the 2026-10-07 review records 34 cells, of which 11 reach EOL.
- **Dropped:** CALCE, NASA RW and C-MAPSS.
- **RQ3 bridge.**
  - Use the same target (R) and the same ground-truth-free instruments on M-R models trained on generated units and on measured cells.
  - The instruments are: M4's shape against the mean component; attribution mass on null channels, using v5.1's appended permutation-null channels on measured data; and ensemble divergence.

### 2.6 Edits to v5.1, for v5.2

1. **§2, §5:** DegradX is now published prior work, a testbed. Drop contribution 2 and novelty leg 3, and cite DegradX instead.
2. **§3.7:** replace the generator specification (fixed double-exponential family, Designs 1–3, P-\* profiles) with "DegradX v1 plus declared extensions". The extensions are: the trended null channel; the y_obs and ψ targets; the event-driven FORM target; and the stress overrides.
3. **§3.7.2:** replace "the accuracy gate ensures the model learned the generating function" with a function-identity gate. The gate is M-obs fit relative to the noise term's SD, declared before running.
4. **§3.9, Tier 1:** the verdict becomes D_b against w(x − b) on M-obs, with the explained mass, read as paired within-model contrasts with member sign agreement.
5. **§3.4, §3.5:**
   - state the explained quantity of each background;
   - correct the semantic statement for B2, the selection-guide row, and the role of K;
   - compute B2's index from x_{1:t−1};
   - add B-pristine, B2\*, B3\* and the coalition-conditional TAB;
   - state B4's kernel requirement.
6. **§3.11, §3.13, E2, E4:** rebind to MATR, HUST and FORM.
   - E2 (fleet size): HUST has 54 fitting cells and FORM 127, plus subsampling.
   - E4 (noise): use the noise-variance override.
7. **§3.12:** the primary synthetic model is the DegradX LSTM, whose ensembles exist. The Attention-LSTM is used only in the case study, and the GBT control is new.
8. **§3.2.3, P-GEN:** DegradX's generator is monotone by construction (monotone families, monotone mappings). A periodic component needs new code, and whether it enters the target must be declared. Under y_obs it does so automatically.
9. **Terminology:**
   - DegradX is a "testbed".
   - The working rule says "mean component", not "level", yet v5.1 builds its taxonomy on "level". Decide which term survives.

### 2.7 Decisions needed

1. Adopt M-obs (the y_obs reference) as the Tier 1 adjudicator?
2. Add the coalition-conditional TAB, or keep R2 and state the narrower question TAB answers?
3. Which longer L for A5? Should it match the ACIIDS sequence length, for case-study continuity?
4. B1 as the mean or the median?

**Compute.** This is a derived estimate at the v2 throughput, for coalition-independent backgrounds only and TimeSHAP at the declared scale:
- 3 profiles × 7 backgrounds (B0, B1, pristine, B2, B3, B2\*, B3\*) × 10 M-obs members × 120 windows = 25,200 explanations, about 7.5 h.
- Not included: B4 and the coalition-conditional TAB, which need the modified kernel.
