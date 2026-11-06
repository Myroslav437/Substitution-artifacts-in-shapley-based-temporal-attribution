# Report for the authors — revision 2 (comments of 2026-11-05)

**Result.** `builds/paper.pdf` (21 pages) is one clean paper: abstract, §1 Introduction, §2 Related Work, §3 Problem setup and notation, §4 Substitution artifacts, §5 Trend-aware backgrounds, §6 Evaluation methodology. It compiles with no errors and no undefined citations or references. Outside these sections the main file is byte-identical to the version you commented on, apart from the preamble's single `\input{paper_setup}`. That version is kept in `notes/baseline_r1/`. Details are in `notes/CHANGELOG.md` (one entry per comment, with "applied by analogy" lists); everything open is in `notes/OPEN_DECISIONS.md`.

## Per comment

| Comment | What was done |
|---|---|
| C1 | All review macros, banners, the Notes box and the review switch removed. `review_setup.tex` became `paper_setup.tex`. Unverifiable content left the text and is marked with 8 `% TODO` comments, all listed in OPEN_DECISIONS §3 |
| C2 | Abstract written: 248 words including placeholders (EAAI limit 250), with five `[RESULT: …]` placeholders. It uses no acronym, because EAAI forbids undefined acronyms in the abstract |
| C3 | Moosavi [1] and the LSTM citation removed. §1 now opens with evidence from three verified systematic reviews: SHAP is "by far" the most used method in 102 predictive-maintenance studies; it is the most common technique in 512 XAI applications, about a third of them; and post hoc methods, SHAP in particular, dominate explainable energy forecasting |
| C4 | SHAP, XAI, LSTM and AI are no longer expanded. RQ, TAB, RUL, TSTR and PCoE are still introduced |
| C5 | All nine listed sentences replaced by their content, plus two found by analogy |
| C6 | The mechanism is stated technically in §1 and formally in §3 (Eq. 5), with the artifact classes named |
| C7 | "Extrapolation" claims are now limited to what Frye et al. and Hooker et al. state, which are: incorrect explanations; different explanations for models that agree on the data; forced extrapolation |
| C8 | "Organizing claim" and "as we argue" removed |
| C9 | The thesis is set inline in `\emph`. It is made precise in §3: one background is the best substitute only for mean-stationary data, and its excess error is the squared systematic substitution distance. It is supported by the literature, by DegradX's published facts and by an optional descriptive Fig. 5. §6.1 "How the thesis is tested" ties it to the evaluation: three consequences, the outcomes that would contradict it, and how RQ1 and RQ2 test it |
| C10 | The Introduction is rewritten as one argument in seven steps: method and weak point; explained quantity; structured error; thesis; characterization; solution; evaluation, RQs and contributions |
| C11 | The DegradX numbers left §1 and now appear once, in §6.1. The revision-1 "implications" block was dissolved into the places where each result motivates a choice |
| C12 | *sequence*, *element*, *population* and *state* are used throughout. DegradX's terms are kept only where DegradX is described ("unit" is named once). "unit" dropped from 81 to 4 occurrences and "cell" from 58 to 14. Figs. 2–4 were relabelled through their scripts |
| C13 | §3 is setup only: the Shapley formula and the coalition sampling are removed. The new §4 gives each artifact A1–A6 its description, the related reports or "to our knowledge, not reported", and its instrument. §5 holds the backgrounds and §6 the evaluation |
| C14 | 28 `:=` reduced to 6, all of them assigned values (L, nsamples, h) |

## Judgment calls to confirm (OPEN_DECISIONS §5)

1. Fig. 5 (optional descriptive figure) was made. It shows input data only and is removable.
2. Order inside §6: the evaluation principle comes before the testbed.
3. Ground truth, distortion and difference game are defined in §3, because §4 needs them.
4. RQ1 was reworded as a test of the thesis. The contributions are now five items (a new first item: the formal statement).
5. A2 now separates the blindness that belongs to the background's question, which the ground truth shares, from the artifact itself.
6. Saarela et al.'s "about a third" is read from their figure. Arabzadeh and Frank's "62 %" is not quoted, because it is ambiguous.
7. Shapley (1953) and Friedman (2001) are kept.

## Open

- **ACIIDS paper still missing.** It blocks D2, D3, the case-study details and the list of findings.
- **Other open identifiers.** The DegradX arXiv identifier, the code URL and the TSHAP details remain open.
- **D1–D9 and method constants.** All are unchanged.
- **Template.** It is still PRIMEarxiv, not `elsarticle`.
- **Remaining gap.** That the stationarity assumption *causes* the distortion stays a hypothesis that only the planned experiments can decide. No experiment was added.
