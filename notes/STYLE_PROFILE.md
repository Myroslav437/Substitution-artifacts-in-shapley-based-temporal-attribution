# Style profile (P1)

Sources: DegradX Introduction and Related Work (closest in-house model); FLICS 2026 "Simulation-Driven Benchmarking Framework…" and "LiDAR-Augmented Wi-Fi…". Binding overrides: `docs/writing_style_preferences.md` (wins over this profile); the brief wins over both.

**Sentences.** Medium length (≈15–30 words), one main clause plus at most one subordinate clause. Key claims stand as short sentences ("The established response is to construct data for which the attribution ground truth is known."). Consecutive sentences are tied by explicit connectors (*therefore, however, since, so, thus*), placed early. Enumerations of reasons use *First, … Second, … Third, …* inside a paragraph. No rhetorical questions, no figurative language.

**Paragraphs.** Topic sentence stating the claim → supporting cited facts or construction details → a consequence sentence that carries the argument forward ("Such measures can therefore establish that two methods differ, but not which…"). One idea per paragraph; 4–8 sentences.

**Qualifying claims.** Hedges are proportionate and attached to the claim they qualify: *to our knowledge* (novelty), *plausibly*, *is consistent with*, *may thus* (mechanisms not tested). Results are stated for what was tested; limitations follow what holds ("reproduce part, but not all, of …").

**Related work.** Grouped by kind of contribution, not by paper. Each paragraph: what the group established → named examples with one-line content → the specific reason it does not provide what is needed ("Their ground truth, however, is the interaction structure itself"). The closing paragraph synthesizes ("Across the overviewed body of work, the properties … are available separately and never together") and places the work in the remaining position, without describing the artefact again.

**Notation, assumptions, definitions.** Introduced inline at first use ("Let W be a window of L := 24 consecutive positions ending at position t"). Declared constants use ":=". Key formulas are numbered displayed equations, followed by "where …" defining each new symbol, then referred to as "Equation (n)". Definitions and design decisions are run-in bold paragraph heads ("Reference model.", "Definition of the degradation state and of EOL."). Each design choice is followed by its reason, often the rejected alternative and why it fails ("The more obvious alternative … would make z_t a function of t/T").

**Figures and tables.** A figure where a construction has several interacting parts (testbed structure; mean-component construction). Captions describe panels (a), (b), … and what is drawn, never what it shows. Tables carry multi-column numeric comparisons only. Text points to a figure with "Figure n shows …".

**Voice and tense.** Present tense for the method and for what the paper does; past tense for what cited works did ("Ismail et al. built 70 datasets"). Impersonal subject for the method ("The generator produces…", "Fitting uses the fitting split only"); "we" only for decisions ("We therefore apply…", "We adopt the first").

**Openings and closings.** A section opens with one or two sentences listing its parts in order ("… consists of a generator, a fitting procedure …, and an evaluation protocol. This section describes them in that order."). The Introduction runs: application context → why the problem matters → the established response and why it does not transfer → what this work provides → RQs as bullets → scope and release. Sections close on the consequence that the next section takes up, not on a summary.
