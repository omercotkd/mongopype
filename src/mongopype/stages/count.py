from typing import TypedDict

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/count/

CountSpec = str

Count = TypedDict("Count", {"$count": CountSpec})

def verify_count(spec: CountSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (field name constraints)
    return True
