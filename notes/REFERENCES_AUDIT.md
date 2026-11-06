# References audit (P2, P8 of revision 1, 2026-11-03; revision 2, 2026-11-05)

Primary records used: DOI resolution through the Crossref API (publisher metadata), PMLR and JMLR proceedings pages, NeurIPS proceedings BibTeX/metadata files, OpenReview (API v2), the camera-ready header of ICLR PDFs ("Published as a conference paper at ICLR 20xx"), the arXiv API (export.arxiv.org), and the publisher/repository page for data sets. DBLP was not reachable (bot check), so it was not used. Claims were checked against the full text of each source (PDF → pdftotext, searched and read in context), except where stated. Full texts are in the scratch session only, not in the project.

Known traps (brief §5.3): TimeGAN and PSA-GAN are not cited in §1–§3, so neither trap applies.

---

## 1. Entry audit (every `.bib` entry)

| Key | Primary record | Result |
|---|---|---|
| kour2014real | Crossref 10.1109/ICFHR.2014.76 | Template placeholder. Title case and booktitle corrected to the IEEE record; DOI added. Cited only by the template demo section |
| kour2014fast | Crossref 10.1109/SOCPAR.2014.7008025 | Template placeholder. Booktitle corrected; DOI added. Demo section only |
| hadash2018estimate | arXiv 1804.09028 (authors, title confirmed); no peer-reviewed version found (Crossref title search) | Template placeholder. Converted to the authors' `@misc` arXiv form. Demo section only |
| shapley1953value | Crossref 10.1515/9781400881970-018 | Pages 307–318 as in the publisher record; author as "L. S." per record |
| lundberg2017unified | NeurIPS metadata (hash 8a20a862…): pp. 4765–4774 | Verified; volume 30 |
| covert2021explaining | JMLR page v22/20-1316: 22(209):1–90 | Verified |
| sundararajan2020many | PMLR 119:9269–9278 | Verified |
| sundararajan2017axiomatic | PMLR 70:3319–3328 | Verified |
| frye2021shapley | arXiv 2006.01272 v4; PDF header "Published as a conference paper at ICLR 2021" | Verified (ICLR 2021) |
| aas2021explaining | Crossref 10.1016/j.artint.2021.103502: AI 298, 103502 | Verified; ø in Løland protected |
| chen2020true | arXiv 2006.16234; no peer-reviewed version found | `@misc` arXiv |
| janzing2020feature | PMLR 108:2907–2916 | Verified |
| yeh2022threading | PMLR 151:1485–1502 (yeh22a); arXiv 2202.11919 | Verified. Note: v5.1 did not give pages; `yeh22b` is a different paper |
| hooker2021unrestricted | Crossref 10.1007/s11222-021-10057-z: Stat. Comput. 31(6), 82 | Verified |
| merrick2020explanation | Crossref 10.1007/978-3-030-57321-8_2: LNCS, Machine Learning and Knowledge Extraction, pp. 17–38 | Verified (CD-MAKE 2020); LNCS volume number not in the record, left out |
| mamalakis2023carefully | Crossref 10.1175/AIES-D-22-0058.1: AIES 2(1) | Verified; article number not in the Crossref record, left out (not guessed) |
| sturmfels2020visualizing | Crossref 10.23915/distill.00022: Distill 5(1) | Verified |
| haug2021baselines | arXiv 2101.00905 (AAAI-21 workshop, comment); no proceedings record | `@misc` arXiv |
| chen2022explaining | Crossref 10.1038/s41467-022-31384-3: Nat. Commun. 13, 4512 | Verified |
| zhang2026baselines | arXiv 2603.05093 **v2 (2026-05-13)** | **Retitled** since v5.1: now "From Baselines to Transport Geodesics: Axiomatic Attribution via Optimal Generative Flows". Key renamed from the draft's `zhang2026axiomatic` |
| jain2022missingness | arXiv 2204.08945; PDF header ICLR 2022 | Verified |
| fong2017interpretable | Crossref 10.1109/ICCV.2017.371: pp. 3449–3457 | Verified |
| chang2019explaining | arXiv 1807.08024; PDF header ICLR 2019 | Verified |
| agarwal2021explaining | Crossref 10.1007/978-3-030-69544-6_7: ACCV 2020, LNCS, pp. 101–118, issued 2021 | Verified; year = publication year 2021 |
| sridhar2026missingness | arXiv 2603.04831 (v2 2026-03-23); no peer-reviewed version found | `@misc` arXiv |
| tonekaboni2020went | NeurIPS BibTeX: vol. 33, pp. 799–809 | Verified; proceedings title (with "black-box models") used, not the arXiv title |
| crabbe2021explaining | PMLR 139:2166–2177 | DegradX cites the arXiv version; the peer-reviewed ICML version is cited here (brief §5.1) |
| enguehard2023learning | PMLR 202:9329–9342 | Verified |
| liu2024explaining | OpenReview: ICLR 2024 poster | Verified |
| kim2026deltaxai | OpenReview: ICLR 2026 Poster; PDF header ICLR 2026 | Verified (new, novelty re-check) |
| menadjiev2026grail | arXiv 2610.29036 (2026-10-21) | `@misc` arXiv (new, novelty re-check) |
| bento2021timeshap | Crossref 10.1145/3447548.3467166: KDD '21, pp. 2565–2573 | Verified |
| nayebi2023windowshap | Crossref 10.1016/j.jbi.2023.104438: JBI 144, 104438 | Verified |
| nguyen2025tshap | Crossref 10.1007/978-3-032-06078-5_4: ECML PKDD 2025 Research Track, LNCS, pp. 60–77 | Verified. Full title "TSHAP: Fast and Exact SHAP for Explaining Time Series Classification and Regression"; first author "Le Nguyen, Thach". Full text not accessible (abstract read via OpenAlex) |
| kim2026groupsegment | arXiv 2601.06114 v2 (2026-08-21) → **peer-reviewed version** Crossref 10.1145/3799682.3840928: CIKM '26, pp. 2138–2149 | CIKM version cited (brief §5.1). Claims checked on arXiv v2; CIKM text not accessible (flagged) |
| papadeas2026empirical | Crossref 10.1007/978-3-032-19105-2_32: CCIS, ECML PKDD 2025 workshops, pp. 458–473 | Verified; title "An Empirical Evaluation of Factors Affecting SHAP Explanation of Time Series Classification" (v5.1 had no title); CCIS volume not in the record, left out |
| zhao2026tempshap | arXiv 2610.33330 (2026-10-23) | `@misc` arXiv (new, novelty re-check) |
| moosavi2024explainable | Crossref 10.3390/electronics13173497: Electronics 13(17), 3497 | Verified (reused from DegradX) |
| qu2026explainable | Crossref 10.1088/1361-6501/ae319f: MST 37(4), 042002 | Verified; article number 042002 added (DegradX's entry lacked it) |
| turbe2023evaluation | Crossref 10.1038/s42256-023-00620-w: NMI 5(3), 250–260 | Verified (reused) |
| simic2025comprehensive | Crossref 10.1038/s41598-025-09538-2: Sci. Rep. 15, 26607 | Verified (reused); Š and ć protected |
| baer2026class | Crossref 10.1007/978-3-032-19105-2_27: CCIS, pp. 380–395 | Verified (reused) |
| ismail2020benchmarking | NeurIPS BibTeX: vol. 33, pp. 6441–6452 | Verified (reused) |
| queen2023encoding | NeurIPS BibTeX: vol. 36, pp. 32129–32159, DOI 10.52202/075280-1395 | Verified (reused); clears v5.1 §9 "TimeX exact reference" |
| baer2026xaitimesynth | arXiv 2603.06781 | `@misc` arXiv (reused) |
| esteban2017real | arXiv 1706.02633; no peer-reviewed version found | `@misc` arXiv (reused) |
| degradx2026 | arXiv PDF in `docs/` (title, authors) | **% TODO: arXiv identifier unknown** (brief §5.3); `\todo` at first citation. DegradX README cites it as an ACIIDS 2027 submission (conflict C4) |
| degradxrepo | github.com/Myroslav437/degradx at f5bba50 (cloned) | Verified |
| mishchuk2026explaining | Crossref 10.1007/978-981-92-0071-9_15: LNCS, Intelligent Information and Database Systems, pp. 216–231, Springer Nature Singapore, 2026 | Taken from DegradX's bibliography and re-verified; Rafał protected. Paper text not available |
| severson2019data, ma2022real, cui2024data | Crossref (DOIs in entries) | Verified (reused); all 14 / 10 / 10 authors in order |
| saha2007battery | PHM Society mirror of the NASA PCoE repository: "B. Saha and K. Goebel (2007). 'Battery Data Set', NASA Prognostics Data Repository, NASA Ames Research Center, Moffett Field, CA" | Verified; initials only, as in the record |
| hochreiter1997long | Crossref 10.1162/neco.1997.9.8.1735 | Verified |
| friedman2001greedy | Crossref 10.1214/aos/1013203451 | Verified |

Removed from the draft's citations: `zhang2026axiomatic` (renamed `zhang2026baselines`, see above). The draft's other keys (frye2021shapley, aas2021explaining, chen2020true, janzing2020feature, sundararajan2020many, yeh2022threading) were missing from the baseline `.bib` and were created and verified here.

---

## 2. Claim audit (every `\cite` in §1–§3)

Verdicts: S = supported, P = partially supported (rewritten), U = unsupported (removed). Locations: §n.m or "Intro Pn" (paragraph n).

| REF | Key | Location | Claim (short) | Support in the source | Verdict / action |
|---|---|---|---|---|---|
| REF-1 | bento2021timeshap | Intro P1, P2; §2.5; §3.1; §3.4 B1; §3.7 | TimeSHAP carries SHAP to sequences, estimates by sampling coalitions; background is an uninformative sample, often zero or average feature values; authors note a null contribution might stem from the background; event/feature/cell levels and pruning | §3 (perturbation function, Eq. 1: "uninformative input sample … zero vector … or average feature values"); §5 global explanations (null contribution "might stem from our choice of a background"); implementation `calc_avg_event` = median (timeshap 1.0.4 `utils/utils.py`, docstring) | S |
| REF-2 | nguyen2025tshap | Intro P2; §2.5; §3.7 | Background selection understudied; regression attribution lacking; sliding-window groups with exact SHAP; methodology for background selection; exact SHAP for groups | Abstract (publisher abstract via OpenAlex) | S at abstract level; **the background-selection rule and applicability to LSTM/cell players not verified** (`\todo`, Notes) |
| REF-3 | kim2026groupsegment | Intro P2; §2.5; §2.7 | Attributions change with the background set; TimeSHAP dataset-dependent, KernelSHAP most sensitive; mean/zero/noise masking compared | arXiv v2, sensitivity section (Fig. 5 text: "SequenceSHAP and TimeSHAP vary by dataset and KernelSHAP is the most sensitive"; Table 8 "Masking mode Mean Zero Noise") | S on arXiv v2; CIKM text not checked (flagged) |
| REF-4 | papadeas2026empirical | Intro P2; §2.5; §2.7 | Zero and average backgrounds at the same level in most cases, average better in some | Contributions list ("the average and the zero background performances are very often at the same level; however, the average background performs better in some cases"); §4.4 | S |
| REF-5 | sundararajan2020many | Intro P2; §2.1 (draft); §2.2; §3.1 | Attributions add up (efficiency); Baseline Shapley game with a single baseline; CES attributes to dummy features | §2 (Shapley value "add up to v(N)"); §2.2 BShap; §2.1.1/§3 CES and Dummy | S |
| REF-6 | merrick2020explanation | Intro P2; §2.2; §2.7 | Explainers differ only in the reference distribution; attributions are contrastive w.r.t. references; references to be chosen consciously for a contrastive question | §1 (decomposition; "attributions vary … as each method chooses a different reference distribution"); §3 ("differ … only in the reference distribution"); §5 FAE ("references must be consciously chosen by the explainee to obtain a specific contrastive explanation") | S |
| REF-7 | mamalakis2023carefully | Intro P2; §2.2; §2.7 | In regression the baseline defines the question; baselines from different periods → different science questions, substantially different attributions | Abstract; §1 (linear-model example); §3 (four baselines, each with its question) | S |
| REF-8 | frye2021shapley | Intro P3, P5; §2.1 (draft); §2.7; §3.4 B4 | Off-manifold Shapley can give incorrect explanations; two on-manifold remedies (generative model; learned value function); data static (also images) | Abstract; §1 contributions; Fig. 1 (MNIST) | S. Draft sentence "static and tabular" → "static (tabular or image data)" (P, rewritten) |
| REF-9 | hooker2021unrestricted | Intro P3; §2.1 (added) | Permute-and-predict forces extrapolation and misleads under strong dependence | Abstract; §1 | S |
| REF-10 | tonekaboni2020went | Intro P3, P5; §2.4; §2.6; §2.7 | FIT: generator conditioned on the past; AFO samples from bootstrapped marginals to avoid OOD noise; with linear trend, perturbation methods sample unlikely/out-of-domain counterfactuals; classification with planted ground truth | §3 (generator G for p(x_t | X_{0:t−1})); §4 baselines (AFO); §4.1 results ("due to the existing linear trend … perturbation methods are noisy as they sample unlikely or out of domain counterfactuals"); DegradX §2 for planted classification ground truth | S |
| REF-11 | aas2021explaining | Intro P5; §2.1 (draft); §2.7 | Conditional-expectation approximations for dependent features in Kernel SHAP | Abstract | S |
| REF-12 | chang2019explaining | Intro P5; §2.3; §2.7 | Generative in-filling conditioned on the rest of the image, because blur/noise generate inputs far from the data distribution | Abstract | S |
| REF-13 | jain2022missingness | Intro P5; §2.3 | Missingness: pixels cannot be removed; blacking out introduces bias | Abstract | S |
| REF-14 | liu2024explaining | Intro P5; §2.4; §2.7 | ContraLSP: contrastive in-domain counterfactual perturbations; smooth constraint considering temporal trends (mask side); classification | §1 contributions ("incorporates counterfactual samples to build uninformative in-domain perturbation"; "smooth constraint by considering temporal trends"); Fig. 1 classes | S. Stated as mask-side trend handling, as v5.1 §9 requires |
| REF-15 | degradx2026 | 32 places | See §3 of this file | DegradX PDF | S (all checked; see below) |
| REF-16 | moosavi2024explainable | Intro P1; §2.6 | Post-hoc attribution is the most frequently applied method across manufacturing and industrial CPS, applicable to an already trained model | As cited by DegradX §1 (claim reused verbatim in sense) | S. §2.6 first draft said "In prognostics, as in industrial applications generally" → rewritten to the survey's scope (P → fixed) |
| REF-17 | lundberg2017unified | Intro P1, P2 | SHAP; local accuracy (attributions add up to f(x) − φ₀) | §2–§3 (Property 1, local accuracy; φ₀ = f(∅)) | S |
| REF-18 | covert2021explaining | Intro P1; §2.2 | Removal-based explanations characterized by how they remove features, what behaviour they explain, how they summarize | Abstract | S. First draft "differ precisely in how they remove" overstated → "one of the respects" (P → fixed) |
| REF-19 | chen2020true | §2.1 (draft) | Observational vs interventional ("true to the model / data") | §1–§2 | S |
| REF-20 | janzing2020feature | §2.1 (draft) | Interventional (unconditional) expectations are the right notion of dropping features | Abstract | S (cited for the axis, as in the draft) |
| REF-21 | yeh2022threading | §2.1 (draft) | Desiderata for value functions; both classes manipulable in low-density regions | Abstract | S |
| REF-22 | zhang2026baselines | §2.1 (draft, removed); §2.2 | Draft: "casts on-manifold attribution as transport along generative flows". v2 abstract: path selected by transporting a reference distribution to the data distribution, "without claiming data-manifold membership" | Abstract (v2) | **P**: draft sentence deleted (`\revdel`), rewritten in §2.2 to "chooses the path itself by transporting a reference distribution to the data distribution" |
| REF-23 | sturmfels2020visualizing | §2.2 | IG baseline encodes what "missing" means; fixed feature values may carry unintended meaning | Article text ("fixed feature values may have unintended meaning") | S |
| REF-24 | haug2021baselines | §2.2 | On tabular data, the baseline significantly alters the discriminative power of attributions | Abstract | S |
| REF-25 | chen2022explaining | §2.2 | Baseline distributions selected by clustering yield explanations relative to interpretable subpopulations | §3.2 ("Natural scientific questions with baseline distributions … answer questions relative to inherently interpretable subpopulations") | S |
| REF-26 | sundararajan2017axiomatic | §2.2 | IG integrates from a baseline input | IG as described in Mamalakis et al. §2 ("considers a baseline vector") and Sturmfels et al.; IG paper itself not downloaded (cited as the method only) | S |
| REF-27 | fong2017interpretable | §2.3 | Meaningful perturbations replace a region by blur, constant or noise | Method section and its figure comparing the three perturbation operators (blur, constant, noise) | S |
| REF-28 | agarwal2021explaining | §2.3 | Generative inpainter in three attribution methods → more plausible counterfactuals, more accurate attributions | Abstract | S |
| REF-29 | sridhar2026missingness | §2.3 | Missingness bias as output-space artifact; fine-tune a linear head on a frozen model; vision, language, tabular | Abstract; §1 | S |
| REF-30 | crabbe2021explaining | §2.4 | Dynamask perturbs by temporal Gaussian blur or fade to moving average | §2.2 (perturbation operators π_g, π_m) | S |
| REF-31 | enguehard2023learning | §2.4 | ExtremalMask learns perturbations with the mask; classification evaluation | Abstract; v5.1 ledger for evaluation (HMM synthetic + MIMIC-III) | S |
| REF-32 | kim2026deltaxai | §2.4; §2.7 | SWING: window shifted d steps into the past as IG baseline, keeping the path near the data manifold; classification; no ground-truth evaluation | §4.2 ("recent past observation"; baseline = window d steps before); §2 (classifier); §5.2 evaluation metrics | S |
| REF-33 | menadjiev2026grail | §2.4 | Region players; baselines from an on-manifold conditional generator (GP posterior); classification | Abstract; §3.1–3.2; §4 | S |
| REF-34 | nayebi2023windowshap | §2.5 | Groups consecutive time steps into windows to reduce cost | Abstract | S |
| REF-35 | zhao2026tempshap | §2.5 | Cell-level Shapley for forecasting; per-feature training mean described as the standard interventional choice | §3.1 ("the per-feature training mean, the standard interventional/marginal choice") | S |
| REF-36 | qu2026explainable | §2.6 | Survey builds its entire evaluation framework from functionally grounded indicators | As cited by DegradX §1–§2 | S (reused claim, same context) |
| REF-37 | turbe2023evaluation | §2.6 | Occlusion skews the input distribution, a motivation for dedicated evaluation frameworks | As cited by DegradX §1 | S (reused) |
| REF-38 | simic2025comprehensive | §2.6 | Perturbation-based validation depends materially on the perturbation method | As cited by DegradX §1 | S (reused) |
| REF-39 | baer2026class | §2.6 | Perturbation- and ground-truth-based metrics can rank attributions in opposite orders | As cited by DegradX §1–§2 | S (reused) |
| REF-40 | ismail2020benchmarking, queen2023encoding | §2.6 | Ground-truth benchmarks plant class-discriminating structure at known positions | As cited by DegradX §1–§2 | S (reused) |
| REF-41 | baer2026xaitimesynth | §2.6 | The planting construction is available as a package | As cited by DegradX §1 | S (reused) |
| REF-42 | esteban2017real | §2.6 | TSTR procedure | As cited by DegradX §2 | S (reused) |
| REF-43 | mishchuk2026explaining | Intro P6; §2.6; §3.6 | The authors' earlier TimeSHAP study of an LSTM model of battery RUL; case-study object | Title (Crossref) and the brief's description of the paper | S for the description; **its findings, Eq. 3, sequence length, data and architecture not verifiable** (paper unavailable; `\todo` ×6) |
| REF-44 | degradxrepo | §2.6; §3.5; §3.7 | `not_adopted` declaration; ensemble configurations; `m_state`; generator overrides and their grids; L grid; TimeSHAP settings; 10,000 BCa resamples | `configs/declarations.yaml` (attribution.baseline.not_adopted; usability.identifiability_floor; responsiveness.generator_settings; attribution.methods.timeshap); `src/degradx/generator/generate.py`; README (seeds; BCa) | S |
| REF-45 | shapley1953value | §3.1 | Definition of the Shapley value (Eq. 2) | Original text not accessible; the formula matches the definition restated in Sundararajan and Najmi §2. Linearity (§3.3) is cited to sundararajan2020many, §2.1 ("Linearity if … the attributions of the linear combination of two functions … is the linear combination"), where it was checked | S (definition); linearity citation moved to REF-5 |
| REF-46 | severson2019data, ma2022real, cui2024data | Intro P7; §3.6 | MATR, HUST, FORM data sets | As cited by DegradX §3.4 | S |
| REF-47 | saha2007battery | §3.6 | NASA PCoE battery data set | Repository citation line | S |
| REF-48 | hochreiter1997long | Intro P5 | LSTM | Standard | S |
| REF-49 | friedman2001greedy | §3.5 | Gradient boosting | Standard | S |

### DegradX claims (REF-15), all checked against the DegradX PDF

| Location | Claim | DegradX source |
|---|---|---|
| Intro P3 | Mean component carries the larger part of the target-relevant information in degradation data | §1 ("this component carries the larger part of the target-relevant information") |
| Intro P5; §2.6; §2.7; §3.5 | Ten equally accurate models differ more than methods in all but one case; methods ≤ 0.073 in rank agreement, ranges ≥ 0.099; 0.32–0.34 in FORM | §4.4 and Abstract |
| Intro P5 | Average-event background moved TimeSHAP's rank agreement by ≤ 0.04 and changed its place in HUST and FORM | §4.4 last paragraph |
| Intro P7; §2.6 | Profiles fitted to three datasets, validated by distributional comparison and TSTR | Abstract; §3.5.1 |
| §2.4 | Mask-optimizing methods excluded since scores depend on hyperparameters whose tuning is a comparison of methods | §3.6 |
| §3.1 R1 | Normalized position encodes total lifetime, hence the target (leakage) | §3.1.1 (definition of z) |
| §3.1 | Decomposition into mean component, patterns, noise; degradation state computable from data up to t | §3.1, Eq. 1–3 |
| §3.2 A3 | FORM's inserted patterns are temporary capacity recoveries | §3.1.2; §4 intro |
| §3.3 | Pattern-free counterpart; retrieval as average precision of the paired difference | §3.2.1; §3.5.3; declarations scoring.retrieval |
| §3.3 | Ensemble range: range of a score over ten equally accurate models | §3.6; Fig. 1 |
| §3.4 | Pristine window is DegradX's primary baseline | §3.6 |
| §3.5 | Generator, mapping, offset, reference model, recency profile with h := L/4, L := 24, null channels and checks, 300 units 210/45/45, 120 windows | §3.1–3.2, §3.5.2, §3.6, §4 |
| §3.5 | MATR share of attribution on zero-weight channels 0.134–0.198 (IR, temperature carry the state) vs ≤ 0.048 in HUST/FORM | §4.4 (and Table 5, zero-weight mass) |
| §3.5 | FORM pattern term 1.7 × 10⁻⁵ of the mean term's variance; removing it leaves the error unchanged | §4.2; Table 3 |
| §3.5 | Equally accurate models need not learn the function defining ϕ⋆ since channels share one degradation state | §3.6; §5 |
| §3.5 | Fitting splits hold 54 (HUST) and 127 (FORM) cells | §4 intro |
| §3.5 | Bootstrap intervals over units | §4 intro |
| §3.6 | TSTR ratios 1.17 [0.94, 1.34], 1.49 [1.04, 2.29], 1.54 [1.28, 1.74]; MATR/FORM reproduce part, not all, of the dependence | Table 2; §4.1 |
| §3.6 | Null channels: constant plus noise with the capacity-noise autocorrelation; measured values of a channel permuted across units and positions | §3.1.1 |
| §3.6 | Splitting rules: normalization on training units; no input from positions after t | §3.3 "Splitting and use of future information" |
| Fig. 2–4 captions | HUST profile, 120 evaluation windows, shared mapping φ_c(z), reference model | §3.1–3.6 |

Not taken from the DegradX paper (repository only, cited as degradxrepo): the `not_adopted` wording; LSTM sizes; override grids; L grid; TimeSHAP settings; 10,000 BCa resamples. The conditional-importance values of MATR's zero-weight channels (readiness F3, `table4_usability.json`) are not used, since the brief asks for DegradX paper numbers (conflict C6).

---

## 3. Novelty re-check (brief §5.4), searches of 2026-11-03

Queries (extended web search): trend-aware/state-conditional backgrounds for temporal Shapley under nonstationarity; TimeSHAP background choice and masking-baseline evaluation; baseline choice and the contrastive question in regression; on-manifold Shapley for time series via conditional imputation; evaluation of masking baselines against ground truth; SHAP backgrounds in battery RUL. Candidates opened and read (arXiv API, full HTML where available):

| Candidate | What it does | Differentiation | Action |
|---|---|---|---|
| Delta-XAI / SWING, Kim et al., ICLR 2026 (arXiv 2511.23036) | IG with the window shifted d := 1 steps into the past as baseline, piecewise path through historical windows to avoid off-manifold transitions; online monitoring | Gradient-path method, classification; raw past window, not a fitted mean component or state; no ground truth | Added to §2.4 |
| GRAIL, Menadjiev et al., arXiv 2610.29036 (Oct 2026) | Region players (ECG intervals) with counterfactual baselines from a GP-posterior conditional generator; Owen values | Classification; generator-based (B4-type), not state-conditioned; no ground truth for the substitute | Added to §2.4 |
| TempShap, Zhao et al., arXiv 2610.33330 (Oct 2026) | Cell-level, loss-based Shapley for forecasting; training-mean baseline | Unconditional background; no background study | Added to §2.5 (supports "mean is the standard choice") |
| Zhang et al., arXiv 2603.05093 v2 (May 2026, retitled) | Path selection for Aumann–Shapley attribution by transport flows | Static data; no manifold claim; path methods | Moved to §2.2, reworded |
| Mamalakis et al., AIES 2023; Merrick and Taly, CD-MAKE 2020 | Baseline/reference distribution fixes the question answered | Establish the explained-quantity view; no separation of distortion; no conditional background | Added to §2.2 (new thread) |
| Mirò-Nicolau et al., arXiv 2609.30397 (Sep 2026) | Synthetic ground truth by controlled interventions; images, tabular, time series | No mean-nonstationary regression; no background study | Not added |
| Tunyi, arXiv 2607.16236 (IJCAI 2026 XAI workshop) | DAG-faithfulness of marginal-conditioning attribution for time series | Different question (temporal dependency graphs) | Not added |

**No candidate provides contribution 2 (formal trend-aware backgrounds with assumptions, diagnostics and envelope) or contribution 3 (per-background exact ground truth on models of a known function). No stop (brief §8).**

---

## 4. v5.1 §9 "To verify before any citation enters the manuscript"

| Item | Status |
|---|---|
| Spurious-regression reference | Not used (argument stands without it) |
| TimeX (Queen et al., NeurIPS 2023) | Verified (NeurIPS BibTeX) |
| Zeiler & Fergus occlusion | Not used |
| Knee-identification references | Not used (knee alignment dropped with the brief's instrument set) |
| CRP-detection paper (Energy 2021) and regeneration sources | Not used here (DegradX cites Ma et al. 2021 for pattern detection; not needed in §1–§3) |
| Battery dataset composition facts | Taken from DegradX §4 only |
| C-MAPSS composition | Not used (dataset dropped) |
| NARMA formulation | Not used |
| TSHAP algorithmic details | Abstract verified ("exact SHAP values for each group"); applicability constraints **open** (`\todo` in §2.5 and §3.7) |
| Publication status of arXiv preprints | Checked 2026-11-03: GroupSegment-SHAP now CIKM '26 (cited so); Dynamask cited in its ICML version; the others remain preprints |

---

# Revision 2 (authors' comments of 2026-11-05)

Locations refer to the revised paper (§1 Introduction, §2 Related Work, §3 Problem setup, §4 Substitution artifacts, §5 Trend-aware backgrounds, §6 Evaluation methodology). Full texts were fetched into the session scratchpad (not the project) and read with `pdftotext` or as HTML.

## 5. Entry audit of new entries

| Key | Primary record | Result |
|---|---|---|
| cummins2024explainable | Crossref 10.1109/ACCESS.2024.3391130: IEEE Access 12, 57574–57602 (2024); seven authors in order | Verified. Crossref gives "Alexander Sommers" (arXiv: "Alex") and splits "Somayeh Bakhtiari / Ramezani"; the Crossref form is used. Peer-reviewed version cited (arXiv 2401.07871 v1 is the preprint) |
| saarela2024recent | Crossref 10.3390/app14198884: Applied Sciences 14(19), 8884 (2024) | Verified; full text read from the University of Maribor repository copy (dk.um.si; publisher PDF, header "Appl. Sci. 2024, 14, 8884") |
| arabzadeh2025four | Crossref 10.3390/make7040153: Machine Learning and Knowledge Extraction 7(4), 153 (2025) | Verified; full text read from the University of Luxembourg repository copy (orbilu; publisher PDF) |

**Removed from the `.bib`** (no longer cited outside the template's demo section):
- `moosavi2024explainable` — it backed only the common statement "post-hoc attribution is the most frequently applied XAI approach" (Introduction, comment C3) and its echo in §2.6; both are replaced by the evidence of REF-50 to REF-52.
- `hochreiter1997long` — the LSTM citation of the Introduction, a common-knowledge citation (C3); the sentence that carried it was removed under C11, and the LSTM is DegradX's model, cited through DegradX.

**Citations removed from sentences but kept in the `.bib`**: `covert2021explaining` (general sentence of the Introduction removed; still in §2.2), `lundberg2017unified` (removed from the efficiency sentence of the Introduction; still at the first mention of SHAP). `shapley1953value` is kept as the pointer for the Shapley values whose formula was removed under C13.

## 6. Claim audit of new and changed citing sentences

| REF | Key | Location | Claim (short) | Support in the source | Verdict / action |
|---|---|---|---|---|---|
| REF-50 | cummins2024explainable | §1 P1; §2.6 | In a systematic review of 102 studies of explainable predictive maintenance, SHAP was by far the most used method | arXiv v1 §III-C ("we finalized a population of 102 articles"), PRISMA 2020 (abstract); §V-A1 ("By far, SHAP is the most used method seen in our sample") | S. Checked on arXiv v1; the IEEE Access text was not accessible (OPEN_DECISIONS §3 item 6) |
| REF-51 | saarela2024recent | §1 P1 | Across 512 recent XAI applications, SHAP was the most common explanation technique, used in about a third of them | Abstract (512 articles, PRISMA, Web of Science); §4.2 ("SHAP and LIME are the most commonly used local XAI methods (Figure 6)", "SHAP's higher popularity"); Fig. 6 bar chart: SHAP ≈ 177 of 512 papers, LIME ≈ 103 (read at 400 dpi against the axis ticks; the text gives no count) | S. "About a third" rests on the figure, not the text; logged as a judgment call |
| REF-52 | arabzadeh2025four | §1 P1 | In explainable forecasting of energy time series, post hoc methods, SHAP in particular, dominate | Abstract and §7 Conclusions ("Post hoc methods, particularly SHAP, dominate the literature (62% of studies)") over 50 studies | S without the number: the source does not say whether 62 % counts SHAP or all post hoc methods, so it is not quoted |
| REF-53 | frye2021shapley | §1 P3, P5, P6; §2.1 (added sentence); §4 A6; §5 B4; §6.1 ensemble divergence | Off-manifold Shapley values can give incorrect explanations and can differ between two models that evaluate identically on the data; studied on static data | Abstract (incorrect explanations); §3.1, "Algebraic model dependence can be misleading" ("Off-manifold Shapley values provide different explanations for two models in the same equivalence class", models that "behave indistinguishably on the data"); Fig. 1 (MNIST), tabular experiments | S |
| REF-54 | hooker2021unrestricted | §2.1 (rewritten); §4 A1; §4 A6 | Breaking dependence forces extrapolation to regions with little or no data, and permute-and-predict measures can be highly misleading; extrapolation inflates importance for random forests and makes neural-network extrapolations more variable | Abstract ("forcing the original model to extrapolate to regions where there is little to no data"; "highly misleading"); §4 ("In the case of neural networks, these exhibit greater variability; in random forests, extrapolation-induced inflation of importance measures is a larger source of concern") | S. The revision-1 wording "The same extrapolation makes …" was rewritten to Hooker's own claim (C7) |
| REF-55 | tonekaboni2020went | §1 P3 (unchanged claim, REF-10); §4 A1 | On series with a linear trend, perturbation-based methods were noisy because they sampled unlikely or out-of-domain counterfactuals | §4.1 ("due to the existing linear trend in our autoregressive features, perturbation methods are noisy as they sample unlikely or out of domain counterfactuals") | S |
| REF-56 | sturmfels2020visualizing | §2.2 (added clause); §4 A2 | A feature at the baseline value receives no attribution, so the method is blind to the baseline colour | Article, section on constant baselines ("If you use a constant black image as a baseline, integrated gradients will not highlight black pixels as important even if black pixels make up the object of interest. More generally, the method is blind to the color you use as a baseline") | S |
| REF-57 | jain2022missingness | §1 P5; §2.3 (added sentence); §4 A3, A4 | Blacked-out patches skew a convolutional network's predictions toward a few unrelated classes (e.g. crossword puzzle), and the network appears to rely on the masking pattern | §1 contributions ("skews the overall output distribution toward unrelated classes"); Fig. 2 caption (ResNet-50 predicts "crossword", "jigsaw puzzle"; "The model seems to be relying on the masking pattern to make the prediction"); §2.1 ("ResNet's predictions skew … toward a few unrelated classes such as maze, crossword puzzle, and carton") | S |
| REF-58 | fong2017interpretable | §2.3 (added clause); §4 A3 | A mask optimized to delete evidence can instead trigger artifacts of the network | §4.3, "Dealing with artifacts" ("our approach incurs the risk of triggering artifacts of the black box"); Fig. 5 caption (the mask "learns to introduce sharp, unnatural artifacts in the sky instead of deleting the pole") | S |
| REF-59 | degradx2026 | §1 P4 (added clause); §6.2 "DegradX as used", "The premise in the testbed" | Trained models read every channel that enters the target; DegradX calls a sequence a unit; z runs from 0 at an early-life reference to 1 at end of life; DegradX's target depends on the mean component apart from a pattern term absent in MATR and HUST and negligible in FORM | §4.2 ("every weighted channel is used by all ten models of every profile"); §3.1 ("A generated unit consists of a multivariate sequence"); §3.1.1 ("The degradation state runs from 0 at the early-life reference to 1 at EOL"); §4 intro ("Neither profile therefore carries inserted patterns" for MATR and HUST); §4.2 (1.7 × 10⁻⁵) | S. All other DegradX claims are reused unchanged from REF-15; the numbers 0.073, 0.099, 0.32–0.34 and 0.04 now appear once, in §6.1 |
| REF-60 | sundararajan2020many | §1 P2 | Shapley values sum to the difference between the outputs on the input and on the fully substituted input | REF-5 (§2, "add up") | S (reused); Lundberg and Lee dropped from this sentence |

Unchanged citing sentences keep their revision-1 verdicts (REF-1 to REF-49). Sentences whose claim changed only in terminology ("unit" → "sequence", "cell" → "element") were not re-checked, since the claim is the same.

## 7. Novelty record, extension of 2026-11-05 (for "to our knowledge" in §1 P5 and §4)

Queries (web search, standard and extended): masking or baseline artifacts of Shapley attribution on time series with trend or nonstationarity; TimeSHAP background choice under degradation or RUL; characterization of out-of-distribution substitution in time-series attribution. Candidates read at abstract level (arXiv API):

| Candidate | What it does | Differentiation |
|---|---|---|
| Zheng et al., arXiv:2608.25897 (Aug 2026) | Information-bottleneck objective for time-series explanation; prevents trivial and out-of-distribution counterfactuals | A new explainer; no characterization of substitution artifacts, no mean-nonstationarity, no Shapley background |
| Hertel et al., arXiv:2512.20514 (Dec 2025) | SHAPformer: sampling-free SHAP for Transformer forecasters by attention manipulation | Removes features inside the model; no background study |
| Ren et al., arXiv:2105.10719 (v4, May 2023) | Whether baseline values faithfully represent absence, via causal patterns; learns baseline values | Static data; no mean-nonstationarity |

Together with the revision-1 record (§3 above), no work characterizes the artifacts of substitution under mean-nonstationarity. The Introduction states the novelty with "to our knowledge"; §4 uses "to our knowledge, … has not been reported" for A2, A3 (time series), A4 (regression on mean-nonstationary data), A5 and A6 on the same basis.

## 8. Target-journal check (comment C2)

EAAI: "The use of undefined acronyms in the title and in the abstract is forbidden", and the abstract "should clearly specify which is the contribution in AI, and which is the application in engineering" (Elsevier journal page, fetched). Abstract limit 250 words (ScienceDirect Guide for Authors, as indexed; the page returned 403 to direct fetches). The abstract has 248 words including the placeholder descriptions and uses no acronym.
