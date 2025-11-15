from typing import Literal, Union

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/sort/

Sort = dict[
    Literal["$sort"],
    dict[str, Union[Literal[1, -1], dict[Literal["$meta"], Literal["textScore"]]]],
]

def verify_sort(stage: Sort, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic
    return True
