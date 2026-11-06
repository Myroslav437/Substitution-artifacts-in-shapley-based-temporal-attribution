r"""Compare a revised main file with the revision-1 snapshot outside the abstract and Sections 1-6.

Expected differences: the preamble's review switch and \input{review_setup} replaced by one \input{paper_setup} line,
and the removed Notes-box input. Everything else (title block, keywords, template demo section, conclusion
placeholder, acknowledgments, bibliography commands) must be byte-identical.
"""
import difflib
import sys


def parts(path):
    text = open(path, "rb").read().decode("utf-8")
    L = text.split("\n")
    a0, a1 = L.index(r"\begin{abstract}"), L.index(r"\end{abstract}")
    s0 = L.index(r"\section{Introduction}") - 1
    e0 = L.index(r"\section{Examples of citations, figures, tables, references}") - 1
    return {"head": L[:a0 + 1], "keywords": L[a1:s0 + 1], "tail": L[e0:]}


old, new = parts(sys.argv[1]), parts(sys.argv[2])
for k in old:
    d = [x for x in difflib.unified_diff(old[k], new[k], lineterm="", n=0) if not x.startswith(("---", "+++", "@@"))]
    print(f"== outside the revised sections, {k}: " + ("identical" if not d else "differs:\n   " + "\n   ".join(d)))
