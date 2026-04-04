from typing import Any, TypedDict

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/listLocalSessions/

ListLocalSessionsSpec = dict[str, Any]

ListLocalSessions = TypedDict("ListLocalSessions", {"$listLocalSessions": ListLocalSessionsSpec})

def verify_list_local_sessions(spec: ListLocalSessionsSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic
    return True
