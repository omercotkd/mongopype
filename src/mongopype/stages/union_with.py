# Done

from typing import Union, TypedDict
from ..types import Version

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/unionWith/


class UnionWithFullSpec(TypedDict, total=False):
    coll: str
    pipeline: list


UnionWithSpec = Union[str, UnionWithFullSpec]

UnionWith = TypedDict("UnionWith", {"$unionWith": UnionWithSpec})
"""
$unionWith stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/unionWith/
"""


def verify_union_with(
    spec: UnionWithSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors = []

    if version < (4, 4):
        errors.append("$unionWith requires MongoDB >= 4.4.")

    if isinstance(spec, str):
        if not spec:
            errors.append("$unionWith collection name must not be empty.")
    elif isinstance(spec, dict):
        has_coll = "coll" in spec and spec["coll"]
        has_pipeline = "pipeline" in spec

        if not has_coll and not has_pipeline:
            errors.append("$unionWith must specify at least 'coll' or 'pipeline'.")

        if has_pipeline and isinstance(spec.get("pipeline"), list):
            for stage in spec["pipeline"]:
                if isinstance(stage, dict):
                    stage_key = next(iter(stage), None)
                    if stage_key in ("$out", "$merge"):
                        errors.append(f"$unionWith sub-pipeline cannot contain {stage_key}.")

    if errors:
        return False, errors

    return True, []
