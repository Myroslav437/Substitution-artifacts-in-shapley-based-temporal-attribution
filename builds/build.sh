#!/bin/sh
# Builds ./builds/paper.pdf from ./paper (pdflatex -> bibtex -> pdflatex x2, plus one more pass if LaTeX asks for it),
# reports undefined citations and references, and checks that nothing outside the abstract and Sections 1-6 changed
# against the revision-1 snapshot except the preamble's \input line.
# Usage: sh builds/build.sh   (from the project root; needs pdflatex, bibtex and python)
set -e
ROOT=$(cd "$(dirname "$0")/.." && pwd)
SRC="$ROOT/paper/_arXiv__Substitution_Artifacts_in_Shapley_Based_Temporal_Attribution"
R1="$ROOT/notes/baseline_r1/_arXiv__Substitution_Artifacts_in_Shapley_Based_Temporal_Attribution"
OUT="$ROOT/builds"
TMP=$(mktemp -d)
cp -r "$SRC"/. "$TMP"/
cd "$TMP"
J=paper
pdflatex -interaction=nonstopmode -halt-on-error -jobname=$J templateArxiv.tex > $J.pass1.log 2>&1 || { tail -30 $J.log; exit 1; }
bibtex $J > $J.bib.log 2>&1 || { cat $J.bib.log; exit 1; }
pdflatex -interaction=nonstopmode -halt-on-error -jobname=$J templateArxiv.tex > $J.pass2.log 2>&1 || { tail -30 $J.log; exit 1; }
pdflatex -interaction=nonstopmode -halt-on-error -jobname=$J templateArxiv.tex > $J.pass3.log 2>&1 || { tail -30 $J.log; exit 1; }
if grep -q "Rerun to get" $J.log; then pdflatex -interaction=nonstopmode -halt-on-error -jobname=$J templateArxiv.tex > $J.pass4.log 2>&1; fi
echo "== $J: $(grep -c 'LaTeX Warning: Citation' $J.log || true) undefined citations, $(grep -c 'LaTeX Warning: Reference' $J.log || true) undefined references, $(grep -c '^!' $J.log || true) errors, bibtex warnings/errors: $(grep -c -E 'Warning--|error message' $J.bib.log || true), pages: $(grep -o 'Output written on [^ ]* ([0-9]* pages' $J.log | grep -o '[0-9]* pages')"
grep -E "^(Overfull|Underfull) \\hbox" $J.log | sort | uniq -c | sort -rn | head -5 || true
cp $J.pdf "$OUT/$J.pdf"
cd "$ROOT"; rm -rf "$TMP"
# Byte-exactness outside the revised sections (against the revision-1 snapshot the authors commented on)
python "$ROOT/builds/check_outside.py" "$R1/templateArxiv.tex" "$SRC/templateArxiv.tex"
for f in PRIMEarxiv.sty README.md; do cmp -s "$R1/$f" "$SRC/$f" && echo "unchanged: $f" || echo "CHANGED: $f"; done
