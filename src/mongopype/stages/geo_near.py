from typing import Literal, Any

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/geoNear/

GeoNear = dict[Literal["$geoNear"], dict[str, Any]]  # Required: near, distanceField

def verify_geo_near(stage: GeoNear, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (near + distanceField required)
    return True
