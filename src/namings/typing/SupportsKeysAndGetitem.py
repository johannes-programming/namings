from collections.abc import Iterable
from typing import Any, Protocol, TypeVar

import setdoc

__all__ = ["SupportsKeysAndGetitem"]


Key = TypeVar("Key", covariant=True)
Value = TypeVar("Value", covariant=True)


class SupportsKeysAndGetitem(Protocol[Key, Value]):
    @setdoc.basic
    def __getitem__(self, key: Any, /) -> Value: ...
    @setdoc.basic
    def keys(self) -> Iterable[Key]: ...
