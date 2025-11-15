from typing import Literal, Any

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/listSearchIndexes/

ListSearchIndexes = dict[Literal["$listSearchIndexes"], dict[str, Any]]

def verify_list_search_indexes(stage: ListSearchIndexes, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (id/name constraints)
    return True
