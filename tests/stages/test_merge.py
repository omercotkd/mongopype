"""Tests for $merge stage."""
from tests.conftest import V_42
from mongopype.stages.merge import verify_merge


def test_merge_last_42_string_into_valid():
    valid, errors = verify_merge("output_coll", V_42, pipeline_index=1, pipeline_length=2, is_atlas=False)
    assert valid is True
    assert errors == []


def test_merge_last_42_dict_into_valid():
    valid, errors = verify_merge({"into": "output_coll"}, V_42, pipeline_index=1, pipeline_length=2, is_atlas=False)
    assert valid is True
    assert errors == []


def test_merge_not_last_fails():
    valid, errors = verify_merge("output_coll", V_42, pipeline_index=0, pipeline_length=3, is_atlas=False)
    assert valid is False
    assert any("last" in e.lower() for e in errors)


def test_merge_below_42_fails():
    valid, errors = verify_merge("output_coll", (4, 1), pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("4.2" in e for e in errors)

