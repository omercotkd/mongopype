from typing import Any, Literal, Union, Optional
from datetime import datetime
from mongopype import types as mongopype_types
# class DBPipeline:
#     def __init__(self):
#         self._stages: list[dict[str, Any]] = []


class PipelineBuilder:
    def __init__(self, strict: bool = False):
        self._stages: list[dict[mongopype_types.Stages, Any]] = []
        # TODO if strict is True verify stage upon addition
        self.strict = strict

    def verify(self, mongo_version: Optional[str] = None):
        # TODO implement verification logic
        # Will check for stage order
        # If a $search or $vectorSearch is used will try to get
        # connection string and make sure cluster supports it - warn if not

        try:
            import pymongo
        except ImportError:
            raise ImportError(
                "pymongo is required for verification. Please install it via 'pip install pymongo'"
            )

        pymongo.MongoClient()  # just to check if pymongo is installed

    def add_stage(self, stage: dict[mongopype_types.Stages, Any]) -> "PipelineBuilder":
        self._stages.append(stage)
        return self

    # STAGES
    def add_fields(self, fields: dict[str, Any]) -> "PipelineBuilder":
        return self.add_stage({"$addFields": fields})

    def bucket(
        self,
        group_by: "mongopype_types.Expression",
        boundaries: Union[list[int], list[float], list[str], list[datetime]],
        default: Union[int, float, str],
        output: dict[
            str, dict["mongopype_types.Accumulator", "mongopype_types.Expression"]
        ],
    ) -> "PipelineBuilder":
        return self.add_stage(
            {
                "$bucket": {
                    "groupBy": group_by,
                    "boundaries": boundaries,
                    "default": default,
                    "output": output,
                }
            }
        )

    def bucket_auto(
        self,
        group_by: "mongopype_types.Expression",
        buckets: int,
        output: dict[
            str, dict["mongopype_types.Accumulator", "mongopype_types.Expression"]
        ],
        granularity: Optional[str] = None,
    ) -> "PipelineBuilder":

        document: mongopype_types.Document = {
            "groupBy": group_by,
            "buckets": buckets,
            "output": output,
        }

        if granularity:
            document["granularity"] = granularity

        return self.add_stage({"$bucketAuto": document})

    # TODO make sure this is the first stage if used
    # TODO should be a db pipeline and not a collection pipeline
    def change_stream(
        self,
        all_changes_for_cluster: Optional[bool] = None,
        full_document: Optional[
            "mongopype_types.ChaneStreamFullDocumentOptions"
        ] = None,
        full_document_before_change: Optional[
            "mongopype_types.ChaneStreamFullDocumentBeforeChangeOptions"
        ] = None,
        resume_after: Optional[mongopype_types.Document] = None,
        # TODO only after mongo ver 6.0
        show_expanded_events: Optional[bool] = None,
        start_after: Optional[mongopype_types.Document] = None,
        # TODO not allow this if resume after or start after is used
        start_at_operation_time: Optional[datetime] = None,
    ) -> "PipelineBuilder":

        document: mongopype_types.Document = {}
        if all_changes_for_cluster is not None:
            document["allChangesForCluster"] = all_changes_for_cluster
        if full_document is not None:
            document["fullDocument"] = full_document
        if full_document_before_change is not None:
            document["fullDocumentBeforeChange"] = full_document_before_change
        if resume_after is not None:
            document["resumeAfter"] = resume_after
        if show_expanded_events is not None:
            document["showExpandedEvents"] = show_expanded_events
        if start_after is not None:
            document["startAfter"] = start_after
        if start_at_operation_time is not None:
            document["startAtOperationTime"] = start_at_operation_time

        return self.add_stage({"$changeStream": document})

    # TODO make sure this is the last stage if used
    # TODO make sure the first stage is $changeStream
    # TODO should be a db pipeline and not a collection pipeline
    def change_stream_split_large_event(
        self,
    ) -> "PipelineBuilder":
        return self.add_stage({"$changeStreamSplitLargeEvent": {}})

    def coll_stats(
        self,
        latency_stats: Optional[dict[Literal["histograms"], bool]] = None,
        storage_stats: Optional[dict[Literal["scale"], Union[int, float]]] = None,
        # TODO make sure count is an empty document
        count: Optional[mongopype_types.Document] = None,
        query_exec_stats: Optional[mongopype_types.Document] = None,
    ) -> "PipelineBuilder":

        document: mongopype_types.Document = {}
        if latency_stats is not None:
            document["latencyStats"] = latency_stats
        if storage_stats is not None:
            document["storageStats"] = storage_stats
        if count is not None:
            document["count"] = count
        if query_exec_stats is not None:
            document["queryExecStats"] = query_exec_stats

        return self.add_stage({"$collStats": document})

    # TODO verify field_name not empty and no $ or . characters
    def count(self, field_name: str) -> "PipelineBuilder":
        return self.add_stage({"$count": field_name})

    def current_op(self) -> "PipelineBuilder":
        raise NotImplementedError("This stage is not yet implemented.")

    def densify(
        self,
        field: str,
        range: mongopype_types.DensifyRange,
        partition_by_fields: Optional[list[str]] = None,
    ) -> "PipelineBuilder":

        document: mongopype_types.Document = {"field": field, "range": range}
        if partition_by_fields is not None:
            document["partitionByFields"] = partition_by_fields

        return self.add_stage({"$densify": document})

    # TODO should be a db pipeline and not a collection pipeline
    def documents(
        self,
        documents: list[mongopype_types.Document],
    ) -> "PipelineBuilder":
        return self.add_stage({"$documents": documents})

    def facet(
        self,
        facets: dict[str, list[dict[mongopype_types.Stages, Any]]],
    ) -> "PipelineBuilder":
        return self.add_stage({"$facet": facets})

    def fill(
        self,
        # field: str,
        # partition_by_fields: Optional[list[str]] = None,
        # sort_by: Optional[dict[str, Literal[1, -1]]] = None,
        # method: Optional[
        #     mongopype_types.FillMethodOptions
        # ] = None,
        # value: Optional["mongopype_types.Expression"] = None,
    ) -> "PipelineBuilder":
        raise NotImplementedError("This stage is not yet implemented.")
        # document: mongopype_types.Document = {"field": field}
        # if partition_by_fields is not None:
        #     document["partitionByFields"] = partition_by_fields
        # if sort_by is not None:
        #     document["sortBy"] = sort_by
        # if method is not None:
        #     document["method"] = method
        # if value is not None:
        #     document["value"] = value

        # return self.add_stage({"$fill": document})

    # TODO check this - done by AI
    def geo_near(
        self,
        near: mongopype_types.Document,
        distance_field: str,
        # TODO define Expression type
        query: Optional["mongopype_types.Expression"] = None,
        spherical: Optional[bool] = None,
        max_distance: Optional[Union[int, float]] = None,
        min_distance: Optional[Union[int, float]] = None,
        include_locs: Optional[str] = None,
        distance_multiplier: Optional[Union[int, float]] = None,
        key: Optional[str] = None,
        unique_docs: Optional[bool] = None,
    ) -> "PipelineBuilder":

        document: mongopype_types.Document = {
            "near": near,
            "distanceField": distance_field,
        }

        if query is not None:
            document["query"] = query
        if spherical is not None:
            document["spherical"] = spherical
        if max_distance is not None:
            document["maxDistance"] = max_distance
        if min_distance is not None:
            document["minDistance"] = min_distance
        if include_locs is not None:
            document["includeLocs"] = include_locs
        if distance_multiplier is not None:
            document["distanceMultiplier"] = distance_multiplier
        if key is not None:
            document["key"] = key
        if unique_docs is not None:
            document["uniqueDocs"] = unique_docs

        return self.add_stage({"$geoNear": document})

    # TODO check this - done by AI
    def graph_lookup(
        self,
        from_collection: str,
        start_with: "mongopype_types.Expression",
        connect_from_field: str,
        connect_to_field: str,
        as_field: str,
        max_depth: Optional[int] = None,
        depth_field: Optional[str] = None,
        restrict_search_with_match: Optional["mongopype_types.Expression"] = None,
    ) -> "PipelineBuilder":

        document: mongopype_types.Document = {
            "from": from_collection,
            "startWith": start_with,
            "connectFromField": connect_from_field,
            "connectToField": connect_to_field,
            "as": as_field,
        }

        if max_depth is not None:
            document["maxDepth"] = max_depth
        if depth_field is not None:
            document["depthField"] = depth_field
        if restrict_search_with_match is not None:
            document["restrictSearchWithMatch"] = restrict_search_with_match

        return self.add_stage({"$graphLookup": document})

    def group(
        self,
        _id: "mongopype_types.Expression",
        fields: dict[
            str, dict["mongopype_types.Accumulator", "mongopype_types.Expression"]
        ],
    ) -> "PipelineBuilder":
        document: mongopype_types.Document = {"_id": _id, **fields}
        return self.add_stage({"$group": document})

    def index_stats(self) -> "PipelineBuilder":
        return self.add_stage({"$indexStats": {}})

    # TODO limit should be non-negative
    def limit(self, limit: int) -> "PipelineBuilder":
        return self.add_stage({"$limit": limit})

    def list_cluster_catalog(
        self,
        shards: Optional[Literal[True]] = None,
        balancing_configuration: Optional[Literal[True]] = None,
    ) -> "PipelineBuilder":

        document: mongopype_types.Document = {}
        if shards is not None:
            document["shards"] = shards
        if balancing_configuration is not None:
            document["balancingConfiguration"] = balancing_configuration
        return self.add_stage({"$listClusterCatalog": document})

    def list_local_sessions(
        self,
        # all_users: Optional[Literal[True]] = None,
    ) -> "PipelineBuilder":
        raise NotImplementedError("This stage is not yet implemented.")
        # document: mongopype_types.Document = {}
        # if all_users is not None:
        #     document["allUsers"] = all_users
        # return self.add_stage({"$listLocalSessions": document})

    # TODO only work on db aggregation pipeline
    # TODO namespace should contain a .
    def list_sampled_queries(
        self,
        namespace: Optional[str] = None,
    ) -> "PipelineBuilder":

        document: mongopype_types.Document = {}
        if namespace is not None:
            document["namespace"] = namespace

        return self.add_stage({"$listSampledQueries": document})

    def list_search_indexes(
        self,
        id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> "PipelineBuilder":

        document: mongopype_types.Document = {}

        if id is not None:
            document["id"] = id
        if name is not None:
            document["name"] = name

        return self.add_stage({"$listSearchIndexes": document})

    def list_sessions(
        self,
        # all_users: Optional[Literal[True]] = None,
    ) -> "PipelineBuilder":
        raise NotImplementedError("This stage is not yet implemented.")
        # document: mongopype_types.Document = {}
        # if all_users is not None:
        #     document["allUsers"] = all_users
        # return self.add_stage({"$listSessions": document})

    # TODO verify that if local_field or foreign_field is excluded
    # then pipeline must be provided
    def lookup(
        self,
        from_: str,
        as_field: str,
        local_field: Optional[str] = None,
        foreign_field: Optional[str] = None,
        let: Optional[dict[str, "mongopype_types.Expression"]] = None,
        pipeline: Optional[list[dict[mongopype_types.Stages, Any]]] = None,
    ) -> "PipelineBuilder":
        document: mongopype_types.Document = {
            "from": from_,
            "as": as_field,
        }

        if local_field is not None:
            document["localField"] = local_field
        if foreign_field is not None:
            document["foreignField"] = foreign_field
        if let is not None:
            document["let"] = let
        if pipeline is not None:
            document["pipeline"] = pipeline

        return self.add_stage({"$lookup": document})

    def match(
        self,
        query: "mongopype_types.Document",
    ) -> "PipelineBuilder":
        return self.add_stage({"$match": query})

    # TODO make sure this is the last stage if used
    def merge(
        self,
        into: Union[str, mongopype_types.OutputInto],
        on: Optional[Union[str, list[str]]] = None,
        when_matched: Optional[
            Union[
                Literal["replace", "keepExisting", "merge", "fail"],
                list[dict[mongopype_types.Stages, Any]],
            ]
        ] = None,
        let: Optional[dict[str, "mongopype_types.Expression"]] = None,
        when_not_matched: Optional[Literal["insert", "discard", "fail"]] = None,
    ) -> "PipelineBuilder":
        document: mongopype_types.Document = {"into": into}

        if on is not None:
            document["on"] = on
        if when_matched is not None:
            document["whenMatched"] = when_matched
        if let is not None:
            document["let"] = let
        if when_not_matched is not None:
            document["whenNotMatched"] = when_not_matched

        return self.add_stage({"$merge": document})

    def out(
        self,
        to: Union[
            str, mongopype_types.OutputInto, mongopype_types.OutputIntoTimeSeries
        ],
    ) -> "PipelineBuilder":
        return self.add_stage({"$out": to})

    def plan_cache_stats(self, all_hosts: Optional[bool] = None) -> "PipelineBuilder":
        document: mongopype_types.Document = {}
        if all_hosts is not None:
            document["allHosts"] = all_hosts
        return self.add_stage({"$planCacheStats": document})

    def project(
        self,
        projection: dict[str, Any],
    ) -> "PipelineBuilder":
        return self.add_stage({"$project": projection})

    # TODO should be the first stage if used
    def query_settings(
        self,
        show_debug_query_shape: Optional[bool] = None,
    ) -> "PipelineBuilder":
        document: mongopype_types.Document = {}
        if show_debug_query_shape is not None:
            document["showDebugQueryShape"] = show_debug_query_shape
        return self.add_stage({"$querySettings": document})

    def query_stats(
        self,
    ) -> "PipelineBuilder":
        raise NotImplementedError("This stage is not yet implemented.")

    def rank_fusion(
        self,
    ) -> "PipelineBuilder":
        raise NotImplementedError("This stage is not yet implemented.")

    # TODO check if "$$PRUNE" OR "$$DESCEND" OR "$$KEEP" is used
    def redact(
        self,
        expression: "mongopype_types.Expression",
    ) -> "PipelineBuilder":
        return self.add_stage({"$redact": expression})

    def replace_root(
        self,
        new_root: "mongopype_types.Expression",
    ) -> "PipelineBuilder":
        return self.add_stage({"$replaceRoot": {"newRoot": new_root}})

    def replace_with(
        self,
        new_value: "mongopype_types.Expression",
    ) -> "PipelineBuilder":
        return self.add_stage({"$replaceWith": new_value})

    def sample(
        self,
        size: int,
    ) -> "PipelineBuilder":
        return self.add_stage({"$sample": {"size": size}})

    def score(
        self,
        score: "mongopype_types.Expression",
        normalization: Optional[Literal["none", "sigmoid", "minMaxScaler"]] = None,
        weight: Optional[Union[int, float]] = None,
    ) -> "PipelineBuilder":
        document: mongopype_types.Document = {"score": score}
        if normalization is not None:
            document["normalization"] = normalization
        if weight is not None:
            document["weight"] = weight
        return self.add_stage({"$score": document})

    def score_fusion(
        self,
    ) -> "PipelineBuilder":
        raise NotImplementedError("This stage is not yet implemented.")

    # TODO can only be the first stage
    def search(
        self,
    ) -> "PipelineBuilder":
        raise NotImplementedError("This stage is not yet implemented.")

    # TODO can only be used if search is used before
    def search_meta(
        self,
    ) -> "PipelineBuilder":
        raise NotImplementedError("This stage is not yet implemented.")

    def set(
        self,
        fields: dict[str, "mongopype_types.Expression"],
    ) -> "PipelineBuilder":
        return self.add_stage({"$set": fields})

    def set_window_fields(
        self,
    ) -> "PipelineBuilder":
        raise NotImplementedError("This stage is not yet implemented.")

    def sharded_data_distribution(
        self,
    ) -> "PipelineBuilder":
        raise NotImplementedError("This stage is not yet implemented.")

    def skip(
        self,
        # TODO skip should be non-negative
        skip: int,
    ) -> "PipelineBuilder":
        return self.add_stage({"$skip": skip})

    def sort(
        self,
        # TODO validate no more then 32 fields
        sort_by: dict[
            str, Union[Literal[1, -1], dict[Literal["$meta"], Literal["textScore"]]]
        ],
    ) -> "PipelineBuilder":
        return self.add_stage({"$sort": sort_by})
    
    def sort_by_count(
        self,
        field: mongopype_types.Expression,
    ) -> "PipelineBuilder":
        return self.add_stage({"$sortByCount": field})
    
    def union_with(
        self,
        # TODO if not coll provided pipeline is required and first stage must be $documents
        coll: Optional[str] = None,
        pipeline: Optional[list[dict[mongopype_types.Stages, Any]]] = None,
    ) -> "PipelineBuilder":
        document: mongopype_types.Document = {}
        if coll is not None:
            document["coll"] = coll
        if pipeline is not None:
            document["pipeline"] = pipeline
        return self.add_stage({"$unionWith": document})

    def unset(
        self,
        fields: Union[str, list[str]],
    ) -> "PipelineBuilder":
        return self.add_stage({"$unset": fields})
    
    def unwind(
        self,
        path: str,
        include_array_index: Optional[str] = None,
        preserve_null_and_empty_arrays: Optional[bool] = None,
    ) -> "PipelineBuilder":
        # TODO path must start with $
        document: mongopype_types.Document = {"path": path}
        # TODO cannot start with $ 
        if include_array_index is not None:
            document["includeArrayIndex"] = include_array_index
        if preserve_null_and_empty_arrays is not None:
            document["preserveNullAndEmptyArrays"] = preserve_null_and_empty_arrays
        return self.add_stage({"$unwind": document})
    
    def vector_search(
        self,
    ) -> "PipelineBuilder":
        raise NotImplementedError("This stage is not yet implemented.")