from abc import abstractmethod
from typing import *

import setdoc
from copyable import Copyable

from namings.abc.BaseNamingABC import BaseNamingABC

__all__ = ["NamingABC"]

MISSING = object()
Value = TypeVar("Value")


class NamingABC(BaseNamingABC[Value], Copyable):
    __slots__ = ()

    @abstractmethod
    @setdoc.basic
    def __delitem__(self: Self, key: object) -> None: ...

    __hash__: Any
    __hash__ = None

    @abstractmethod
    @setdoc.basic
    def __ior__(self: Self, other: Any) -> Self: ...

    @abstractmethod
    @setdoc.basic
    def __setitem__(self: Self, key: object, value: Any) -> None: ...

    @abstractmethod
    def clear(self: Self) -> None: ...

    @overload
    def pop(self: Self, key: object, /) -> Value: ...

    @overload
    def pop(self: Self, key: object, default: Any, /) -> Any: ...

    @abstractmethod
    def pop(self: Self, key: object, default: Any = MISSING, /) -> Any: ...

    @abstractmethod
    @setdoc.basic
    def setdefault(self: Self, key: object, default: Any = None, /) -> Value: ...

    @abstractmethod
    def update(self: Self, data: Any = (), /, **kwargs: Any) -> None:
        "This method updates the key-value-pairs."
        ...
