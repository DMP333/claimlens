"""
Project A - Probe scorer (go/no-go gate for the sentence-bounded labeling standard).

Relabels the graded validation probe under the LOCKED strict prompt with one or more
models, then scores each model against your gold grades and reports:
  - gold vs llm overall agreement and Cohen's kappa (chance-corrected)
  - 3x3 confusion matrix (gold rows x llm cols)
  - agreement broken down by OLD llm-label band (did the over-reach get fixed?)
  - agreement on JUST the rows your strict re-grade CHANGED from the old label
    (the crux: does the strict prompt reproduce your corrections on its own?)
  - the llm's own neutral rate (pathology / kill-signal check)
  - every disagreement dumped to csv so you can eyeball clear-error vs gray-tie

IMPORTANT: the PROMPT below must be IDENTICAL to the one you patch into
label_sentences.py before the full relabel, or the validation does not represent
production. Patch this same block in over there.

Run from repo root, in venv `falseclaim`, with ANTHROPIC_API_KEY set:
    python finetune/score_probe.py

Inputs (finetune/):
    probe_graded_v1.csv   -> id, claim, sentence, your_label    (your gold)
    probe_key_*.csv       -> id, claim, sentence, old_llm_label (optional, for by-band)
Outputs (finetune/):
    scored_<model>.csv         -> every row with gold, old, llm_label
    disagreements_<model>.csv  -> rows where gold != llm_label
"""
import os
import csv
import json
import glob
import re
import time
from collections import Counter, OrderedDict

# --- config -------------------------------------------------------------
# Default runs both. Override to run one model per command for separate cost tracking:
#   MODELS=claude-sonnet-4-6 python finetune/score_probe.py
#   MODELS=claude-opus-4-8   python finetune/score_probe.py
MODELS = [m.strip() for m in os.environ.get(
    "MODELS", "claude-sonnet-4-6,claude-opus-4-8").split(",") if m.strip()]
# If a model string 404s, verify the exact id against your SDK / docs and edit here.

_DIR = os.path.dirname(os.path.abspath(__file__))
GRADED_PATH = os.environ.get("GRADED", os.path.join(_DIR, "probe_graded_v1.csv"))
LABELS = ("supporting", "opposing", "neutral")
MAX_TOKENS = 1500

PROMPT = """TASK: Label each SENTENCE's stance toward the CLAIM, judging the sentence ALONE.
Output one of: supporting, opposing, neutral.

MASTER RULE - read first, applies everywhere:
Judge ONLY the words in the sentence and the claim. Add nothing, remove nothing.
Do not supply a fact, definition, causal link, or inference the sentence does not state.
Do not add doubt or a "they're only claiming this" frame the sentence does not state.
If linking the sentence to the claim needs a step the sentence does not make, do not make
it; that is neutral. Almost every wrong label comes from supplying the missing step yourself.

LABELS:
- supporting: the sentence, alone, asserts or gives evidence the claim is TRUE.
- opposing:   the sentence, alone, asserts or gives evidence the claim is FALSE.
- neutral:    the sentence does not decide either way under the rules below.

R1  ATTRIBUTION IS NOT NEUTRAL. "A study found X", "according to Y", "the anchor said X"
    is a source asserting X. Judge the asserted content, not the attribution.
    Ex: claim "Amazon produces 20% of the world's oxygen"; sentence "It provides 20% of the
    planet's oxygen, the anchor said" -> supporting.

R2  FALSE-FRAMING = OPPOSING. A sentence flips to opposing only when a word IN the sentence
    frames the claim as false: "the myth that", "the false claim that", "debunked", "wrongly".
    (Merely mentioning or quoting the claim without asserting it is neutral; see R7.)

R3  NO-EVIDENCE / NO-EFFECT = OPPOSING. "No evidence that X", "does not affect", "no
    significant impact" -> opposing. The mirror ("established/confirmed/proven") -> supporting.

R4  MATCH THE CLAIM'S MODIFIER BY TYPE.
    - DEGREE modifier (superlative / comparative / ranking / exact count: driest, largest,
      greatest, only, most, three): the sentence must establish THAT degree; a weaker
      version is neutral. Ex: claim "driest continent"; "Antarctica is dry" -> neutral.
    - QUANTIFIER (all / most / some / none): match the claim's quantifier. "not all X"
      neither establishes nor contradicts "most X"; "some X" does not establish "most X".
    - SCOPE modifier (a when/where/who restriction: throughout their lives, in winter): if
      the sentence supports the core assertion and does not contradict the scope, supporting;
      do not downgrade over an unaddressed scope detail or import outside facts about it.

R5  OPINION / VALUE CLAIMS (should, better, greatest, belongs). Supporting requires the
    sentence to make the evaluative case FOR the position. A bare fact, statistic, or
    achievement the sentence does not itself connect to the position is neutral.
    Ex: claim "LeBron is the greatest"; "passed Abdul-Jabbar, 11,000 points ahead" -> neutral.

R6  REFERENCES. Resolve "it / this / the study / they" to the obvious subject of the claim
    when that is the only sensible reading. If you cannot tell what it refers to, neutral.

R7  NON-CONTENT is neutral: reference lists, citations, funding lines, bylines, navigation
    text. Pure depiction, hypothetical, or "some believe" without endorsement is neutral.

R8  TIE-BREAK. If after R1-R7 you still cannot tell, label neutral.

OUTPUT: a JSON array only, one object per sentence, exactly like
[{"i": 0, "stance": "neutral"}, {"i": 1, "stance": "supporting"}]
No preamble, no explanation, no markdown fences, nothing but the array.

CLAIM: {claim}
SENTENCES:
{items}"""


