from typing import TypedDict
from ..types import Version


SkipSpec = int

Skip = TypedDict("Skip", {"$skip": SkipSpec})
"""
$skip stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/skip/
"""


def verify_skip(
    spec: SkipSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    if spec < 0:
        errors.append(f"$skip value must be a non-negative integer, got {spec}.")

    if errors:
        return False, errors

    return True, []
