# Research and writing style preferences: Myroslav Mishchuk

*Compiled 2026-11-03 from the paper-writing and editing conversations of the project "[SCI] SHAP Masking" (July–October 2026) and from the project's working notes. Every rule below restates something the author asked for or corrected. Examples quote real corrections.*

**How to use this file**
- It is binding for any agent writing or editing the author's papers.
- Where it conflicts with a style-guide paper, this file wins.
- Where it conflicts with the brief of the current task, the brief wins.

---

## 1. Research and argument

1. **Justify every design choice** with evidence, a measurement or a cited source, never by assertion.
2. **Keep claims inside the tested scope.**
   - A mechanism may be argued generally. Results are stated for what was tested.
   - A claim that bridges synthetic and measured data is hedged and rests on the measurement that supports it (e.g. TSTR).
3. **State methods in general terms.**
   - Domain vocabulary ("battery", "remaining useful life") appears only where the application is discussed, never in general-scope sections.
   - A general method must not read as domain-specific. TAB is defined for any mean-nonstationary series; battery capacity is one instance of its state index.
4. **Give each dataset, experiment and model a stated purpose.**
   - Nothing is included for volume.
   - An experiment should serve more than one question where it can.
   - Material peripheral to the contribution stays short: for example, three attribution methods, reported in aggregate only.
5. **Call out contradictions and logical inconsistencies, and fix them.** Do not paper over them. Never reintroduce an error that was already corrected.
6. **Add no unsupported content.**
7. **Be objective without being harsher than the evidence.**
   - Where a result is imperfect, state what holds first, then the limitation.
     - Example: "lacks part of the dependence" → "reproduces part, but not all, of the dependence".
   - Ease statements that would need further experiments to support and that needlessly undermine the contribution.
     - Example: "scores depend more on which model was trained than on the method" was eased.
   - Never skew a result.

## 2. What goes into the paper

1. **Only what was used and run.** Keep out:
   - internal rules;
   - thresholds that every reported result satisfied;
   - stop rules and selection criteria;
   - datasets that were dropped;
   - measures that were defined but not run;
   - hypothesis tests that are not part of the final configuration;
   - any "earlier" or "later" version. The paper has one version: the one that was run.
2. **No filler** such as "we report X" or "we verify X".
   - Keep such a sentence only if it explains a decision: X was checked, Y was found, so Z was done.
3. **Concrete values instead of "a declared X"** wherever the value is a constant of the method. Keep symbols where a formula needs the abstraction.
4. **Not every computed number.**
   - Report only numbers that serve the narrative or a research question.
   - Do not repeat in the text numbers that a table already shows.
5. **Results.** Say what a number means, so that a reader of the paper alone can interpret it.
   - Never compare it with an internal target the reader has not been given. The "so what?" test must have an answer.
6. **Discussion.** Draw conclusions and hypotheses from the results; do not describe them again.
   - Limitations and future work go in one subsection, as prose, not as a list.
7. **Abstract.** It must be understandable to someone who has not read the paper.
   - State what each finding means ("…, indicating that …").
   - Lead with the contribution, not the implementation.
   - Name the evaluation means before the results.
   - End with the practical use.
8. **Conclusion.** Like the abstract, it states the practical value.
9. **Introduced measures are flagged.** Measures or scores the paper introduces are said to be introduced, including in the abstract and conclusion.
10. **Related Work: chain and synthesis.**
    - It reads as one argument, not a list of claims.
    - Each paragraph follows claim → cited example → cited limitation, so every cited work comes with a clear reason why it does not solve the problem.
    - The closing paragraph is a synthesis derived from the reviewed works, placing the contribution in the gap they leave. Describing the artefact belongs in the Introduction.
11. **Related Work: coverage.**
    - Works cited in the Introduction that belong to a Related Work thread also appear there.
    - An antecedent needed by the closing argument gets its own short paragraph. TSTR and the fidelity literature were one such case.

## 3. Sentences and wording

1. **Concise and technically precise.** No elaborate sub-clauses and no book-length explanations. The text reads as a scientific paper, not as technical documentation.
2. **Split long sentences** that can easily be split. Do this systematically from the Methodology on.
3. **Make reasoning explicit.** Sentences carry their reasoning; the link between consecutive sentences is stated, not left to the reader.
4. **Prefer plain, established words.**

   | Before | After | Reason |
   |---|---|---|
   | "standing objection" | "invites the objection" | "standing" is an unusual modifier |
   | "the departure between the two" | "the difference between the two" | a departure is *from* something |
   | "a measured quantity rather than an assertion" | "something measured rather than asserted" | parallel verbs, no nominalisation |
   | "covariate" | "input variable" | correct but forecasting-specific; the paper already has "input variable" |
   | "degradation trajectory" (in a general section) | "mean component" | the established term of the paper |
   | "added decline" | removed | informal, and unnecessary once the sentence was rebuilt |

5. **No invented terms or phrases, and no "fancy" wording.** Rejected in past edits: "model competence gate", "trajectory geometry", "level attained", "void", "readable".
   - "Innovations" was questioned. If the concept is needed, use the established time-series term with a definition and a citation.
6. **No vague replacements.** When text has to go, delete it or move it; do not swap it for vaguer words.

