from typing import Any, TypedDict

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/planCacheStats/

PlanCacheStatsSpec = dict[str, Any]

PlanCacheStats = TypedDict("PlanCacheStats", {"$planCacheStats": PlanCacheStatsSpec})

def verify_plan_cache_stats(spec: PlanCacheStatsSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic
    return True
