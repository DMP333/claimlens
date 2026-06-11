import asyncio
import hashlib
import heapq
import re
from app.models.schemas import ClaimRequest, SourceResult, ClaimResponse, Source
from app.services.google_factcheck import search_factcheck
from app.services.wikipedia import search_wikipedia
from app.services.semantic_scholar import search_semantic_scholar
from app.services.open_alex import search_openalex
from app.services.duckduckgo import search_duckduckgo
from app.services.nli_service import (
    classify_stance,
    classify_stance_sentences,
    classify_stance_sentences_batch,
    compute_relevance,
)
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


def _normalize_title(title: str) -> str:
    """Normalize a title for duplicate comparison.

    Strips punctuation, collapses whitespace, lowercases.
    'Blind Humans Can Develop the Superpower of Bats!'
    -> 'blind humans can develop the superpower of bats'
    """
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9\s]', '', title.lower())).strip()


def _snippet_hash(snippet: str) -> str:
    """Hash the first 200 chars of a snippet for content-based dedup."""
    normalized = re.sub(r'\s+', ' ', snippet.strip()[:200].lower())
    return hashlib.md5(normalized.encode()).hexdigest()


def _dedup_priority(source: Source) -> int:
    """Higher number = higher priority to keep when deduplicating.

    Prefers sources with more metadata signal (citations, credibility info).
    """
    score = 0
    citations = (source.metadata or {}).get("citation_count", 0) or 0
    score += min(citations, 1000)  # cap so one mega-cited paper doesn't dominate
    # Prefer sources with richer snippets
    score += min(len(source.snippet or ""), 500) // 100
    # Prefer fact_check and encyclopedia over raw academic
    if source.source_type == "fact_check":
        score += 2000
    elif source.source_type == "encyclopedia":
        score += 1500
    return score


def _deduplicate_sources(sources: list[Source]) -> list[Source]:
    """Deduplicate sources using three layers:
    1. URL normalization (http vs https, trailing slash)
    2. Title normalization (same paper, different URL)
    3. Content hash (same text, different title/URL)
    """
    unique = []
    seen_urls = {}         # normalized_url -> index in unique[]
    seen_titles = {}      # normalized_title -> index in unique[]
    seen_content = {}     # content_hash -> index in unique[]
    url_dupes = 0
    title_dupes = 0
    content_dupes = 0

    for source in sources:
        # Layer 1: URL dedup
        url_key = re.sub(r'^https?://(www\.)?', '', source.url.rstrip("/").lower())
        if url_key in seen_urls:
            existing_idx = seen_urls[url_key]
            existing = unique[existing_idx]
            if _dedup_priority(source) > _dedup_priority(existing):
                print(f"[DEDUP-URL] replaced: '{existing.title[:60]}' with '{source.title[:60]}' (higher priority)")
                unique[existing_idx] = source
            else:
                print(f"[DEDUP-URL] dropped: {source.title[:80]}")
            url_dupes += 1
            continue
        seen_urls[url_key] = len(unique)

        # Layer 2: Title dedup
        norm_title = _normalize_title(source.title)
        if norm_title and len(norm_title) > 10 and norm_title in seen_titles:
            existing_idx = seen_titles[norm_title]
            existing = unique[existing_idx]
            # Keep the one with higher priority (more citations, richer metadata)
            if _dedup_priority(source) > _dedup_priority(existing):
                print(f"[DEDUP-TITLE] replaced: '{existing.title[:60]}' with '{source.title[:60]}' (higher priority)")
                unique[existing_idx] = source
            else:
                print(f"[DEDUP-TITLE] dropped: '{source.title[:60]}' (lower priority than existing)")
            title_dupes += 1
            continue

        # Layer 3: Content hash dedup
        snippet = source.snippet or ""
        if len(snippet) >= 50:
            content_key = _snippet_hash(snippet)
            if content_key in seen_content:
                existing_idx = seen_content[content_key]
                existing = unique[existing_idx]
                if _dedup_priority(source) > _dedup_priority(existing):
                    print(f"[DEDUP-CONTENT] replaced: '{existing.title[:60]}' with '{source.title[:60]}'")
                    unique[existing_idx] = source
                else:
                    print(f"[DEDUP-CONTENT] dropped: '{source.title[:60]}'")
                content_dupes += 1
                continue
            seen_content[content_key] = len(unique)

        # No duplicate found, keep it
        if norm_title and len(norm_title) > 10:
            seen_titles[norm_title] = len(unique)
        unique.append(source)

    total_dropped = url_dupes + title_dupes + content_dupes
    print(f"[DEDUP] {len(sources)} -> {len(unique)} (dropped {total_dropped}: {url_dupes} url, {title_dupes} title, {content_dupes} content)")
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
        if text == "":
            print(f"[FILTERED-EMPTY] no title or snippet | {source.url[:80]}")
            continue
        if score >= RELEVANCE_THRESHOLD:
            filtered.append(source)
        else:
            print(f"[FILTERED] {score:.2f} | {source.title[:80]}")

    print(f"[RELEVANCE] {len(sources)} sources -> {len(filtered)} after filtering")
    return filtered


