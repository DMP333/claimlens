"""
Source routing: configures each API based on claim domain and content.

Given a claim's domain classification and text, produces a configuration
dict that tells each source API: whether to run, how many results to fetch,
what field filters to apply, and any query modifications.

Usage:
    from app.services.source_router import build_routing_config
    config = build_routing_config(claim_domain, claim_text)
    # config["semantic_scholar"]["enabled"] -> True/False
    # config["semantic_scholar"]["field_filters"] -> ["Biology", "Medicine"]
    # config["wikipedia"]["max_results"] -> 5
"""

import re


# =============================================================
# Academic field keyword mapping
#
# Maps claim keywords to Semantic Scholar field-of-study names.
# When a claim contains keywords from a field, that field gets
# included in the API query filter. Top 2 fields are selected
# for cross-disciplinary coverage.
# =============================================================

_BIOLOGY_KEYWORDS = {
    "species", "animal", "animals", "mammal", "insect", "bird", "birds",
    "gene", "genes", "genetic", "dna", "rna", "evolution", "evolve",
    "cell", "cells", "organism", "photosynthesis", "ecosystem", "biodiversity",
    "bat", "bats", "spider", "spiders", "shark", "whale",
    "goldfish", "lemming", "lemmings", "ostrich", "chameleon",
    "dog", "dogs", "cat", "cats", "chimpanzee", "chimpanzees", "primate",
    "blind", "deaf", "taste", "smell", "vision", "hearing",
    "tongue", "eye", "eyes", "feather", "egg", "nest",
    "swallow", "digest", "hibernate",
}

_MEDICINE_KEYWORDS = {
    "vaccine", "vaccines", "vaccination",
    "virus", "viral", "bacteria", "bacterial",
    "disease", "diseases", "cancer", "tumor",
    "health", "healthy", "unhealthy",
    "medicine", "medical", "drug", "drugs", "pharmaceutical",
    "symptom", "symptoms", "treatment", "cure", "diagnosis",
    "autism", "disorder", "syndrome", "infection",
    "antibiotic", "antibiotics", "cholesterol",
    "sugar", "nutrition", "diet", "dietary",
    "arthritis", "joint", "knuckle", "knuckles",
    "heart", "lung", "lungs", "liver", "kidney", "skin",
    "caffeine", "coffee", "alcohol", "smoking", "cigarette", "tobacco",
    "anxiety", "depression",
    "calorie", "calories", "protein", "fat",
    "eyesight", "carrot", "carrots",
    "msg", "glutamate",
    "detox", "toxin", "toxins",
    "organic",  # in food context
}

_PHYSICS_KEYWORDS = {
    "light", "gravity", "atom", "atoms", "energy",
    "temperature", "boil", "boils", "boiling",
    "freeze", "freezes", "freezing", "melt", "melting",
    "radiation", "quantum", "particle", "molecule",
    "speed", "velocity", "force", "mass", "weight",
    "magnetic", "electric", "nuclear", "fission", "fusion",
    "sound", "wave", "frequency", "lightning",
    "heat", "thermal", "celsius", "fahrenheit",
}

_ENVIRO_KEYWORDS = {
    "climate", "atmosphere", "ozone", "carbon", "greenhouse",
    "pollution", "ocean", "glacier", "rainforest", "deforestation",
    "oxygen", "earth", "environment", "environmental",
    "sea", "ice", "arctic", "antarctic", "antarctica",
    "fossil", "renewable", "solar",
}

_PSYCHOLOGY_KEYWORDS = {
    "brain", "brains", "memory", "cognitive", "sleep", "sleeping",
    "behavior", "behavioural", "hyperactive", "hyperactivity",
    "stress", "meditation", "iq", "intelligence",
    "mental", "psychology", "psychological",
    "violence", "violent", "aggression",
}

_ECONOMICS_KEYWORDS = {
    "economy", "economic", "recession", "inflation", "deflation",
    "gdp", "unemployment", "employment",
    "wage", "wages", "salary", "income", "poverty",
    "trade", "market", "stock", "tariff",
    "immigration", "manufacturing", "automation",
    "cryptocurrency", "bitcoin",
}

_POLISCI_KEYWORDS = {
    "election", "vote", "voting", "congress", "senate",
    "parliament", "legislation", "policy", "regulation",
    "government", "democracy", "democratic",
    "surveillance", "crime", "criminal",
    "capitalism", "socialism", "communism",
}

_FIELD_MAP = {
    "Biology": _BIOLOGY_KEYWORDS,
    "Medicine": _MEDICINE_KEYWORDS,
    "Physics": _PHYSICS_KEYWORDS,
    "Environmental Science": _ENVIRO_KEYWORDS,
    "Psychology": _PSYCHOLOGY_KEYWORDS,
    "Economics": _ECONOMICS_KEYWORDS,
    "Political Science": _POLISCI_KEYWORDS,
}


