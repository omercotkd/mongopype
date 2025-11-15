from typing import Literal, Any

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/collStats/

CollStats = dict[Literal["$collStats"], dict[str, Any]]

def verify_coll_stats(stage: CollStats, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic
    return True
