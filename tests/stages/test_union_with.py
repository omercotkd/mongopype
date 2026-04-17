"""Tests for $unionWith stage."""
from tests.conftest import V_44, V_OLD
from mongopype.pipeline import Pipeline
from mongopype.stages.union_with import verify_union_with


def test_union_with_string_form_valid():
    valid, errors = verify_union_with("other_coll", V_44, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True
    assert errors == []


def test_union_with_empty_string_fails():
    valid, errors = verify_union_with("", V_44, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False


def test_union_with_below_44_fails():
    valid, errors = verify_union_with("other_coll", (4, 3), pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("4.4" in e for e in errors)


def test_union_with_dict_coll_only_valid():
    valid, errors = verify_union_with({"coll": "other_coll"}, V_44, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True


def test_union_with_dict_pipeline_only_valid():
    valid, errors = verify_union_with(
        {"pipeline": Pipeline([{"$match": {"x": 1}}])},
        V_44, pipeline_index=0, pipeline_length=1, is_atlas=False
    )
    assert valid is True


def test_union_with_dict_neither_coll_nor_pipeline_fails():
    valid, errors = verify_union_with({}, V_44, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("coll" in e or "pipeline" in e for e in errors)


def test_union_with_sub_pipeline_with_out_fails():
    valid, errors = verify_union_with(
        {"coll": "other", "pipeline": Pipeline([{"$out": "results"}])},
        V_44, pipeline_index=0, pipeline_length=1, is_atlas=False
    )
    assert valid is False
    assert any("$out" in e for e in errors)


def test_union_with_sub_pipeline_with_merge_fails():
    valid, errors = verify_union_with(
        {"coll": "other", "pipeline": Pipeline([{"$merge": "target"}])},
        V_44, pipeline_index=0, pipeline_length=1, is_atlas=False
    )
    assert valid is False
    assert any("$merge" in e for e in errors)
