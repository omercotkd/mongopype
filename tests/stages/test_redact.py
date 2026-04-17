"""Tests for $redact stage."""
from tests.conftest import call_verify
from mongopype.stages.redact import verify_redact


def test_redact_always_valid_string():
    valid, errors = call_verify(verify_redact, "$$DESCEND")
    assert valid is True
    assert errors == []


def test_redact_always_valid_dict():
    valid, errors = call_verify(verify_redact, {"$cond": {"if": True, "then": "$$KEEP", "else": "$$PRUNE"}})
    assert valid is True
    assert errors == []


def test_redact_any_position_valid():
    valid, errors = verify_redact("$$KEEP", (6, 0), pipeline_index=2, pipeline_length=5, is_atlas=False)
    assert valid is True
