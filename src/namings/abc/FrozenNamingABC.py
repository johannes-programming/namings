from typing import *

import setdoc

from namings.abc.BaseNamingABC import BaseNamingABC

__all__ = ["FrozenNamingABC"]
Value = TypeVar("Value")


class FrozenNamingABC(BaseNamingABC[Value]):
    __slots__ = ()

    @setdoc.basic
    def __copy__(self: Self) -> Self:
        return self

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(self.items())
