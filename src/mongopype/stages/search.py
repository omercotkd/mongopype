# Done

from typing import Any, TypedDict
from ..types import Version

# https://www.mongodb.com/docs/atlas/atlas-search/

SearchSpec = dict[str, Any]

Search = TypedDict("Search", {"$search": SearchSpec})
"""
$search stage (Atlas only):
https://www.mongodb.com/docs/atlas/atlas-search/
"""


def verify_search(
    spec: SearchSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors = []

    if not is_atlas:
        errors.append("$search is only available on MongoDB Atlas.")

    if pipeline_index != 0:
        errors.append("$search must be the first stage in the pipeline.")

    if errors:
        return False, errors

    return True, []
