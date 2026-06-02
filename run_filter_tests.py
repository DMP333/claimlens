"""
Source Contamination Filter Testing Suite
Run this locally in your falseclaim venv.

Prerequisites:
    pip install sentence-transformers scikit-learn

Usage:
    python run_filter_tests.py

This tests multiple approaches to source contamination filtering:
- Decision 3: Which model (bi-encoder vs cross-encoder vs NLI-as-relevance)
- Decision 2: What input (title only, snippet only, title+snippet, full content)
- Decision 5: Source-type-specific analysis

Results include both quantitative metrics AND text samples for manual review.
"""

import json
import sys
import time
import numpy as np
from collections import Counter
from sklearn.metrics import roc_auc_score
from sklearn.metrics.pairwise import cosine_similarity


def load_data(path="labeled_sources.json"):
    with open(path) as f:
        return json.load(f)


# ============================================================
# SCORING FUNCTIONS
# ============================================================

def get_biencoder_scorer():
    """Current approach: MiniLM bi-encoder cosine similarity."""
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("all-MiniLM-L6-v2")

    def score(claim, text):
        if not text.strip():
            return 0.0
        emb_c = model.encode([claim])
        emb_t = model.encode([text])
        return float(cosine_similarity(emb_c, emb_t)[0][0])

    return score, "bi-encoder (MiniLM)"


def get_crossencoder_scorer():
    """Cross-encoder: processes claim+text together."""
    from sentence_transformers import CrossEncoder
    model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

    def score(claim, text):
        if not text.strip():
            return -10.0
        return float(model.predict([(claim, text)])[0])

    return score, "cross-encoder (ms-marco)"


def get_nli_relevance_scorer():
    """Use the NLI model to check topical relevance.

    Hypothesis: 'This text discusses whether [claim]'
    If entailment score is high, text is about the claim topic.
    """
    from transformers import pipeline
    nli = pipeline("text-classification",
                   model="MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli",
                   device=-1,  # CPU
                   top_k=None)

    def score(claim, text):
        if not text.strip():
            return 0.0
        # Truncate to avoid token limit
        text = text[:500]
        hypothesis = f"This text discusses whether {claim}"
        try:
            result = nli(f"{text}", candidate_labels=[hypothesis],
                        hypothesis_template="{}")
        except:
            # Fallback: use raw NLI
            try:
                result = nli({"text": text, "text_pair": hypothesis})
                # Find entailment score
                for item in result:
                    if item["label"] == "ENTAILMENT" or item["label"] == "entailment":
                        return item["score"]
                return 0.5
            except:
                return 0.5
        return 0.5  # fallback

    # Actually, let's use the NLI model more directly
    from transformers import AutoTokenizer, AutoModelForSequenceClassification
    import torch

    tokenizer = AutoTokenizer.from_pretrained("MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli")
    model = AutoModelForSequenceClassification.from_pretrained("MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli")
    model.eval()

    def score_nli(claim, text):
        if not text.strip():
            return 0.0
        text = text[:400]  # truncate for speed
        hypothesis = f"This text discusses whether {claim}"
        inputs = tokenizer(text, hypothesis, return_tensors="pt", truncation=True, max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)
        probs = torch.softmax(outputs.logits, dim=1)[0]
        # Model outputs: [entailment, neutral, contradiction]
        # For relevance: entailment = text IS about the topic
        return float(probs[0])  # entailment probability

    return score_nli, "NLI-as-relevance (DeBERTa)"


# ============================================================
# BATCH SCORING (much faster than one-by-one)
# ============================================================

def batch_score_biencoder(claims, texts):
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("all-MiniLM-L6-v2")
    claim_embs = model.encode(claims, show_progress_bar=True, batch_size=64)
    text_embs = model.encode(texts, show_progress_bar=True, batch_size=64)
    # Pairwise cosine similarity (not all-vs-all, just matching pairs)
    scores = []
    for i in range(len(claims)):
        sim = cosine_similarity([claim_embs[i]], [text_embs[i]])[0][0]
        scores.append(float(sim))
    return scores


def batch_score_crossencoder(claims, texts):
    from sentence_transformers import CrossEncoder
    model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
    pairs = list(zip(claims, texts))
    scores = model.predict(pairs, show_progress_bar=True, batch_size=32)
    return [float(s) for s in scores]


