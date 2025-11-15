from typing import Literal, Union
from ..types import Expression, AccumulatorExpression

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/group/

Group = dict[Literal["$group"], dict[str, Union[Expression, AccumulatorExpression]]]

def verify_group(stage: Group, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (_id required, accumulator forms)
    return True
