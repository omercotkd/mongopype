from typing import Any, TypedDict

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/currentOp/

CurrentOpSpec = dict[str, Any]

CurrentOp = TypedDict("CurrentOp", {"$currentOp": CurrentOpSpec})

def verify_current_op(spec: CurrentOpSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (requires admin privileges)
    return True
