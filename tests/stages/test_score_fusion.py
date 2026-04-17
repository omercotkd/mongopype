"""Tests for $scoreFusion stage."""
from tests.conftest import V_60
from mongopype.stages.score_fusion import verify_score_fusion


def test_score_fusion_atlas_valid():
    valid, errors = verify_score_fusion({}, V_60, pipeline_index=0, pipeline_length=1, is_atlas=True)
    assert valid is True
    assert errors == []


def test_score_fusion_not_atlas_fails():
    valid, errors = verify_score_fusion({}, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("Atlas" in e for e in errors)
