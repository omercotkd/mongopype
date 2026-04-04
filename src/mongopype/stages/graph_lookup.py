from typing import Any, TypedDict

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/graphLookup/

GraphLookupSpec = dict[str, Any]

GraphLookup = TypedDict("GraphLookup", {"$graphLookup": GraphLookupSpec})

def verify_graph_lookup(spec: GraphLookupSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (required fields present)
    return True
