from typing import Literal

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/limit/

Limit = dict[Literal["$limit"], int]

def verify_limit(stage: Limit, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (non-negative check)
    return True
