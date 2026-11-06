# CHANGELOG — TAB journal paper (revision 1: brief of 2026-11-03; revision 2: authors' comments of 2026-11-05)

Each entry names its source: B§ = agent brief, R§ = readiness review (2026-11-03), V§ = methodology v5.1,
P§ = writing_style_preferences.md, DX = DegradX arXiv paper, DXR = DegradX repository at f5bba50, REF-n = REFERENCES_AUDIT.md.

---

## P0 — Inventory (2026-11-03)

### Inputs found

| Input (brief §1) | Location | State |
|---|---|---|
| Journal draft | `paper/_arXiv__Substitution_Artifacts_in_Shapley_Based_Temporal_Attribution/` | 4 files: `templateArxiv.tex` (main), `PRIMEarxiv.sty`, `references.bib`, `README.md` |
| Style preferences | `docs/writing_style_preferences.md` | present, read in full |
| Style-guide papers | `style/` | 3 PDFs: DegradX (identical to the copy in `docs/`, `cmp` equal), FLICS 2026 "LiDAR-Augmented Wi-Fi Signal Strength Prediction", FLICS 2026 "Simulation-Driven Benchmarking Framework for LiDAR-Based Collision Avoidance on AGVs" |
| ACIIDS paper | **not found** in `style/`, `docs/` or `paper/` (checked twice) | see conflict C2 |
| Methodology v5.1 | `docs/Masking_Backgrounds_Methodology_v5.1.md` | present (655 lines), read in full |
| Readiness review | `docs/masking_degradx_readiness_2026-11-03.md` | present, read in full |
| DegradX paper | `docs/_arXiv__DegradX__…pdf` (20 pp., built 2026-10-30) | read in full (text extracted with pdftotext) |
| DegradX repository | cloned from `github.com/Myroslav437/degradx`, checked out at `f5bba50` (scratch copy, not in the project) | declarations, generator, LSTM config and TimeSHAP wrapper read |

### Project inventory (baseline)

- Main file `templateArxiv.tex`: `\documentclass{article}` + `PRIMEarxiv.sty` (PRIME/George Kour arXiv style).
- Packages: inputenc, fontenc, hyperref, url, booktabs, amsfonts, nicefrac, microtype, lipsum, fancyhdr, graphicx (`\graphicspath{{media/}}`; no `media/` folder exists). No natbib, no amsmath, no xcolor.
- Bibliography: `\bibliographystyle{unsrt}`, `\bibliography{references}`; `references.bib` holds only the three template placeholder entries (kour2014real, kour2014fast, hadash2018estimate).
- Sections at baseline:
  1. Introduction — heading + subsection "Research questions" with RQ1–RQ3 (old wording).
  2. Related Work — subsection "The value-function problem in Shapley explanations" (two authored paragraphs, citing frye2021shapley, aas2021explaining, chen2020true, janzing2020feature, sundararajan2020many, yeh2022threading, zhang2026axiomatic — none in the `.bib`); empty subsection headings: Off-manifold Shapley on tabular data, Masking artifacts and realistic infilling in image XAI, Realistic perturbations for time-series saliency, Temporal Shapley methods and background sensitivity, XAI in prognostics, The gap; then template demo content (`\lipsum[4]`, "Headings: second level", HMM equation, "Headings: third level", "Paragraph").
  3. "Examples of citations, figures, tables, references" — template demo section (lipsum, sample figure, sample table, list).
  4. Conclusion — "Your conclusion here".
  - Acknowledgments — template placeholder ("This was was supported in part by......").
  - Abstract — `\lipsum[1]`.