# --- llm calls ----------------------------------------------------------
def get_client():
    from anthropic import Anthropic
    return Anthropic()


def parse_labels(text, n):
    out = [None] * n
    t = (text or "").strip()
    t = re.sub(r"^```(?:json)?", "", t).strip()
    t = re.sub(r"```$", "", t).strip()
    # strategy 1: parse a JSON array
    try:
        m = re.search(r"\[.*\]", t, flags=re.DOTALL)
        arr = json.loads(m.group(0)) if m else json.loads(t)
        for obj in arr:
            i = int(obj["i"])
            stance = str(obj["stance"]).strip().lower()
            if 0 <= i < n and stance in LABELS:
                out[i] = stance
    except Exception:
        pass
    # strategy 2: rescue individual objects via regex if the array was wrapped/malformed
    if any(v is None for v in out):
        for mo in re.finditer(r'"i"\s*:\s*(\d+)\s*,\s*"stance"\s*:\s*"([A-Za-z]+)"', t):
            i = int(mo.group(1))
            stance = mo.group(2).strip().lower()
            if 0 <= i < n and stance in LABELS and out[i] is None:
                out[i] = stance
    return out


def label_batch(client, model, claim, sentences):
    items = "\n".join(f"[{i}] {s}" for i, s in enumerate(sentences))
    prompt = PROMPT.replace("{claim}", claim).replace("{items}", items)
    last_it = last_ot = 0
    for attempt in range(2):
        try:
            resp = client.messages.create(
                model=model, max_tokens=MAX_TOKENS,
                messages=[{"role": "user", "content": prompt}],
            )
            text = "".join(b.text for b in resp.content
                           if getattr(b, "type", "") == "text")
            u = getattr(resp, "usage", None)
            last_it = getattr(u, "input_tokens", 0) or 0
            last_ot = getattr(u, "output_tokens", 0) or 0
            labels = parse_labels(text, len(sentences))
            if any(v is not None for v in labels) or attempt == 1:
                return labels, last_it, last_ot
            time.sleep(1)  # parsed to nothing -> retry once
        except Exception as e:
            if attempt == 0:
                time.sleep(2)
                continue
            print(f"    batch failed ({model}): {e}")
            return [None] * len(sentences), last_it, last_ot
    return [None] * len(sentences), last_it, last_ot


# --- data ---------------------------------------------------------------
def load_rows():
    if not os.path.exists(GRADED_PATH):
        raise SystemExit(f"missing {GRADED_PATH}")
    rows = []
    with open(GRADED_PATH) as f:
        for r in csv.DictReader(f):
            gold = (r.get("your_label") or "").strip().lower()
            rows.append({"id": r.get("id"), "claim": r["claim"],
                         "sentence": r["sentence"], "gold": gold,
                         "old": None, "llm": {}, "fb": {}})

    gset = {(x["claim"], x["sentence"]) for x in rows}
    best, best_map, best_ov = None, {}, -1
    for kf in sorted(glob.glob(os.path.join(_DIR, "probe_key*.csv"))):
        with open(kf) as f:
            kmap = {(r["claim"], r["sentence"]): (r.get("old_llm_label") or "").strip().lower()
                    for r in csv.DictReader(f)}
        ov = len(gset & set(kmap))
        if ov > best_ov:
            best, best_map, best_ov = kf, kmap, ov
    if best and best_ov > 0:
        for x in rows:
            x["old"] = best_map.get((x["claim"], x["sentence"]))
        print(f"old labels from {os.path.basename(best)} ({best_ov}/{len(rows)} matched)")
    else:
        print("no matching probe_key*.csv found -> skipping by-old-band breakdown")

    bad = [x["id"] for x in rows if x["gold"] not in LABELS]
    if bad:
        print(f"WARNING: {len(bad)} rows have a blank/invalid gold label (ids {bad[:10]}...)")
    return rows


