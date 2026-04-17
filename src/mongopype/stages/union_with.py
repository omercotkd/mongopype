from typing import Union, TypedDict, TYPE_CHECKING
from ..types import Version

if TYPE_CHECKING:
    from ..pipeline import Pipeline

class UnionWithFullSpec(TypedDict, total=False):
    coll: str
    pipeline: "Pipeline"

UnionWithSpec = Union[str, UnionWithFullSpec]

UnionWith = TypedDict("UnionWith", {"$unionWith": UnionWithSpec})
"""
$unionWith stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/unionWith/
"""


def verify_union_with(
    spec: UnionWithSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    if version < (4, 4):
        errors.append("$unionWith requires MongoDB >= 4.4.")

    if isinstance(spec, str):
        if not spec:
            errors.append("$unionWith collection name must not be empty.")
    else:
        has_coll = "coll" in spec and spec["coll"]
        has_pipeline = "pipeline" in spec

        if not has_coll and not has_pipeline:
            errors.append("$unionWith must specify at least 'coll' or 'pipeline'.")

        if has_pipeline:
            for stage in spec["pipeline"]:
                stage_key = next(iter(stage), None)
                if stage_key in ("$out", "$merge"):
                    errors.append(f"$unionWith sub-pipeline cannot contain {stage_key}.")
            v, e = spec["pipeline"].verify(version, is_atlas) 
            if not v:
                errors.extend(f"$unionWith sub-pipeline: {err}" for err in e)       

    if errors:
        return False, errors

    return True, []
