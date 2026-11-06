# TAB journal paper — agent brief, revision 2: the authors' comments on the first draft

*Issued 2026-11-05. It follows brief rev. 1 (`./docs/brief_rev1_2026-11-03.md`), under which the first draft of §1–§3 was written on 2026-11-03.*

*Scope:*
- *revise the paper in `./paper` according to the authors' comments (§2), applying each comment everywhere its reason applies, not only at the quoted passage;*
- *restructure the paper's sections as the comments ask (§3);*
- *write the abstract, with placeholders for the results;*
- *verify every new reference and keep the logs current.*

*No experiments are run. No section beyond the abstract and the current §1–§3 material is written.*

---

## 0. Where things stand

- **The first draft exists.** Brief rev. 1 produced §1 Introduction, §2 Related Work and §3 Methodology, four figures, an audited `.bib`, and a review build with colour highlighting, margin notes, banners and a Notes box.
- **The authors have read it and commented** (§2). They did not review it line by line. Their comments apply generally: wherever the same problem occurs elsewhere and they would write the same comment, fix it there too, and log where.
- **What the comments change about the method of working.** The paper is at an early stage, so it no longer carries review machinery. It is one clean paper. Everything the authors still have to decide, or that could not be verified, lives in `./notes/OPEN_DECISIONS.md`, not in the PDF.
- **What the comments do not change.** The design of brief rev. 1 §2–§3 is still binding: the backgrounds, instruments, models, the DegradX usage and extensions, and the D1–D9 defaults. So are its rules on numbers, references, tense and scope (rev. 1 §4.3–§4.5, §5). Rev. 1 §7 (review build) and §2.1's instruction to *display* the thesis are superseded.

---

## 1. Inputs and precedence

All paths are relative to the working directory.

| Input | Where | Use |
|---|---|---|
| **Authors' comments** | §2 of this brief | Binding; they win over everything else |
| Current paper (Overleaf project) | `./paper/_arXiv__Substitution_Artifacts_in_Shapley_Based_Temporal_Attribution/`: `templateArxiv.tex` (main), `references.bib` (audited), `review_setup.tex`, `review_notes.tex`, `media/*.pdf` | The text to revise. **Read `./builds/paper_clean.pdf` first:** it is the version the authors commented on |
| Figure scripts | `./paper/figures/scripts/` (see its `README.md`) | Regenerate every figure whose terms or labels change |
| Brief rev. 1 | `./docs/brief_rev1_2026-11-03.md` | The design (its §2–§3), binding decisions, and the rules on numbers, references, tense and scope |
| Notes from rev. 1 | `./notes/`: `CHANGELOG.md`, `REFERENCES_AUDIT.md` (entry and claim logs, REF-n, novelty re-check), `OPEN_DECISIONS.md` (D1–D9, open constants, unverified items, unresolved conflicts), `OUTLINE.md`, `STYLE_PROFILE.md`; baseline of rev. 1 in `./notes/baseline/` | What was done and why; what is verified; what is open |
| Authors' style preferences | `./docs/writing_style_preferences.md` | Binding writing rules (they win over the style papers) |
| Style profile and style papers | `./notes/STYLE_PROFILE.md`; `./style/` (DegradX and two FLICS 2026 papers) | The DegradX Introduction and Related Work are the closest in-house model of the target style |
| Initial methodology | `./docs/Masking_Backgrounds_Methodology_v5.1.md` | Content source for the problem, the artifacts (its §1.2, §3.3), the backgrounds (§3.4–§3.5) and the case study (§3.14), as amended by brief rev. 1 §3. It predates DegradX |
| Readiness review | `./docs/masking_degradx_readiness_2026-11-03.md` | The redesign around DegradX; overrides v5.1 |
| DegradX | `./docs/_arXiv__DegradX__…pdf`; repository `github.com/Myroslav437/degradx` at commit `f5bba50` | The only source for anything said about DegradX, and the source of the figure data |
| ACIIDS paper | Was **not** in `./style` on 2026-11-03. Check `./style`, `./docs` and `./paper` again | The only source for its published findings (case study, B1 as its Eq. 3, its sequence length for D2) |

