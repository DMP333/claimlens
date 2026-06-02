"""
Shared utilities for the Project A diagnostic harness.

Design goals:
  - Reuse the real pipeline functions where possible (max fidelity).
  - Keep verdict math as a local replica so the data-only scripts
    (oracle, neutral-injection on cached stances) don't have to import
    the heavy model-loading modules.
  - Operate on the cached snippets in labeled_sources.json so the
    diagnostics are reproducible and don't require live API calls.

The verdict replica below mirrors app.services.claim_service.compute_verdict
exactly (same bands, same weighting). If you change compute_verdict, update
this too, or import the real one (it triggers model load via nli_service).
"""

import json
import os
from dataclasses import dataclass

DEFAULT_SOURCES = os.environ.get("LABELED_SOURCES", "labeled_sources.json")


@dataclass
class SourceStance:
    """Minimal stand-in for SourceResult; only what compute_verdict reads."""
    stance: str
    stance_confidence: float
    credibility_score: float = 1.0   # default = unweighted view
    source_type: str = ""
    is_contaminated: bool = False
    claim: str = ""
    title: str = ""


def load_sources(path: str = DEFAULT_SOURCES) -> list[dict]:
    with open(path) as f:
        return json.load(f)


def by_claim(rows: list[dict]) -> dict[str, list[dict]]:
    out: dict[str, list[dict]] = {}
    for r in rows:
        out.setdefault(r["claim"], []).append(r)
    return out


def compute_verdict_local(sources: list[SourceStance], claim_type: str) -> tuple[str, float]:
    """EXACT replica of claim_service.compute_verdict (bands + weighting)."""
    ws = wo = 0.0
    for s in sources:
        if s.stance == "neutral":
            continue
        w = s.stance_confidence * s.credibility_score
        if s.stance == "supporting":
            ws += w
        elif s.stance == "opposing":
            wo += w
    total = ws + wo
    if total == 0:
        return ("insufficient evidence", 0.0)
    ratio = ws / total
    confidence = abs(ratio - 0.5) * 2
    if claim_type == "opinion":
        if ratio >= 0.60:
            v = "sources lean supporting"
        elif ratio > 0.40:
            v = "sources divided"
        else:
            v = "sources lean opposing"
        return (v, round(confidence, 4))
    if ratio >= 0.80:
        v = "strongly supported"
    elif ratio >= 0.60:
        v = "likely supported"
    elif ratio > 0.40:
        v = "contested"
    elif ratio >= 0.20:
        v = "likely opposed"
    else:
        v = "strongly opposed"
    return (v, round(confidence, 4))


def verdict_band(ratio):
    """Coarse factual band from a support ratio (for ablation reporting)."""
    if ratio is None:
        return "insufficient"
    if ratio >= 0.80:
        return "strongly supported"
    if ratio >= 0.60:
        return "likely supported"
    if ratio > 0.40:
        return "contested"
    if ratio >= 0.20:
        return "likely opposed"
    return "strongly opposed"


def load_json(path, default=None):
    if not os.path.exists(path):
        return default
    with open(path) as f:
        return json.load(f)
