"""Tests for $shardedDataDistribution stage."""
from tests.conftest import V_60, V_OLD
from mongopype.stages.sharded_data_distribution import verify_sharded_data_distribution


def test_sharded_data_distribution_first_60_empty_valid():
    valid, errors = verify_sharded_data_distribution({}, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True
    assert errors == []


def test_sharded_data_distribution_not_first_fails():
    valid, errors = verify_sharded_data_distribution({}, V_60, pipeline_index=1, pipeline_length=2, is_atlas=False)
    assert valid is False
    assert any("first" in e.lower() for e in errors)


def test_sharded_data_distribution_below_60_fails():
    valid, errors = verify_sharded_data_distribution({}, (5, 9), pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("6.0" in e for e in errors)


def test_sharded_data_distribution_non_empty_spec_fails():
    valid, errors = verify_sharded_data_distribution({"extra": "val"}, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("empty" in e.lower() for e in errors)
