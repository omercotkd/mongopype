from typing import Literal, TypedDict, Any, TYPE_CHECKING, NotRequired
from ..types import Version, OutputInto



if TYPE_CHECKING:
    from ..pipeline import Pipeline


class MergeDocSpec(TypedDict):
    into: str | OutputInto
    on: NotRequired[str | list[str]]
    let: NotRequired[dict[str, Any]]
    whenMatched: NotRequired[
        Literal["replace", "keepExisting", "merge", "fail"]
        | "Pipeline"
    ]
    whenNotMatched: NotRequired[Literal["insert", "discard", "fail"]]


MergeSpec = str | MergeDocSpec

Merge = TypedDict("Merge", {"$merge": MergeSpec})
"""
$merge stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/merge/
"""


def verify_merge(
    spec: MergeSpec,
    version: Version,
    pipeline_index: int,
    pipeline_length: int,
    is_atlas: bool,
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    if version < (4, 2):
        errors.append("$merge requires MongoDB >= 4.2.")

    if pipeline_index != pipeline_length - 1:
        errors.append("$merge must be the last stage in the pipeline.")

    if errors:
        return False, errors

    return True, []
