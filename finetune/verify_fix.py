"""
Verify the truncation fix on the REAL pipeline before committing to a full recollect.

It drives your actual retrieval route (the same calls collect_sources.py uses), then
splits + filters every source exactly as label_sentences.collect_pairs and the production
stance path now do, and dumps the result so the kept/dropped sentences can be inspected.

PRECONDITION: deploy the patched files FIRST so this exercises the live trim + filter:
    app/services/content_extractor.py   (sentence-boundary trim)
    app/services/nli_service.py          (ends_complete + serve-path filter)

Run from repo root, inside venv `falseclaim`:
    python finetune/verify_fix.py
    VERIFY_CLAIMS="the earth is flat; honey never expires" python finetune/verify_fix.py

Writes finetune/verify_fix_report.json (upload that) and prints a summary.
Non-destructive: it does NOT touch labeled_sources.json or the collect checkpoint.
"""
import os
import sys
import json
import asyncio

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.dirname(_SCRIPT_DIR)
for _p in (_REPO_ROOT, _SCRIPT_DIR, os.getcwd()):
    if _p not in sys.path:
        sys.path.insert(0, _p)

# real pipeline (identical imports to collect_sources.py)
from app.models.schemas import ClaimRequest                       # noqa: E402
from app.services.claim_service import (                          # noqa: E402
    search_sources, _filter_relevant_sources, _deduplicate_sources,
)
from app.services.claim_classifier import classify_claim_domain   # noqa: E402
from app.services.source_router import build_routing_config       # noqa: E402
# the patched splitter + filter (same ones training and serving use)
from app.services.nli_service import split_sentences, ends_complete, DEFAULT_MIN_WORDS  # noqa: E402

SENT_TYPES = {"encyclopedia", "academic", "web"}   # the types collect_pairs labels
OUT = os.path.join(_SCRIPT_DIR, "verify_fix_report.json")

# Three claims that span web / encyclopedia / academic and are prone to clipping.
DEFAULT_CLAIMS = [
    "the great wall of china is visible from space",
    "smoking causes lung cancer",
    "climate change is caused by human activity",
]


def analyze_source(s) -> dict:
    snip = s.snippet or ""
    sents = split_sentences(snip)
    kept, dropped_truncated, dropped_short = [], [], []
    for x in sents:
        if len(x.split()) >= DEFAULT_MIN_WORDS:
            (kept if ends_complete(x) else dropped_truncated).append(x)
        else:
            dropped_short.append(x)
    return {
        "source_type": s.source_type,
        "url": s.url,
        "snippet_words": len(snip.split()),
        "snippet_ends_clean": ends_complete(snip),   # validates the content_extractor trim
        "snippet_tail": snip[-120:],
        "n_sentences": len(sents),
        "kept": kept,                                 # what gets labeled/trained on
        "dropped_truncated": dropped_truncated,       # filter removes these; should look clipped
        "n_dropped_short": len(dropped_short),
    }


async def run_claim(claim: str) -> dict:
    req = ClaimRequest(claim=claim)
    domain = classify_claim_domain(claim)
    rc = build_routing_config(domain, claim)
    raw = await search_sources(req, rc)
    raw = _filter_relevant_sources(claim, raw)
    raw = _deduplicate_sources(raw)
    srcs = [analyze_source(s) for s in raw if s.source_type in SENT_TYPES]
    return {"claim": claim, "domain": domain, "n_sent_sources": len(srcs), "sources": srcs}


async def main():
    env = os.environ.get("VERIFY_CLAIMS")
    claims = [c.strip() for c in env.split(";") if c.strip()] if env else DEFAULT_CLAIMS
    report = []
    for c in claims:
        print(f"[FETCH] {c!r} ...")
        try:
            r = await run_claim(c)
            report.append(r)
            print(f"   {r['n_sent_sources']} web/enc/academic sources")
        except Exception as e:  # noqa: BLE001
            print(f"   [ERR] {e}")
            report.append({"claim": c, "error": str(e)})

    with open(OUT, "w") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    src = kept = dropt = clean = 0
    sanity_bad = []
    for r in report:
        for s in r.get("sources", []):
            src += 1
            kept += len(s["kept"])
            dropt += len(s["dropped_truncated"])
            clean += 1 if s["snippet_ends_clean"] else 0
            sanity_bad += [k for k in s["kept"] if not ends_complete(k)]
    print("\n=== SUMMARY ===")
    print(f"web/enc/academic sources: {src}  |  snippets ending clean: {clean}/{src}")
    print(f"kept sentences: {kept}  |  dropped as truncated by filter: {dropt}")
    print(f"SANITY (kept sentences still truncated, MUST be 0): {len(sanity_bad)}")
    print(f"\nwrote {OUT}  ->  upload this file for verification")


if __name__ == "__main__":
    asyncio.run(main())