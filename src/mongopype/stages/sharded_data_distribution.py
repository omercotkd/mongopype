from typing import Any, TypedDict

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/shardedDataDistribution/

ShardedDataDistributionSpec = dict[str, Any]

ShardedDataDistribution = TypedDict("ShardedDataDistribution", {"$shardedDataDistribution": ShardedDataDistributionSpec})

def verify_sharded_data_distribution(spec: ShardedDataDistributionSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (requires sharded cluster)
    return True
