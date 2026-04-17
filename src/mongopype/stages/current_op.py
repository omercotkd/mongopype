from typing import TypedDict, NotRequired
from ..types import Version

class CurrentOpSpec(TypedDict, total=False):
    allUsers: NotRequired[bool]
    idleConnections: NotRequired[bool]
    idleCursors: NotRequired[bool]
    idleSessions: NotRequired[bool]
    localOps: NotRequired[bool]
    targetAllNodes: NotRequired[bool]


CurrentOp = TypedDict("CurrentOp", {"$currentOp": CurrentOpSpec})
"""
$currentOp stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/currentOp/
"""


def verify_current_op(
    spec: CurrentOpSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    if pipeline_index != 0:
        errors.append("$currentOp must be the first stage in the pipeline.")

    if "targetAllNodes" in spec and version < (7, 1):
        errors.append("$currentOp 'targetAllNodes' requires MongoDB >= 7.1.")

    if errors:
        return False, errors

    return True, []
