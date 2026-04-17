from typing import Union, TypedDict
from ..types import Document, Expression, Version


DocumentsSpec = Union[list[Document], Expression]

Documents = TypedDict("Documents", {"$documents": DocumentsSpec})
"""
$documents stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/documents/
"""


def verify_documents(
    spec: DocumentsSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    if version < (6, 0):
        errors.append("$documents requires MongoDB >= 6.0.")

    if pipeline_index != 0:
        errors.append("$documents must be the first stage in the pipeline.")

    if errors:
        return False, errors

    return True, []
