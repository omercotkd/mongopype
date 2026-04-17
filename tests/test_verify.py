"""Tests for verify_accumulator_expression utility."""
from tests.conftest import V_OLD, V_50, V_52, V_70, V_80, V_81
from mongopype.verify import verify_accumulator_expression


# --- Valid accumulator ---

def test_valid_sum_accumulator():
    valid, err = verify_accumulator_expression({"$sum": "$price"}, V_60)
    assert valid is True
    assert err == ""

def test_valid_avg_accumulator():
    valid, err = verify_accumulator_expression({"$avg": "$amount"}, V_60)
    assert valid is True

def test_valid_push_accumulator():
    valid, err = verify_accumulator_expression({"$push": "$$ROOT"}, V_60)
    assert valid is True


# --- Multiple operators (invalid) ---

def test_two_operators_fails():
    valid, err = verify_accumulator_expression({"$sum": "$x", "$avg": "$y"}, V_60)
    assert valid is False
    assert "exactly one operator" in err


def test_empty_expression_fails():
    valid, err = verify_accumulator_expression({}, V_60)
    assert valid is False


# --- $count (requires >= 5.0) ---

def test_count_accumulator_below_50_fails():
    valid, err = verify_accumulator_expression({"$count": {}}, (4, 9))
    assert valid is False
    assert "5.0" in err

def test_count_accumulator_at_50_ok():
    valid, err = verify_accumulator_expression({"$count": {}}, V_50)
    assert valid is True


# --- 5.2 accumulators ---

V_60 = (6, 0)

def test_bottom_below_52_fails():
    valid, err = verify_accumulator_expression({"$bottom": {}}, (5, 1))
    assert valid is False
    assert "5.2" in err

def test_bottom_at_52_ok():
    valid, err = verify_accumulator_expression({"$bottom": {}}, V_52)
    assert valid is True

def test_bottomN_below_52_fails():
    valid, err = verify_accumulator_expression({"$bottomN": {}}, (5, 1))
    assert valid is False

def test_firstN_below_52_fails():
    valid, err = verify_accumulator_expression({"$firstN": {}}, (5, 1))
    assert valid is False

def test_lastN_below_52_fails():
    valid, err = verify_accumulator_expression({"$lastN": {}}, (5, 1))
    assert valid is False

def test_maxN_below_52_fails():
    valid, err = verify_accumulator_expression({"$maxN": {}}, (5, 1))
    assert valid is False

def test_minN_below_52_fails():
    valid, err = verify_accumulator_expression({"$minN": {}}, (5, 1))
    assert valid is False

def test_topN_below_52_fails():
    valid, err = verify_accumulator_expression({"$topN": {}}, (5, 1))
    assert valid is False

def test_top_at_52_ok():
    valid, err = verify_accumulator_expression({"$top": {}}, V_52)
    assert valid is True


# --- 7.0 accumulators ---

def test_median_below_70_fails():
    valid, err = verify_accumulator_expression({"$median": {}}, (6, 9))
    assert valid is False
    assert "7.0" in err

def test_median_at_70_ok():
    valid, err = verify_accumulator_expression({"$median": {}}, V_70)
    assert valid is True

def test_percentile_below_70_fails():
    valid, err = verify_accumulator_expression({"$percentile": {}}, (6, 9))
    assert valid is False

def test_percentile_at_70_ok():
    valid, err = verify_accumulator_expression({"$percentile": {}}, V_70)
    assert valid is True


# --- 8.1 accumulators ---

def test_concatArrays_below_81_fails():
    valid, err = verify_accumulator_expression({"$concatArrays": []}, V_80)
    assert valid is False
    assert "8.1" in err

def test_concatArrays_at_81_ok():
    valid, err = verify_accumulator_expression({"$concatArrays": []}, V_81)
    assert valid is True

def test_setUnion_below_81_fails():
    valid, err = verify_accumulator_expression({"$setUnion": []}, V_80)
    assert valid is False

def test_setUnion_at_81_ok():
    valid, err = verify_accumulator_expression({"$setUnion": []}, V_81)
    assert valid is True


# --- $accumulator removed in 8.0 ---

def test_accumulator_below_80_ok():
    valid, err = verify_accumulator_expression({"$accumulator": {}}, (7, 9))
    assert valid is True

def test_accumulator_at_80_fails():
    valid, err = verify_accumulator_expression({"$accumulator": {}}, V_80)
    assert valid is False
    assert "8.0" in err
