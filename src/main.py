from mongopype.pipeline import Pipeline


res = Pipeline(
    [
        {"$addFields": {"total": {"$sum": "$amount"}, "average": {"$avg": "$amount"}}},
        {"$count": "totalCount"},
    ]
).verify(version="6.0")

print(f"Pipeline verification result: {res}")