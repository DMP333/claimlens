"""Tier 1 unit tests: source deduplication.

Uses the make_source factory. Guards that the same source arriving twice
collapses to one, and that the higher-priority copy is the survivor.
this test is checking source filtering, ones with same sources or texts, while avoiding filtering the differnt ones
"""
from app.services.claim_service import _deduplicate_sources


def test_same_url_collapses(make_source):
    # http vs https, www, and trailing slash all normalize to the same URL
    a = make_source(url="https://example.com/a", title="Title one")
    b = make_source(url="http://www.example.com/a/", title="Title one variant")
    result = _deduplicate_sources([a, b])
    assert len(result) == 1


def test_same_title_collapses_and_keeps_higher_priority(make_source):
    # same normalized title, different URLs; fact_check outranks web, so it survives
    web = make_source(url="https://x.com/1", title="Blind Humans Develop Bat Superpower",
                      source_type="web")
    fc = make_source(url="https://y.com/2", title="blind humans develop bat superpower!",
                     source_type="fact_check")
    result = _deduplicate_sources([web, fc])
    assert len(result) == 1
    assert result[0].source_type == "fact_check"


def test_distinct_sources_are_kept(make_source):
    a = make_source(url="https://x.com/1", title="Totally different topic alpha", snippet="aaa")
    b = make_source(url="https://y.com/2", title="Completely unrelated thing beta", snippet="bbb")
    result = _deduplicate_sources([a, b])
    assert len(result) == 2