"""
Scan claim_roster.json for duplicate / overlapping claims, ALL pairs including
existing-vs-existing (which the roster builder skipped). Two detectors:

  1. Semantic near-dup (MiniLM cosine, if available): catches paraphrases even when
     wording differs, e.g. "10 percent of their brain" vs "10% of our brains".
  2. Shared distinctive keyword: catches SAME-ENTITY claims that are different
     propositions (e.g. Everest 'highest mountain' vs Everest 'closest to space'),
     which semantic similarity misses because the claims genuinely differ.

Reports two groups:
  CRITICAL = overlap spans TRAIN and TEST  -> leakage, fix before training.
  CLEANUP  = overlap within the same split -> redundant, optional to trim.

Pure stdlib if sentence-transformers is missing (falls back to string similarity).
Run after editing the roster to confirm it's clean.
  python diagnostics/find_duplicates.py
"""
import json, re, os
from itertools import combinations
from collections import defaultdict
from difflib import SequenceMatcher

SEM = float(os.environ.get("SEM_THRESHOLD", "0.80"))   # semantic near-dup
STR = float(os.environ.get("STR_THRESHOLD", "0.80"))   # string near-dup fallback
STOP = set("a an the is are was were be been being of to in on for and or not no this that "
           "with from as it its by at do does did have has had will would can could should "
           "may might must than then so such about into over under more most less least only "
           "just both each any all some which who whom whose what when where why how their our "
           "his her them they we you i he she".split())

def tokens(c):
    return set(w for w in re.findall(r"[a-z']+", c.lower()) if w not in STOP and len(w) > 2)

def main():
    roster = json.load(open("claim_roster.json"))
    claims = [r["claim"] for r in roster]
    splits = [r["split"] for r in roster]
    toks = [tokens(c) for c in claims]

    # semantic matrix (optional)
    sem = None
    try:
        from sentence_transformers import SentenceTransformer
        m = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        emb = m.encode(claims, normalize_embeddings=True)
        sem = emb @ emb.T
        print("Semantic detector: MiniLM embeddings")
    except Exception as e:
        print(f"Semantic detector unavailable ({e}); using string similarity only")

    # which claims contain each word, to find distinctive (entity-like) shared words
    word_claims = defaultdict(list)
    for i, t in enumerate(toks):
        for w in t:
            word_claims[w].append(i)

    flagged = []
    for i, j in combinations(range(len(claims)), 2):
        s = float(sem[i][j]) if sem is not None else SequenceMatcher(None, claims[i], claims[j]).ratio()
        shared = toks[i] & toks[j]
        distinctive = sorted(w for w in shared if 2 <= len(word_claims[w]) <= 3)
        reason = None
        if s >= (SEM if sem is not None else STR):
            reason = f"near-dup ({s:.2f})"
        elif distinctive:
            reason = f"same entity: {distinctive}"
        if reason:
            flagged.append((i, j, reason, s))

    crit = [(i, j, r, s) for i, j, r, s in flagged if splits[i] != splits[j]]
    clean = [(i, j, r, s) for i, j, r, s in flagged if splits[i] == splits[j]]

    print(f"\nScanned {len(claims)} claims. Flagged {len(flagged)} overlapping pairs.\n")
    print(f"=== CRITICAL: spans train/test ({len(crit)}) -> fix these (drop one side) ===")
    for i, j, r, s in sorted(crit, key=lambda x: -x[3]):
        print(f"  [{splits[i]} | {splits[j]}] {r}")
        print(f"     '{claims[i]}'")
        print(f"     '{claims[j]}'")
    print(f"\n=== CLEANUP: same split ({len(clean)}) -> redundant, optional ===")
    for i, j, r, s in sorted(clean, key=lambda x: -x[3]):
        print(f"  [{splits[i]}] {r}")
        print(f"     '{claims[i]}'")
        print(f"     '{claims[j]}'")
    if not crit:
        print("\n(No train/test leaks. Roster is clean on that axis.)")

if __name__ == "__main__":
    main()