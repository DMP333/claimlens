import csv
import os
from urllib.parse import urlparse
import httpx
from app.core.config import settings
from app.models.schemas import Source

MBFC_DATA = {}
OPENPAGERANK_URL = "https://openpagerank.com/api/v1.0/getPageRank"

FACTUAL_SCORE_MAP = {
    "very high": 0.95,
    "high": 0.85,
    "mostly factual": 0.75,
    "mixed": 0.50,
    "low": 0.25,
    "very low": 0.10,
}

#TODO: set up automated MBFC data refresh (idiap scraper + GitHub Action)


def _load_mbfc_data():
    csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "mbfc_raw.csv")
    with open(csv_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            domain = row["source"].strip().lower()
            MBFC_DATA[domain] = {
                "bias": row.get("bias", "").strip(),
                "factual_reporting": row.get("factual_reporting", "").strip(),
            }

_load_mbfc_data()


def _extract_domain(url: str) -> str:
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.lower()
        if domain.startswith("www."):
            domain = domain[4:]
        return domain
    except Exception:
        return ""


def _check_mbfc(domain: str) -> dict | None:
    if domain in MBFC_DATA:
        entry = MBFC_DATA[domain]
        factual = entry["factual_reporting"].lower()
        score = FACTUAL_SCORE_MAP.get(factual, 0.50)
        return {
            "credibility_tier": "verified",
            "credibility_score": score,
            "bias_rating": entry["bias"],
            "factual_reporting": entry["factual_reporting"],
        }
    return None


def _score_academic(source: Source) -> float:
    citations = (source.metadata or {}).get("citation_count", 0) or 0
    if citations >= 1000:
        return 0.95
    elif citations >= 100:
        return 0.80
    elif citations >= 10:
        return 0.65
    elif citations >= 1:
        return 0.55
    return 0.40


def _score_wikipedia(source: Source) -> float:
    meta = source.metadata or {}
    if meta.get("is_featured"):
        return 0.95
    if meta.get("is_good"):
        return 0.90
    length = meta.get("article_length", 0) or 0
    if length >= 50000:
        return 0.85
    elif length >= 15000:
        return 0.80
    elif length >= 5000:
        return 0.70
    return 0.55


async def _batch_openpagerank(domains: list[str]) -> dict[str, float]:
    if not domains or not settings.OPEN_PAGE_RANK_KEY:
        return {}

    results = {}
    #TODO: handle pagination if more than 100 domains
    batch = domains[:100]
    params = [("domains[]", d) for d in batch]
    headers = {"API-OPR": settings.OPEN_PAGE_RANK_KEY}

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(OPENPAGERANK_URL, params=params, headers=headers)

        if response.status_code != 200:
            return {}

        data = response.json()
        for item in data.get("response", []):
            if item.get("status_code") == 200:
                domain = item.get("domain", "")
                page_rank = item.get("page_rank_decimal", 0)
                results[domain] = page_rank / 10.0
    except Exception:
        return {}

    return results


async def score_all_sources(sources: list[Source]) -> list[dict]:
    source_domains = [_extract_domain(s.url) for s in sources]

    mbfc_results = {}
    unknown_domains = []

    for domain in set(source_domains):
        if not domain:
            continue
        mbfc = _check_mbfc(domain)
        if mbfc:
            mbfc_results[domain] = mbfc
        else:
            unknown_domains.append(domain)

    opr_scores = await _batch_openpagerank(unknown_domains)

    results = []
    for source, domain in zip(sources, source_domains):
        # Tier 1: MBFC verified
        if domain in mbfc_results:
            results.append(mbfc_results[domain])
            continue

        # Tier 2: source-type-specific with dynamic scoring
        if source.source_type == "academic":
            results.append({
                "credibility_tier": "estimated",
                "credibility_score": _score_academic(source),
                "bias_rating": None,
                "factual_reporting": None,
            })
            continue

        if source.source_type == "encyclopedia":
            results.append({
                "credibility_tier": "estimated",
                "credibility_score": _score_wikipedia(source),
                "bias_rating": None,
                "factual_reporting": None,
            })
            continue

        if source.source_type == "fact_check":
            results.append({
                "credibility_tier": "estimated",
                "credibility_score": 0.85,
                "bias_rating": None,
                "factual_reporting": None,
            })
            continue

        # Tier 2: OpenPageRank for web sources
        if domain in opr_scores and opr_scores[domain] > 0:
            results.append({
                "credibility_tier": "estimated",
                "credibility_score": max(opr_scores[domain], 0.20),
                "bias_rating": None,
                "factual_reporting": None,
            })
            continue

        # Tier 3: unverified
        results.append({
            "credibility_tier": "unverified",
            "credibility_score": 0.30,
            "bias_rating": None,
            "factual_reporting": None,
        })

    return results