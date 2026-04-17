"""Tests for Pipeline.verify()."""
from tests.conftest import V_60, V_70
from mongopype.pipeline import Pipeline


def test_empty_pipeline_is_valid():
    pipeline = Pipeline([])
    valid, errors = pipeline.verify(V_60)
    assert valid is True
    assert errors == []


def test_single_valid_match_stage():
    pipeline = Pipeline([{"$match": {"status": "active"}}])
    valid, errors = pipeline.verify(V_60)
    assert valid is True
    assert errors == []


def test_unknown_stage_returns_error():
    pipeline = Pipeline([{"$unknownOp": {}}])
    valid, errors = pipeline.verify(V_60)
    assert valid is False
    assert len(errors) == 1
    assert "Unknown stage operator." in errors[0][1]


def test_errors_include_stage_index_label():
    pipeline = Pipeline([{"$unknownOp": {}}])
    valid, errors = pipeline.verify(V_60)
    assert "Stage 0" in errors[0][0]


def test_multiple_stages_all_valid():
    pipeline = Pipeline([
        {"$match": {"active": True}},
        {"$limit": 10},
        {"$skip": 0},
    ])
    valid, errors = pipeline.verify(V_60)
    assert valid is True


def test_multiple_stages_one_invalid_collects_all_errors():
    # $limit with 0 is invalid; $count with empty string is invalid
    pipeline = Pipeline([
        {"$limit": 0},
        {"$match": {"x": 1}},
        {"$count": ""},
    ])
    valid, errors = pipeline.verify(V_60)
    assert valid is False
    assert len(errors) == 2


def test_version_forwarded_to_stage():
    # $documents requires >= 6.0; at index 0 it should still fail on version with old version
    pipeline = Pipeline([{"$documents": [{"x": 1}]}])
    valid_new, _ = pipeline.verify(V_60)
    valid_old, errors_old = pipeline.verify((5, 9))
    assert valid_new is True
    assert valid_old is False
    assert any("6.0" in e for _, errs in errors_old for e in errs)


def test_is_atlas_forwarded_to_stage():
    # $vectorSearch requires is_atlas=True and must be first stage
    pipeline = Pipeline([
        {"$vectorSearch": {"index": "idx", "path": "emb", "queryVector": [0.1], "limit": 5}}
    ])
    valid_atlas, _ = pipeline.verify(V_60, is_atlas=True)
    valid_non_atlas, errors = pipeline.verify(V_60, is_atlas=False)
    assert valid_atlas is True
    assert valid_non_atlas is False
    assert any("Atlas" in e for _, errs in errors for e in errs)


def test_error_labels_include_correct_indices():
    pipeline = Pipeline([
        {"$unknownA": {}},
        {"$match": {}},
        {"$unknownB": {}},
    ])
    valid, errors = pipeline.verify(V_60)
    labels = [label for label, _ in errors]
    assert any("Stage 0" in l for l in labels)
    assert any("Stage 2" in l for l in labels)
    assert not any("Stage 1" in l for l in labels)
