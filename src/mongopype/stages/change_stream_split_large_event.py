from typing import Any, TypedDict

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/changeStreamSplitLargeEvent/

ChangeStreamSplitLargeEventSpec = dict[str, Any]

ChangeStreamSplitLargeEvent = TypedDict("ChangeStreamSplitLargeEvent", {"$changeStreamSplitLargeEvent": ChangeStreamSplitLargeEventSpec})

def verify_change_stream_split_large_event(spec: ChangeStreamSplitLargeEventSpec, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (ordering: must follow $changeStream)
    return True
