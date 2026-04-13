# Done

from typing import TypedDict
from ..types import Version

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/planCacheStats/


class PlanCacheStatsSpec(TypedDict, total=False):
    allHosts: bool


PlanCacheStats = TypedDict("PlanCacheStats", {"$planCacheStats": PlanCacheStatsSpec})
"""
$planCacheStats stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/planCacheStats/
"""


def verify_plan_cache_stats(
    spec: PlanCacheStatsSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors = []

    if pipeline_index != 0:
        errors.append("$planCacheStats must be the first stage in the pipeline.")

    if errors:
        return False, errors

    return True, []