def batch_score_nli_relevance(claims, texts):
    from transformers import AutoTokenizer, AutoModelForSequenceClassification
    import torch

    tokenizer = AutoTokenizer.from_pretrained("MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli")
    model = AutoModelForSequenceClassification.from_pretrained("MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli")
    model.eval()

    scores = []
    batch_size = 16
    for i in range(0, len(claims), batch_size):
        batch_texts = texts[i:i+batch_size]
        batch_claims = claims[i:i+batch_size]
        hypotheses = [f"This text discusses whether {c}" for c in batch_claims]

        inputs = tokenizer(
            batch_texts, hypotheses,
            return_tensors="pt", truncation=True,
            max_length=512, padding=True
        )
        with torch.no_grad():
            outputs = model(**inputs)
        probs = torch.softmax(outputs.logits, dim=1)
        # entailment is index 0 for this model
        batch_scores = probs[:, 0].tolist()
        scores.extend(batch_scores)

        if (i + batch_size) % 100 == 0:
            print(f"  {i+batch_size}/{len(claims)}...")

    return scores


# ============================================================
# EVALUATION (from test_harness.py, inlined for standalone use)
# ============================================================

def evaluate(scores, data, input_field, approach_name, show_samples=5):
    labels = [d["is_contaminated"] for d in data]
    contam_scores = [s for s, l in zip(scores, labels) if l]
    clean_scores = [s for s, l in zip(scores, labels) if not l]

    print(f"\n{'='*80}")
    print(f"EVALUATION: {approach_name} (input: {input_field})")
    print(f"{'='*80}")

    print(f"\nScore Distribution:")
    print(f"  Contaminated ({len(contam_scores)}): mean={np.mean(contam_scores):.4f}, median={np.median(contam_scores):.4f}")
    print(f"  Clean ({len(clean_scores)}):         mean={np.mean(clean_scores):.4f}, median={np.median(clean_scores):.4f}")

    roc_labels = [0 if l else 1 for l in labels]
    try:
        auc = roc_auc_score(roc_labels, scores)
    except:
        auc = 0.5
    print(f"  ROC AUC: {auc:.4f} (1.0=perfect, 0.5=random)")

    # Find best threshold
    all_scores_sorted = sorted(set(scores))
    step = max(1, len(all_scores_sorted) // 50)
    thresholds = [all_scores_sorted[i] for i in range(0, len(all_scores_sorted), step)]

    best_f1 = 0
    best_thresh = 0
    best_stats = {}

    for thresh in thresholds:
        tp = sum(1 for s, l in zip(scores, labels) if s < thresh and l)
        fp = sum(1 for s, l in zip(scores, labels) if s < thresh and not l)
        fn = sum(1 for s, l in zip(scores, labels) if s >= thresh and l)

        prec = tp / (tp + fp) if (tp + fp) > 0 else 0
        rec = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0

        if f1 > best_f1:
            best_f1 = f1
            best_thresh = thresh
            best_stats = {"tp": tp, "fp": fp, "fn": fn, "prec": prec, "rec": rec}

    print(f"\n  Best F1: {best_f1:.3f} at threshold {best_thresh:.4f}")
    print(f"  Precision: {best_stats.get('prec', 0):.3f}, Recall: {best_stats.get('rec', 0):.3f}")
    print(f"  Catches {best_stats.get('tp', 0)}/{len(contam_scores)} contaminated, loses {best_stats.get('fp', 0)}/{len(clean_scores)} clean")

    # Breakdown by source type
    print(f"\n  By Source Type:")
    for stype in ["encyclopedia", "academic", "web", "knowledge_graph"]:
        st_contam = [(s, d) for s, d in zip(scores, data) if d["source_type"] == stype and d["is_contaminated"]]
        st_clean = [(s, d) for s, d in zip(scores, data) if d["source_type"] == stype and not d["is_contaminated"]]
        caught = sum(1 for s, d in st_contam if s < best_thresh)
        lost = sum(1 for s, d in st_clean if s < best_thresh)
        print(f"    {stype:15s}: catches {caught}/{len(st_contam)} contam, loses {lost}/{len(st_clean)} clean")

    # Text samples
    tp_items = [(s, d) for s, d in zip(scores, data) if s < best_thresh and d["is_contaminated"]]
    fp_items = [(s, d) for s, d in zip(scores, data) if s < best_thresh and not d["is_contaminated"]]
    fn_items = [(s, d) for s, d in zip(scores, data) if s >= best_thresh and d["is_contaminated"]]

    def show(name, items, n):
        print(f"\n  {name} ({len(items)} total, showing {min(n, len(items))}):")
        items_sorted = sorted(items, key=lambda x: abs(x[0] - best_thresh))
        for score, d in items_sorted[:n]:
            print(f"    Score={score:.4f} [{d['source_type']}] \"{d['claim'][:35]}\" -> \"{d['source_title'][:55]}\"")

    show("TRUE POSITIVES (caught contamination)", tp_items, show_samples)
    show("FALSE POSITIVES (wrongly filtered clean)", fp_items, show_samples)
    show("FALSE NEGATIVES (missed contamination)", fn_items, show_samples)

    return {"approach": approach_name, "input": input_field, "auc": auc, "f1": best_f1, "thresh": best_thresh}


# ============================================================
# MAIN: Run all tests
# ============================================================

def main():
    data = load_data()
    print(f"Loaded {len(data)} sources ({sum(1 for d in data if d['is_contaminated'])} contaminated)")

    input_fields = ["title_only", "snippet_only", "title_plus_snippet"]
    all_results = []

    # ---- BI-ENCODER ----
    print("\n" + "#"*80)
    print("MODEL 1: Bi-encoder (current approach)")
    print("#"*80)

    for field in input_fields:
        claims = [d["claim"] for d in data]
        texts = [d.get(field, "") or "" for d in data]

        print(f"\nScoring with bi-encoder on {field}...")
        t0 = time.time()
        scores = batch_score_biencoder(claims, texts)
        print(f"  Done in {time.time()-t0:.1f}s")

        result = evaluate(scores, data, field, f"bi-encoder / {field}")
        all_results.append(result)

    # ---- CROSS-ENCODER ----
    print("\n" + "#"*80)
    print("MODEL 2: Cross-encoder")
    print("#"*80)

    for field in input_fields:
        claims = [d["claim"] for d in data]
        texts = [d.get(field, "") or "" for d in data]

        # Replace empty strings with a placeholder
        texts = [t if t.strip() else "no content available" for t in texts]

        print(f"\nScoring with cross-encoder on {field}...")
        t0 = time.time()
        scores = batch_score_crossencoder(claims, texts)
        print(f"  Done in {time.time()-t0:.1f}s")

        result = evaluate(scores, data, field, f"cross-encoder / {field}")
        all_results.append(result)

    # ---- NLI AS RELEVANCE ----
    print("\n" + "#"*80)
    print("MODEL 3: NLI-as-relevance (DeBERTa)")
    print("#"*80)

    for field in input_fields:
        claims = [d["claim"] for d in data]
        texts = [d.get(field, "") or "" for d in data]
        texts = [t[:400] if t.strip() else "no content available" for t in texts]

        print(f"\nScoring with NLI-as-relevance on {field}...")
        t0 = time.time()
        scores = batch_score_nli_relevance(claims, texts)
        print(f"  Done in {time.time()-t0:.1f}s")

        result = evaluate(scores, data, field, f"NLI-relevance / {field}")
        all_results.append(result)

    # ---- COMPARISON ----
    print("\n" + "="*80)
    print("FINAL COMPARISON")
    print("="*80)
    print(f"\n  {'Approach':45s} | {'AUC':>6s} | {'F1':>6s} | {'Threshold':>9s}")
    print(f"  {'-'*45}-+-{'-'*6}-+-{'-'*6}-+-{'-'*9}")
    for r in sorted(all_results, key=lambda x: -x["auc"]):
        print(f"  {r['approach']:45s} | {r['auc']:>6.4f} | {r['f1']:>6.3f} | {r['thresh']:>9.4f}")

    # Save results
    with open("filter_test_results.json", "w") as f:
        json.dump(all_results, f, indent=2)
    print("\nResults saved to filter_test_results.json")


if __name__ == "__main__":
    main()