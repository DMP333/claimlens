"""Tier 2 integration test: the full /verify pipeline.

Drives a real POST through the endpoint with the outer edges faked (the search
APIs, the NLI/relevance models, credibility scoring, and the classifier/router),
so the real chain in between -- relevance filter, dedup, the stance branch,
verdict, response assembly -- runs on known data. This proves the wiring, not
the individual pieces (those are covered by the Tier 1 unit tests and the model
eval).
we just check at the end point rather we are getting expected output after input in the beginning of the pipeline, also check for invalid one
"""


async def _empty_search(*args, **kwargs):
    return []


def _stub_sources(make_source):
    # two that support, one that opposes; the faked stance fn below decodes the
    # stance from the snippet text so the result is fully deterministic
    return [
        make_source(url="https://a.com/1", title="First source on the topic",
                    snippet="This evidence clearly supports the claim in detail."),
        make_source(url="https://b.com/2", title="Second source on the topic",
                    snippet="Further analysis here supports the claim as well."),
        make_source(url="https://c.com/3", title="Third source on the topic",
                    snippet="This source opposes and refutes the claim entirely."),
    ]


def _fake_stance_sentences(premise, hypothesis, *args, **kwargs):
    stance = "supporting" if "support" in premise.lower() else "opposing"
    return (stance, 0.9, [{"text": premise}])


def _install_fakes(monkeypatch, sources):
    """Replace every networked / model-backed / nondeterministic edge.

    Note the TWO patch locations, because the names are imported two ways:

    (A) Imported at the TOP of claim_service  ->  patch them ON claim_service,
        because that module's own copy of the name is what the code calls.
    """
    cs = "app.services.claim_service"

    async def _return_sources(*a, **k):
        return sources

    # the six searches: one yields our sources, the rest yield nothing
    monkeypatch.setattr(f"{cs}.search_duckduckgo", _return_sources)
    for name in ("search_factcheck", "search_wikipedia", "search_semantic_scholar",
                 "search_openalex", "search_wikidata"):
        monkeypatch.setattr(f"{cs}.{name}", _empty_search)

    # models + scoring (no model ever loads)
    monkeypatch.setattr(f"{cs}.classify_stance_sentences", _fake_stance_sentences)
    monkeypatch.setattr(f"{cs}.classify_stance", lambda p, h: ("neutral", 0.0))
    monkeypatch.setattr(f"{cs}.compute_relevance", lambda claim, texts: [1.0] * len(texts))

    async def _fake_credibility(srcs):
        return [{"credibility_tier": "verified", "credibility_score": 0.9,
                 "bias_rating": None, "factual_reporting": None} for _ in srcs]
    monkeypatch.setattr(f"{cs}.score_all_sources", _fake_credibility)

    # (B) Imported INSIDE analyze_claim as local imports  ->  patch them ON
    #     THEIR ORIGIN modules, because the local import re-fetches them there.
    monkeypatch.setattr("app.services.claim_classifier.classify_claim_type",
                        lambda claim: ("factual", 0.9))
    monkeypatch.setattr("app.services.claim_classifier.classify_claim_domain",
                        lambda claim: "scientific")
    monkeypatch.setattr("app.services.source_router.build_routing_config",
                        lambda domain, claim: {})


def test_verify_runs_full_pipeline_and_shows_both_sides(client, make_source, monkeypatch):
    _install_fakes(monkeypatch, _stub_sources(make_source))

    resp = client.post("/verify", json={"claim": "Bats can sense magnetic fields"})
    assert resp.status_code == 200
    body = resp.json()

    # response shape, including the claim_domain field added in Step 1
    assert set(body) >= {"claim", "claim_type", "claim_type_confidence",
                         "claim_domain", "verdict", "confidence_in_verdict", "sources"}
    assert body["claim_domain"] == "scientific"

    # the core contract: both sides are present
    stances = {s["stance"] for s in body["sources"]}
    assert "supporting" in stances
    assert "opposing" in stances

    # two supporting vs one opposing -> leans supported, confidence in range
    assert body["verdict"] == "likely supported"
    assert 0.0 <= body["confidence_in_verdict"] <= 1.0
    assert len(body["sources"]) == 3


def test_verify_rejects_bad_input(client):
    # validation added in Step 1: blank and over-long claims never reach the pipeline
    assert client.post("/verify", json={"claim": ""}).status_code == 422
    assert client.post("/verify", json={"claim": "x" * 1001}).status_code == 422