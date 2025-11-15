from typing import Literal, Any

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/shardedDataDistribution/

ShardedDataDistribution = dict[Literal["$shardedDataDistribution"], dict[str, Any]]

def verify_sharded_data_distribution(stage: ShardedDataDistribution, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (requires sharded cluster)
    return True
