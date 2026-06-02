"""
DIAGNOSTIC 5 (FEASIBILITY, label-free spend): is fine-tuning even the right tool?

This does NOT trust the verdict number. It asks the mechanistic question directly:
are DeBERTa's per-sentence mistakes SYSTEMATIC and LEARNABLE, or random/capacity-bound?

It crosses DeBERTa's cached per-sentence labels (sentence_nli_cache.json, from d1)
against the LLM silver labels (sentence_labels_llm.json) and reports:

  1. DeBERTa per-sentence accuracy vs the LLM reference (overall).
  2. Confusion matrix: what DeBERTa says when the truth is X.
  3. The "poison pile": CONFIDENT disagreements (DeBERTa sure AND wrong). These are
     the sentences that survive any aggregator and corrupt verdicts. Broken by
     direction, because DeBERTa->supporting/opposing when truth is neutral is the
     forced-vote pathology, and supporting<->opposing flips are the hard NLI errors.
  4. Negation slice: accuracy on claims containing not/never/only vs the rest. If
     much lower, negation is a concrete, learnable target.
  5. Top claims by disagreement, so you can eyeball WHERE it fails.

Reading it: fine-tuning is FEASIBLE and worth it if the poison pile is large AND
concentrated in nameable categories (negation, neutral-forced-to-vote). If DeBERTa
already agrees with the LLM ~95% and the few disagreements are low-confidence and
scattered, fine-tuning has little to grip and you should not bother.

No model load, no API calls, no spend. Just reads two JSON files.
  python diagnostics/d5_sentence_error_analysis.py
"""
import json, re
from collections import Counter, defaultdict
from common import load_json

CONF = 0.55
NEG_WORDS = re.compile(r"\b(not|never|no|n't|cannot|only)\b", re.I)

def argmax_label(p):
    pairs = [("supporting", p.get("p_supp", 0)), ("neutral", p.get("p_neut", 0)),
             ("opposing", p.get("p_opp", 0))]
    return max(pairs, key=lambda x: x[1])[0]

def deberta_conf(p):
    return max(p.get("p_supp", 0), p.get("p_neut", 0), p.get("p_opp", 0))

def main():
    cache = load_json("sentence_nli_cache.json")
    llm = load_json("sentence_labels_llm.json")
    if not cache or not llm:
        print("Need sentence_nli_cache.json (run d1) and sentence_labels_llm.json (run step 6).")
        return

    keys = [k for k in llm if k in cache]
    print(f"Sentences with BOTH DeBERTa and LLM labels: {len(keys)}")
    if not keys:
        print("No overlap. The cache and the LLM labels cover different sentences.")
        print("(If you labeled Tier A only, the d1 cache still has them; check key formatting.)")
        return

    conf_mat = defaultdict(Counter)        # truth(LLM) -> Counter(deberta)
    correct = 0
    poison = []                            # confident disagreements
    neg_total = neg_correct = pos_total = pos_correct = 0
    per_claim_dis = Counter()

    for k in keys:
        claim = k.split("||", 1)[0]
        d = cache[k]["claim"]
        dl = argmax_label(d)
        tl = llm[k]
        dc = deberta_conf(d)
        conf_mat[tl][dl] += 1
        ok = (dl == tl)
        correct += ok
        if not ok:
            per_claim_dis[claim] += 1
            if dc >= CONF:
                poison.append((claim, tl, dl, round(dc, 2), k.split("||", 1)[1]))
        if NEG_WORDS.search(claim):
            neg_total += 1; neg_correct += ok
        else:
            pos_total += 1; pos_correct += ok

    n = len(keys)
    print(f"\n1) DeBERTa per-sentence accuracy vs LLM reference: {correct}/{n} = {correct/n:.1%}")

    print("\n2) Confusion matrix (rows = LLM truth, cols = DeBERTa said):")
    labels = ["supporting", "neutral", "opposing"]
    print(f"   {'truth:':<16}" + "".join(f"{c[:5]:>9}" for c in labels))
    for t in labels:
        row = conf_mat[t]
        print(f"   {t:<16}" + "".join(f"{row[c]:>9}" for c in labels))

    print(f"\n3) Poison pile (DeBERTa confident >= {CONF} AND disagrees): {len(poison)} sentences"
          f"  ({len(poison)/n:.1%} of all)")
    dir_counts = Counter((t, d) for _, t, d, _, _ in poison)
    for (t, d), c in sorted(dir_counts.items(), key=lambda x: -x[1]):
        tag = ""
        if t == "neutral" and d in ("supporting", "opposing"):
            tag = "  <- FORCED VOTE (off-topic/uncertain pushed to a side)"
        elif {t, d} == {"supporting", "opposing"}:
            tag = "  <- HARD FLIP (negation / myth-restatement class)"
        print(f"   truth={t:<11} DeBERTa={d:<11} n={c}{tag}")

    print(f"\n4) Negation slice (claims containing not/never/only):")
    if neg_total:
        print(f"   negated claims : {neg_correct}/{neg_total} = {neg_correct/neg_total:.1%}")
    print(f"   other claims   : {pos_correct}/{pos_total} = {pos_correct/pos_total:.1%}")
    if neg_total and pos_total:
        gap = pos_correct/pos_total - neg_correct/neg_total
        print(f"   gap = {gap:+.1%}  (large positive gap => negation is a concrete learnable target)")

    print("\n5) Top claims by DeBERTa/LLM disagreement:")
    for claim, c in per_claim_dis.most_common(12):
        print(f"   {c:>3} disagreements  {claim[:54]}")

    print("\n--- FEASIBILITY READ ---")
    big = len(poison) / n
    if big >= 0.10:
        print(f"   Poison pile is {big:.0%} of sentences. That is a large, confident-wrong")
        print("   population. If it concentrates in the FORCED VOTE and HARD FLIP rows above,")
        print("   those are systematic, in-domain, learnable patterns -> fine-tuning is the")
        print("   right tool and should transfer. Aggregation alone cannot remove HARD FLIPs")
        print("   (confident + on-topic), so the model fix is doing real work here.")
    else:
        print(f"   Poison pile is only {big:.0%}. DeBERTa mostly agrees with the LLM and the")
        print("   disagreements are sparse. Fine-tuning has little to grip; prefer the")
        print("   aggregation fix alone and skip the fine-tune.")
    json.dump({"accuracy": correct/n, "poison_frac": len(poison)/n,
               "poison": poison[:200]}, open("d5_results.json", "w"), indent=2)
    print("\nWrote d5_results.json")

if __name__ == "__main__":
    main()