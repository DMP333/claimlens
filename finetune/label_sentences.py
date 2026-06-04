"""
Project A - Step 3: LLM sentence labeling (silver standard).

Adapted from archive/pre_finetune/diagnostics/llm_label_sentences.py. The labeling
logic and PROMPT are UNCHANGED from the original (so label semantics match your d5
diagnosis); what's new is: paths anchored to the finetune/ track, no dependency on
common.py / tiers.json, and incremental save + resume so a crash mid-run never
re-spends or loses work.

What it does: read finetune/labeled_sources.json, take every web/encyclopedia/academic
source, split its snippet with your LOCKED production splitter (nli_service.split_sentences),
keep sentences with >= DEFAULT_MIN_WORDS words (exactly what production scores), dedup
identical (claim, sentence) pairs, and label each as supporting/opposing/neutral via the LLM.
Fact-check and wikidata sources are skipped (rating bypass / excluded from NLI).

Requires: pip install anthropic ; export ANTHROPIC_API_KEY=...
This is OFFLINE labeling, separate from the 'no LLM in the stance path' rule.

Run from repo root, inside venv `falseclaim`:
    # cheap dry-run first: confirm the model string works and see real cost in your console
    LABEL_LIMIT=100 python finetune/label_sentences.py
    # then the full run
    python finetune/label_sentences.py

Knobs: LABEL_MODEL (default claude-sonnet-4-6), LABEL_LIMIT, LABEL_CONFIRM=1 (skip prompt),
       LABELED_SOURCES / LABELS_OUT / AUDIT_OUT to override paths.
"""
import json
import sys
import os
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
# original used claude-sonnet-4-5 (likely retired). claude-sonnet-4-6 is the current
# same-tier model; override with LABEL_MODEL if you want a stronger one for silver labels.
MODEL = os.environ.get("LABEL_MODEL", "claude-sonnet-4-6")
BATCH = 20

# PROMPT: verbatim from the original labeler. Do not edit without re-auditing.
PROMPT = """You label the stance of a SENTENCE toward a CLAIM, judging the sentence ALONE.
Return ONLY one word per item: supporting, opposing, or neutral.
- supporting: the sentence, read alone, provides evidence the claim is TRUE.
- opposing: the sentence provides evidence the claim is FALSE.
- neutral: off-topic, or states the claim without evidence, or is about a different entity/subtopic.
Treat a sentence that merely RESTATES a myth (without endorsing it) as neutral or opposing per its actual content, not supporting.
Return a JSON array of {"i": <index>, "stance": "<label>"} and nothing else.

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
    labels_dict maps sentence -> stance for whatever the model labeled.
    refused is True only when the model declined (stop_reason=refusal / empty content)."""
    items = "\n".join(f"{i}: {s}" for i, s in enumerate(chunk))
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
            if "[" not in txt:
                raise ValueError("no JSON array in response")
            txt = txt[txt.index("["):txt.rindex("]") + 1]
            out = {}
            for o in json.loads(txt):
                try:
                    idx = int(o["i"])
                    stance = str(o["stance"]).strip().lower()
                except (KeyError, ValueError, TypeError):
                    continue
                if 0 <= idx < len(chunk) and stance in ("supporting", "opposing", "neutral"):
                    out[chunk[idx]] = stance
            return out, False
        except Exception:  # noqa: BLE001 - transport/JSON error -> retry
            time.sleep(1.5)
    return {}, False  # transport failure after retries (not a refusal)


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
          f"-> ~{approx_calls} API calls, ~{approx_calls*1300:,} tokens.")
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
            if was_refused and len(chunk) > 1:
                # isolate the trigger: re-label one sentence at a time, recover the innocent ones
                print(f"  [refusal] splitting {len(chunk)}-sentence batch in {claim[:40]!r} to recover the rest")
                for s in chunk:
                    g1, r1 = label_chunk(client, claim, [s])
                    if g1:
                        got.update(g1)
                    elif r1:
                        refused += 1
            elif was_refused:
                refused += 1
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
    print("  ^ confirm neutral is ~70%; that's the basis for the class-weighted-loss plan.")

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
    print(f"Wrote {AUDIT_PATH}: fill 'your_label' on the 150 rows, then measure agreement:")
    print("  import pandas as pd; df=pd.read_csv(...); (df.llm_label==df.your_label).mean()")


if __name__ == "__main__":
    main()