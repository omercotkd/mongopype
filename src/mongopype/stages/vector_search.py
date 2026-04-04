from typing import Any, TypedDict

# Placeholder for $vectorSearch stage (MongoDB Vector Search / Atlas Search related)

VectorSearchSpec = dict[str, Any]

VectorSearch = TypedDict("VectorSearch", {"$vectorSearch": VectorSearchSpec})

def verify_vector_search(spec: VectorSearchSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (must be first stage; vector index presence)
    return True
