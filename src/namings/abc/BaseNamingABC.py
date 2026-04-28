import collections.abc
import types
from abc import abstractmethod
from typing import *

import setdoc

__all__ = ["BaseNamingABC"]

Value = TypeVar("Value")


class BaseNamingABC(collections.abc.Collection[Value]):
    __slots__ = ()

    @abstractmethod
    @setdoc.basic
    def __contains__(self: Self, other: Any) -> bool: ...

    @abstractmethod
    @setdoc.basic
    def __eq__(
        self: Self,
        other: object,
    ) -> types.NotImplementedType | bool: ...

    @abstractmethod
    @setdoc.basic
    def __getitem__(self: Self, key: Any) -> Any: ...

    @abstractmethod
    @setdoc.basic
    def __init__(self: Self, data: Any = (), /, **kwargs: Any) -> None: ...

    @abstractmethod
    @setdoc.basic
    def __iter__(self: Self) -> Iterable[tuple[str, Value]]: ...

    @abstractmethod
    @setdoc.basic
    def __len__(self: Self) -> int: ...

    @abstractmethod
    @setdoc.basic
    def __or__(self: Self, other: Any) -> Self: ...

    @abstractmethod
    @setdoc.basic
    def __repr__(self: Self) -> str: ...

    @abstractmethod
    @setdoc.basic
    def __reversed__(self: Self) -> reversed: ...

    @abstractmethod
    def get(self: Self, key: Any, default: Any = None, /) -> Any:
        "This method returns the value for an existing key or default for a not existing key."
        ...

    @abstractmethod
    def keys(self: Self) -> collections.abc.Collection[str]:
        "This method returns an iterable of the keys."
        ...

    @abstractmethod
    def items(self: Self) -> collections.abc.Collection[tuple[str, Value]]:
        "This method returns an iterable of the key-value-pairs."
        ...

    @abstractmethod
    def values(self: Self) -> collections.abc.Collection[Value]:
        "This method returns an iterable of the values."
        ...
