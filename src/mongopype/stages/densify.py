from typing import TypedDict
from ..types import DensifyRange

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/densify/

DensifySpec = dict[str, DensifyRange | list[str]]
# Required: field, range; Optional: partitionByFields

Densify = TypedDict("Densify", {"$densify": DensifySpec})

def verify_densify(spec: DensifySpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (range correctness, field present)
    return True
