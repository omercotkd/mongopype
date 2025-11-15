from typing import Literal, Any

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/score/

Score = dict[Literal["$score"], dict[str, Any]]

def verify_score(stage: Score, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (normalization options, weight numeric)
    return True
