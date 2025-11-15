from typing import Literal
from ..types import Expression

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/set/

Set = dict[Literal["$set"], dict[str, Expression]]

def verify_set(stage: Set, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic
    return True
