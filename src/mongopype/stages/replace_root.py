from typing import TypedDict
from ..types import Expression

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/replaceRoot/


class ReplaceRootSpec(TypedDict):
    newRoot: Expression


ReplaceRoot = TypedDict("ReplaceRoot", {"$replaceRoot": ReplaceRootSpec})

def verify_replace_root(spec: ReplaceRootSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic
    return True
