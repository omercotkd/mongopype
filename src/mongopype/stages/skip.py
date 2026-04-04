from typing import TypedDict

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/skip/

SkipSpec = int

Skip = TypedDict("Skip", {"$skip": SkipSpec})

def verify_skip(spec: SkipSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (non-negative check)
    return True
