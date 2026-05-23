import asyncio
import heapq
import re
from app.models.schemas import ClaimRequest, SourceResult, ClaimResponse, Source
from app.services.google_factcheck import search_factcheck
from app.services.wikipedia import search_wikipedia
from app.services.semantic_scholar import search_semantic_scholar
from app.services.open_alex import search_openalex
from app.services.duckduckgo import search_duckduckgo
from app.services.wikidata import search_wikidata
from app.services.nli_service import classify_stance, compute_relevance
from app.services.credibility_service import score_all_sources


# Each known fact-checker rating → (polarity, confidence)
# Confidence reflects how definitive that specific rating is.
# Sources: PolitiFact, Snopes, AFP, Reuters, WaPo, Full Fact, AP
RATING_LOOKUP = {
    # --- NEGATIVE: fact-checker says claim is false/misleading ---
    # PolitiFact scale
    "pants on fire":    ("negative", 0.99),
    "false":            ("negative", 0.95),
    "mostly false":     ("negative", 0.85),
    "half true":        ("negative", 0.55),  # borderline, barely counts
    "barely true":      ("negative", 0.80),
    # Snopes scale
    "mixture":          ("negative", 0.55),  # borderline, like half true
    "unproven":         ("negative", 0.70),
    "miscaptioned":     ("negative", 0.80),
    "misattributed":    ("negative", 0.80),
    "outdated":         ("negative", 0.70),
    "legend":           ("negative", 0.80),
    "satire":           ("negative", 0.80),
    # AFP scale
    "fabricated":       ("negative", 0.95),
    "altered":          ("negative", 0.85),
    "manipulated":      ("negative", 0.85),
    "partly false":     ("negative", 0.80),
    # Reuters / shared
    "misleading":       ("negative", 0.75),
    "missing context":  ("negative", 0.65),
    "lacks context":    ("negative", 0.65),
    "needs context":    ("negative", 0.65),
    "no evidence":      ("negative", 0.80),
    # WaPo scale
    "four pinocchios":  ("negative", 0.95),
    "three pinocchios": ("negative", 0.85),
    "two pinocchios":   ("negative", 0.65),
    # Generic negative (used across orgs or in freeform ratings)
    "incorrect":        ("negative", 0.95),
    "inaccurate":       ("negative", 0.95),
    "fake":             ("negative", 0.95),
    "wrong":            ("negative", 0.95),
    "not true":         ("negative", 0.95),
    "not correct":      ("negative", 0.95),
    "not accurate":     ("negative", 0.95),
    "debunked":         ("negative", 0.95),
    "unfounded":        ("negative", 0.90),
    "baseless":         ("negative", 0.90),
    "unsupported":      ("negative", 0.80),
    "flawed":           ("negative", 0.75),
    "distorts":         ("negative", 0.75),
    "exaggerated":      ("negative", 0.70),
    # --- POSITIVE: fact-checker says claim is true ---
    # PolitiFact / Snopes / Reuters
    "true":             ("positive", 0.95),
    "mostly true":      ("positive", 0.85),
    # WaPo
    "one pinocchio":    ("positive", 0.75),
    # Generic positive
    "correct":          ("positive", 0.95),
    "accurate":         ("positive", 0.95),
    "confirmed":        ("positive", 0.95),
    "mostly correct":   ("positive", 0.85),
}

NON_CONTENT_PATTERNS = [
    "(film)", "(movie)", "(song)", "(album)", "(tv series)",
    "(advertisement)", "(disambiguation)", "(video game)",
    "(band)", "(novel)", "(book)", "(magazine)",
]


def _is_non_content(title: str) -> bool:
    title_lower = title.lower()
    # Matches "(film)", "(2001 film)", "(TV series)", "(2024 movie)", etc.
    if re.search(r'\(\d{0,4}\s*(film|movie|song|album|tv series|advertisement|disambiguation|video game|band|novel|book|magazine)\)', title_lower):
        return True
    return False


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


def _extract_rating_label(rating: str) -> str:
    """Extract the verdict label from a rating string.

    Handles: "False" → "false"
             "false. the images were taken..." → "false"
             "FALSE" → "false"
    """
    r = rating.lower().strip()
    # Split on separators between label and explanation
    for sep in [". ", ", ", ": ", " - ", " — "]:
        if sep in r:
            r = r[:r.index(sep)].strip()
            break
    return r.rstrip(".,:;")


