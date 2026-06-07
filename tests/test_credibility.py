"""Tier 1 unit tests: credibility scoring.

Covers the pure per-source-type scorers and the tier selection inside
score_all_sources, with the OpenPageRank network call mocked out so nothing
touches the network.
- check appropriate sources receives appropriate credibility
"""
import asyncio

from app.services.credibility_service import (
    _score_academic,
    _score_wikipedia,
    score_all_sources,
)


def test_score_academic_by_citation_count(make_source):
    assert _score_academic(make_source(metadata={"citation_count": 1500})) == 0.95
    assert _score_academic(make_source(metadata={"citation_count": 50})) == 0.65
    assert _score_academic(make_source(metadata={})) == 0.40


def test_score_wikipedia_by_quality_signals(make_source):
    assert _score_wikipedia(make_source(metadata={"is_featured": True})) == 0.95
    assert _score_wikipedia(make_source(metadata={"article_length": 20000})) == 0.80
    assert _score_wikipedia(make_source(metadata={"article_length": 100})) == 0.55


def test_unknown_web_source_is_unverified(make_source, monkeypatch):
    async def _no_opr(domains):
        return {}
    monkeypatch.setattr("app.services.credibility_service._batch_openpagerank", _no_opr)

    web = make_source(url="https://some-unknown-blog.example/post", source_type="web")
    results = asyncio.run(score_all_sources([web]))
    assert results[0]["credibility_tier"] == "unverified"
    assert results[0]["credibility_score"] == 0.30


def test_academic_source_gets_estimated_tier(make_source, monkeypatch):
    async def _no_opr(domains):
        return {}
    monkeypatch.setattr("app.services.credibility_service._batch_openpagerank", _no_opr)

    paper = make_source(url="https://some-unknown-journal.example/p",
                        source_type="academic", metadata={"citation_count": 1500})
    results = asyncio.run(score_all_sources([paper]))
    assert results[0]["credibility_tier"] == "estimated"
    assert results[0]["credibility_score"] == 0.95