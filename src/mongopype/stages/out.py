from typing import Literal, Any

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/out/

Out = dict[Literal["$out"], Any]

def verify_out(stage: Out, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (type union correctness)
    return True
