"""Tests for $lookup stage."""
from tests.conftest import V_60, V_51
from mongopype.pipeline import Pipeline
from mongopype.stages.lookup import verify_lookup


def test_lookup_equality_form_valid():
    spec = {
        "from": "orders",
        "localField": "customerId",
        "foreignField": "_id",
        "as": "orders",
    }
    valid, errors = verify_lookup(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True
    assert errors == []


def test_lookup_equality_form_missing_as_fails():
    spec = {"from": "orders", "localField": "customerId", "foreignField": "_id"}
    valid, errors = verify_lookup(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("'as'" in e for e in errors)


def test_lookup_equality_form_missing_local_field_fails():
    spec = {"from": "orders", "foreignField": "_id", "as": "orders"}
    valid, errors = verify_lookup(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("localField" in e for e in errors)


def test_lookup_equality_form_missing_foreign_field_fails():
    spec = {"from": "orders", "localField": "cid", "as": "orders"}
    valid, errors = verify_lookup(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("foreignField" in e for e in errors)


def test_lookup_pipeline_form_valid():
    spec = {
        "from": "orders",
        "pipeline": Pipeline([{"$match": {"active": True}}]),
        "as": "orders",
    }
    valid, errors = verify_lookup(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True


def test_lookup_pipeline_form_with_local_foreign_below_51_fails():
    spec = {
        "from": "orders",
        "localField": "cid",
        "foreignField": "_id",
        "pipeline": Pipeline([]),
        "as": "orders",
    }
    valid, errors = verify_lookup(spec, (5, 0), pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("5.1" in e for e in errors)


def test_lookup_pipeline_form_with_local_foreign_at_51_ok():
    spec = {
        "from": "orders",
        "localField": "cid",
        "foreignField": "_id",
        "pipeline": Pipeline([]),
        "as": "orders",
    }
    valid, errors = verify_lookup(spec, V_51, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True


def test_lookup_sub_pipeline_with_out_fails():
    spec = {
        "from": "orders",
        "pipeline": Pipeline([{"$out": "results"}]),
        "as": "orders",
    }
    valid, errors = verify_lookup(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("$out" in e for e in errors)


def test_lookup_sub_pipeline_with_merge_fails():
    spec = {
        "from": "orders",
        "pipeline": Pipeline([{"$merge": "target"}]),
        "as": "orders",
    }
    valid, errors = verify_lookup(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("$merge" in e for e in errors)
