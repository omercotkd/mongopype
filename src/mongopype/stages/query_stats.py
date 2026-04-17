# Done

from typing import Literal, TypedDict, Any
from ..types import Version

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/queryStats/


class TransformIdentifiersSpec(TypedDict, total=False):
    algorithm: Literal["hmac-sha-256"]
    hmacKey: Any

class QueryStatsSpec(TypedDict, total=False):
    transformIdentifiers: TransformIdentifiersSpec


QueryStats = TypedDict("QueryStats", {"$queryStats": QueryStatsSpec})
"""
$queryStats stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/queryStats/
"""


def verify_query_stats(
    spec: QueryStatsSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    if not is_atlas:
        errors.append("$queryStats is only supported on MongoDB Atlas.")
    
    if version < (8, 0):
        errors.append("$queryStats requires MongoDB >= 8.0.")

    if pipeline_index != 0:
        errors.append("$queryStats must be the first stage in the pipeline.")

    if errors:
        return False, errors

    return True, []
