"""Tests for $listClusterCatalog stage."""
from tests.conftest import V_81, V_OLD
from mongopype.stages.list_cluster_catalog import verify_list_cluster_catalog


def test_list_cluster_catalog_at_first_valid():
    valid, errors = verify_list_cluster_catalog({}, V_81, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True
    assert errors == []


def test_list_cluster_catalog_not_first_fails():
    valid, errors = verify_list_cluster_catalog({}, V_81, pipeline_index=1, pipeline_length=2, is_atlas=False)
    assert valid is False
    assert any("first" in e.lower() for e in errors)


def test_list_cluster_catalog_below_81_fails():
    valid, errors = verify_list_cluster_catalog({}, (8, 0), pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("8.1" in e for e in errors)


def test_list_cluster_catalog_at_81_ok():
    valid, errors = verify_list_cluster_catalog({}, V_81, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True
