from typing import Literal
from ..types import Expression

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/replaceWith/

ReplaceWith = dict[Literal["$replaceWith"], Expression]

def verify_replace_with(stage: ReplaceWith, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic
    return True
