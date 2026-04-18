from typing import TypedDict
from ..types import Version, BSON


ProjectSpec = dict[str, BSON]

Project = TypedDict("Project", {"$project": ProjectSpec})
"""
$project stage:
https://www.mongodb.com/docs/manual/reference/operator/aggregation/project/
"""


def verify_project(
    spec: ProjectSpec, version: Version, pipeline_index: int, pipeline_length: int, is_atlas: bool
) -> tuple[bool, list[str]]:

    errors: list[str] = []

    if not spec:
        errors.append("$project specification must not be empty.")
        return False, errors

    has_inclusion = False
    has_exclusion = False

    for key, value in spec.items():
        if key == "_id":
            continue
        if value == 0 or value is False:
            has_exclusion = True
        elif value == 1 or value is True or isinstance(value, (str, dict)):
            has_inclusion = True

    if has_inclusion and has_exclusion:
        errors.append("$project cannot mix inclusion and exclusion (except for _id).")

    if errors:
        return False, errors

    return True, []
