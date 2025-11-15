from typing import Literal, Any, Optional, TypedDict, Union


# TODO expand these type
Expression = Union[str, int, float, dict[str, Any], list[Any]]

Document = dict[str, Any]

Stages = Literal[
    "$addFields",
    "$bucket",
    "$bucketAuto",
    "$changeStream",
    "$changeStreamSplitLargeEvent",
    "$collStats",
    "$count",
    "$currentOp",
    "$densify",
    "$documents",
    "$facet",
    "$fill",
    "$geoNear",
    "$graphLookup",
    "$group",
    "$indexStats",
    "$limit",
    "$listClusterCatalog",
    "$listLocalSessions",
    "$listSampledQueries",
    "$listSearchIndexes",
    "$listSessions",
    "$lookup",
    "$match",
    "$merge",
    "$out",
    "$planCacheStats",
    "$project",
    "$querySettings",
    "$queryStats",
    "$rankFusion",
    "$redact",
    "$replaceRoot",
    "$replaceWith",
    "$sample",
    "$score",
    "$scoreFusion",
    "$search",
    "$searchMeta",
    "$set",
    "$setWindowFields",
    "$shardedDataDistribution",
    "$skip",
    "$sort",
    "$sortByCount",
    "$unionWith",
    "$unset",
    "$unwind",
    "$vectorSearch",
]


# https://www.mongodb.com/docs/manual/reference/mql/accumulators/
Accumulator = Literal[
    # TODO make sure not used in mongo ver >= 8
    "$accumulator",
    "$addToSet",
    "$avg",
    # TODO mongo ver >= 5.2
    "$bottom",
    # TODO mongo ver >= 5.2
    "$bottomN",
    # TODO mongo ver >= 8.1
    "$concatArrays",
    # TODO mongo ver >= 5.0
    "$count",
    "$first",
    # TODO mongo ver >= 5.2
    "$firstN",
    "$last",
    # TODO mongo ver >= 5.2
    "$lastN",
    "$max",
    # TODO mongo ver >= 5.2
    "$maxN",
    # TODO mongo ver >= 7.0
    "$median",
    "$mergeObjects",
    "$min",
    # TODO mongo ver >= 5.2
    "$minN",
    # TODO mongo ver >= 7.0
    "$percentile",
    "$push",
    # TODO mongo ver >= 8.1
    "$setUnion",
    "$stdDevPop",
    "$stdDevSamp",
    "$sum",
    "$top",
    # TODO mongo ver >= 5.2
    "$topN",
]

BucketAutoGranularity = Literal[
    "R5",
    "R10",
    "R20",
    "R40",
    "R80",
    "1-2-5",
    "E6",
    "E12",
    "E24",
    "E48",
    "E96",
    "E192",
    "POWERSOF2",
]

ChaneStreamFullDocumentOptions = Literal[
    "default",
    "required",
    "updateLookup",
    "whenAvailable",
]

ChaneStreamFullDocumentBeforeChangeOptions = Literal[
    "off",
    "whenAvailable",
    "required",
]

TimeUnits = Literal[
    "millisecond",
    "second",
    "minute",
    "hour",
    "day",
    "week",
    "month",
    "quarter",
    "year",
]


class DensifyRange(TypedDict):
    bounds: Union[Literal["full", "partition"], tuple[Any, Any]]
    step: Union[int, float]
    unit: Optional[TimeUnits]


class OutputInto(TypedDict):
    db: str
    coll: str


class OutputIntoTimeSeries(OutputInto):
    db: str
    coll: str
    timeField: str
    # should not be the _id field
    metaField: Optional[str]
    granularity: Optional[Literal["seconds", "minutes", "hours"]]
    # Possible values are 1-31536000 ver 6.3 and later
    bucketMaxSpanSeconds: Optional[int]
    #  ver 6.3 and later must be eq to bucketMaxSpanSeconds
    bucketRoundingSeconds: Optional[int]
