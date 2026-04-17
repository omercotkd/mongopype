"""Tests for $sort stage."""
from tests.conftest import call_verify
from mongopype.stages.sort import verify_sort


def test_sort_single_field_valid():
    valid, errors = call_verify(verify_sort, {"age": 1})
    assert valid is True
    assert errors == []


def test_sort_multiple_fields_valid():
    valid, errors = call_verify(verify_sort, {"age": 1, "name": -1})
    assert valid is True


def test_sort_32_fields_valid():
    spec = {f"field{i}": 1 for i in range(32)}
    valid, errors = call_verify(verify_sort, spec)
    assert valid is True


def test_sort_33_fields_fails():
    spec = {f"field{i}": 1 for i in range(33)}
    valid, errors = call_verify(verify_sort, spec)
    assert valid is False
    assert any("32" in e for e in errors)


def test_sort_empty_spec_fails():
    valid, errors = call_verify(verify_sort, {})
    assert valid is False
    assert any("at least" in e.lower() or "must specify" in e.lower() for e in errors)


def test_sort_desc_valid():
    valid, errors = call_verify(verify_sort, {"score": -1})
    assert valid is True
