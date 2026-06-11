"""API + pipeline tests for the async-job verification flow.

Three deterministic groups, none of which touch a real database or load a model:

1. Pipeline wiring: drives the real chain (relevance filter -> dedup -> stance
   branch -> verdict -> response assembly -> _present_sources) by calling
   analyze_claim directly with the networked/model edges stubbed. This is the
   integration coverage; the real Postgres round-trip is validated manually, not
   here, by design (see the backend handoff).

2. _present_sources unit test: the pure presentation logic, neutral-drop plus
   stance-grouped credibility ordering, on a handmade list.

3. Route HTTP-code mapping: the only real logic in the thin routes is which
   status code they return, so verification_service is mocked and get_session is
   overridden, letting the route's branching (202 / 404 / 503 / 200) run with no
   database behind it.
"""
import asyncio
import uuid
from datetime import datetime, timezone
from types import SimpleNamespace

import pytest
from sqlalchemy.exc import SQLAlchemyError

from app.models.schemas import ClaimRequest
from app.services import claim_service


# ===========================================================================
# 1. PIPELINE WIRING (analyze_claim directly, edges stubbed)
# ===========================================================================

async def _empty_search(*args, **kwargs):
    return []


def _stub_sources(make_source):
    # two support, one oppose, one neutral; the faked stance fn decodes the
    # stance from the snippet text so the result is fully deterministic
    return [
        make_source(url="https://a.com/1", title="First source on the topic",
                    snippet="This evidence clearly supports the claim in detail."),
        make_source(url="https://b.com/2", title="Second source on the topic",
                    snippet="Further analysis here supports the claim as well."),
        make_source(url="https://c.com/3", title="Third source on the topic",
                    snippet="This source opposes and refutes the claim entirely."),
        make_source(url="https://d.com/4", title="Fourth source on the topic",
                    snippet="This is neutral background with no stance either way."),
    ]


def _fake_stance_sentences(premise, hypothesis, *args, **kwargs):
    low = premise.lower()
    if "neutral" in low:
        stance = "neutral"
    elif "support" in low:
        stance = "supporting"
    else:
        stance = "opposing"
    return (stance, 0.9, [{"text": premise}])


def _fake_stance_sentences_batch(premises, hypothesis, *args, **kwargs):
    """Batch seam fake: same deterministic snippet-decoding as the single
    fake, applied per premise. Mirrors the production contract of
    classify_stance_sentences_batch (one tuple per premise, input order)."""
    return [_fake_stance_sentences(p, hypothesis) for p in premises]


def _install_fakes(monkeypatch, sources):
    """Replace every networked / model-backed / nondeterministic edge.

    Names imported at the TOP of claim_service are patched ON claim_service,
    because that module's own copy of the name is what the code calls. Names
    imported INSIDE analyze_claim (the classifier/router) are patched on their
    origin modules, because the local import re-fetches them there.
    """
    cs = "app.services.claim_service"

    async def _return_sources(*a, **k):
        return sources

    monkeypatch.setattr(f"{cs}.search_duckduckgo", _return_sources)
    for name in ("search_factcheck", "search_wikipedia", "search_semantic_scholar",
                 "search_openalex"):
        monkeypatch.setattr(f"{cs}.{name}", _empty_search)

    monkeypatch.setattr(f"{cs}.classify_stance_sentences", _fake_stance_sentences)
    monkeypatch.setattr(f"{cs}.classify_stance_sentences_batch", _fake_stance_sentences_batch)
    monkeypatch.setattr(f"{cs}.classify_stance", lambda p, h: ("neutral", 0.0))
    monkeypatch.setattr(f"{cs}.compute_relevance", lambda claim, texts: [1.0] * len(texts))

    async def _fake_credibility(srcs):
        return [{"credibility_tier": "verified", "credibility_score": 0.9,
                 "bias_rating": None, "factual_reporting": None} for _ in srcs]
    monkeypatch.setattr(f"{cs}.score_all_sources", _fake_credibility)

    monkeypatch.setattr("app.services.claim_classifier.classify_claim_type",
                        lambda claim: ("factual", 0.9))
    monkeypatch.setattr("app.services.claim_classifier.classify_claim_domain",
                        lambda claim: "scientific")
    monkeypatch.setattr("app.services.source_router.build_routing_config",
                        lambda domain, claim: {})


