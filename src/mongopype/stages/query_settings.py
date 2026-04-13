# Done

from typing import TypedDict
from ..types import Version

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/querySettings/


class QuerySettingsSpec(TypedDict, total=False):
    showDebugQueryShape: bool


QuerySettings = TypedDict("QuerySettings", {"$querySettings": QuerySettingsSpec})
"""
$querySettings stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/querySettings/
"""


def verify_query_settings(
    spec: QuerySettingsSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors = []

    if version < (8, 0):
        errors.append("$querySettings requires MongoDB >= 8.0.")

    if pipeline_index != 0:
        errors.append("$querySettings must be the first stage in the pipeline.")

    if errors:
        return False, errors

    return True, []
