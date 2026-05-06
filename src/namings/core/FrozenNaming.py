import collections.abc
from types import MappingProxyType
from typing import *

import setdoc
from datarepr import datarepr

from namings._utils.digest import digest_data
from namings.core.BaseNaming import BaseNaming

__all__ = ["FrozenNaming"]
Value = TypeVar("Value")


class FrozenNaming(BaseNaming[Value], collections.abc.Hashable):
    __slots__ = ("_items", "_keys", "_mapping", "_repr", "_values")

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(self.items())

    @setdoc.basic
    def __init__(self: Self, data: Any = (), /, **kwargs: Any) -> None:
        dict_: dict
        x: Any
        y: Any
        if isinstance(data, BaseNaming):
            dict_ = dict(data._mapping)
        else:
            dict_ = digest_data(data)
        for x, y in kwargs.items():
            dict_[str(x)] = y
        self._items = None
        self._keys = None
        self._mapping = MappingProxyType(dict_)
        self._repr = datarepr(type(self).__name__, dict_)
        self._values = None

    @setdoc.basic
    def __or__(self: Self, other: Any) -> Self:
        ans: Self
        mapping: dict
        mapping = self._mapping | digest_data(other)
        ans = object.__new__(type(self))
        ans._mapping = MappingProxyType(mapping)
        ans._repr = datarepr(type(self).__name__, mapping)
        ans._items = None
        ans._keys = None
        ans._values = None
        return ans

    @setdoc.basic
    def __repr__(self: Self) -> str:
        return self._repr
