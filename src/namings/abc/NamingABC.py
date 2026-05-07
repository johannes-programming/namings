from abc import abstractmethod
from typing import *

import setdoc
from copyable import Copyable

from namings.abc.BaseNamingABC import BaseNamingABC

__all__ = ["Naming"]

MISSING = object()
Value = TypeVar("Value")


class NamingABC(Copyable, BaseNamingABC[Value]):
    __slots__ = ()

    @abstractmethod
    @setdoc.basic
    def __delitem__(self: Self, key: Any) -> None: ...

    @abstractmethod
    @setdoc.basic
    def __ior__(self: Self, other: Any) -> Self: ...

    @abstractmethod
    @setdoc.basic
    def __or__(self: Self, other: Any) -> Self: ...

    @abstractmethod
    @setdoc.basic
    def __setitem__(self: Self, key: Any, value: Any) -> Any: ...

    @abstractmethod
    def clear(self: Self) -> None:
        "This method discards all key-value-pairs."
        ...

    @overload
    def pop(self: Self, key: Any, /) -> Value: ...

    @overload
    def pop(self: Self, key: Any, default: Any, /) -> Any: ...

    @abstractmethod
    def pop(self: Self, key: Any, default: Any = MISSING, /) -> Any: ...

    @abstractmethod
    @setdoc.basic
    def setdefault(self: Self, key: Any, default: Any = None, /) -> Value: ...

    @abstractmethod
    def update(self: Self, data: Any = (), /, **kwargs: Any) -> None:
        "This method updates the key-value-pairs."
        ...
