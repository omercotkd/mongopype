from .types import AccumulatorExpression, Version


def verify_accumulator_expression(
    accumulator_expression: AccumulatorExpression, version: Version
) -> tuple[bool, str]:
    """
    Verify the version against the accumulator used.
    In the future full verification of the accumulator specification could be added here.
    """

    if not len(accumulator_expression) == 1:
        return (
            False,
            f"Invalid accumulator expression: {accumulator_expression}. Must contain exactly one operator.",
        )

    operator, _ = next(iter(accumulator_expression.items()))

    # min 5.0 ver accumulators:
    if operator in ["$count"] and version < (5, 0):
        return False, f"{operator} accumulator requires MongoDB >= 5.0."

    # min 5.2 ver accumulators:
    if operator in [
        "$bottom",
        "$bottomN",
        "$firstN",
        "$lastN",
        "$maxN",
        "$minN",
        "$topN",
    ] and version < (5, 2):
        return False, f"{operator} accumulator requires MongoDB >= 5.2."

    # min 8.1 ver accumulators:
    if operator in ["$concatArrays", "$setUnion"] and version < (8, 1):
        return False, f"{operator} accumulator requires MongoDB >= 8.1."

    # min 7.0 ver accumulators:
    if operator in ["$median", "$percentile"] and version < (7, 0):
        return False, f"{operator} accumulator requires MongoDB >= 7.0."

    if operator in ["$accumulator"] and version >= (8, 0):
        return False, f"{operator} is not supported in MongoDB 8.0 and later."

    return True, ""
