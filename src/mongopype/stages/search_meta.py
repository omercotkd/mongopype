from typing import Literal, Any

# https://www.mongodb.com/docs/atlas/atlas-search/

SearchMeta = dict[Literal["$searchMeta"], dict[str, Any]]

def verify_search_meta(stage: SearchMeta, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (must follow $search)
    return True
