"""Tier 1 unit tests: source routing (build_routing_config).

Pure logic mapping a claim's domain + text to per-source API configuration.
#tesitng how 6 api should behave given scenarios
"""
from app.services.source_router import build_routing_config

ALL_SOURCES = {"google_factcheck", "wikipedia", "semantic_scholar",
               "open_alex", "duckduckgo"}


def test_config_always_has_all_five_sources():
    config = build_routing_config("statistical", "the unemployment rate is data")
    assert set(config) == ALL_SOURCES


def test_scientific_claim_sets_academic_field_filters():
    config = build_routing_config("scientific", "vaccines cause autism")
    assert config["semantic_scholar"]["field_filters"] == ["Medicine"]
    assert config["open_alex"]["field_filters"] == ["Medicine"]
    assert config["semantic_scholar"]["max_results"] == 7


def test_general_claim_without_fields_disables_academic():
    config = build_routing_config("general", "pineapple tastes great")
    assert config["semantic_scholar"]["enabled"] is False
    assert config["open_alex"]["enabled"] is False


def test_historical_claim_boosts_wikipedia_and_uses_history_field():
    config = build_routing_config("historical", "napoleon conquered europe")
    assert config["wikipedia"]["max_results"] == 7
    assert config["semantic_scholar"]["field_filters"] == ["History"]