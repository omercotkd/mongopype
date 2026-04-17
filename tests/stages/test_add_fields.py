"""Tests for $addFields stage."""
from tests.conftest import call_verify, V_60
from mongopype.stages.add_fields import verify_add_fields


def test_add_fields_always_valid():
    valid, errors = call_verify(verify_add_fields, {"total": {"$sum": "$price"}})
    assert valid is True
    assert errors == []


def test_add_fields_empty_spec_valid():
    valid, errors = call_verify(verify_add_fields, {})
    assert valid is True
    assert errors == []


def test_add_fields_any_position_valid():
    valid, errors = verify_add_fields({}, V_60, pipeline_index=5, pipeline_length=10, is_atlas=False)
    assert valid is True
