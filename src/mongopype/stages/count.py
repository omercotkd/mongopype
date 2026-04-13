# Done

from typing import TypedDict
from ..types import Version

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/count/

CountSpec = str

Count = TypedDict("Count", {"$count": CountSpec})
"""
$count stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/count/
"""


def verify_count(
    spec: CountSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors = []

    if not isinstance(spec, str):
        errors.append("$count spec must be a string.")
    else:
        if not spec:
            errors.append("$count field name must be non-empty.")
        if spec.startswith("$"):
            errors.append(f"$count field name '{spec}' must not start with '$'.")
        if "." in spec:
            errors.append(f"$count field name '{spec}' must not contain '.'.")

    if errors:
        return False, errors

    return True, []
