"""Tests for $match stage."""
from tests.conftest import call_verify
from mongopype.stages.match import verify_match


def test_match_always_valid():
    valid, errors = call_verify(verify_match, {"status": "active"})
    assert valid is True
    assert errors == []


def test_match_empty_spec_valid():
    valid, errors = call_verify(verify_match, {})
    assert valid is True
    assert errors == []


def test_match_any_position_valid():
    valid, errors = verify_match({}, (6, 0), pipeline_index=3, pipeline_length=10, is_atlas=False)
    assert valid is True
