import collections.abc
from typing import *

import setdoc
from copyable import Copyable

from namings.core.BaseNaming import BaseNaming

__all__ = ["Naming"]

MISSING = object()
Value = TypeVar("Value")


class Naming(BaseNaming[Value], Copyable, collections.abc.MutableMapping[Value]):
    __slots__ = ()

    @setdoc.basic
    def __delitem__(self: Self, key: Any) -> None:
        try:
            del self._data[str(key)]
        except KeyError:
            raise KeyError("Key %r unknown." % key)

    __hash__ = None

    @setdoc.basic
    def __ior__(self: Self, other: Iterable) -> Self:
        a: dict
        x: Any
        y: Any
        a = dict(other)
        for x, y in a.items():
            self._data[str(x)] = y
        return self

    @setdoc.basic
    def __setitem__(self: Self, key: Any, value: Any) -> Any:
        self._data[str(key)] = value

    def clear(self: Self) -> None:
        "This method discards all key-value-pairs."
        self._data.clear()

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self)

    @overload
    def pop(self: Self, key: Any, /) -> Value: ...

    @overload
    def pop(self: Self, key: Any, default: Any, /) -> Value: ...

    def pop(self: Self, key: Any, default: Any = MISSING, /) -> Value:
        if default is MISSING:
            return self._data.pop(str(key))
        else:
            return self._data.pop(str(key), default)

    def popitem(self: Self) -> tuple[str, Value]:
        "This method deletes and returns the last key-value-pair."
        return self._data.popitem()

    def setdefault(self: Self, key: Any, default: Value = None) -> Value:
        return self._data.setdefault(str(key), default)

    def update(self: Self, data: Any, /, **kwargs: Any) -> None:
        "This method updates the key-value-pairs."
        a: dict
        x: Any
        y: Any
        a = dict(data, **kwargs)
        for x, y in a.items():
            self._data[str(x)] = y
