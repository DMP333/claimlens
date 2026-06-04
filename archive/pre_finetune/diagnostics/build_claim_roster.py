"""
STEP 1 of dataset expansion: assemble a clean, NON-OVERLAPPING, STRATIFIED roster.

Does NOT retrieve or label. It:
  1. Loads existing claims (already have data -> training pool).
  2. Loads candidate new claims WITH their category (true/false/contested) parsed
     from the '# =====' section headers in the candidates file.
  3. Exact-dedup + near-dup flag (sentence embeddings) within candidates and vs existing.
  4. STRATIFIED split: the test set is balanced across true/false (so the accuracy
     number can't be gamed by a class prior) with contested filling the remainder;
     existing -> train, leftover new -> train up to TARGET_TRAIN.
  5. Hard boundary check: no test claim is a near-dup of any train claim.
  6. Writes claim_roster.json (with category) and prints per-category counts + dup pairs.

Inputs (repo root):
  labeled_sources.json
  CANDIDATES_FILE=path.txt   (headers '# ===== ... TRUE/FALSE/CONTESTED ... =====')
Tunables: SIM_THRESHOLD (0.85), TARGET_TRAIN (100), TARGET_TEST (50), SEED (0)

  CANDIDATES_FILE=diagnostics/claims_candidates.txt python diagnostics/build_claim_roster.py
"""
import os, sys, json, re, random
from common import load_sources

SIM = float(os.environ.get("SIM_THRESHOLD", "0.85"))
TARGET_TRAIN = int(os.environ.get("TARGET_TRAIN", "100"))
TARGET_TEST = int(os.environ.get("TARGET_TEST", "50"))
random.seed(int(os.environ.get("SEED", "0")))

def normalize(c):
    c = c.strip().lower(); c = re.sub(r"\s+", " ", c); c = re.sub(r"[.?!]+$", "", c)
    return c

def header_category(line):
    u = line.upper()
    if "FALSE" in u or "DEBUNK" in u: return "false"
    if "TRUE" in u: return "true"
    if "CONTESTED" in u or "OPINION" in u or "DEBATED" in u: return "contested"
    return None

def load_candidates():
    """Return list of (claim, category). Category from the most recent '# =====' header."""
    f = os.environ.get("CANDIDATES_FILE")
    if not (f and os.path.exists(f)):
        print(f"Set CANDIDATES_FILE to your claims .txt. Got: {f}")
        return []
    out, cat = [], "unknown"
    for line in open(f):
        s = line.strip()
        if not s:
            continue
        if s.startswith("#"):
            hc = header_category(s)
            if hc: cat = hc
            continue
        out.append((s, cat))
    return out

def similarity_fn(all_claims):
    try:
        from sentence_transformers import SentenceTransformer
        m = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        emb = m.encode(all_claims, normalize_embeddings=True)
        sim = emb @ emb.T
        return (lambda i, j: float(sim[i][j])), "MiniLM embeddings"
    except Exception as e:
        from difflib import SequenceMatcher
        print(f"  (sentence-transformers unavailable: {e}; difflib fallback)")
        return (lambda i, j: SequenceMatcher(None, all_claims[i], all_claims[j]).ratio()), "difflib"

