"""
Generate candidate negations for each claim (for the negation metamorphic test).

Output: claim_negations.json  { claim: {negation, method, auto_confidence, reviewed} }

A negation only needs to be a hypothesis whose CORRECT stance is the opposite of
the original. Auto-gen is heuristic (POS-based); rows with auto_confidence < 0.8
want a human glance. Reviewing 62 claims takes a few minutes. Set "reviewed": true
once checked. The metamorphic test reads this file.

Requires: nltk (punkt_tab, averaged_perceptron_tagger_eng).
Re-run:  python gen_negations.py [labeled_sources.json]
"""
import json, re, sys
import nltk
for _p in ["punkt_tab", "averaged_perceptron_tagger_eng"]:
    nltk.download(_p, quiet=True)
from nltk import pos_tag, word_tokenize

AUX_INSERT = {"is","are","was","were","be","been","can","could","will",
              "would","shall","should","may","might","must"}

def _base(verb: str) -> str:
    v = verb
    if v.endswith("ies"): return v[:-3] + "y"
    if v.endswith(("ches","shes","sses","xes","zes","oes")): return v[:-2]
    if v.endswith("s") and not v.endswith("ss"): return v[:-1]
    return v

def _base_past(verb: str) -> str:
    v = verb
    if v.endswith("ied"): return v[:-3] + "y"
    if v.endswith("eed"): return v[:-1]
    if v.endswith("ed"):
        stem = v[:-2]
        if len(stem) >= 2 and stem[-1] == stem[-2]:  # stopped -> stop
            stem = stem[:-1]
        return stem
    return v

def negate(c: str):
    cl = c.strip(); low = cl.lower()
    # 1) already negative -> affirm
    for pat in ["do not ","does not ","did not ","cannot ","can not ",
                "can't ","don't ","doesn't ","didn't ","will not ","won't ","n't "]:
        if pat in low:
            i = low.index(pat); return (cl[:i] + cl[i+len(pat):]).strip(), "affirm", 0.7
    if " never " in low:
        i = low.index(" never "); return (cl[:i] + " " + cl[i+len(" never "):]).strip(), "affirm", 0.7
    if " not " in low:
        i = low.index(" not "); return (cl[:i] + " " + cl[i+len(" not "):]).strip(), "affirm", 0.6

    toks = cl.split()
    norm = [re.sub(r"[^a-z]", "", t.lower()) for t in toks]
    # 2) has/have/had -> does/do/did not have
    for k, n in enumerate(norm):
        if n in {"has","have","had"}:
            repl = {"has":"does not have","have":"do not have","had":"did not have"}[n]
            return " ".join(toks[:k] + [repl] + toks[k+1:]), "have-neg", 0.85
    # 3) copula/modal -> insert not after
    for k, n in enumerate(norm):
        if n in AUX_INSERT:
            if n == "can":
                return " ".join(toks[:k] + ["cannot"] + toks[k+1:]), "modal", 0.6
            return " ".join(toks[:k+1] + ["not"] + toks[k+1:]), "insert-aux", 0.85
    # 4) POS: negate the first main verb
    tags = pos_tag(word_tokenize(cl))
    # map tagged tokens back to original whitespace tokens by order of alpha tokens
    verb_pos = None  # (token_index_in_toks, tag, surface)
    ti = 0
    for surf, tag in tags:
        if not re.search(r"[A-Za-z]", surf):
            continue
        # advance ti to the toks index whose alpha-normalized form matches
        while ti < len(toks) and re.sub(r"[^a-z]", "", toks[ti].lower()) != re.sub(r"[^a-z]", "", surf.lower()):
            ti += 1
        if ti >= len(toks): break
        if tag in ("VBZ","VBP","VBD","VB") and ti >= 1:
            verb_pos = (ti, tag, toks[ti]); break
        ti += 1
    if verb_pos:
        k, tag, surf = verb_pos
        if tag == "VBZ":   ins, base = "does not", _base(surf)
        elif tag == "VBD": ins, base = "did not", _base_past(surf)
        else:              ins, base = "do not", surf  # VBP / VB
        conf = 0.8 if tag in ("VBZ","VBP","VB") else 0.6
        return " ".join(toks[:k] + [ins, base] + toks[k+1:]), f"verb-{tag}", conf
    # 5) clean periphrastic fallback (always grammatical, valid negation)
    return ("It is not true that " + cl[0].lower() + cl[1:]), "periphrastic", 0.5

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "/mnt/user-data/uploads/labeled_sources.json"
    rows = json.load(open(path)); claims = sorted(set(r["claim"] for r in rows))
    out = {}
    print(f'{"conf":>4} {"method":<12} negation')
    print("-" * 84)
    for c in claims:
        neg, how, conf = negate(c)
        out[c] = {"negation": neg, "method": how, "auto_confidence": conf, "reviewed": False}
        print(f'{conf:>4} {how:<12} {neg[:62]}{"  <-- REVIEW" if conf < 0.8 else ""}')
    json.dump(out, open("claim_negations.json", "w"), indent=2)
    print(f"\nWrote claim_negations.json ({len(out)} claims).")

if __name__ == "__main__":
    main()
