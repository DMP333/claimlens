"""
DIAGNOSTIC 1  (Step 1a, LABEL-FREE):  Does the NLI model read negation?

Hypothesis: a chunk of the "true claim scored as opposed" failures (antibiotics,
honey, ...) are negation blindness. If the model handles negation, then for a
sentence that SUPPORTS a claim, the same sentence should OPPOSE the claim's
negation. We run NLI(sentence, claim) and NLI(sentence, negated_claim) for every
sentence and measure how often the polarity flips.

  flip          : supporting<->opposing when claim is negated  (GOOD)
  same-polarity : same direction for claim and its negation     (NEGATION BLIND)
  to-neutral    : non-neutral -> neutral

A high same-polarity rate among CONFIDENT non-neutral sentences = negation failure,
and that alone explains the wrong-both-ways class. No labels required.

Run from repo root (where app/ lives), with labeled_sources.json + claim_negations.json present.
  pip install transformers torch nltk sentence-transformers
  python diagnostics/d1_negation_metamorphic.py
Outputs: prints summary; writes sentence_nli_cache.json (reused by d2/d4) and d1_results.json
"""
import json, sys, os
sys.path.insert(0, os.getcwd())
from collections import Counter
from app.services.nli_service import split_sentences, _run_nli_batch, DEFAULT_MIN_WORDS
from common import load_sources, by_claim, load_json

CONF = 0.55          # "confident" non-neutral threshold
SENT_TYPES = {"encyclopedia", "academic", "web"}  # sources that go through sentence NLI

def polarity(label): return {"supporting": 1, "opposing": -1, "neutral": 0}[label]

def main():
    rows = load_sources()
    negs = load_json("claim_negations.json")
    if not negs:
        print("Missing claim_negations.json. Run: python diagnostics/gen_negations.py"); return
    unreviewed = sum(1 for v in negs.values() if not v.get("reviewed"))
    if unreviewed:
        print(f"WARNING: {unreviewed}/{len(negs)} negations not marked reviewed. "
              f"Low-confidence ones may distort results. Proceeding anyway.\n")

    cache = {}            # f"{claim}||{sent}" -> {claim:probs, neg:probs}
    tally = Counter()
    by_method = {}        # negation method -> Counter
    offenders = []        # confident, did-not-flip cases (evidence)

    claims = by_claim(rows)
    for ci, (claim, srcs) in enumerate(claims.items(), 1):
        neg = negs.get(claim, {}).get("negation")
        method = negs.get(claim, {}).get("method", "?")
        if not neg:
            continue
        # collect this claim's sentences from sentence-NLI source snippets
        sents = []
        for r in srcs:
            if r["source_type"] not in SENT_TYPES:
                continue
            text = r.get("snippet_only") or r.get("title_only") or ""
            for s in split_sentences(text):
                if len(s.split()) >= DEFAULT_MIN_WORDS:
                    sents.append(s)
        sents = list(dict.fromkeys(sents))  # dedup, keep order
        if not sents:
            continue
        pos = _run_nli_batch(sents, claim)
        neo = _run_nli_batch(sents, neg)
        by_method.setdefault(method, Counter())
        for s, pc, pn in zip(sents, pos, neo):
            cache[f"{claim}||{s}"] = {"claim": pc, "neg": pn}
            if pc["label"] == "neutral" or pc["confidence"] < CONF:
                continue  # only judge confident non-neutral under the original claim
            tally["confident_nonneutral"] += 1
            by_method[method]["n"] += 1
            if pn["label"] == "neutral":
                tally["to_neutral"] += 1; by_method[method]["to_neutral"] += 1
            elif polarity(pc["label"]) == -polarity(pn["label"]):
                tally["flip"] += 1; by_method[method]["flip"] += 1
            else:
                tally["same_polarity"] += 1; by_method[method]["same"] += 1
                if pn["confidence"] >= CONF and len(offenders) < 40:
                    offenders.append({"claim": claim, "neg": neg, "sent": s,
                                      "claim_label": pc["label"], "claim_conf": round(pc["confidence"],3),
                                      "neg_label": pn["label"], "neg_conf": round(pn["confidence"],3)})
        print(f"  [{ci}/{len(claims)}] {claim[:46]:<46} sents={len(sents)}")

    n = max(tally["confident_nonneutral"], 1)
    print("\n" + "=" * 70)
    print("NEGATION METAMORPHIC RESULT")
    print("=" * 70)
    print(f"Confident non-neutral (claim) sentences: {tally['confident_nonneutral']}")
    print(f"  flipped polarity when negated (GOOD)        : {tally['flip']:>5} ({tally['flip']/n:.1%})")
    print(f"  SAME polarity when negated (NEGATION BLIND) : {tally['same_polarity']:>5} ({tally['same_polarity']/n:.1%})")
    print(f"  went neutral when negated                   : {tally['to_neutral']:>5} ({tally['to_neutral']/n:.1%})")
    print("\nInterpretation: same-polarity >~35% => the model substantially ignores")
    print("hypothesis negation, which is a primary, fine-tuning-addressable failure.")

    print("\nBy negation method (verbal 'does/do not' is the form that matters most):")
    for m, c in sorted(by_method.items()):
        nn = max(c["n"], 1)
        print(f"  {m:<13} n={c['n']:>4}  flip={c.get('flip',0)/nn:.0%}  same={c.get('same',0)/nn:.0%}  neutral={c.get('to_neutral',0)/nn:.0%}")

    print("\nWorst offenders (confident, did NOT flip = model blind to the negation):")
    for o in offenders[:15]:
        print(f"  [{o['claim_label']}->{o['neg_label']}] {o['sent'][:70]}")
        print(f"      claim: \"{o['claim'][:46]}\"  |  neg: \"{o['neg'][:46]}\"")

    json.dump(cache, open("sentence_nli_cache.json", "w"))
    json.dump({"tally": dict(tally), "offenders": offenders}, open("d1_results.json", "w"), indent=2)
    print("\nWrote sentence_nli_cache.json (reused by d2/d4) and d1_results.json")

if __name__ == "__main__":
    main()
