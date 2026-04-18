from typing import Any, TypedDict, NotRequired
from ..types import Version



class ScoreSpec(TypedDict):
    score: Any
    scoreDetails: NotRequired[bool]
    normalization: NotRequired[str]
    weight: NotRequired[float]



Score = TypedDict("Score", {"$score": ScoreSpec})
"""
$score stage (Atlas only):
https://www.mongodb.com/docs/manual/reference/operator/aggregation/score/
"""


def verify_score(
    spec: ScoreSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    if not is_atlas:
        errors.append("$score is only available on MongoDB Atlas.")

    if errors:
        return False, errors

    return True, []
