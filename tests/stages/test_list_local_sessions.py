"""Tests for $listLocalSessions stage."""
from tests.conftest import V_60
from mongopype.stages.list_local_sessions import verify_list_local_sessions


def test_list_local_sessions_first_empty_valid():
    valid, errors = verify_list_local_sessions({}, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True
    assert errors == []


def test_list_local_sessions_all_users_only_valid():
    valid, errors = verify_list_local_sessions({"allUsers": True}, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True


def test_list_local_sessions_users_only_valid():
    spec = {"users": [{"user": "alice", "db": "admin"}]}
    valid, errors = verify_list_local_sessions(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is True


def test_list_local_sessions_not_first_fails():
    valid, errors = verify_list_local_sessions({}, V_60, pipeline_index=1, pipeline_length=2, is_atlas=False)
    assert valid is False
    assert any("first" in e.lower() for e in errors)


def test_list_local_sessions_all_users_and_users_fails():
    spec = {"allUsers": True, "users": [{"user": "alice", "db": "admin"}]}
    valid, errors = verify_list_local_sessions(spec, V_60, pipeline_index=0, pipeline_length=1, is_atlas=False)
    assert valid is False
    assert any("allUsers" in e and "users" in e for e in errors)
