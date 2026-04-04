from typing import Any, TypedDict

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/out/

OutSpec = Any

Out = TypedDict("Out", {"$out": OutSpec})

def verify_out(spec: OutSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (type union correctness)
    return True
