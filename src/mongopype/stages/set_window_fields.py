from typing import Literal, Any

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/setWindowFields/

SetWindowFields = dict[Literal["$setWindowFields"], dict[str, Any]]

def verify_set_window_fields(stage: SetWindowFields, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (partitionBy, sortBy, output specs)
    return True
