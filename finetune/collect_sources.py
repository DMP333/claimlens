"""
Project A - Step 2: source collection.

Drives the REAL production retrieval route over all 150 roster claims and writes
one self-contained source file. No reimplementation: this calls your actual
search_sources / _filter_relevant_sources / _deduplicate_sources, in the exact
order analyze_claim uses them, stopping before analyze_sources (no NLI here).

Route per claim (identical to analyze_claim front matter):
    domain  = classify_claim_domain(claim)
    rc      = build_routing_config(domain, claim)
    raw     = await search_sources(ClaimRequest(claim=claim), rc)
    raw     = _filter_relevant_sources(claim, raw)     # MiniLM relevance, thr 0.35
    raw     = _deduplicate_sources(raw)                # url + title + content-hash

Run from repo root, inside venv `falseclaim`:
    python finetune/collect_sources.py
    # paths are anchored to the script, so launching from elsewhere also works

Env knobs (all optional):
    ROSTER=claim_roster.json   OUT=labeled_sources_v2.json   CKPT=collect_checkpoint.json
    CONCURRENCY=3              RETRIES=3

Resumable: per-claim results are checkpointed to disk after each claim. Re-running
skips done claims and re-attempts only FAILED ones, so an interrupted or partial run
costs nothing. Delete a claim's checkpoint entry to force a fresh re-collect of it.
"""

import os
import sys
import json
import time
import random
import asyncio

# --- repo layout anchored to THIS file, so it runs from any working directory ---
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))   # .../finetune
_REPO_ROOT = os.path.dirname(_SCRIPT_DIR)                  # repo root (parent of finetune/)
# put repo root on sys.path so `app.*` resolves no matter where you launch from
for _p in (_REPO_ROOT, _SCRIPT_DIR, os.getcwd()):
    if _p not in sys.path:
        sys.path.insert(0, _p)

# importing claim_service triggers nli_service, which eager-loads DeBERTa + MiniLM
from app.models.schemas import ClaimRequest, Source  # noqa: E402
from app.services.claim_service import (              # noqa: E402
    search_sources,
    _filter_relevant_sources,
    _deduplicate_sources,
)
from app.services.claim_classifier import classify_claim_domain  # noqa: E402
from app.services.source_router import build_routing_config      # noqa: E402

# ---------------- config ----------------
# roster lives at repo root; outputs land next to this script (finetune/)
ROSTER_PATH = os.environ.get("ROSTER", os.path.join(_REPO_ROOT, "claim_roster.json"))
OUT_PATH = os.environ.get("OUT", os.path.join(_SCRIPT_DIR, "labeled_sources.json"))
CKPT_PATH = os.environ.get("CKPT", os.path.join(_SCRIPT_DIR, "collect_checkpoint.json"))
MAX_CONCURRENCY = int(os.environ.get("CONCURRENCY", "3"))
MAX_RETRIES = int(os.environ.get("RETRIES", "3"))

# stance_method is routing intent, derived purely from source_type (matches existing data 100%)
_STANCE_METHOD = {"fact_check": "factcheck_rating", "knowledge_graph": "wikidata_bypass"}


def stance_method_for(source_type: str) -> str:
    return _STANCE_METHOD.get(source_type, "sentence_nli")


def to_record(source: Source, claim: str, split: str, category: str) -> dict:
    """Source -> labeled_sources record. The first 10 keys reproduce the existing
    schema exactly; url/split/category are additive so this file is self-contained."""
    title = source.title or ""
    snippet = source.snippet or ""
    tps = f"{title}. {snippet}" if (title and snippet) else (title or snippet)
    return {
        "claim": claim,
        "source_title": title,
        "source_type": source.source_type,
        "stance_method": stance_method_for(source.source_type),
        "title_only": title,
        "snippet_only": snippet,
        "title_plus_snippet": tps,
        "full_content": "",        # production pipeline does not surface full text
        "is_contaminated": False,  # not labeled at collection (not the fine-tune lever)
        "pipeline_stance": None,   # NLI not run at collection time
        # --- additive: self-contained single source of truth ---
        "url": source.url,
        "split": split,
        "category": category,
    }


def load_json(path, default):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return default


def save_json(path, obj, indent=None):
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(obj, f, ensure_ascii=False, indent=indent)
    os.replace(tmp, path)  # atomic, so a kill mid-write can't corrupt the file


