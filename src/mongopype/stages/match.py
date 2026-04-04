from typing import TypedDict
from ..types import Document

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/match/

MatchSpec = Document

Match = TypedDict("Match", {"$match": MatchSpec})

def verify_match(spec: MatchSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic
    return True
