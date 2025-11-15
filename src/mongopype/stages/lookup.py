from typing import Literal, Any

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/lookup/

Lookup = dict[Literal["$lookup"], dict[str, Any]]

def verify_lookup(stage: Lookup, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (from, as, either local/foreign or pipeline with let)
    return True
