from typing import Literal
from ..types import Expression

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/replaceRoot/

ReplaceRoot = dict[Literal["$replaceRoot"], dict[Literal["newRoot"], Expression]]

def verify_replace_root(stage: ReplaceRoot, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic
    return True
