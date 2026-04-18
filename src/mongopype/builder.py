from typing import Union, Unpack, Literal, Any
from . import types as mongopype_types
from .pipeline import Pipeline, PipelineHint
from .stages.bucket import BucketSpec
from .stages.bucket_auto import BucketAutoSpec
from .stages.change_stream import ChangeStreamSpec
from .stages.coll_stats import CollStatsSpec
from .stages.current_op import CurrentOpSpec
from .stages.densify import DensifySpec
from .stages.documents import DocumentsSpec
from .stages.fill import FillSpec
from .stages.geo_near import GeoNearSpec
from .stages.graph_lookup import GraphLookupSpec, GraphLookupKwargsSpec
from .stages.list_cluster_catalog import ListClusterCatalogSpec
from .stages.list_local_sessions import ListLocalSessionsKwargsSpec
from .stages.list_sampled_queries import ListSampledQueriesSpec
from .stages.list_search_indexes import ListSearchIndexesSpec
from .stages.list_sessions import ListSessionsKwargsSpec
from .stages.lookup import LookupKwargsSpec, LookupSpec
from .stages.merge import MergeDocSpec
from .stages.out import OutSpec
from .stages.plan_cache_stats import PlanCacheStatsSpec
from .stages.query_settings import QuerySettingsSpec
from .stages.query_stats import QueryStatsSpec
from .stages.rank_fusion import RankFusionSpec
from .stages.replace_root import ReplaceRootSpec
from .stages.sample import SampleSpec
from .stages.score import ScoreSpec
from .stages.score_fusion import ScoreFusionSpec
from .stages.set_window_fields import SetWindowFieldsSpec
from .stages.union_with import UnionWithFullSpec
from .stages.unwind import UnwindDocSpec
from .stages.vector_search import VectorSearchSpec


