"""Tests for $unwind stage."""
from tests.conftest import call_verify
from mongopype.stages.unwind import verify_unwind


def test_unwind_string_with_dollar_valid():
    valid, errors = call_verify(verify_unwind, "$tags")
    assert valid is True
    assert errors == []


def test_unwind_string_without_dollar_fails():
    valid, errors = call_verify(verify_unwind, "tags")
    assert valid is False
    assert any("$" in e for e in errors)


def test_unwind_doc_form_with_dollar_path_valid():
    valid, errors = call_verify(verify_unwind, {"path": "$tags"})
    assert valid is True


def test_unwind_doc_form_missing_path_fails():
    valid, errors = call_verify(verify_unwind, {"includeArrayIndex": "idx"})
    assert valid is False
    assert any("path" in e for e in errors)


def test_unwind_doc_form_path_without_dollar_fails():
    valid, errors = call_verify(verify_unwind, {"path": "tags"})
    assert valid is False
    assert any("$" in e for e in errors)


def test_unwind_doc_form_with_options_valid():
    spec = {"path": "$tags", "includeArrayIndex": "tagIdx", "preserveNullAndEmptyArrays": True}
    valid, errors = call_verify(verify_unwind, spec)
    assert valid is True
