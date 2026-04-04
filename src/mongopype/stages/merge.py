from typing import Any, TypedDict

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/merge/

MergeSpec = dict[str, Any]

Merge = TypedDict("Merge", {"$merge": MergeSpec})

def verify_merge(spec: MergeSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (into required; on optional; version-specific rules)
    return True
