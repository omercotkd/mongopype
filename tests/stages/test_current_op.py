"""Tests for $currentOp stage."""
from tests.conftest import call_verify, V_60, V_71, V_OLD
from mongopype.stages.current_op import verify_current_op


def test_current_op_at_first_position_valid():
    valid, errors = call_verify(verify_current_op, {}, index=0)
    assert valid is True
    assert errors == []


def test_current_op_not_first_fails():
    valid, errors = verify_current_op({}, V_60, pipeline_index=1, pipeline_length=2, is_atlas=False)
    assert valid is False
    assert any("first" in e.lower() for e in errors)


def test_current_op_target_all_nodes_below_71_fails():
    valid, errors = verify_current_op(
        {"targetAllNodes": True}, (7, 0), pipeline_index=0, pipeline_length=1, is_atlas=False
    )
    assert valid is False
    assert any("7.1" in e for e in errors)


def test_current_op_target_all_nodes_at_71_ok():
    valid, errors = verify_current_op(
        {"targetAllNodes": True}, V_71, pipeline_index=0, pipeline_length=1, is_atlas=False
    )
    assert valid is True
