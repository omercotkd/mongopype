from typing import Any, TypedDict

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/changeStream/

ChangeStreamSpec = dict[str, Any]

ChangeStream = TypedDict("ChangeStream", {"$changeStream": ChangeStreamSpec})

def verify_change_stream(spec: ChangeStreamSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (must be first stage, version checks)
    return True
