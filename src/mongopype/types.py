from typing import Literal, Any, TypedDict
from collections.abc import Callable
from bson import (
    ObjectId,
    DatetimeMS,
    Binary,
    Int64,
    Code,
    DBRef,
    MaxKey,
    MinKey,
    Regex,
    # SON,
    Timestamp,
    Decimal128,
)
import datetime, uuid


Version = tuple[int, int]  # major, minor

ValidationFunction = Callable[[Any, Version, int, int, bool], tuple[bool, list[str]]]

BSON = (
    str
    | bytes
    | int
    | float
    | bool
    | None
    | DatetimeMS
    | ObjectId
    | Binary
    | Code
    | DBRef
    | MaxKey
    | MinKey
    | Regex[str]
    | Regex[bytes]
    | Timestamp
    | Decimal128
    | Int64
    | datetime.datetime
    | uuid.UUID
    | tuple["BSON", ...]
    | dict[str, "BSON"]
    | list["BSON"]
)

Expression = str | int | float | dict[str, Any] | list[Any]


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


class OutputInto(TypedDict):
    db: str
    coll: str


MetaTextScore = dict[Literal["$meta"], Literal["textScore"]]

SortOrder = dict[str, Literal[1, -1] | MetaTextScore]


class UserDocument(TypedDict):
    user: str
    db: str


TimeUnit = Literal[
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
