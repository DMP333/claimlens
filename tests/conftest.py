"""Shared test fixtures.

pytest auto-discovers this file (no import needed). Anything defined here as a
fixture is available to every test in this directory and below, simply by naming
it as a test-function argument.
utilizes factory design pattern
- schmea changes mean we just need to change this file
- stable controlled variables
- Each fixture represents "frequently used input object" that is used for testing
"""
import pytest

from app.models.schemas import Source, SourceResult


@pytest.fixture
def make_result(): #fixed condition for the test, 과학 실험 할때 controlled variable
    """Factory for SourceResult objects.

    Returns a function, so each test can build as many results as it wants and
    override only the fields it cares about. The verdict logic only reads stance,
    stance_confidence, and credibility_score, so those are the easy-to-set args;
    everything else gets a harmless default.
    """
    def _make(stance="supporting", stance_confidence=0.85, credibility_score=0.9, **overrides):
        defaults = dict(
            url="https://example.com/a",
            title="Example",
            stance=stance,
            stance_confidence=stance_confidence,
            credibility_tier="verified",
            credibility_score=credibility_score,
            bias_rating=None,
            factual_reporting=None,
            method="sentence_nli",
        )
        defaults.update(overrides)
        return SourceResult(**defaults)
    return _make #returns function (not the call)


@pytest.fixture
def make_source():
    """Factory for raw Source objects (pre-analysis). Used by dedup + API tests."""
    def _make(**overrides):
        defaults = dict(
            url="https://example.com/a",
            title="Example title",
            snippet="Example snippet about the claim.",
            source_type="web",
            credibility=None,
            raw_claim_rating=None,
            metadata=None,
        )
        defaults.update(overrides)
        return Source(**defaults)
    return _make


@pytest.fixture
def client():
    """A FastAPI test client for hitting the real endpoints in-process.

    Imported lazily inside the fixture so Tier 1 logic tests (which never request
    `client`) don't import the whole app just to test a pure function.
    """
    from fastapi.testclient import TestClient
    from app.main import app
    return TestClient(app) #hands back the finished object as client object can be fixed for entirity of testing, unlike other 2 functions where depending on parameter object can change