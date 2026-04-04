from typing import Any, TypedDict

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/queryStats/

QueryStatsSpec = dict[str, Any]

QueryStats = TypedDict("QueryStats", {"$queryStats": QueryStatsSpec})

def verify_query_stats(spec: QueryStatsSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic
    return True
