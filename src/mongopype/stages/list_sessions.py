from typing import NotRequired, TypedDict
from ..types import Version, UserDocument



class _AllUsersSpec(TypedDict):
    allUsers: bool


class _UsersSpec(TypedDict):
    users: list[UserDocument]


ListSessionsSpec = _AllUsersSpec | _UsersSpec


class ListSessionsKwargsSpec(TypedDict):
    allUsers: NotRequired[bool]
    users: NotRequired[list[UserDocument]]

ListSessions = TypedDict("ListSessions", {"$listSessions": ListSessionsSpec})
"""
$listSessions stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/listSessions/
"""


def verify_list_sessions(
    spec: ListSessionsSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    if pipeline_index != 0:
        errors.append("$listSessions must be the first stage in the pipeline.")

    if "allUsers" in spec and "users" in spec:
        errors.append("$listSessions cannot specify both 'allUsers' and 'users'.")

    if errors:
        return False, errors

    return True, []
