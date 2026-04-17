from typing import Any, TypedDict
from ..types import Version

# (Future) Placeholder for $scoreFusion stage if available


class ScoreFusionSpec(TypedDict, total=False):
    inputNormalization: str
    combination: dict[str, Any]


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
