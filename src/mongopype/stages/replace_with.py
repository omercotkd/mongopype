from typing import TypedDict
from ..types import Expression

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/replaceWith/

ReplaceWithSpec = Expression

ReplaceWith = TypedDict("ReplaceWith", {"$replaceWith": ReplaceWithSpec})

def verify_replace_with(spec: ReplaceWithSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic
    return True
