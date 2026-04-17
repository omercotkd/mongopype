"""Tests for $querySettings stage."""
from tests.conftest import V_80, V_OLD
from mongopype.stages.query_settings import verify_query_settings


def test_query_settings_at_first_at_80_valid():
    valid, errors = verify_query_settings({}, V_80, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True
    assert errors == []


def test_query_settings_not_first_fails():
    valid, errors = verify_query_settings({}, V_80, pipeline_index=1, pipeline_length=2, is_atlas=False)
    assert valid is False
    assert any("first" in e.lower() for e in errors)


def test_query_settings_below_80_fails():
    valid, errors = verify_query_settings({}, (7, 9), pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("8.0" in e for e in errors)


def test_query_settings_at_80_ok():
    valid, errors = verify_query_settings({}, V_80, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True
