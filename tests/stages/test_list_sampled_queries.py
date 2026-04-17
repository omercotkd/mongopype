"""Tests for $listSampledQueries stage."""
from tests.conftest import V_70
from mongopype.stages.list_sampled_queries import verify_list_sampled_queries


def test_list_sampled_queries_at_70_valid():
    valid, errors = verify_list_sampled_queries({}, V_70, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True
    assert errors == []


def test_list_sampled_queries_below_70_fails():
    valid, errors = verify_list_sampled_queries({}, (6, 9), pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("7.0" in e for e in errors)


def test_list_sampled_queries_namespace_valid():
    valid, errors = verify_list_sampled_queries({"namespace": "mydb.mycoll"}, V_70, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True


def test_list_sampled_queries_namespace_without_dot_fails():
    valid, errors = verify_list_sampled_queries({"namespace": "nodothere"}, V_70, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("database.collection" in e for e in errors)
