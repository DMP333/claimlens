"""
Project A - Probe sampler (round-aware) for the sentence-bounded labeling standard.

Draws a fresh 150-sentence validation probe from the silver labels, EXCLUDING:
  - the original audit set (sentence_audit_sample.csv), and
  - every prior probe round (probe_blank*.csv / probe_key*.csv).
so each new set is untouched. Stratified 50/50/50 by the OLD llm label so the stance
bands (where the over-reach lives) are well represented; neutrals ride along as a
regression guard. A soft per-claim cap stops one verbose source dominating a band,
and the final 150 are shuffled so row position never leaks the old label.

Re-run it after any rule change and it auto-increments the round, excluding all
earlier rounds, so the tune/validation split stays clean with zero edits.

Run from repo root, inside venv `falseclaim`:
    python finetune/build_probe.py

Outputs (in finetune/), where N is the next round:
    probe_blank_rN.csv -> id, claim, sentence, your_label   (YOU fill, blind, under R1-R8)
    probe_key_rN.csv   -> id, claim, sentence, old_llm_label (DO NOT open until grading is done)
"""
import json
import os
import csv
import glob

_DIR = os.path.dirname(os.path.abspath(__file__))
LABELS_PATH = os.environ.get("LABELS_OUT", os.path.join(_DIR, "sentence_labels_llm.json"))
AUDIT_PATH = os.environ.get("AUDIT_OUT", os.path.join(_DIR, "sentence_audit_sample.csv"))

PER_LABEL = 50
PER_CLAIM_CAP = 3  # soft cap so one verbose claim can't dominate a band


def load_labels():
    with open(LABELS_PATH) as f:
        return json.load(f)  # {"claim||sentence": "supporting|opposing|neutral"}


def keys_from_csv(path):
    """Reconstruct claim||sentence keys from any probe/audit CSV (claim + sentence cols)."""
    out = set()
    if not os.path.exists(path):
        return out
    with open(path) as f:
        for row in csv.DictReader(f):
            if row.get("claim") is not None and row.get("sentence") is not None:
                out.add(f"{row['claim']}||{row['sentence']}")
    return out


def build_exclusion():
    used = set()
    used |= keys_from_csv(AUDIT_PATH)
    prior = sorted(set(glob.glob(os.path.join(_DIR, "probe_blank*.csv")))
                   | set(glob.glob(os.path.join(_DIR, "probe_key*.csv"))))
    for p in prior:
        used |= keys_from_csv(p)
    return used, prior


def next_round():
    existing = glob.glob(os.path.join(_DIR, "probe_blank*.csv"))
    return len(existing) + 1


def pick(keys, n, cap, rng):
    """Greedy pick up to n keys, at most `cap` per claim; relax the cap to fill any shortfall."""
    keys = list(keys)
    rng.shuffle(keys)
    chosen, per_claim = [], {}
    for k in keys:
        claim = k.split("||", 1)[0]
        if per_claim.get(claim, 0) < cap:
            chosen.append(k)
            per_claim[claim] = per_claim.get(claim, 0) + 1
            if len(chosen) == n:
                return chosen
    chosen_set = set(chosen)
    for k in keys:
        if k not in chosen_set:
            chosen.append(k)
            if len(chosen) == n:
                break
    return chosen


def main():
    import random
    round_n = next_round()
    rng = random.Random(round_n)  # distinct per round, reproducible

    labels = load_labels()
    used, prior = build_exclusion()
    print(f"{len(labels)} labels on disk | round {round_n} | excluding {len(used)} prior rows "
          f"(audit + {len(prior)} prior probe files)")

    by_label = {"neutral": [], "supporting": [], "opposing": []}
    for k, v in labels.items():
        if k in used:
            continue
        if v in by_label:
            by_label[v].append(k)

    sample = []
    for lab in ("neutral", "supporting", "opposing"):
        avail = by_label[lab]
        if len(avail) < PER_LABEL:
            print(f"  WARNING: only {len(avail)} '{lab}' rows left (< {PER_LABEL})")
        sel = pick(avail, min(PER_LABEL, len(avail)), PER_CLAIM_CAP, rng)
        sample += [(k, lab) for k in sel]
        print(f"  {lab}: selected {len(sel)} (from {len(avail)} available)")

    rng.shuffle(sample)  # mix bands so position never hints the old label

    blank_out = os.path.join(_DIR, f"probe_blank_r{round_n}.csv")
    key_out = os.path.join(_DIR, f"probe_key_r{round_n}.csv")
    with open(blank_out, "w", newline="") as fb, open(key_out, "w", newline="") as fk:
        wb, wk = csv.writer(fb), csv.writer(fk)
        wb.writerow(["id", "claim", "sentence", "your_label"])
        wk.writerow(["id", "claim", "sentence", "old_llm_label"])
        for i, (k, lab) in enumerate(sample):
            claim, sent = k.split("||", 1)
            wb.writerow([i, claim, sent, ""])
            wk.writerow([i, claim, sent, lab])

    print(f"\nWrote {blank_out} ({len(sample)} rows).")
    print("  -> Fill 'your_label' with supporting / opposing / neutral under R1-R8. Grade blind.")
    print(f"Wrote {key_out}.")
    print("  -> Do NOT open until you have finished grading; it carries the old label per row.")


if __name__ == "__main__":
    main()