## 4. Terminology and notation

1. **No forward use.**
   - Establish every term, concept and symbol before it is used.
   - If information depends on a later definition, move it to just after that definition, or delete it.
2. **One term per concept, applied consistently:**

   | Use | Not |
   |---|---|
   | ground truth | reference ("reference model" is fine for the affine model g) |
   | mean component | level; degradation trajectory (in general sections) |
   | target variable | target |
   | conditioning variable | feature ("feature" is reserved for input channels) |
   | testbed (DegradX) | benchmark ("benchmark" stays for other authors' works) |
   | calibrated and validated (DegradX profiles) | paired |
   | pattern-free counterpart | counterpart |

3. **Paper-defined terms.**
   - Define each at first use.
   - Anchor it in one sentence to its nearest established term.
   - List it in the notation table.
4. **Abbreviations.**
   - Introduce each at its first mention, then always use it (RQ1, LSTM, IG, …).
   - Exceptions: the abstract and the conclusion.
5. **Assignments use ":="** wherever a specific value is assigned to a symbol (L := 24).
6. **Key formulas are displayed equations** (`equation` environment), defined once and referred to by name.
   - Repeat a formula only to remove ambiguity.
   - Example: the exact attribution w(x − x⁰) was over-repeated in an earlier draft.
7. **Section cross-references** only where needed for understanding or to remove ambiguity. No references to later sections.

## 5. Figures, tables, captions

1. **Use figures only where they add clarity:** complex, non-trivial or multi-step aspects.
   - New figures are welcome where they help.
   - Keep them in academic style, matching the DegradX figures.
2. **Explain visually and mathematically where possible.** Examples come before abstractions. Minimal toy walkthroughs with concrete numbers work better than prose.
3. **Do not overuse tables.** Drop a table, or fold it into the text, if it adds little.
4. **Captions explain the figure or table only.**
   - No values the table already shows.
   - No interpretation: that belongs in the text.
   - Keep them short.
5. **Figure content agrees with its caption and the text.** The labels inside a figure are updated when the terms change (e.g. "ensemble range", not "ensemble floor").
6. **Generate every number and label in a figure** by a script from the results or declarations. Never type them by hand.

## 6. Numbers and references

1. **No fabrication.**
   - Every number traces to the repository results or a cited source, checked twice.
   - No invented illustrative numbers.
2. **Verify references against primary sources, never against secondary literature or memory.** Secondary literature was wrong before:
   - TimeGAN uses an LSTM, not a GRU;
   - PSA-GAN's Context-FID uses the encoder of Franceschi et al., not TS2Vec.
3. **Check every reference on two levels:**
   - the bibliographic data;
   - that the cited claim matches the cited paper's findings or novelty.
4. **Flag what cannot be verified.** Unverifiable items get a TODO in `.bib` and are flagged in the text, never filled with guesses.
5. **Prefer the article over a separate dataset record** when the article covers the dataset. Dataset version and licence can go in a footnote.
6. **arXiv preprints** take one of two forms:
   - `@article` with "arXiv preprint arXiv:XXXX" in `journal`;
   - `@misc` with `howpublished = {\emph{arXiv preprint} arXiv:XXXX}`.
   - Note that `unsrt` drops `url` and `doi`; `unsrtnat` keeps them.

## 7. Editing workflow

1. **Writing order:** Introduction → Related Work → Methodology → experiments.
2. **The proposal is reference material.** The paper reflects the current research vision.
3. **Sections the author has finished** serve as the style reference and are not modified unless asked.
4. **Edit only what is asked.**
   - A comment's "spirit" may be applied to similar passages elsewhere.
   - It never licenses broader rewrites. When asked to change one word, change that word only.
5. **A cleaning pass should leave the text shorter.**
6. **Mark every change and log it.**
   - Use `\rev{}` with a reason, plus latexdiff.
   - Keep a changelog per comment.
   - Flag judgment calls for the author instead of deciding them silently.
7. **The author reviews only the final paper.** It must be complete and current, with methodology changes visible and diagrams redrawn.
8. **Verify your own work before delivering:**
   - compile without errors;
   - check every number;
   - confirm by diff that nothing outside the scope changed.

---

## Sources

**Conversations in this project:**
- "Research proposal review for XAI masking methods" (2026-07-18)
- "Temporal Shapley attributions on mean-nonstationary data" (2026-07-19)
- "Research proposal revision and methodological concerns" (2026-07-22)
- "Splitting research into conference thesis and journal article" (2026-08-11)
- "Rewriting benchmark paper's related work conclusion" (2026-08-12)
- "BibTeX @misc citation formatting for arXiv preprints" (2026-08-12)
- "Research proposal review and dataset selection" (2026-09-01)
- "Methodology review comments and document revisions" (2026-09-15)
- "Paper revision comments" (2026-10-14, two conversations; 2026-10-27; 2026-10-28)
- "Offset δc,i rationale analysis" (2026-10-14)
- "Paper revisions per reviewer comments" (2026-10-26)
- "Revising DegradX paper per review comments" (2026-10-28)
- "Paper revision and review feedback" (2026-10-28)
- "Paper revision feedback for ACIIDS" (2026-10-30)

**Project notes:** writing workflow, terminology and citation discipline.
