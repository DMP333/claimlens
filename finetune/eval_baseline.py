#!/usr/bin/env python3
"""
eval_baseline.py  --  Project A fine-tune: Step A (split + freeze) + Step C (BEFORE baseline).

Run from your repo ROOT:  python finetune/eval_baseline.py
(falseclaim venv active, on the M2 Max.)

WHAT IT DOES, in order:
  1. Loads claim_roster.json (100 train / 50 test) and finetune/sentence_labels_llm.json.
  2. Splits the silver labels by the roster's `split` field.
  3. Leakage fix (T1b): drops any TRAIN row whose sentence text also appears in TEST.
     TEST is NEVER modified. The held-out 50 claims stay frozen and complete.
  4. Verifies and HARD-ABORTS if any contamination guard fails:
        - unmatched labels (claim not in roster)  must be 0
        - claims appearing in both splits          must be 0
        - shared premise sentences after the fix   must be 0
  5. Writes the FROZEN split files (train_split_labels.json, test_split_labels_HELDOUT.json).
     Training later reads ONLY train; eval reads ONLY test. Two files on disk = no cross-contamination.
  6. Runs the CURRENT DeBERTa over every TEST sentence, one NLI call per (sentence, claim) pair,
     reusing nli_service._run_nli_batch and its LABEL_MAP -> identical to the live pipeline.
  7. Compares predictions to silver labels and writes metrics_BEFORE_baseline.json:
        overall accuracy, per-class precision/recall/F1, macro-F1, confusion matrix,
        plus a per-sentence dump for later error analysis and the paired before/after comparison.

AFTER fine-tuning, re-run this EXACT script with --model-dir pointing at the fine-tuned weights:
        python finetune/eval_baseline.py --model-dir finetune/model_v1
It swaps ONLY nli_service.model (same harness, same code path) and writes metrics_AFTER_finetune.json.
The before/after delta is the resume number.
"""
import os
import sys
import json
import argparse
from collections import Counter, defaultdict

# ---------------- CONFIG: edit ONLY if your layout differs ----------------
REPO_ROOT    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # finetune/ -> repo root
SERVICES_DIR = os.path.join(REPO_ROOT, "app", "services")
ROSTER_PATH  = os.path.join(REPO_ROOT, "claim_roster.json")
LABELS_PATH  = os.path.join(REPO_ROOT, "finetune", "sentence_labels_llm.json")
OUT_DIR      = os.path.join(REPO_ROOT, "finetune")
TRAIN_OUT    = os.path.join(OUT_DIR, "train_split_labels.json")
TEST_OUT     = os.path.join(OUT_DIR, "test_split_labels_HELDOUT.json")
DROPPED_OUT  = os.path.join(OUT_DIR, "_dropped_leakage_rows.json")
# --------------------------------------------------------------------------

# Must match nli_service.LABEL_MAP order: 0=supporting, 1=neutral, 2=opposing
LABELS   = ["supporting", "neutral", "opposing"]
LABEL2ID = {"supporting": 0, "neutral": 1, "opposing": 2}


