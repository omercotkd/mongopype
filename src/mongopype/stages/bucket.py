from typing import TypedDict, Union, Optional
from datetime import datetime
from ..types import AccumulatorExpression, Expression, Version
from ..verify import verify_accumulator_expression


class BucketSpec(TypedDict):
    groupBy: Expression
    boundaries: Union[list[int], list[float], list[str], list[datetime]]
    default: Optional[Union[int, float, str, datetime]]
    """
    Default is the ID of the bucket for all the documents that do not fit into the specified boundaries.
    """
    output: dict[str, AccumulatorExpression]


Bucket = TypedDict("Bucket", {"$bucket": BucketSpec})
"""
$bucket stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/bucket/
"""


def verify_bucket(
    spec: BucketSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    for key, value in spec["output"].items():
        is_valid, error = verify_accumulator_expression(value, version)
        if not is_valid:
            errors.append(f"Invalid output specification for field '{key}': {error}")

    for i in range(len(spec["boundaries"]) - 1):
        if spec["boundaries"][i] >= spec["boundaries"][i + 1]:  # type: ignore
            errors.append(
                f"Invalid boundaries: {spec['boundaries']}. Boundaries must be in ascending order."
            )
    
    if "default" in spec and spec["default"] is not None:
        default_value = spec["default"]
        # If the default is string its always valid
        if not isinstance(default_value, str):
            # if the default value is the same type as the boundaries, 
            # it must be less than the first boundary or greater than or equal to the last boundary
            if type(default_value) == type(spec["boundaries"][0]):
                if default_value < spec["boundaries"][0] or default_value >= spec["boundaries"][-1]:  # type: ignore
                    errors.append(
                        f"Invalid default value: {default_value}. Default value must be less than the first boundary or greater than or equal to the last boundary."
                    )
    if errors:
        return False, errors

    return True, []
