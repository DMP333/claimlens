"""
DIAGNOSTIC 2  (Step 1b, LABEL-FREE):  How much of the problem is 3K aggregation?

3K never returns neutral and manufactures a confident direction from accumulated
weak per-sentence signal, so off-topic sources cannot drop out. We re-aggregate the
SAME per-sentence NLI outputs with 3K / 3A / 3J / 3N (neutral-capable) and measure:
  (1) do contaminated sources go NEUTRAL under 3N (i.e. does abstention neutralize them)
  (2) do Tier A verdicts move toward the correct answer under 3N vs 3K

Reuses sentence_nli_cache.json from d1 if present (else re-runs NLI on snippets).
Run from repo root with labeled_sources.json (+ tiers.json for verdict scoring).
  python diagnostics/d2_aggregation_swap.py
"""
import json, sys, os
sys.path.insert(0, os.getcwd())
from collections import Counter
from app.services.nli_service import split_sentences, _run_nli_batch, DEFAULT_MIN_WORDS, compute_relevance
from common import load_sources, by_claim, load_json, SourceStance, compute_verdict_local, verdict_band
from aggregators import STRATEGIES

SENT_TYPES = {"encyclopedia", "academic", "web"}

def sent_probs_for(rows, cache):
    """Return {source_index: [per-sentence prob dicts]} for sentence-NLI sources.
    Pulls NLI probs from cache by (claim, sentence) (running NLI only for misses)
    and attaches per-sentence relevance ('rel', MiniLM cosine to the claim) used by 3R."""
    out, sents_by_i, missing = {}, {}, []
    for i, r in enumerate(rows):
        if r["source_type"] not in SENT_TYPES:
            continue
        claim = r["claim"]; text = r.get("snippet_only") or r.get("title_only") or ""
        sents = [s for s in split_sentences(text) if len(s.split()) >= DEFAULT_MIN_WORDS]
        sents_by_i[i] = sents
        probs = []
        for s in sents:
            key = f"{claim}||{s}"
            if cache and key in cache:
                probs.append(dict(cache[key]["claim"]))   # copy so 'rel' attaches per-source
            else:
                missing.append((i, len(probs), claim, s)); probs.append(None)
        out[i] = probs
    if missing:
        print(f"  NLI cache miss for {len(missing)} sentences; running NLI...")
        by_c = {}
        for idx, pos, claim, s in missing:
            by_c.setdefault(claim, []).append((idx, pos, s))
        for claim, items in by_c.items():
            r = _run_nli_batch([s for *_, s in items], claim)
            for (idx, pos, _s), pr in zip(items, r):
                out[idx][pos] = pr
    # attach per-sentence relevance to the claim (reuses existing MiniLM scorer)
    for i, sents in sents_by_i.items():
        if not sents:
            continue
        rels = compute_relevance(rows[i]["claim"], sents)
        for p, rel in zip(out[i], rels):
            if p is not None:
                p["rel"] = rel
    return out

def main():
    rows = load_sources()
    cache = load_json("sentence_nli_cache.json")
    tiers = load_json("tiers.json", {})
    if not cache:
        print("(no sentence_nli_cache.json; will run NLI fresh - slower. Run d1 first to cache.)")
    sp = sent_probs_for(rows, cache)

    # ---- per-source stance under each strategy ----
    stances = {name: {} for name in STRATEGIES}     # name -> {src_index: (stance, conf)}
    for i, probs in sp.items():
        probs = [p for p in probs if p]
        for name, fn in STRATEGIES.items():
            stances[name][i] = fn(probs) if probs else ("neutral", 0.0)

    # ---- (1) contamination neutralization: 3N vs 3K ----
    print("=" * 72)
    print("(1) Does 3N send contaminated sources to neutral? (3K cannot, by design)")
    print("=" * 72)
    for name in list(STRATEGIES):
        c_total = c_neutral = clean_total = clean_neutral = 0
        for i, r in enumerate(rows):
            if i not in stances[name]:
                continue
            st = stances[name][i][0]
            if r["is_contaminated"]:
                c_total += 1; c_neutral += (st == "neutral")
            else:
                clean_total += 1; clean_neutral += (st == "neutral")
        print(f"  {name}: contaminated->neutral {c_neutral:>3}/{c_total:<3} | "
              f"clean->neutral {clean_neutral:>4}/{clean_total:<4}")
    print("  (3N should neutralize many contaminated sources while keeping most clean ones non-neutral.)")

    # ---- (2) Tier A verdict accuracy under each strategy ----
    def claim_type(c): return "factual"  # Tier A are factual
    def predicts(band):
        if band in ("strongly supported","likely supported"): return True
        if band in ("strongly opposed","likely opposed"): return False
        return None  # contested / insufficient => abstain (counts as miss for accuracy)

    claims = by_claim(rows)
    idx_of = {}
    pos = 0
    # map (claim)-> list of (global source row index) by reconstructing order
    # rebuild: iterate rows once, group indices by claim
    claim_rows = {}
    for i, r in enumerate(rows):
        claim_rows.setdefault(r["claim"], []).append(i)

    print("\n" + "=" * 72)
    print("(2) Tier A verdict band per strategy (truth from tiers.json)")
    print("=" * 72)
    correct = Counter(); total_A = 0
    detail = []
    for claim, idxs in claim_rows.items():
        t = tiers.get(claim, {})
        if t.get("tier") != "A" or t.get("truth") is None:
            continue
        total_A += 1
        truth = t["truth"]
        row_bands = {}
        for name in list(STRATEGIES):
            srcs = []
            for i in idxs:
                r = rows[i]
                if r["source_type"] == "knowledge_graph":
                    srcs.append(SourceStance("neutral", 1.0))
                elif r["source_type"] == "fact_check":
                    srcs.append(SourceStance(r["pipeline_stance"], 1.0))
                elif i in stances[name]:
                    st, _ = stances[name][i]
                    srcs.append(SourceStance(st, 1.0))
            # unweighted verdict (conf=cred=1) to isolate stance composition
            ws = sum(1 for s in srcs if s.stance == "supporting")
            wo = sum(1 for s in srcs if s.stance == "opposing")
            ratio = ws/(ws+wo) if (ws+wo) else None
            band = verdict_band(ratio)
            row_bands[name] = (band, ws, wo)
            if predicts(band) == truth:
                correct[name] += 1
        detail.append((claim, truth, row_bands))

    print(f"\n  Tier A claims scored: {total_A}")
    print(f"  {'strategy':<8} correct verdicts")
    for name in list(STRATEGIES):
        print(f"  {name:<8} {correct[name]:>3}/{total_A}")
    print("\n  Per-claim (T=true F=false; band [S/O]):")
    for claim, truth, rb in sorted(detail, key=lambda x: x[0]):
        cells = "  ".join(f"{n}:{rb[n][0][:9]:<9}[{rb[n][1]}/{rb[n][2]}]" for n in ["3K","3N","3R"])
        print(f"    {'T' if truth else 'F'} {claim[:34]:<34} {cells}")

    json.dump({"contam_neutralization": True, "tierA_correct": dict(correct), "total_A": total_A},
              open("d2_results.json", "w"), indent=2)
    print("\nWrote d2_results.json")

if __name__ == "__main__":
    main()