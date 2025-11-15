from typing import Literal, TypedDict, Union, Any
from datetime import datetime
from ..types import AccumulatorExpression, Expression

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/bucket/


class BucketSpec(TypedDict):
    groupBy: Expression
    boundaries: Union[list[int], list[float], list[str], list[datetime]]
    # TODO find better type for "default"
    default: Any
    output: dict[str, AccumulatorExpression]


Bucket = dict[
    Literal["$bucket"],
    BucketSpec,
]

def verify_bucket(stage: Bucket, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic
    return True
