from typing import Any, TypedDict

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/listClusterCatalog/

ListClusterCatalogSpec = dict[str, Any]

ListClusterCatalog = TypedDict("ListClusterCatalog", {"$listClusterCatalog": ListClusterCatalogSpec})

def verify_list_cluster_catalog(spec: ListClusterCatalogSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic
    return True
