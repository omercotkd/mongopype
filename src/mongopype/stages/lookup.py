from typing import Any, TypedDict

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/lookup/

LookupSpec = dict[str, Any]

Lookup = TypedDict("Lookup", {"$lookup": LookupSpec})

def verify_lookup(spec: LookupSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (from, as, either local/foreign or pipeline with let)
    return True
