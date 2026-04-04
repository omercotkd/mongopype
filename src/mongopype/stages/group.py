from typing import Union, TypedDict
from ..types import Expression, AccumulatorExpression

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/group/

GroupSpec = dict[str, Union[Expression, AccumulatorExpression]]

Group = TypedDict("Group", {"$group": GroupSpec})

def verify_group(spec: GroupSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (_id required, accumulator forms)
    return True
