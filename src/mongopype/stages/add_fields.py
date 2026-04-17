from typing import TypedDict, Literal
from ..types import Document, Version

AddFieldsSpec = Document

AddFields = TypedDict("AddFields", {"$addFields": AddFieldsSpec})
"""
$addFields stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/addFields/
"""


def verify_add_fields(
    spec: AddFieldsSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[Literal[True], list[str]]:
    # As long as the pylance is happy with the spec type, this is a valid stage.
    # Add fields can be in any position in the pipeline.
    return True, []
