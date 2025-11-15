from typing import Literal, Any

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/fill/

Fill = dict[Literal["$fill"], dict[str, Any]]

def verify_fill(stage: Fill, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (method/value rules)
    return True