def main():
    existing = sorted({normalize(r["claim"]) for r in load_sources()})
    cand_raw = load_candidates()
    if not cand_raw:
        return

    # exact dedup (vs existing and within candidates), keep category
    seen = set(existing); cands = []; cats = {}; exact = 0
    for c, cat in cand_raw:
        nc = normalize(c)
        if nc in seen:
            exact += 1; continue
        seen.add(nc); cands.append(nc); cats[nc] = cat
    print(f"\nExisting: {len(existing)} | candidates after exact-dedup: {len(cands)} "
          f"| exact dups removed: {exact}")
    by_cat = {}
    for c in cands: by_cat.setdefault(cats[c], []).append(c)
    print("  candidate categories: " + ", ".join(f"{k}={len(v)}" for k, v in sorted(by_cat.items())))

    all_claims = existing + cands
    sim, method = similarity_fn(all_claims)
    print(f"Near-dup detection: {method}, threshold {SIM}")
    nE = len(existing)

    # near-dup flags
    flagged = set(); ve = []; vc = []
    for ci in range(len(cands)):
        gi = nE + ci
        for ei in range(nE):
            if sim(gi, ei) >= SIM:
                ve.append((cands[ci], existing[ei], round(sim(gi, ei), 2))); flagged.add(ci); break
    for a in range(len(cands)):
        if a in flagged: continue
        for b in range(a + 1, len(cands)):
            if b in flagged: continue
            if sim(nE + a, nE + b) >= SIM:
                vc.append((cands[a], cands[b], round(sim(nE + a, nE + b), 2))); flagged.add(b)
    if ve:
        print(f"\nNEAR-DUP vs existing (candidate dropped): {len(ve)}")
        for c, e, s in ve[:30]: print(f"   {s}  new:'{c[:42]}' ~ exist:'{e[:42]}'")
    if vc:
        print(f"\nNEAR-DUP candidate vs candidate (one dropped): {len(vc)}")
        for a, b, s in vc[:30]: print(f"   {s}  '{a[:42]}' ~ '{b[:42]}'")

    # unique-new by category, shuffled for fair sampling
    uniq = {}
    for c in cands:
        if c in [cands[i] for i in flagged]: continue
        uniq.setdefault(cats[c], []).append(c)
    for k in uniq: random.shuffle(uniq[k])
    total_uniq = sum(len(v) for v in uniq.values())

    # ---- STRATIFIED test split: balance true vs false, contested fills remainder ----
    n_contested = min(len(uniq.get("contested", [])), TARGET_TEST // 4)   # ~25% contested
    rem = TARGET_TEST - n_contested
    per_tf = rem // 2
    n_true = min(len(uniq.get("true", [])), per_tf)
    n_false = min(len(uniq.get("false", [])), per_tf)
    # top up to TARGET_TEST if a category was short
    test = (uniq.get("true", [])[:n_true] + uniq.get("false", [])[:n_false]
            + uniq.get("contested", [])[:n_contested])
    pools_left = (uniq.get("true", [])[n_true:] + uniq.get("false", [])[n_false:]
                  + uniq.get("contested", [])[n_contested:])
    random.shuffle(pools_left)
    while len(test) < TARGET_TEST and pools_left:
        test.append(pools_left.pop())
    test_set = set(test)

    # ---- train: existing + leftover new up to TARGET_TRAIN ----
    train_new_needed = max(0, TARGET_TRAIN - len(existing))
    train_new = [c for c in (sum(uniq.values(), [])) if c not in test_set][:train_new_needed]
    train_claims = existing + train_new

    # ---- hard boundary check: no test near-dups a train claim ----
    leaks = []; safe_test = []
    train_gi = {c: all_claims.index(c) for c in train_claims}
    for t in test:
        gi = all_claims.index(t)
        leak = next((tr for tr in train_claims if sim(gi, train_gi[tr]) >= SIM), None)
        (leaks.append((t, leak)) if leak else safe_test.append(t))
    if leaks:
        print(f"\nBOUNDARY LEAK BLOCKED ({len(leaks)} test claims near-dup a train claim, dropped):")
        for t, tr in leaks[:20]: print(f"   test:'{t[:42]}' ~ train:'{tr[:42]}'")

    roster = ([{"claim": c, "split": "train", "origin": "existing", "category": "existing"} for c in existing]
              + [{"claim": c, "split": "train", "origin": "new", "category": cats[c], "needs_retrieval": True} for c in train_new]
              + [{"claim": c, "split": "test", "origin": "new", "category": cats[c], "needs_retrieval": True} for c in safe_test])
    json.dump(roster, open("claim_roster.json", "w"), indent=2)

    def catcount(items):
        cc = {};
        for c in items: cc[cats.get(c, "existing")] = cc.get(cats.get(c, "existing"), 0) + 1
        return cc
    print("\n" + "=" * 56)
    print(f"ROSTER  (target train {TARGET_TRAIN}, test {TARGET_TEST})")
    print(f"  TRAIN: {len(train_claims)}  = {len(existing)} existing + {len(train_new)} new")
    print(f"     new-claim categories: {catcount(train_new)}")
    print(f"  TEST:  {len(safe_test)} new  categories: {catcount(safe_test)}")
    tf = catcount(safe_test)
    print(f"     true/false balance in test: true={tf.get('true',0)} false={tf.get('false',0)} "
          f"(should be roughly equal so the accuracy number can't be gamed)")
    if total_uniq < train_new_needed + TARGET_TEST:
        print(f"\n  NOTE: only {total_uniq} unique new claims; wanted {train_new_needed + TARGET_TEST}. "
              f"Add more to a category if a split came up short.")
    print("\nWrote claim_roster.json. Review dup pairs (if any) and the test true/false balance.")

if __name__ == "__main__":
    main()