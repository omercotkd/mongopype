"""Tests for PipelineBuilder output shapes and chaining."""
from mongopype.builder import PipelineBuilder
from mongopype.pipeline import Pipeline


def _builder() -> PipelineBuilder:
    return PipelineBuilder()


def _stage(builder: PipelineBuilder) -> dict:
    """Return the last (or only) stage from the builder's pipeline."""
    return builder._pipeline[-1]


# --- add_stage ---

def test_add_stage_appends_raw_dict():
    b = _builder().add_stage({"$match": {"x": 1}})
    assert _stage(b) == {"$match": {"x": 1}}


def test_add_stage_returns_builder_for_chaining():
    b = _builder()
    result = b.add_stage({"$match": {}})
    assert result is b


# --- add_fields ---

def test_add_fields():
    b = _builder().add_fields(total={"$sum": "$price"})
    assert _stage(b) == {"$addFields": {"total": {"$sum": "$price"}}}


# --- bucket ---

def test_bucket():
    b = _builder().bucket(
        groupBy="$price",
        boundaries=[0, 10, 100],
        default="Other",
        output={"count": {"$sum": 1}},
    )
    stage = _stage(b)
    assert "$bucket" in stage
    assert stage["$bucket"]["groupBy"] == "$price"
    assert stage["$bucket"]["boundaries"] == [0, 10, 100]


# --- bucket_auto ---

def test_bucket_auto():
    b = _builder().bucket_auto(
        groupBy="$price",
        buckets=5,
        output={"count": {"$sum": 1}},
    )
    stage = _stage(b)
    assert "$bucketAuto" in stage
    assert stage["$bucketAuto"]["buckets"] == 5


# --- change_stream ---

def test_change_stream_empty():
    b = _builder().change_stream()
    assert _stage(b) == {"$changeStream": {}}


def test_change_stream_with_options():
    b = _builder().change_stream(fullDocument="updateLookup")
    assert _stage(b)["$changeStream"]["fullDocument"] == "updateLookup"


# --- change_stream_split_large_event ---

def test_change_stream_split_large_event():
    b = _builder().change_stream_split_large_event()
    assert _stage(b) == {"$changeStreamSplitLargeEvent": {}}


# --- coll_stats ---

def test_coll_stats():
    b = _builder().coll_stats(count={})
    assert "$collStats" in _stage(b)
    assert _stage(b)["$collStats"]["count"] == {}


# --- count ---

def test_count():
    b = _builder().count("total")
    assert _stage(b) == {"$count": "total"}


# --- current_op ---

def test_current_op_empty():
    b = _builder().current_op()
    assert _stage(b) == {"$currentOp": {}}


def test_current_op_with_options():
    b = _builder().current_op(allUsers=True)
    assert _stage(b)["$currentOp"]["allUsers"] is True


# --- densify ---

def test_densify():
    b = _builder().densify(field="timestamp", range={"step": 1, "bounds": "full"})
    stage = _stage(b)
    assert "$densify" in stage
    assert stage["$densify"]["field"] == "timestamp"


# --- documents ---

def test_documents():
    docs = [{"x": 1}, {"x": 2}]
    b = _builder().documents(docs)
    assert _stage(b) == {"$documents": docs}


# --- facet ---

def test_facet():
    sub = Pipeline([{"$match": {"active": True}}])
    b = _builder().facet(active=sub)
    stage = _stage(b)
    assert "$facet" in stage
    assert "active" in stage["$facet"]


# --- fill ---

def test_fill():
    b = _builder().fill(output={"score": {"value": 0}})
    assert "$fill" in _stage(b)
    assert _stage(b)["$fill"]["output"] == {"score": {"value": 0}}


# --- geo_near ---

def test_geo_near():
    b = _builder().geo_near(
        near={"type": "Point", "coordinates": [0.0, 0.0]},
        distanceField="dist",
    )
    stage = _stage(b)
    assert "$geoNear" in stage
    assert stage["$geoNear"]["distanceField"] == "dist"


# --- graph_lookup: from_/as_ renamed ---

