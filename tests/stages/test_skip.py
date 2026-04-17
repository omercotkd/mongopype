"""Tests for $skip stage."""
from tests.conftest import call_verify
from mongopype.stages.skip import verify_skip


def test_skip_zero_valid():
    valid, errors = call_verify(verify_skip, 0)
    assert valid is True
    assert errors == []


def test_skip_positive_valid():
    valid, errors = call_verify(verify_skip, 100)
    assert valid is True


def test_skip_negative_fails():
    valid, errors = call_verify(verify_skip, -1)
    assert valid is False
    assert any("non-negative" in e.lower() for e in errors)
