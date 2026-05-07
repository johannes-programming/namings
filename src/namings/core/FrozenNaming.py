from typing import *

import setdoc

from namings._utils.digest import digest_data
from namings.abc.BaseNamingABC import BaseNamingABC
from namings.abc.FrozenNamingABC import FrozenNamingABC
from namings.core.BaseNaming import BaseNaming

__all__ = ["FrozenNaming"]
Value = TypeVar("Value")


class FrozenNaming(BaseNaming[Value], FrozenNamingABC[Value]):
    __slots__ = ()

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(self.items())

    @setdoc.basic
    def __init__(self: Self, data: Any = (), /, **kwargs: Any) -> None:
        x: Any
        y: Any
        if isinstance(data, BaseNaming):
            self._dict = dict(data._dict)
        elif isinstance(data, BaseNamingABC):
            self._dict = dict(data)
        else:
            self._dict = digest_data(data)
        for x, y in kwargs.items():
            self._dict[str(x)] = y
        self._items = None
        self._keys = None
        self._values = None

    @setdoc.basic
    def __or__(self: Self, other: Any) -> Self:
        ans: Self
        ans = object.__new__(type(self))
        ans._dict = self._dict | digest_data(other)
        ans._items = None
        ans._keys = None
        ans._values = None
        return ans
