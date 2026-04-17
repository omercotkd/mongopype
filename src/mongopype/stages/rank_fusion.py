from typing import Any, TypedDict
from ..types import Version



class RankFusionSpec(TypedDict, total=False):
    input: dict[str, Any]
    combination: dict[str, Any]


RankFusion = TypedDict("RankFusion", {"$rankFusion": RankFusionSpec})
"""
$rankFusion stage (Atlas only):
https://www.mongodb.com/docs/manual/reference/operator/aggregation/rankFusion/
"""


def verify_rank_fusion(
    spec: RankFusionSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    if not is_atlas:
        errors.append("$rankFusion is only available on MongoDB Atlas.")

    if "input" not in spec:
        errors.append("$rankFusion requires the 'input' field.")
    elif "pipelines" not in spec.get("input", {}):
        errors.append("$rankFusion 'input' requires the 'pipelines' field.")

    if errors:
        return False, errors

    return True, []
