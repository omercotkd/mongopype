from typing import Literal, Any

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/listSampledQueries/

ListSampledQueries = dict[Literal["$listSampledQueries"], dict[str, Any]]

def verify_list_sampled_queries(stage: ListSampledQueries, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (namespace format)
    return True
