#!/usr/bin/env python3
"""
train.py  --  Project A fine-tune: trains ONE configuration of the DeBERTa stance model.

Run ONE config (validate the harness first), e.g.:
    python train.py --run-name lr2e5_effnum --lr 2e-5 --loss weighted --class-weights effnum \
        --batch-size 32 --epochs 5 --output-dir /workspace/runs/lr2e5_effnum

The sweep = calling this repeatedly with different flags; every run appends a row per epoch to
runs_log.csv so the whole sweep is auditable. Selection is on DEV macro-F1. The 50-claim TEST set
is never read here; it is scored once at the end via eval_baseline.py --model-dir <best run dir>.

What it does:
  1. Reads train_split_labels.json (test-leakage-fixed train rows) and dev_split.json.
  2. Splits into 80 inner-train claims / 20 dev claims; drops inner-train rows whose sentence also
     appears in dev (premise-leakage guard). Dev is never touched.
  3. Optional data balancing (none / undersample-neutral / oversample-stance) on inner-train only.
  4. Tokenizes (premise=sentence, hypothesis=claim), max_length 128.
  5. Trains with the chosen loss (plain CE / class-weighted CE / focal), full fine-tune or LoRA.
  6. Evaluates on dev each epoch: macro-F1, accuracy, per-class recall, confusion matrix -> CSV.
  7. Early-stops on dev macro-F1, keeps the best checkpoint, saves the best model for the test run.
"""
import os, sys, json, csv, argparse, random, inspect
from collections import defaultdict, Counter
import numpy as np
import torch
import torch.nn.functional as F
from transformers import (AutoTokenizer, AutoModelForSequenceClassification,
                          TrainingArguments, Trainer, TrainerCallback, set_seed,
                          DataCollatorWithPadding)
from transformers.trainer_utils import get_last_checkpoint
from datasets import Dataset
from sklearn.metrics import f1_score, accuracy_score, recall_score, confusion_matrix

MODEL_NAME = os.environ.get("BASE_MODEL", "MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli")
LABEL2ID = {"supporting": 0, "neutral": 1, "opposing": 2}
LABELS_ORDER = [0, 1, 2]
MAX_LEN = int(os.environ.get("MAX_LEN", "128"))
_LAST_CM = {}   # compute_metrics stashes the latest dev confusion matrix here


def load_rows(repo_root):
    train = json.load(open(os.path.join(repo_root, "finetune", "train_split_labels.json"), encoding="utf-8"))
    devs  = json.load(open(os.path.join(repo_root, "finetune", "dev_split.json"), encoding="utf-8"))
    dev_claims   = set(devs["dev_claims"])
    inner_claims = set(devs["inner_train_claims"])
    inner = [r for r in train if r["claim"] in inner_claims]
    dev   = [r for r in train if r["claim"] in dev_claims]
    # premise-leakage guard: drop inner-train rows whose sentence also appears in dev
    dev_sents = set(r["sentence"] for r in dev)
    before = len(inner)
    inner = [r for r in inner if r["sentence"] not in dev_sents]
    print(f"inner-train {len(inner)} (dropped {before-len(inner)} dev-overlap) | dev {len(dev)}")
    leaked = set(r["claim"] for r in inner) & dev_claims
    assert not leaked, f"ABORT: dev claim leaked into inner-train: {leaked}"
    return inner, dev


def balance(rows, method, seed):
    if method == "none":
        return rows
    rnd = random.Random(seed)
    byc = defaultdict(list)
    for r in rows:
        byc[r["label_id"]].append(r)
    if method == "under":   # cut neutral down to 2x the larger stance class
        target = 2 * max(len(byc[0]), len(byc[2]))
        if len(byc[1]) > target:
            byc[1] = rnd.sample(byc[1], target)
    elif method == "over":  # duplicate stance up to the neutral count
        target = len(byc[1])
        for c in (0, 2):
            base = byc[c]
            if not base:
                continue
            full = base * (target // len(base)) + rnd.sample(base, target % len(base))
            byc[c] = full[:target]
    out = [r for c in byc for r in byc[c]]
    rnd.shuffle(out)
    print(f"balanced[{method}] -> {dict(Counter(r['label_id'] for r in out))}")
    return out


def class_weights(scheme, rows):
    n = Counter(r["label_id"] for r in rows)
    counts = np.array([n[0], n[1], n[2]], dtype=float)
    if scheme == "none":
        w = np.ones(3)
    elif scheme == "effnum":          # effective number of samples (Cui et al.), beta=0.999
        beta = 0.999
        eff = (1 - np.power(beta, counts)) / (1 - beta)
        w = 1.0 / eff
    elif scheme == "sqrt":            # milder inverse-frequency
        w = np.sqrt(counts.sum() / counts)
    else:                             # explicit "a,b,c"
        w = np.array([float(x) for x in scheme.split(",")], dtype=float)
    w = w / w.mean()                  # normalize to mean 1 so the LR stays comparable
    print(f"class weights [{scheme}] = supp {w[0]:.2f} neut {w[1]:.2f} opp {w[2]:.2f}")
    return torch.tensor(w, dtype=torch.float)


class LossTrainer(Trainer):
    def __init__(self, *a, loss_type="weighted", weights=None, focal_gamma=2.0, **kw):
        super().__init__(*a, **kw)
        self.loss_type = loss_type
        self.focal_gamma = focal_gamma
        self.register_buffer_weights = weights

    def compute_loss(self, model, inputs, return_outputs=False, **kw):
        labels = inputs.pop("labels")
        outputs = model(**inputs)
        logits = outputs.logits.float()   # compute loss in fp32 (dtype-safe + stable)
        w = self.register_buffer_weights
        if w is not None:
            w = w.to(device=logits.device, dtype=logits.dtype)
        if self.loss_type == "focal":
            ce = F.cross_entropy(logits, labels, weight=w, reduction="none")
            pt = torch.exp(-ce)
            loss = ((1 - pt) ** self.focal_gamma * ce).mean()
        elif self.loss_type == "weighted":
            loss = F.cross_entropy(logits, labels, weight=w)
        else:  # plain CE
            loss = F.cross_entropy(logits, labels)
        return (loss, outputs) if return_outputs else loss


def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=-1)
    rec = recall_score(labels, preds, average=None, labels=LABELS_ORDER, zero_division=0)
    _LAST_CM["cm"] = confusion_matrix(labels, preds, labels=LABELS_ORDER).tolist()
    return {
        "macro_f1": f1_score(labels, preds, average="macro", labels=LABELS_ORDER, zero_division=0),
        "accuracy": accuracy_score(labels, preds),
        "recall_supporting": rec[0], "recall_neutral": rec[1], "recall_opposing": rec[2],
    }


