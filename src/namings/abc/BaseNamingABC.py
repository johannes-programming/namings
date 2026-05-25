from __future__ import annotations

import types
from abc import abstractmethod
from collections.abc import (
    Collection,
    Iterable,
    Iterator,
    Reversible,
    Sequence,
)
from typing import Any, Optional, Self, TypeVar

import setdoc

from namings.typing.SupportsKeysAndGetitem import SupportsKeysAndGetitem

__all__ = ["BaseNamingABC"]

Value = TypeVar("Value", covariant=True)
Value_ = TypeVar("Value_")


class BaseNamingABC(
    Collection[tuple[str, Value]],
    Reversible[tuple[str, Value]],
):
    __slots__ = ()

    @setdoc.basic
    def __contains__(self: Self, other: object, /) -> bool:
        return other in self.items()

    @setdoc.basic
    def __eq__(
        self: Self,
        other: object,
        /,
    ) -> types.NotImplementedType | bool:
        if isinstance(other, BaseNamingABC):
            return bool(tuple(self) == tuple(other))
        else:
            return NotImplemented

    @setdoc.basic
    def __ge__(
        self: Self,
        other: object,
        /,
    ) -> types.NotImplementedType | bool:
        if isinstance(other, BaseNamingABC):
            return bool(tuple(self) >= tuple(other))
        else:
            return NotImplemented

    @setdoc.basic
    def __gt__(
        self: Self,
        other: object,
        /,
    ) -> types.NotImplementedType | bool:
        if isinstance(other, BaseNamingABC):
            return bool(tuple(self) > tuple(other))
        else:
            return NotImplemented

    @abstractmethod
    @setdoc.basic
    def __getitem__(self: Self, key: object, /) -> Value: ...

    @abstractmethod
    @setdoc.basic
    def __init__(
        self: Self,
        data: (
            SupportsKeysAndGetitem[Value] | Iterable[tuple[object, Value]]
        ) = (),
        /,
        **kwargs: Value,
    ) -> None: ...

    @setdoc.basic
    def __iter__(self: Self) -> Iterator[tuple[str, Value]]:
        return iter(self.items())

    @setdoc.basic
    def __le__(
        self: Self,
        other: object,
        /,
    ) -> types.NotImplementedType | bool:
        if isinstance(other, BaseNamingABC):
            return bool(tuple(self) <= tuple(other))
        else:
            return NotImplemented

    @setdoc.basic
    def __len__(self: Self) -> int:
        return len(self.items())

    @setdoc.basic
    def __lt__(
        self: Self,
        other: object,
        /,
    ) -> types.NotImplementedType | bool:
        if isinstance(other, BaseNamingABC):
            return bool(tuple(self) < tuple(other))
        else:
            return NotImplemented

    @setdoc.basic
    def __ne__(
        self: Self,
        other: object,
        /,
    ) -> types.NotImplementedType | bool:
        if isinstance(other, BaseNamingABC):
            return bool(tuple(self) != tuple(other))
        else:
            return NotImplemented

    @abstractmethod
    @setdoc.basic
    def __or__(self: Self, other: BaseNamingABC[Value], /) -> Self: ...

    @setdoc.basic
    def __repr__(self: Self) -> str:
        return f"{type(self).__name__}({dict(self)})"

    @setdoc.basic
    def __reversed__(self: Self) -> Iterator[tuple[str, Value]]:
        return reversed(self.items())

    def get(
        self: Self,
        key: object,
        default: Optional[Value_] = None,
        /,
    ) -> Optional[Value | Value_]:
        "This method returns the value for an existing key or default for a not existing key."
        try:
            return self[key]
        except KeyError:
            return default

    @abstractmethod
    def keys(self: Self) -> Sequence[str]:
        "This method returns a sequence of the keys."
        ...

    @abstractmethod
    def items(self: Self) -> Sequence[tuple[str, Value]]:
        "This method returns a sequence of the items."
        ...

    @abstractmethod
    def values(self: Self) -> Sequence[Value]:
        "This method returns a sequence of the values."
        ...
