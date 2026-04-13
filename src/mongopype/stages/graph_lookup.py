# Done

from typing import TypedDict
from ..types import Version, Expression, Document

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/graphLookup/


class GraphLookupSpec(TypedDict, total=False):
    from_: str  # Note: actual key is 'from'
    startWith: Expression
    connectFromField: str
    connectToField: str
    as_: str  # Note: actual key is 'as'
    maxDepth: int
    depthField: str
    restrictSearchWithMatch: Document


GraphLookup = TypedDict("GraphLookup", {"$graphLookup": GraphLookupSpec})
"""
$graphLookup stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/graphLookup/
"""

_REQUIRED_FIELDS = ["from", "startWith", "connectFromField", "connectToField", "as"]


def verify_graph_lookup(
    spec: GraphLookupSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors = []

    for field in _REQUIRED_FIELDS:
        if field not in spec:
            errors.append(f"$graphLookup requires the '{field}' field.")

    if "maxDepth" in spec:
        max_depth = spec["maxDepth"]
        if not isinstance(max_depth, int) or max_depth < 0:
            errors.append("$graphLookup 'maxDepth' must be a non-negative integer.")

    if errors:
        return False, errors

    return True, []
