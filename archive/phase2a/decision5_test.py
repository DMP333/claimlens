"""
Decision 5 Test: Sentence-Level Relevance Filtering

Tests whether filtering sentences before aggregation helps accuracy.
Uses existing decision2_3_data.json (no pipeline re-run needed).

Configurations tested:
  Filters: none (baseline), 5B (pattern), 5C (MiniLM relevance), 5B+5C
  Strategies: 3K, 3A, 3J
  5C thresholds: 0.2, 0.3, 0.4, 0.5

Key tracking:
  - FALSE REMOVALS: non-neutral sentences incorrectly filtered out
  - REGRESSIONS: sources correct without filter, wrong with filter
  - IMPROVEMENTS: sources wrong without filter, correct with filter

Usage:
  python decision5_test.py

Requires: decision2_3_data.json in tests/ (from Decision 2+3 collect phase)
Output: tests/decision5_report.txt
"""

import json
import os
import re
import math
from datetime import datetime
from collections import defaultdict, Counter

from sentence_transformers import SentenceTransformer
import numpy as np

DATA_PATH = "tests/decision2_3_data.json"
REPORT_PATH = "tests/decision5_report.txt"

# ============================================================
# 5B: PATTERN-BASED JUNK REMOVAL
# ============================================================

# Patterns that indicate a sentence is non-content junk
JUNK_PATTERNS = [
    # Citation identifiers
    r'\bISBN\b',
    r'\bDOI\b',
    r'\bISSN\b',
    r'\bPMID\b',
    r'\bOCLC\b',
    r'\bdoi:\s*10\.',
    # Date retrieval / archival
    r'\bRetrieved\s+\d',
    r'\bAccessed\s+\d',
    r'\bArchived\s+from\s+the\s+original',
    # Wikipedia citation markers
    r'^-\s*\^',
    r'^\^\s*[a-z]\s+[a-z]\s+',
    # Section/editorial markers
    r'^\[edit\]',
    r'\[citation\s+needed\]',
    r'\[unreliable',
    # Navigation / boilerplate
    r'\bBecome\s+a\s+member\b',
    r'\bFollow\s+us\s+on\b',
    r'\bSign\s+up\b.*\bnewsletter\b',
    r'\bSubscribe\b.*\b(newsletter|updates)\b',
    r'\bMore\s+from\s+the\s+Fact-Check\b',
    # URL-heavy (sentence is mostly a URL)
    r'https?://\S{50,}',
]

_compiled_junk = [re.compile(p, re.IGNORECASE) for p in JUNK_PATTERNS]


def is_junk_5b(text: str) -> bool:
    """Returns True if the sentence matches any junk pattern."""
    for pattern in _compiled_junk:
        if pattern.search(text):
            return True
    return False


# ============================================================
# 5C: MINILM RELEVANCE FILTERING
# ============================================================

def compute_sentence_relevance(claim: str, sentences: list[str], model) -> list[float]:
    """Compute MiniLM cosine similarity between claim and each sentence."""
    if not sentences:
        return []
    claim_emb = model.encode([claim], normalize_embeddings=True)
    sent_embs = model.encode(sentences, normalize_embeddings=True)
    scores = np.dot(sent_embs, claim_emb.T).flatten()
    return scores.tolist()


# ============================================================
# AGGREGATION STRATEGIES (same as nli_service.py)
# ============================================================

def agg_3k(sents):
    if not sents:
        return "neutral", 0.5
    lo = sum(math.log(max(s["p_supp"], 1e-6) / max(s["p_opp"], 1e-6)) for s in sents)
    if abs(lo) > 500:
        p = 1.0 if lo > 0 else 0.0
    else:
        p = 1.0 / (1.0 + math.exp(-lo))
    return ("supporting" if p > 0.5 else "opposing"), (p if p > 0.5 else 1.0 - p)


def agg_3a(sents):
    if not sents:
        return "neutral", 0.5
    best = max(sents, key=lambda s: max(s["p_supp"], s["p_opp"]))
    return ("supporting" if best["p_supp"] > best["p_opp"] else "opposing"), max(best["p_supp"], best["p_opp"])


def agg_3j(sents, k=3):
    if not sents:
        return "neutral", 0.5
    k_actual = min(k, len(sents))
    by_s = sorted(sents, key=lambda s: s["p_supp"], reverse=True)
    by_o = sorted(sents, key=lambda s: s["p_opp"], reverse=True)
    avg_s = sum(s["p_supp"] for s in by_s[:k_actual]) / k_actual
    avg_o = sum(s["p_opp"] for s in by_o[:k_actual]) / k_actual
    if abs(avg_s - avg_o) < 0.01:
        return "neutral", 0.5
    return ("supporting" if avg_s > avg_o else "opposing"), max(avg_s, avg_o)