def test_graph_lookup_renames_from_and_as():
    b = _builder().graph_lookup(
        from_="employees",
        startWith="$reportsTo",
        connectFromField="reportsTo",
        connectToField="name",
        as_="reportingHierarchy",
    )
    stage = _stage(b)["$graphLookup"]
    assert "from" in stage
    assert "as" in stage
    assert "from_" not in stage
    assert "as_" not in stage
    assert stage["from"] == "employees"
    assert stage["as"] == "reportingHierarchy"


# --- group ---

def test_group():
    b = _builder().group(_id="$category", total={"$sum": "$amount"})
    stage = _stage(b)
    assert "$group" in stage
    assert stage["$group"]["_id"] == "$category"


# --- index_stats ---

def test_index_stats():
    b = _builder().index_stats()
    assert _stage(b) == {"$indexStats": {}}


# --- limit ---

def test_limit():
    b = _builder().limit(10)
    assert _stage(b) == {"$limit": 10}


# --- list_cluster_catalog ---

def test_list_cluster_catalog():
    b = _builder().list_cluster_catalog(shards=True)
    assert _stage(b)["$listClusterCatalog"]["shards"] is True


# --- list_local_sessions ---

def test_list_local_sessions_all_users():
    b = _builder().list_local_sessions(allUsers=True)
    assert _stage(b)["$listLocalSessions"]["allUsers"] is True


# --- list_sampled_queries ---

def test_list_sampled_queries():
    b = _builder().list_sampled_queries(namespace="db.col")
    assert _stage(b)["$listSampledQueries"]["namespace"] == "db.col"


# --- list_search_indexes ---

def test_list_search_indexes_by_name():
    b = _builder().list_search_indexes(name="my_index")
    assert _stage(b)["$listSearchIndexes"]["name"] == "my_index"


# --- list_sessions ---

def test_list_sessions():
    b = _builder().list_sessions(allUsers=False)
    assert "$listSessions" in _stage(b)


# --- lookup: from_/as_ renamed ---

def test_lookup_equality_form_renames_keys():
    b = _builder().lookup(
        from_="orders",
        localField="customerId",
        foreignField="_id",
        as_="orders",
    )
    stage = _stage(b)["$lookup"]
    assert "from" in stage
    assert "as" in stage
    assert "from_" not in stage
    assert "as_" not in stage
    assert stage["from"] == "orders"
    assert stage["localField"] == "customerId"


# --- match ---

def test_match():
    b = _builder().match(status="active")
    assert _stage(b) == {"$match": {"status": "active"}}


# --- merge ---

def test_merge():
    b = _builder().merge(into="output_collection")
    assert _stage(b)["$merge"]["into"] == "output_collection"


# --- out string form ---

def test_out_string():
    b = _builder().out("results")
    assert _stage(b) == {"$out": "results"}


def test_out_dict_form():
    b = _builder().out({"db": "mydb", "coll": "results"})
    assert _stage(b)["$out"]["db"] == "mydb"


# --- plan_cache_stats ---

def test_plan_cache_stats():
    b = _builder().plan_cache_stats()
    assert "$planCacheStats" in _stage(b)


# --- project ---

def test_project():
    b = _builder().project(name=1, age=1)
    stage = _stage(b)
    assert "$project" in stage
    assert stage["$project"]["name"] == 1


# --- query_settings ---

def test_query_settings():
    b = _builder().query_settings(showDebugQueryShape=True)
    assert _stage(b)["$querySettings"]["showDebugQueryShape"] is True


# --- query_stats ---

def test_query_stats():
    b = _builder().query_stats()
    assert "$queryStats" in _stage(b)


# --- rank_fusion ---

def test_rank_fusion():
    b = _builder().rank_fusion(input={"pipelines": {"p1": []}})
    assert "$rankFusion" in _stage(b)


# --- redact ---

def test_redact():
    b = _builder().redact("$$DESCEND")
    assert _stage(b) == {"$redact": "$$DESCEND"}


# --- replace_root ---

