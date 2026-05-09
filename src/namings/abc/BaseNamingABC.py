import collections.abc
import types
from abc import abstractmethod
from typing import *

import setdoc

__all__ = ["BaseNamingABC"]

Value = TypeVar("Value")


class BaseNamingABC(collections.abc.Collection[tuple[str, Value]]):
    __slots__ = ()

    @setdoc.basic
    def __contains__(self: Self, other: Any, /) -> bool:
        return other in self.items()

    @setdoc.basic
    def __eq__(
        self: Self,
        other: object,
        /,
    ) -> types.NotImplementedType | bool:
        if isinstance(other, BaseNamingABC):
            return tuple(self) == tuple(other)
        else:
            return NotImplemented

    @abstractmethod
    @setdoc.basic
    def __getitem__(self: Self, key: object, /) -> Value: ...

    @abstractmethod
    @setdoc.basic
    def __init__(self: Self, data: Any = (), /, **kwargs: Any) -> None: ...

    @setdoc.basic
    def __iter__(self: Self) -> Iterable[tuple[str, Value]]:
        return iter(self.items())

    @setdoc.basic
    def __len__(self: Self) -> int:
        return len(self.items())

    @abstractmethod
    @setdoc.basic
    def __or__(self: Self, other: Any, /) -> Self: ...

    @setdoc.basic
    def __repr__(self: Self) -> str:
        return f"{type(self).__name__}({dict(self)})"

    @setdoc.basic
    def __reversed__(self: Self) -> Iterable[tuple[str, Value]]:
        return reversed(self.items())

    def get(self: Self, key: object, default: Any = None, /) -> Any:
        "This method returns the value for an existing key or default for a not existing key."
        try:
            return self[key]
        except KeyError:
            return default

    @abstractmethod
    def keys(self: Self) -> tuple[str, ...]:
        "This method returns an iterable of the keys."
        ...

    @abstractmethod
    def items(self: Self) -> tuple[tuple[str, Value], ...]:
        "This method returns an iterable of the key-value-pairs."
        ...

    @abstractmethod
    def values(self: Self) -> tuple[Value, ...]:
        "This method returns an iterable of the values."
        ...
