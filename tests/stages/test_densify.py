"""Tests for $densify stage."""

from tests.conftest import V_51
from mongopype.stages.densify import verify_densify, DensifySpec


_VALID_SPEC: DensifySpec = {
    "field": "timestamp",
    "range": {"step": 1, "bounds": "full"},
}


def test_densify_valid():
    valid, errors = verify_densify(
        _VALID_SPEC, V_51, pipeline_index=0, pipeline_length=1, is_atlas=False
    )
    assert valid is True
    assert errors == []


def test_densify_below_51_fails():
    valid, errors = verify_densify(
        _VALID_SPEC, (5, 0), pipeline_index=0, pipeline_length=1, is_atlas=False
    )
    assert valid is False
    assert any("5.1" in e for e in errors)


def test_densify_at_51_ok():
    valid, _ = verify_densify(
        _VALID_SPEC, V_51, pipeline_index=0, pipeline_length=1, is_atlas=False
    )
    assert valid is True


def test_densify_step_zero_fails():
    spec: DensifySpec = {"field": "timestamp", "range": {"step": 0, "bounds": "full"}}
    valid, errors = verify_densify(
        spec, V_51, pipeline_index=0, pipeline_length=1, is_atlas=False
    )
    assert valid is False
    assert any("step" in e for e in errors)


def test_densify_step_negative_fails():
    spec: DensifySpec = {"field": "timestamp", "range": {"step": -1, "bounds": "full"}}
    valid, _ = verify_densify(
        spec, V_51, pipeline_index=0, pipeline_length=1, is_atlas=False
    )
    assert valid is False



def test_densify_partition_by_fields_valid():
    spec: DensifySpec = {
        "field": "timestamp",
        "partitionByFields": ["category"],
        "range": {"step": 1, "bounds": "full"},
    }
    valid, _ = verify_densify(
        spec, V_51, pipeline_index=0, pipeline_length=1, is_atlas=False
    )
    assert valid is True
