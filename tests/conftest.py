"""Shared fixtures and helpers for mongopype tests."""
from mongopype.types import Version

# Version constants
V_OLD: Version = (3, 6)
V_42: Version = (4, 2)
V_44: Version = (4, 4)
V_50: Version = (5, 0)
V_51: Version = (5, 1)
V_52: Version = (5, 2)
V_53: Version = (5, 3)
V_60: Version = (6, 0)
V_70: Version = (7, 0)
V_71: Version = (7, 1)
V_80: Version = (8, 0)
V_81: Version = (8, 1)


def call_verify(fn, spec, version=V_60, index=0, length=1, is_atlas=False):
    """Call a stage verify function with the given arguments."""
    return fn(spec, version, index, length, is_atlas)
