from typing import Any, TypedDict

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/listSampledQueries/

ListSampledQueriesSpec = dict[str, Any]

ListSampledQueries = TypedDict("ListSampledQueries", {"$listSampledQueries": ListSampledQueriesSpec})

def verify_list_sampled_queries(spec: ListSampledQueriesSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (namespace format)
    return True
