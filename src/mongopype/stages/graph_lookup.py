from typing import TypedDict, NotRequired
from ..types import Version, Expression, Document



GraphLookupSpec = TypedDict(
    "GraphLookupSpec",
    {
        "from": str,
        "startWith": Expression,
        "connectFromField": str,
        "connectToField": str,
        "as": str,
        "maxDepth": NotRequired[int],
        "depthField": NotRequired[str],
        "restrictSearchWithMatch": NotRequired[Document],
    },
)


GraphLookupKwargsSpec = TypedDict(
    "GraphLookupKwargsSpec",
    {
        "from_": str,
        "startWith": Expression,
        "connectFromField": str,
        "connectToField": str,
        "as_": str,
        "maxDepth": NotRequired[int],
        "depthField": NotRequired[str],
        "restrictSearchWithMatch": NotRequired[Document],
    },
)

GraphLookup = TypedDict("GraphLookup", {"$graphLookup": GraphLookupSpec})
"""
$graphLookup stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/graphLookup/
"""



def verify_graph_lookup(
    spec: GraphLookupSpec,
    version: Version,
    pipeline_index: int,
    pipeline_length: int,
    is_atlas: bool,
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    if "maxDepth" in spec:
        max_depth = spec["maxDepth"]
        if max_depth < 0:
            errors.append("$graphLookup 'maxDepth' must be a non-negative integer.")

    if errors:
        return False, errors

    return True, []
