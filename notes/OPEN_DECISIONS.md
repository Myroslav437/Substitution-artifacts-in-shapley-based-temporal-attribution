# Open decisions, open constants, unverified items, conflicts and judgment calls

*Revision 2 (authors' comments of 2026-11-05). The paper no longer carries review machinery (comment C1), so this file is the only record of everything the authors still have to decide or that could not be verified. Section numbers refer to the revised paper (`builds/paper.pdf`); line numbers to `paper/…/templateArxiv.tex`.*

---

## 1. Open decisions D1–D9 (brief rev. 1 §2.9) — defaults written in the text, without markers

| ID | Default written in the text | Where | Note |
|---|---|---|---|
| D1 | B2c (coalition-conditional TAB) included as a variant of TAB-state | §5 "B2c", Table 2; §6.6 (modified masking step) | Sums to f(x) − f(b₁) exactly |
| D2 | Longer window L := 96, from DegradX's declared grid [8, 16, 24, 48, 96] | §6.2 "One longer window"; Table 4 (A5) | `% TODO` l. 418: replace by the ACIIDS sequence length if that paper states one (paper not available) |
| D3 | B1 = per-channel training mean; TimeSHAP's average event (median) as a variant | §5 "B0, B1 and B-pristine" | "As in the ACIIDS paper's Eq. 3" removed from the text (unverifiable); `% TODO` l. 298 |
| D4 | "mean component", not "level"; "state index" | §3 and throughout | |
| D5 | M-ψ included, "conditional on the pilot" | §6.2 (targets), §6.3 (M-ψ) | ψ itself is not specified by any input (open constant, §2) |
| D6 | Non-Shapley comparators dropped from the design; discussed in Related Work only | §2.4, last sentence | Same reason as DegradX's exclusion of mask-optimizing methods |
| D7 | Primary synthetic architecture = DegradX's LSTM; attention LSTM in the case study only | §6.3, §6.5 | |
| D8 | Threshold ϑ of the function-identity check left open in the text | §6.3 (M-obs) | X9 pilot (HUST; IG and occlusion only): M-obs fits to 1–2 % of the noise term's SD; ten models span 0.45–0.47 in temporal profile error against a method gap of 0.035 (readiness review §2.2). Unpublished, so not in the text |
| D9 | Target journal EAAI | not in the text | Conflicts with the PRIMEarxiv template (conflict C1 below). EAAI's abstract rules (≤ 250 words; no undefined acronyms) are applied to the abstract |

## 2. Method constants that no input fixes (written as symbols; to be set before the experiments)

- TAB-state: K, bin scheme (per-coordinate product or scalar index), minimum bin count; the running summary h, cap d and near-duplicate threshold of the index-channel screen.
- TAB-traj: t_min, function family 𝓜, weight profile ω, penalty P (λ by cross-validation).
- B4: imputer architecture and training.
- Control: boosted-tree implementation and hyperparameters.
- M-ψ: ψ.
- M2: quantiles defining the near and far bands.
- M5: the positions u₀ swept.
- Precision of permutation sampling for ϕ*_b (B2c, B4, M-ψ).
- P-GEN: amplitude, period, phase of the periodic component.
- E2: subsample fractions.
- Cross-estimator check: which profile.

Chosen in revision 1 and still to be confirmed:
- Trended null channel: another sequence's degradation-state trajectory from a random start, held after that sequence's end of life, mapped through the charge-time mapping, with charge-time noise.
- M-R ensembles use DegradX's ten-member design (needed for ensemble divergence on the measured arms).
- Recency weighting only (DegradX's primary); uniform weighting not run.
- The background function may read the sequence's history before the window (R1).

## 3. Unverified items (`% TODO` comments in the source, invisible in the PDF)

| # | Item | Where |
|---|---|---|
| 1 | DegradX arXiv identifier (`degradx2026`: `arXiv:XXXX.XXXXX`) | `references.bib` l. 490 |
| 2 | Repository URL of this paper's code | `templateArxiv.tex` l. 111 (§1, last sentence) |
| 3 | ACIIDS paper (`mishchuk2026explaining`) still absent from `./style`, `./docs` and `./paper` (checked 2026-11-05). Not in the text: B1 "as in its Eq. 3" (D3, l. 298); its sequence length (D2, l. 418); PCoE battery cells and preprocessing, attention-LSTM architecture (l. 467); what the published pipeline did differently (l. 469); the list of published findings for the case study (l. 471). Its bibliographic record is verified (Crossref) | §5, §6.2, §6.5 |
| 4 | TSHAP: only the publisher abstract was read. Its background-selection rule (l. 142) and its applicability to the LSTM regressor and to element-level players (l. 478) are unverified | §2.5, §6.6 |
| 5 | GroupSegment-SHAP is cited in its CIKM '26 version; the claims were checked on arXiv v2 (2026-08-21); the CIKM text was not accessible | §1, §2.5, §2.7 |
| 6 | Cummins et al. are cited in their IEEE Access version; the claim was checked on arXiv v1 (2401.07871); the IEEE text was not accessible (Xplore bot wall) | §1, §2.6 |
| 7 | EAAI word limit (250 words) taken from the ScienceDirect Guide for Authors as indexed by search; the guide page itself returned 403. The acronym rule was read on the Elsevier journal page | abstract |

## 4. Conflicts between inputs not resolved

- **C1 (from rev. 1)**: brief rev. 1 names `elsarticle`; the project uses PRIMEarxiv. Template untouched; an EAAI submission needs a port.
- **C2/C5 (from rev. 1)**: ACIIDS findings quoted in v5.1 (Eq. 3; Spearman 0.078; 16.9 % pruning; Reviewer 4) are not used, since the paper is the only allowed source and is unavailable.
- **C4 (from rev. 1)**: DegradX's README/CITATION.cff cite it as an ACIIDS 2027 submission; the brief asks for the arXiv entry.
- **C9 (from rev. 1)**: v5.1's B4 validity gate also used fill surprisal; only the held-out imputation error is kept.
- **Rev. 1**: brief §2.5 omits P-GEN from the extensions while §3 item 8 and E5 require it — included as a declared extension.
- **New, C4 vs EAAI**: C4 asks to use "SHAP" unexpanded; EAAI forbids undefined acronyms in the abstract. Resolved by writing the abstract without any acronym ("Shapley-value attribution", "remaining useful life"); SHAP is used unexpanded in the body.
- **New, RQ wording**: brief rev. 1 §2.1 gives the RQs verbatim; comment C9 (d) asks RQ1 and RQ2 to read as tests of the thesis. The comment wins: RQ1 now asks whether the distortion is structured by the distance between the mean component and the background (and how large it is); RQ2 and RQ3 keep their substance.

## 5. Judgment calls of revision 2 (for the authors to confirm or reverse)

1. **Evidence that SHAP is the most used method (C3).** Found and verified in three systematic reviews (details: `REFERENCES_AUDIT.md`, REF-50 to REF-52):
   - Cummins et al. 2024 (IEEE Access), 102 studies of explainable predictive maintenance: "By far, SHAP is the most used method seen in our sample."
   - Saarela and Podgorelec 2024 (Applied Sciences), 512 XAI application articles: SHAP the most common technique; "about a third" is read from their Fig. 6 (≈177 of 512; the text gives no count).
   - Arabzadeh and Frank 2025 (MAKE), 50 studies of explainable energy time-series forecasting: "post hoc methods, particularly SHAP, dominate". Their "62 % of studies" is **not** quoted, since the sentence does not say whether it counts SHAP or all post hoc methods.
   - Not found: a review that counts methods in time-series *regression* or RUL prediction specifically. Qu et al. 2026 (RUL survey, IOP) could not be read in full.
   - Moosavi et al. 2024 (the former [1]) is removed from the paper and the `.bib`.
2. **Descriptive figure (C9 c, optional) — made.** Figure 5 (`fig_substitution_distance.py`) shows |μ_c(z) − b_c| / σ_c(z) of B1 and B-pristine against the exact degradation state, for the weighted channels of the three profiles, from DegradX training sequences of generation seed 0. It describes input data only; no attribution is computed. It shows the premise of Equation 5 on the testbed (B1 close to the population only around one state, B-pristine only near the start; on capacity the distance far exceeds the within-state spread). The text states no number from it. It can be removed by deleting the figure environment and the paragraph "The premise in the testbed" in §6.2 (the paragraph's last sentence, on what trained models read, should then move to the end of "DegradX as used").
3. **Neutral terms (C12).** Chosen and used throughout outside the DegradX parts; recorded in the notation table where they are symbols:
   - *sequence* for one multivariate time series of the population (DegradX's *unit*; said once in §6.2, "which it calls units"). "Sequence" is also TimeSHAP's term for its input. Used also in the DegradX parts, so that one concept has one term (preferences §4.2); the figure scripts keep DegradX's code names (`units()`).
   - *element* for one channel at one position (DegradX's own word in its Introduction); TimeSHAP's *cell* is anchored once (§3; and §2.5 for its levels "events, features and cells") and survives only as the name of TimeSHAP's granularity ("cell level", §6.6).
   - *population* (not fleet); *state* and the state-conditional mean μ_c(s) (not degradation state) in general sections; "early or late along the mean component" (not "in their life").
   - Kept as DegradX's terms in the DegradX parts and in captions of figures drawn from DegradX data: *degradation state* z, *early-life reference*, *end of life*, *pristine reference point* x⁰. The label **B-pristine** is kept (binding design name); §5 describes it neutrally ("the initial value of the mean component shared by the population, which DegradX calls the pristine reference point").
   - *battery cells* only in the measured-data, testbed and case-study parts.
4. **Section arrangement (C13).** As proposed in brief rev. 2 §3, with one change inside §6: the principle of the evaluation (6.1: why each background needs its own ground truth, the known function, ensemble divergence, how the thesis is tested) precedes the testbed (6.2). DegradX's three implications from revision 1 are no longer a block of their own: each is stated where it motivates a choice (6.1 per-background ground truth; 6.2 trended null channel; 6.2 event-driven target), so each DegradX number appears once (C11).
5. **Formal items placed in §3 for §4 (C13).** Ground truth ϕ*_b, distortion D_b and the difference game Δ_b are defined in §3 (they are needed to state the instruments of §4); §6.1 explains how the known function is obtained and why the ground truth is exact. Ensemble divergence is defined in §6.1 (only the evaluation uses it); the notation table lists it with its equation number.
6. **Abbreviations (C4).** Treated as known to EAAI readers and used unexpanded: SHAP, XAI, LSTM, AI. Introduced at first use: RQ, TAB, RUL, TSTR, PCoE. "GBT" is no longer used (written "gradient-boosted regression trees"). The abstract uses no acronym (EAAI rule).
7. **Citations of common knowledge (C3, applied by analogy).** Removed: Moosavi et al. (common statement); the LSTM citation (Hochreiter and Schmidhuber; the LSTM is DegradX's, cited through DegradX); Covert et al. and Lundberg and Lee from Introduction sentences where they backed a general statement (both still cited where they support a specific claim). Kept: Shapley (1953) as the pointer for the Shapley values whose formula C13 removed ("cite instead"); Friedman (2001) for the boosted-tree control, as the source of a method that is run and must be reimplementable.
8. **Contributions.** Five items: one per main point of the story (formal statement of the assumption; characterization; TAB), plus the evaluation design and the case study. No placeholder was needed: none of them anticipates a result.
9. **A2 stated with its ground-truth part (C9, C13).** Part of the "blindness" near the background is the explained quantity of that background (Sturmfels et al.'s blindness to the baseline value) and is shared by the ground truth; the artifact is the band-dependence of pattern retrieval beyond it, which M2 measures. This makes A2 consistent with the per-background ground truth; the instrument is unchanged.
10. **Thesis support without experiments (brief rev. 2 §6, second item).** What the paper now offers: (a) a formal statement (Eq. 5: an unconditional background is the best substitute only under mean-stationarity; its excess error is the squared systematic substitution distance); (b) the argument in §1; (c) verified literature (Frye et al.: incorrect off-manifold explanations, and different explanations for models equal on the data; FIT's out-of-domain counterfactuals under a linear trend; missingness bias) and DegradX's published facts (the mean component carries most target-relevant information; trained models use every weighted channel; the pattern term is negligible or absent), plus the descriptive Figure 5; (d) §6.1 "How the thesis is tested": three consequences, the outcomes that would contradict the thesis, and the mapping to RQ1/RQ2. **Remaining gap:** that the stationarity assumption is what *causes* the distortion is a hypothesis; only the planned experiments (oracles B2*/B3* against B1, M1/M2/M4 against substitution distance, P-GEN) can support or refute it. No experiment was added. Options for the authors: keep as is (recommended); or, if a pre-result illustration is wanted, a single M-obs pilot on one profile under B1 and B3* (would be a result and needs the authors' decision).

## 6. Novelty record (for "to our knowledge" in §1 and §4)

Revision 1 (2026-11-03) found no work providing contributions 2 or 3 (`REFERENCES_AUDIT.md` §3). The extension of 2026-11-05 searched for a characterization of substitution artifacts under trend or mean-nonstationarity and for TimeSHAP background effects in degradation data. New candidates, none of which characterizes such artifacts: arXiv:2608.25897 (information-bottleneck time-series explainer; out-of-distribution counterfactuals), arXiv:2512.20514 (SHAPformer, sampling-free SHAP by attention masking), arXiv:2105.10719 (learning baseline values via causal patterns; static data). Not added to Related Work.
