"""
SCALABLE LABELER:  use a strong LLM to label per-sentence stance for the WHOLE set,
so you never hand-label thousands. Output is the silver-standard reference consumed
by d4 (oracle) and by per-sentence NLI accuracy.

Workflow:
  1. python diagnostics/llm_label_sentences.py            # labels all sentences via API
  2. hand-label the emitted audit sample (~150) and compare agreement (script prints how)
  3. if agreement is high, trust the LLM labels across the full set

Requires: pip install anthropic ; export ANTHROPIC_API_KEY=...
Note: this is OFFLINE labeling, separate from the 'no LLM in the stance path' rule.
"""
import json, sys, os, csv, random, time
sys.path.insert(0, os.getcwd())
random.seed(0)
from app.services.nli_service import split_sentences, DEFAULT_MIN_WORDS
from common import load_sources, load_json

SENT_TYPES = {"encyclopedia", "academic", "web"}
MODEL = os.environ.get("LABEL_MODEL", "claude-sonnet-4-5")   # change as needed
BATCH = 20

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

def collect_pairs(rows, allowed_claims=None):
    pairs = []
    seen = set()
    for r in rows:
        if r["source_type"] not in SENT_TYPES: continue
        claim = r["claim"]
        if allowed_claims is not None and claim not in allowed_claims: continue
        text = r.get("snippet_only") or ""
        for s in split_sentences(text):
            if len(s.split()) >= DEFAULT_MIN_WORDS:
                key = f"{claim}||{s}"
                if key not in seen:
                    seen.add(key); pairs.append((claim, s))
    return pairs

def main():
    try:
        import anthropic
    except ImportError:
        print("pip install anthropic"); return
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("export ANTHROPIC_API_KEY=..."); return
    client = anthropic.Anthropic()

    rows = load_sources()
    allowed = None
    if os.environ.get("TIER_A_ONLY") == "1":
        tiers = load_json("tiers.json", {})
        allowed = {c for c, v in tiers.items() if v.get("tier") == "A"}
        print(f"TIER_A_ONLY=1: labeling only Tier A claims ({len(allowed)} of {len(tiers)}).")
    pairs = collect_pairs(rows, allowed)
    limit = int(os.environ.get("LABEL_LIMIT", "0"))
    if limit and len(pairs) > limit:
        pairs = pairs[:limit]
        print(f"LABEL_LIMIT={limit}: labeling only the first {limit} pairs (cheap test run).")
    n = len(pairs)
    approx_calls = -(-n // BATCH)            # ceil
    print(f"{n} unique (claim, sentence) pairs -> ~{approx_calls} API calls, ~{approx_calls*1300:,} tokens total.")
    print(f"Model: {MODEL}. One-time OFFLINE cost. Check your Anthropic console for the exact charge.")
    print("Tip: run once with LABEL_LIMIT=100 to see the real cost in your console, then run the rest.")
    if os.environ.get("LABEL_CONFIRM") != "1":
        try:
            input("Press Enter to proceed, or Ctrl-C to abort (set LABEL_CONFIRM=1 to skip this prompt). ")
        except (EOFError, KeyboardInterrupt):
            print("\nAborted, nothing spent."); return

    # group by claim, batch sentences per call
    by_c = {}
    for claim, s in pairs:
        by_c.setdefault(claim, []).append(s)

    labels = {}
    done = 0
    for claim, sents in by_c.items():
        for b in range(0, len(sents), BATCH):
            chunk = sents[b:b+BATCH]
            items = "\n".join(f'{i}: {s}' for i, s in enumerate(chunk))
            msg = PROMPT.replace("{claim}", claim).replace("{items}", items)
            for attempt in range(3):
                try:
                    resp = client.messages.create(model=MODEL, max_tokens=1024,
                                                   messages=[{"role":"user","content":msg}])
                    txt = resp.content[0].text.strip()
                    txt = txt[txt.index("["):txt.rindex("]")+1]
                    arr = json.loads(txt)
                    for o in arr:
                        labels[f"{claim}||{chunk[int(o['i'])]}"] = o["stance"].strip().lower()
                    break
                except Exception as e:
                    if attempt == 2: print("  fail:", str(e)[:80])
                    time.sleep(1.5)
            done += len(chunk)
            if done % 200 < BATCH: print(f"  {done}/{len(pairs)}")
    json.dump(labels, open("sentence_labels_llm.json", "w"), indent=2)
    print(f"Wrote sentence_labels_llm.json ({len(labels)} labels)")

    # audit sample (stratified by LLM label), for human cross-check
    by_label = {}
    for k, v in labels.items():
        by_label.setdefault(v, []).append(k)
    sample = []
    for v, ks in by_label.items():
        random.shuffle(ks); sample += [(k, v) for k in ks[:50]]
    with open("sentence_audit_sample.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(["claim","sentence","llm_label","your_label"])
        for k, v in sample[:150]:
            claim, s = k.split("||", 1); w.writerow([claim, s, v, ""])
    print("Wrote sentence_audit_sample.csv (fill 'your_label', then measure agreement:")
    print("  pandas: df=read_csv(...); (df.llm_label==df.your_label).mean())")

if __name__ == "__main__":
    main()