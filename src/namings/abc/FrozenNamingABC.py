import collections.abc
from typing import *

from namings.abc.BaseNamingABC import BaseNamingABC

__all__ = ["FrozenNamingABC"]
Value = TypeVar("Value", covariant=True)


class FrozenNamingABC(BaseNamingABC[Value], collections.abc.Hashable):
    __slots__ = ()
