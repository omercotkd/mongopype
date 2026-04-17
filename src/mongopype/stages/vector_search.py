from typing import Any, Union, TypedDict
from ..types import Version



class VectorSearchSpec(TypedDict, total=False):
    index: str
    path: Union[str, list[str]]
    queryVector: list[float]
    numCandidates: int
    limit: int
    filter: dict[str, Any]
    exact: bool


VectorSearch = TypedDict("VectorSearch", {"$vectorSearch": VectorSearchSpec})
"""
$vectorSearch stage (Atlas only):
https://www.mongodb.com/docs/atlas/atlas-vector-search/vector-search-stage/
"""


def verify_vector_search(
    spec: VectorSearchSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    if not is_atlas:
        errors.append("$vectorSearch is only available on MongoDB Atlas.")

    if pipeline_index != 0:
        errors.append("$vectorSearch must be the first stage in the pipeline.")

    if "index" not in spec:
        errors.append("$vectorSearch requires the 'index' field.")

    if "path" not in spec:
        errors.append("$vectorSearch requires the 'path' field.")

    if "queryVector" not in spec:
        errors.append("$vectorSearch requires the 'queryVector' field.")

    if "limit" not in spec:
        errors.append("$vectorSearch requires the 'limit' field.")

    if errors:
        return False, errors

    return True, []
