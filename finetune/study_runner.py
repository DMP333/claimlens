"""
Source-utility study, step 1 of 2: the data run.

Drives the FULL production pipeline (retrieval -> relevance -> dedup -> stance)
over all roster claims and records EVERY analyzed source, INCLUDING neutrals
(which the API response hides), tagged with its connector and retrieval rank.
No reimplementation: calls the exact functions analyze_claim calls, in order.

Run INSIDE the app container (model, CUDA, .env all live there):
    docker compose exec app python finetune/study_runner.py

Env knobs (optional):
    ROSTER=claim_roster.json  OUT=finetune/study_results.json
    CKPT=finetune/study_checkpoint.json  CONCURRENCY=2  RETRIES=3

Checkpointed per claim like collect_sources.py: re-running skips done claims
and retries only FAILED ones, so interruptions cost nothing.
"""

import os
import sys
import re
import json
import time
import random
import asyncio
from urllib.parse import urlparse

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.dirname(_SCRIPT_DIR)
for _p in (_REPO_ROOT, _SCRIPT_DIR, os.getcwd()):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from app.models.schemas import ClaimRequest  # noqa: E402
from app.services.claim_service import (  # noqa: E402
    search_sources,
    _filter_relevant_sources,
    _deduplicate_sources,
    analyze_sources,
    compute_verdict,
)
from app.services.claim_classifier import classify_claim_type, classify_claim_domain  # noqa: E402
from app.services.source_router import build_routing_config  # noqa: E402

ROSTER_PATH = os.environ.get("ROSTER", os.path.join(_REPO_ROOT, "claim_roster.json"))
OUT_PATH = os.environ.get("OUT", os.path.join(_SCRIPT_DIR, "study_results.json"))
CKPT_PATH = os.environ.get("CKPT", os.path.join(_SCRIPT_DIR, "study_checkpoint.json"))
MAX_CONCURRENCY = int(os.environ.get("CONCURRENCY", "2"))
MAX_RETRIES = int(os.environ.get("RETRIES", "3"))

# "Sentence-NLI: opposing (1.00, 17 sents)" -> 17
_SENTS_RE = re.compile(r"\([\d.]+, (\d+) sents\)")


def load_json(path, default):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return default


def save_json(path, obj, indent=None):
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(obj, f, ensure_ascii=False, indent=indent)
    os.replace(tmp, path)


async def study_one(entry: dict, sem: asyncio.Semaphore, ckpt: dict, lock: asyncio.Lock):
    claim = entry["claim"]
    async with sem:
        last_err = None
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                req = ClaimRequest(claim=claim)
                claim_type, _ = classify_claim_type(claim)
                domain = classify_claim_domain(claim)
                rc = build_routing_config(domain, claim)

                t0 = time.perf_counter()
                raw = await search_sources(req, rc)
                raw = await asyncio.to_thread(_filter_relevant_sources, claim, raw)
                raw = _deduplicate_sources(raw)
                t_search = time.perf_counter() - t0

                # Rank = position within the connector's own results, in the
                # post-dedup order (mirrors retrieval order). Tagged BEFORE
                # analysis; joined back to results by URL.
                rank_of = {}
                seen_per_type: dict[str, int] = {}
                for s in raw:
                    seen_per_type[s.source_type] = seen_per_type.get(s.source_type, 0) + 1
                    rank_of[s.url] = (s.source_type, seen_per_type[s.source_type])

                t1 = time.perf_counter()
                analyzed = await analyze_sources(claim, raw)
                t_stance = time.perf_counter() - t1

                verdict, vconf = compute_verdict(analyzed, claim_type)

                sources = []
                for r in analyzed:
                    stype, rank = rank_of.get(r.url, ("unknown", -1))
                    m = _SENTS_RE.search(r.support_summary or "")
                    summary = r.support_summary or ""
                    sources.append({
                        "url": r.url,
                        "site": urlparse(r.url).netloc,
                        "title": r.title,
                        "source_type": stype,
                        "rank": rank,
                        "stance": r.stance,
                        "stance_confidence": r.stance_confidence,
                        "credibility_score": r.credibility_score,
                        "credibility_tier": r.credibility_tier,
                        "n_sents": int(m.group(1)) if m else None,
                        "method": "fc_rating" if summary.startswith("Fact-check") else "sentence_nli",
                    })

                record = {
                    "claim": claim,
                    "claim_type": claim_type,
                    "category": entry.get("category", ""),
                    "split": entry.get("split", ""),
                    "verdict": verdict,
                    "verdict_confidence": vconf,
                    "n_sources_analyzed": len(sources),
                    "t_search": round(t_search, 2),
                    "t_stance": round(t_stance, 2),
                    "sources": sources,
                    "attempt": attempt,
                }
                async with lock:
                    ckpt[claim] = record
                    save_json(CKPT_PATH, ckpt)
                print(f"[DONE] {claim[:55]!r}: {len(sources)} src -> {verdict} "
                      f"(search {t_search:.1f}s, stance {t_stance:.1f}s)")
                return
            except Exception as e:  # noqa: BLE001
                last_err = e
                wait = (2 ** attempt) + random.random()
                print(f"[RETRY {attempt}/{MAX_RETRIES}] {claim[:55]!r}: {e} (sleep {wait:.1f}s)")
                await asyncio.sleep(wait)

        async with lock:
            ckpt[claim] = {"claim": claim, "FAILED": True, "error": str(last_err)}
            save_json(CKPT_PATH, ckpt)
        print(f"[FAILED] {claim[:55]!r}: {last_err}")


async def main():
    roster = load_json(ROSTER_PATH, [])
    if not roster:
        print(f"[FATAL] no roster at {ROSTER_PATH}")
        return
    ckpt = load_json(CKPT_PATH, {})

    def needs_work(e):
        rec = ckpt.get(e["claim"])
        return rec is None or rec.get("FAILED")

    todo = [e for e in roster if needs_work(e)]
    print(f"[START] roster={len(roster)} done={len(roster) - len(todo)} to_do={len(todo)} "
          f"concurrency={MAX_CONCURRENCY}")

    sem = asyncio.Semaphore(MAX_CONCURRENCY)
    lock = asyncio.Lock()
    t0 = time.time()
    await asyncio.gather(*(study_one(e, sem, ckpt, lock) for e in todo))
    print(f"\n[RUN] finished in {time.time() - t0:.0f}s")

    results = [ckpt[e["claim"]] for e in roster
               if e["claim"] in ckpt and not ckpt[e["claim"]].get("FAILED")]
    save_json(OUT_PATH, results, indent=2)
    failed = [e["claim"] for e in roster
              if e["claim"] not in ckpt or ckpt[e["claim"]].get("FAILED")]
    print(f"[WRITE] {len(results)} claims -> {OUT_PATH}")
    if failed:
        print(f"[FAILED x{len(failed)}] re-run this script to retry:")
        for c in failed:
            print("   ", repr(c[:70]))


if __name__ == "__main__":
    asyncio.run(main())
