"""
Claim classification: type (fact vs opinion) and domain routing.

Two independent classifiers:
  - classify_claim_type:   determines verdict framing (factual vs opinion)
  - classify_claim_domain: determines source routing (scientific, historical, etc.)

Approach: keyword/phrase matching + POS tagging for comparative/superlative
detection. DeBERTa zero-shot as optional fallback for ambiguous claims.

Replaces the previous XLM-R-based classify_claim_type in nli_service.py.
"""

import re
from nltk import pos_tag, word_tokenize


# =============================================================
# CLAIM TYPE: factual vs opinion
# =============================================================

# Layer 1a: Multi-word opinion phrases (highest confidence, 0.95)
# Checked via substring match on lowercased claim
_OPINION_PHRASES = [
    # Personal framing
    "i think", "i believe", "in my opinion", "i feel that", "i feel like",
    # Comparative constructions
    "is better than", "is worse than",
    # Superlative constructions
    "is the best", "is the worst", "is the greatest", "is the least",
    "is the most important", "is the most dangerous",
    # Prescriptive
    "should be", "should not be", "shouldn't be", "should have",
    "ought to", "needs to be",
    # Value judgments about belonging/deserving
    "belongs on", "deserves to", "deserves a",
    "is worth", "isn't worth", "is not worth",
    # Evaluative effect phrases
    "is good for", "is bad for",
]

# Layer 1b: Single-word opinion markers (confidence 0.90)
# Checked via exact word match after stripping punctuation
_OPINION_KEYWORDS = {
    # Prescriptive modals
    "should", "ought",
    # Subjective evaluators
    "overrated", "underrated", "overhyped",
    "beautiful", "ugly", "terrible", "amazing", "wonderful", "horrible",
    "perfect", "awful", "excellent", "superior", "inferior",
    # Moral/ethical judgments
    "immoral", "unethical", "evil", "righteous",
    "corrupt", "dishonest",
    # Safety/risk evaluators
    "dangerous", "unsafe", "harmful", "toxic", "risky",
    "safe",
    # Health evaluators
    "unhealthy", "wholesome",
    # Quality evaluators
    "wasteful", "pointless", "useless", "worthless",
}

# Layer 2: POS tagging catches comparatives/superlatives the keywords miss.
# But quantitative comparisons ("spends more than 10 countries") are factual,
# not opinion. These patterns identify quantitative context to suppress
# false-positive opinion signals from POS tags.
_STATISTICAL_PATTERNS = [
    r'\d+\s*%',
    r'\$[\d,]+',
    r'\d+\s*(million|billion|trillion)',
    r'(?:more|less|fewer) than \d+',
    r'spends?\s+more',
    r'costs?\s+more',
    r'(?:times|x)\s+(?:more|as much)',
    r'per\s+(?:capita|person|year|day|month)',
    r'\d+\s+(?:out of|in every)',
]

# "most" + countable noun = "majority of" (quantitative), not superlative
_QUANTITATIVE_MOST = re.compile(
    r'\bmost\s+(?:jobs|people|workers|countries|students|cases|'
    r'americans|things|adults|children|of\b)',
    re.IGNORECASE,
)

# Superlatives describing measurable quantities, not value judgments
# "largest economy" is measurable, "greatest player" is opinion
_QUANTITATIVE_SUPERLATIVE = re.compile(
    r'\b(?:largest|smallest|tallest|shortest|highest|lowest|fastest|slowest|'
    r'oldest|youngest|longest|heaviest|lightest|richest|poorest)\s+'
    r'(?:economy|country|city|population|gdp|building|mountain|river|ocean|'
    r'company|market|army|military|budget|deficit|surplus|producer|exporter|'
    r'importer|continent|planet|star|lake|desert|island|forest)',
    re.IGNORECASE,
)


def _has_statistical_context(claim_lower: str) -> bool:
    for pattern in _STATISTICAL_PATTERNS:
        if re.search(pattern, claim_lower):
            return True
    if _QUANTITATIVE_MOST.search(claim_lower):
        return True
    if _QUANTITATIVE_SUPERLATIVE.search(claim_lower):
        return True
    return False


