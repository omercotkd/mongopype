from typing import Literal, Any

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/merge/

Merge = dict[Literal["$merge"], dict[str, Any]]

def verify_merge(stage: Merge, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (into required; on optional; version-specific rules)
    return True
