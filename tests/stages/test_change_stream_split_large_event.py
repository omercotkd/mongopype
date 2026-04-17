"""Tests for $changeStreamSplitLargeEvent stage."""
from tests.conftest import V_70, V_OLD
from mongopype.stages.change_stream_split_large_event import verify_change_stream_split_large_event


def test_change_stream_split_last_70_empty_valid():
    valid, errors = verify_change_stream_split_large_event({}, V_70, pipeline_index=2, pipeline_length=3, is_atlas=False)
    assert valid is True
    assert errors == []


def test_change_stream_split_not_last_fails():
    valid, errors = verify_change_stream_split_large_event({}, V_70, pipeline_index=0, pipeline_length=3, is_atlas=False)
    assert valid is False
    assert any("last" in e.lower() for e in errors)


def test_change_stream_split_below_70_fails():
    valid, errors = verify_change_stream_split_large_event({}, (6, 9), pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("7.0" in e for e in errors)


def test_change_stream_split_at_70_ok():
    valid, errors = verify_change_stream_split_large_event({}, V_70, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True


def test_change_stream_split_non_empty_spec_fails():
    valid, errors = verify_change_stream_split_large_event({"x": 1}, V_70, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("empty" in e.lower() for e in errors)
