"""Tier 1 unit tests: claim classifier (type + domain).

Pure logic (keyword sets, regex, POS tagging). For type we assert the label and
the confidence of the layer that fired (proving the right layer matched); for
domain we assert routing on clear single-domain claims.

Note: classify_* uses nltk POS tagging, so the nltk data (punkt_tab plus the
averaged_perceptron_tagger) must be available. See the runtime note about
ensuring that data so this also works in CI / a fresh deploy.
- Simply put, this file is testing: are we categorizing claim type correctly using already proven set, and also source type for scholar article search
"""
from app.services.claim_classifier import classify_claim_type, classify_claim_domain


# --- type ----------------------------------------------------------------

def test_opinion_phrase_is_highest_confidence():
    assert classify_claim_type("I think pineapple belongs on pizza") == ("opinion", 0.95)
    assert classify_claim_type("Pineapple is better than pepperoni") == ("opinion", 0.95)


def test_opinion_keyword_layer():
    assert classify_claim_type("Schools should ban phones") == ("opinion", 0.90)
    assert classify_claim_type("Modern art is overrated") == ("opinion", 0.90)


def test_comparative_pos_layer():
    # no opinion phrase or keyword, but a comparative adjective -> opinion at 0.85
    assert classify_claim_type("Tuesdays are worse than Mondays") == ("opinion", 0.85)


def test_statistical_context_suppresses_false_opinion():
    # "more than 10" is a quantity, not a value judgment, so this stays factual
    assert classify_claim_type("The US spends more than 10 countries on military") == ("factual", 0.80)


def test_plain_factual_default():
    assert classify_claim_type("Vaccines cause autism") == ("factual", 0.80)


# --- domain --------------------------------------------------------------

def test_domain_scientific():
    assert classify_claim_domain("Vaccines cause autism") == "scientific"


def test_domain_historical():
    assert classify_claim_domain("Napoleon was a French emperor") == "historical"


def test_domain_current_events():
    assert classify_claim_domain("The unemployment rate affects the economy") == "current_events"


def test_domain_general_when_no_keywords():
    assert classify_claim_domain("asdfgh qwerty zxcvb") == "general"
