from typing import TypedDict
from ..types import Version


UnsetSpec = str | list[str]

Unset = TypedDict("Unset", {"$unset": UnsetSpec})
"""
$unset stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/unset/
"""


def verify_unset(
    spec: UnsetSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    if version < (4, 2):
        errors.append("$unset requires MongoDB >= 4.2.")

    if errors:
        return False, errors

    return True, []
