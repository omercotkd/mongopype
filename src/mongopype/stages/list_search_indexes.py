from typing import Any, TypedDict

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/listSearchIndexes/

ListSearchIndexesSpec = dict[str, Any]

ListSearchIndexes = TypedDict("ListSearchIndexes", {"$listSearchIndexes": ListSearchIndexesSpec})

def verify_list_search_indexes(spec: ListSearchIndexesSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (id/name constraints)
    return True
