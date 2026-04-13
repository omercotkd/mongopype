# Done

from typing import Union, Literal, TypedDict
from ..types import Version, OutputInto

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/merge/


class MergeDocSpec(TypedDict, total=False):
    into: Union[str, OutputInto]
    on: Union[str, list[str]]
    let: dict
    whenMatched: Union[
        Literal["replace", "keepExisting", "merge", "fail"],
        list,  # aggregation pipeline
    ]
    whenNotMatched: Literal["insert", "discard", "fail"]


MergeSpec = Union[str, MergeDocSpec]

Merge = TypedDict("Merge", {"$merge": MergeSpec})
"""
$merge stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/merge/
"""


def verify_merge(
    spec: MergeSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors = []

    if version < (4, 2):
        errors.append("$merge requires MongoDB >= 4.2.")

    if pipeline_index != pipeline_length - 1:
        errors.append("$merge must be the last stage in the pipeline.")

    if isinstance(spec, dict):
        if "into" not in spec:
            errors.append("$merge requires the 'into' field.")
    elif not isinstance(spec, str):
        errors.append("$merge spec must be a string (collection name) or a document.")

    if errors:
        return False, errors

    return True, []
