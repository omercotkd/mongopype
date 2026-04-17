"""Tests for $bucketAuto stage."""

from tests.conftest import V_60
from mongopype.stages.bucket_auto import verify_bucket_auto, BucketAutoSpec


def test_bucket_auto_valid():
    spec: BucketAutoSpec = {
        "groupBy": "$price",
        "buckets": 5,
        "output": {"count": {"$sum": 1}},
    }
    valid, errors = verify_bucket_auto(
        spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False
    )
    assert valid is True
    assert errors == []


def test_bucket_auto_buckets_zero_fails():
    spec: BucketAutoSpec = {"groupBy": "$price", "buckets": 0, "output": {}}
    valid, errors = verify_bucket_auto(
        spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False
    )
    assert valid is False
    assert any("buckets" in e.lower() for e in errors)


def test_bucket_auto_buckets_negative_fails():
    spec: BucketAutoSpec = {"groupBy": "$price", "buckets": -1, "output": {}}
    valid, _ = verify_bucket_auto(
        spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False
    )
    assert valid is False


def test_bucket_auto_buckets_exceeds_32bit_fails():
    spec: BucketAutoSpec = {"groupBy": "$price", "buckets": 2**31, "output": {}}
    valid, _ = verify_bucket_auto(
        spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False
    )
    assert valid is False


def test_bucket_auto_max_valid_buckets():
    spec: BucketAutoSpec = {"groupBy": "$price", "buckets": 2**31 - 1, "output": {}}
    valid, _ = verify_bucket_auto(
        spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False
    )
    assert valid is True


def test_bucket_auto_invalid_accumulator_fails():
    spec: BucketAutoSpec = {
        "groupBy": "$price",
        "buckets": 5,
        "output": {"bad": {"$sum": 1, "$avg": 1}},  # two operators
    }
    valid, _ = verify_bucket_auto(
        spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False
    )
    assert valid is False
