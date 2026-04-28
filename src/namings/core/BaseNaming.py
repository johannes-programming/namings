import collections.abc
from abc import abstractmethod
from itertools import repeat
from typing import *

import setdoc
from datarepr import datarepr
from iterflat import iterflat

__all__ = ["BaseNaming"]

Value = TypeVar("Value")


class BaseNaming(collections.abc.Mapping[str, Value]):
    __slots__ = ("_data",)

    @setdoc.basic
    def __contains__(self: Self, other: Any) -> bool:
        x: Any
        y: Any
        try:
            x, y = other
            return (str(x), y) in self._data.items()
        except Exception:
            return False

    @setdoc.basic
    def __eq__(self: Self, other: Any) -> bool:
        return type(self) is type(other) and tuple(self._data.items()) == tuple(
            other._data.items()
        )

    @setdoc.basic
    def __getitem__(self: Self, key: Any) -> Any:
        x: str
        x = str(key)
        try:
            return self._data[x]
        except KeyError:
            raise KeyError("Key %r unknown." % key) from None

    @abstractmethod
    @setdoc.basic
    def __hash__(self: Self) -> int: ...

    @setdoc.basic
    def __init__(self: Self, data: Any = (), /, **kwargs: Any) -> None:
        a: dict
        x: Any
        y: Any
        self._data = dict()
        a = dict(data, **kwargs)
        for x, y in a.items():
            self._data[str(x)] = y

    @setdoc.basic
    def __iter__(self: Self) -> Iterable[tuple[str, Value]]:
        yield from self._data.items()

    @setdoc.basic
    def __len__(self: Self) -> int:
        return len(self._data)

    __ne__ = object.__ne__

    @setdoc.basic
    def __or__(self: Self, other: Any) -> Self:
        return type(self)(self._data | dict(other))

    @setdoc.basic
    def __repr__(self: Self) -> str:
        return datarepr(type(self).__name__, self._data)

    @setdoc.basic
    def __reversed__(self: Self) -> Iterator[tuple[str, Value]]:
        yield from reversed(self._data.items())

    @classmethod
    def fromkeys(cls: type[Self], keys: Iterable, value: Value = None, /) -> Self:
        return cls(zip(map(str, keys), repeat(value)))

    def get(self: Self, key: Any, default: Any = None, /) -> Value:
        "This method returns the value for an existing key or default for a not existing key."
        return self._data.get(str(key), default)

    def keys(self: Self) -> Iterator[str]:
        "This method returns an iterable of the keys."
        yield from self._data.keys()

    def items(self: Self) -> Iterator[tuple[str, Value]]:
        "This method returns an iterable of the key-value-pairs."
        yield from self._data.items()

    def values(self: Self) -> Iterator[Value]:
        "This method returns an iterable of the values."
        yield from self._data.values()
