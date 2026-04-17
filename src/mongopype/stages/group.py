from typing import Union, TypedDict
from ..types import Expression, AccumulatorExpression, Version


GroupSpec = dict[str, Union[Expression, AccumulatorExpression]]

Group = TypedDict("Group", {"$group": GroupSpec})
"""
$group stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/group/
"""


def verify_group(
    spec: GroupSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    if "_id" not in spec:
        errors.append("$group requires an '_id' field.")

    if errors:
        return False, errors

    return True, []
