from typing import Any, TypedDict

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/rankFusion/

RankFusionSpec = dict[str, Any]

RankFusion = TypedDict("RankFusion", {"$rankFusion": RankFusionSpec})

def verify_rank_fusion(spec: RankFusionSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (requires Atlas Search usage)
    return True
