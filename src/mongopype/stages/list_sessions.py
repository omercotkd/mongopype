# Done

from typing import Union, TypedDict
from ..types import Version, UserDocument

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/listSessions/


class _AllUsersSpec(TypedDict, total=False):
    allUsers: bool


class _UsersSpec(TypedDict, total=False):
    users: list[UserDocument]


ListSessionsSpec = Union[_AllUsersSpec, _UsersSpec]


class ListSessionsKwargsSpec(TypedDict, total=False):
    allUsers: bool
    users: list[UserDocument]


ListSessions = TypedDict("ListSessions", {"$listSessions": ListSessionsSpec})
"""
$listSessions stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/listSessions/
"""


def verify_list_sessions(
    spec: ListSessionsSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors = []

    if pipeline_index != 0:
        errors.append("$listSessions must be the first stage in the pipeline.")

    if isinstance(spec, dict) and "allUsers" in spec and "users" in spec:
        errors.append("$listSessions cannot specify both 'allUsers' and 'users'.")

    if errors:
        return False, errors

    return True, []
