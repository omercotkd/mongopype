from typing import TypedDict
from ..types import DensifyRange, Version


class DensifySpec(TypedDict, total=False):
    field: str
    range: DensifyRange
    partitionByFields: list[str]


DensifySpec.__required_keys__ = frozenset({"field", "range"})


Densify = TypedDict("Densify", {"$densify": DensifySpec})
"""
$densify stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/densify/
"""


def verify_densify(
    spec: DensifySpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    if version < (5, 1):
        errors.append("$densify requires MongoDB >= 5.1.")

    if "field" not in spec:
        errors.append("$densify requires the 'field' field.")

    if "range" not in spec:
        errors.append("$densify requires the 'range' field.")
    else:
        range_spec = spec["range"]
        if "step" not in range_spec:
            errors.append("$densify 'range' requires the 'step' field.")
        elif range_spec["step"] <= 0:
            errors.append(f"$densify 'range.step' must be a positive number, got {range_spec['step']}.")
        if "bounds" not in range_spec:
            errors.append("$densify 'range' requires the 'bounds' field.")

    if errors:
        return False, errors

    return True, []
