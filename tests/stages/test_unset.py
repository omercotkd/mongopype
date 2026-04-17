"""Tests for $unset stage."""
from tests.conftest import V_42, V_OLD
from mongopype.stages.unset import verify_unset


def test_unset_string_at_42_valid():
    valid, errors = verify_unset("password", V_42, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True
    assert errors == []


def test_unset_list_at_42_valid():
    valid, errors = verify_unset(["password", "secret"], V_42, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True


def test_unset_below_42_fails():
    valid, errors = verify_unset("password", V_OLD, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("4.2" in e for e in errors)
