from typing import Literal
from ..types import Document

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/documents/

Documents = dict[Literal["$documents"], list[Document]]

def verify_documents(stage: Documents, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (must be first in unionWith sub-pipeline in some cases)
    return True
