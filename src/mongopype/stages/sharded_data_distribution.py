# Done

from typing import TypedDict
from ..types import Version

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/shardedDataDistribution/

ShardedDataDistributionSpec = dict[str, object]

ShardedDataDistribution = TypedDict(
    "ShardedDataDistribution",
    {"$shardedDataDistribution": ShardedDataDistributionSpec},
)
"""
$shardedDataDistribution stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/shardedDataDistribution/
"""


def verify_sharded_data_distribution(
    spec: ShardedDataDistributionSpec,
    version: Version,
    pipeline_index: int,
    pipeline_length: int,
    is_atlas: bool,
) -> tuple[bool, list[str]]:

    errors = []

    if version < (6, 0):
        errors.append("$shardedDataDistribution requires MongoDB >= 6.0.")

    if pipeline_index != 0:
        errors.append("$shardedDataDistribution must be the first stage in the pipeline.")

    if spec:
        errors.append("$shardedDataDistribution takes an empty document {}.")

    if errors:
        return False, errors

    return True, []
