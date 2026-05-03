import collections.abc
from itertools import repeat
from typing import *

import setdoc
from copyable import Copyable
from datarepr import datarepr

from namings.core.BaseNaming import BaseNaming

__all__ = ["Naming"]

MISSING = object()
Value = TypeVar("Value")


class Naming(BaseNaming[Value], Copyable, collections.abc.MutableMapping[Value]):
    __slots__ = ("_dict",)

    @setdoc.basic
    def __contains__(self: Self, other: Any) -> bool:
        x: Any
        y: Any
        try:
            x, y = other
            return (str(x), y) in self._dict.items()
        except Exception:
            return False

    @setdoc.basic
    def __delitem__(self: Self, key: Any) -> None:
        try:
            del self._dict[str(key)]
        except KeyError:
            raise KeyError("Key %r unknown." % key)

    @setdoc.basic
    def __eq__(self: Self, other: Any) -> bool:
        return type(self) is type(other) and tuple(self._dict.items()) == tuple(
            other._dict.items()
        )

    @setdoc.basic
    def __getitem__(self: Self, key: Any) -> Any:
        x: str
        x = str(key)
        try:
            return self._dict[x]
        except KeyError:
            raise KeyError("Key %r unknown." % key) from None

    __hash__ = None

    @setdoc.basic
    def __init__(self: Self, data: Any = (), /, **kwargs: Any) -> None:
        a: dict
        x: Any
        y: Any
        self._dict = dict()
        a = dict(data, **kwargs)
        for x, y in a.items():
            self._dict[str(x)] = y

    @setdoc.basic
    def __ior__(self: Self, other: Iterable) -> Self:
        a: dict
        x: Any
        y: Any
        a = dict(other)
        for x, y in a.items():
            self._dict[str(x)] = y
        return self

    @setdoc.basic
    def __iter__(self: Self) -> Iterable[tuple[str, Value]]:
        yield from self._dict.items()

    @setdoc.basic
    def __len__(self: Self) -> int:
        return len(self._dict)

    __ne__ = object.__ne__

    @setdoc.basic
    def __or__(self: Self, other: Any) -> Self:
        return type(self)(self._dict | dict(other))

    @setdoc.basic
    def __repr__(self: Self) -> str:
        return datarepr(type(self).__name__, self._dict)

    @setdoc.basic
    def __reversed__(self: Self) -> Iterator[tuple[str, Value]]:
        yield from reversed(self._dict.items())

    @setdoc.basic
    def __setitem__(self: Self, key: Any, value: Any) -> Any:
        self._dict[str(key)] = value

    def clear(self: Self) -> None:
        "This method discards all key-value-pairs."
        self._dict.clear()

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self)

    @classmethod
    def fromkeys(cls: type[Self], keys: Iterable, value: Value = None, /) -> Self:
        return cls(zip(map(str, keys), repeat(value)))

    def get(self: Self, key: Any, default: Any = None, /) -> Value:
        "This method returns the value for an existing key or default for a not existing key."
        return self._dict.get(str(key), default)

    def items(self: Self) -> Iterator[tuple[str, Value]]:
        "This method returns an iterable of the key-value-pairs."
        yield from self._dict.items()

    def keys(self: Self) -> Iterator[str]:
        "This method returns an iterable of the keys."
        yield from self._dict.keys()

    @overload
    def pop(self: Self, key: Any, /) -> Value: ...

    @overload
    def pop(self: Self, key: Any, default: Any, /) -> Value: ...

    def pop(self: Self, key: Any, default: Any = MISSING, /) -> Value:
        if default is MISSING:
            return self._dict.pop(str(key))
        else:
            return self._dict.pop(str(key), default)

    def popitem(self: Self) -> tuple[str, Value]:
        "This method deletes and returns the last key-value-pair."
        return self._dict.popitem()

    def setdefault(self: Self, key: Any, default: Value = None) -> Value:
        return self._dict.setdefault(str(key), default)

    def update(self: Self, data: Any, /, **kwargs: Any) -> None:
        "This method updates the key-value-pairs."
        a: dict
        x: Any
        y: Any
        a = dict(data, **kwargs)
        for x, y in a.items():
            self._dict[str(x)] = y

    def values(self: Self) -> Iterator[Value]:
        "This method returns an iterable of the values."
        yield from self._dict.values()
