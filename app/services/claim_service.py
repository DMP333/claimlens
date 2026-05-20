import asyncio
import heapq
from app.models.schemas import ClaimRequest, SourceResult, ClaimResponse, Source
from app.services.google_factcheck import search_factcheck
from app.services.wikipedia import search_wikipedia
from app.services.semantic_scholar import search_semantic_scholar
from app.services.open_alex import search_openalex
from app.services.duckduckgo import search_duckduckgo
from app.services.wikidata import search_wikidata
from app.services.nli_service import classify_stance, compute_relevance
from app.services.credibility_service import score_all_sources


NEGATIVE_RATINGS = {"false", "incorrect", "inaccurate", "misleading", "pants on fire",
                    "fake", "wrong", "not true", "unproven", "unsupported",
                    "no evidence", "debunked", "unfounded", "baseless",
                    "flawed", "distorts"}
POSITIVE_RATINGS = {"true", "correct", "accurate", "mostly true", "confirmed"}

def _deduplicate_sources(sources: list[Source]) -> list[Source]:
    #TODO: non-url based duplicate fixing
    seen_urls = set()
    unique = []
    for source in sources:
        url = source.url.rstrip("/").lower()
        if url in seen_urls:
            print(f"[DEDUP] dropped duplicate: {source.title[:80]}")
            continue
        seen_urls.add(url)
        unique.append(source)
    print(f"[DEDUP] {len(sources)} sources -> {len(unique)} after dedup")
    return unique

def _stance_from_factcheck(source: Source, claim: str) -> tuple[str | None, float | None]:
    rating = (source.raw_claim_rating or "").lower().strip()
    claim_reviewed = (source.metadata or {}).get("claim_reviewed", "")

    if not claim_reviewed or not rating:
        return None, None

    alignment, alignment_conf = classify_stance(claim_reviewed, claim)

    print(f"[FC-DEBUG] claim_reviewed: '{claim_reviewed}'")
    print(f"[FC-DEBUG] user_claim: '{claim}'")
    print(f"[FC-DEBUG] alignment: {alignment} ({alignment_conf:.2f}) | rating: '{rating}'")

    if alignment == "neutral" or alignment_conf < 0.70:
        return None, None

    rating_is_negative = any(neg in rating for neg in NEGATIVE_RATINGS)
    rating_is_positive = any(pos in rating for pos in POSITIVE_RATINGS)

    if rating_is_negative:
        if alignment == "supporting":
            return "opposing", 0.95
        elif alignment == "opposing":
            return "supporting", 0.95
    elif rating_is_positive:
        if alignment == "supporting":
            return "supporting", 0.95
        elif alignment == "opposing":
            return "opposing", 0.95

    return None, None

RELEVANCE_THRESHOLD = 0.35 #how relevant the source is suppose to be with the claim

def _filter_relevant_sources(claim: str, sources: list[Source]) -> list[Source]:
    texts = []
    for source in sources:
        if source.title and source.snippet:
            text = f"{source.title}. {source.snippet}"
        else:
            text = source.title or source.snippet or ""
        texts.append(text)

    scores = compute_relevance(claim, texts)

    filtered = []
    for source, text, score in zip(sources, texts, scores):
        if text == "" or score >= RELEVANCE_THRESHOLD:
            filtered.append(source)
        else:
            print(f"[FILTERED] {score:.2f} | {source.title[:80]}")

    print(f"[RELEVANCE] {len(sources)} sources -> {len(filtered)} after filtering")
    return filtered

async def analyze_claim(request: ClaimRequest) -> ClaimResponse:
    from app.services.nli_service import classify_claim_type

    claim_type, claim_type_confidence = classify_claim_type(request.claim)
    raw_sources = await search_sources(request)
    raw_sources = _filter_relevant_sources(request.claim, raw_sources) #filtering added
    raw_sources = _deduplicate_sources(raw_sources) #filter duplicate sources
    analyzed_sources = await analyze_sources(request.claim, raw_sources)
    verdict, confidence_in_verdict = compute_verdict(analyzed_sources, claim_type)
    return ClaimResponse(
        claim=request.claim,
        claim_type=claim_type,
        claim_type_confidence=claim_type_confidence,
        verdict=verdict,
        confidence_in_verdict=confidence_in_verdict,
        sources=analyzed_sources,
    )

async def search_sources(request: ClaimRequest) -> list[Source]:
    service_names = [
        "google_factcheck",
        "wikipedia",
        "semantic_scholar",
        "open_alex",
        "duckduckgo",
        "wikidata",
    ]

    results = await asyncio.gather(
        search_factcheck(request),
        search_wikipedia(request),
        search_semantic_scholar(request),
        search_openalex(request),
        search_duckduckgo(request),
        search_wikidata(request),
        return_exceptions=True,
    )

    all_sources = []
    for name, result in zip(service_names, results):
        if isinstance(result, Exception):
            print(f"[ERROR] {name}: {result}")
        else:
            print(f"[OK] {name}: {len(result)} sources")
            all_sources.extend(result)

    return all_sources

async def analyze_sources(claim: str, raw_sources: list[Source]) -> list[SourceResult]:
    credibility_results = await score_all_sources(raw_sources)

    results = []
    for source, cred in zip(raw_sources, credibility_results):
        if not source.snippet:
            continue

        # Fact-check sources: use rating instead of NLI on snippet
        if source.source_type == "fact_check" and source.raw_claim_rating:
            fc_stance, fc_conf = _stance_from_factcheck(source, claim)
            if fc_stance:
                results.append(
                    SourceResult(
                        url=source.url,
                        title=source.title,
                        stance=fc_stance,
                        stance_confidence=fc_conf,
                        credibility_tier=cred["credibility_tier"],
                        credibility_score=cred["credibility_score"],
                        bias_rating=cred["bias_rating"],
                        factual_reporting=cred["factual_reporting"],
                        support_summary=f"Fact-check: '{source.raw_claim_rating}' (rating-based)",
                    )
                )
                continue

        # All other sources: NLI as usual
        premise = f"{source.title}. {source.snippet}" if source.title else source.snippet
        stance, confidence = classify_stance(premise, claim)

        results.append(
            SourceResult(
                url=source.url,
                title=source.title,
                stance=stance,
                stance_confidence=confidence,
                credibility_tier=cred["credibility_tier"],
                credibility_score=cred["credibility_score"],
                bias_rating=cred["bias_rating"],
                factual_reporting=cred["factual_reporting"],
                support_summary=f"NLI: {stance} ({confidence:.2f})",
            )
        )
    return results

def compute_verdict(source_results_list: list[SourceResult], claim_type: str) -> tuple[str, float]:
    weighted_supporting = 0.0
    weighted_opposing = 0.0

    for source in source_results_list:
        if source.stance == "neutral":
            continue
        if source.stance_confidence < 0.60: #0.6 threshold
            continue
        weight = source.stance_confidence * source.credibility_score
        if source.stance == "supporting":
            weighted_supporting += weight
        elif source.stance == "opposing":
            weighted_opposing += weight

    total = weighted_supporting + weighted_opposing

    if total == 0:
        return ("insufficient evidence", 0.0)

    ratio = weighted_supporting / total
    confidence = abs(ratio - 0.5) * 2

    if ratio >= 0.80:
        verdict = "strongly supported"
    elif ratio >= 0.60:
        verdict = "likely supported"
    elif ratio > 0.40:
        verdict = "contested"
    elif ratio >= 0.20:
        verdict = "likely opposed"
    else:
        verdict = "strongly opposed"

    return (verdict, round(confidence, 4))