async def collect_one(entry: dict, sem: asyncio.Semaphore, ckpt: dict, lock: asyncio.Lock):
    claim = entry["claim"]
    split = entry.get("split", "")
    category = entry.get("category", "")
    async with sem:
        last_err = None
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                req = ClaimRequest(claim=claim)
                domain = classify_claim_domain(claim)
                rc = build_routing_config(domain, claim)

                raw = await search_sources(req, rc)        # real, async, 6 APIs
                raw = _filter_relevant_sources(claim, raw)  # real MiniLM relevance
                raw = _deduplicate_sources(raw)             # real 3-layer dedup

                records = [to_record(s, claim, split, category) for s in raw]

                by_type = {}
                for r in records:
                    by_type[r["source_type"]] = by_type.get(r["source_type"], 0) + 1

                if len(records) == 0:
                    raise RuntimeError("zero sources after filter/dedup")

                academic_enabled = (
                    rc.get("semantic_scholar", {}).get("enabled", True)
                    or rc.get("open_alex", {}).get("enabled", True)
                )
                flags = []
                if academic_enabled and by_type.get("academic", 0) == 0:
                    flags.append("no_academic_despite_enabled")

                async with lock:
                    ckpt[claim] = {
                        "records": records, "by_type": by_type,
                        "domain": domain, "flags": flags, "attempt": attempt,
                    }
                    save_json(CKPT_PATH, ckpt)
                print(f"[DONE] {claim[:55]!r}: {len(records)} src {by_type} flags={flags}")
                return
            except Exception as e:  # noqa: BLE001 - we want to retry on anything transient
                last_err = e
                wait = (2 ** attempt) + random.random()
                print(f"[RETRY {attempt}/{MAX_RETRIES}] {claim[:55]!r}: {e} (sleep {wait:.1f}s)")
                await asyncio.sleep(wait)

        async with lock:
            ckpt[claim] = {"records": [], "by_type": {}, "flags": ["FAILED"], "error": str(last_err)}
            save_json(CKPT_PATH, ckpt)
        print(f"[FAILED] {claim[:55]!r}: {last_err}")


def report(roster, ckpt):
    print("\n" + "=" * 60 + "\nCOLLECTION REPORT\n" + "=" * 60)
    by_type_total, counts, failed, no_acad = {}, [], [], []
    for e in roster:
        c = e["claim"]
        rec = ckpt.get(c)
        if not rec:
            failed.append(c)
            continue
        if rec.get("flags") == ["FAILED"]:
            failed.append(c)
            continue
        n = len(rec["records"])
        counts.append(n)
        for st, k in rec["by_type"].items():
            by_type_total[st] = by_type_total.get(st, 0) + k
        if "no_academic_despite_enabled" in rec.get("flags", []):
            no_acad.append(c)
    total = sum(counts)
    print(f"claims done: {len(counts)}/{len(roster)}  |  total sources: {total}")
    if counts:
        counts.sort()
        print(f"sources/claim: min {counts[0]}  max {counts[-1]}  mean {total/len(counts):.1f}")
    print("by source_type:", by_type_total)
    print(f"\nFAILED (re-run to retry): {len(failed)}")
    for c in failed:
        print("   ", repr(c[:70]))
    print(f"\nflagged no_academic_despite_enabled (eyeball, may be real or a 429 miss): {len(no_acad)}")
    for c in no_acad:
        print("   ", repr(c[:70]))


async def main():
    roster = load_json(ROSTER_PATH, [])
    if not roster:
        print(f"[FATAL] no roster at {ROSTER_PATH}")
        return
    ckpt = load_json(CKPT_PATH, {})

    def needs_work(e):
        c = e["claim"]
        return (c not in ckpt) or (ckpt[c].get("flags") == ["FAILED"])

    todo = [e for e in roster if needs_work(e)]
    print(f"[START] roster={len(roster)}  in_checkpoint={len(ckpt)}  to_do={len(todo)}  "
          f"concurrency={MAX_CONCURRENCY}")

    sem = asyncio.Semaphore(MAX_CONCURRENCY)
    lock = asyncio.Lock()
    t0 = time.time()
    await asyncio.gather(*(collect_one(e, sem, ckpt, lock) for e in todo))
    print(f"\n[COLLECT] finished in {time.time()-t0:.0f}s")

    # assemble one file in roster order
    all_records = []
    for e in roster:
        rec = ckpt.get(e["claim"])
        if rec and rec.get("records"):
            all_records.extend(rec["records"])
    save_json(OUT_PATH, all_records, indent=2)
    print(f"[WRITE] {len(all_records)} records -> {OUT_PATH}")
    report(roster, ckpt)


if __name__ == "__main__":
    asyncio.run(main())