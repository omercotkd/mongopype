from typing import TypedDict
from ..types import Expression, Version


RedactSpec = Expression

Redact = TypedDict("Redact", {"$redact": RedactSpec})
"""
$redact stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/redact/
"""


def verify_redact(
    spec: RedactSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:
    return True, []