**Precedence:** the authors' comments (§2) > this brief > brief rev. 1 > `writing_style_preferences.md` (writing) and the readiness review (design) > v5.1 > the current draft text. Log every conflict you resolve in `./notes/CHANGELOG.md`; list every conflict you cannot resolve in `./notes/OPEN_DECISIONS.md`.

---

## 2. The authors' comments, and what to do about each

The comments are quoted verbatim. "What to do" is the brief's reading of each comment; where the comment and the reading differ, the comment wins. The places listed under "Also here" are those already known to have the same problem in the current draft; they are a starting point, not a complete list.

### C1. Remove the review machinery

> As this paper is currently in the initial stage, no need to highlighligh in the paper changes, revwhys and provide notes for authors (includeing new section, etc.) - they should be removed.

**What to do**
- Remove from the paper every `\rev`, `\revw`, `\revwhy`, `\revwhyw`, `\revdel`, `\dec`, `\newsectionbanner` and `\todo`, keeping the text inside them as plain text. Remove the Notes box (`review_notes.tex` and its `\input`) and the `\ifreview` switch.
- Reduce `review_setup.tex` to the packages and macros the text needs (natbib with numbers, amsmath/amssymb, array/tabularx, the macros `\mask`, `\EM`, `\ED` if they survive), and drop xcolor, tcolorbox and todonotes unless something still needs them. You may rename the file (for example `paper_setup.tex`); the preamble keeps a single `\input` line, and the template files stay untouched.
- The defaults of D1–D9 stay written in the text, without markers. Everything that the Notes box held moves to, or stays in, `./notes/OPEN_DECISIONS.md`: open decisions, method constants that no input fixes, unverified items, unresolved conflicts.
- Nothing unverified may appear in the text, and visible notes are no longer allowed. Where a passage depended on content that could not be verified (the ACIIDS paper, TSHAP's full text), write it without the unverified specifics. Then mark the place with a LaTeX comment (`% TODO: …`, invisible in the PDF) and list it in `OPEN_DECISIONS.md`. The DegradX arXiv identifier keeps its `% TODO` in the `.bib`.
- One build only: the clean paper. Review and latexdiff builds are not required.

### C2. Write the abstract

> The abstract with placeholders should also be written.

**What to do**
- Replace `\lipsum[1]` with a full abstract. Results do not exist yet, so every result appears as a visible placeholder of one uniform form, for example `\textbf{[RESULT: size of the distortion under the training-mean background]}`. Everything else is written in full.
- Follow `writing_style_preferences.md` §2.7 and §2.9. The abstract must be understandable without the paper. It leads with the contribution, not the implementation, and names the evaluation means before the results. It states what each finding means ("…, indicating that …", with the finding as a placeholder) and ends with the practical use. It says that the measures it mentions are introduced here.
- No citations. Check the word limit for abstracts in the Guide for Authors of the target journal (EAAI, D9) and keep within it.
- The abstract tells the same story as the restructured Introduction (C10).

### C3. Common-knowledge citations; evidence that SHAP-based methods dominate

> In the introduction, references like [1] are quite useless as it is common statement so such references might be dropped. Better indicate that SHAP-based methods are the most popular based on some surway papers or other such data. In this way we target the question on "why don't we just use other methods on such data" - the main-chose/most popular choise argument is strong here.

**What to do**
- Drop citations that only support common statements. [1] is Moosavi et al. 2024, cited for "post-hoc attribution is the most frequently applied XAI approach".
- Open the Introduction with evidence that SHAP-based attribution is the most used family, preferably with figures from a survey or review: for example, the share of reviewed studies using SHAP, in time-series XAI, prognostics or industrial XAI. The point is to pre-empt "why not just use another method on such data": the method affected is the one most practitioners use.
- Find the evidence yourself and verify it under brief rev. 1 §5 (entry audit and claim audit against the source's own text; log it in `REFERENCES_AUDIT.md`). Possible leads, **none verified, do not rely on these titles or on memory**: the surveys already in the `.bib` (Qu et al. 2026 on XAI for RUL; Moosavi et al. 2024 on industrial XAI), in case they count methods; reviews of XAI for predictive maintenance or prognostics and health management; reviews of XAI for time series; bibliometric studies of SHAP use. Cite only what the source's text supports, with its numbers if it gives them.
- **If no source supports the popularity claim, do not make it.** Report this, with what you found, in `OPEN_DECISIONS.md`.
- **Also here:** apply the same test to every citation in §1–§3 that backs a statement any reader in the field accepts without one. Candidates: the LSTM citation in the Introduction; the citation of Shapley (1953) for a formula that C13 removes anyway. Keep citations that support a specific claim.

### C4. Do not expand SHAP

> "which carries SHapley Additive exPlanations (SHAP)" - it is common shortening and no need to provide it here.

**What to do**
- Remove the expansion. Use "SHAP" as a known name.
- Apply the same criterion to other abbreviations that every reader of the target venue knows (decide XAI and LSTM explicitly and log the decision). Abbreviations specific to this paper or to a sub-field (TAB, TSTR, RUL, PCoE, …) are still introduced at first use (`writing_style_preferences.md` §4.4).

### C5. No meta-sentences

> "The choice matters for a second reason, beyond sensitivity" - such sentences increase cognitive load on the reader and are useless. Better to write somithing like "Beyond sensitivey, <and write what other effects the background selection migh have>." e.g..

**What to do**
- Replace sentences that announce content with the content itself, attached to the transition. For example: "Beyond sensitivity, the background also fixes which quantity the attribution explains, because …".
- **Also here** (current draft; decide each, keep only what carries a claim):
  - "This is the organizing claim of the paper:" (see C8);
  - "We address three research questions (RQs):";
  - the opening of the Methodology, "This section first fixes the notation and the quantity an attribution explains. It then states …";
  - "One instrument is defined per artifact.";
  - "Three results of DegradX determine the design.";
  - "Five predictions test the selection guide on existing arms.";
  - "The findings are stated for TimeSHAP, but the argument for their generality covers …";
  - "Table 2 lists the backgrounds by the quantity each one explains, following Equation (3).";
  - "Each is stated in its general form, indexed by the mean component rather than by position, and then in the monotone instance evaluated here."
- A short roadmap sentence at the start of a long section may stay only if it orients a reader who needs it; otherwise remove it.

### C6. State the substitution-distance argument technically

> "an unconditional background is systematically far from the observations wherever the mean component is far from it." it is important take. I think we should write it more technically or detailed, and indicate that it can producde hypotesised artefacts.

**What to do**
- This is the mechanism of the paper. State it precisely where it is introduced, then formally where the notation exists (§3, C13).
- One way, built from the current draft: masking element (t, c) with background b perturbs the input by the substitution distance d = |x_{t,c} − b_c|. With x = m + r, where m is the mean component and r is localized patterns plus noise, its systematic part is |m_{t,c} − b_c|. Under an unconditional background, b_c does not change with the state, while m does under mean-nonstationarity. The systematic part is therefore near zero only where the mean component is near b and grows with their difference. A coalition then combines observed values from one state with substitutes that correspond to another state, so the model is evaluated on combinations its training data do not contain.
- State the consequence: the model's response to those inputs enters the attribution. Name the hypothesized artifacts it can produce, at least by class: magnitude (inflation far from b, blindness near b), semantic (spurious localized patterns, a directional offset of the prediction) and propagation (recurrent carry-over, compounding across coalitions). Define them in the artifacts section (C13).

### C7. Remove "its output is an extrapolation"

> "where its output is an extrapolation" - no clear why do we write it. The model's output may not only be extrapolation. Some questionable info and it should be either rewritten or removed.

**What to do**
- Remove the claim, or rewrite it to what the sources support. Frye et al.: off-manifold Shapley values can give incorrect explanations. Hooker et al.: permute-and-predict measures can be highly misleading under strong dependence among features. In general terms: outside the support of its training data, nothing constrains the model's output, so attributions computed from such evaluations need not reflect the model's behaviour on real data. Check the wording against the verified claims REF-8 and REF-9 in `REFERENCES_AUDIT.md`.
- **Also here:** every sentence that asserts a specific behaviour of the model off its support (for example "the model's arbitrary reaction", "where training does not constrain its output") must say no more than the sources or the argument support.

### C8. Nothing that speaks from the authors' side

> " This is the organizing claim of the paper" - it is organising in the author's head, not for the reader. Such info should not be in the paper.

**What to do**
- Remove it. **Also here:** remove any other statement about the paper's own organization or intent that gives the reader nothing (for example "as we argue" if no argument follows at that point).

### C9. The thesis must be supported, and formatted inline

> The take "The explainer assumes stationarity where the model does not." is not investigated or proven/shown in a sufficient manner which is critical for that paper. Also, such formatting as is currently for that line is not acceptable and should not be used. If it needs to be outlined use \emph or bold.

**What to do**
- **Formatting.** No centred display. If the sentence is set off at all, use `\emph{…}` or bold inline.
- **Substance.** This is the most important comment. The thesis must be (a) made precise, (b) argued, (c) supported by what is available without experiments, and (d) explicitly tied to the evaluation that tests it. It is a thesis whose consequences the paper tests, not a result. Phrase it as such and keep every claim within the tested scope.
  - (a) **Make it precise** (a suggestion; improve it if you can). An unconditional background uses one substitute for every position and state. For squared substitution error, the single best substitute is the population mean. It coincides with the best state-wise substitute, E[x | state], at every state only if the mean component does not vary, that is, if the data are mean-stationary. Using one substitute everywhere therefore treats the data as if they were mean-stationary: this is the sense in which the explainer assumes stationarity. The model does not. It is trained on a population of sequences whose target variable depends on the mean component, and it reads that component.
  - (b) **Argue it** in the Introduction (C10), and formally in the problem setup or the artifacts section (C13).
  - (c) **Support it.** Use the verified literature: FIT's observation that, on series with a linear trend, perturbation methods sampled out-of-domain counterfactuals; off-manifold Shapley; missingness bias. Use DegradX's published facts: the mean component carries the larger part of the target-relevant information; trained models use every weighted channel; the pattern term is negligible against the mean term. **Optional** (a judgment call, logged for the authors in `OPEN_DECISIONS.md`): a descriptive figure, generated by a committed script from DegradX generated units, of the systematic substitution distance |m − b₁| against the degradation state for each profile. It would show that the premise holds in the testbed data. It describes the input data, not an attribution result. Do not report any attribution result.
  - (d) **Tie it to the evaluation.** State in the methodology which outcomes would support or contradict the thesis. If the stationarity assumption is what distorts the attributions, the distortion D_b under unconditional backgrounds is structured by |m − b| (the A1, A2 and A4 signatures). It is also smaller under the backgrounds that drop the assumption (TAB, and the oracles B2\*, B3\*), with the explained mass reported beside it. P-GEN tests the general, non-monotone form. RQ1 and RQ2 should read as tests of these consequences.

### C10. Restructure the Introduction as one argument

> Also, current introduction seems not very logical and is not easy to follow. The main "oraganising parts" are not deduced from the domain and generally are disconnected (characterisation of artifacts, explainer assumption of sationarity, TAB are not following from each other and not distinguishable as main points of the paper). A more logical structure would be something like (just initial thoughts, can be updated) - that we have this problem that in shap that the missing values should be substituted. Then mention the more detailed problem with assumption of mean-nonstationarity, more detailed arguments that it exists and then then provide the "The explainer assumes stationarity where the model does not." claim. Then we can say that therefore we try to systematically describe/organise/check such artifacts (if i understand correcly - the first in the literature). And then mention that we propose that based on this we also propose a solution for such situations. Claims like "Detrending the inputs does not remove the problem" etc. should be used as argurments or leading to such problems, because for how we don't have a story but rather a bunch or statements that are neither logical or easy to follow. For sure it is the initial draft on the oranization of claims and can be changed if it can be improved.

**What to do** — rewrite the Introduction so that each paragraph follows from the previous one and the three main points (the problem and the thesis, the characterization, the solution) are distinguishable. A possible order, refining the authors' outline:
1. **The method and its weak point.** SHAP-based attribution is the most used family (C3). It measures importance by removing input elements, which a trained model cannot receive, so removed elements are substituted by a background. The background is left to the user: TimeSHAP's zero or average; TSHAP calls background selection understudied; GroupSegment-SHAP and Papadeas et al. measure sensitivity.
2. **Beyond sensitivity** (C5): the background fixes which quantity is explained (efficiency; Merrick and Taly; Mamalakis et al.).
3. **Why mean-nonstationarity makes it a structured problem** (C6). Then the arguments that the problem is real and cannot be avoided. The mean component carries target-relevant information, so the model legitimately reads it. Detrending is not a way out (use it here as an argument, not as a free-standing statement): explaining a detrended model explains a different model; detrending only at explanation time recreates the off-support evaluation; removing the mean component removes the signal the target depends on. The literature has observed the effect (FIT, off-manifold Shapley).
4. **The thesis**, inline and emphasized (C9), as the conclusion of paragraph 3.
5. **Therefore, a systematic characterization** of the artifacts this mismatch produces, and of how each can be detected. Before writing "the first", check the novelty record (`REFERENCES_AUDIT.md` §3, re-check of 2026-11-03), extend it if needed, and phrase with "to our knowledge".
6. **Based on the characterization, a solution:** trend-aware backgrounds condition the substitute on a low-dimensional state, dropping the stationarity assumption without a generative model. The learned imputer is the established alternative it is compared with.
7. **How it is evaluated, briefly.** The ground truth must be known per background, so the models are trained to reproduce a known function, and the evaluation uses DegradX as the testbed (one sentence: what it supplies). The RQs follow. Then the case study, the contributions (one per main point, plus the evaluation design and the case study) and the scope (mechanism general; experiments on the monotone instance plus the P-GEN probe; battery RUL as the flagship application through DegradX's profiles).
- The contributions and the RQs must map onto this story. Keep the Introduction within 1.5–2 pages.

### C11. Keep the Introduction at the level of the argument

> Sentences like " Its own results, however, show that this ground truth cannot rank backgrounds on trained models. " are better fit to methdology or related works. The introduction should not be that detailed. Also, the RQs do not depend on it and for better following the DegaradX should be mentioned as instrument used and not describe it here in details. There are a lot of similar issues but the core idea that we want to tell here well-argued, logical story where the motivation of the paper is clear, and additing some random information like "Ten equally accurate long short-term memory (LSTM) networks [19] differ more than the attribution methods do in all but one case: in rank agreement, for instance, the methods differ by at most 0.073, whereas each method's range over the ten models is at least 0.099. Switching TimeSHAP's background moved its rank agreement by at most 0.04, and this was enough to change its place among the methods in two of the three profiles [14]. " - is redundant and not logical.

**What to do**
- Remove the DegradX results from the Introduction: the 0.073, 0.099 and 0.04 numbers and the ensemble disagreement. They already appear in Related Work (§2.6) and in the Methodology ("What DegradX's results imply"), where they motivate the design. Check that they still appear there once, where they are used, and nowhere twice.
- In the Introduction, DegradX is the testbed used, described in one sentence by what it provides.
- **Also here:** in every section, remove details that do not serve the point being made at that location. Move a detail to where it is used, or delete it.

### C12. Domain-neutral terms outside the DegradX parts

> In methodology and everywere else we used therms "units", " cells" etc. It seems like they are taken from the DegradX terminology and probably are Battery-specific. We should not assume the battery domain in the paper everywehere except the specific validation on DegradX so these terms should be double-checked and, if needed, changed to the better ones.

**What to do**
- The current draft uses "unit" about 80 times and "cell" about 55 times in §1–§3. "Cell" has two meanings there, which also has to be fixed: an element (position, channel) of a window, taken from TimeSHAP's "cell level", and a battery cell in "measured cells".
- Choose domain-neutral terms for the general sections, check them against the attribution and time-series literature, use them consistently, and record them in the notation table. A starting proposal:
  - **unit** → *sequence* (or *series* / *instance*, whichever the literature uses for one multivariate time series of a population);
  - **cell (position, channel)** → *element* or *input element*. Keep "cell level" only as the name of TimeSHAP's explanation granularity, anchored once;
  - **battery cells** → *battery cells*, only in the DegradX, measured-data and case-study parts;
  - in general sections, also replace "life", "early or late in their life", "end of life", "fleet", "pristine" and "degradation state" with neutral terms (for example "early or late along the mean component", "population"). Keep the DegradX terms where DegradX's own objects are described, and say once that they are DegradX's terms.
- Regenerate the figures whose labels or captions use the old terms (for example "training units", "departure of the unit", "the unit's own past") through their scripts (`writing_style_preferences.md` §5.5–§5.6).

### C13. Problem setup without common knowledge; a separate section for the artifacts

> I like the problem setup and notation section, but note that we do not want to write "common knowledge" (e.g., how SHAP works) here. After that, however, I would expect the description of the hypotesized substitution artefacts, their description, if such artifacts were reported and how they can be tested. Hence, I would rather have a separate section with this and methodology would descripbe how these artefacts would be evaluated in this paper. If some formal stuff needed for that artifacts setion, we can easily intoroduce it in that previous section.

**What to do** (see the section plan in §3)
- **Problem setup and notation.** Keep the formal setup. Remove what is common knowledge: the Shapley formula (current Eq. 2), how SHAP and TimeSHAP compute values, sampling of coalitions. Cite instead. Keep only what later sections use: the masking operator and value function; efficiency as the reason the background fixes the explained quantity (one sentence and the equation, if the equation is used later); the background function and R1–R3; the mean component, the state and the state index; the substitution distance; the formal reading of the stationarity assumption (C9 a); the notation table.
- **A new section, "Substitution artifacts"** (hypotheses). For each of A1–A6:
  - its description, in the general form indexed by the mean component or state, with the monotone instance;
  - whether it, or a related effect, has been reported, with verified sources (for example missingness bias in images, out-of-domain counterfactuals on trended series in FIT, incorrect off-manifold Shapley explanations). Where nothing has been reported, say so with "to our knowledge";
  - how it can be tested: its observable signature and the instrument M1–M6 in general form.

  The state-band geometry (Figure 1) belongs here.
- **Methodology** then describes how this paper evaluates the artifacts: ground truth per background, distortion, explained mass and ensemble divergence; DegradX as used and its extensions; the model families and the function-identity check; the realization of the instruments; the envelope predictions; statistics; the measured arms; the case study; the implementation.
- **The backgrounds**, TAB included, are the proposed solution, not the evaluation. The recommendation is a section of their own between the artifacts and the methodology. Another arrangement is allowed if it reads better; log the choice.

### C14. ":=" only for assigned values

> Regarding the usage of ":=" - it is clearly used incorrectly in the paper. In all cases we should use simple "=". The ":=" appears only if we specify some value to some parameter. E.g., we define the learning rate and how it is used in the formulas, and if in our paper we use, for example 0.01, then the notation of asssignemnt ":=" can be used in that specific case

**What to do**
- Use "=" for every definition. The current draft has 28 occurrences of ":=" in §1–§3. Change to "=" those that define a quantity:
  - the masking operator; $v^f_b(S)$; $\phi_i(v)$ (removed anyway under C13); $\EM_b$; $h_u$; $d_{u,c}$; $\phi^\star_b$ and $v^g_b$; $D_b$; $\Delta_b$; $\ED_b$; $\mathrm{M5}(\ell)$;
  - $b^{\mathrm{state}}$, $\hat m^{(u)}_c$, $b^{\mathrm{traj}}$, $b^{\mathrm{2c}}$, $S_c$;
  - $g(x_W)$, $x^0_c = \varphi_c(0)$, B2\*, B3\*, $y_{\mathrm{obs}}$, $y_{\mathrm{ev}}$.
- Keep ":=" only where a specific value is assigned to a parameter: $L := 24$, $L := 96$, $\textit{nsamples} := 32{,}000$, and the half-life $h := L/4 = 6$, written as DegradX writes it.
- This agrees with `writing_style_preferences.md` §4.5; the first draft applied it wrongly. `./notes/STYLE_PROFILE.md` already states the rule correctly.

### Closing remark of the authors

> Please note that the paper was not reviewed line-by line and these comments apply generally to the whole paper. If there are similar situations in other places and I would probably write the same comment on them they can also be updated

**What to do:** after the comment-by-comment pass, read the whole paper once per comment (C3–C14) and fix every further instance. Log each one under its comment in the CHANGELOG ("applied by analogy: …").

---

## 3. Target structure (a proposal; improve it if a better order exists)

| § | Section | Content | Pages |
|---|---|---|---|
| — | Abstract | C2 | — |
| 1 | Introduction | C3–C11; the argument of C10 | 1.5–2 |
| 2 | Related Work | The current threads, revised under C3–C8, C11 and C12. It keeps the DegradX results that motivate the design (§2.6) and the gap (§2.7) | 2–2.5 |
| 3 | Problem setup and notation | C13; formal items needed by §4–§6; the formal stationarity reading (C9 a) | ≈ 1.5 |
| 4 | Substitution artifacts | A1–A6: description, prior reports, testable signature and instrument; state bands (Fig. 1) | ≈ 2 |
| 5 | Trend-aware backgrounds | B0, B1, B-pristine; TAB-state, TAB-traj with assumptions and diagnostics; oracles; B2c; B4; the explained quantity of each (Table 2, toy figure, TAB figure); selection guide | ≈ 2.5–3 |
| 6 | Evaluation methodology | Ground truth per background, distortion, explained mass, ensemble divergence; how the thesis is tested (C9 d); DegradX as used, its implications and extensions; models; instruments on DegradX (table); envelope predictions; statistics; measured arms; case study; implementation | ≈ 4–4.5 |

- The template's demo section ("Examples of citations, figures, tables, references"), the conclusion placeholder and the acknowledgments stay as they are, after the new sections.
- With the new numbering, references to later sections are still not allowed (`writing_style_preferences.md` §4.7). Cross-reference earlier sections only where it removes ambiguity.
- Update `./notes/OUTLINE.md` to the new structure before rewriting: headings, then one line per paragraph with its claim and citations.

---

## 4. Rules that still apply (from brief rev. 1 and the preferences)

- **No fabrication.** Numbers are only published DegradX values (cited), declared constants (written with ":=" per C14) or values from other cited sources. No results; placeholders only in the abstract (and, if needed, in the contribution list, in the same form).
- **References.** Every new or changed citing sentence is checked against the source's own text and logged (REF-n) in `REFERENCES_AUDIT.md`. Every new `.bib` entry is checked against its primary record: Crossref DOI, publisher page, PMLR/NeurIPS/OpenReview, the arXiv API. Claims already verified (REF-1 to REF-49) may be reused as they are; if a sentence changes what it claims, re-check it. Remove from the `.bib` any entry no longer cited outside the template's demo section, and log its removal.
- **Terminology** (`writing_style_preferences.md` §4.2): "mean component" (not "level", decision D4), "state index", "ground truth", "target variable", "testbed" for DegradX, "calibrated and validated profiles", "pattern-free counterpart", plus the neutral terms chosen under C12.
- **No forward use** of terms, symbols or definitions; abbreviations introduced at first use except well-known ones (C4).
- **Tense and scope.** Present tense for the method; no proposal language; nothing claimed beyond the tested scope.
- **Design.** Brief rev. 1 §2–§3 and its D1–D9 defaults stay binding; the defaults are written without markers (C1).
- **Do not touch** the template files (`PRIMEarxiv.sty`, the title and author block), the acknowledgments, or the template's demo section.
- **Figures.** Generated by the committed scripts; every label and number comes from the text or from DegradX; schematics marked as such; captions describe, the text interprets.

---

## 5. Practical notes from the previous run

- **DegradX repository.** Clone `github.com/Myroslav437/degradx` and check out `f5bba50`. Set `DEGRADX_REPO` to the clone for the figure scripts. They need Python with numpy, scipy, scikit-learn, pandas, pyyaml and matplotlib; the system Python lacked pyyaml and pandas, so use a virtual environment. The figure README explains the placeholder pool for the `null_permuted` channel.
- **Reference lookups.** The Crossref API and the arXiv API work from the shell. DBLP sits behind a bot check. Most PDFs can be fetched and searched with `pdftotext`. Springer pages need a login; OpenAlex gives publisher abstracts when nothing else is reachable.
- **LaTeX.** MiKTeX pdflatex and bibtex. `unsrtnat` is needed for `\citet`. BibTeX reads an `@` inside a `.bib` comment as the start of an entry.
- **Byte-exactness.** When rewriting `templateArxiv.tex`, keep everything outside the revised sections byte-identical to the current file (trailing spaces included). A full-file rewrite stripped them once.

---

## 6. Stop and report

Write down the state, the options and your recommendation.

- **No verifiable source supports the claim that SHAP-based methods are the most used** (C3): continue without the claim and report.
- **The thesis cannot be supported or tied to the evaluation without new experiments** beyond the optional descriptive figure (C9): write what the available evidence supports, report the gap, and propose options. Do not add an experiment to the design.
- **A comment, read literally, contradicts a binding design decision** of brief rev. 1, or the restructuring requires a methodological change that neither brief lists.
- **A neutral term would misdescribe DegradX:** keep DegradX's own term where DegradX is described, and report.
- **The ACIIDS paper is still missing:** continue (C1 handling) and keep its items in `OPEN_DECISIONS.md`.

---

## 7. Deliverables

- **Before any edit,** a snapshot of the current paper in `./notes/baseline_r1/` (the state the authors commented on).
- **The revised `./paper`:** clean, with no review machinery; with the abstract; restructured as in §3; terminology, notation and citations fixed throughout; figures regenerated by their scripts.
- **One PDF,** `./builds/paper.pdf`, compiling with no errors, undefined references or undefined citations. Update `./builds/build.sh` to produce it.
- **Notes:**
  - `./notes/CHANGELOG.md`: a section "Revision 2 (authors' comments of 2026-11-05)" with one entry per comment C1–C14. Each entry says what changed and where, and lists "applied by analogy" instances.
  - `./notes/REFERENCES_AUDIT.md`: new entries and claims, removed citations, any novelty check added for "the first".
  - `./notes/OPEN_DECISIONS.md`: now the only record of open decisions, open constants, unverified items, unresolved conflicts and judgment calls. In particular: the popularity evidence, the optional descriptive figure, the chosen neutral terms, the section arrangement, and the abbreviation choices.
  - `./notes/OUTLINE.md`: the new structure.
- **A short report** for the authors: what was done per comment, the judgment calls, and what remains open.
