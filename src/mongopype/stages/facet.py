from typing import TypedDict, TYPE_CHECKING
from ..types import Version

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
    spec: FacetSpec,
    version: Version,
    pipeline_index: int,
    pipeline_length: int,
    is_atlas: bool,
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    for field_name, sub_pipeline in spec.items():
        for stage in sub_pipeline:
            stage_key = next(iter(stage), None)
            if stage_key in _RESTRICTED_STAGES:
                errors.append(
                    f"$facet sub-pipeline '{field_name}' cannot contain {stage_key}."
                )
        valid, sub_errors = sub_pipeline.verify(version, is_atlas)
        if not valid:
            errors.extend(str(f"$facet sub-pipeline '{field_name}' error: {err}") for err in sub_errors)

    if errors:
        return False, errors

    return True, []
