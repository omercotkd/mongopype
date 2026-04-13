# Done

from typing import TypedDict
from ..types import Version

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/currentOp/


class CurrentOpSpec(TypedDict, total=False):
    allUsers: bool
    idleConnections: bool
    idleCursors: bool
    idleSessions: bool
    localOps: bool
    targetAllNodes: bool


CurrentOp = TypedDict("CurrentOp", {"$currentOp": CurrentOpSpec})
"""
$currentOp stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/currentOp/
"""


def verify_current_op(
    spec: CurrentOpSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors = []

    if pipeline_index != 0:
        errors.append("$currentOp must be the first stage in the pipeline.")

    if "targetAllNodes" in spec and version < (7, 1):
        errors.append("$currentOp 'targetAllNodes' requires MongoDB >= 7.1.")

    if errors:
        return False, errors

    return True, []
