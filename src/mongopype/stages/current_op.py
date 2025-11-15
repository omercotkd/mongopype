from typing import Literal, Any

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/currentOp/

CurrentOp = dict[Literal["$currentOp"], dict[str, Any]]

def verify_current_op(stage: CurrentOp, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (requires admin privileges)
    return True
