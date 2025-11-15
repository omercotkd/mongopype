from typing import Union, Any
from .stages.add_fields import AddFields, verify_add_fields
from .stages.bucket import Bucket, verify_bucket
from .stages.bucket_auto import BucketAuto, verify_bucket_auto
from .stages.change_stream import ChangeStream, verify_change_stream
from .stages.change_stream_split_large_event import (
    ChangeStreamSplitLargeEvent,
    verify_change_stream_split_large_event,
)
from .stages.coll_stats import CollStats, verify_coll_stats
from .stages.count import Count, verify_count
from .stages.current_op import CurrentOp, verify_current_op
from .stages.densify import Densify, verify_densify
from .stages.documents import Documents, verify_documents
from .stages.facet import Facet, verify_facet
from .stages.fill import Fill, verify_fill
from .stages.geo_near import GeoNear, verify_geo_near
from .stages.graph_lookup import GraphLookup, verify_graph_lookup
from .stages.group import Group, verify_group
from .stages.index_stats import IndexStats, verify_index_stats
from .stages.limit import Limit, verify_limit
from .stages.list_cluster_catalog import (
    ListClusterCatalog,
    verify_list_cluster_catalog,
)
from .stages.list_local_sessions import (
    ListLocalSessions,
    verify_list_local_sessions,
)
from .stages.list_sampled_queries import (
    ListSampledQueries,
    verify_list_sampled_queries,
)
from .stages.list_search_indexes import (
    ListSearchIndexes,
    verify_list_search_indexes,
)
from .stages.list_sessions import ListSessions, verify_list_sessions
from .stages.lookup import Lookup, verify_lookup
from .stages.match import Match, verify_match
from .stages.merge import Merge, verify_merge
from .stages.out import Out, verify_out
from .stages.plan_cache_stats import PlanCacheStats, verify_plan_cache_stats
from .stages.project import Project, verify_project
from .stages.query_settings import QuerySettings, verify_query_settings
from .stages.query_stats import QueryStats, verify_query_stats
from .stages.rank_fusion import RankFusion, verify_rank_fusion
from .stages.redact import Redact, verify_redact
from .stages.replace_root import ReplaceRoot, verify_replace_root
from .stages.replace_with import ReplaceWith, verify_replace_with
from .stages.sample import Sample, verify_sample
from .stages.score import Score, verify_score
from .stages.score_fusion import ScoreFusion, verify_score_fusion
from .stages.search import Search, verify_search
from .stages.search_meta import SearchMeta, verify_search_meta
from .stages.set import Set, verify_set
from .stages.set_window_fields import SetWindowFields, verify_set_window_fields
from .stages.sharded_data_distribution import (
    ShardedDataDistribution,
    verify_sharded_data_distribution,
)
from .stages.skip import Skip, verify_skip
from .stages.sort import Sort, verify_sort
from .stages.sort_by_count import SortByCount, verify_sort_by_count
from .stages.union_with import UnionWith, verify_union_with
from .stages.unset import Unset, verify_unset
from .stages.unwind import Unwind, verify_unwind
from .stages.vector_search import VectorSearch, verify_vector_search


PipelineHint = Union[
    AddFields,
    Bucket,
    BucketAuto,
    ChangeStream,
    ChangeStreamSplitLargeEvent,
    CollStats,
    Count,
    CurrentOp,
    Densify,
    Documents,
    Facet,
    Fill,
    GeoNear,
    GraphLookup,
    Group,
    IndexStats,
    Limit,
    ListClusterCatalog,
    ListLocalSessions,
    ListSampledQueries,
    ListSearchIndexes,
    ListSessions,
    Lookup,
    Match,
    Merge,
    Out,
    PlanCacheStats,
    Project,
    QuerySettings,
    QueryStats,
    RankFusion,
    Redact,
    ReplaceRoot,
    ReplaceWith,
    Sample,
    Score,
    ScoreFusion,
    Search,
    SearchMeta,
    Set,
    SetWindowFields,
    ShardedDataDistribution,
    Skip,
    Sort,
    SortByCount,
    UnionWith,
    Unset,
    Unwind,
    VectorSearch,
]


__MAPPING__: Any = {
    "$addFields": verify_add_fields,
    "$bucket": verify_bucket,
    "$bucketAuto": verify_bucket_auto,
    "$changeStream": verify_change_stream,
    "$changeStreamSplitLargeEvent": verify_change_stream_split_large_event,
    "$collStats": verify_coll_stats,
    "$count": verify_count,
    "$currentOp": verify_current_op,
    "$densify": verify_densify,
    "$documents": verify_documents,
    "$facet": verify_facet,
    "$fill": verify_fill,
    "$geoNear": verify_geo_near,
    "$graphLookup": verify_graph_lookup,
    "$group": verify_group,
    "$indexStats": verify_index_stats,
    "$limit": verify_limit,
    "$listClusterCatalog": verify_list_cluster_catalog,
    "$listLocalSessions": verify_list_local_sessions,
    "$listSampledQueries": verify_list_sampled_queries,
    "$listSearchIndexes": verify_list_search_indexes,
    "$listSessions": verify_list_sessions,
    "$lookup": verify_lookup,
    "$match": verify_match,
    "$merge": verify_merge,
    "$out": verify_out,
    "$planCacheStats": verify_plan_cache_stats,
    "$project": verify_project,
    "$querySettings": verify_query_settings,
    "$queryStats": verify_query_stats,
    "$rankFusion": verify_rank_fusion,
    "$redact": verify_redact,
    "$replaceRoot": verify_replace_root,
    "$replaceWith": verify_replace_with,
    "$sample": verify_sample,
    "$score": verify_score,
    "$scoreFusion": verify_score_fusion,
    "$search": verify_search,
    "$searchMeta": verify_search_meta,
    "$set": verify_set,
    "$setWindowFields": verify_set_window_fields,
    "$shardedDataDistribution": verify_sharded_data_distribution,
    "$skip": verify_skip,
    "$sort": verify_sort,
    "$sortByCount": verify_sort_by_count,
    "$unionWith": verify_union_with,
    "$unset": verify_unset,
    "$unwind": verify_unwind,
    "$vectorSearch": verify_vector_search,
}

class Pipeline(list[PipelineHint]):
    def verify(self, version: str) -> bool:
        for index, stage in enumerate(self):
            stage_key = next(iter(stage))
            verify_function = __MAPPING__.get(stage_key)
            if verify_function:
                if not verify_function(stage, version, index):
                    return False
        return True