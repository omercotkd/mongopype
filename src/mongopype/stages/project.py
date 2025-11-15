from typing import Literal, Any

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/project/

Project = dict[Literal["$project"], dict[str, Any]]

def verify_project(stage: Project, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic
    return True
