from typing import Literal, Union, TypedDict

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/sort/

SortSpec = dict[str, Union[Literal[1, -1], dict[Literal["$meta"], Literal["textScore"]]]]

Sort = TypedDict("Sort", {"$sort": SortSpec})

def verify_sort(spec: SortSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic
    return True
