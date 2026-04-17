"""Tests for $geoNear stage."""
from tests.conftest import V_60, V_81
from mongopype.stages.geo_near import verify_geo_near


_VALID_SPEC = {
    "near": {"type": "Point", "coordinates": [0.0, 0.0]},
    "distanceField": "dist",
}


def test_geo_near_first_with_near_and_distance_field_valid():
    valid, errors = verify_geo_near(_VALID_SPEC, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True
    assert errors == []


def test_geo_near_not_first_fails():
    valid, errors = verify_geo_near(_VALID_SPEC, V_60, pipeline_index=1, pipeline_length=2, is_atlas=False)
    assert valid is False
    assert any("first" in e.lower() for e in errors)


def test_geo_near_missing_near_fails():
    spec = {"distanceField": "dist"}
    valid, errors = verify_geo_near(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("near" in e for e in errors)


def test_geo_near_missing_distance_field_below_81_fails():
    spec = {"near": {"type": "Point", "coordinates": [0.0, 0.0]}}
    valid, errors = verify_geo_near(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("distanceField" in e for e in errors)


def test_geo_near_missing_distance_field_at_81_ok():
    spec = {"near": {"type": "Point", "coordinates": [0.0, 0.0]}}
    valid, errors = verify_geo_near(spec, V_81, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True
