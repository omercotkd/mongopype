from typing import Union, Literal, TypedDict, Any, TYPE_CHECKING
from ..types import Version, OutputInto

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/merge/


if TYPE_CHECKING:
    from ..pipeline import Pipeline


class MergeDocSpec(TypedDict, total=False):
    into: Union[str, OutputInto]
    on: Union[str, list[str]]
    let: dict[str, Any]
    whenMatched: Union[
        Literal["replace", "keepExisting", "merge", "fail"],
        Pipeline,
    ]
    whenNotMatched: Literal["insert", "discard", "fail"]


MergeSpec = Union[str, MergeDocSpec]

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

    if isinstance(spec, dict):
        if "into" not in spec:
            errors.append("$merge requires the 'into' field.")

    if errors:
        return False, errors

    return True, []
