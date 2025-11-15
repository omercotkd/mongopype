from typing import Literal, Any

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/changeStream/

ChangeStream = dict[Literal["$changeStream"], dict[str, Any]]

def verify_change_stream(stage: ChangeStream, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (must be first stage, version checks)
    return True
