from typing import Literal, TypedDict
from ..types import Expression, AccumulatorExpression

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/bucketAuto/

Granularity = Literal[
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

class BucketAutoSpec(TypedDict, total=False):
    groupBy: Expression
    buckets: int
    output: dict[str, AccumulatorExpression]
    granularity: Granularity

BucketAuto = dict[Literal["$bucketAuto"], BucketAutoSpec]

def verify_bucket_auto(stage: BucketAuto, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (buckets > 1, boundaries ordering, granularity valid for version)
    return True
