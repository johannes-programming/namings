from collections.abc import Iterable
from typing import Protocol, TypeVar

import setdoc

__all__ = ["SupportsKeysAndGetitem"]


Value = TypeVar("Value", covariant=True)


class SupportsKeysAndGetitem(Protocol[Value]):
    @setdoc.basic
    def __getitem__(self, key: object, /) -> Value: ...

    def keys(self) -> Iterable[object]: ...
