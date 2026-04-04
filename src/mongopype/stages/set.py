from typing import TypedDict
from ..types import Expression

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/set/

SetSpec = dict[str, Expression]

Set = TypedDict("Set", {"$set": SetSpec})

def verify_set(spec: SetSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic
    return True
