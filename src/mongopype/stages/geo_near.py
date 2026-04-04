from typing import Any, TypedDict

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/geoNear/

GeoNearSpec = dict[str, Any]  # Required: near, distanceField

GeoNear = TypedDict("GeoNear", {"$geoNear": GeoNearSpec})

def verify_geo_near(spec: GeoNearSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (near + distanceField required)
    return True
