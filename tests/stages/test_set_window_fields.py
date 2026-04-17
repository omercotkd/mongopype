"""Tests for $setWindowFields stage."""
from tests.conftest import V_50, V_OLD
from mongopype.stages.set_window_fields import verify_set_window_fields


def test_set_window_fields_at_50_with_output_valid():
    spec = {"sortBy": {"date": 1}, "output": {"runningTotal": {"$sum": "$amount"}}}
    valid, errors = verify_set_window_fields(spec, V_50, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True
    assert errors == []


def test_set_window_fields_below_50_fails():
    spec = {"output": {"total": {"$sum": "$x"}}}
    valid, errors = verify_set_window_fields(spec, (4, 9), pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("5.0" in e for e in errors)


def test_set_window_fields_missing_output_fails():
    spec = {"sortBy": {"date": 1}}
    valid, errors = verify_set_window_fields(spec, V_50, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("output" in e for e in errors)
