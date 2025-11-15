from typing import Literal, Any

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/unionWith/

UnionWith = dict[Literal["$unionWith"], dict[str, Any]]

def verify_union_with(stage: UnionWith, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (pipeline or coll rules)
    return True
