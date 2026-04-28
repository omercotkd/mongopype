from typing import TypedDict, NotRequired, Literal, Any
from ..types import Version, Expression, SortOrder, TimeUnit

WindowOperators = Literal[
    "$addToSet",
    "$avg",
    "$bottom",
    "$bottomN",
    "$concatArrays",
    "$count",
    "$covariancePop",
    "$covarianceSamp",
    "$derivative",
    "$expMovingAvg",
    "$first",
    "$firstN",
    "$integral",
    "$last",
    "$lastN",
    "$max",
    "$maxN",
    "$median",
    "$min",
    "$minN",
    "$percentile",
    "$push",
    "$setUnion",
    "$stdDevPop",
    "$stdDevSamp",
    "$sum",
    "$top",
    "$topN",
    # Gap filling operators
    "$linearFill",
    "$locf",
    # Order operators
    "$shift",
]


class WindowOperatorRangeSpec(TypedDict):
    range: list[Literal["unbounded", "current"] | int | float]
    unit: TimeUnit


class WindowOperatorDocumentsSpec(TypedDict):
    documents: list[Literal["unbounded", "current"] | int | float]


WindowOperatorsSpec = WindowOperatorRangeSpec | WindowOperatorDocumentsSpec

OutputWindowOperatorSpec = TypedDict(
    "OutputWindowOperatorSpec",
    {
        "window": WindowOperatorsSpec,
        "$addToSet": Any,
        "$avg": Any,
        "$bottom": Any,
        "$bottomN": Any,
        "$concatArrays": Any,
        "$count": Any,
        "$covariancePop": Any,
        "$covarianceSamp": Any,
        "$derivative": Any,
        "$expMovingAvg": Any,
        "$first": Any,
        "$firstN": Any,
        "$integral": Any,
        "$last": Any,
        "$lastN": Any,
        "$max": Any,
        "$maxN": Any,
        "$median": Any,
        "$min": Any,
        "$minN": Any,
        "$percentile": Any,
        "$push": Any,
        "$setUnion": Any,
        "$stdDevPop": Any,
        "$stdDevSamp": Any,
        "$sum": Any,
        "$top": Any,
        "$topN": Any,
        # Gap filling operators
        "$linearFill": Any,
        "$locf": Any,
        # Order operators
        "$shift": Any,
    },
)


class SetWindowFieldsSpec(TypedDict):
    partitionBy: NotRequired[Expression]
    sortBy: NotRequired[SortOrder]
    output: dict[str, OutputWindowOperatorSpec]


SetWindowFields = TypedDict(
    "SetWindowFields", {"$setWindowFields": SetWindowFieldsSpec}
)
"""
$setWindowFields stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/setWindowFields/
"""


def verify_set_window_fields(
    spec: SetWindowFieldsSpec,
    version: Version,
    pipeline_index: int,
    pipeline_length: int,
    is_atlas: bool,
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    if version < (5, 0):
        errors.append("$setWindowFields requires MongoDB >= 5.0.")

    if "output" not in spec:
        errors.append("$setWindowFields requires the 'output' field.")

    if errors:
        return False, errors

    return True, []