class NaNStopper(TrainerCallback):
    def on_log(self, args, state, control, logs=None, **kw):
        import math
        if logs and ("loss" in logs):
            v = logs["loss"]
            if v is None or math.isnan(v) or math.isinf(v):
                print(f"[NaN-STOP] train loss={v} at step {state.global_step}; aborting run.")
                control.should_training_stop = True
        return control


class CSVLogger(TrainerCallback):
    def __init__(self, path, run_name, cfg):
        self.path, self.run_name, self.cfg = path, run_name, cfg
    def on_evaluate(self, args, state, control, metrics=None, **kw):
        row = {"run": self.run_name, "epoch": round(state.epoch or 0, 2), **self.cfg,
               "eval_loss": metrics.get("eval_loss"),
               "macro_f1": metrics.get("eval_macro_f1"),
               "accuracy": metrics.get("eval_accuracy"),
               "r_supp": metrics.get("eval_recall_supporting"),
               "r_neut": metrics.get("eval_recall_neutral"),
               "r_opp": metrics.get("eval_recall_opposing"),
               "cm": json.dumps(_LAST_CM.get("cm"))}
        new = not os.path.exists(self.path)
        with open(self.path, "a", newline="") as f:
            wr = csv.DictWriter(f, fieldnames=list(row.keys()))
            if new: wr.writeheader()
            wr.writerow(row)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", default=os.environ.get("REPO_ROOT", "."))
    ap.add_argument("--run-name", required=True)
    ap.add_argument("--output-dir", required=True, help="put this on the NETWORK VOLUME")
    ap.add_argument("--lr", type=float, default=2e-5)
    ap.add_argument("--batch-size", type=int, default=32)
    ap.add_argument("--epochs", type=int, default=5)
    ap.add_argument("--loss", choices=["ce", "weighted", "focal"], default="weighted")
    ap.add_argument("--class-weights", default="effnum", help="none|effnum|sqrt|'a,b,c'")
    ap.add_argument("--focal-gamma", type=float, default=2.0)
    ap.add_argument("--balance", choices=["none", "under", "over"], default="none")
    ap.add_argument("--arch", choices=["full", "lora"], default="full")
    ap.add_argument("--lora-r", type=int, default=16)
    ap.add_argument("--lora-alpha", type=int, default=32)
    ap.add_argument("--lora-dropout", type=float, default=0.1)
    ap.add_argument("--lora-targets", choices=["qkv", "all"], default="qkv",
                    help="qkv = attention q/k/v only; all = q/k/v + every dense layer (more capacity)")
    ap.add_argument("--freeze-layers", type=int, default=0,
                    help="full arch only: freeze embeddings + this many bottom encoder layers")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--csv", default=None, help="shared sweep log (default <output-dir>/../runs_log.csv)")
    args = ap.parse_args()

    set_seed(args.seed)
    os.makedirs(args.output_dir, exist_ok=True)
    csv_path = args.csv or os.path.join(os.path.dirname(args.output_dir.rstrip("/")), "runs_log.csv")

    inner, dev = load_rows(args.repo_root)
    inner = balance(inner, args.balance, args.seed)
    weights = class_weights(args.class_weights, inner) if args.loss in ("weighted", "focal") else None

    tok = AutoTokenizer.from_pretrained(MODEL_NAME)
    def tokenize(b):  # premise = sentence, hypothesis = claim (matches the live pipeline + base model)
        return tok(b["sentence"], b["claim"], truncation=True, max_length=MAX_LEN)
    def to_ds(rows):
        ds = Dataset.from_list([{"sentence": r["sentence"], "claim": r["claim"], "labels": r["label_id"]} for r in rows])
        return ds.map(tokenize, batched=True, remove_columns=["sentence", "claim"])
    train_ds, dev_ds = to_ds(inner), to_ds(dev)

    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=3)
    if args.arch == "lora":
        from peft import LoraConfig, get_peft_model, TaskType
        tgts = ["query_proj", "key_proj", "value_proj"]
        if args.lora_targets == "all":
            tgts = tgts + ["dense"]   # adds attention-output + both FFN dense layers
        model = get_peft_model(model, LoraConfig(
            task_type=TaskType.SEQ_CLS, r=args.lora_r, lora_alpha=args.lora_alpha,
            lora_dropout=args.lora_dropout, target_modules=tgts))
        model.print_trainable_parameters()

    if args.arch == "full" and args.freeze_layers > 0:
        n = args.freeze_layers
        for name, p in model.named_parameters():
            if ("embeddings" in name) or any(f".layer.{i}." in name for i in range(n)):
                p.requires_grad = False
        tr = sum(p.numel() for p in model.parameters() if p.requires_grad)
        print(f"[freeze] froze embeddings + bottom {n} encoder layers | trainable params: {tr:,}")

    use_amp = os.environ.get("AMP", "1") != "0"   # AMP=0 -> full fp32 (DeBERTa-v3 stable)
    bf16 = use_amp and torch.cuda.is_available() and torch.cuda.is_bf16_supported()
    fp16 = use_amp and torch.cuda.is_available() and not bf16
    # arg name moved eval -> eval_strategy across versions; pick whichever exists
    ev = "eval_strategy" if "eval_strategy" in inspect.signature(TrainingArguments.__init__).parameters else "evaluation_strategy"
    ta_kwargs = {
        "output_dir": args.output_dir, "num_train_epochs": args.epochs,
        "per_device_train_batch_size": args.batch_size, "per_device_eval_batch_size": 64,
        "learning_rate": args.lr, "weight_decay": 0.01, "warmup_ratio": 0.10,
        "max_grad_norm": 1.0, "adam_epsilon": 1e-6,   # explicit grad clip + stable optimizer eps
        ev: "epoch", "save_strategy": "epoch", "save_total_limit": 2,
        "load_best_model_at_end": True, "metric_for_best_model": "macro_f1",
        "greater_is_better": True, "logging_steps": 50, "seed": args.seed,
        "bf16": bf16, "fp16": fp16, "report_to": "none",
    }
    targs = TrainingArguments(**ta_kwargs)

    cfg = {"lr": args.lr, "bs": args.batch_size, "loss": args.loss, "cw": args.class_weights,
           "balance": args.balance, "arch": args.arch, "seed": args.seed}
    collator = DataCollatorWithPadding(tokenizer=tok)   # dynamic padding; tok still valid on the collator
    tparams = inspect.signature(Trainer.__init__).parameters
    proc_kw = {"processing_class": tok} if "processing_class" in tparams else {"tokenizer": tok}
    trainer = LossTrainer(
        model=model, args=targs, train_dataset=train_ds, eval_dataset=dev_ds,
        compute_metrics=compute_metrics, data_collator=collator,
        loss_type=args.loss, weights=weights, focal_gamma=args.focal_gamma,
        callbacks=[CSVLogger(csv_path, args.run_name, cfg), NaNStopper()],
        **proc_kw,
    )

    pre = trainer.evaluate()
    print(f"[WARM-START before training] dev macro_f1 {pre.get('eval_macro_f1'):.4f} | "
          f"R supp {pre.get('eval_recall_supporting'):.3f} neut {pre.get('eval_recall_neutral'):.3f} "
          f"opp {pre.get('eval_recall_opposing'):.3f}")
    last_ckpt = get_last_checkpoint(args.output_dir) if os.path.isdir(args.output_dir) else None
    trainer.train(resume_from_checkpoint=last_ckpt)   # resumes if a checkpoint exists on the volume

    best = trainer.evaluate()
    best_dir = os.path.join(args.output_dir, "best_model")
    trainer.save_model(best_dir)
    tok.save_pretrained(best_dir)
    summary = {"run": args.run_name, "config": cfg, "best_dev": best,
               "best_dev_cm": _LAST_CM.get("cm"), "best_model_dir": best_dir}
    json.dump(summary, open(os.path.join(args.output_dir, "summary.json"), "w"), indent=2)
    print("\n=== BEST DEV ===")
    print(f"macro_f1 {best.get('eval_macro_f1'):.4f} | acc {best.get('eval_accuracy'):.4f} | "
          f"R supp {best.get('eval_recall_supporting'):.3f} neut {best.get('eval_recall_neutral'):.3f} "
          f"opp {best.get('eval_recall_opposing'):.3f}")
    print("dev confusion (rows=gold supp/neut/opp):", _LAST_CM.get("cm"))
    print(f"best model -> {best_dir}")
    print(f"sweep log  -> {csv_path}")


if __name__ == "__main__":
    main()