"""Tests for $listSearchIndexes stage."""
from tests.conftest import V_70
from mongopype.stages.list_search_indexes import verify_list_search_indexes


def test_list_search_indexes_atlas_70_valid():
    valid, errors = verify_list_search_indexes({}, V_70, pipeline_index=0, pipeline_length=1, is_atlas=True)
    assert valid is True
    assert errors == []


def test_list_search_indexes_not_atlas_fails():
    valid, errors = verify_list_search_indexes({}, V_70, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("Atlas" in e for e in errors)


def test_list_search_indexes_below_70_fails():
    valid, errors = verify_list_search_indexes({}, (6, 9), pipeline_index=0, pipeline_length=1, is_atlas=True)
    assert valid is False
    assert any("7.0" in e for e in errors)


def test_list_search_indexes_id_and_name_fails():
    spec = {"id": "abc123", "name": "my_index"}
    valid, errors = verify_list_search_indexes(spec, V_70, pipeline_index=0, pipeline_length=1, is_atlas=True)
    assert valid is False
    assert any("id" in e and "name" in e for e in errors)


def test_list_search_indexes_name_only_valid():
    valid, errors = verify_list_search_indexes({"name": "my_index"}, V_70, pipeline_index=0, pipeline_length=1, is_atlas=True)
    assert valid is True


def test_list_search_indexes_id_only_valid():
    valid, errors = verify_list_search_indexes({"id": "abc123"}, V_70, pipeline_index=0, pipeline_length=1, is_atlas=True)
    assert valid is True
