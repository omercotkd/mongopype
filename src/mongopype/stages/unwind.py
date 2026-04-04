from typing import TypedDict
from ..types import Expression

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/unwind/

UnwindSpec = dict[str, Expression | int | bool]
# NOTE: This is a loose type; path is required (string), includeArrayIndex optional (string), preserveNullAndEmptyArrays optional (bool)

Unwind = TypedDict("Unwind", {"$unwind": UnwindSpec})

def verify_unwind(spec: UnwindSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (path starts with $, index name validity)
    return True
