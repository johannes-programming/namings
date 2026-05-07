from typing import *

import setdoc
from copyable import Copyable

from namings._utils.digest import digest_data
from namings.core.BaseNaming import BaseNaming

__all__ = ["Naming"]

MISSING = object()
Value = TypeVar("Value")


class Naming(BaseNaming[Value], Copyable):
    __slots__ = ("_dict", "_items", "_keys", "_values")

    _dict: dict[str, Value]

    @setdoc.basic
    def __delitem__(self: Self, key: Any) -> None:
        try:
            del self._dict[str(key)]
        except KeyError:
            raise KeyError("Key %r unknown." % key) from None
        finally:
            self._reset()

    __hash__ = None

    @setdoc.basic
    def __init__(self: Self, data: Any = (), /, **kwargs: Any) -> None:
        x: Any
        y: Any
        self._reset()
        if isinstance(data, BaseNaming):
            self._dict = dict(data._dict)
        else:
            self._dict = digest_data(data)
        for x, y in kwargs.items():
            self._dict[str(x)] = y

    @setdoc.basic
    def __ior__(self: Self, other: Any) -> Self:
        try:
            if isinstance(other, BaseNaming):
                self._dict |= other._dict
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
    def __setitem__(self: Self, key: Any, value: Any) -> Any:
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
        ans._items = self._items
        ans._keys = self._keys
        ans._dict = self._dict.copy()
        ans._values = self._values
        return ans

    @overload
    def pop(self: Self, key: Any, /) -> Value: ...

    @overload
    def pop(self: Self, key: Any, default: Any, /) -> Any: ...

    def pop(self: Self, key: Any, default: Any = MISSING, /) -> Value:
        try:
            if default is MISSING:
                return self._dict.pop(str(key))
            else:
                return self._dict.pop(str(key), default)
        finally:
            self._reset()

    def popitem(self: Self) -> tuple[str, Value]:
        "This method deletes and returns the last key-value-pair."
        try:
            return self._dict.popitem()
        finally:
            self._reset()

    def setdefault(self: Self, key: Any, default: Any = None, /) -> Value:
        try:
            return self._dict.setdefault(str(key), default)
        finally:
            self._reset()

    def update(self: Self, data: Any = (), /, **kwargs: Any) -> None:
        "This method updates the key-value-pairs."
        x: Any
        y: Any
        try:
            if isinstance(data, BaseNaming):
                self._dict |= data._dict
            else:
                self._dict |= digest_data(data)
            for x, y in kwargs.items():
                self._dict[str(x)] = y
        finally:
            self._reset()
