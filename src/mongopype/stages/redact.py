from typing import TypedDict
from ..types import Expression

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/redact/

RedactSpec = Expression

Redact = TypedDict("Redact", {"$redact": RedactSpec})

def verify_redact(spec: RedactSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic ($$PRUNE/$$KEEP/$$DESCEND usage)
    return True