def classify_claim_type(claim: str) -> tuple[str, float]:
    """Classify a claim as factual or opinion.

    Returns:
        ("factual", confidence) or ("opinion", confidence)

    Three detection layers, checked in order:
      1. Phrase/keyword matching (catches explicit opinion language)
      2. POS tagging (catches comparative/superlative structures)
      3. Default to factual (DeBERTa fallback available but off by default)
    """
    claim_lower = claim.lower().strip()
    words = claim_lower.split()

    # Layer 1a: phrase matching
    for phrase in _OPINION_PHRASES:
        if phrase in claim_lower:
            return ("opinion", 0.95)

    # Layer 1b: keyword matching
    for word in words:
        clean = re.sub(r'[.,!?;:\'"()\[\]]', '', word)
        if clean in _OPINION_KEYWORDS:
            return ("opinion", 0.90)

    # Layer 2: POS comparative/superlative detection
    tokens = word_tokenize(claim)
    tags = pos_tag(tokens)
    has_comparative = any(
        tag in ("JJR", "JJS", "RBR", "RBS") for _, tag in tags
    )
    if has_comparative and not _has_statistical_context(claim_lower):
        return ("opinion", 0.85)

    # Layer 3: default to factual
    # TODO: optional DeBERTa zero-shot fallback for ambiguous claims
    # from app.services.nli_service import classify_stance
    # stance, conf = classify_stance(claim, "This is a personal opinion or value judgment.")
    # if stance == "supporting" and conf > 0.7:
    #     return ("opinion", conf * 0.8)
    return ("factual", 0.80)


# =============================================================
# CLAIM DOMAIN: routing to appropriate sources
# =============================================================

_SCIENTIFIC_TERMS = {
    # ----- Biology / zoology -----
    "species", "animal", "animals", "mammal", "insect", "bird",
    "gene", "genes", "genetic", "dna", "rna",
    "evolution", "evolve", "evolved",
    "cell", "cells", "organism",
    "brain", "tongue", "blood", "muscle", "bone",
    "eye", "eyes", "heart", "lung", "lungs", "liver", "kidney", "skin",
    "blind", "deaf", "taste", "smell", "vision", "hearing",
    "bat", "bats", "spider", "spiders", "shark", "whale",
    "photosynthesis", "ecosystem", "biodiversity",
    # ----- Medical -----
    "vaccine", "vaccines", "vaccination",
    "virus", "viral", "bacteria", "bacterial",
    "disease", "diseases", "cancer",
    "health", "healthy", "unhealthy",
    "medicine", "medical", "drug", "drugs", "pharmaceutical",
    "symptom", "symptoms", "treatment", "cure", "diagnosis",
    "autism", "disorder", "syndrome", "infection",
    "antibiotic", "cholesterol",
    "sugar", "fat", "protein", "calorie", "calories", "nutrition",
    "wine", "alcohol", "caffeine", "diet", "dietary",
    "stress", "anxiety", "meditation",
    "knuckle", "knuckles", "arthritis", "joint", "joints",
    "gmo", "gmos", "organic", "genetically",
    "breakfast", "meal",
    # ----- Physics / chemistry -----
    "light", "gravity", "atom", "atoms", "energy",
    "temperature", "boil", "boils", "boiling",
    "freeze", "freezes", "freezing", "melt", "melting",
    "radiation", "quantum", "particle", "molecule",
    "speed", "velocity", "force", "mass", "weight",
    "magnetic", "electric", "nuclear", "fission", "fusion",
    # ----- Earth / environment -----
    "climate", "earth", "globe", "ocean", "atmosphere",
    "earthquake", "volcano", "fossil", "glacier", "ozone",
    "carbon", "oxygen", "greenhouse", "pollution",
    # ----- Scientific action words -----
    "cause", "causes", "caused",
    "swallow", "swallows", "digest",
    "sleep", "sleeping",
    "violence", "violent",
}

