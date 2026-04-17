"""Tests for $searchMeta stage."""
from tests.conftest import V_60
from mongopype.stages.search_meta import verify_search_meta


def test_search_meta_atlas_first_valid():
    valid, errors = verify_search_meta({}, V_60, pipeline_index=0, pipeline_length=1, is_atlas=True)
    assert valid is True
    assert errors == []


def test_search_meta_not_atlas_fails():
    valid, errors = verify_search_meta({}, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("Atlas" in e for e in errors)


def test_search_meta_not_first_fails():
    valid, errors = verify_search_meta({}, V_60, pipeline_index=1, pipeline_length=2, is_atlas=True)
    assert valid is False
    assert any("first" in e.lower() for e in errors)
