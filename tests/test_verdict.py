"""Tier 1 unit tests: compute_verdict.

Pure logic, no network, no model. We assert two kinds of things:
  - verdict LABELS exactly (they are a stable contract the front end relies on)
  - confidence as ranges/relationships, never an exact magic number (it is tunable)
  - These files are responsible for testing the outputs of the functions given the input
  - What this is testing simply: given a set of anaylzed source, does compute verdict produce the right label?
"""
from app.services.claim_service import compute_verdict


def test_all_supporting_factual_is_strongly_supported(make_result):
    sources = [make_result("supporting") for _ in range(3)]
    verdict, confidence = compute_verdict(sources, "factual")
    assert verdict == "strongly supported"
    assert 0.0 < confidence <= 1.0


def test_all_opposing_factual_is_strongly_opposed(make_result):
    sources = [make_result("opposing") for _ in range(3)]
    verdict, confidence = compute_verdict(sources, "factual")
    assert verdict == "strongly opposed"
    assert 0.0 < confidence <= 1.0


def test_even_split_is_contested_with_zero_confidence(make_result):
    sources = [make_result("supporting", 0.8, 0.9), make_result("opposing", 0.8, 0.9)]
    verdict, confidence = compute_verdict(sources, "factual")
    assert verdict == "contested"
    assert confidence == 0.0


def test_no_sources_is_insufficient_evidence(make_result):
    verdict, confidence = compute_verdict([], "factual")
    assert verdict == "insufficient evidence"
    assert confidence == 0.0


def test_all_neutral_is_insufficient_evidence(make_result):
    sources = [make_result("neutral"), make_result("neutral")]
    verdict, confidence = compute_verdict(sources, "factual")
    assert verdict == "insufficient evidence"
    assert confidence == 0.0


def test_opinion_claim_uses_soft_language(make_result):
    # ratio 0.75 -> a factual claim would say "strongly"/"likely"; opinion stays soft
    sources = [make_result("supporting") for _ in range(3)] + [make_result("opposing")]
    verdict, _ = compute_verdict(sources, "opinion")
    assert verdict == "sources lean supporting"


def test_opinion_even_split_is_divided(make_result):
    sources = [make_result("supporting", 0.8, 0.9), make_result("opposing", 0.8, 0.9)]
    verdict, _ = compute_verdict(sources, "opinion")
    assert verdict == "sources divided"


def test_richer_evidence_yields_higher_confidence(make_result):
    # Locks in the confidence fix: both unanimous (same label), but more and
    # stronger evidence must produce higher confidence than thin/weak evidence.
    thin = compute_verdict([make_result("supporting", 0.6, 0.6)], "factual")
    rich = compute_verdict([make_result("supporting", 0.9, 0.9) for _ in range(6)], "factual")
    assert thin[0] == rich[0] == "strongly supported"
    assert rich[1] > thin[1]


def test_confidence_always_in_unit_range(make_result):
    cases = [
        compute_verdict([make_result("supporting")], "factual"),
        compute_verdict([make_result("opposing")] * 5, "factual"),
        compute_verdict([make_result("supporting"), make_result("opposing")], "factual"),
        compute_verdict([], "factual"),
    ]
    for _verdict, confidence in cases:
        assert 0.0 <= confidence <= 1.0