_HISTORICAL_TERMS = {
    "war", "wars", "empire", "dynasty", "ancient", "medieval",
    "century", "colonial", "revolution", "independence",
    "founded", "discovered", "invented", "built", "conquered",
    "king", "queen", "emperor", "pharaoh",
    "viking", "vikings", "roman", "greek", "egyptian",
    "byzantine", "ottoman", "aztec", "maya",
    "napoleon", "columbus", "lincoln", "cleopatra", "caesar",
    "gladiator", "knight", "knights", "samurai",
    "pyramid", "pyramids", "colosseum",
    "landing", "landed", "apollo",
    "faked", "alien", "aliens",
    "wall", "helmet", "helmets", "horned",
}

_CURRENT_EVENTS_TERMS = {
    "economy", "economic", "recession", "inflation", "deflation", "gdp",
    "unemployment", "employment",
    "election", "elections", "vote", "voting", "voter",
    "congress", "senate", "parliament", "legislation",
    "policy", "policies", "regulation", "regulations",
    "stock", "market", "markets", "trade", "tariff", "tariffs",
    "sanctions", "immigration", "border",
    "wage", "wages", "salary", "income", "minimum",
    "ai", "artificial", "technology",
    "pandemic", "covid", "coronavirus", "5g",
}

_STATISTICAL_TERMS = {
    "percent", "percentage", "ratio", "rate", "average", "median",
    "population", "statistic", "statistics", "data",
    "rank", "ranked", "ranking",
    "military", "spending", "budget", "cost",
}

# If a claim involves causation AND has scientific terms,
# scientific routing wins over current_events
_CAUSATION_WORDS = {
    "cause", "causes", "caused", "causing",
    "leads", "lead", "linked", "link",
}


def classify_claim_domain(claim: str) -> str:
    """Classify a claim's domain for source routing.

    Returns one of:
        "scientific"     -> prioritize academic w/ field filter, Wikipedia, DDG
        "historical"     -> prioritize Wikipedia, Wikidata, DDG
        "current_events" -> prioritize DDG, Google FC; restrict academic to recent
        "statistical"    -> prioritize DDG, academic; verify with structured data
        "general"        -> query all sources normally, no special filtering
    """
    claim_lower = claim.lower().strip()
    words_set = set(
        re.sub(r'[.,!?;:\'"()\[\]]', '', w) for w in claim_lower.split()
    )

    scores = {
        "scientific": 0.0,
        "historical": 0.0,
        "current_events": 0.0,
        "statistical": 0.0,
    }

    # Keyword scoring
    scores["scientific"] = len(words_set & _SCIENTIFIC_TERMS)
    scores["historical"] = len(words_set & _HISTORICAL_TERMS)
    scores["current_events"] = len(words_set & _CURRENT_EVENTS_TERMS)
    scores["statistical"] = len(words_set & _STATISTICAL_TERMS)

    # Statistical pattern boost (numbers, percentages, etc.)
    for pattern in _STATISTICAL_PATTERNS:
        if re.search(pattern, claim_lower):
            scores["statistical"] += 2
            break

    # Causation + scientific terms present -> scientific wins over current_events
    if words_set & _CAUSATION_WORDS:
        if scores["scientific"] > 0 and scores["current_events"] > 0:
            scores["scientific"] += 2

    # Past tense -> mild historical boost
    try:
        tokens = word_tokenize(claim)
        tags = pos_tag(tokens)
        past_verbs = sum(1 for _, t in tags if t == "VBD")
        if past_verbs > 0:
            scores["historical"] += 0.5
    except Exception:
        pass

    # Pick highest scoring domain
    best = max(scores, key=scores.get)
    if scores[best] == 0:
        return "general"

    # Tie-breaking priority: scientific > current > historical > statistical
    max_score = scores[best]
    tied = [k for k, v in scores.items() if v == max_score]
    if len(tied) > 1:
        for priority in ("scientific", "current_events", "historical", "statistical"):
            if priority in tied:
                return priority

    return best