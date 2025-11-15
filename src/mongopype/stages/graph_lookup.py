from typing import Literal, Any

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/graphLookup/

GraphLookup = dict[Literal["$graphLookup"], dict[str, Any]]

def verify_graph_lookup(stage: GraphLookup, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (required fields present)
    return True
