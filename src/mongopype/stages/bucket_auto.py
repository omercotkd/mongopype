from typing import Literal, TypedDict, NotRequired
from ..types import Expression, AccumulatorExpression, Version
from ..verify import verify_accumulator_expression

class BucketAutoSpec(TypedDict, total=True):
    groupBy: Expression
    buckets: int
    output: NotRequired[dict[str, AccumulatorExpression]]
    granularity: NotRequired[Literal[
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
    ]]


BucketAuto = TypedDict("BucketAuto", {"$bucketAuto": BucketAutoSpec})
"""
$bucketAuto stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/bucketAuto/
"""


def verify_bucket_auto(
    spec: BucketAutoSpec,
    version: Version,
    pipeline_index: int,
    pipeline_length: int,
    is_atlas: bool,
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    # buckets must be positve 32-bit integer
    if not 0 < spec["buckets"] <= 2**31 - 1:
        errors.append(
            f"Invalid 'buckets' value: {spec['buckets']}. Must be a positive 32-bit integer."
        )

    if "output" in spec:
        for key, value in spec["output"].items():
            is_valid, error = verify_accumulator_expression(value, version)
            if not is_valid:
                errors.append(f"Invalid output specification for field '{key}': {error}")


    if errors:
        return False, errors

    return True, []
