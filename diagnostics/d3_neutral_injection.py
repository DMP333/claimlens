"""
DIAGNOSTIC 3  (Instrument C, LABEL-FREE):  Do irrelevant sources move the verdict?

Invariant: adding a clearly-irrelevant source to a claim's evidence set should NOT
change the verdict. We borrow snippets from topically-distant claims, score them
against the target claim, inject them, and measure verdict drift under 3K vs 3N.

Under 3K (no neutral) injected junk must vote -> drift. Under 3N it should abstain
-> ~no drift. This quantifies the architectural hole and whether 3N closes it.
No truth labels needed (it is a consistency test, not a correctness test).

Run from repo root with labeled_sources.json (+ tiers.json to scope Tier A).
  python diagnostics/d3_neutral_injection.py
"""
import json, sys, os, random
sys.path.insert(0, os.getcwd())
random.seed(0)
from app.services.nli_service import split_sentences, _run_nli_batch, DEFAULT_MIN_WORDS
from common import load_sources, by_claim, load_json, verdict_band
from aggregators import agg_3k, agg_3n

SENT_TYPES = {"encyclopedia", "academic", "web"}
STOP = set("the a an is are was were be of to in on for and or not no this that with from as it its by at do does did have has had only most about".split())
N_INJECT = 3

def words(c): return {w for w in c.lower().split() if w not in STOP and len(w) > 2}

def src_stance_cache(rows, cache, fn):
    """stance per sentence-NLI source under aggregator fn, using cached probs."""
    out = {}
    for i, r in enumerate(rows):
        if r["source_type"] not in SENT_TYPES: continue
        claim = r["claim"]; text = r.get("snippet_only") or r.get("title_only") or ""
        sents = [s for s in split_sentences(text) if len(s.split()) >= DEFAULT_MIN_WORDS]
        probs = [cache[f"{claim}||{s}"]["claim"] for s in sents if cache and f"{claim}||{s}" in cache]
        out[i] = fn(probs) if probs else ("neutral", 0.0)
    return out

def ratio_of(stances):
    ws = sum(1 for s,_ in stances if s == "supporting")
    wo = sum(1 for s,_ in stances if s == "opposing")
    return ws/(ws+wo) if (ws+wo) else None

def main():
    rows = load_sources()
    cache = load_json("sentence_nli_cache.json")
    tiers = load_json("tiers.json", {})
    if not cache:
        print("Run d1 first to build sentence_nli_cache.json (needed for baseline stances)."); return

    claims = by_claim(rows)
    # pre-pick borrowed snippets: for each claim, snippets from claims sharing no content words
    snippets_by_claim = {c: [r.get("snippet_only","") for r in rs
                             if r["source_type"] in SENT_TYPES and r.get("snippet_only")]
                         for c, rs in claims.items()}

    claim_rows = {}
    for i, r in enumerate(rows):
        claim_rows.setdefault(r["claim"], []).append(i)

    results = {"3K": [], "3N": []}
    for claim, idxs in claim_rows.items():
        t = tiers.get(claim, {})
        if t.get("tier") != "A":  # scope to Tier A for a clean set
            continue
        cw = words(claim)
        donors = [c for c in claims if c != claim and not (words(c) & cw)]
        if not donors: continue
        borrowed = []
        random.shuffle(donors)
        for dc in donors:
            for sn in snippets_by_claim.get(dc, []):
                borrowed.append(sn);  break
            if len(borrowed) >= N_INJECT: break
        if len(borrowed) < N_INJECT: continue

        for name, fn in [("3K", agg_3k), ("3N", agg_3n)]:
            base = src_stance_cache(rows, cache, fn)
            base_st = [base[i] for i in idxs if i in base]
            r0 = ratio_of(base_st)
            # score borrowed snippets against THIS claim, inject
            inj_st = list(base_st)
            for sn in borrowed:
                sents = [s for s in split_sentences(sn) if len(s.split()) >= DEFAULT_MIN_WORDS]
                if not sents: continue
                pr = _run_nli_batch(sents, claim)
                inj_st.append(fn(pr))
            r1 = ratio_of(inj_st)
            if r0 is None or r1 is None: continue
            results[name].append((claim, r0, r1, verdict_band(r0), verdict_band(r1)))

    print("=" * 70)
    print(f"NEUTRAL-INJECTION INVARIANT  (inject {N_INJECT} irrelevant sources / claim)")
    print("=" * 70)
    for name in ["3K", "3N"]:
        rs = results[name]
        if not rs: continue
        drift = sum(abs(r1-r0) for _,r0,r1,_,_ in rs)/len(rs)
        flips = sum(1 for _,_,_,b0,b1 in rs if b0 != b1)
        print(f"  {name}: mean |ratio drift| = {drift:.3f} | verdict-band flips = {flips}/{len(rs)} claims")
    print("\n  A good system has ~0 drift and 0 flips (irrelevant sources are ignored).")
    print("  Expect 3K to drift/flip and 3N to stay put, confirming the hole and the fix.")
    json.dump({k: [(c, round(a,3), round(b,3)) for c,a,b,_,_ in v] for k,v in results.items()},
              open("d3_results.json","w"), indent=2)
    print("Wrote d3_results.json")

if __name__ == "__main__":
    main()
