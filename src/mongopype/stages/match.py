# Done

from typing import TypedDict
from ..types import Document, Version

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/match/

MatchSpec = Document

Match = TypedDict("Match", {"$match": MatchSpec})
"""
$match stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/match/
"""


def verify_match(
    spec: MatchSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:
    return True, []
