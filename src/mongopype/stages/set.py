# Done

from typing import TypedDict
from ..types import Expression, Version

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/set/

SetSpec = dict[str, Expression]

Set = TypedDict("Set", {"$set": SetSpec})
"""
$set stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/set/
"""


def verify_set(
    spec: SetSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors = []

    if version < (4, 2):
        errors.append("$set requires MongoDB >= 4.2.")

    if errors:
        return False, errors

    return True, []
