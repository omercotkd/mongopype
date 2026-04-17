from typing import Any, TypedDict
from ..types import Version, Expression, SortOrder



class SetWindowFieldsSpec(TypedDict, total=False):
    partitionBy: Expression
    sortBy: SortOrder
    output: dict[str, Any]


SetWindowFields = TypedDict("SetWindowFields", {"$setWindowFields": SetWindowFieldsSpec})
"""
$setWindowFields stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/setWindowFields/
"""


def verify_set_window_fields(
    spec: SetWindowFieldsSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    if version < (5, 0):
        errors.append("$setWindowFields requires MongoDB >= 5.0.")

    if "output" not in spec:
        errors.append("$setWindowFields requires the 'output' field.")

    if errors:
        return False, errors

    return True, []
