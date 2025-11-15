from typing import Literal, Any

# https://www.mongodb.com/docs/manual/reference/operator/aggregation/changeStreamSplitLargeEvent/

ChangeStreamSplitLargeEvent = dict[Literal["$changeStreamSplitLargeEvent"], dict[str, Any]]

def verify_change_stream_split_large_event(stage: ChangeStreamSplitLargeEvent, version: str, pipeline_index: int) -> bool:
    # TODO implement verification logic (ordering: must follow $changeStream)
    return True
