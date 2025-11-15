from typing import Literal, Union

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/unset/

Unset = dict[Literal["$unset"], Union[str, list[str]]]

def verify_unset(stage: Unset, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic
    return True
