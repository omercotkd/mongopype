"""Tests for $planCacheStats stage."""
from tests.conftest import V_60
from mongopype.stages.plan_cache_stats import verify_plan_cache_stats


def test_plan_cache_stats_at_first_valid():
    valid, errors = verify_plan_cache_stats({}, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True
    assert errors == []


def test_plan_cache_stats_not_first_fails():
    valid, errors = verify_plan_cache_stats({}, V_60, pipeline_index=1, pipeline_length=2, is_atlas=False)
    assert valid is False
    assert any("first" in e.lower() for e in errors)


def test_plan_cache_stats_with_all_hosts_valid():
    valid, errors = verify_plan_cache_stats({"allHosts": True}, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True
