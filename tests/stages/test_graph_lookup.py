"""Tests for $graphLookup stage."""
from tests.conftest import V_60
from mongopype.stages.graph_lookup import verify_graph_lookup, GraphLookupSpec


_VALID_SPEC: GraphLookupSpec = {
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



def test_graph_lookup_max_depth_negative_fails():
    spec: GraphLookupSpec = {**_VALID_SPEC, "maxDepth": -1}
    valid, errors = verify_graph_lookup(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("maxDepth" in e for e in errors)


def test_graph_lookup_max_depth_zero_valid():
    spec: GraphLookupSpec = {**_VALID_SPEC, "maxDepth": 0}
    valid, _ = verify_graph_lookup(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True


def test_graph_lookup_max_depth_positive_valid():
    spec: GraphLookupSpec = {**_VALID_SPEC, "maxDepth": 5}
    valid, _ = verify_graph_lookup(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True
