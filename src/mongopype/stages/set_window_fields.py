from typing import Any, TypedDict

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/setWindowFields/

SetWindowFieldsSpec = dict[str, Any]

SetWindowFields = TypedDict("SetWindowFields", {"$setWindowFields": SetWindowFieldsSpec})

def verify_set_window_fields(spec: SetWindowFieldsSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (partitionBy, sortBy, output specs)
    return True
