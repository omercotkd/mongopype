from typing import Literal

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/count/

Count = dict[Literal["$count"], str]

def verify_count(stage: Count, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (field name constraints)
    return True
