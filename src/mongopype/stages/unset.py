from typing import Union, TypedDict

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/unset/

UnsetSpec = Union[str, list[str]]

Unset = TypedDict("Unset", {"$unset": UnsetSpec})

def verify_unset(spec: UnsetSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic
    return True
