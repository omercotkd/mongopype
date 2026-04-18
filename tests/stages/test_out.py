"""Tests for $out stage."""
from tests.conftest import V_60
from mongopype.stages.out import verify_out


def test_out_string_form_last_valid():
    valid, errors = verify_out("results", V_60, pipeline_index=1, pipeline_length=2, is_atlas=False)
    assert valid is True
    assert errors == []


def test_out_string_not_last_fails():
    valid, errors = verify_out("results", V_60, pipeline_index=0, pipeline_length=3, is_atlas=False)
    assert valid is False
    assert any("last" in e.lower() for e in errors)


def test_out_empty_string_fails():
    valid, errors = verify_out("", V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("empty" in e.lower() or "not empty" in e.lower() for e in errors)


def test_out_dict_form_last_valid():
    valid, errors = verify_out({"db": "mydb", "coll": "results"}, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True
    assert errors == []

