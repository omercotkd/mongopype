"""Tests for $search stage."""
from tests.conftest import V_60
from mongopype.stages.search import verify_search


def test_search_atlas_first_valid():
    valid, errors = verify_search({"text": {"query": "hello", "path": "body"}}, V_60, pipeline_index=0, pipeline_length=1, is_atlas=True)
    assert valid is True
    assert errors == []


def test_search_not_atlas_fails():
    valid, errors = verify_search({}, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("Atlas" in e for e in errors)


def test_search_not_first_fails():
    valid, errors = verify_search({}, V_60, pipeline_index=1, pipeline_length=2, is_atlas=True)
    assert valid is False
    assert any("first" in e.lower() for e in errors)
