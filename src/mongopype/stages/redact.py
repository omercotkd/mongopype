from typing import Literal
from ..types import Expression

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/redact/

Redact = dict[Literal["$redact"], Expression]

def verify_redact(stage: Redact, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic ($$PRUNE/$$KEEP/$$DESCEND usage)
    return True
