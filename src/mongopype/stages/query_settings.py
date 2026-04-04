from typing import Any, TypedDict

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/querySettings/

QuerySettingsSpec = dict[str, Any]

QuerySettings = TypedDict("QuerySettings", {"$querySettings": QuerySettingsSpec})

def verify_query_settings(spec: QuerySettingsSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (must be first stage)
    return True