def test_pipeline_runs_chain_drops_neutral_and_shows_both_sides(make_source, monkeypatch):
    _install_fakes(monkeypatch, _stub_sources(make_source))

    result = asyncio.run(
        claim_service.analyze_claim(ClaimRequest(claim="Bats can sense magnetic fields"))
    )

    # classifier/router stubs flowed through to the response
    assert result.claim_domain == "scientific"

    # the core contract: both sides present, neutral dropped from the output
    stances = {s.stance for s in result.sources}
    assert "supporting" in stances
    assert "opposing" in stances
    assert "neutral" not in stances

    # four stubbed sources, the neutral one dropped -> three shown
    assert len(result.sources) == 3

    # two supporting vs one opposing among the scored sources -> likely supported
    assert result.verdict == "likely supported"
    assert 0.0 <= result.confidence_in_verdict <= 1.0


# ===========================================================================
# 2. _present_sources (pure logic: drop neutral + order)
# ===========================================================================

def test_present_sources_drops_neutral_and_orders_by_credibility(make_result):
    sources = [
        make_result(stance="opposing", credibility_score=0.9),
        make_result(stance="supporting", credibility_score=0.5),
        make_result(stance="neutral", credibility_score=0.99),   # high cred, still dropped
        make_result(stance="supporting", credibility_score=0.8),
    ]

    out = claim_service._present_sources(sources)

    # neutral is gone regardless of its credibility
    assert all(s.stance != "neutral" for s in out)
    # supporting group first, then opposing
    assert [s.stance for s in out] == ["supporting", "supporting", "opposing"]
    # credibility descending within each group
    assert [s.credibility_score for s in out] == [0.8, 0.5, 0.9]


# ===========================================================================
# 3. ROUTE HTTP-CODE MAPPING (verification_service mocked, session overridden)
# ===========================================================================

@pytest.fixture
def api_client():
    """TestClient with the DB session dependency stubbed to None, so route
    tests never open a real database. The mocked service ignores the session.
    """
    from fastapi.testclient import TestClient
    from app.main import app
    from app.db.session import get_session

    app.dependency_overrides[get_session] = lambda: None
    try:
        yield TestClient(app)
    finally:
        app.dependency_overrides.clear()


def test_submit_returns_202_with_pending(api_client, monkeypatch):
    job_id = uuid.uuid4()

    async def _fake_submit(claim, session):
        return job_id

    monkeypatch.setattr("app.services.verification_service.submit_job", _fake_submit)

    resp = api_client.post("/verify", json={"claim": "A perfectly valid claim"})
    assert resp.status_code == 202
    body = resp.json()
    assert body["id"] == str(job_id)
    assert body["status"] == "pending"


def test_submit_returns_503_when_db_unavailable(api_client, monkeypatch):
    async def _boom(claim, session):
        raise SQLAlchemyError("connection refused")

    monkeypatch.setattr("app.services.verification_service.submit_job", _boom)

    resp = api_client.post("/verify", json={"claim": "A perfectly valid claim"})
    assert resp.status_code == 503


def test_submit_rejects_bad_input(api_client):
    # validation happens before the endpoint; blank and over-long never reach it
    assert api_client.post("/verify", json={"claim": ""}).status_code == 422
    assert api_client.post("/verify", json={"claim": "x" * 1001}).status_code == 422


def test_poll_unknown_id_returns_404(api_client, monkeypatch):
    async def _none(verification_id, session):
        return None

    monkeypatch.setattr("app.services.verification_service.get_job", _none)

    resp = api_client.get(f"/verify/{uuid.uuid4()}")
    assert resp.status_code == 404


def test_poll_returns_200_with_job_status(api_client, monkeypatch):
    job = SimpleNamespace(
        id=uuid.uuid4(),
        status="pending",
        result=None,
        error=None,
        created_at=datetime.now(timezone.utc),
        completed_at=None,
    )

    async def _get(verification_id, session):
        return job

    monkeypatch.setattr("app.services.verification_service.get_job", _get)

    resp = api_client.get(f"/verify/{job.id}")
    assert resp.status_code == 200
    body = resp.json()
    assert body["id"] == str(job.id)
    assert body["status"] == "pending"
    assert body["result"] is None


def test_poll_returns_503_when_db_unavailable(api_client, monkeypatch):
    async def _boom(verification_id, session):
        raise SQLAlchemyError("connection refused")

    monkeypatch.setattr("app.services.verification_service.get_job", _boom)

    resp = api_client.get(f"/verify/{uuid.uuid4()}")
    assert resp.status_code == 503