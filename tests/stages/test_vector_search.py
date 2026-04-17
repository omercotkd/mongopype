"""Tests for $vectorSearch stage."""
from tests.conftest import V_60
from mongopype.stages.vector_search import verify_vector_search

_VALID_SPEC = {
    "index": "vector_index",
    "path": "embedding",
    "queryVector": [0.1, 0.2, 0.3],
    "limit": 10,
}


def test_vector_search_atlas_first_valid():
    valid, errors = verify_vector_search(_VALID_SPEC, V_60, pipeline_index=0, pipeline_length=1, is_atlas=True)
    assert valid is True
    assert errors == []


def test_vector_search_not_atlas_fails():
    valid, errors = verify_vector_search(_VALID_SPEC, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("Atlas" in e for e in errors)


def test_vector_search_not_first_fails():
    valid, errors = verify_vector_search(_VALID_SPEC, V_60, pipeline_index=1, pipeline_length=2, is_atlas=True)
    assert valid is False
    assert any("first" in e.lower() for e in errors)


def test_vector_search_missing_index_fails():
    spec = {k: v for k, v in _VALID_SPEC.items() if k != "index"}
    valid, errors = verify_vector_search(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=True)
    assert valid is False
    assert any("index" in e for e in errors)


def test_vector_search_missing_path_fails():
    spec = {k: v for k, v in _VALID_SPEC.items() if k != "path"}
    valid, errors = verify_vector_search(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=True)
    assert valid is False
    assert any("path" in e for e in errors)


def test_vector_search_missing_query_vector_fails():
    spec = {k: v for k, v in _VALID_SPEC.items() if k != "queryVector"}
    valid, errors = verify_vector_search(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=True)
    assert valid is False
    assert any("queryVector" in e for e in errors)


def test_vector_search_missing_limit_fails():
    spec = {k: v for k, v in _VALID_SPEC.items() if k != "limit"}
    valid, errors = verify_vector_search(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=True)
    assert valid is False
    assert any("limit" in e for e in errors)
