"""Tests for $sample stage."""
from tests.conftest import call_verify
from mongopype.stages.sample import verify_sample


def test_sample_size_zero_valid():
    valid, errors = call_verify(verify_sample, {"size": 0})
    assert valid is True
    assert errors == []


def test_sample_positive_size_valid():
    valid, errors = call_verify(verify_sample, {"size": 100})
    assert valid is True


def test_sample_negative_size_fails():
    valid, errors = call_verify(verify_sample, {"size": -1})
    assert valid is False
    assert any("non-negative" in e.lower() or "size" in e.lower() for e in errors)
