from typing import Literal, Any

# https://www.mongodb.com/docs/atlas/atlas-search/

Search = dict[Literal["$search"], dict[str, Any]]

def verify_search(stage: Search, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (must be first stage; cluster capability)
    return True
