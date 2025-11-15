from typing import Literal, Any

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/listClusterCatalog/

ListClusterCatalog = dict[Literal["$listClusterCatalog"], dict[str, Any]]

def verify_list_cluster_catalog(stage: ListClusterCatalog, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic
    return True
