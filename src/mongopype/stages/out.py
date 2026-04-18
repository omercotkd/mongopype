from typing import Union, TypedDict, NotRequired, Literal
from ..types import Version, OutputInto


class TimeSeriesSpec(TypedDict):
    timeField: str
    metaField: NotRequired[str]
    granularity: NotRequired[Literal["seconds", "minutes", "hours"]]
    # Possible values are 1-31536000 ver 6.3 and later
    bucketMaxSpanSeconds: NotRequired[int]
    #  ver 6.3 and later must be eq to bucketMaxSpanSeconds
    bucketRoundingSeconds: NotRequired[int]


class OutputIntoTimeSeries(OutputInto):
    timeseries: TimeSeriesSpec


OutSpec = Union[str, OutputInto, OutputIntoTimeSeries]

Out = TypedDict("Out", {"$out": OutSpec})
"""
$out stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/out/
"""


def verify_out(
    spec: OutSpec,
    version: Version,
    pipeline_index: int,
    pipeline_length: int,
    is_atlas: bool,
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    if pipeline_index != pipeline_length - 1:
        errors.append("$out must be the last stage in the pipeline.")

    if isinstance(spec, str):
        if not spec:
            errors.append("$out collection name must not be empty.")
    else:
        if "timeseries" in spec:
            if version < (7, 0):
                errors.append("$out with 'timeseries' requires MongoDB >= 7.0.")
            if "metaField" in spec["timeseries"]:
                if spec["timeseries"]["metaField"] == spec["timeseries"]["timeField"]:
                    errors.append("$out 'metaField' and 'timeField' must be different.")
                if spec["timeseries"]["metaField"] == "_id":
                    errors.append("$out 'metaField' cannot be '_id'.")
            if "granularity" in spec["timeseries"]:
                if "bucketRoundingSeconds" in spec["timeseries"]:
                    errors.append("$out 'timeseries' cannot specify both 'granularity' and 'bucketRoundingSeconds'.")
                if "bucketMaxSpanSeconds" in spec["timeseries"]:
                    errors.append("$out 'timeseries' cannot specify both 'granularity' and 'bucketMaxSpanSeconds'.")
            if "bucketMaxSpanSeconds" in spec["timeseries"]:
                if "bucketRoundingSeconds" in spec["timeseries"]:
                    if not spec["timeseries"]["bucketRoundingSeconds"] == spec["timeseries"]["bucketMaxSpanSeconds"]:
                        errors.append("$out 'timeseries' requires 'bucketRoundingSeconds' to be equal to 'bucketMaxSpanSeconds' when both are specified.")
                if not (1 <= spec["timeseries"]["bucketMaxSpanSeconds"] <= 31536000):
                    errors.append("$out 'timeseries' 'bucketMaxSpanSeconds' must be between 1 and 31536000.")
    if errors:
        return False, errors

    return True, []
