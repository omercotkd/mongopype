"""Tests for $replaceRoot stage."""
from tests.conftest import call_verify
from mongopype.stages.replace_root import verify_replace_root


def test_replace_root_always_valid():
    valid, errors = call_verify(verify_replace_root, {"newRoot": "$embedded"})
    assert valid is True
    assert errors == []


def test_replace_root_string_expression_valid():
    valid, errors = call_verify(verify_replace_root, {"newRoot": "$$ROOT"})
    assert valid is True
    assert errors == []


def test_replace_root_any_position_valid():
    valid, errors = verify_replace_root({"newRoot": "$doc"}, (6, 0), pipeline_index=3, pipeline_length=5, is_atlas=False)
    assert valid is True
