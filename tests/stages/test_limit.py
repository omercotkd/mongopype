"""Tests for $limit stage."""
from tests.conftest import call_verify
from mongopype.stages.limit import verify_limit


def test_limit_positive_valid():
    valid, errors = call_verify(verify_limit, 10)
    assert valid is True
    assert errors == []


def test_limit_one_valid():
    valid, errors = call_verify(verify_limit, 1)
    assert valid is True


def test_limit_large_value_valid():
    valid, errors = call_verify(verify_limit, 1_000_000)
    assert valid is True


def test_limit_zero_fails():
    valid, errors = call_verify(verify_limit, 0)
    assert valid is False
    assert any("positive" in e.lower() for e in errors)


def test_limit_negative_fails():
    valid, errors = call_verify(verify_limit, -1)
    assert valid is False