class PipelineBuilder:
    def __init__(self):
        self._pipeline: Pipeline = Pipeline([])

    def verify(self):
        return self._pipeline.verify((0, 0), True)

    def add_stage(self, stage: PipelineHint) -> "PipelineBuilder":
        self._pipeline.append(stage)
        return self

    # STAGES
    def add_fields(self, **kwargs: Any) -> "PipelineBuilder":
        return self.add_stage({"$addFields": kwargs})

    def bucket(
        self,
        **kwargs: Unpack[BucketSpec],
    ) -> "PipelineBuilder":
        return self.add_stage(
            {
                "$bucket": kwargs,
            }
        )

    def bucket_auto(
        self,
        **kwargs: Unpack[BucketAutoSpec],
    ) -> "PipelineBuilder":

        return self.add_stage({"$bucketAuto": kwargs})

    def change_stream(self, **kwargs: Unpack[ChangeStreamSpec]) -> "PipelineBuilder":

        return self.add_stage({"$changeStream": kwargs})

    def change_stream_split_large_event(
        self,
    ) -> "PipelineBuilder":
        return self.add_stage({"$changeStreamSplitLargeEvent": {}})

    def coll_stats(self, **kwargs: Unpack[CollStatsSpec]) -> "PipelineBuilder":
        return self.add_stage({"$collStats": kwargs})

    def count(self, field_name: str) -> "PipelineBuilder":
        return self.add_stage({"$count": field_name})

    def current_op(self, **kwargs: Unpack[CurrentOpSpec]) -> "PipelineBuilder":
        return self.add_stage({"$currentOp": kwargs})

    def densify(self, **kwargs: Unpack[DensifySpec]) -> "PipelineBuilder":
        return self.add_stage({"$densify": kwargs})

    def documents(self, documents: DocumentsSpec) -> "PipelineBuilder":
        return self.add_stage({"$documents": documents})

    def facet(self, **kwargs: Pipeline) -> "PipelineBuilder":
        return self.add_stage({"$facet": kwargs})

    def fill(self, **kwargs: Unpack[FillSpec]) -> "PipelineBuilder":
        return self.add_stage({"$fill": kwargs})

    def geo_near(self, **kwargs: Unpack[GeoNearSpec]) -> "PipelineBuilder":
        return self.add_stage({"$geoNear": kwargs})

    def graph_lookup(
        self, **kwargs: Unpack[GraphLookupKwargsSpec]
    ) -> "PipelineBuilder":
        spec: GraphLookupSpec = kwargs  # type: ignore
        if "from_" in kwargs:
            spec["from"] = kwargs.pop("from_") # type: ignore
        if "as_" in kwargs:
            spec["as"] = kwargs.pop("as_") # type: ignore
        return self.add_stage({"$graphLookup": spec})

    def group(
        self,
        **kwargs: Union[
            mongopype_types.Expression, mongopype_types.AccumulatorExpression
        ],
    ) -> "PipelineBuilder":
        return self.add_stage({"$group": kwargs})

    def index_stats(self) -> "PipelineBuilder":
        return self.add_stage({"$indexStats": {}})

    def limit(self, limit: int) -> "PipelineBuilder":
        return self.add_stage({"$limit": limit})

    def list_cluster_catalog(
        self, **kwargs: Unpack[ListClusterCatalogSpec]
    ) -> "PipelineBuilder":
        return self.add_stage({"$listClusterCatalog": kwargs})

    def list_local_sessions(
        self, **kwargs: Unpack[ListLocalSessionsKwargsSpec]
    ) -> "PipelineBuilder":
        return self.add_stage({"$listLocalSessions": kwargs}) # type: ignore

    def list_sampled_queries(
        self, **kwargs: Unpack[ListSampledQueriesSpec]
    ) -> "PipelineBuilder":
        return self.add_stage({"$listSampledQueries": kwargs})

    def list_search_indexes(
        self, **kwargs: Unpack[ListSearchIndexesSpec]
    ) -> "PipelineBuilder":
        return self.add_stage({"$listSearchIndexes": kwargs})

    def list_sessions(
        self, **kwargs: Unpack[ListSessionsKwargsSpec]
    ) -> "PipelineBuilder":
        return self.add_stage({"$listSessions": kwargs}) # type: ignore

    def lookup(self, **kwargs: Unpack[LookupKwargsSpec]) -> "PipelineBuilder":
        spec: LookupSpec = kwargs  # type: ignore
        if "from_" in kwargs:
            spec["from"] = kwargs.pop("from_") # type: ignore
        if "as_" in kwargs:
            spec["as"] = kwargs.pop("as_") # type: ignore

        return self.add_stage({"$lookup": spec})

    def match(self, **kwargs: mongopype_types.BSON) -> "PipelineBuilder":
        return self.add_stage({"$match": kwargs})

    def merge(self, **kwargs: Unpack[MergeDocSpec]) -> "PipelineBuilder":
        return self.add_stage({"$merge": kwargs})

    def out(
        self,
        to: OutSpec,
    ) -> "PipelineBuilder":
        return self.add_stage({"$out": to})

    def plan_cache_stats(
        self, **kwargs: Unpack[PlanCacheStatsSpec]
    ) -> "PipelineBuilder":
        return self.add_stage({"$planCacheStats": kwargs})

    def project(self, **kwargs: Any) -> "PipelineBuilder":
        return self.add_stage({"$project": kwargs})

    def query_settings(self, **kwargs: Unpack[QuerySettingsSpec]) -> "PipelineBuilder":
        return self.add_stage({"$querySettings": kwargs})

    def query_stats(self, **kwargs: Unpack[QueryStatsSpec]) -> "PipelineBuilder":
        return self.add_stage({"$queryStats": kwargs})

    def rank_fusion(self, **kwargs: Unpack[RankFusionSpec]) -> "PipelineBuilder":
        return self.add_stage({"$rankFusion": kwargs})

    def redact(self, expression: mongopype_types.Expression) -> "PipelineBuilder":
        return self.add_stage({"$redact": expression})

    def replace_root(self, **kwargs: Unpack[ReplaceRootSpec]) -> "PipelineBuilder":
        return self.add_stage({"$replaceRoot": kwargs})

    def replace_with(self, new_value: mongopype_types.Expression) -> "PipelineBuilder":
        return self.add_stage({"$replaceWith": new_value})

    def sample(self, **kwargs: Unpack[SampleSpec]) -> "PipelineBuilder":
        return self.add_stage({"$sample": kwargs})

    def score(self, **kwargs: Unpack[ScoreSpec]) -> "PipelineBuilder":
        return self.add_stage({"$score": kwargs})

    def score_fusion(self, **kwargs: Unpack[ScoreFusionSpec]) -> "PipelineBuilder":
        return self.add_stage({"$scoreFusion": kwargs})

    def search(self, **kwargs: Any) -> "PipelineBuilder":
        return self.add_stage({"$search": kwargs})

    def search_meta(self, **kwargs: Any) -> "PipelineBuilder":
        return self.add_stage({"$searchMeta": kwargs})

    def set(self, **kwargs: mongopype_types.Expression) -> "PipelineBuilder":
        return self.add_stage({"$set": kwargs})

    def set_window_fields(
        self, **kwargs: Unpack[SetWindowFieldsSpec]
    ) -> "PipelineBuilder":
        return self.add_stage({"$setWindowFields": kwargs})

    def sharded_data_distribution(self) -> "PipelineBuilder":
        return self.add_stage({"$shardedDataDistribution": {}})

    def skip(self, skip: int) -> "PipelineBuilder":
        return self.add_stage({"$skip": skip})

    def sort(
        self, **kwargs: Union[Literal[1, -1], mongopype_types.MetaTextScore]
    ) -> "PipelineBuilder":
        return self.add_stage({"$sort": kwargs})

    def sort_by_count(self, field: mongopype_types.Expression) -> "PipelineBuilder":
        return self.add_stage({"$sortByCount": field})

    def union_with(self, **kwargs: Unpack[UnionWithFullSpec]) -> "PipelineBuilder":
        return self.add_stage({"$unionWith": kwargs})

    def unset(self, fields: Union[str, list[str]]) -> "PipelineBuilder":
        return self.add_stage({"$unset": fields})

    def unwind(self, **kwargs: Unpack[UnwindDocSpec]) -> "PipelineBuilder":
        return self.add_stage({"$unwind": kwargs})

    def vector_search(self, **kwargs: Unpack[VectorSearchSpec]) -> "PipelineBuilder":
        return self.add_stage({"$vectorSearch": kwargs})
