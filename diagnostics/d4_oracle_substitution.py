"""
DIAGNOSTIC 4  (Step 4):  Oracle substitution = WHERE is the bottleneck?

Replace one stage's output with ground truth at a time; measure Tier A verdict
accuracy. The rung with the biggest jump from baseline is the stage to fix.

Rungs:
  R0 baseline            : current pipeline_stance               (data-only)
  R1 oracle_relevance    : drop contaminated sources             (data-only)
                           Δ(R1-R0) = ceiling from PERFECT filtering
  R2 oracle_sent_labels  : gold sentence labels -> 3K aggregation (needs LLM labels)
                           Δ(R2-R0) = ceiling from fixing the per-sentence MODEL
  R3 oracle_source_stance: gold sentence labels -> IDEAL (neutral-capable) aggregation
                           Δ(R3-R2) = headroom from fixing AGGREGATION specifically

Tier A only (truth-labelable). Verdict is unweighted (conf=cred=1) to match d2.
Run from repo root with labeled_sources.json + tiers.json (+ sentence_labels_llm.json for R2/R3).
  python diagnostics/d4_oracle_substitution.py
"""
import json, sys, os
sys.path.insert(0, os.getcwd())
from collections import Counter
from common import load_sources, load_json, SourceStance, verdict_band
from aggregators import agg_3k

SENT_TYPES = {"encyclopedia", "academic", "web"}
PSEUDO = {"supporting": {"p_supp":0.9,"p_neut":0.05,"p_opp":0.05},
          "opposing":   {"p_supp":0.05,"p_neut":0.05,"p_opp":0.9},
          "neutral":    {"p_supp":0.1,"p_neut":0.8,"p_opp":0.1}}

def predicts(band):
    if band in ("strongly supported","likely supported"): return True
    if band in ("strongly opposed","likely opposed"): return False
    return None

def unweighted_verdict(stances):
    ws = sum(1 for s in stances if s == "supporting")
    wo = sum(1 for s in stances if s == "opposing")
    return verdict_band(ws/(ws+wo) if (ws+wo) else None)

def ideal_agg(labels):
    s = labels.count("supporting"); o = labels.count("opposing")
    if s == o: return "neutral"
    return "supporting" if s > o else "opposing"

def main():
    rows = load_sources()
    tiers = load_json("tiers.json", {})
    try:
        from app.services.nli_service import split_sentences, DEFAULT_MIN_WORDS
    except Exception:
        split_sentences = None
    sent_labels = load_json("sentence_labels_llm.json")  # may be None

    claim_rows = {}
    for i, r in enumerate(rows):
        claim_rows.setdefault(r["claim"], []).append(i)

    tierA = [(c, idxs) for c, idxs in claim_rows.items()
             if tiers.get(c, {}).get("tier") == "A" and tiers.get(c, {}).get("truth") is not None]
    total = len(tierA)
    acc = Counter(); have_R23 = bool(sent_labels and split_sentences)

    per_claim = []
    for claim, idxs in tierA:
        truth = tiers[claim]["truth"]
        bands = {}

        # R0 baseline
        st0 = [rows[i]["pipeline_stance"] for i in idxs]
        bands["R0"] = unweighted_verdict(st0)

        # R1 oracle relevance (drop contaminated)
        st1 = [rows[i]["pipeline_stance"] for i in idxs if not rows[i]["is_contaminated"]]
        bands["R1"] = unweighted_verdict(st1)

        if have_R23:
            # build sentence-NLI source stances from gold labels
            src_stances_R2, src_stances_R3 = [], []
            for i in idxs:
                r = rows[i]
                if r["source_type"] == "knowledge_graph":
                    src_stances_R2.append("neutral"); src_stances_R3.append("neutral"); continue
                if r["source_type"] == "fact_check":
                    src_stances_R2.append(r["pipeline_stance"]); src_stances_R3.append(r["pipeline_stance"]); continue
                text = r.get("snippet_only") or ""
                sents = [s for s in split_sentences(text) if len(s.split()) >= DEFAULT_MIN_WORDS]
                glabels = [sent_labels.get(f"{claim}||{s}") for s in sents]
                glabels = [g for g in glabels if g]
                if not glabels:
                    src_stances_R2.append("neutral"); src_stances_R3.append("neutral"); continue
                # R2: gold labels -> pseudo-probs -> 3K (current aggregation)
                st_r2, _ = agg_3k([PSEUDO[g] for g in glabels])
                src_stances_R2.append(st_r2)
                # R3: gold labels -> ideal neutral-capable aggregation
                src_stances_R3.append(ideal_agg(glabels))
            bands["R2"] = unweighted_verdict(src_stances_R2)
            bands["R3"] = unweighted_verdict(src_stances_R3)

        for k, b in bands.items():
            if predicts(b) == truth: acc[k] += 1
        per_claim.append((claim, truth, bands))

    print("=" * 64)
    print(f"ORACLE SUBSTITUTION  (Tier A, n={total})")
    print("=" * 64)
    rungs = ["R0","R1"] + (["R2","R3"] if have_R23 else [])
    names = {"R0":"baseline (current stances)","R1":"+oracle relevance (drop contam)",
             "R2":"+gold sentence labels, 3K agg","R3":"+gold labels, ideal agg"}
    prev = None
    for k in rungs:
        d = f"   Δ {acc[k]-prev:+d}" if prev is not None else ""
        print(f"  {k}  {acc[k]:>3}/{total}  {names[k]:<34}{d}")
        prev = acc[k]
    if not have_R23:
        print("\n  (R2/R3 skipped: run llm_label_sentences.py to produce sentence_labels_llm.json,")
        print("   then re-run. R2-R0 = model ceiling; R3-R2 = aggregation headroom.)")
    else:
        print("\n  Read it: large R1-R0 => filtering is the lever (we expect SMALL).")
        print("           large R2-R0 => per-sentence NLI model is the bottleneck.")
        print("           large R3-R2 => aggregation (3K) is a distinct, separable problem.")
    json.dump({"acc": dict(acc), "total": total}, open("d4_results.json","w"), indent=2)
    print("\nWrote d4_results.json")

if __name__ == "__main__":
    main()
