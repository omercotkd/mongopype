from typing import Literal, Any

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/querySettings/

QuerySettings = dict[Literal["$querySettings"], dict[str, Any]]

def verify_query_settings(stage: QuerySettings, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (must be first stage)
    return True
