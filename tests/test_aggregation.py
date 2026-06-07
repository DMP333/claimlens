"""Tier 1 unit tests: NLI aggregation strategies (3A, 3K, 3J).

Pure math over per-sentence probabilities. We feed crafted sentence results
(no model involved) and check each strategy points the right direction. The
exact confidence is asserted only where it's just an input we passed through.
Simply put, this is testing: 3 nli strategy each working
"""
from app.services.nli_service import (
    _agg_3a_strongest,
    _agg_3k_bayesian,
    _agg_3j_topk,
)


def _s(p_supp, p_opp):
    """A per-sentence NLI result with just the fields the aggregators read."""
    return {"p_supp": p_supp, "p_opp": p_opp, "p_neut": max(0.0, 1 - p_supp - p_opp)}


def test_3a_picks_the_single_strongest_signal():
    supporting = [_s(0.9, 0.05), _s(0.2, 0.10)]
    assert _agg_3a_strongest(supporting) == ("supporting", 0.9)

    opposing = [_s(0.10, 0.30), _s(0.05, 0.85)]
    assert _agg_3a_strongest(opposing) == ("opposing", 0.85)


def test_3k_bayesian_accumulates_direction():
    assert _agg_3k_bayesian([_s(0.8, 0.1), _s(0.7, 0.15)])[0] == "supporting"
    assert _agg_3k_bayesian([_s(0.1, 0.8), _s(0.15, 0.7)])[0] == "opposing"


def test_3j_topk_compares_best_of_each_side():
    stance, _conf = _agg_3j_topk([_s(0.8, 0.1), _s(0.6, 0.2), _s(0.2, 0.5)])
    assert stance == "supporting"


def test_3j_returns_neutral_on_tie_or_empty():
    assert _agg_3j_topk([_s(0.5, 0.5), _s(0.5, 0.5)]) == ("neutral", 0.5)
    assert _agg_3j_topk([]) == ("neutral", 0.5)
