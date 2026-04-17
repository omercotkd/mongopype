"""Tests for $project stage."""
from tests.conftest import call_verify
from mongopype.stages.project import verify_project


def test_project_inclusion_only_valid():
    valid, errors = call_verify(verify_project, {"name": 1, "age": 1})
    assert valid is True
    assert errors == []


def test_project_exclusion_only_valid():
    valid, errors = call_verify(verify_project, {"password": 0, "secret": 0})
    assert valid is True
    assert errors == []


def test_project_id_exclusion_with_inclusions_valid():
    valid, errors = call_verify(verify_project, {"_id": 0, "name": 1, "age": 1})
    assert valid is True
    assert errors == []


def test_project_mixed_inclusion_exclusion_fails():
    valid, errors = call_verify(verify_project, {"name": 1, "password": 0})
    assert valid is False
    assert any("mix" in e.lower() for e in errors)


def test_project_empty_spec_fails():
    valid, errors = call_verify(verify_project, {})
    assert valid is False
    assert any("empty" in e.lower() for e in errors)


def test_project_expression_value_counts_as_inclusion():
    # computed field (dict expression) + another inclusion is ok
    valid, errors = call_verify(verify_project, {"fullName": {"$concat": ["$first", "$last"]}, "age": 1})
    assert valid is True
