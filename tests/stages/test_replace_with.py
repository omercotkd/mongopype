"""Tests for $replaceWith stage."""
from tests.conftest import V_42, V_OLD
from mongopype.stages.replace_with import verify_replace_with


def test_replace_with_at_42_valid():
    valid, errors = verify_replace_with("$embedded", V_42, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True
    assert errors == []


def test_replace_with_below_42_fails():
    valid, errors = verify_replace_with("$embedded", V_OLD, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("4.2" in e for e in errors)
