from typing import TypedDict, NotRequired
from ..types import Version, Document



class RankFusionSpec(TypedDict):
    input: Document
    combination: NotRequired[Document]


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
