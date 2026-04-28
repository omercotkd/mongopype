from typing import Literal, TypedDict, NotRequired
from ..types import Version, Expression, SortOrder

class FillOutputValueField(TypedDict):
    value: Expression


class FillOutputMethodField(TypedDict):
    method: Literal["linear", "locf"]


FillOutputField = FillOutputValueField | FillOutputMethodField


class FillSpec(TypedDict):
    partitionBy: NotRequired[Expression]
    partitionByFields: NotRequired[list[str]]
    sortBy: NotRequired[SortOrder]
    output: dict[str, FillOutputField]


Fill = TypedDict("Fill", {"$fill": FillSpec})
"""
$fill stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/fill/
"""


def verify_fill(
    spec: FillSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    if version < (5, 3):
        errors.append("$fill requires MongoDB >= 5.3.")

    if "output" not in spec:
        errors.append("$fill requires the 'output' field.")

    if "partitionBy" in spec and "partitionByFields" in spec:
        errors.append("$fill cannot specify both 'partitionBy' and 'partitionByFields'.")


    for field_name, field_spec in spec["output"].items():
        has_method = "method" in field_spec
        if has_method and "sortBy" not in spec:
            errors.append(
                f"$fill output field '{field_name}' uses 'method' but no 'sortBy' is specified."
            )

    if errors:
        return False, errors

    return True, []
