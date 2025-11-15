from typing import Literal, Any

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/listSessions/

ListSessions = dict[Literal["$listSessions"], dict[str, Any]]

def verify_list_sessions(stage: ListSessions, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic
    return True
