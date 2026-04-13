# Done

from typing import Union, TypedDict
from ..types import Version, OutputInto, OutputIntoTimeSeries

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/out/

OutSpec = Union[str, OutputInto, OutputIntoTimeSeries]

Out = TypedDict("Out", {"$out": OutSpec})
"""
$out stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/out/
"""


def verify_out(
    spec: OutSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors = []

    if pipeline_index != pipeline_length - 1:
        errors.append("$out must be the last stage in the pipeline.")

    if isinstance(spec, str):
        if not spec:
            errors.append("$out collection name must not be empty.")
    elif isinstance(spec, dict):
        if "db" not in spec or "coll" not in spec:
            errors.append("$out document form requires 'db' and 'coll' fields.")
        if "timeseries" in spec and version < (7, 0):
            errors.append("$out with 'timeseries' requires MongoDB >= 7.0.")

    if errors:
        return False, errors

    return True, []
