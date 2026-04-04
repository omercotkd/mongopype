from typing import TypedDict, TYPE_CHECKING

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/facet/

if TYPE_CHECKING:
    from ..pipeline import Pipeline


FacetSpec = dict[str, "Pipeline"]

Facet = TypedDict("Facet", {"$facet": FacetSpec})


def verify_facet(spec: FacetSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (sub-pipelines valid)
    return True
