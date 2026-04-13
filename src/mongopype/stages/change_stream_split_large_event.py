# Done

from typing import TypedDict
from ..types import Version

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/changeStreamSplitLargeEvent/

ChangeStreamSplitLargeEventSpec = dict[str, object]

ChangeStreamSplitLargeEvent = TypedDict(
    "ChangeStreamSplitLargeEvent",
    {"$changeStreamSplitLargeEvent": ChangeStreamSplitLargeEventSpec},
)
"""
$changeStreamSplitLargeEvent stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/changeStreamSplitLargeEvent/
"""


def verify_change_stream_split_large_event(
    spec: ChangeStreamSplitLargeEventSpec,
    version: Version,
    pipeline_index: int,
    pipeline_length: int,
    is_atlas: bool,
) -> tuple[bool, list[str]]:

    errors = []

    if version < (7, 0):
        errors.append("$changeStreamSplitLargeEvent requires MongoDB >= 7.0.")

    if pipeline_index != pipeline_length - 1:
        errors.append("$changeStreamSplitLargeEvent must be the last stage in the pipeline.")

    if spec:
        errors.append("$changeStreamSplitLargeEvent takes an empty document {}.")

    if errors:
        return False, errors

    return True, []
