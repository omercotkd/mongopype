from typing import Any, TypedDict, TYPE_CHECKING, NotRequired
from ..types import Version


if TYPE_CHECKING:
    from ..pipeline import Pipeline

LookupEqualitySpec = TypedDict(
    "LookupEqualitySpec",
    {
        "from": str,
        "localField": str,
        "foreignField": str,
        "as": str,
    },
)

LookupPipelineSpec = TypedDict(
    "LookupPipelineSpec",
    {
        "from": str,
        "let": NotRequired[dict[str, Any]],
        "pipeline": "Pipeline",
        "as": str,
    },
)

MixedLookupSpec = TypedDict(
    "MixedLookupSpec",
    {
        "from": str,
        "localField": str,
        "foreignField": str,
        "let": NotRequired[dict[str, Any]],
        "pipeline": "Pipeline",
        "as": str,
    },
    total=False,
)


LookupSpec = LookupEqualitySpec | LookupPipelineSpec | MixedLookupSpec


class LookupKwargsSpec(TypedDict):
    from_: str
    as_: str
    localField: NotRequired[str]
    foreignField: NotRequired[str]
    let: NotRequired[dict[str, Any]]
    pipeline: NotRequired["Pipeline"]


Lookup = TypedDict("Lookup", {"$lookup": LookupSpec})
"""
$lookup stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/lookup/
"""


def verify_lookup(
    spec: LookupSpec,
    version: Version,
    pipeline_index: int,
    pipeline_length: int,
    is_atlas: bool,
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    if "as" not in spec:
        errors.append("$lookup requires the 'as' field.")

    has_pipeline = "pipeline" in spec
    has_local_foreign = "localField" in spec or "foreignField" in spec

    if has_pipeline:
        # Pipeline form
        if has_local_foreign and version < (5, 1):
            errors.append(
                "$lookup combining 'localField'/'foreignField' with 'pipeline' requires MongoDB >= 5.1."
            )
        if isinstance(spec.get("pipeline"), list):
            for stage in spec["pipeline"]:
                stage_key = next(iter(stage), None)
                if stage_key in ("$out", "$merge"):
                    errors.append(
                        f"$lookup sub-pipeline cannot contain {stage_key}."
                    )
            v, e = spec["pipeline"].verify(version, is_atlas)
            if not v:
                errors.extend(f"$lookup sub-pipeline: {err}" for err in e)
    else:
        # Equality form
        if "localField" not in spec:
            errors.append("$lookup equality form requires 'localField'.")
        if "foreignField" not in spec:
            errors.append("$lookup equality form requires 'foreignField'.")

    if errors:
        return False, errors

    return True, []
