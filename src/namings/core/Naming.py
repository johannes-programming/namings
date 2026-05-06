import collections.abc
from typing import *

import setdoc
from copyable import Copyable
from datarepr import datarepr

from namings._utils.digest import digest_data
from namings.core.BaseNaming import BaseNaming

__all__ = ["Naming"]

MISSING = object()
Value = TypeVar("Value")


class Naming(BaseNaming[Value], Copyable, collections.abc.MutableMapping[str, Value]):
    __slots__ = ("_items", "_keys", "_mapping", "_repr", "_values")

    @setdoc.basic
    def __copy__(self: Self) -> Self:
        return self.copy()

    @setdoc.basic
    def __delitem__(self: Self, key: Any) -> None:
        try:
            del self._mapping[str(key)]
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
            self._mapping = dict(data._mapping)
        else:
            self._mapping = digest_data(data)
        for x, y in kwargs.items():
            self._mapping[str(x)] = y

    @setdoc.basic
    def __ior__(self: Self, other: Any) -> Self:
        try:
            if isinstance(other, BaseNaming):
                self._mapping |= other._mapping
            else:
                self._mapping |= digest_data(other)
            return self
        finally:
            self._reset()

    @setdoc.basic
    def __or__(self: Self, other: Any) -> Self:
        ans: Self
        ans = self.copy()
        if isinstance(other, BaseNaming):
            ans._mapping |= other._mapping
        else:
            ans._mapping |= digest_data(other)
        return ans

    @setdoc.basic
    def __repr__(self: Self) -> str:
        if self._repr is None:
            self._repr = datarepr(type(self).__name__, self._mapping)
        return self._repr

    @setdoc.basic
    def __setitem__(self: Self, key: Any, value: Any) -> Any:
        try:
            self._mapping[str(key)] = value
        finally:
            self._reset()

    def _reset(self: Self) -> None:
        self._items = None
        self._keys = None
        self._repr = None
        self._values = None

    def clear(self: Self) -> None:
        "This method discards all key-value-pairs."
        try:
            self._mapping.clear()
        finally:
            self._reset()

    @setdoc.basic
    def copy(self: Self) -> Self:
        ans: Self
        ans = object.__new__(type(self))
        ans._reset()
        ans._mapping = self._mapping.copy()
        return ans

    @overload
    def pop(self: Self, key: Any, /) -> Value: ...

    @overload
    def pop(self: Self, key: Any, default: Any, /) -> Value: ...

    def pop(self: Self, key: Any, default: Any = MISSING, /) -> Value:
        try:
            if default is MISSING:
                return self._mapping.pop(str(key))
            else:
                return self._mapping.pop(str(key), default)
        finally:
            self._reset()

    def popitem(self: Self) -> tuple[str, Value]:
        "This method deletes and returns the last key-value-pair."
        try:
            return self._mapping.popitem()
        finally:
            self._reset()

    def setdefault(self: Self, key: Any, default: Value = None, /) -> Value:
        try:
            return self._mapping.setdefault(str(key), default)
        finally:
            self._reset()

    def update(self: Self, data: Any = (), /, **kwargs: Any) -> None:
        "This method updates the key-value-pairs."
        x: Any
        y: Any
        try:
            if isinstance(data, BaseNaming):
                self._mapping |= data._mapping
            else:
                self._mapping |= digest_data(data)
            for x, y in kwargs.items():
                self._mapping[str(x)] = y
        finally:
            self._reset()
