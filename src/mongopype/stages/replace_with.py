from typing import TypedDict
from ..types import Expression, Version


ReplaceWithSpec = Expression

ReplaceWith = TypedDict("ReplaceWith", {"$replaceWith": ReplaceWithSpec})
"""
$replaceWith stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/replaceWith/
"""


def verify_replace_with(
    spec: ReplaceWithSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    if version < (4, 2):
        errors.append("$replaceWith requires MongoDB >= 4.2.")

    if errors:
        return False, errors

    return True, []