# Display order for the response source list: supporting first, then opposing.
# Neutral is dropped in _present_sources, so its rank only matters if neutral
# is ever re-included in the output later.
_STANCE_RANK = {"supporting": 0, "opposing": 1, "neutral": 2}


def _present_sources(sources: list[SourceResult]) -> list[SourceResult]:
    """Shape the analyzed sources for the API response.

    Drops neutral sources: they contribute nothing to the verdict (compute_verdict
    already skips them) and a stanceless source does not serve a show-both-sides
    output. Then groups by stance (supporting, then opposing) and sorts by
    credibility descending within each group. Pure function, no I/O.
    """
    visible = [s for s in sources if s.stance != "neutral"]
    visible.sort(key=lambda s: (_STANCE_RANK.get(s.stance, 99), -s.credibility_score))
    return visible


async def analyze_claim(request: ClaimRequest) -> ClaimResponse:
    import time
    from app.services.claim_classifier import classify_claim_type, classify_claim_domain
    from app.services.source_router import build_routing_config

    t0 = time.perf_counter()
    claim_type, claim_type_confidence = classify_claim_type(request.claim)
    claim_domain = classify_claim_domain(request.claim)
    routing_config = build_routing_config(claim_domain, request.claim)
    t_classify = time.perf_counter()
    print(f"[CLAIM] type={claim_type} ({claim_type_confidence:.2f}) | domain={claim_domain}")

    raw_sources = await search_sources(request, routing_config)
    t_search = time.perf_counter()

    raw_sources = await asyncio.to_thread(_filter_relevant_sources, request.claim, raw_sources)
    t_relevance = time.perf_counter()
    raw_sources = _deduplicate_sources(raw_sources)
    t_dedup = time.perf_counter()

    analyzed_sources = await analyze_sources(request.claim, raw_sources)
    t_nli = time.perf_counter()

    verdict, confidence_in_verdict = compute_verdict(analyzed_sources, claim_type)
    t_end = time.perf_counter()

    print(
        f"[TIMING] classify={t_classify-t0:.2f} search={t_search-t_classify:.2f} "
        f"relevance={t_relevance-t_search:.2f} dedup={t_dedup-t_relevance:.2f} "
        f"nli={t_nli-t_dedup:.2f} verdict={t_end-t_nli:.2f} "
        f"| model_locked(relevance+nli)={(t_relevance-t_search)+(t_nli-t_dedup):.2f} "
        f"TOTAL={t_end-t0:.2f}"
    )
    return ClaimResponse(
        claim=request.claim,
        claim_type=claim_type,
        claim_type_confidence=claim_type_confidence,
        claim_domain=claim_domain,
        verdict=verdict,
        confidence_in_verdict=confidence_in_verdict,
        sources=_present_sources(analyzed_sources),
    )


# Per-source network timeout. One slow/hanging API is dropped after this many
# seconds instead of stalling the whole request. Tune as needed.
SOURCE_TIMEOUT_SECONDS = 10.0


