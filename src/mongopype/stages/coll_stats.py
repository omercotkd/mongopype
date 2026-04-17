from typing import TypedDict
from ..types import Version


class LatencyStatsOptions(TypedDict, total=False):
    histograms: bool


class StorageStatsOptions(TypedDict, total=False):
    scale: int


class CollStatsSpec(TypedDict, total=False):
    latencyStats: LatencyStatsOptions
    storageStats: StorageStatsOptions
    count: dict[str, object]
    queryExecStats: dict[str, object]


CollStats = TypedDict("CollStats", {"$collStats": CollStatsSpec})
"""
$collStats stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/collStats/
"""


def verify_coll_stats(
    spec: CollStatsSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    if pipeline_index != 0:
        errors.append("$collStats must be the first stage in the pipeline.")

    if errors:
        return False, errors

    return True, []
