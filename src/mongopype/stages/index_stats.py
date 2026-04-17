from typing import TypedDict
from ..types import Version


IndexStatsSpec = dict[str, object]

IndexStats = TypedDict("IndexStats", {"$indexStats": IndexStatsSpec})
"""
$indexStats stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/indexStats/
"""


def verify_index_stats(
    spec: IndexStatsSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    if pipeline_index != 0:
        errors.append("$indexStats must be the first stage in the pipeline.")

    if spec:
        errors.append("$indexStats takes an empty document {}.")

    if errors:
        return False, errors

    return True, []
