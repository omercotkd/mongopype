from typing import Literal, Any

# Placeholder for $vectorSearch stage (MongoDB Vector Search / Atlas Search related)

VectorSearch = dict[Literal["$vectorSearch"], dict[str, Any]]

def verify_vector_search(stage: VectorSearch, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (must be first stage; vector index presence)
    return True
