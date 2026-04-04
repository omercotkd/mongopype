from typing import Any, TypedDict

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/project/

ProjectSpec = dict[str, Any]

Project = TypedDict("Project", {"$project": ProjectSpec})

def verify_project(spec: ProjectSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic
    return True
