"""Tests for $collStats stage."""
from tests.conftest import call_verify, V_60
from mongopype.stages.coll_stats import verify_coll_stats


def test_coll_stats_at_first_position_valid():
    valid, errors = call_verify(verify_coll_stats, {}, index=0)
    assert valid is True
    assert errors == []


def test_coll_stats_not_first_position_fails():
    valid, errors = verify_coll_stats({}, V_60, pipeline_index=1, pipeline_length=2, is_atlas=False)
    assert valid is False
    assert any("first" in e.lower() for e in errors)


def test_coll_stats_with_options_at_first_valid():
    spec = {"latencyStats": {"histograms": True}, "storageStats": {"scale": 1024}}
    valid, errors = call_verify(verify_coll_stats, spec, index=0)
    assert valid is True
