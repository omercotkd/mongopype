# Done

from typing import TypedDict
from ..types import SortOrder, Version

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/sort/

SortSpec = SortOrder

Sort = TypedDict("Sort", {"$sort": SortSpec})
"""
$sort stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/sort/
"""


def verify_sort(
    spec: SortSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors = []

    if not spec:
        errors.append("$sort must specify at least one sort field.")

    if len(spec) > 32:
        errors.append(f"$sort cannot have more than 32 sort keys, got {len(spec)}.")

    if errors:
        return False, errors

    return True, []
