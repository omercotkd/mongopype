from typing import TypedDict, NotRequired
from ..types import Version


class ListSearchIndexesSpec(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]


ListSearchIndexes = TypedDict("ListSearchIndexes", {"$listSearchIndexes": ListSearchIndexesSpec})
"""
$listSearchIndexes stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/listSearchIndexes/
"""


def verify_list_search_indexes(
    spec: ListSearchIndexesSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    if not is_atlas:
        errors.append("$listSearchIndexes is only available on MongoDB Atlas.")

    if version < (7, 0):
        errors.append("$listSearchIndexes requires MongoDB >= 7.0.")

    if "id" in spec and "name" in spec:
        errors.append("$listSearchIndexes cannot specify both 'id' and 'name'.")

    if errors:
        return False, errors

    return True, []