def _get_academic_fields(claim: str) -> list[str] | None:
    """Determine which academic fields are relevant to a claim.

    Returns the top 2 matching fields (for cross-disciplinary coverage),
    or None if no fields match (meaning academic sources should be skipped
    or queried without field filters).
    """
    words = set(
        re.sub(r'[.,!?;:\'"()\[\]]', '', w.lower()) for w in claim.split()
    )

    field_scores: dict[str, int] = {}
    for field_name, keywords in _FIELD_MAP.items():
        overlap = len(words & keywords)
        if overlap > 0:
            field_scores[field_name] = overlap

    if not field_scores:
        return None

    sorted_fields = sorted(field_scores.items(), key=lambda x: -x[1])
    return [field for field, _ in sorted_fields[:2]]


# =============================================================
# Routing config builder
# =============================================================

# Default config: what each source gets when no routing is applied
_DEFAULTS = {
    "google_factcheck": {"enabled": True, "max_results": 10},
    "wikipedia":        {"enabled": True, "max_results": 5},
    "semantic_scholar":  {"enabled": True, "max_results": 10, "field_filters": None},
    "open_alex":        {"enabled": True, "max_results": 10, "field_filters": None},
    "duckduckgo":       {"enabled": True, "max_results": 10},
    "wikidata":         {"enabled": True},
}


def build_routing_config(claim_domain: str, claim_text: str) -> dict:
    """Build per-source API configuration based on claim domain and content.

    Args:
        claim_domain: one of "scientific", "historical", "current_events",
                      "statistical", "general"
        claim_text: the raw claim text (used for keyword-to-field mapping)

    Returns:
        Dict with per-source configuration. Each source key maps to a dict with:
          - enabled: bool (whether to query this source)
          - max_results: int (how many results to request)
          - field_filters: list[str] | None (academic field-of-study filters)
    """
    # Start with defaults
    config = {k: dict(v) for k, v in _DEFAULTS.items()}

    # -- SCIENTIFIC claims --
    # Academic sources get field filtering. Wikipedia is useful.
    # Wikidata useful for structured facts (height, temperature, etc.)
    if claim_domain == "scientific":
        fields = _get_academic_fields(claim_text)
        if fields:
            config["semantic_scholar"]["field_filters"] = fields
            config["open_alex"]["field_filters"] = fields
        # Reduce academic results since they're now filtered (higher quality, fewer needed)
        config["semantic_scholar"]["max_results"] = 7
        config["open_alex"]["max_results"] = 7

    # -- HISTORICAL claims --
    # Wikipedia and Wikidata are primary. Academic sources deprioritized.
    # DDG still useful for debunking articles.
    elif claim_domain == "historical":
        config["wikipedia"]["max_results"] = 7  # more Wikipedia results for historical
        config["semantic_scholar"]["max_results"] = 5
        config["open_alex"]["max_results"] = 5
        fields = _get_academic_fields(claim_text)
        if fields:
            config["semantic_scholar"]["field_filters"] = fields
            config["open_alex"]["field_filters"] = fields
        else:
            # Historical claims without specific academic keywords
            # Use History field or disable academic
            config["semantic_scholar"]["field_filters"] = ["History"]
            config["open_alex"]["field_filters"] = ["History"]

    # -- CURRENT EVENTS claims --
    # DDG and FC are primary (recent web content). Academic sources
    # filtered to relevant fields if available.
    elif claim_domain == "current_events":
        config["duckduckgo"]["max_results"] = 10
        config["semantic_scholar"]["max_results"] = 5
        config["open_alex"]["max_results"] = 5
        fields = _get_academic_fields(claim_text)
        if fields:
            config["semantic_scholar"]["field_filters"] = fields
            config["open_alex"]["field_filters"] = fields

    # -- STATISTICAL claims --
    # All sources useful. Academic sources might need Economics/Mathematics.
    elif claim_domain == "statistical":
        fields = _get_academic_fields(claim_text)
        if fields:
            config["semantic_scholar"]["field_filters"] = fields
            config["open_alex"]["field_filters"] = fields

    # -- GENERAL / OPINION claims --
    # For opinion claims: skip academic entirely (academic papers don't
    # answer opinion questions). For general: query everything normally.
    elif claim_domain == "general":
        # Check if claim was classified as opinion
        # If it's opinion with no academic field match, skip academic
        fields = _get_academic_fields(claim_text)
        if not fields:
            config["semantic_scholar"]["enabled"] = False
            config["open_alex"]["enabled"] = False

    return config