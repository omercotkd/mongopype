from typing import Any, TypedDict
from ..types import Version


SearchMetaSpec = dict[str, Any]

SearchMeta = TypedDict("SearchMeta", {"$searchMeta": SearchMetaSpec})
"""
$searchMeta stage (Atlas only):
https://www.mongodb.com/docs/atlas/atlas-search/
"""


def verify_search_meta(
    spec: SearchMetaSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    if not is_atlas:
        errors.append("$searchMeta is only available on MongoDB Atlas.")

    if pipeline_index != 0:
        errors.append("$searchMeta must be the first stage in the pipeline.")

    if errors:
        return False, errors

    return True, []
