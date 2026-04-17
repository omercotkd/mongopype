"""Tests for $indexStats stage."""
from tests.conftest import call_verify, V_60
from mongopype.stages.index_stats import verify_index_stats


def test_index_stats_at_first_empty_spec_valid():
    valid, errors = verify_index_stats({}, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True
    assert errors == []


def test_index_stats_not_first_fails():
    valid, errors = verify_index_stats({}, V_60, pipeline_index=1, pipeline_length=2, is_atlas=False)
    assert valid is False
    assert any("first" in e.lower() for e in errors)


def test_index_stats_non_empty_spec_fails():
    valid, errors = verify_index_stats({"extra": "value"}, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("empty" in e.lower() for e in errors)
