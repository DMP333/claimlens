"""Tier 1 unit tests: claim domain classifier.

Pure logic (keyword sets, regex, POS tagging). We assert routing on clear
single-domain claims.

Note: classify_claim_domain uses nltk POS tagging, so the nltk data (punkt_tab
plus the averaged_perceptron_tagger) must be available. See the runtime note
about ensuring that data so this also works in CI / a fresh deploy.

(The fact-vs-opinion classifier was removed, so only domain routing is tested now.)
"""
from app.services.claim_classifier import classify_claim_domain


def test_domain_scientific():
    assert classify_claim_domain("Vaccines cause autism") == "scientific"


def test_domain_historical():
    assert classify_claim_domain("Napoleon was a French emperor") == "historical"


def test_domain_current_events():
    assert classify_claim_domain("The unemployment rate affects the economy") == "current_events"


def test_domain_general_when_no_keywords():
    assert classify_claim_domain("asdfgh qwerty zxcvb") == "general"