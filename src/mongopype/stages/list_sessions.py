from typing import Any, TypedDict

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/listSessions/

ListSessionsSpec = dict[str, Any]

ListSessions = TypedDict("ListSessions", {"$listSessions": ListSessionsSpec})

def verify_list_sessions(spec: ListSessionsSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic
    return True
