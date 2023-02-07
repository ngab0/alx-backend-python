#!/usr/bin/env python3
""" 11 """
from typing import TypeVar, Union, Mapping, Any

T = TypeVar("T")
Def = Union[T, None]
res = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> res:
    """Implementing the Type Var annotation"""
    if key in dct:
        return dct[key]
    else:
        return default
