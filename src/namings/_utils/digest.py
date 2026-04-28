from collections.abc import Iterable
from typing import Any, TypeVar, cast

from ..typing.SupportsKeysAndGetitem import SupportsKeysAndGetitem

__all__ = ["digest_data"]

Value = TypeVar("Value")

MISSING = object()


def digest_data(
    data: SupportsKeysAndGetitem[Value] | Iterable[tuple[object, Value]],
    /,
) -> dict[str, Value]:
    ans: dict[str, Value]
    x: object
    y: Value
    z: object
    ans = dict()
    if isinstance(data, SupportsKeysAndGetitem):
        for z in data.keys():
            ans[str(z)] = data[z]
    else:
        for x, y in data:
            ans[str(x)] = y
    return ans
