"""Tests for $rankFusion stage."""
from tests.conftest import V_60
from mongopype.stages.rank_fusion import verify_rank_fusion


def test_rank_fusion_atlas_with_input_pipelines_valid():
    spec = {"input": {"pipelines": {"p1": [], "p2": []}}}
    valid, errors = verify_rank_fusion(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=True)
    assert valid is True
    assert errors == []


def test_rank_fusion_not_atlas_fails():
    spec = {"input": {"pipelines": {}}}
    valid, errors = verify_rank_fusion(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("Atlas" in e for e in errors)


def test_rank_fusion_missing_input_fails():
    valid, errors = verify_rank_fusion({}, V_60, pipeline_index=0, pipeline_length=1, is_atlas=True)
    assert valid is False
    assert any("input" in e for e in errors)


def test_rank_fusion_input_without_pipelines_fails():
    spec = {"input": {"combination": {}}}
    valid, errors = verify_rank_fusion(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=True)
    assert valid is False
    assert any("pipelines" in e for e in errors)
