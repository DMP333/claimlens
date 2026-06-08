import asyncio
import time
from app.models.schemas import ClaimRequest
from app.services import claim_service
from app.services.claim_classifier import classify_claim_domain
from app.services.source_router import build_routing_config
from app.services.google_factcheck import search_factcheck
from app.services.wikipedia import search_wikipedia
from app.services.semantic_scholar import search_semantic_scholar
from app.services.open_alex import search_openalex
from app.services.duckduckgo import search_duckduckgo
from app.services.wikidata import search_wikidata

CLAIM = "Vaccines cause autism"

async def main():
    req = ClaimRequest(claim=CLAIM)
    domain = classify_claim_domain(CLAIM)
    rc = build_routing_config(domain, CLAIM)

    def cfg(name):
        return rc.get(name, {})

    connectors = [
        ("google_factcheck", lambda: search_factcheck(req)),
        ("wikipedia",        lambda: search_wikipedia(req)),
        ("semantic_scholar", lambda: search_semantic_scholar(req, cfg("semantic_scholar"))),
        ("open_alex",        lambda: search_openalex(req, cfg("open_alex"))),
        ("duckduckgo",       lambda: search_duckduckgo(req)),
        ("wikidata",         lambda: search_wikidata(req)),
    ]
    enabled = [(n, f) for (n, f) in connectors if cfg(n).get("enabled", True)]

    print("\n==== INDIVIDUAL, one at a time ====")
    serial_total = 0.0
    durations = {}
    for name, factory in enabled:
        t = time.perf_counter()
        try:
            count = len(await factory())
        except Exception as e:
            count = f"ERROR {type(e).__name__}"
        d = time.perf_counter() - t
        durations[name] = d
        serial_total += d
        print(f"  {name:18s} {d:6.2f}s   ({count})")
    slowest = max(durations, key=durations.get)
    print(f"  {'SERIAL SUM':18s} {serial_total:6.2f}s")
    print(f"  {'SLOWEST ONE':18s} {durations[slowest]:6.2f}s   ({slowest})")

    print("\n==== GATHER, real pipeline path ====")
    t = time.perf_counter()
    res = await claim_service.search_sources(req, rc)
    gather_total = time.perf_counter() - t
    print(f"  {'search_sources':18s} {gather_total:6.2f}s   ({len(res)} sources)")

    print("\n==== READING ====")
    print("  gather close to SLOWEST ONE means parallel works, that connector is the bottleneck")
    print("  gather close to SERIAL SUM means the gather is NOT parallel (a real bug)\n")

asyncio.run(main())