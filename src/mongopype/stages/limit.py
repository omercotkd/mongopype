from typing import TypedDict

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/limit/

LimitSpec = int

Limit = TypedDict("Limit", {"$limit": LimitSpec})

def verify_limit(spec: LimitSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (non-negative check)
    return True
