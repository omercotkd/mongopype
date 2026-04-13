# Done

from typing import Literal, TypedDict, Union
from ..types import Version, Expression, SortOrder

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/fill/


class FillOutputValueField(TypedDict):
    value: Expression


class FillOutputMethodField(TypedDict):
    method: Literal["linear", "locf"]


FillOutputField = Union[FillOutputValueField, FillOutputMethodField]


class FillSpec(TypedDict, total=False):
    partitionBy: Expression
    partitionByFields: list[str]
    sortBy: SortOrder
    output: dict[str, FillOutputField]


Fill = TypedDict("Fill", {"$fill": FillSpec})
"""
$fill stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/fill/
"""


def verify_fill(
    spec: FillSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors = []

    if version < (5, 3):
        errors.append("$fill requires MongoDB >= 5.3.")

    if "output" not in spec:
        errors.append("$fill requires the 'output' field.")

    if "partitionBy" in spec and "partitionByFields" in spec:
        errors.append("$fill cannot specify both 'partitionBy' and 'partitionByFields'.")

    if "output" in spec and isinstance(spec["output"], dict):
        for field_name, field_spec in spec["output"].items():
            if isinstance(field_spec, dict):
                has_method = "method" in field_spec
                if has_method and "sortBy" not in spec:
                    errors.append(
                        f"$fill output field '{field_name}' uses 'method' but no 'sortBy' is specified."
                    )

    if errors:
        return False, errors

    return True, []
