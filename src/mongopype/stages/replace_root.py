# Done

from typing import TypedDict
from ..types import Expression, Version

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/replaceRoot/


class ReplaceRootSpec(TypedDict):
    newRoot: Expression


ReplaceRoot = TypedDict("ReplaceRoot", {"$replaceRoot": ReplaceRootSpec})
"""
$replaceRoot stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/replaceRoot/
"""


def verify_replace_root(
    spec: ReplaceRootSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:
    return True, []
