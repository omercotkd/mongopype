from typing import Any, TypedDict

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/score/

ScoreSpec = dict[str, Any]

Score = TypedDict("Score", {"$score": ScoreSpec})

def verify_score(spec: ScoreSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (normalization options, weight numeric)
    return True
