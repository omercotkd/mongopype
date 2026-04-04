from typing import TypedDict
from ..types import Expression

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/sortByCount/

SortByCountSpec = Expression

SortByCount = TypedDict("SortByCount", {"$sortByCount": SortByCountSpec})

def verify_sort_by_count(spec: SortByCountSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (expression validity)
    return True
