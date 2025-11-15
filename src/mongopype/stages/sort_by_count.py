from typing import Literal
from ..types import Expression

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/sortByCount/

SortByCount = dict[Literal["$sortByCount"], Expression]

def verify_sort_by_count(stage: SortByCount, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (expression validity)
    return True
