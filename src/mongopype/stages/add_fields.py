from typing import Literal
from ..types import Expression

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/addFields/

AddFields = dict[Literal["$addFields"], dict[str, Expression]]


def verify_add_fields(stage: AddFields, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic
    return True
