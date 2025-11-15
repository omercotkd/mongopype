from typing import Literal

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/sample/

Sample = dict[Literal["$sample"], dict[Literal["size"], int]]

def verify_sample(stage: Sample, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (size positive)
    return True
