from typing import Literal, Any

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/indexStats/

IndexStats = dict[Literal["$indexStats"], dict[str, Any]]

def verify_index_stats(stage: IndexStats, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (no options; stage shape is fixed)
    return True
