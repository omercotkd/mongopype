from typing import NotRequired, Union, TypedDict
from ..types import Version, UserDocument



class _AllUsersSpec(TypedDict):
    allUsers: bool


class _UsersSpec(TypedDict):
    users: list[UserDocument]


ListLocalSessionsSpec = Union[_AllUsersSpec, _UsersSpec]


class ListLocalSessionsKwargsSpec(TypedDict):
    allUsers: NotRequired[bool]
    users: NotRequired[list[UserDocument]]


ListLocalSessions = TypedDict("ListLocalSessions", {"$listLocalSessions": ListLocalSessionsSpec})
"""
$listLocalSessions stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/listLocalSessions/
"""


def verify_list_local_sessions(
    spec: ListLocalSessionsSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    if pipeline_index != 0:
        errors.append("$listLocalSessions must be the first stage in the pipeline.")

    if "allUsers" in spec and "users" in spec:
        errors.append("$listLocalSessions cannot specify both 'allUsers' and 'users'.")

    if errors:
        return False, errors

    return True, []
