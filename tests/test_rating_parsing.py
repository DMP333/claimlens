"""Tier 1 unit tests: fact-check rating parsing.

Pure string logic, no fixtures needed. These guard how messy external rating
text gets read into a (polarity, confidence) the verdict can trust.
fact checker api is handled differently so testing for that
- Simply put, this is testing: for fact checker api, are we extracting the correct rating and its label?
"""
from app.services.claim_service import _classify_rating, _extract_rating_label


def test_extract_label_strips_trailing_explanation():
    # the label is just the part before the first separator
    assert _extract_rating_label("False. The images were taken in 2019") == "false"
    assert _extract_rating_label("False") == "false"


def test_clear_negative_ratings():
    assert _classify_rating("false") == ("negative", 0.95)
    assert _classify_rating("mostly false") == ("negative", 0.85)


def test_clear_positive_ratings():
    assert _classify_rating("true") == ("positive", 0.95)
    assert _classify_rating("mostly true") == ("positive", 0.85)


def test_specific_key_beats_generic_one():
    # "not true" must be read as negative, not as the positive "true"
    assert _classify_rating("not true")[0] == "negative"
    # "mostly false" matches its own key (0.85), not bare "false" (0.95)
    assert _classify_rating("mostly false") == ("negative", 0.85)
    assert _classify_rating("false") == ("negative", 0.95)


def test_inexact_match_falls_to_substring_and_caps_confidence():
    # trailing "!" means no exact label match; substring path matches and caps at 0.75
    polarity, conf = _classify_rating("Pants on Fire!")
    assert polarity == "negative"
    assert conf <= 0.75


def test_label_matching_is_case_insensitive():
    assert _classify_rating("Mostly True") == ("positive", 0.85)


def test_unrecognized_rating_is_unknown():
    assert _classify_rating("we looked into it") == ("unknown", 0.0)