"""Tests for $sortByCount stage."""
from tests.conftest import call_verify
from mongopype.stages.sort_by_count import verify_sort_by_count


def test_sort_by_count_dollar_string_valid():
    valid, errors = call_verify(verify_sort_by_count, "$category")
    assert valid is True
    assert errors == []


def test_sort_by_count_string_without_dollar_fails():
    valid, errors = call_verify(verify_sort_by_count, "category")
    assert valid is False
    assert any("$" in e for e in errors)


def test_sort_by_count_dict_expression_valid():
    valid, errors = call_verify(verify_sort_by_count, {"$toLower": "$category"})
    assert valid is True


def test_sort_by_count_integer_expression_valid():
    valid, errors = call_verify(verify_sort_by_count, 1)
    assert valid is True
