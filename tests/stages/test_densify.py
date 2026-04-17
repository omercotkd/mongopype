"""Tests for $densify stage."""
from tests.conftest import V_51, V_OLD
from mongopype.stages.densify import verify_densify


_VALID_SPEC = {
    "field": "timestamp",
    "range": {"step": 1, "bounds": "full"},
}


def test_densify_valid():
    valid, errors = verify_densify(_VALID_SPEC, V_51, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True
    assert errors == []


def test_densify_below_51_fails():
    valid, errors = verify_densify(_VALID_SPEC, (5, 0), pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("5.1" in e for e in errors)


def test_densify_at_51_ok():
    valid, errors = verify_densify(_VALID_SPEC, V_51, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True


def test_densify_missing_field_fails():
    spec = {"range": {"step": 1, "bounds": "full"}}
    valid, errors = verify_densify(spec, V_51, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("field" in e for e in errors)


def test_densify_missing_range_fails():
    spec = {"field": "timestamp"}
    valid, errors = verify_densify(spec, V_51, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("range" in e for e in errors)


def test_densify_step_zero_fails():
    spec = {"field": "timestamp", "range": {"step": 0, "bounds": "full"}}
    valid, errors = verify_densify(spec, V_51, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("step" in e for e in errors)


def test_densify_step_negative_fails():
    spec = {"field": "timestamp", "range": {"step": -1, "bounds": "full"}}
    valid, errors = verify_densify(spec, V_51, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False


def test_densify_missing_bounds_fails():
    spec = {"field": "timestamp", "range": {"step": 1}}
    valid, errors = verify_densify(spec, V_51, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("bounds" in e for e in errors)


def test_densify_partition_by_fields_valid():
    spec = {
        "field": "timestamp",
        "partitionByFields": ["category"],
        "range": {"step": 1, "bounds": "full"},
    }
    valid, errors = verify_densify(spec, V_51, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True
