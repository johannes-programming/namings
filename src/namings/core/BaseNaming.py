import collections.abc
from abc import abstractmethod
from itertools import repeat
from typing import *

import setdoc

__all__ = ["BaseNaming"]

Value = TypeVar("Value")


class BaseNaming(collections.abc.Collection, Generic[Value]):
    __slots__ = ()

    _dict: dict[str, Value]
    _items: Optional[tuple[tuple[str, Value], ...]]
    _keys: Optional[tuple[str, ...]]
    _values: Optional[tuple[Value, ...]]

    @setdoc.basic
    def __contains__(self: Self, other: Any) -> bool:
        return other in self.items()

    @setdoc.basic
    def __eq__(self: Self, other: Any) -> bool:
        return type(self) is type(other) and self.items() == other.items()

    @setdoc.basic
    def __getitem__(self: Self, key: Any) -> Any:
        x: str
        x = str(key)
        try:
            return self._dict[x]
        except KeyError:
            raise KeyError("Key %r unknown." % key) from None

    @abstractmethod
    @setdoc.basic
    def __hash__(self: Self) -> int: ...

    @abstractmethod
    @setdoc.basic
    def __init__(self: Self, data: Any = (), /, **kwargs: Any) -> None: ...

    @setdoc.basic
    def __iter__(self: Self) -> Iterable[tuple[str, Value]]:
        return iter(self.items())

    @setdoc.basic
    def __len__(self: Self) -> int:
        return len(self._dict)

    @abstractmethod
    @setdoc.basic
    def __or__(self: Self, other: Any) -> Self: ...

    @setdoc.basic
    def __repr__(self: Self) -> str:
        return f"{type(self).__name__}({self._dict})"

    @setdoc.basic
    def __reversed__(self: Self) -> reversed:
        return reversed(self.items())

    @classmethod
    def fromkeys(cls: type[Self], keys: Iterable, value: Any = None, /) -> Self:
        return cls(zip(keys, repeat(value)))

    def get(self: Self, key: Any, default: Any = None, /) -> Any:
        "This method returns the value for an existing key or default for a not existing key."
        return self._dict.get(str(key), default)

    def keys(self: Self) -> tuple[str, ...]:
        "This method returns an iterable of the keys."
        if self._keys is None:
            self._keys = tuple(self._dict.keys())
        return self._keys

    def items(self: Self) -> tuple[tuple[str, Value], ...]:
        "This method returns an iterable of the key-value-pairs."
        if self._items is None:
            self._items = tuple(self._dict.items())
        return self._items

    def values(self: Self) -> tuple[Value, ...]:
        "This method returns an iterable of the values."
        if self._values is None:
            self._values = tuple(self._dict.values())
        return self._values