def _classify_rating(rating: str) -> tuple[str, float]:
    """Classify a fact-check rating into (polarity, confidence).

    1. Extract label portion, exact match against known scales
    2. Substring fallback on full text (longest match first so
       'not true' beats 'true', 'mostly false' beats 'false')
    3. Unknown if nothing matches
    """
    label = _extract_rating_label(rating)

    # Step 1: exact match on extracted label
    if label in RATING_LOOKUP:
        return RATING_LOOKUP[label]

    # Step 2: substring match on full text, longest label first
    r = rating.lower().strip()
    for known in sorted(RATING_LOOKUP, key=len, reverse=True):
        if known in r:
            polarity, conf = RATING_LOOKUP[known]
            return polarity, min(conf, 0.75)  # cap confidence for inferred match

    return "unknown", 0.0


def _stance_from_factcheck(source: Source, claim: str) -> tuple[str | None, float | None]:
    rating = (source.raw_claim_rating or "").lower().strip()
    claim_reviewed = (source.metadata or {}).get("claim_reviewed", "")

    if not claim_reviewed or not rating:
        return None, None

    alignment, alignment_conf = classify_stance(claim_reviewed, claim)

    print(f"[FC-DEBUG] claim_reviewed: '{claim_reviewed}'")
    print(f"[FC-DEBUG] user_claim: '{claim}'")
    print(f"[FC-DEBUG] alignment: {alignment} ({alignment_conf:.2f}) | rating: '{rating}'")

    if alignment == "neutral" or alignment_conf < 0.55:
        return None, None

    rating_polarity, rating_conf = _classify_rating(rating)

    if rating_polarity == "unknown":
        print(f"[FC-BYPASS] rating not recognized, skipping")
        return None, None

    # Case 1: FC claim aligns with (supports) user claim
    # FC reviewed "X causes Y", user asks "X causes Y", rating says false
    # → the claim the user asked about is false → opposing
    if alignment == "supporting":
        if rating_polarity == "negative":
            print(f"[FC-BYPASS] supporting + negative → opposing ({rating_conf})")
            return "opposing", rating_conf
        else:
            print(f"[FC-BYPASS] supporting + positive → supporting ({rating_conf})")
            return "supporting", rating_conf

    # Case 2: FC claim opposes user claim (double-inversion)
    # FC reviewed "climate change is a hoax" (opposes "climate change is real")
    # Rating: "false" → the hoax claim is false → climate change IS real → supporting
    # Guard: high alignment confidence + strong ratings only (conf >= 0.85)
    if alignment == "opposing":
        if alignment_conf < 0.85:
            print(f"[FC-BYPASS] opposing alignment too weak ({alignment_conf:.2f} < 0.85), skipping")
            return None, None
        if rating_polarity == "negative" and rating_conf >= 0.85:
            print(f"[FC-BYPASS] opposing + strong negative → supporting (0.90)")
            return "supporting", 0.90
        elif rating_polarity == "positive" and rating_conf >= 0.85:
            print(f"[FC-BYPASS] opposing + strong positive → opposing (0.90)")
            return "opposing", 0.90
        # Weak/ambiguous rating + opposing alignment → too risky, skip
        print(f"[FC-BYPASS] opposing + weak/ambiguous rating, skipping")
        return None, None

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
        if _is_non_content(source.title):
            print(f"[FILTERED-TYPE] {source.title[:80]}")
            continue
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

        # Wikidata: structured entity data, not suited for NLI
        if source.source_type == "knowledge_graph":
            results.append(
                SourceResult(
                    url=source.url,
                    title=source.title,
                    stance="neutral",
                    stance_confidence=0.0,
                    credibility_tier=cred["credibility_tier"],
                    credibility_score=cred["credibility_score"],
                    bias_rating=cred["bias_rating"],
                    factual_reporting=cred["factual_reporting"],
                    support_summary="Wikidata: excluded from NLI (factual reference only)",
                )
            )
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
             # Bypass couldn't parse the rating - skip entirely
            # Snippet is the false claim text, NLI on it would be wrong
            print(f"[FC-SKIP] Bypass failed, dropping: {source.title[:80]}")
            continue

        # All other sources: NLI on snippet only (not title)
        # Title contains the topic name which misleads NLI into thinking
        # "about X" means "supports X" (e.g. "Flat Earth" article classified as supporting flat earth)
        # Snippet/abstract contains the actual argument, which NLI can classify correctly
        premise = source.snippet if source.snippet else source.title
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

    # Opinion claims: show what sources say, but don't give hard true/false verdict
    if claim_type == "opinion":
        if ratio >= 0.60:
            verdict = "sources lean supporting"
        elif ratio > 0.40:
            verdict = "sources divided"
        else:
            verdict = "sources lean opposing"
        return (verdict, round(confidence, 4))

    # Factual claims: normal verdict
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