"""Tests for $group stage."""
from tests.conftest import call_verify
from mongopype.stages.group import verify_group


def test_group_with_id_valid():
    valid, errors = call_verify(verify_group, {"_id": "$category", "total": {"$sum": "$amount"}})
    assert valid is True
    assert errors == []


def test_group_id_null_valid():
    valid, errors = call_verify(verify_group, {"_id": None})
    assert valid is True


def test_group_missing_id_fails():
    valid, errors = call_verify(verify_group, {"total": {"$sum": "$amount"}})
    assert valid is False
    assert any("_id" in e for e in errors)
