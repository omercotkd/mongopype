from typing import Any, TypedDict

# https://www.mongodb.com/docs/atlas/atlas-search/

SearchMetaSpec = dict[str, Any]

SearchMeta = TypedDict("SearchMeta", {"$searchMeta": SearchMetaSpec})

def verify_search_meta(spec: SearchMetaSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (must follow $search)
    return True