STRATEGIES = {"3K": agg_3k, "3A": agg_3a, "3J": agg_3j}
RELEVANCE_THRESHOLDS = [0.2, 0.3, 0.4, 0.5]


# ============================================================
# MAIN
# ============================================================

def main():
    with open(DATA_PATH) as f:
        all_data = json.load(f)

    scoreable = [d for d in all_data if d["expected_stance"] != "mixed"]
    print(f"Loaded {len(all_data)} sources, {len(scoreable)} scoreable")

    # Compute relevance scores for all sentences (one-time)
    print("Loading MiniLM for sentence relevance scoring...")
    rel_model = SentenceTransformer("all-MiniLM-L6-v2")

    print("Computing per-sentence relevance scores...")
    for d in all_data:
        texts = [s["text"] for s in d["sentences"]]
        if texts:
            scores = compute_sentence_relevance(d["claim"], texts, rel_model)
            for s, score in zip(d["sentences"], scores):
                s["relevance"] = round(score, 4)
        else:
            for s in d["sentences"]:
                s["relevance"] = 0.0
    print("Relevance scores computed.")

    # ============================================================
    # Define filter configurations
    # ============================================================
    filter_configs = [
        ("none", lambda s, d: True),
    ]

    # 5B only
    filter_configs.append(("5B_pattern", lambda s, d: not is_junk_5b(s["text"])))

    # 5C at various thresholds
    for t in RELEVANCE_THRESHOLDS:
        filter_configs.append((f"5C_rel>{t}", lambda s, d, thresh=t: s.get("relevance", 1.0) >= thresh))

    # 5B + 5C combined
    for t in RELEVANCE_THRESHOLDS:
        filter_configs.append((
            f"5B+5C_rel>{t}",
            lambda s, d, thresh=t: (not is_junk_5b(s["text"])) and s.get("relevance", 1.0) >= thresh
        ))

    out = []
    out.append(f"Decision 5 Analysis Report")
    out.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    out.append(f"Scoreable sources: {len(scoreable)}")
    out.append(f"Filter configs: {len(filter_configs)}")
    out.append(f"Strategies: {list(STRATEGIES.keys())}")
    out.append("")

    # ============================================================
    # SECTION 1: WHAT DOES 5B ACTUALLY REMOVE?
    # ============================================================
    out.append("=" * 80)
    out.append("SECTION 1: 5B PATTERN FILTER IMPACT")
    out.append("=" * 80)
    out.append("")

    total_removed_5b = 0
    removed_labels_5b = Counter()
    false_removals_5b = []

    for d in scoreable:
        mw_sents = [s for s in d["sentences"] if s["word_count"] >= 10]
        for s in mw_sents:
            if is_junk_5b(s["text"]):
                total_removed_5b += 1
                removed_labels_5b[s["label"]] += 1
                if s["label"] != "neutral":
                    false_removals_5b.append({
                        "claim": d["claim"][:30],
                        "title": d["title"][:40],
                        "label": s["label"],
                        "conf": max(s["p_supp"], s["p_opp"]),
                        "text": s["text"][:100],
                    })

    total_mw_sents = sum(len([s for s in d["sentences"] if s["word_count"] >= 10]) for d in scoreable)
    out.append(f"  Total sentences (mw>=10): {total_mw_sents}")
    out.append(f"  Removed by 5B: {total_removed_5b} ({100*total_removed_5b/max(total_mw_sents,1):.1f}%)")
    out.append(f"  Removed by label:")
    for label, count in removed_labels_5b.most_common():
        out.append(f"    {label:12s}: {count}")
    out.append("")

    if false_removals_5b:
        out.append(f"  *** FALSE REMOVALS (non-neutral removed by 5B): {len(false_removals_5b)} ***")
        for fr in false_removals_5b[:15]:
            out.append(f"    [{fr['label']:10s} {fr['conf']:.3f}] {fr['claim']} | {fr['text'][:80]}")
        if len(false_removals_5b) > 15:
            out.append(f"    ... and {len(false_removals_5b)-15} more")
    else:
        out.append(f"  No false removals (all removed sentences were neutral)")
    out.append("")

    # ============================================================
    # SECTION 2: WHAT DOES 5C REMOVE AT EACH THRESHOLD?
    # ============================================================
    out.append("=" * 80)
    out.append("SECTION 2: 5C RELEVANCE FILTER IMPACT")
    out.append("=" * 80)
    out.append("")

    for t in RELEVANCE_THRESHOLDS:
        removed = 0
        removed_labels = Counter()
        false_removals = []
        sources_emptied = 0

        for d in scoreable:
            mw_sents = [s for s in d["sentences"] if s["word_count"] >= 10]
            remaining = [s for s in mw_sents if s.get("relevance", 1.0) >= t]
            if mw_sents and not remaining:
                sources_emptied += 1
            for s in mw_sents:
                if s.get("relevance", 1.0) < t:
                    removed += 1
                    removed_labels[s["label"]] += 1
                    if s["label"] != "neutral":
                        false_removals.append({
                            "claim": d["claim"][:30],
                            "title": d["title"][:40],
                            "label": s["label"],
                            "conf": max(s["p_supp"], s["p_opp"]),
                            "relevance": s.get("relevance", 0),
                            "text": s["text"][:80],
                        })

        out.append(f"  Threshold > {t}:")
        out.append(f"    Removed: {removed}/{total_mw_sents} ({100*removed/max(total_mw_sents,1):.1f}%)")
        out.append(f"    Sources emptied (all sents removed): {sources_emptied}")
        out.append(f"    Removed by label: neutral={removed_labels.get('neutral',0)}  "
                   f"opposing={removed_labels.get('opposing',0)}  "
                   f"supporting={removed_labels.get('supporting',0)}")
        out.append(f"    *** FALSE REMOVALS: {len(false_removals)} non-neutral sentences ***")
        if false_removals:
            for fr in false_removals[:5]:
                out.append(f"      [{fr['label']:10s} {fr['conf']:.3f} rel={fr['relevance']:.3f}] "
                          f"{fr['claim']} | {fr['text'][:70]}")
            if len(false_removals) > 5:
                out.append(f"      ... and {len(false_removals)-5} more")
        out.append("")

    # ============================================================
    # SECTION 3: ACCURACY COMPARISON GRID
    # ============================================================
    out.append("=" * 80)
    out.append("SECTION 3: ACCURACY COMPARISON")
    out.append("=" * 80)
    out.append("")
    out.append(f"{'Filter':<20s} {'3K':>8s} {'3A':>8s} {'3J':>8s}")
    out.append("-" * 50)

    results = {}  # (filter_name, strategy_name) -> {correct, wrong, neutral, ...}

    for filter_name, filter_fn in filter_configs:
        row = {}
        for strat_name, strat_fn in STRATEGIES.items():
            correct = 0
            wrong = 0
            neutral = 0
            for d in scoreable:
                mw_sents = [s for s in d["sentences"] if s["word_count"] >= 10]
                filtered = [s for s in mw_sents if filter_fn(s, d)]

                if not filtered:
                    neutral += 1
                    continue

                pred, conf = strat_fn(filtered)
                if pred == d["expected_stance"]:
                    correct += 1
                elif pred == "neutral":
                    neutral += 1
                else:
                    wrong += 1

            key = (filter_name, strat_name)
            results[key] = {"correct": correct, "wrong": wrong, "neutral": neutral,
                           "total": len(scoreable), "acc": correct / max(len(scoreable), 1)}
            row[strat_name] = f"{correct}/{len(scoreable)} ({100*correct/max(len(scoreable),1):.1f}%)"

        out.append(f"  {filter_name:<20s} {row.get('3K',''):>18s} {row.get('3A',''):>18s} {row.get('3J',''):>18s}")

    out.append("")

    # ============================================================
    # SECTION 4: REGRESSION AND IMPROVEMENT TRACKING
    # ============================================================
    out.append("=" * 80)
    out.append("SECTION 4: REGRESSIONS AND IMPROVEMENTS vs BASELINE (no filter)")
    out.append("=" * 80)
    out.append("")

    for strat_name in STRATEGIES:
        out.append(f"  Strategy: {strat_name}")
        out.append(f"  {'Filter':<20s} {'Improvements':>13s} {'Regressions':>13s} {'Net':>6s}")
        out.append(f"  " + "-" * 55)

        # Baseline predictions for this strategy
        baseline_preds = {}
        for di, d in enumerate(scoreable):
            mw_sents = [s for s in d["sentences"] if s["word_count"] >= 10]
            if not mw_sents:
                baseline_preds[di] = "neutral"
            else:
                pred, _ = STRATEGIES[strat_name](mw_sents)
                baseline_preds[di] = pred

        for filter_name, filter_fn in filter_configs:
            if filter_name == "none":
                continue

            improvements = []
            regressions = []

            for di, d in enumerate(scoreable):
                mw_sents = [s for s in d["sentences"] if s["word_count"] >= 10]
                filtered = [s for s in mw_sents if filter_fn(s, d)]

                if not filtered:
                    filtered_pred = "neutral"
                else:
                    filtered_pred, _ = STRATEGIES[strat_name](filtered)

                base_correct = baseline_preds[di] == d["expected_stance"]
                filt_correct = filtered_pred == d["expected_stance"]

                if not base_correct and filt_correct:
                    improvements.append((d, baseline_preds[di], filtered_pred))
                elif base_correct and not filt_correct:
                    regressions.append((d, baseline_preds[di], filtered_pred))

            net = len(improvements) - len(regressions)
            out.append(f"  {filter_name:<20s} {len(improvements):>10d}    {len(regressions):>10d}  {net:>+5d}")

        out.append("")

    # ============================================================
    # SECTION 5: DETAILED REGRESSIONS FOR TOP FILTERS
    # ============================================================
    out.append("=" * 80)
    out.append("SECTION 5: DETAILED REGRESSIONS (what filter broke)")
    out.append("=" * 80)
    out.append("")

    # Show regressions for 5B and best 5C on 3K
    for filter_name, filter_fn in filter_configs:
        if filter_name not in ["5B_pattern", "5C_rel>0.3", "5B+5C_rel>0.3"]:
            continue

        strat_fn = STRATEGIES["3K"]
        regressions = []

        for di, d in enumerate(scoreable):
            mw_sents = [s for s in d["sentences"] if s["word_count"] >= 10]
            filtered = [s for s in mw_sents if filter_fn(s, d)]

            if not mw_sents:
                continue

            base_pred, _ = strat_fn(mw_sents)
            if not filtered:
                filt_pred = "neutral"
            else:
                filt_pred, _ = strat_fn(filtered)

            if base_pred == d["expected_stance"] and filt_pred != d["expected_stance"]:
                # Find what was removed
                removed = [s for s in mw_sents if not filter_fn(s, d)]
                removed_nonneutral = [s for s in removed if s["label"] != "neutral"]
                regressions.append({
                    "claim": d["claim"],
                    "title": d["title"][:50],
                    "expected": d["expected_stance"],
                    "base_pred": base_pred,
                    "filt_pred": filt_pred,
                    "removed_count": len(removed),
                    "removed_nonneutral": len(removed_nonneutral),
                    "removed_samples": [(s["label"], s["text"][:60], s.get("relevance", 0))
                                       for s in removed[:3]],
                })

        out.append(f"  {filter_name} + 3K: {len(regressions)} regressions")
        for r in regressions[:10]:
            out.append(f"    {r['claim'][:30]} | {r['title']}")
            out.append(f"      base={r['base_pred']} -> filtered={r['filt_pred']} (expected {r['expected']})")
            out.append(f"      removed {r['removed_count']} sents ({r['removed_nonneutral']} non-neutral)")
            for label, text, rel in r["removed_samples"]:
                out.append(f"        [{label:10s} rel={rel:.3f}] {text}")
        out.append("")

    # ============================================================
    # SECTION 6: RELEVANCE SCORE DISTRIBUTION
    # ============================================================
    out.append("=" * 80)
    out.append("SECTION 6: RELEVANCE SCORE DISTRIBUTION BY SENTENCE LABEL")
    out.append("=" * 80)
    out.append("")

    all_rels = {"supporting": [], "neutral": [], "opposing": []}
    for d in scoreable:
        for s in d["sentences"]:
            if s["word_count"] >= 10 and "relevance" in s:
                all_rels[s["label"]].append(s["relevance"])

    for label in ["supporting", "neutral", "opposing"]:
        scores = all_rels[label]
        if not scores:
            continue
        out.append(f"  {label:12s} (n={len(scores):4d}): "
                   f"mean={sum(scores)/len(scores):.3f}  "
                   f"median={sorted(scores)[len(scores)//2]:.3f}  "
                   f"min={min(scores):.3f}  "
                   f"max={max(scores):.3f}")

    out.append("")
    out.append("  If supporting/opposing sentences have HIGHER relevance than neutral,")
    out.append("  then 5C filtering can remove noise without removing signal.")
    out.append("  If they overlap heavily, 5C will cause false removals.")

    # Write report
    os.makedirs("tests", exist_ok=True)
    with open(REPORT_PATH, "w") as f:
        f.write("\n".join(out))

    print(f"\nReport written to {REPORT_PATH}")

    # Quick summary
    print("\nQuick summary:")
    for strat_name in ["3K", "3A", "3J"]:
        base = results[("none", strat_name)]["acc"]
        print(f"\n  {strat_name} baseline: {100*base:.1f}%")
        for fn, _ in filter_configs:
            if fn == "none":
                continue
            acc = results[(fn, strat_name)]["acc"]
            diff = acc - base
            if abs(diff) > 0.001:
                print(f"    {fn:<20s}: {100*acc:.1f}% ({100*diff:+.1f}pp)")


if __name__ == "__main__":
    main()