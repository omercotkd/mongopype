# Done

from typing import Literal, TypedDict
from ..types import Expression, AccumulatorExpression, Version


class BucketAutoSpec(TypedDict, total=True):
    groupBy: Expression
    buckets: int
    output: dict[str, AccumulatorExpression]
    granularity: Literal[
        "R5",
        "R10",
        "R20",
        "R40",
        "R80",
        "1-2-5",
        "E6",
        "E12",
        "E24",
        "E48",
        "E96",
        "E192",
        "POWERSOF2",
    ]


BucketAuto = TypedDict("BucketAuto", {"$bucketAuto": BucketAutoSpec})
"""
$bucketAuto stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/bucketAuto/
"""


def verify_bucket_auto(
    spec: BucketAutoSpec, version: Version, pipeline_index: int
) -> tuple[bool, list[str]]:

    errors = []

    # buckets must be positve 32-bit integer
    if not (isinstance(spec["buckets"], int) and 0 < spec["buckets"] <= 2**31 - 1):
        errors.append(
            f"Invalid 'buckets' value: {spec['buckets']}. Must be a positive 32-bit integer."
        )

    for key, value in spec["output"].items():
        if not len(value) == 1:
            errors.append(f"Invalid output specification for field '{key}': {value}. Must contain exactly one accumulator expression.")
    
    if errors:
        return False, errors

    return True, []
