# Done

from typing import Any, TypedDict
from ..types import Version

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/score/


class ScoreSpec(TypedDict, total=False):
    score: Any
    normalizeFunction: str
    weight: float


Score = TypedDict("Score", {"$score": ScoreSpec})
"""
$score stage (Atlas only):
https://www.mongodb.com/docs/manual/reference/operator/aggregation/score/
"""


def verify_score(
    spec: ScoreSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors = []

    if not is_atlas:
        errors.append("$score is only available on MongoDB Atlas.")

    if "score" not in spec:
        errors.append("$score requires the 'score' field.")

    if errors:
        return False, errors

    return True, []
