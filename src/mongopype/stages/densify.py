from typing import TypedDict, NotRequired, Literal, Any
from ..types import Version, TimeUnit


class DensifyRange(TypedDict):
    bounds: Literal["full", "partition"] | tuple[Any, Any]
    step: int | float
    unit: NotRequired[TimeUnit]


class DensifySpec(TypedDict):
    field: str
    range: DensifyRange
    partitionByFields: NotRequired[list[str]]


Densify = TypedDict("Densify", {"$densify": DensifySpec})
"""
$densify stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/densify/
"""


def verify_densify(
    spec: DensifySpec,
    version: Version,
    pipeline_index: int,
    pipeline_length: int,
    is_atlas: bool,
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    if version < (5, 1):
        errors.append("$densify requires MongoDB >= 5.1.")

    if spec["range"]["step"] <= 0:
        errors.append(
            f"$densify 'range.step' must be a positive number, got {spec['range']['step']}."
        )

    if errors:
        return False, errors

    return True, []
