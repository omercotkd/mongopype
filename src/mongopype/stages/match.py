from typing import Literal
from ..types import Document

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/match/

Match = dict[Literal["$match"], Document]

def verify_match(stage: Match, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic
    return True
