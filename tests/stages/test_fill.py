"""Tests for $fill stage."""
from tests.conftest import V_53
from mongopype.stages.fill import verify_fill, FillSpec


def test_fill_valid_value_output():
    spec: FillSpec = {"output": {"score": {"value": 0}}}
    valid, errors = verify_fill(spec, V_53, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True
    assert errors == []


def test_fill_below_53_fails():
    spec: FillSpec = {"output": {"score": {"value": 0}}}
    valid, errors = verify_fill(spec, (5, 2), pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("5.3" in e for e in errors)


def test_fill_at_53_ok():
    spec: FillSpec = {"output": {"score": {"value": 0}}}
    valid, _ = verify_fill(spec, V_53, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True


def test_fill_missing_output_fails():
    spec = {"partitionBy": "$category"}
    valid, errors = verify_fill(spec, V_53, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("output" in e for e in errors)


def test_fill_both_partition_by_and_partition_by_fields_fails():
    spec = {
        "partitionBy": "$category",
        "partitionByFields": ["group"],
        "output": {"score": {"value": 0}},
    }
    valid, errors = verify_fill(spec, V_53, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("partitionBy" in e and "partitionByFields" in e for e in errors)


def test_fill_method_without_sort_by_fails():
    spec = {
        "output": {"score": {"method": "linear"}},
    }
    valid, errors = verify_fill(spec, V_53, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("sortBy" in e or "sort" in e.lower() for e in errors)


def test_fill_method_with_sort_by_valid():
    spec = {
        "sortBy": {"date": 1},
        "output": {"score": {"method": "linear"}},
    }
    valid, errors = verify_fill(spec, V_53, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True


def test_fill_value_without_sort_by_valid():
    spec = {"output": {"score": {"value": 0}}}
    valid, errors = verify_fill(spec, V_53, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True
