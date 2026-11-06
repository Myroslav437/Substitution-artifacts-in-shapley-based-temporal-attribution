# Open decisions and flags — mirrors the Notes box of the review build (`paper/…/review_notes.tex`)

*Revision-1 version (2026-11-03), preserved on 2026-11-05 before `notes/OPEN_DECISIONS.md` was rewritten for revision 2.*

## 1. Open decisions D1–D9 (default written in the text, coloured and tagged [Dn] in the review build)

| ID | Default written | Where | Note |
|---|---|---|---|
| D1 | B2c (coalition-conditional TAB) included as a variant of B2 | §3.4 "B2c", Table 2 | Sums to f(x) − f(b₁) exactly; needs the modified masking step (§3.7) |
| D2 | Longer window L := 96, from DegradX's declared grid [8, 16, 24, 48, 96] | §3.5 "Declared extensions" | The ACIIDS sequence length could not be checked (paper not in `./style`) |
| D3 | B1 = per-channel training mean; TimeSHAP's average event (median) as a variant | §3.4 "B0, B1 and B-pristine" | "As in ACIIDS Eq. 3" is unverified (`\todo`) |
| D4 | "mean component", not "level"; v5.1's "level index" → "state index" | §3.1 (first use), §2.1 wording, throughout | |
| D5 | M-ψ included, marked "conditional on the pilot" | §3.5 targets and model families | ψ itself is not specified by any input |
| D6 | Non-Shapley comparators dropped from the design; discussed in Related Work only | §2.4 | Same reason as DegradX's exclusion of mask-optimizing methods |
| D7 | Primary synthetic architecture = DegradX's LSTM; attention LSTM in the case study only | §3.5 "Model families", §3.6 | |
| D8 | Threshold ϑ of the function-identity check left open | §3.5 M-obs | X9 pilot (HUST; IG and occlusion only): M-obs fits to 1–2 % of the noise term's SD; ten models span 0.45–0.47 in temporal profile error against a method gap of 0.035 (readiness review §2.2). Unpublished → Notes box only |
| D9 | Target journal EAAI | not in the text | Conflicts with the PRIMEarxiv template (C1) |

## 2. Method constants that no input fixes (written as symbols; to be set before the experiments)

- B2: K, bin scheme (per-coordinate product or scalar index), minimum bin count; the running summary h, cap d and near-duplicate threshold of the index-channel screen.
- B3: t_min, function family 𝓜, weight profile ω, penalty P (λ by cross-validation).
- B4: imputer architecture and training.
- Control: boosted-tree implementation and hyperparameters.
- M-ψ: ψ.
- M2: quantiles defining the near and far bands.
- M5: the positions u₀ swept.
- Precision of permutation sampling for ϕ*_b (B2c, B4, M-ψ).
- P-GEN: amplitude, period, phase of the periodic component.
- E2: subsample fractions.
- Cross-estimator check: which profile.

Chosen here and to be confirmed:
- Trended null channel: another unit's degradation-state trajectory from a random start, held after that unit's end of life, mapped through the charge-time mapping, with charge-time noise.
- M-R ensembles use DegradX's ten-member design (needed for ensemble divergence on the measured arms).
- Recency weighting only (DegradX's primary); uniform weighting not run.
- Background function may read the unit's history before the window (R1).

## 3. Unverified items (`% TODO` in `.bib`, `\todo` in the text)

1. DegradX arXiv identifier (`degradx2026`).
2. ACIIDS paper absent from `./style`: B1 as in its Eq. 3; its sequence length (D2); the PCoE cells and preprocessing; the attention-LSTM architecture; what the pipeline correction changes; the list of published findings for the case study. Bibliographic record verified via Crossref.
3. TSHAP: title and abstract only; its background-selection rule and its applicability to the LSTM regressor and to cell-level players.
4. GroupSegment-SHAP: claims checked on arXiv v2 (2026-08-21); the cited CIKM '26 version was not accessible.
5. Repository URL for this paper's code.
6. v5.1 §9 list: see `REFERENCES_AUDIT.md` §4.

## 4. Conflicts between inputs not resolved

- C1: brief names `elsarticle`; the project uses PRIMEarxiv. Template untouched; an EAAI submission needs a port.
- C2/C5: ACIIDS findings quoted in v5.1 (Eq. 3; Spearman 0.078; 16.9 % pruning; Reviewer 4) not used: the paper is the only allowed source and is unavailable.
- C4: DegradX README/CITATION.cff cite it as an ACIIDS 2027 submission; brief asks for the arXiv entry.
- C9: v5.1's B4 validity gate also used fill surprisal (needs the density model the brief's instrument set drops); only held-out imputation error kept.
- Brief §2.5 omits P-GEN from the extensions, while brief §3 item 8 and E5 require it: included as a declared extension.
- "Function-identity gate" (brief) written as "function-identity check" (preferences §3.4, plain words; "gate" is plan vocabulary).
- RQ1/RQ2 written without the labels B0, B1, B-pristine, B4, which are defined only in §3 (preferences §4.1, no forward use).
- Bibliography style `unsrt` → `unsrtnat` and natbib loaded: the existing `\citet` calls need them (baseline did not compile). Outside §1–§3 the template's demo section, the lipsum abstract and the conclusion placeholder remain.

## 5. Novelty re-check (2026-11-03)

No candidate provides contribution 2 or 3. Added to Related Work: Delta-XAI/SWING (§2.4), GRAIL (§2.4), TempShap (§2.5), Zhang et al. v2 (moved to §2.2), Merrick and Taly and Mamalakis et al. (§2.2). Not added: arXiv:2609.30397, arXiv:2607.16236. Details: `REFERENCES_AUDIT.md` §3.
