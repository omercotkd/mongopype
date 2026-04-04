from mongopype.pipeline import Pipeline, PipelineHint

# from mongopype.stages.add_fields import verify_add_fields
from mongopype.stages.bucket import BucketSpec
from mongopype.stages.bucket_auto import BucketAutoSpec
from typing import NotRequired, TypedDict, Union, Never

res = Pipeline(
    [
        {"$addFields": {"total": {"$sum": "$amount"}, "average": {"$avg": "$amount"}}},
        {
            "$bucket": {
                "boundaries": [0, 100, 200, 300],
                "default": "Other",
                "groupBy": "$amount",
                "output": {"count": {"$sum": 1}},
            }
        },
        {"$group": {"_id": "$category", "totalAmount": {"$sum": "$amount"}}},
        {"$count": "totalCount"},
        {
            "$bucketAuto": {
                "buckets": 5,
                "output": {"count": {"$sum": 1}},
                "groupBy": "$amount",
                "granularity": "E48"
            }
        },
    ]
).verify(version="6.0")

# print(f"Pipeline verification result: {res}")


# BucketAuto = TypedDict(
#     "BucketAuto",
#     {"$bucketAuto": BucketAutoSpec},
# )
# Bucket = TypedDict(
#     "Bucket", {"$bucket": BucketSpec}
# )

# PipelineV2 = list[
#     Union[
#         BucketAuto,
#         Bucket,
#     ]
# ]

# x: PipelineV2 = [
#     {
#         "$bucket": {
#             "boundaries": [],
#             "default": "",
#             "groupBy": 1,
#             "output": {"count": {"$sum": 1}},
#         }
#     },
#     {'$bucketAuto': {
#         ""
#     }}
# ]
