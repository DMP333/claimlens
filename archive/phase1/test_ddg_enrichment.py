"""
Quick test to verify DDG enrichment is working.
Run from project root with venv activated:
    python test_ddg_enrichment.py
"""
import asyncio
from app.models.schemas import ClaimRequest
from app.services.duckduckgo import search_duckduckgo


async def test_claim(claim_text: str):
    print(f"\n{'='*70}")
    print(f"CLAIM: {claim_text}")
    print(f"{'='*70}")

    request = ClaimRequest(claim=claim_text)
    sources = await search_duckduckgo(request)

    for i, source in enumerate(sources):
        enriched = (source.metadata or {}).get("enriched", False)
        ddg_original = (source.metadata or {}).get("ddg_snippet", "")
        tag = "ENRICHED" if enriched else "DDG-FALLBACK"
        snippet_words = len(source.snippet.split())

        print(f"\n--- [{i+1}] [{tag}] {source.title} ---")
        print(f"URL: {source.url}")
        if enriched and ddg_original:
            print(f"DDG ORIGINAL ({len(ddg_original.split())}w):")
            print(f"  {ddg_original}")
        print(f"FINAL SNIPPET ({snippet_words}w):")
        print(f"  {source.snippet}")
        print()


async def main():
    await test_claim("cracking your knuckles causes arthritis")
    print("\n\n")
    await test_claim("lightning never strikes the same place twice")


if __name__ == "__main__":
    asyncio.run(main())