async def search_sources(request: ClaimRequest, routing_config: dict | None = None) -> list[Source]:
    rc = routing_config or {}

    # Build list of (name, coroutine) pairs, skipping disabled sources
    tasks = []
    task_names = []

    source_calls = {
        "google_factcheck": lambda cfg: search_factcheck(request),
        "wikipedia":        lambda cfg: search_wikipedia(request),
        "semantic_scholar":  lambda cfg: search_semantic_scholar(request, cfg),
        "open_alex":        lambda cfg: search_openalex(request, cfg),
        "duckduckgo":       lambda cfg: search_duckduckgo(request),
    }

    for name, call_fn in source_calls.items():
        cfg = rc.get(name, {})
        if not cfg.get("enabled", True):
            print(f"[SKIP] {name} (disabled by routing)")
            continue
        tasks.append(asyncio.wait_for(call_fn(cfg), timeout=SOURCE_TIMEOUT_SECONDS))
        task_names.append(name)

    results = await asyncio.gather(*tasks, return_exceptions=True)

    all_sources = []
    for name, result in zip(task_names, results):
        if isinstance(result, Exception):
            print(f"[ERROR] {name}: {result}")
        else:
            print(f"[OK] {name}: {len(result)} sources")
            all_sources.extend(result)

    return all_sources


async def analyze_sources(claim: str, raw_sources: list[Source]) -> list[SourceResult]:
    credibility_results = await score_all_sources(raw_sources)

    # Pass 1: route each source. Fact-check sources resolve immediately via
    # the rating bypass (unchanged). All other sources are COLLECTED instead
    # of classified one-by-one, so their sentence pairs can share one GPU run.
    entries: list[tuple[int, SourceResult]] = []   # (original index, result)
    nli_jobs: list[tuple[int, Source, dict, str]] = []  # (idx, source, cred, premise)

    for idx, (source, cred) in enumerate(zip(raw_sources, credibility_results)):
        if not source.snippet:
            continue

        # Fact-check sources: use rating instead of NLI on snippet
        if source.source_type == "fact_check" and source.raw_claim_rating:
            fc_stance, fc_conf = await asyncio.to_thread(_stance_from_factcheck, source, claim)
            if fc_stance:
                entries.append((idx,
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
                ))
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
        nli_jobs.append((idx, source, cred, premise))

    # Pass 2: ONE cross-source batched inference for every collected premise.
    # Same sentences, same model, same aggregation as the per-source path;
    # only the GPU batching granularity changes (claim-level, not source-level).
    if nli_jobs:
        premises = [premise for _, _, _, premise in nli_jobs]
        batch_results = await asyncio.to_thread(
            classify_stance_sentences_batch, premises, claim
        )
        for (idx, source, cred, _), (stance, confidence, sent_details) in zip(
            nli_jobs, batch_results
        ):
            entries.append((idx,
                SourceResult(
                    url=source.url,
                    title=source.title,
                    stance=stance,
                    stance_confidence=confidence,
                    credibility_tier=cred["credibility_tier"],
                    credibility_score=cred["credibility_score"],
                    bias_rating=cred["bias_rating"],
                    factual_reporting=cred["factual_reporting"],
                    support_summary=f"Sentence-NLI: {stance} ({confidence:.2f}, {len(sent_details)} sents)",
                )
            ))

    # Restore original source order (FC and NLI results interleave as before).
    entries.sort(key=lambda pair: pair[0])
    return [result for _, result in entries]


# How much total weighted evidence is "a lot." Higher = more sources/strength
# needed before confidence saturates. Tune against real runs.
EVIDENCE_SATURATION_K = 2.0


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

    # Confidence = how lopsided (direction) x how much credible evidence (mass).
    # Thin or weak evidence can no longer score 1.0 just by being unanimous.
    direction = abs(ratio - 0.5) * 2
    evidence_factor = total / (total + EVIDENCE_SATURATION_K)
    confidence = round(direction * evidence_factor, 4)

    # Opinion claims: show what sources say, but don't give hard true/false verdict
    if claim_type == "opinion":
        if ratio >= 0.60:
            verdict = "sources lean supporting"
        elif ratio > 0.40:
            verdict = "sources divided"
        else:
            verdict = "sources lean opposing"
        return (verdict, confidence)

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

    return (verdict, confidence)