#!/usr/bin/env python3
"""
eval_finetuned.py -- score the LoRA fine-tuned (or untuned) DeBERTa-v3-large stance
model on the FROZEN held-out test set, matching TRAINING inference exactly:
  premise = sentence, hypothesis = claim, max_len 256,
  label order: index 0 = supporting, 1 = neutral, 2 = opposing.

Reuses the SAME frozen test file the original eval_baseline.py created
(finetune/test_split_labels_HELDOUT.json). The test seal is unchanged.

Run from repo ROOT with the falseclaim venv active.
Deps (install once):  pip install peft sentencepiece
On Mac, prefix with PYTORCH_ENABLE_MPS_FALLBACK=1 so any unsupported MPS op
falls back to CPU instead of erroring.

BEFORE (untuned large baseline -- the honest "before" for this model):
    PYTORCH_ENABLE_MPS_FALLBACK=1 python finetune/eval_finetuned.py \
        --out finetune/metrics_BEFORE_large.json

AFTER (one run per seed; report all three, lead with the mean):
    PYTORCH_ENABLE_MPS_FALLBACK=1 python finetune/eval_finetuned.py \
        --adapter-dir finetune/runs/large_len256/best_model    --out finetune/metrics_AFTER_s42.json
    PYTORCH_ENABLE_MPS_FALLBACK=1 python finetune/eval_finetuned.py \
        --adapter-dir finetune/runs/large_len256_s1/best_model --out finetune/metrics_AFTER_s1.json
    PYTORCH_ENABLE_MPS_FALLBACK=1 python finetune/eval_finetuned.py \
        --adapter-dir finetune/runs/large_len256_s2/best_model --out finetune/metrics_AFTER_s2.json
"""
import os, json, argparse
from collections import Counter
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix

REPO_ROOT    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEST_PATH    = os.path.join(REPO_ROOT, "finetune", "test_split_labels_HELDOUT.json")
BASE_DEFAULT = "MoritzLaurer/deberta-v3-large-mnli-fever-anli-ling-wanli"
LABELS       = ["supporting", "neutral", "opposing"]   # index == model logit position


def pick_device(override):
    if override:
        return override
    if torch.cuda.is_available():
        return "cuda"
    if getattr(torch.backends, "mps", None) and torch.backends.mps.is_available():
        return "mps"
    return "cpu"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-model", default=BASE_DEFAULT)
    ap.add_argument("--adapter-dir", default=None, help="LoRA adapter dir; OMIT for the untuned baseline")
    ap.add_argument("--max-len", type=int, default=256)   # MUST match training
    ap.add_argument("--batch-size", type=int, default=32)
    ap.add_argument("--device", default=None, help="cuda|mps|cpu (default: auto)")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    tag = "AFTER" if args.adapter_dir else "BEFORE"
    out_path = args.out or os.path.join(REPO_ROOT, "finetune", f"metrics_{tag}.json")

    assert os.path.exists(TEST_PATH), (
        f"missing frozen test file:\n  {TEST_PATH}\n"
        "Run the original eval_baseline.py once to create it (it freezes the split).")
    test = json.load(open(TEST_PATH, encoding="utf-8"))
    print(f"loaded {len(test)} frozen TEST sentences")

    device = pick_device(args.device)
    print(f"device: {device}  |  base: {args.base_model}  |  adapter: {args.adapter_dir}  |  max_len: {args.max_len}")

    tok = AutoTokenizer.from_pretrained(args.adapter_dir or args.base_model)
    model = AutoModelForSequenceClassification.from_pretrained(args.base_model)
    if args.adapter_dir:
        from peft import PeftModel
        # Load adapter ON TOP of the base. Do NOT merge: PeftModel.forward applies both the
        # LoRA deltas and the trained classifier head (modules_to_save) correctly.
        model = PeftModel.from_pretrained(model, args.adapter_dir)
    model.to(device).eval()

    y_true, y_pred, rows = [], [], []
    bs = args.batch_size
    for i in range(0, len(test), bs):
        chunk = test[i:i + bs]
        prem = [e["sentence"] for e in chunk]
        hyp  = [e["claim"] for e in chunk]
        enc = tok(prem, hyp, truncation=True, max_length=args.max_len,
                  padding=True, return_tensors="pt").to(device)
        with torch.no_grad():
            logits = model(**enc).logits
        probs = torch.softmax(logits.float(), dim=-1).cpu()
        preds = probs.argmax(dim=-1).tolist()
        for e, p, pr in zip(chunk, preds, probs.tolist()):
            y_true.append(e["label"])
            y_pred.append(LABELS[p])
            rows.append({"claim": e["claim"], "sentence": e["sentence"],
                         "gold": e["label"], "pred": LABELS[p],
                         "p_supp": pr[0], "p_neut": pr[1], "p_opp": pr[2]})
        print(f"  scored {min(i + bs, len(test))}/{len(test)}", end="\r")
    print()

    acc      = accuracy_score(y_true, y_pred)
    macro_f1 = f1_score(y_true, y_pred, labels=LABELS, average="macro", zero_division=0)
    report   = classification_report(y_true, y_pred, labels=LABELS, output_dict=True, zero_division=0)
    cm       = confusion_matrix(y_true, y_pred, labels=LABELS).tolist()
    floor    = Counter(y_true)["neutral"] / len(y_true)

    print(f"\n=== {tag} ===")
    print(f"accuracy {acc*100:6.2f}%   (all-neutral floor {floor*100:.2f}%)   macro-F1 {macro_f1:.4f}")
    print(f"{'class':<12}{'prec':>9}{'rec':>9}{'f1':>9}{'n':>8}")
    for c in LABELS:
        r = report[c]
        print(f"{c:<12}{r['precision']:>9.3f}{r['recall']:>9.3f}{r['f1-score']:>9.3f}{int(r['support']):>8}")
    print(f"confusion (rows gold, cols pred) order {LABELS}:")
    for c, row in zip(LABELS, cm):
        print(f"  gold={c:<12}{row}")

    out = {"tag": tag, "base_model": args.base_model, "adapter_dir": args.adapter_dir,
           "max_len": args.max_len, "n_test": len(y_true), "accuracy": acc, "macro_f1": macro_f1,
           "neutral_floor": floor, "per_class": {c: report[c] for c in LABELS},
           "confusion_matrix": {"labels": LABELS, "matrix": cm}}
    json.dump(out, open(out_path, "w"), indent=2)
    json.dump(rows, open(out_path.replace(".json", "_rows.json"), "w"), ensure_ascii=False)
    print(f"\nmetrics -> {out_path}")
    print(f"rows    -> {out_path.replace('.json', '_rows.json')}")


if __name__ == "__main__":
    main()