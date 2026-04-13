# Done

from typing import Union, TypedDict
from ..types import Version

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/unwind/


class UnwindDocSpec(TypedDict, total=False):
    path: str
    includeArrayIndex: str
    preserveNullAndEmptyArrays: bool


UnwindSpec = Union[str, UnwindDocSpec]

Unwind = TypedDict("Unwind", {"$unwind": UnwindSpec})
"""
$unwind stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/unwind/
"""


def verify_unwind(
    spec: UnwindSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors = []

    if isinstance(spec, str):
        if not spec.startswith("$"):
            errors.append("$unwind path must start with '$'.")
    elif isinstance(spec, dict):
        if "path" not in spec:
            errors.append("$unwind document form requires a 'path' field.")
        elif isinstance(spec["path"], str) and not spec["path"].startswith("$"):
            errors.append("$unwind 'path' must start with '$'.")

    if errors:
        return False, errors

    return True, []
