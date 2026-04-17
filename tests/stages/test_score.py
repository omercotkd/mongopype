"""Tests for $score stage."""
from tests.conftest import V_60
from mongopype.stages.score import verify_score


def test_score_atlas_with_score_field_valid():
    spec = {"score": {"$meta": "searchScore"}}
    valid, errors = verify_score(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=True)
    assert valid is True
    assert errors == []


def test_score_not_atlas_fails():
    spec = {"score": {"$meta": "searchScore"}}
    valid, errors = verify_score(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("Atlas" in e for e in errors)


def test_score_missing_score_field_fails():
    valid, errors = verify_score({}, V_60, pipeline_index=0, pipeline_length=1, is_atlas=True)
    assert valid is False
    assert any("score" in e for e in errors)
