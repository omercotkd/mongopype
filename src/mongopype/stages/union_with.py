from typing import Any, TypedDict

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/unionWith/

UnionWithSpec = dict[str, Any]

UnionWith = TypedDict("UnionWith", {"$unionWith": UnionWithSpec})

def verify_union_with(spec: UnionWithSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (pipeline or coll rules)
    return True
