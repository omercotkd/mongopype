# Done

from typing import TypedDict
from ..types import Version

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/sample/


class SampleSpec(TypedDict):
    size: int


Sample = TypedDict("Sample", {"$sample": SampleSpec})
"""
$sample stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/sample/
"""


def verify_sample(
    spec: SampleSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors = []

    if not isinstance(spec.get("size"), int) or spec["size"] < 0:  # type: ignore
        errors.append(f"$sample 'size' must be a non-negative integer, got {spec.get('size')}.")

    if errors:
        return False, errors

    return True, []