def partition_and_freeze():
    roster = json.load(open(ROSTER_PATH, encoding="utf-8"))
    split_of = {r["claim"]: r["split"] for r in roster}
    labels = json.load(open(LABELS_PATH, encoding="utf-8"))

    train, test, unmatched = {}, {}, []
    for key, lab in labels.items():
        claim, _sent = key.split("||", 1)
        sp = split_of.get(claim)
        if sp is None:
            unmatched.append(key)
            continue
        (train if sp == "train" else test)[key] = lab

    # T1b leakage fix: remove TRAIN rows whose sentence also appears in TEST. TEST untouched.
    test_sents = set(k.split("||", 1)[1] for k in test)
    drop = {k for k in train if k.split("||", 1)[1] in test_sents}
    train_clean = {k: v for k, v in train.items() if k not in drop}

    train_claims = set(k.split("||", 1)[0] for k in train_clean)
    test_claims  = set(k.split("||", 1)[0] for k in test)
    shared_after = set(k.split("||", 1)[1] for k in train_clean) & test_sents

    print("=" * 64)
    print("STEP A : SPLIT + FREEZE + LEAKAGE VERIFICATION")
    print("=" * 64)
    print(f"train rows (raw)            : {len(train)}")
    print(f"train rows (leakage-fixed)  : {len(train_clean)}")
    print(f"test  rows (HELD OUT)       : {len(test)}")
    print(f"unmatched labels            : {len(unmatched)}   <-- must be 0")
    print(f"[T1a] claims in BOTH splits : {len(train_claims & test_claims)}   <-- must be 0")
    print(f"[T1b] train rows dropped    : {len(drop)}")
    print(f"[T1b] shared premise AFTER  : {len(shared_after)}   <-- must be 0")
    print(f"train label dist            : {dict(Counter(train_clean.values()))}")
    print(f"test  label dist            : {dict(Counter(test.values()))}")

    # HARD ABORTS: refuse to proceed on any contamination.
    assert len(unmatched) == 0, "ABORT: labels map to a claim not in the roster."
    assert len(train_claims & test_claims) == 0, "ABORT: a claim appears in both splits."
    assert len(shared_after) == 0, "ABORT: premise leakage remains in train after fix."

    def to_examples(d):
        out = []
        for k, v in d.items():
            c, s = k.split("||", 1)
            out.append({"claim": c, "sentence": s, "label": v, "label_id": LABEL2ID[v]})
        return out

    json.dump(to_examples(train_clean), open(TRAIN_OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    json.dump(to_examples(test),        open(TEST_OUT,  "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    json.dump(to_examples({k: train[k] for k in drop}),
              open(DROPPED_OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print(f"\nFROZEN -> {TRAIN_OUT}")
    print(f"FROZEN -> {TEST_OUT}")
    print("Train file and test file are now separate on disk. Nothing reads both.\n")
    return to_examples(test)


def load_model(nli_service, model_dir):
    """Swap ONLY the weights so before/after share the exact same inference code path."""
    if model_dir:
        from transformers import AutoModelForSequenceClassification, AutoTokenizer
        print(f"Loading FINE-TUNED model from: {model_dir}")
        nli_service.model = AutoModelForSequenceClassification.from_pretrained(model_dir)
        nli_service.model.eval()
        try:
            nli_service.tokenizer = AutoTokenizer.from_pretrained(model_dir)
        except Exception:
            print("  (no tokenizer in model dir; keeping base tokenizer)")
    else:
        print("Using BASE (un-fine-tuned) model from nli_service.")


def run_eval(test_examples, nli_service):
    """One NLI call per (sentence, claim). Group by claim because _run_nli_batch takes a single hypothesis."""
    by_claim = defaultdict(list)
    for ex in test_examples:
        by_claim[ex["claim"]].append(ex)

    y_true, y_pred, rows = [], [], []
    n = len(by_claim)
    for ci, (claim, exs) in enumerate(by_claim.items(), 1):
        premises = [e["sentence"] for e in exs]
        results = nli_service._run_nli_batch(premises, claim)   # SAME harness as live pipeline
        for e, r in zip(exs, results):
            y_true.append(e["label"])
            y_pred.append(r["label"])
            rows.append({
                "claim": claim, "sentence": e["sentence"],
                "gold": e["label"], "pred": r["label"],
                "p_supp": r["p_supp"], "p_neut": r["p_neut"], "p_opp": r["p_opp"],
            })
        print(f"  [{ci:>3}/{n}] {claim[:48]:48s} ({len(exs)} sents)   ", end="\r")
    print()
    return y_true, y_pred, rows


def compute_metrics(y_true, y_pred):
    from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score
    acc      = accuracy_score(y_true, y_pred)
    macro_f1 = f1_score(y_true, y_pred, labels=LABELS, average="macro", zero_division=0)
    report   = classification_report(y_true, y_pred, labels=LABELS, output_dict=True, zero_division=0)
    cm       = confusion_matrix(y_true, y_pred, labels=LABELS).tolist()
    return acc, macro_f1, report, cm


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model-dir", default=os.environ.get("FT_MODEL_DIR"),
                    help="Fine-tuned model dir. OMIT for the BASE baseline run.")
    ap.add_argument("--out", default=None, help="metrics output json path")
    args = ap.parse_args()

    tag = "AFTER_finetune" if args.model_dir else "BEFORE_baseline"
    out_path = args.out or os.path.join(OUT_DIR, f"metrics_{tag}.json")

    # Split + freeze FIRST (does not need the model). Aborts on any contamination.
    test_examples = partition_and_freeze()

    # Import the live pipeline (loads DeBERTa once), then optionally swap weights.
    sys.path.insert(0, SERVICES_DIR)
    import nli_service
    load_model(nli_service, args.model_dir)

    print("=" * 64)
    print(f"STEP C : SCORING {tag} on {len(test_examples)} held-out TEST sentences")
    print("=" * 64)
    y_true, y_pred, rows = run_eval(test_examples, nli_service)
    acc, macro_f1, report, cm = compute_metrics(y_true, y_pred)

    floor = Counter(y_true)["neutral"] / len(y_true)
    print(f"\nOVERALL ACCURACY : {acc*100:6.2f}%    (predict-all-neutral floor = {floor*100:.2f}%)")
    print(f"MACRO-F1         : {macro_f1:6.4f}")
    print(f"\n{'class':<12}{'precision':>11}{'recall':>11}{'f1':>11}{'support':>11}")
    for c in LABELS:
        r = report[c]
        print(f"{c:<12}{r['precision']:>11.3f}{r['recall']:>11.3f}{r['f1-score']:>11.3f}{int(r['support']):>11}")
    print(f"\nConfusion matrix  (rows = gold, cols = pred), order {LABELS}:")
    for c, row in zip(LABELS, cm):
        print(f"  gold={c:<12} {row}")

    out = {
        "tag": tag,
        "model_dir": args.model_dir,
        "n_test": len(y_true),
        "accuracy": acc,
        "macro_f1": macro_f1,
        "neutral_floor": floor,
        "per_class": {c: report[c] for c in LABELS},
        "confusion_matrix": {"labels": LABELS, "matrix": cm},
    }
    json.dump(out, open(out_path, "w", encoding="utf-8"), indent=2)
    rows_path = out_path.replace(".json", "_rows.json")
    json.dump(rows, open(rows_path, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print(f"\nFROZEN METRICS -> {out_path}")
    print(f"PER-SENTENCE   -> {rows_path}")
    print("\nDone. Send me metrics_BEFORE_baseline.json and we read the baseline together.")


if __name__ == "__main__":
    main()