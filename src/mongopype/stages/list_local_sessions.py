from typing import Literal, Any

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/listLocalSessions/

ListLocalSessions = dict[Literal["$listLocalSessions"], dict[str, Any]]

def verify_list_local_sessions(stage: ListLocalSessions, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic
    return True
