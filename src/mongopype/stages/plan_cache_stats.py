from typing import TypedDict, NotRequired
from ..types import Version



class PlanCacheStatsSpec(TypedDict):
    allHosts: NotRequired[bool]


PlanCacheStats = TypedDict("PlanCacheStats", {"$planCacheStats": PlanCacheStatsSpec})
"""
$planCacheStats stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/planCacheStats/
"""


def verify_plan_cache_stats(
    spec: PlanCacheStatsSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    if pipeline_index != 0:
        errors.append("$planCacheStats must be the first stage in the pipeline.")

    if errors:
        return False, errors

    return True, []
