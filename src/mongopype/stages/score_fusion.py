from typing import Any, NotRequired, TypedDict
from ..types import Version

class ScoreFusionSpec(TypedDict):
    input: dict[str, Any]
    combination: NotRequired[dict[str, Any]]
    scoreDetails: NotRequired[bool]


ScoreFusion = TypedDict("ScoreFusion", {"$scoreFusion": ScoreFusionSpec})
"""
$scoreFusion stage (Atlas only):
https://www.mongodb.com/docs/manual/reference/operator/aggregation/scoreFusion/
"""


def verify_score_fusion(
    spec: ScoreFusionSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    if not is_atlas:
        errors.append("$scoreFusion is only available on MongoDB Atlas.")

    if errors:
        return False, errors

    return True, []
