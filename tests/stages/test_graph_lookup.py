"""Tests for $graphLookup stage."""
from tests.conftest import V_60
from mongopype.stages.graph_lookup import verify_graph_lookup


_VALID_SPEC = {
    "from": "employees",
    "startWith": "$reportsTo",
    "connectFromField": "reportsTo",
    "connectToField": "name",
    "as": "reportingHierarchy",
}


def test_graph_lookup_all_required_fields_valid():
    valid, errors = verify_graph_lookup(_VALID_SPEC, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True
    assert errors == []


def test_graph_lookup_missing_from_fails():
    spec = {k: v for k, v in _VALID_SPEC.items() if k != "from"}
    valid, errors = verify_graph_lookup(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("from" in e for e in errors)


def test_graph_lookup_missing_start_with_fails():
    spec = {k: v for k, v in _VALID_SPEC.items() if k != "startWith"}
    valid, errors = verify_graph_lookup(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("startWith" in e for e in errors)


def test_graph_lookup_missing_connect_from_field_fails():
    spec = {k: v for k, v in _VALID_SPEC.items() if k != "connectFromField"}
    valid, errors = verify_graph_lookup(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False


def test_graph_lookup_missing_connect_to_field_fails():
    spec = {k: v for k, v in _VALID_SPEC.items() if k != "connectToField"}
    valid, errors = verify_graph_lookup(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False


def test_graph_lookup_missing_as_fails():
    spec = {k: v for k, v in _VALID_SPEC.items() if k != "as"}
    valid, errors = verify_graph_lookup(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("'as'" in e for e in errors)


def test_graph_lookup_max_depth_negative_fails():
    spec = {**_VALID_SPEC, "maxDepth": -1}
    valid, errors = verify_graph_lookup(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("maxDepth" in e for e in errors)


def test_graph_lookup_max_depth_zero_valid():
    spec = {**_VALID_SPEC, "maxDepth": 0}
    valid, errors = verify_graph_lookup(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True


def test_graph_lookup_max_depth_positive_valid():
    spec = {**_VALID_SPEC, "maxDepth": 5}
    valid, errors = verify_graph_lookup(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True
