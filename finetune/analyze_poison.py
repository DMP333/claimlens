"""
TEST 1 (Layer 1): does the silver label fix DeBERTa where it counts?

Run AFTER scoring the poison set:
    GRADED=finetune/probe_poison_graded.csv MODELS=claude-sonnet-4-6 python finetune/score_probe.py
which writes scored_claude-sonnet-4-6.csv.

Joins three labels per sentence:
    gold     = your hand label            (probe_poison_graded.csv)
    deberta  = current model's call       (probe_poison_key.csv)
    silver   = strict-prompt LLM label    (scored_<model>.csv)

GUARD: verifies the scored file's sentences match the poison sentences by id and aborts
if they don't, so it can never silently grade against the wrong scored file again.

Only rows where silver != deberta can move the model. Those split three ways:
    BENEFICIAL : silver != deberta AND silver == gold
    HARMFUL    : silver != deberta AND silver != gold AND deberta == gold
    WASTED     : silver != deberta AND silver != gold AND deberta != gold
Headline = beneficial share of the disagreement set, on non-truncated rows.

    python finetune/analyze_poison.py
    SCORED=scored_claude-opus-4-8.csv python finetune/analyze_poison.py
"""
import csv, os, sys

_DIR = os.path.dirname(os.path.abspath(__file__))
GRADED = os.environ.get("GRADED", os.path.join(_DIR, "probe_poison_graded.csv"))
KEY    = os.environ.get("KEY",    os.path.join(_DIR, "probe_poison_key.csv"))
SCORED = os.environ.get("SCORED", os.path.join(_DIR, "scored_claude-sonnet-4-6.csv"))
LABELS = ("supporting", "opposing", "neutral")


def norm(x):
    return (x or "").strip().lower()


def load(path):
    if not os.path.exists(path):
        sys.exit(f"missing {path} (run score_probe.py first, or set SCORED=...)")
    with open(path) as f:
        return list(csv.DictReader(f))


def pick(row, *names):
    for n in names:
        for k in row:
            if k.strip().lower() == n:
                return row[k]
    return None


def norm_sent(s):
    return " ".join((s or "").split())[:60].lower()


def main():
    gold, trunc, gsent, direction, deb = {}, {}, {}, {}, {}
    for r in load(GRADED):
        i = r["id"]; gold[i] = norm(r["your_label"])
        trunc[i] = norm(r.get("is_truncated")) == "yes"
        gsent[i] = norm_sent(r["sentence"])
    for r in load(KEY):
        i = r["id"]; direction[i] = (norm(r["old_llm_label"]), norm(r["deberta_label"]))
        deb[i] = norm(r["deberta_label"])

    silver, ssent = {}, {}
    for r in load(SCORED):
        i = pick(r, "id"); lab = pick(r, "llm_label", "llm", "pred", "prediction")
        sen = pick(r, "sentence")
        if i is not None and lab is not None:
            silver[i] = norm(lab); ssent[i] = norm_sent(sen) if sen is not None else None

    # ---- GUARD: scored sentences must match the graded sentences by id ----
    checkable = [i for i in silver if i in gsent and ssent.get(i)]
    if checkable:
        mismatch = [i for i in checkable if ssent[i] != gsent[i]]
        if len(mismatch) > 0.05 * len(checkable):
            ex = mismatch[0]
            sys.exit(
                f"\nABORT: {SCORED} does not match the poison set.\n"
                f"  {len(mismatch)}/{len(checkable)} sentences differ by id.\n"
                f"  e.g. id {ex}:\n    scored: {ssent[ex]!r}\n    poison: {gsent[ex]!r}\n"
                f"You are pointing at the wrong scored file (likely a stale v1 run).\n"
                f"Re-run score_probe with GRADED=finetune/probe_poison_graded.csv and make\n"
                f"sure it prints 'wrote scored_...csv' at the end.\n")
    else:
        print("note: scored file has no sentence column to verify against; skipping guard")

    ids = [i for i in gold if i in deb and i in silver and gold[i] in LABELS]
    if not ids:
        sys.exit("no joinable rows; check the 'id' column in scored_*.csv")

    def report(subset, title):
        dis = [i for i in subset if silver[i] != deb[i]]
        agree = [i for i in subset if silver[i] == deb[i]]
        ben = [i for i in dis if silver[i] == gold[i]]
        harm = [i for i in dis if silver[i] != gold[i] and deb[i] == gold[i]]
        wast = [i for i in dis if silver[i] != gold[i] and deb[i] != gold[i]]
        n = len(subset)
        sg = sum(silver[i] == gold[i] for i in subset)
        print(f"\n=== {title} (n={n}) ===")
        print(f"silver vs gold overall:  {sg}/{n} = {sg/n:.0%}")
        print(f"disagreement set (silver != deberta): {len(dis)}")
        if dis:
            print(f"   BENEFICIAL (silver right, overrides DeBERTa): {len(ben)}/{len(dis)} = {len(ben)/len(dis):.0%}  <- the number that decides it")
            print(f"   HARMFUL   (silver wrong, DeBERTa was right):  {len(harm)}/{len(dis)} = {len(harm)/len(dis):.0%}")
            print(f"   WASTED    (both wrong):                        {len(wast)}/{len(dis)} = {len(wast)/len(dis):.0%}")
        if agree:
            ok = sum(gold[i] == silver[i] for i in agree)
            print(f"agreement set (silver == deberta): {len(agree)} | gold confirms: {ok}/{len(agree)} = {ok/len(agree):.0%}")

    report(ids, "ALL graded rows")
    report([i for i in ids if not trunc[i]], "NON-TRUNCATED only (matches the filtered training set)")

    print("\n=== beneficial share by poison direction (non-truncated) ===")
    buckets = {}
    for i in ids:
        if trunc[i]: continue
        old, d = direction[i]
        dname = (f"forced_{d}" if old == "neutral" and d in ("supporting", "opposing")
                 else f"undercall_{old}" if d == "neutral" else "hardflip")
        buckets.setdefault(dname, []).append(i)
    for name, b in sorted(buckets.items()):
        dis = [i for i in b if silver[i] != deb[i]]
        ben = [i for i in dis if silver[i] == gold[i]]
        share = f"{len(ben)}/{len(dis)} = {len(ben)/len(dis):.0%}" if dis else "no disagreements"
        print(f"   {name:<22} beneficial {share}")


if __name__ == "__main__":
    main()