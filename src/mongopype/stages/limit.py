# Done

from typing import TypedDict
from ..types import Version

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/limit/

LimitSpec = int

Limit = TypedDict("Limit", {"$limit": LimitSpec})
"""
$limit stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/limit/
"""


def verify_limit(
    spec: LimitSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors = []

    if not isinstance(spec, int) or spec <= 0:
        errors.append(f"$limit value must be a positive integer, got {spec}.")

    if errors:
        return False, errors

    return True, []
