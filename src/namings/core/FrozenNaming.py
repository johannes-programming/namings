import collections.abc
from typing import *

import setdoc

from namings._utils.digest import digest_data
from namings.core.BaseNaming import BaseNaming

__all__ = ["FrozenNaming"]
Value = TypeVar("Value")


class FrozenNaming(BaseNaming[Value], collections.abc.Hashable):
    __slots__ = ("_dict", "_items", "_keys", "_dict", "_values")

    @setdoc.basic
    def __copy__(self: Self) -> Self:
        return self

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(self.items())

    @setdoc.basic
    def __init__(self: Self, data: Any = (), /, **kwargs: Any) -> None:
        dict_: dict
        x: Any
        y: Any
        if isinstance(data, BaseNaming):
            dict_ = dict(data._dict)
        else:
            dict_ = digest_data(data)
        for x, y in kwargs.items():
            dict_[str(x)] = y
        self._dict = dict_
        self._items = None
        self._keys = None
        self._values = None

    @setdoc.basic
    def __or__(self: Self, other: Any) -> Self:
        ans: Self
        dict_: dict
        dict_ = self._dict | digest_data(other)
        ans = object.__new__(type(self))
        ans._dict = dict_
        ans._items = None
        ans._keys = None
        ans._values = None
        return ans
