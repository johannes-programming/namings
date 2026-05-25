from collections.abc import Iterable
from typing import Any, Final, Optional, Self, TypeVar, cast, overload

import setdoc

from namings._utils.digest import digest_data
from namings.abc.BaseNamingABC import BaseNamingABC
from namings.abc.NamingABC import NamingABC
from namings.core.BaseNaming import BaseNaming
from namings.typing.SupportsKeysAndGetitem import SupportsKeysAndGetitem

__all__ = ["Naming"]

MISSING: Final[object] = object()
Value = TypeVar("Value")
Value_ = TypeVar("Value_")


class Naming(BaseNaming[Value], NamingABC[Value]):
    __slots__ = ()

    _dict: dict[str, Value]

    @setdoc.basic
    def __delitem__(self: Self, key: object) -> None:
        try:
            del self._dict[str(key)]
        except KeyError:
            raise KeyError("Key %r unknown." % key) from None
        finally:
            self._reset()

    __hash__ = None

    @setdoc.basic
    def __init__(
        self: Self,
        data: (
            SupportsKeysAndGetitem[Value] | Iterable[tuple[object, Value]]
        ) = (),
        /,
        **kwargs: Value,
    ) -> None:
        x: str
        y: Value
        self._reset()
        if isinstance(data, BaseNaming):
            self._dict = dict(data._dict)
        elif isinstance(data, BaseNamingABC):
            self._dict = dict(data)
        else:
            self._dict = digest_data(data)
        for x, y in kwargs.items():
            self._dict[str(x)] = y

    @setdoc.basic
    def __ior__(self: Self, other: Any) -> Self:
        try:
            if isinstance(other, BaseNaming):
                self._dict |= other._dict
            elif isinstance(other, BaseNamingABC):
                self._dict |= other
            else:
                self._dict |= digest_data(other)
            return self
        finally:
            self._reset()

    @setdoc.basic
    def __or__(self: Self, other: Any) -> Self:
        ans: Self
        ans = self.copy()
        ans.__ior__(other)
        return ans

    @setdoc.basic
    def __setitem__(self: Self, key: object, value: Any) -> None:
        try:
            self._dict[str(key)] = value
        finally:
            self._reset()

    def _reset(self: Self) -> None:
        self._items = None
        self._keys = None
        self._values = None

    def clear(self: Self) -> None:
        "This method discards all key-value-pairs."
        try:
            self._dict.clear()
        finally:
            self._reset()

    @setdoc.basic
    def copy(self: Self) -> Self:
        ans: Self
        ans = object.__new__(type(self))
        ans._dict = self._dict.copy()
        ans._items = self._items
        ans._keys = self._keys
        ans._values = self._values
        return ans

    @overload
    def pop(self: Self, key: object, /) -> Value: ...

    @overload
    def pop(
        self: Self,
        key: object,
        default: Value_,
        /,
    ) -> Value | Value_: ...

    def pop(
        self: Self,
        key: object,
        default: Value_ | object = MISSING,
        /,
    ) -> Optional[Value | Value_]:
        ans: Any
        try:
            if default is MISSING:
                return self._dict.pop(str(key))
            else:
                return self._dict.pop(str(key), cast(Value_, default))
        finally:
            self._reset()

    @setdoc.basic
    def setdefault(
        self: Self,
        key: object,
        default: Value,
        /,
    ) -> Value:
        try:
            return self._dict.setdefault(str(key), default)
        finally:
            self._reset()

    def update(
        self: Self,
        data: (
            SupportsKeysAndGetitem[Value] | Iterable[tuple[object, Value]]
        ) = (),
        /,
        **kwargs: Value,
    ) -> None:
        "This method updates the key-value-pairs."
        x: Any
        y: Any
        try:
            if isinstance(data, BaseNaming):
                self._dict |= data._dict
            elif isinstance(data, BaseNamingABC):
                self._dict |= data
            else:
                self._dict |= digest_data(data)
            for x, y in kwargs.items():
                self._dict[str(x)] = y
        finally:
            self._reset()
