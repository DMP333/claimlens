"""Aggregation strategies over per-sentence NLI probs.
3K/3A/3J mirror app.services.nli_service; 3N is neutral-capable; 3R adds relevance weighting.
Each sentence dict has p_supp/p_neut/p_opp; 3R also reads 'rel' (relevance to claim)."""
import math

def agg_3k(sr, **k):
    lo = 0.0
    for s in sr:
        lo += math.log(max(s["p_supp"],1e-6)/max(s["p_opp"],1e-6))
    p = 1.0 if lo>500 else 0.0 if lo<-500 else 1.0/(1.0+math.exp(-lo))
    return ("supporting", p) if p>0.5 else ("opposing", 1.0-p)

def agg_3a(sr, **k):
    b = max(sr, key=lambda s: max(s["p_supp"], s["p_opp"]))
    return ("supporting", b["p_supp"]) if b["p_supp"]>b["p_opp"] else ("opposing", b["p_opp"])

def agg_3j(sr, k=3, **kw):
    ka = min(k, len(sr))
    if ka == 0: return "neutral", 0.5
    bs = sorted(sr, key=lambda s: s["p_supp"], reverse=True)
    bo = sorted(sr, key=lambda s: s["p_opp"], reverse=True)
    a_s = sum(s["p_supp"] for s in bs[:ka])/ka
    a_o = sum(s["p_opp"] for s in bo[:ka])/ka
    if abs(a_s-a_o) < 0.01: return "neutral", 0.5
    return ("supporting", a_s) if a_s>a_o else ("opposing", a_o)

def agg_3n(sr, conf=0.55, margin=0.10, **k):
    """Neutral-capable confident vote: sentences without a confident non-neutral
    signal ABSTAIN; if nothing confident remains, or sides are within `margin`, neutral."""
    vs, vo = [], []
    for s in sr:
        top = max(s["p_supp"], s["p_opp"])
        if top < conf or s["p_neut"] >= top:
            continue
        (vs if s["p_supp"] >= s["p_opp"] else vo).append(top)
    ssum, osum = sum(vs), sum(vo); tot = ssum + osum
    if tot == 0: return "neutral", 0.0
    if abs(ssum-osum) < margin*tot: return "neutral", 0.0
    return ("supporting", ssum/tot) if ssum>osum else ("opposing", osum/tot)

def agg_3r(sr, band=0.15, rel_floor=0.25, **k):
    """Relevance-weighted, neutral-capable (the production candidate).
    Relevance acts as BOTH a gate and a weight: sentences below `rel_floor` are
    dropped entirely (so an all-junk source returns neutral), and the survivors are
    weighted by relevance x directional-mass (1 - p_neut), so model-uncertain
    sentences also fade. Returns the weighted mean direction; abstains to neutral
    when no sentence clears the floor or the direction is inside `band`.
    rel_floor/band are tunable (his source RELEVANCE_THRESHOLD is 0.35; sentences sit lower)."""
    kept = [s for s in sr if s.get("rel", 1.0) >= rel_floor]
    if not kept:
        return "neutral", 0.0                          # nothing sufficiently on-topic
    signal = mass = 0.0
    for s in kept:
        w = s.get("rel", 1.0) * (s["p_supp"] + s["p_opp"])
        signal += w * (s["p_supp"] - s["p_opp"])
        mass += w
    if mass <= 1e-9:
        return "neutral", 0.0
    score = signal / mass                              # weighted mean of (p_supp - p_opp), [-1,1]
    if abs(score) < band:
        return "neutral", abs(score)
    return ("supporting", score) if score > 0 else ("opposing", -score)

STRATEGIES = {"3K": agg_3k, "3A": agg_3a, "3J": agg_3j, "3N": agg_3n, "3R": agg_3r}