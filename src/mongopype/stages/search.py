from typing import Any, TypedDict

# https://www.mongodb.com/docs/atlas/atlas-search/

SearchSpec = dict[str, Any]

Search = TypedDict("Search", {"$search": SearchSpec})

def verify_search(spec: SearchSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (must be first stage; cluster capability)
    return True
