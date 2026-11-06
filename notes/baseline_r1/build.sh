#!/bin/sh
# Builds the three PDFs of brief Section 7 from ./paper and the baseline in ./notes/baseline:
#   paper_review.pdf  review build (colour, margin notes, banners, Notes box)
#   paper_clean.pdf   clean build (\reviewfalse via \cleanbuild)
#   paper_diff.pdf    latexdiff of the baseline against the current text, typeset as the clean build
# Usage: sh builds/build.sh   (from the project root; needs pdflatex, bibtex, latexdiff)
set -e
ROOT=$(cd "$(dirname "$0")/.." && pwd)
# latexdiff needs Perl's Algorithm::Diff; MiKTeX's self-contained latexdiff-so bundles it.
if latexdiff --version > /dev/null 2>&1; then LATEXDIFF="latexdiff"
else LATEXDIFF="perl $(dirname "$(command -v latexdiff)")/../../../scripts/latexdiff/latexdiff-so"; fi
SRC="$ROOT/paper/_arXiv__Substitution_Artifacts_in_Shapley_Based_Temporal_Attribution"
BASE="$ROOT/notes/baseline/_arXiv__Substitution_Artifacts_in_Shapley_Based_Temporal_Attribution"
OUT="$ROOT/builds"
TMP=$(mktemp -d)
cp -r "$SRC"/. "$TMP"/
cd "$TMP"

run() {  # run <jobname> <tex-source-expression>
  for pass in 1 2; do pdflatex -interaction=nonstopmode -halt-on-error -jobname="$1" "$2" > "$1.pass$pass.log" 2>&1 || { tail -30 "$1.log"; exit 1; }
    [ "$pass" = 1 ] && bibtex "$1" > "$1.bib.log" 2>&1; done
  pdflatex -interaction=nonstopmode -halt-on-error -jobname="$1" "$2" > "$1.pass3.log" 2>&1
  grep -q "Rerun to get" "$1.log" && pdflatex -interaction=nonstopmode -jobname="$1" "$2" > "$1.pass4.log" 2>&1
  echo "== $1: $(grep -c 'LaTeX Warning: Citation' "$1.log" || true) undefined citations, $(grep -c 'LaTeX Warning: Reference' "$1.log" || true) undefined references, bibtex errors: $(grep -c 'error message' "$1.bib.log" || true)"
  cp "$1.pdf" "$OUT/$1.pdf"
}

run paper_review templateArxiv.tex
run paper_clean '\def\cleanbuild{}\input{templateArxiv.tex}'

# latexdiff: baseline vs current main file; \rev, \revw are text commands, notes are safe commands.
$LATEXDIFF --type=UNDERLINE --math-markup=whole --graphics-markup=none \
  --append-textcmd="rev,revw,dec" --append-safecmd="revwhy,revwhyw,revdel,newsectionbanner,todo" \
  "$BASE/templateArxiv.tex" templateArxiv.tex > diff_raw.tex 2> latexdiff.log
# The baseline's \ref{sec:headings} pointed to a label that never existed; show it as text in the deleted span.
sed 's/\\ref{sec:headings}/[ref: sec:headings]/g' diff_raw.tex > paper_diff.tex
run paper_diff '\def\cleanbuild{}\input{paper_diff.tex}'
cp paper_diff.tex "$OUT/paper_diff.tex"
rm -rf "$TMP"

# Highlighting coverage of the Related Work section against the baseline (brief Section 7)
python -I "$OUT/check_rev_coverage.py" "$BASE/templateArxiv.tex" "$SRC/templateArxiv.tex"
# Nothing outside Sections 1-3 may change except the preamble line that loads review_setup and the bibliography style
echo "== changes outside Sections 1-3 (expected: review switch + \\input{review_setup}, Notes box input, bibliography style):"
diff <(sed '/^\\section{Introduction}/,/^\\section{Examples of citations/d' "$BASE/templateArxiv.tex") \
     <(sed '/^\\section{Introduction}/,/^\\section{Examples of citations/d' "$SRC/templateArxiv.tex") | grep '^[<>]' || true
for f in PRIMEarxiv.sty README.md; do cmp -s "$BASE/$f" "$SRC/$f" && echo "unchanged: $f" || echo "CHANGED: $f"; done
