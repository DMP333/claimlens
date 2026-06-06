"""
Project A - Step 3: LLM sentence labeling (silver standard).

Adapted from archive/pre_finetune/diagnostics/llm_label_sentences.py. Paths anchored to
the finetune/ track, no dependency on common.py / tiers.json, incremental save + resume.

CHANGED from the original: the PROMPT is now the LOCKED strict sentence-bounded block
(R1-R8), the same one validated in finetune/score_probe.py against the human gold
(~84% agreement, kappa ~0.69 on Sonnet). The parser is hardened (JSON array first, then a
regex rescue for wrapped/malformed/partial output), and batch recovery fires on partial
parses too, not only refusals: any sentence a batch misses is re-sent individually.

What it does: read finetune/labeled_sources.json, take every web/encyclopedia/academic
source, split its snippet with the LOCKED production splitter (nli_service.split_sentences),
keep sentences with >= DEFAULT_MIN_WORDS words, dedup identical (claim, sentence) pairs,
and label each as supporting/opposing/neutral via the LLM. Fact-check and wikidata sources
are skipped (rating bypass / excluded from NLI).

Requires: pip install anthropic ; export ANTHROPIC_API_KEY=...
This is OFFLINE labeling, separate from the 'no LLM in the stance path' rule.

Run from repo root, inside venv `falseclaim`:
    LABEL_LIMIT=100 python finetune/label_sentences.py   # cheap dry-run: model string + real cost
    python finetune/label_sentences.py                   # full run

Knobs: LABEL_MODEL (default claude-sonnet-4-6), LABEL_LIMIT, LABEL_CONFIRM=1 (skip prompt),
       LABELED_SOURCES / LABELS_OUT / AUDIT_OUT to override paths.
"""
import json
import sys
import os
import re
import csv
import random
import time

random.seed(0)

# --- repo layout anchored to THIS file ---
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))   # .../finetune
_REPO_ROOT = os.path.dirname(_SCRIPT_DIR)
for _p in (_REPO_ROOT, _SCRIPT_DIR, os.getcwd()):
    if _p not in sys.path:
        sys.path.insert(0, _p)

# the LOCKED production splitter (importing nli_service loads DeBERTa+MiniLM; harmless here,
# we only use nltk-based split_sentences, but we import the real one so it stays single-source)
from app.services.nli_service import split_sentences, DEFAULT_MIN_WORDS  # noqa: E402

SOURCES_PATH = os.environ.get("LABELED_SOURCES", os.path.join(_SCRIPT_DIR, "labeled_sources.json"))
LABELS_PATH = os.environ.get("LABELS_OUT", os.path.join(_SCRIPT_DIR, "sentence_labels_llm.json"))
AUDIT_PATH = os.environ.get("AUDIT_OUT", os.path.join(_SCRIPT_DIR, "sentence_audit_sample.csv"))

SENT_TYPES = {"encyclopedia", "academic", "web"}
MODEL = os.environ.get("LABEL_MODEL", "claude-sonnet-4-6")
BATCH = 20
LABELS = ("supporting", "opposing", "neutral")

# PROMPT: LOCKED strict block. Must stay identical to score_probe.py's PROMPT, since that is
# what the ~84%/kappa-0.69 validation was measured on. Do not edit without re-validating on a
# FRESH probe set (changing it and re-scoring the same 150 would just overfit the rubric).
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


def load_sources(path):
    with open(path) as f:
        return json.load(f)


def collect_pairs(rows):
    pairs, seen = [], set()
    for r in rows:
        if r["source_type"] not in SENT_TYPES:
            continue
        claim = r["claim"]
        text = r.get("snippet_only") or ""
        for s in split_sentences(text):
            if len(s.split()) >= DEFAULT_MIN_WORDS:
                key = f"{claim}||{s}"
                if key not in seen:
                    seen.add(key)
                    pairs.append((claim, s))
    return pairs


def save_labels(labels):
    tmp = LABELS_PATH + ".tmp"
    with open(tmp, "w") as f:
        json.dump(labels, f, ensure_ascii=False, indent=2)
    os.replace(tmp, LABELS_PATH)


def label_chunk(client, claim, chunk):
    """Label one chunk. Returns (labels_dict, refused).
    labels_dict maps sentence -> stance for whatever parsed (JSON array first, then a regex
    rescue for wrapped/malformed/partial JSON). refused is True only when the model declined
    (stop_reason=refusal / empty content). A fully unparseable response raises internally so
    the attempt loop retries."""
    items = "\n".join(f"[{i}] {s}" for i, s in enumerate(chunk))
    msg = PROMPT.replace("{claim}", claim).replace("{items}", items)
    for attempt in range(3):
        try:
            resp = client.messages.create(
                model=MODEL, max_tokens=1500,
                messages=[{"role": "user", "content": msg}],
            )
            txt = "".join(
                b.text for b in (resp.content or []) if getattr(b, "type", "") == "text"
            ).strip()
            if getattr(resp, "stop_reason", "") == "refusal" or not txt:
                return {}, True  # model declined this chunk
            txt = re.sub(r"^```(?:json)?", "", txt).strip()
            txt = re.sub(r"```$", "", txt).strip()
            idx_out = {}
            # strategy 1: parse the JSON array
            try:
                arr = txt[txt.index("["):txt.rindex("]") + 1]
                for o in json.loads(arr):
                    i = int(o["i"])
                    stance = str(o["stance"]).strip().lower()
                    if 0 <= i < len(chunk) and stance in LABELS:
                        idx_out[i] = stance
            except Exception:
                pass
            # strategy 2: rescue individual objects if the array was wrapped/malformed/partial
            if len(idx_out) < len(chunk):
                for mo in re.finditer(r'"i"\s*:\s*(\d+)\s*,\s*"stance"\s*:\s*"([A-Za-z]+)"', txt):
                    i = int(mo.group(1))
                    stance = mo.group(2).strip().lower()
                    if 0 <= i < len(chunk) and stance in LABELS and i not in idx_out:
                        idx_out[i] = stance
            if idx_out:
                return {chunk[i]: st for i, st in idx_out.items()}, False
            raise ValueError("unparseable response")  # nothing recovered -> retry
        except Exception:  # noqa: BLE001 - transport/JSON error -> retry
            time.sleep(1.5)
    return {}, False  # failure after retries (not a refusal)