def test_replace_root():
    b = _builder().replace_root(newRoot="$embedded")
    assert _stage(b)["$replaceRoot"]["newRoot"] == "$embedded"


# --- replace_with ---

def test_replace_with():
    b = _builder().replace_with("$embedded")
    assert _stage(b) == {"$replaceWith": "$embedded"}


# --- sample ---

def test_sample():
    b = _builder().sample(size=100)
    assert _stage(b) == {"$sample": {"size": 100}}


# --- score ---

def test_score():
    b = _builder().score(score={"$meta": "searchScore"})
    assert "$score" in _stage(b)


# --- score_fusion ---

def test_score_fusion():
    b = _builder().score_fusion()
    assert "$scoreFusion" in _stage(b)


# --- search ---

def test_search():
    b = _builder().search(text={"query": "hello", "path": "content"})
    assert "$search" in _stage(b)
    assert "text" in _stage(b)["$search"]


# --- search_meta ---

def test_search_meta():
    b = _builder().search_meta(facet={"operator": {}, "facets": {}})
    assert "$searchMeta" in _stage(b)


# --- set ---

def test_set():
    b = _builder().set(fullName={"$concat": ["$first", " ", "$last"]})
    assert "$set" in _stage(b)
    assert "fullName" in _stage(b)["$set"]


# --- set_window_fields ---

def test_set_window_fields():
    b = _builder().set_window_fields(
        sortBy={"date": 1},
        output={"runningTotal": {"$sum": "$amount"}},
    )
    stage = _stage(b)
    assert "$setWindowFields" in stage
    assert stage["$setWindowFields"]["sortBy"] == {"date": 1}


# --- sharded_data_distribution ---

def test_sharded_data_distribution():
    b = _builder().sharded_data_distribution()
    assert _stage(b) == {"$shardedDataDistribution": {}}


# --- skip ---

def test_skip():
    b = _builder().skip(20)
    assert _stage(b) == {"$skip": 20}


# --- sort ---

def test_sort():
    b = _builder().sort(age=1, name=-1)
    stage = _stage(b)
    assert "$sort" in stage
    assert stage["$sort"]["age"] == 1
    assert stage["$sort"]["name"] == -1


# --- sort_by_count ---

def test_sort_by_count():
    b = _builder().sort_by_count("$category")
    assert _stage(b) == {"$sortByCount": "$category"}


# --- union_with ---

def test_union_with_coll():
    b = _builder().union_with(coll="other_collection")
    assert _stage(b)["$unionWith"]["coll"] == "other_collection"


# --- unset string form ---

def test_unset_string():
    b = _builder().unset("password")
    assert _stage(b) == {"$unset": "password"}


def test_unset_list():
    b = _builder().unset(["password", "secret"])
    assert _stage(b) == {"$unset": ["password", "secret"]}


# --- unwind ---

def test_unwind():
    b = _builder().unwind(path="$tags")
    stage = _stage(b)
    assert "$unwind" in stage
    assert stage["$unwind"]["path"] == "$tags"


# --- vector_search ---

def test_vector_search():
    b = _builder().vector_search(
        index="vector_index",
        path="embedding",
        queryVector=[0.1, 0.2, 0.3],
        limit=10,
    )
    stage = _stage(b)
    assert "$vectorSearch" in stage
    assert stage["$vectorSearch"]["index"] == "vector_index"


# --- chaining ---

def test_chaining_produces_correct_pipeline_length():
    b = _builder().match(active=True).limit(10).skip(0)
    assert len(b._pipeline) == 3


def test_chaining_stages_in_correct_order():
    b = _builder().match(active=True).limit(10)
    assert "$match" in b._pipeline[0]
    assert "$limit" in b._pipeline[1]


def test_chaining_returns_same_builder_instance():
    b = _builder()
    b2 = b.match().limit(5)
    assert b2 is b


# --- verify delegation ---

def test_verify_delegates_to_pipeline():
    b = _builder().count("total")
    # count with a valid field should pass verification at version (0,0)
    valid, errors = b.verify()
    assert valid is True
