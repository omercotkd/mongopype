"""Tests for $queryStats stage."""
from tests.conftest import V_80, V_OLD
from mongopype.stages.query_stats import verify_query_stats


def test_query_stats_atlas_first_80_valid():
    valid, errors = verify_query_stats({}, V_80, pipeline_index=0, pipeline_length=1, is_atlas=True)
    assert valid is True
    assert errors == []


def test_query_stats_not_atlas_fails():
    valid, errors = verify_query_stats({}, V_80, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("Atlas" in e for e in errors)


def test_query_stats_below_80_fails():
    valid, errors = verify_query_stats({}, (7, 9), pipeline_index=0, pipeline_length=1, is_atlas=True)
    assert valid is False
    assert any("8.0" in e for e in errors)


def test_query_stats_not_first_fails():
    valid, errors = verify_query_stats({}, V_80, pipeline_index=1, pipeline_length=2, is_atlas=True)
    assert valid is False
    assert any("first" in e.lower() for e in errors)