def main():
    try:
        import anthropic
    except ImportError:
        print("pip install anthropic"); return
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("export ANTHROPIC_API_KEY=..."); return
    client = anthropic.Anthropic()

    rows = load_sources(SOURCES_PATH)
    all_pairs = collect_pairs(rows)

    # resume: load existing labels and skip pairs already done
    labels = {}
    if os.path.exists(LABELS_PATH):
        labels = load_sources(LABELS_PATH)
        print(f"[RESUME] {len(labels)} labels already on disk; will skip those.")
    pairs = [(c, s) for (c, s) in all_pairs if f"{c}||{s}" not in labels]

    limit = int(os.environ.get("LABEL_LIMIT", "0"))
    if limit and len(pairs) > limit:
        pairs = pairs[:limit]
        print(f"LABEL_LIMIT={limit}: labeling only the first {limit} new pairs (cheap test run).")

    n = len(pairs)
    if n == 0:
        print("Nothing new to label."); return
    approx_calls = -(-n // BATCH)
    print(f"{len(all_pairs)} total eligible pairs | {n} still to label "
          f"-> ~{approx_calls} API calls, ~{approx_calls*1700:,} tokens.")
    print(f"Model: {MODEL}. OFFLINE one-time cost; check your Anthropic console for the charge.")
    print("Tip: LABEL_LIMIT=100 first to confirm the model string + real cost, then run the rest.")
    if os.environ.get("LABEL_CONFIRM") != "1":
        try:
            input("Press Enter to proceed, Ctrl-C to abort (LABEL_CONFIRM=1 skips this). ")
        except (EOFError, KeyboardInterrupt):
            print("\nAborted, nothing spent."); return

    by_c = {}
    for claim, s in pairs:
        by_c.setdefault(claim, []).append(s)

    done = 0
    refused = 0
    for claim, sents in by_c.items():
        for b in range(0, len(sents), BATCH):
            chunk = sents[b:b + BATCH]
            got, was_refused = label_chunk(client, claim, chunk)
            missing = [s for s in chunk if s not in got]
            if missing and len(chunk) > 1:
                # recover whatever the batch missed (refusal OR partial parse) one at a time
                tag = "refusal" if was_refused else "partial parse"
                print(f"  [{tag}] re-labeling {len(missing)}/{len(chunk)} missed in {claim[:40]!r} individually")
                for s in missing:
                    g1, r1 = label_chunk(client, claim, [s])
                    if g1:
                        got.update(g1)
                    elif r1:
                        refused += 1
            elif missing and was_refused:
                refused += len(missing)
            for s, stance in got.items():
                labels[f"{claim}||{s}"] = stance
            done += len(chunk)
            if done % 200 < BATCH:
                print(f"  {done}/{n}")
        save_labels(labels)  # checkpoint after each claim: crash-safe + resumable

    save_labels(labels)
    print(f"Wrote {LABELS_PATH} ({len(labels)} labels) | {refused} sentence(s) refused by safety and left unlabeled")

    covered = sum(1 for (c, s) in all_pairs if f"{c}||{s}" in labels)
    miss = len(all_pairs) - covered
    print(f"coverage: {covered}/{len(all_pairs)} sentences labeled"
          f"{f' ({miss} still unlabeled; rerun to retry them)' if miss else ' (complete)'}")

    dist = {}
    for v in labels.values():
        dist[v] = dist.get(v, 0) + 1
    tot = sum(dist.values()) or 1
    print("label distribution:", {k: f"{v} ({v*100//tot}%)" for k, v in dist.items()})
    print("  ^ under the strict prompt expect neutral ~75-80%; that's the class-weighted-loss basis.")

    # stratified audit sample for the human cross-check (this is what validates the silver labels)
    by_label = {}
    for k, v in labels.items():
        by_label.setdefault(v, []).append(k)
    sample = []
    for v, ks in by_label.items():
        random.shuffle(ks)
        sample += [(k, v) for k in ks[:50]]
    with open(AUDIT_PATH, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["claim", "sentence", "llm_label", "your_label"])
        for k, v in sample[:150]:
            claim, s = k.split("||", 1)
            w.writerow([claim, s, v, ""])
    print(f"Wrote {AUDIT_PATH}: optional extra human cross-check on a fresh 150 rows.")


if __name__ == "__main__":
    main()