from typing import Any, TypedDict

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/indexStats/

IndexStatsSpec = dict[str, Any]

IndexStats = TypedDict("IndexStats", {"$indexStats": IndexStatsSpec})

def verify_index_stats(spec: IndexStatsSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (no options; stage shape is fixed)
    return True
