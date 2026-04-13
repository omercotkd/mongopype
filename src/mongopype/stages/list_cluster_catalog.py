# Done

from typing import TypedDict
from ..types import Version

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/listClusterCatalog/


class ListClusterCatalogSpec(TypedDict, total=False):
    shards: bool
    balancingConfiguration: bool


ListClusterCatalog = TypedDict("ListClusterCatalog", {"$listClusterCatalog": ListClusterCatalogSpec})
"""
$listClusterCatalog stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/listClusterCatalog/
"""


def verify_list_cluster_catalog(
    spec: ListClusterCatalogSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors = []

    if version < (8, 1):
        errors.append("$listClusterCatalog requires MongoDB >= 8.1.")

    if pipeline_index != 0:
        errors.append("$listClusterCatalog must be the first stage in the pipeline.")

    if errors:
        return False, errors

    return True, []
