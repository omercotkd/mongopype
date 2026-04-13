# Done

from typing import Optional, TypedDict, Any
from ..types import (
    ChaneStreamFullDocumentOptions,
    ChaneStreamFullDocumentBeforeChangeOptions,
    Version,
)

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/changeStream/


class ChangeStreamSpec(TypedDict, total=False):
    allChangesForCluster: bool
    fullDocument: ChaneStreamFullDocumentOptions
    fullDocumentBeforeChange: ChaneStreamFullDocumentBeforeChangeOptions
    resumeAfter: dict[str, Any]
    showExpandedEvents: bool
    startAfter: dict[str, Any]
    startAtOperationTime: Any


ChangeStream = TypedDict("ChangeStream", {"$changeStream": ChangeStreamSpec})
"""
$changeStream stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/changeStream/
"""


def verify_change_stream(
    spec: ChangeStreamSpec,
    version: Version,
    pipeline_index: int,
    pipeline_length: int,
    is_atlas: bool,
) -> tuple[bool, list[str]]:

    errors = []

    if pipeline_index != 0:
        errors.append("$changeStream must be the first stage in the pipeline.")

    if "showExpandedEvents" in spec and version < (6, 0):
        errors.append("$changeStream 'showExpandedEvents' requires MongoDB >= 6.0.")

    # resumeAfter, startAfter, startAtOperationTime are mutually exclusive
    resume_fields = ["resumeAfter", "startAfter", "startAtOperationTime"]
    present = [f for f in resume_fields if f in spec]
    if len(present) > 1:
        errors.append(
            f"$changeStream fields {', '.join(present)} are mutually exclusive."
        )

    if errors:
        return False, errors

    return True, []
