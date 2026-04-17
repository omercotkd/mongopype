"""Tests for $bucket stage."""
from tests.conftest import V_60
from mongopype.stages.bucket import verify_bucket, BucketSpec


def test_bucket_valid_ascending_boundaries():
    spec: BucketSpec = {
        "groupBy": "$price",
        "boundaries": [0, 10, 100],
        "default": "Other",
        "output": {"count": {"$sum": 1}},
    }
    valid, errors = verify_bucket(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True
    assert errors == []


def test_bucket_non_ascending_boundaries_fails():
    spec: BucketSpec = {
        "groupBy": "$price",
        "boundaries": [100, 10, 0],
        "output": {},
    }
    valid, errors = verify_bucket(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("ascending" in e.lower() or "order" in e.lower() for e in errors)


def test_bucket_equal_adjacent_boundaries_fails():
    spec: BucketSpec = {
        "groupBy": "$price",
        "boundaries": [0, 10, 10, 100],
        "output": {},
    }
    valid, _ = verify_bucket(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False


def test_bucket_invalid_accumulator_fails():
    spec: BucketSpec = {
        "groupBy": "$price",
        "boundaries": [0, 10, 100],
        "output": {"bad": {"$sum": 1, "$avg": 1}},  # two operators
    }
    valid, _ = verify_bucket(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False


def test_bucket_numeric_default_outside_boundaries_fails():
    spec: BucketSpec = {
        "groupBy": "$price",
        "boundaries": [0, 10, 100],
        "default": 5,  # inside boundaries — invalid
        "output": {},
    }
    valid, errors = verify_bucket(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("default" in e.lower() for e in errors)


def test_bucket_numeric_default_below_first_boundary_valid():
    spec: BucketSpec = {
        "groupBy": "$price",
        "boundaries": [0, 10, 100],
        "default": -1,  # less than first boundary
        "output": {},
    }
    valid, _ = verify_bucket(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True


def test_bucket_string_default_always_valid():
    spec: BucketSpec = {
        "groupBy": "$price",
        "boundaries": [0, 10, 100],
        "default": "Other",
        "output": {},
    }
    valid, _ = verify_bucket(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True
