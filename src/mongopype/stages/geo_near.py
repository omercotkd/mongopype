from typing import Literal, Union, TypedDict, NotRequired
from ..types import Version, Document


class GeoJSONPoint(TypedDict):
    type: Literal["Point"]
    coordinates: list[float]


class GeoNearSpec(TypedDict):
    near: Union[GeoJSONPoint, list[float]]
    distanceField: NotRequired[str] 
    """
    not required since MongoDB 8.1 for queries on non time-series collections
    """
    distanceMultiplier: NotRequired[float]
    includeLocs: NotRequired[str]
    key: NotRequired[str]
    maxDistance: NotRequired[float]
    minDistance: NotRequired[float]
    query: NotRequired[Document]
    spherical: NotRequired[bool]


GeoNear = TypedDict("GeoNear", {"$geoNear": GeoNearSpec})
"""
$geoNear stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/geoNear/
"""


def verify_geo_near(
    spec: GeoNearSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    if pipeline_index != 0:
        errors.append("$geoNear must be the first stage in the pipeline.")

    if "distanceField" not in spec and version < (8, 1):
        errors.append("$geoNear requires a 'distanceField' field (optional since MongoDB 8.1).")

    if errors:
        return False, errors

    return True, []
