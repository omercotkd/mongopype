from typing import Literal
from ..types import Expression

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/unwind/

Unwind = dict[Literal["$unwind"], dict[str, Expression | int | bool]]
# NOTE: This is a loose type; path is required (string), includeArrayIndex optional (string), preserveNullAndEmptyArrays optional (bool)

def verify_unwind(stage: Unwind, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (path starts with $, index name validity)
    return True
