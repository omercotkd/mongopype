from typing import Callable, Literal, Any, Optional, TypedDict, Union


Version = tuple[int, int]  # major, minor

ValidationFunction = Callable[[Any, Version, int, int, bool], tuple[bool, list[str]]]

Expression = Union[str, int, float, dict[str, Any], list[Any]]

BSON = Union[str, int, float, bool, None, dict[str, "BSON"], list["BSON"]]

Document = dict[str, BSON]

Stage = Literal[
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
    # ver <= 8
    "$accumulator",
    "$addToSet",
    "$avg",
    # ver >= 5.2
    "$bottom",
    # ver >= 5.2
    "$bottomN",
    # ver >= 8.1
    "$concatArrays",
    # ver >= 5.0
    "$count",
    "$first",
    # ver >= 5.2
    "$firstN",
    "$last",
    # ver >= 5.2
    "$lastN",
    "$max",
    # ver >= 5.2
    "$maxN",
    # ver >= 7.0
    "$median",
    "$mergeObjects",
    "$min",
    # ver >= 5.2
    "$minN",
    # ver >= 7.0
    "$percentile",
    "$push",
    # ver >= 8.1
    "$setUnion",
    "$stdDevPop",
    "$stdDevSamp",
    "$sum",
    "$top",
    # ver >= 5.2
    "$topN",
]

AccumulatorExpression = dict[Accumulator, Expression]

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


MetaTextScore = dict[Literal["$meta"], Literal["textScore"]]

SortOrder = dict[str, Union[Literal[1, -1], MetaTextScore]]


class UserDocument(TypedDict):
    user: str
    db: str
