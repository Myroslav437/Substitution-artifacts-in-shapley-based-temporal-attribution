"""Check that every word added to or changed in the Related Work section against the baseline lies inside \\rev{} or
\\revw{} (brief Section 7). Margin-note commands (\\revwhy, \\revwhyw, \\revdel, \\todo, \\dec) are annotations and are
removed before the comparison. Prints uncovered insertions; exit code 1 if any.

usage: python check_rev_coverage.py <baseline.tex> <current.tex>
"""
import difflib
import re
import sys

NOTES = ("revwhy", "revwhyw", "revdel", "todo")
WRAP = ("rev", "revw")


def section(tex: str) -> str:
    a = tex.index(r"\section{Related Work}")
    b = tex.index(r"\section{", a + 10)
    return tex[a:b]


def arg_end(s: str, i: int) -> int:
    """index just after the brace group that starts at s[i] == '{'"""
    depth = 0
    for j in range(i, len(s)):
        if s[j] == "{":
            depth += 1
        elif s[j] == "}":
            depth -= 1
            if depth == 0:
                return j + 1
    raise ValueError("unbalanced braces")


def strip_notes(s: str) -> str:
    # non-printing material: labels and the table-of-contents argument of sectioning commands
    s = re.sub(r"\\label\{[^}]*\}", "", s)
    s = re.sub(r"(\\(?:sub)*section)\[[^\]]*\]", r"\1", s)
    out, i = [], 0
    pat = re.compile(r"\\(" + "|".join(NOTES) + r")(\[[^\]]*\])?\{")
    while True:
        m = pat.search(s, i)
        if not m:
            out.append(s[i:])
            return "".join(out)
        out.append(s[i:m.start()])
        i = arg_end(s, m.end() - 1)


def tokens_with_cover(s: str):
    """word tokens of s with a flag: inside a \\rev{}/\\revw{} argument (or a \\subsection[...]{\\rev{...}})"""
    covered = [False] * len(s)
    for m in re.finditer(r"\\(" + "|".join(WRAP) + r")\{", s):
        end = arg_end(s, m.end() - 1)
        for k in range(m.start(), end):
            covered[k] = True
    toks = [(t.group(), covered[t.start()]) for t in re.finditer(r"[A-Za-z0-9]+", s)]
    # drop the wrapper command names themselves
    return [(w, c) for w, c in toks if w not in WRAP]


def main(base_path, cur_path):
    base = strip_notes(section(open(base_path, encoding="utf-8").read()))
    cur = strip_notes(section(open(cur_path, encoding="utf-8").read()))
    bt = [w for w, _ in tokens_with_cover(base)]
    ct = tokens_with_cover(cur)
    sm = difflib.SequenceMatcher(a=bt, b=[w for w, _ in ct], autojunk=False)
    bad, n_ins = [], 0
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op in ("insert", "replace"):
            n_ins += j2 - j1
            unc = [ct[j][0] for j in range(j1, j2) if not ct[j][1]]
            if unc:
                bad.append((op, " ".join(bt[i1:i2])[:80], " ".join(unc)[:160]))
    print(f"Related Work: {n_ins} inserted/changed words, {sum(len(b[2].split()) for b in bad)} outside \\rev/\\revw")
    for b in bad:
        print("  UNCOVERED", b)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
