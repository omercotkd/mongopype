
from typing import TypedDict
from ..types import Expression, Version

SortByCountSpec = Expression

SortByCount = TypedDict("SortByCount", {"$sortByCount": SortByCountSpec})
"""
$sortByCount stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/sortByCount/
"""


def verify_sort_by_count(
    spec: SortByCountSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    if isinstance(spec, str) and not spec.startswith("$"):
        errors.append(f"$sortByCount expression string must start with '$', got '{spec}'.")

    if errors:
        return False, errors

    return True, []
