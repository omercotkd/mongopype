from typing import TypedDict

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/sample/


class SampleSpec(TypedDict):
    size: int


Sample = TypedDict("Sample", {"$sample": SampleSpec})

def verify_sample(spec: SampleSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (size positive)
    return True
