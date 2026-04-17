"""Tests for $changeStream stage."""
from tests.conftest import V_60
from mongopype.stages.change_stream import verify_change_stream


def test_change_stream_at_first_valid():
    valid, errors = verify_change_stream({}, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True
    assert errors == []


def test_change_stream_not_first_fails():
    valid, errors = verify_change_stream({}, V_60, pipeline_index=1, pipeline_length=2, is_atlas=False)
    assert valid is False
    assert any("first" in e.lower() for e in errors)


def test_change_stream_show_expanded_events_below_60_fails():
    valid, errors = verify_change_stream(
        {"showExpandedEvents": True}, (5, 9), pipeline_index=0, pipeline_length=1, is_atlas=False
    )
    assert valid is False
    assert any("6.0" in e for e in errors)


def test_change_stream_show_expanded_events_at_60_ok():
    valid, errors = verify_change_stream(
        {"showExpandedEvents": True}, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False
    )
    assert valid is True


def test_change_stream_resume_after_and_start_after_mutually_exclusive():
    spec = {"resumeAfter": {"_data": "abc"}, "startAfter": {"_data": "xyz"}}
    valid, errors = verify_change_stream(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("exclusive" in e.lower() or "mutually" in e.lower() for e in errors)


def test_change_stream_resume_after_and_start_at_op_time_mutually_exclusive():
    spec = {"resumeAfter": {"_data": "abc"}, "startAtOperationTime": "2024-01-01"}
    valid, errors = verify_change_stream(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False


def test_change_stream_start_after_and_start_at_op_time_mutually_exclusive():
    spec = {"startAfter": {"_data": "abc"}, "startAtOperationTime": "2024-01-01"}
    valid, errors = verify_change_stream(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False


def test_change_stream_all_three_resume_fields_mutually_exclusive():
    spec = {
        "resumeAfter": {"_data": "a"},
        "startAfter": {"_data": "b"},
        "startAtOperationTime": "2024-01-01",
    }
    valid, errors = verify_change_stream(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False


def test_change_stream_single_resume_field_valid():
    valid, errors = verify_change_stream(
        {"resumeAfter": {"_data": "abc"}}, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False
    )
    assert valid is True
