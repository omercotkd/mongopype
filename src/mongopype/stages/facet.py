from typing import Literal, TYPE_CHECKING

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/facet/

if TYPE_CHECKING:
    from ..pipeline import Pipeline


Facet = dict[Literal["$facet"], dict[str, "Pipeline"]]


def verify_facet(stage: Facet, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (sub-pipelines valid)
    return True