- Existing figures: none (only the template's `\fbox` placeholder).

### Baseline record

- Not a git repository. Baseline = byte copy in `notes/baseline/_arXiv__Substitution_Artifacts_in_Shapley_Based_Temporal_Attribution/`, with `notes/baseline/SHA256SUMS` (main tex sha256 `17dcf199…6cc`).
- Baseline compile (pdflatex → bibtex → pdflatex ×2, in scratch): PDF produced, but with **5 × "Undefined control sequence"** (`\citet`/`\citep`, natbib not loaded), undefined citations (keys not in `.bib`), and an undefined reference `sec:headings` (no such label). All causes lie in §2 (Related Work), i.e. inside the brief's scope, so they are repaired there (see P4–P6 entries), not in the template.

### Conflicts between inputs found at P0

| ID | Conflict | Resolution | Status |
|---|---|---|---|
| C1 | Brief §0 says the template is `elsarticle`; the project uses PRIMEarxiv (`article` class). | Template left untouched (brief §9 "Do not touch the template"). Flagged: an EAAI submission needs a port to `elsarticle`. | Unresolved → Notes box |
| C2 | ACIIDS paper absent from `./style` (and from `./docs`, `./paper`). Springer full text not reachable (login wall). | Brief §8: continue with `\todo{}` wherever its content is needed. Bibliographic record verified via Crossref only. | Unresolved → Notes box |
| C3 | Baseline does not compile cleanly (see above). | Repaired inside §2: natbib loaded (numbers), bibliography style `unsrt` → `unsrtnat` (needed for `\citet` author names; matches DegradX's reference format, which prints DOIs as unsrtnat does; P§6.6). | Resolved; style change flagged in Notes box |
| C4 | DegradX README/CITATION.cff cite DegradX as an ACIIDS 2027 submission; brief §5.3 says cite the arXiv entry, identifier unknown. | Brief wins: `@misc` arXiv entry, identifier flagged `% TODO`. | Flag kept → Notes box |
| C5 | v5.1 states ACIIDS internals (Eq. 3 global mean, Spearman 0.078, 16.9 % pruning, Reviewer 4) from "project files". Brief §1: the ACIIDS paper is the only source for its findings. | Not used in the text; replaced by `\todo{}` (C2). | Unresolved → Notes box |
| C6 | Brief §2.5 "zero-weight channels that carry the state are read by models"; the readiness review supports it with conditional-importance values from `table4_usability.json`, which the DegradX paper does not print. Brief §2.5: "take the numbers from the DegradX paper". | Text uses DX Table 5/§4.4 (share of attribution on zero-weight channels 0.134–0.198 in MATR, where they carry the state, vs ≤ 0.048 in HUST/FORM) plus the argument that a state-carrying channel predicts the target. | Resolved |
| C7 | Brief §2.3 gives "≈ f(x) − E f" for B2c and B4. With B2c's fallback to the training mean, v(∅) = f(b₁) exactly. | Text states B2c's sum exactly as f(x) − f(b₁) ("keeps B1's explained quantity", brief §2.6) and B4's as ≈ f(x) − f(b₁) under a conditional-mean fill. | Resolved (precision) |
| C8 | v5.1 instruments absent from brief §2.7–2.8: substitution surprisal / H-S (V§3.10), dual-scheme deletion faithfulness, Kendall-W stability bands, knee alignment, Holm/BH families, decision rules. | Dropped: brief §2.7–2.8 fix the instrument and statistics set; P§2.1 (only what is run). | Resolved |
| C9 | v5.1 B4 validity gate has two diagnostics: held-out imputation error and fill surprisal (V§3.9.2). Surprisal needs the density model dropped under C8. | Gate kept with the imputation-error diagnostic only. | Judgment call → Notes box |
| C10 | Brief §1 lists DegradX at f5bba50 as a source; R§1.3 notes tag v1 points to c7737c9 and does not reproduce the committed FORM permutation. | Paper cites the repository at commit f5bba50 (the brief's pin). | Resolved |

### Verified facts used from the DegradX repository (DXR, f5bba50)

- `configs/declarations.yaml` `attribution.methods.timeshap`: nsamples 32000, pruning off, cell level (top_x_events = L, top_x_feats = C), timeshap 1.0.4.
- `usability.identifiability_floor`: ensemble = init seeds 0–4 × {A: hidden 64 × 2 layers, B: hidden 128 × 1 layer}.
- `responsiveness.generator_settings`: noise_variance_multiplier, transition_sharpness_multiplier (z → z^s), pattern_amplitude_multiplier; window_length_L grid [8, 16, 24, 48, 96]. Note: the declarations mark this sweep "not run with offsets (D25)"; R§1.3.5 asks for construction checks before use (experiment plan, kept out of the paper).
- `attribution.baseline.not_adopted`: "a background conditioned on the local mean component: it would make trend-conditional backgrounds correct by construction and any later evaluation of them circular".
- `attribution.baseline.primary.applied_as.timeshap`: background (1, C) tiled over L. `secondary`: `calc_avg_event` = per-channel median.
- `src/degradx/generator/generate.py`: `GeneratedUnit.m_state` = φ_c(z) without offsets; overrides as above.
- `configs/models/lstm.yaml`: linear head on last hidden state, Adam 1e-3, batch 256, ≤ 100 epochs, early stopping (patience 10), MSE; elapsed position is an input for the transfer target only.
- `scripts/s15_reference_values.py` / `export_benchmark.py`: 120 evaluation windows per profile, stratified across test units, rule parameterised by L.
- TimeSHAP 1.0.4 wheel (`timeshap/explainer/kernel/timeshap_kernel.py`, l. 154–167): a 2-D background of shape (L, C) equal to the explained length is accepted as a background sequence; (1, C) is tiled. `calc_avg_event` = median of numerical features.

---

## P1 — Style profile
- `notes/STYLE_PROFILE.md` written from the DegradX Introduction/Related Work and the two FLICS 2026 papers; binding overrides from `docs/writing_style_preferences.md`.

## P2 — Entry audit of the existing `.bib`
- The baseline `.bib` held only the three template placeholders (kour2014real, kour2014fast, hadash2018estimate). All three verified (Crossref, arXiv) and corrected (title case, booktitle, DOIs, `@misc` arXiv form). They remain cited only by the template demo section. Log: `REFERENCES_AUDIT.md` §1.
- The seven keys cited by the draft Related Work were missing from the `.bib`; created and verified.

## Novelty re-check (brief §5.4), run before P4 because of the stop rule of brief §8
- No candidate provides contribution 2 or 3; no stop. Candidates and differentiation: `REFERENCES_AUDIT.md` §3.

## P3 — Outline
- `notes/OUTLINE.md`. Structure adapted to the skeleton: §1 keeps the RQ list (now inline, no subsection); §2 keeps its seven subsections, with "Off-manifold Shapley on tabular data" (empty, overlapping §2.1) replaced by the new thread "What a background explains" (brief §5.5) and "XAI in prognostics" extended to "… and its evaluation" (brief §5.5 thread 6); §3 Methodology new, ordered as brief P6.

## P4 — Introduction (new; banner in the review build)
| Change | Source |
|---|---|
| Context → background left to the user → explained quantity → mechanism → thesis (displayed) → why not detrend → existing remedies → DegradX's limits → this work → RQs → case study → contributions → scope | B§2.1–2.2; V§1.1, §1.4 (Q1); DX §1, §4.4 |
| RQ1–RQ3 replaced by the brief's wording, without the labels B0/B1/B-pristine/B4 (defined only in §3; P§4.1) | B§2.1 |
| Contributions: the four of B§2.2; no benchmark/testbed contribution | B§2.2, B§3 item 1 |
| DegradX numbers: ≤ 0.073 vs ≥ 0.099 (rank agreement), ≤ 0.04 background switch, reorder in HUST and FORM | DX §4.4 |
| Abbreviations introduced: XAI, SHAP, LSTM, TAB, RQ, RUL | P§4.4 |

## P5 — Related Work (updated; every change in `\rev`/`\revw` with a `\revwhy` source; deletions marked `\revdel`)
| Change | Category | Source |
|---|---|---|
| §2.1: Hooker et al. sentence added | claim | B§5.5 thread 1; P§2.11 (cited in §1) |
| §2.1: Zhang et al. sentence deleted (source retitled, disclaims manifold membership); reworded in §2.2 | claim | REF-22 |
| §2.1: "static and tabular (or, in the recent theoretical work, image-like)" → "static (tabular or image data)" | claim | REF-8; dangling reference after the deletion |
| §2.1: "the position a sequence has reached along its mean trajectory" → "the state a unit has reached along its mean component" | wording | D4; P§4.2 |
| §2.2 new: what a background explains (Covert; Merrick–Taly; Baseline Shapley; Mamalakis; IG baselines; Haug; Zhang; G-DeepSHAP) | claim | B§5.5 (new thread) |
| §2.3–2.6 written into the empty headings; novelty candidates SWING, GRAIL, TempShap added; D6 stated in §2.4 | claim | B§5.5; B§5.4; D6 |
| §2.7 gap repositioned around DegradX and the explained quantity (B§2.3) | claim | B P5 |
| Template demo text inside §2 (lipsum, sample headings, HMM equation, undefined `\ref{sec:headings}`) removed | deletion | baseline compile fix (C3) |
- Coverage verified by `builds/check_rev_coverage.py` (difflib against the baseline): 1,482 inserted/changed words in §2, 0 outside `\rev`/`\revw` (labels and TOC arguments of renamed headings excluded as non-printing).

## P6 — Methodology (new; banner)
| Element | Source |
|---|---|
| §3.1 notation, masking operator, value function, Shapley values, efficiency → explained quantity; explained mass (introduced); R1–R3; mean component and state index; notation table | V§3.5.1; B§2.3–2.4; R§2.1; P§4.3 |
| §3.2 A1–A6 in general (mean-component-indexed) form with monotone instances; state bands (Fig. 1) | V§1.2 (nicknames "edge inflation" etc. dropped: "trajectory" is not used in general sections, P§3.4) |
| §3.3 ground truth per background (Eq. 5), distortion (Eq. 6) and its difference-game form (Eq. 7, by linearity), ensemble divergence (Eq. 8, introduced), instruments M1–M6 | B§2.4, §2.7; R§2.2 |
| §3.4 backgrounds: Table 2 (explained quantity); B0 raw zeros; B1 mean (D3); B-pristine; TAB-state with index from x_{1:u−1}, K changes the question, robust variant (median, no trimming constant), index-channel screen, S1–S4; TAB-traj, fallback, T1–T4, shift in meaning; oracles; B2c (D1); B4 with held-out imputation error; corrected selection guide (Table 3) | B§2.6, §3 item 5; V§3.4–3.5 |
| §3.5 DegradX as used; three implications; declared extensions incl. P-GEN; model families with function-identity check (D8); instruments table (Table 4, replaces v5.1 Fig. T); envelope predictions E1–E5 rebound; statistics | B§2.5, §2.7–2.8, §3 items 2–4, 7–8; DX; DXR |
| §3.6 measured arms (TSTR ratios, appended null channels, necessary-condition instruments); case study (two steps, `\todo` for ACIIDS content) | B§2.8; V§3.9.1, §3.14 |
| §3.7 implementation: TimeSHAP 1.0.4 settings, background sequence interface, modified masking step for B2c/B4, cross-estimator check with the value-function argument | B§2.8; V§3.6; DXR; TimeSHAP 1.0.4 kernel |
- Dropped from v5.1 per brief: double-exponential generator, Designs 1–3, P-* profiles, CALCE/NASA RW/C-MAPSS, B-L (not in B§2.6), non-Shapley comparators (D6), surprisal/H-S, deletion faithfulness, stability bands, decision rules, pre-registration (C8; B§3 item 10).
- Operationalizations chosen here (flagged in the Notes box): ED_b as the sum over cells of the across-member SD; M4 and M6 on the difference game over the estimator's coalitions; M5 as the change in distortion at other positions after substituting one position; trended null channel construction; M-ev as the name of the event-driven model family; recency weighting only.

## P7 — Figures (`paper/figures/scripts/`, output `media/`)
| Figure | Script | Note |
|---|---|---|
| Fig. 1 state bands | `fig_state_bands.py` | Schematic (analytic shapes), labelled as such |
| Fig. 2 toy window | `fig_toy_window.py` | DegradX HUST, seed 0; window = the evaluation window with the largest final degradation state (unit 54, t = 2178). Drawn with the oracles B2⋆/B3⋆ because K, the index and the fit family are open constants. Sums of g's exact attribution computed by the script |
| Fig. 3 TAB-state vs TAB-traj | `fig_tab_state_traj.py` | Same unit; estimands only, for the same reason |
| Fig. 4 evaluation design | `fig_eval_design.py` | Diagram |
- Numbering follows placement in the text (brief listed the toy example first; it appears in §3.4 after the state bands of §3.2).
- The window rule is replicated from DegradX's code (`select_windows`, evaluation stream of the base seed); it reproduces DegradX's counts (120 windows over 45 test units) and its HUST pristine value; DegradX does not commit the window list, so the identity of the window cannot be cross-checked further.
- DegradX's style module (`degradx.viz.style`) is applied; generator units are regenerated and their lengths asserted against DegradX's committed tables.

## P8 — Claim audit, novelty re-check, consistency pass
- Claim audit: 52 keys cited in §1–§3, all checked (`REFERENCES_AUDIT.md` §2). Three claims were partially supported and rewritten (REF-8 Frye: scope of data; REF-16 Moosavi: scope; REF-18 Covert: "precisely"), and the draft's Zhang et al. sentence (REF-22) was deleted and reworded; linearity re-cited from Shapley (1953, not accessible) to Sundararajan and Najmi (REF-45/REF-5). Unverifiable items flagged (`\todo`, `% TODO`, Notes box).
- Self-review before the first compile: 14 fixes (stray brace in B2c; κ clash with DegradX's channel factor → ℓ; paraphrase of DegradX's `not_adopted` declaration; null channels wrongly said to be appended "as in DegradX"; overclaim "differ precisely"; "training does not constrain its output" → extrapolation/incorrect explanations; FIT conditions on the past, so the novelty claims were narrowed to a low-dimensional state (Intro, §2.4, §2.7); accuracy-gate claim not in the DegradX paper → rewritten from DX §3.6; circularity sentence added to §3.3; duplicated raw-space sentence removed; Fig. 2 caption terms; notation table).
- Consistency pass, three lenses plus a refuter, on the typeset clean build: **22 findings, all applied**.
  - Numbers (3): "all but one case" qualifier; §3.5 point 1 no longer repeats the Introduction's numbers; MATR zero-weight share phrased as DegradX reports it (share of attribution, not "trained models place").
  - Consistency and claims (12): XAI, SHAP, PCoE defined at first mention; §2.6 opening matched to Moosavi's scope; "level" removed from A3, B2c and TAB-traj (D4); "trajectory" removed from Table 2 and the guide; doubled "the mean" in B1; forward reference in "Choosing a background" removed; forward reference to the function-identity check in §3.3 removed; "trap channel" defined at first use; ϑ phrasing.
  - Brief compliance (3): explained quantity of the oracles stated where they are defined; RQ3 comparison includes M-obs; cross-estimator profile listed among open constants.
  - Refuter (4): D_b also contains the residual on-support misfit (f ≈ g); ensemble divergence likewise; M3's zero ground truth justified (substitution inserts no generated patterns); R1 states that the background may read the unit's history before the window.
- Template whitespace: the first full rewrite of `templateArxiv.tex` had stripped trailing spaces from template lines; the file was rebuilt so that everything outside §1–§3 is byte-identical to the baseline except the intended insertions (review switch + `\input{review_setup}`, Notes box input) and `\bibliographystyle{unsrtnat}` (verified by `diff` in `builds/build.sh`; `PRIMEarxiv.sty` and `README.md` unchanged).

## P9 — Builds (`builds/build.sh`)
- `builds/paper_review.pdf`, `builds/paper_clean.pdf`, `builds/paper_diff.pdf` (+ `paper_diff.tex`): each compiles with 0 undefined citations, 0 undefined references, 0 BibTeX errors.
- latexdiff: Git Bash's Perl lacks Algorithm::Diff; the script falls back to MiKTeX's self-contained `latexdiff-so`. In the diff, the baseline's dangling `\ref{sec:headings}` (deleted text) is rendered as literal text.
- Review machinery in `review_setup.tex` (packages, `\rev`, `\revw`, `\revwhy`, `\revdel`, `\dec`, banners, Notes box environment); Notes box content in `review_notes.tex`. `\reviewfalse` (or `\def\cleanbuild{}`) removes all of it.


---

# Revision 2 (authors' comments of 2026-11-05)

Source of every change: the authors' comment Cn (brief rev. 2 §2), the brief rev. 2 (B2§), brief rev. 1 (B1§), the preferences (P§) or the audit (REF-n). Section numbers are those of the revised paper: §1 Introduction, §2 Related Work, §3 Problem setup and notation, §4 Substitution artifacts, §5 Trend-aware backgrounds, §6 Evaluation methodology.

## R2-P0 — Inventory and snapshot

- Snapshot of the state the authors commented on, before any edit: `notes/baseline_r1/` (paper folder, figure scripts, `paper_clean.pdf`, `build.sh`), with `SHA256SUMS`. The revision-1 build outputs (`paper_review.pdf`, `paper_clean.pdf`, `paper_diff.pdf/.tex`, `check_rev_coverage.py`, old `build.sh`) were moved to `notes/baseline_r1/builds_r1/`.
- `./builds/paper_clean.pdf` read first; its text matches `templateArxiv.tex` of revision 1.
- ACIIDS paper: still absent from `./style`, `./docs` and `./paper` (checked 2026-11-05). Handled as C1 requires (`% TODO` comments, OPEN_DECISIONS §3).
- DegradX cloned at `f5bba50` into the session scratchpad; figure scripts run in a virtual environment (numpy, scipy, scikit-learn, pandas, pyyaml, matplotlib 3.10.8).
- `notes/OUTLINE.md` rewritten to the new structure before the text (B2§3).

## C1 — Review machinery removed

- Removed every `\rev`, `\revw`, `\revwhy`, `\revwhyw`, `\revdel`, `\dec`, `\newsectionbanner`, `\todo`, the `\ifreview` switch and the Notes box (`review_notes.tex` and its `\input`); the text inside the wrappers is kept as plain text.
- `review_setup.tex` replaced by `paper_setup.tex` (natbib with numbers, amsmath/amssymb, array/tabularx, `\mask`, `\EM`, `\ED`); xcolor, tcolorbox, todonotes and multirow dropped (nothing needs them). The preamble has one `\input{paper_setup}` line.
- The D1–D9 defaults stay in the text without markers; the content of the Notes box moved to `OPEN_DECISIONS.md`, now the only record.
- Unverified content removed from the text and marked with `% TODO` (8 in `templateArxiv.tex`, 1 in `.bib`): ACIIDS Eq. 3 (D3) and sequence length (D2), PCoE cells and preprocessing, attention-LSTM architecture, pipeline differences, list of findings; TSHAP selection rule and applicability; repository URL; DegradX arXiv identifier.
- One build only: `builds/paper.pdf`; `builds/build.sh` rewritten.
- *Applied by analogy*: the figure-script docstring that referred to the "Notes box" now refers to `OPEN_DECISIONS.md`; the review build, the latexdiff build and the highlighting-coverage check are no longer produced.

## C2 — Abstract

- `\lipsum[1]` replaced by a full abstract: contribution first (the stationarity assumption, six artifacts with instruments, trend-aware backgrounds), evaluation means before results (models of a known function on a testbed calibrated to three battery datasets), introduced measures flagged ("an instrument introduced here", "a measure introduced here"), five result placeholders of one form `\textbf{[RESULT: …]}`, each finding with "indicating that" where its meaning is result-dependent, and the practical use last (P§2.7, §2.9).
- EAAI rules applied (D9): 248 words including the placeholder descriptions (limit 250); no acronym at all, since undefined acronyms are forbidden in the abstract; the AI contribution and the engineering application (battery remaining useful life) are both named. No citations. It tells the story of the restructured Introduction (C10).

## C3 — Common-knowledge citations; SHAP is the most used method

- [1] (Moosavi et al. 2024, "post-hoc attribution is the most frequently applied XAI approach") removed from the Introduction and from §2.6, and from the `.bib`.
- The Introduction now opens with the evidence that SHAP is the most used explanation method, from three verified systematic reviews (REF-50 to REF-52): Cummins et al. 2024 (by far the most used method in 102 studies of explainable predictive maintenance); Saarela and Podgorelec 2024 (most common technique across 512 XAI applications, about a third of them, read from their Fig. 6); Arabzadeh and Frank 2025 (post hoc methods, SHAP in particular, dominate explainable energy time-series forecasting; their "62 %" not quoted because it is ambiguous). The paragraph ends on the consequence: a weakness of substitution affects the attributions most practitioners compute.
- §2.6 opens with the predictive-maintenance evidence (Cummins et al.) instead of Moosavi et al.
- *Applied by analogy*: the LSTM citation (Hochreiter and Schmidhuber) removed with its sentence (C11) and from the `.bib`; Covert et al. removed from the Introduction's general sentence (kept in §2.2 for a specific claim); Lundberg and Lee dropped from the efficiency sentence (kept at the first mention of SHAP). Kept, with reasons in OPEN_DECISIONS §5 item 7: Shapley (1953), now the pointer for the Shapley values whose formula C13 removed; Friedman (2001) for the boosted-tree control.

## C4 — SHAP not expanded

- "which carries SHapley Additive exPlanations (SHAP)" removed; SHAP used as a known name.
- *Applied by analogy*: "explainable artificial intelligence (XAI)" and "long short-term memory (LSTM)" expansions removed; XAI, LSTM and AI treated as known to EAAI readers. RQ, TAB, RUL, TSTR and PCoE are still introduced at first use. The abbreviation GBT is no longer used. Decision logged (OPEN_DECISIONS §5 item 6).

## C5 — No meta-sentences

Each listed sentence replaced by its content or removed:
- "The choice matters for a second reason, beyond sensitivity" → "Beyond sensitivity, the background also fixes which quantity the attribution explains." (§1 P2)
- "This is the organizing claim of the paper:" → removed (C8).
- "We address three research questions (RQs):" → "The research questions (RQs) test the consequences of the thesis:" (§1).
- The Methodology opening "This section first fixes …" → removed; no section opens with a roadmap.
- "One instrument is defined per artifact." → removed; each instrument is defined inside its artifact paragraph (§4).
- "Three results of DegradX determine the design." → removed; each result is stated where it motivates a choice (C11).
- "Five predictions test the selection guide on existing arms." → paragraph head "Predictions for the selection guide." and "Each row of Table 3 is bound to an existing arm." (§6.4).
- "The findings are stated for TimeSHAP, but the argument for their generality covers …" → "The background enters every substitution-based Shapley estimator only through v_b, since …" (§6.6).
- "Table 2 lists the backgrounds by the quantity each one explains, following Equation (3)." → "Each background fixes what its attributions sum to (Equation 2), so the backgrounds below differ in the question they answer as well as in their distortion (Table 2)." (§5).
- "Each is stated in its general form, indexed by the mean component …" → removed; §4 opens with the content ("the excess substitution error of Equation 5 is concentrated at the states whose mean lies far from the background; the artifacts below are hypotheses about how the model's response … enters D_b").
- *Applied by analogy*: "Methods that optimize a mask per instance are discussed here but not compared" → "… are not compared in this paper, for the reason DegradX gave for excluding them" (§2.4); "This separates the two parts named in the introduction." (revision-1 §3.3) removed.

## C6 — The substitution-distance argument, technically

- §1 P3 states the mechanism: masking (u, c) perturbs by |x_{u,c} − b_c|; its systematic part is |m − b|; an unconditional b is constant across states while m moves with the state, so the systematic distance is near zero only near b and grows with the difference; coalitions combine values of different states; the model is evaluated on combinations its training data do not contain; the response enters the attribution. It names the hypothesized artifacts by class (magnitude: inflation far from b, suppression near b; meaning: spurious localized patterns, directional shift; propagation: recurrent carry-over, compounding across coalitions).
- §3 states it formally: substitution distance and its systematic part, and Equation 5 (expected squared substitution distance = within-state variance + squared distance of the state-conditional mean from b).
- §4 defines the artifacts on this basis.

## C7 — "its output is an extrapolation" removed

- Replaced by what the sources and the argument support: "There, the training data do not constrain the model's output. Shapley values computed from such evaluations can give incorrect explanations and can differ between two models that agree on the data [Frye]" (§1 P3; REF-53).
- *Applied by analogy*: §2.1 "The same extrapolation makes permute-and-predict importance measures misleading" → Hooker et al.'s own claim (forced extrapolation to regions with little or no data; can be highly misleading; REF-54); §6.1 ensemble divergence "behaviour that no training data constrain" → "behaviour that the training data do not constrain", with Frye et al.'s equivalence-class result as support; A1 uses Hooker et al.'s wording (inflation for random forests, greater variability for neural networks).

## C8 — Nothing from the authors' side

- "This is the organizing claim of the paper" removed.
- *Applied by analogy*: "as we argue" removed from §2.1 (otherwise the authors' paragraph is unchanged apart from "unit" → "sequence"); "This separates the two parts named in the introduction" removed.

## C9 — The thesis: formatted inline, made precise, argued, supported, tied to the evaluation

- *Formatting*: the centred display removed; the sentence is set inline with `\emph{}` as the conclusion of §1 P4.
- *(a) Precise*: §3 "Substitution distance and the stationarity assumption" with Equation 5: the best constant substitute is the population mean, the best substitute at state s is μ_c(s); they coincide at every state only for a mean-stationary channel; otherwise the excess is (μ_c(s) − b_c)², zero only where the state-conditional mean equals b. "Using one substitute for every position and state therefore treats the data as mean-stationary." The model side: trained on a population whose target variable depends on the state, which the mean component carries.
- *(b) Argued*: §1 P3–P4 (mechanism; why it cannot be avoided; the mismatch of assumptions), and formally in §3.
- *(c) Supported*: Frye et al. (incorrect off-manifold explanations; different explanations for models equal on the data), FIT (out-of-domain counterfactuals under a linear trend), missingness bias (§1, §4); DegradX's facts (mean component carries most target-relevant information, trained models read every weighted channel — §1 P4, §6.2; pattern term absent or negligible — §6.2). Optional descriptive figure made: Figure 5 (OPEN_DECISIONS §5 item 2).
- *(d) Tied to the evaluation*: §6.1 "How the thesis is tested": three consequences (structure by substitution distance in M1, M2, M4 across B0/B1/B-pristine; reduction under TAB and most directly under the oracles, read beside explained mass; persistence under a non-monotone mean component, P-GEN), the outcomes that would contradict the thesis, and RQ1 ↔ (i), (iii), RQ2 ↔ (ii). RQ1 reworded as a test (OPEN_DECISIONS §4). "This paper states the thesis formally and tests its consequences" (§1) marks it as a thesis, not a result.
- *Applied by analogy*: §5 B1 paragraph links B1 to Equation 5 (the best constant background, so B0/B-pristine vs B1 vary the distance while the assumption stays); the oracles "test the thesis most directly"; P-GEN "tests consequence (iii)".

## C10 — The Introduction as one argument

Rewritten in seven steps (old → new): (1) SHAP is the most used family; removal by substitution (old P1, Moosavi replaced by evidence); (2) background left to the user, and beyond sensitivity it fixes the explained quantity (old P2); (3) why mean-nonstationarity makes it structured, with the literature that observed it (old P3, technical, C6); (4) why it cannot be avoided, detrending used as an argument, and the thesis as the conclusion (old P3 end + old P4); (5) therefore a characterization, "to our knowledge" checked against the novelty record (new); (6) based on it, the solution, with the learned imputer as the established alternative (old P5 + P6, without the list of remedies); (7) evaluation in brief, DegradX in one sentence, RQs as tests, case study, five contributions mapped onto the story, scope. ≈ 1.6 pages.

## C11 — The Introduction at the level of the argument

- DegradX results removed from the Introduction (0.073, 0.099, 0.04, ensemble disagreement, the switch of TimeSHAP's background). The numbers now appear once, in §6.1 "Why each background needs its own ground truth", where they motivate the per-background ground truth; §2.6 keeps the qualitative statement only.
- DegradX is described in one sentence in §1 (what it provides).
- *Applied by analogy*: the revision-1 block "What DegradX's results imply" is dissolved: implication 2 (zero-weight channels that carry the state) moved into the trended-null-channel item, implication 3 (FORM patterns carry a negligible share) into the event-driven-target item, both in §6.2; the general A3 paragraph no longer mentions DegradX's FORM profile; the Introduction's sentence on Covert et al. removed; the list of on-manifold remedies (old P5) reduced to the learned imputer that the paper compares against.

## C12 — Domain-neutral terms

- Revision 1 had 81 "unit(s)" and 58 "cell(s)" in the main file; revision 2 has 4 and 14. Remaining "unit(s)": measurement units (3) and "which it calls units" (DegradX's term, said once, §6.2). Remaining "cell(s)": TimeSHAP's cell / cell level (anchored to "element" in §2.5 and §3), TempShap's "cell-level", and "battery cells" in the scope sentence, the measured arms and the case study.
- Chosen terms (OPEN_DECISIONS §5 item 3): sequence; element; population; state and state-conditional mean μ_c(s); "early or late along the mean component". DegradX's own terms (degradation state z, early-life reference, end of life, pristine reference point) kept where DegradX's objects are described; the label B-pristine kept and described neutrally in §5.
- Notation table updated: "unit sequence" → "sequence", elements, s_u, μ_c, σ²_c, per-sequence offset.
- Figures regenerated by their scripts: Fig. 2 ("departure of the sequence", "units of the target variable"), Fig. 3 ("training sequences", "the sequence's own past"), Fig. 4 ("DegradX sequences", "measured battery data … battery cells"); captions changed accordingly. Fig. 1 is unchanged in content (regenerated).
- No neutral term misdescribes DegradX (B2§6): DegradX's units are multivariate sequences, as DegradX itself defines them.

## C13 — Problem setup without common knowledge; a separate section for the artifacts

- New structure (B2§3): §3 Problem setup and notation; §4 Substitution artifacts; §5 Trend-aware backgrounds; §6 Evaluation methodology (6.1 ground truth per background; 6.2 testbed and its extensions; 6.3 models; 6.4 instruments, predictions and statistics; 6.5 measured data and case study; 6.6 implementation). Order inside §6 changed against the brief's proposal (principle before testbed), logged in OPEN_DECISIONS §5 item 4.
- §3: the Shapley formula (revision-1 Eq. 2) and "TimeSHAP estimates these values by sampling coalitions" removed; Shapley values cited instead. Kept: masking operator, value function, efficiency (used for Table 2 and explained mass), R1–R3, mean component, state, state index, substitution distance, the formal stationarity reading (C9 a), and the formal items §4 needs (ground truth, distortion, difference game).
- §4: A1–A6, each with its description (general, with the monotone instance), related effects reported so far (Hooker; FIT; Sturmfels; Jain; Fong and Vedaldi; Frye) or "to our knowledge, not reported" (REF-53 to REF-58, novelty record §7), and its signature and instrument M1–M6 in general form; the band geometry (Fig. 1).
- §5: the backgrounds as the proposed solution (Table 2, Figs. 2–3, Table 3).
- §6: how this paper evaluates the artifacts and the backgrounds.

## C14 — ":=" only for assigned values

- 28 occurrences in revision 1 → 6. Changed to "=": the masking operator, v^f_b, φ_i (removed), EM_b, h_u, d_{u,c}, φ*_b and v^g_b, D_b, Δ_b, ED_b, M5(ℓ), b^state, m̂^(u), b^traj, b^2c, S_c, g(x_W), x⁰_c = φ_c(0), B2*, B3*, y_obs, y_ev.
- Kept: L := 24 (Fig. 2 caption, §6.2), L := 96 (§6.2, Table 4), nsamples := 32,000 (§6.6), h := L/4 = 6 (§6.2, as DegradX writes it).

## Conflicts resolved in revision 2

- C4 vs EAAI's acronym rule → abstract without acronyms (OPEN_DECISIONS §4).
- Brief rev. 1 RQ wording vs C9 (d) → RQ1 reworded as a test (OPEN_DECISIONS §4).
- Brief rev. 2 C13 says the ground truth belongs to the methodology, while §4 needs it to define the instruments → the definitions in §3, the construction in §6.1 (OPEN_DECISIONS §5 item 5).

## Figures

| Figure | Script | Change |
|---|---|---|
| Fig. 1 bands (§4) | `fig_state_bands.py` | Regenerated; docstring renumbered |
| Fig. 2 toy window (§5) | `fig_toy_window.py` | Labels "departure of the sequence", "[units of the target variable]"; same window as revision 1 (HUST, sequence 54, t = 2178) |
| Fig. 3 TAB-state vs TAB-traj (§5) | `fig_tab_state_traj.py` | Labels "training sequences", "(b) TAB-traj: the sequence's own past" |
| Fig. 4 evaluation design (§6) | `fig_eval_design.py` | "DegradX sequences", "measured battery data", "… battery cells" |
| Fig. 5 substitution distance (§6.2) | `fig_substitution_distance.py` (new) | Descriptive, input data only (C9 c, optional; judgment call) |

`run_all.sh` and `README.md` of the scripts updated.

## Verification

- `sh builds/build.sh`: `builds/paper.pdf`, 21 pages, 0 errors, 0 undefined citations, 0 undefined references, 0 BibTeX warnings, no overfull boxes.
- Outside the abstract and §1–§6, `templateArxiv.tex` is byte-identical to revision 1 except the preamble (review switch and `\input{review_setup}` → `\input{paper_setup}`; Notes-box input removed), checked by `builds/check_outside.py`; against the original template, the only difference outside the revised sections is the `\input{paper_setup}` line, the rule line before the Introduction and `unsrtnat`. `PRIMEarxiv.sty` and `README.md` unchanged; title, author block, keywords, demo section, conclusion placeholder and acknowledgments unchanged.
- Every cited key is in the `.bib` and every entry is cited (56 entries; the demo section's three placeholders included).
- One read of the whole paper per comment C3–C14 (term and notation scans plus a full reading of the typeset text); the "applied by analogy" lists above are its result.
- The text is longer than revision 1 (≈ 11,300 against ≈ 9,600 words in the main file), because of the abstract, the formal statement and test of the thesis, the prior reports of each artifact and the premise figure, which the comments asked for.
