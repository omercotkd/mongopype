from typing import Any, TypedDict

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/fill/

FillSpec = dict[str, Any]

Fill = TypedDict("Fill", {"$fill": FillSpec})

def verify_fill(spec: FillSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (method/value rules)
    return True
