"""
Contamination Filter Test Harness

Usage:
    1. Load labeled_sources.json (1,178 sources with contamination labels)
    2. For each approach you want to test, provide a scoring function:
       score_fn(claim: str, text: str) -> float  (higher = more relevant)
    3. Call evaluate(scores, labeled_data) to get metrics + samples

The harness is model-agnostic. It evaluates ANY scoring function
against the same labeled data, ensuring objective comparison.

Output:
    - Quantitative: precision, recall, F1 at various thresholds
    - Qualitative: sample texts for each quadrant (TP, FP, TN, FN)
    - Breakdown: by source type and contamination mechanism
"""

import json
import numpy as np
from collections import Counter


def load_labeled_data(path="labeled_sources.json"):
    with open(path) as f:
        return json.load(f)


def evaluate(
    scores: list[float],
    data: list[dict],
    input_field: str = "title_plus_snippet",
    approach_name: str = "unnamed",
    show_samples: int = 5,
    thresholds: list[float] | None = None,
):
    """
    Evaluate a set of relevance scores against labeled contamination data.
    
    Args:
        scores: relevance score for each source (higher = more relevant)
        data: labeled source data
        input_field: which text field was scored (for display)
        approach_name: name for this approach (for display)
        show_samples: how many text samples to show per quadrant
        thresholds: specific thresholds to test. If None, auto-generates.
    
    Returns:
        dict with full evaluation results
    """
    assert len(scores) == len(data), f"Score count {len(scores)} != data count {len(data)}"
    
    labels = [d["is_contaminated"] for d in data]
    
    # Separate contaminated vs clean scores
    contam_scores = [s for s, l in zip(scores, labels) if l]
    clean_scores = [s for s, l in zip(scores, labels) if not l]
    
    print(f"\n{'='*80}")
    print(f"EVALUATION: {approach_name}")
    print(f"Input: {input_field}")
    print(f"{'='*80}")
    
    # Score distribution
    print(f"\nScore Distribution:")
    print(f"  Contaminated ({len(contam_scores)}): mean={np.mean(contam_scores):.4f}, median={np.median(contam_scores):.4f}, min={np.min(contam_scores):.4f}, max={np.max(contam_scores):.4f}")
    print(f"  Clean ({len(clean_scores)}):         mean={np.mean(clean_scores):.4f}, median={np.median(clean_scores):.4f}, min={np.min(clean_scores):.4f}, max={np.max(clean_scores):.4f}")
    
    # Separation quality (how well scores separate the two groups)
    # Use area under ROC as a single metric
    from sklearn.metrics import roc_auc_score
    # For ROC, positive class = clean (we want to KEEP clean, FILTER contaminated)
    # Higher score should mean "more relevant" = "keep"
    # So clean should have higher scores, contaminated lower
    roc_labels = [0 if l else 1 for l in labels]  # 1 = clean (positive), 0 = contaminated
    try:
        auc = roc_auc_score(roc_labels, scores)
    except:
        auc = 0.5
    print(f"\n  ROC AUC (separation quality): {auc:.4f}")
    print(f"  (1.0 = perfect separation, 0.5 = random, <0.5 = inverted)")
    
    # Threshold analysis
    if thresholds is None:
        all_scores = sorted(set(scores))
        # Test ~20 thresholds spanning the score range
        if len(all_scores) > 20:
            step = len(all_scores) // 20
            thresholds = [all_scores[i] for i in range(0, len(all_scores), step)]
        else:
            thresholds = all_scores
    
    print(f"\nThreshold Analysis (sources with score < threshold get FILTERED):")
    print(f"  {'Threshold':>10s} | {'Filtered':>8s} | {'Contam Caught':>13s} | {'Clean Lost':>10s} | {'Precision':>9s} | {'Recall':>6s} | {'F1':>6s}")
    print(f"  {'-'*10}-+-{'-'*8}-+-{'-'*13}-+-{'-'*10}-+-{'-'*9}-+-{'-'*6}-+-{'-'*6}")
    
    best_f1 = 0
    best_threshold = 0
    
    for thresh in thresholds:
        # Sources below threshold get filtered (predicted contaminated)
        pred_contam = sum(1 for s in scores if s < thresh)
        true_pos = sum(1 for s, l in zip(scores, labels) if s < thresh and l)  # correctly caught contamination
        false_pos = sum(1 for s, l in zip(scores, labels) if s < thresh and not l)  # wrongly filtered clean
        false_neg = sum(1 for s, l in zip(scores, labels) if s >= thresh and l)  # missed contamination
        
        precision = true_pos / pred_contam if pred_contam > 0 else 0
        recall = true_pos / len(contam_scores) if len(contam_scores) > 0 else 0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
        
        if f1 > best_f1:
            best_f1 = f1
            best_threshold = thresh
        
        # Only print interesting thresholds
        if pred_contam > 0 and pred_contam < len(scores) * 0.5:
            print(f"  {thresh:>10.4f} | {pred_contam:>8d} | {true_pos:>6d}/{len(contam_scores):<6d} | {false_pos:>10d} | {precision:>9.3f} | {recall:>6.3f} | {f1:>6.3f}")
    
    print(f"\n  Best F1: {best_f1:.3f} at threshold {best_threshold:.4f}")
    
    # Breakdown by source type at best threshold
    print(f"\nBreakdown by Source Type (at best threshold {best_threshold:.4f}):")
    for stype in ["fact_check", "encyclopedia", "academic", "web", "knowledge_graph"]:
        type_data = [(s, d) for s, d in zip(scores, data) if d["source_type"] == stype]
        if not type_data:
            continue
        type_contam = [(s, d) for s, d in type_data if d["is_contaminated"]]
        type_clean = [(s, d) for s, d in type_data if not d["is_contaminated"]]
        caught = sum(1 for s, d in type_contam if s < best_threshold)
        lost = sum(1 for s, d in type_clean if s < best_threshold)
        print(f"  {stype:15s}: caught {caught}/{len(type_contam)} contaminated, lost {lost}/{len(type_clean)} clean")
    
    # QUALITATIVE SAMPLES at best threshold
    print(f"\n{'='*80}")
    print(f"TEXT SAMPLES (at threshold {best_threshold:.4f})")
    print(f"{'='*80}")
    
    # Build quadrants
    tp = [(s, d) for s, d in zip(scores, data) if s < best_threshold and d["is_contaminated"]]
    fp = [(s, d) for s, d in zip(scores, data) if s < best_threshold and not d["is_contaminated"]]
    fn = [(s, d) for s, d in zip(scores, data) if s >= best_threshold and d["is_contaminated"]]
    tn = [(s, d) for s, d in zip(scores, data) if s >= best_threshold and not d["is_contaminated"]]
    
    def show_quadrant(name, items, n):
        print(f"\n--- {name} ({len(items)} total, showing {min(n, len(items))}) ---")
        # Sort by score to show most interesting cases (closest to threshold)
        items_sorted = sorted(items, key=lambda x: abs(x[0] - best_threshold))
        for score, d in items_sorted[:n]:
            print(f"  Score: {score:.4f} | [{d['source_type']}] Claim: \"{d['claim'][:40]}\"")
            print(f"    Source: \"{d['source_title'][:70]}\"")
            text = d.get(input_field, "")[:150]
            print(f"    Text: \"{text}\"")
    
    show_quadrant("TRUE POSITIVES (correctly caught contamination)", tp, show_samples)
    show_quadrant("FALSE POSITIVES (wrongly filtered clean sources)", fp, show_samples)
    show_quadrant("FALSE NEGATIVES (missed contamination)", fn, show_samples)
    show_quadrant("TRUE NEGATIVES (correctly kept, closest to threshold)", tn, show_samples)
    
    return {
        "approach": approach_name,
        "input_field": input_field,
        "auc": auc,
        "best_f1": best_f1,
        "best_threshold": best_threshold,
        "total_contaminated": len(contam_scores),
        "total_clean": len(clean_scores),
        "contam_mean_score": float(np.mean(contam_scores)),
        "clean_mean_score": float(np.mean(clean_scores)),
    }


def compare_approaches(results: list[dict]):
    """Compare multiple approach results side by side."""
    print(f"\n{'='*80}")
    print(f"COMPARISON SUMMARY")
    print(f"{'='*80}")
    print(f"  {'Approach':40s} | {'Input':20s} | {'AUC':>6s} | {'Best F1':>7s} | {'Threshold':>9s} | {'Contam Mean':>11s} | {'Clean Mean':>10s}")
    print(f"  {'-'*40}-+-{'-'*20}-+-{'-'*6}-+-{'-'*7}-+-{'-'*9}-+-{'-'*11}-+-{'-'*10}")
    for r in sorted(results, key=lambda x: -x["auc"]):
        print(f"  {r['approach']:40s} | {r['input_field']:20s} | {r['auc']:>6.4f} | {r['best_f1']:>7.3f} | {r['best_threshold']:>9.4f} | {r['contam_mean_score']:>11.4f} | {r['clean_mean_score']:>10.4f}")


if __name__ == "__main__":
    # Quick test with current bi-encoder scores
    print("Test harness loaded. Use:")
    print("  data = load_labeled_data()")
    print("  results = evaluate(scores, data, 'title_plus_snippet', 'My Approach')")
    print("  compare_approaches([result1, result2, ...])")
