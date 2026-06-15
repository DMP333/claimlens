"""
Claim domain classification for source routing.

classify_claim_domain determines which sources to query (scientific, historical,
current_events, statistical, general) via keyword matching and POS tagging.

(The previous fact-vs-opinion classifier was removed: it only switched the
verdict wording, relied on brittle keyword matching, and the verdict now reads
uniformly as "Sources <verdict> this claim" for every claim.)
"""

import re
import nltk
from nltk import pos_tag, word_tokenize


# nltk data (sentence tokenizer + POS tagger) is downloaded once, on first use,
# so a fresh CI runner / container has it instead of crashing on first claim.
_nltk_ready = False


def _ensure_nltk() -> None:
    """Download the nltk data the classifier needs, once, on first use."""
    global _nltk_ready
    if not _nltk_ready:
        for pkg in ("punkt_tab", "averaged_perceptron_tagger_eng", "averaged_perceptron_tagger"):
            nltk.download(pkg, quiet=True)
        _nltk_ready = True


# Statistical patterns (numbers, percentages, money, quantitative comparisons).
# Used by classify_claim_domain to boost the "statistical" bucket.
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
    "body", "head", "hair", "teeth", "tooth",
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
    "temperature", "boil", "boils", "boiling", "heat",
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
        "historical"     -> prioritize Wikipedia, DDG
        "current_events" -> prioritize DDG, Google FC; restrict academic to recent
        "statistical"    -> prioritize DDG, academic; verify with structured data
        "general"        -> query all sources normally, no special filtering
    """
    _ensure_nltk()
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