from typing import TypedDict
from ..types import Document

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/documents/

DocumentsSpec = list[Document]

Documents = TypedDict("Documents", {"$documents": DocumentsSpec})

def verify_documents(spec: DocumentsSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (must be first in unionWith sub-pipeline in some cases)
    return True
