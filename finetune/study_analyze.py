"""
Source-utility study, step 2 of 2: the offline analysis.

Reads study_results.json (one record per claim with EVERY analyzed source,
neutrals included) and answers two questions with zero additional pipeline runs:

  1. UTILITY: which connectors/ranks produce sources that end up neutral,
     i.e. contribute nothing to the verdict and are dropped from output anyway?
  2. SAFETY: if we cut candidate ranks, do any of the 150 verdicts change?
     compute_verdict is a pure function, so every ablation is replayed offline
     on the logged stances. No re-searching, no re-inference.

Run inside the app container (imports compute_verdict from the app):
    docker compose exec app python finetune/study_analyze.py
"""

import os
import sys
import json
from types import SimpleNamespace

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.dirname(_SCRIPT_DIR)
for _p in (_REPO_ROOT, _SCRIPT_DIR, os.getcwd()):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from app.services.claim_service import compute_verdict  # noqa: E402

RESULTS_PATH = os.environ.get("RESULTS", os.path.join(_SCRIPT_DIR, "study_results.json"))

RANK_BUCKETS = [(1, 2), (3, 5), (6, 10), (11, 99)]


def bucket(rank: int) -> str:
    for lo, hi in RANK_BUCKETS:
        if lo <= rank <= hi:
            return f"{lo}-{hi}"
    return "?"


def pct(n, d):
    return f"{100.0 * n / d:5.1f}%" if d else "    -"


def verdict_for(sources, claim_type):
    objs = [SimpleNamespace(stance=s["stance"],
                            stance_confidence=s["stance_confidence"],
                            credibility_score=s["credibility_score"])
            for s in sources]
    return compute_verdict(objs, claim_type)[0]


def main():
    with open(RESULTS_PATH) as f:
        claims = json.load(f)
    all_sources = [s for c in claims for s in c["sources"]]
    total_sents = sum(s["n_sents"] or 0 for s in all_sources)
    print(f"claims: {len(claims)}   sources analyzed: {len(all_sources)}   "
          f"sentence-pairs: {total_sents}\n")

    # ---------- Table A: utility by connector ----------
    print("=" * 72)
    print("A. STANCE MIX BY CONNECTOR (neutral = contributes nothing, hidden anyway)")
    print("=" * 72)
    by_type = {}
    for s in all_sources:
        by_type.setdefault(s["source_type"], []).append(s)
    print(f"{'connector':<14}{'n':>5}{'neutral':>9}{'support':>9}{'oppose':>9}"
          f"{'sents':>7}{'sents%':>8}")
    for stype, srcs in sorted(by_type.items(), key=lambda kv: -len(kv[1])):
        n = len(srcs)
        neu = sum(1 for s in srcs if s["stance"] == "neutral")
        sup = sum(1 for s in srcs if s["stance"] == "supporting")
        opp = sum(1 for s in srcs if s["stance"] == "opposing")
        sents = sum(s["n_sents"] or 0 for s in srcs)
        print(f"{stype:<14}{n:>5}{pct(neu, n):>9}{pct(sup, n):>9}{pct(opp, n):>9}"
              f"{sents:>7}{pct(sents, total_sents):>8}")

    # ---------- Table B: neutral rate by connector x rank ----------
    print()
    print("=" * 72)
    print("B. NEUTRAL RATE BY CONNECTOR x RANK (is the tail junk?)")
    print("=" * 72)
    buckets = [f"{lo}-{hi}" for lo, hi in RANK_BUCKETS]
    print(f"{'connector':<14}" + "".join(f"{b + ' n/neu':>16}" for b in buckets))
    for stype, srcs in sorted(by_type.items(), key=lambda kv: -len(kv[1])):
        row = f"{stype:<14}"
        for b in buckets:
            grp = [s for s in srcs if bucket(s["rank"]) == b]
            neu = sum(1 for s in grp if s["stance"] == "neutral")
            row += f"{f'{len(grp)}/{pct(neu, len(grp)).strip()}':>16}"
        print(row)

    # ---------- Ablations ----------
    print()
    print("=" * 72)
    print("C. VERDICT-STABILITY ABLATIONS (offline replay of compute_verdict)")
    print("=" * 72)

    def cut_web(k):
        return lambda s: not (s["source_type"] == "web" and s["rank"] > k)

    def cut_type(stype, k):
        return lambda s: not (s["source_type"] == stype and s["rank"] > k)

    def combo(*keeps):
        return lambda s: all(keep(s) for keep in keeps)

    policies = [
        ("drop neutral sources (harness sanity: MUST be 0 flips)",
         lambda s: s["stance"] != "neutral"),
        ("web: keep top 5", cut_web(5)),
        ("web: keep top 3", cut_web(3)),
        ("academic: keep top 3", cut_type("academic", 3)),
        ("encyclopedia: keep top 3", cut_type("encyclopedia", 3)),
        ("fact_check: keep top 5", cut_type("fact_check", 5)),
        ("combo: web<=5 + academic<=3", combo(cut_web(5), cut_type("academic", 3))),
        ("combo: web<=3 + academic<=3 + encyclopedia<=3",
         combo(cut_web(3), cut_type("academic", 3), cut_type("encyclopedia", 3))),
    ]

    for name, keep in policies:
        flips = []
        removed_sources = 0
        removed_sents = 0
        for c in claims:
            kept = [s for s in c["sources"] if keep(s)]
            removed = [s for s in c["sources"] if not keep(s)]
            removed_sources += len(removed)
            removed_sents += sum(s["n_sents"] or 0 for s in removed)
            new_verdict = verdict_for(kept, c["claim_type"])
            if new_verdict != c["verdict"]:
                flips.append((c["claim"], c["verdict"], new_verdict))
        print(f"\n  {name}")
        print(f"    sources removed: {removed_sources}/{len(all_sources)} "
              f"({pct(removed_sources, len(all_sources)).strip()})  |  "
              f"sentence-pairs removed: {removed_sents}/{total_sents} "
              f"({pct(removed_sents, total_sents).strip()})")
        print(f"    verdict flips: {len(flips)}/{len(claims)}")
        for claim, old, new in flips[:8]:
            print(f"      FLIP {claim[:50]!r}: {old} -> {new}")
        if len(flips) > 8:
            print(f"      ... and {len(flips) - 8} more")


if __name__ == "__main__":
    main()
