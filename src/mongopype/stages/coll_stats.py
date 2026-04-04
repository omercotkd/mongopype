from typing import Any, TypedDict

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/collStats/

CollStatsSpec = dict[str, Any]

CollStats = TypedDict("CollStats", {"$collStats": CollStatsSpec})

def verify_coll_stats(spec: CollStatsSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic
    return True
