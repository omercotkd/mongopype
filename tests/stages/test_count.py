"""Tests for $count stage."""
from tests.conftest import call_verify
from mongopype.stages.count import verify_count


def test_count_valid_field_name():
    valid, errors = call_verify(verify_count, "total")
    assert valid is True
    assert errors == []


def test_count_empty_string_fails():
    valid, errors = call_verify(verify_count, "")
    assert valid is False
    assert any("empty" in e.lower() or "non-empty" in e.lower() for e in errors)


def test_count_dollar_prefix_fails():
    valid, errors = call_verify(verify_count, "$total")
    assert valid is False
    assert any("$" in e for e in errors)


def test_count_dot_in_name_fails():
    valid, errors = call_verify(verify_count, "group.total")
    assert valid is False
    assert any("." in e for e in errors)


def test_count_underscore_name_valid():
    valid, errors = call_verify(verify_count, "_count")
    assert valid is True
