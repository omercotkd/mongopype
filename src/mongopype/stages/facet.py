# Done

from typing import TypedDict, TYPE_CHECKING
from ..types import Version

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/facet/

if TYPE_CHECKING:
    from ..pipeline import Pipeline


FacetSpec = dict[str, "Pipeline"]

Facet = TypedDict("Facet", {"$facet": FacetSpec})
"""
$facet stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/facet/
"""

_RESTRICTED_STAGES = {
    "$collStats",
    "$facet",
    "$geoNear",
    "$indexStats",
    "$out",
    "$merge",
    "$planCacheStats",
    "$search",
    "$searchMeta",
    "$vectorSearch",
}


def verify_facet(
    spec: FacetSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors = []

    for field_name, sub_pipeline in spec.items():
        if not isinstance(sub_pipeline, list):
            errors.append(f"$facet field '{field_name}' must be an array (pipeline).")
            continue
        for stage in sub_pipeline:
            if isinstance(stage, dict):
                stage_key = next(iter(stage), None)
                if stage_key in _RESTRICTED_STAGES:
                    errors.append(
                        f"$facet sub-pipeline '{field_name}' cannot contain {stage_key}."
                    )

    if errors:
        return False, errors

    return True, []
