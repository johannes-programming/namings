import collections.abc
import copy
from types import MappingProxyType
from typing import *

import setdoc
from datarepr import datarepr

from namings._utils.digest import digest_data
from namings.core.BaseNaming import BaseNaming

__all__ = ["FrozenNaming"]
Value = TypeVar("Value")


class FrozenNaming(BaseNaming[Value], collections.abc.Hashable):
    __slots__ = ("_items", "_keys", "_mapping", "_values")

    @setdoc.basic
    def __copy__(self: Self) -> Self:
        return self

    @setdoc.basic
    def __deepcopy__(self: Self, memo: dict[int, Any]) -> Self:
        ans: Self
        ans = object.__new__(type(self))
        ans._items = None
        ans._keys = None
        ans._mapping = copy.deepcopy(self._mapping, memo)
        ans._values = None
        return ans

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
        self._values = None

    @setdoc.basic
    def __or__(self: Self, other: Any) -> Self:
        ans: Self
        dict_: dict
        dict_ = self._mapping | digest_data(other)
        ans = object.__new__(type(self))
        ans._items = None
        ans._keys = None
        ans._mapping = MappingProxyType(dict_)
        ans._values = None
        return ans

    @setdoc.basic
    def __repr__(self: Self) -> str:
        return datarepr(type(self).__name__, dict(self._mapping))
