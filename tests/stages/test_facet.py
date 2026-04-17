"""Tests for $facet stage."""
from tests.conftest import V_60
from mongopype.pipeline import Pipeline
from mongopype.stages.facet import verify_facet


def test_facet_valid_sub_pipelines():
    spec = {
        "byCategory": Pipeline([{"$match": {"active": True}}]),
        "byStatus": Pipeline([{"$group": {"_id": "$status"}}]),
    }
    valid, errors = verify_facet(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True
    assert errors == []


def test_facet_sub_pipeline_with_collStats_fails():
    spec = {"stats": Pipeline([{"$collStats": {}}])}
    valid, errors = verify_facet(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("$collStats" in e for e in errors)


def test_facet_sub_pipeline_with_out_fails():
    spec = {"out": Pipeline([{"$out": "results"}])}
    valid, errors = verify_facet(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("$out" in e for e in errors)


def test_facet_sub_pipeline_with_merge_fails():
    spec = {"merged": Pipeline([{"$merge": "target"}])}
    valid, errors = verify_facet(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("$merge" in e for e in errors)


def test_facet_sub_pipeline_with_search_fails():
    spec = {"s": Pipeline([{"$search": {}}])}
    valid, errors = verify_facet(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("$search" in e for e in errors)


def test_facet_sub_pipeline_validation_errors_propagated():
    # $limit 0 is invalid
    spec = {"broken": Pipeline([{"$limit": 0}])}
    valid, errors = verify_facet(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