def group_by_claim(rows):
    g = OrderedDict()
    for x in rows:
        g.setdefault(x["claim"], []).append(x)
    return g


# --- metrics ------------------------------------------------------------
def agreement(pairs):
    if not pairs:
        return float("nan"), 0
    return sum(1 for a, b in pairs if a == b) / len(pairs), len(pairs)


def kappa(pairs):
    n = len(pairs)
    if n == 0:
        return float("nan")
    po = sum(1 for a, b in pairs if a == b) / n
    ca, cb = Counter(a for a, _ in pairs), Counter(b for _, b in pairs)
    pe = sum((ca[l] / n) * (cb[l] / n) for l in LABELS)
    return (po - pe) / (1 - pe) if pe != 1 else float("nan")


def run_model(client, model, rows):
    groups = group_by_claim(rows)
    fb, in_tok, out_tok = 0, 0, 0
    for ci, (claim, items) in enumerate(groups.items(), 1):
        labels, it, ot = label_batch(client, model, claim, [x["sentence"] for x in items])
        in_tok += it
        out_tok += ot
        for x, lab in zip(items, labels):
            if lab is None:
                fb += 1
                x["fb"][model] = True
                lab = "neutral"
            x["llm"][model] = lab
        if ci % 10 == 0:
            print(f"    {model}: {ci}/{len(groups)} claims")
    return fb, in_tok, out_tok


def report(model, rows, fb, in_tok, out_tok):
    valid = [x for x in rows if x["gold"] in LABELS and x["llm"].get(model) in LABELS]
    pairs = [(x["gold"], x["llm"][model]) for x in valid]
    acc, n = agreement(pairs)
    k = kappa(pairs)
    gd = Counter(x["gold"] for x in valid)
    ld = Counter(x["llm"][model] for x in valid)

    print(f"\n================  {model}  ================")
    print(f"scored {n} rows | fallbacks (forced neutral): {fb} | "
          f"tokens: in {in_tok:,}  out {out_tok:,}")
    print(f"gold dist : " + "  ".join(f"{l} {gd[l]}" for l in LABELS))
    print(f"llm  dist : " + "  ".join(f"{l} {ld[l]}" for l in LABELS)
          + f"   (llm neutral rate {ld['neutral']/n:.0%})")
    print(f"\noverall agreement vs gold : {acc:.1%}   kappa : {k:.2f}")

    print("\nconfusion (rows=gold, cols=llm):")
    print("            " + "".join(f"{l[:4]:>8}" for l in LABELS))
    for g in LABELS:
        row = Counter(x["llm"][model] for x in valid if x["gold"] == g)
        print(f"  {g:<9} " + "".join(f"{row[l]:>8}" for l in LABELS))

    if any(x["old"] in LABELS for x in valid):
        print("\nagreement by OLD-label band (did over-reach get fixed?):")
        for band in LABELS:
            ba, bn = agreement([(x["gold"], x["llm"][model])
                                for x in valid if x["old"] == band])
            print(f"  old={band:<11} {ba:.1%}  (n={bn})")
        corr = [(x["gold"], x["llm"][model])
                for x in valid if x["old"] in LABELS and x["gold"] != x["old"]]
        ca, cn = agreement(corr)
        print(f"\nCRUX - rows your re-grade CHANGED from old label: "
              f"llm matches gold {ca:.1%}  (n={cn})")
        print("  (high here = the strict prompt reproduces your corrections unsupervised)")

    with open(os.path.join(_DIR, f"scored_{model}.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "claim", "sentence", "gold", "old", "llm_label", "fallback"])
        for x in rows:
            w.writerow([x["id"], x["claim"], x["sentence"], x["gold"],
                        x["old"], x["llm"].get(model), int(x["fb"].get(model, False))])
    dis = [x for x in valid if x["gold"] != x["llm"][model]]
    with open(os.path.join(_DIR, f"disagreements_{model}.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "claim", "sentence", "gold", "old", "llm_label"])
        for x in dis:
            w.writerow([x["id"], x["claim"], x["sentence"], x["gold"], x["old"], x["llm"][model]])
    print(f"\nwrote scored_{model}.csv and disagreements_{model}.csv ({len(dis)} disagreements)")


def main():
    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise SystemExit("set ANTHROPIC_API_KEY")
    rows = load_rows()
    client = get_client()
    for model in MODELS:
        print(f"\nrelabeling under strict prompt with {model} ...")
        fb, in_tok, out_tok = run_model(client, model, rows)
        report(model, rows, fb, in_tok, out_tok)


if __name__ == "__main__":
    main()