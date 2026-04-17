from typing import TypedDict
from ..types import Version


class ListSampledQueriesSpec(TypedDict, total=False):
    namespace: str


ListSampledQueries = TypedDict(
    "ListSampledQueries", {"$listSampledQueries": ListSampledQueriesSpec}
)
"""
$listSampledQueries stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/listSampledQueries/
"""


def verify_list_sampled_queries(
    spec: ListSampledQueriesSpec,
    version: Version,
    pipeline_index: int,
    pipeline_length: int,
    is_atlas: bool,
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    if version < (7, 0):
        errors.append("$listSampledQueries requires MongoDB >= 7.0.")

    if "namespace" in spec:
        ns = spec["namespace"]
        if "." not in ns:
            errors.append(
                "$listSampledQueries 'namespace' must be a string in the format 'database.collection'."
            )

    if errors:
        return False, errors

    return True, []
