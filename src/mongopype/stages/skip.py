from typing import Literal

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/skip/

Skip = dict[Literal["$skip"], int]

def verify_skip(stage: Skip, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (non-negative check)
    return True
