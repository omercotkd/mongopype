"""Tests for $documents stage."""
from tests.conftest import call_verify, V_60, V_OLD
from mongopype.stages.documents import verify_documents


def test_documents_at_first_position_valid():
    valid, errors = call_verify(verify_documents, [{"x": 1}], version=V_60, index=0)
    assert valid is True
    assert errors == []


def test_documents_not_first_fails():
    valid, errors = verify_documents([{"x": 1}], V_60, pipeline_index=1, pipeline_length=2, is_atlas=False)
    assert valid is False
    assert any("first" in e.lower() for e in errors)


def test_documents_below_60_fails():
    valid, errors = verify_documents([{"x": 1}], (5, 9), pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("6.0" in e for e in errors)


def test_documents_at_60_valid():
    valid, errors = verify_documents([{"x": 1}], V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True
