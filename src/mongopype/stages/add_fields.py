from typing import Literal, TypedDict
from ..types import Expression

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/addFields/

# AddFields = dict[Literal["$addFields"], dict[str, Expression]]

AddFieldsSpec = dict[str, Expression]

AddFields = TypedDict("AddFields", {"$addFields": AddFieldsSpec})


def verify_add_fields(spec: AddFieldsSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic
    return True

