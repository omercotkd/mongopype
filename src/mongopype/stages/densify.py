from typing import Literal
from ..types import DensifyRange

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/densify/

Densify = dict[Literal["$densify"], dict[str, DensifyRange | list[str]]]
# Required: field, range; Optional: partitionByFields

def verify_densify(stage: Densify, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (range correctness, field present)
    return True
