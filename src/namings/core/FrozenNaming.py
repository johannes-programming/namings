import collections.abc
from typing import *

import setdoc

from namings.core.BaseNaming import BaseNaming

__all__ = ["FrozenNaming"]
Value = TypeVar("Value")


class FrozenNaming(BaseNaming[Value], collections.abc.Hashable):
    __slots__ = ()

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(tuple(self._data.items()))
