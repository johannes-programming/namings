from typing import *

__all__ = ["digest_data"]

MISSING = object()


def digest_data(data: Any, /) -> dict[str, Any]:
    ans: dict
    keys: Any
    x: Any
    y: Any
    ans = dict()
    keys = getattr(type(data), "keys", MISSING)
    if keys is MISSING:
        for x, y in data:
            ans[str(x)] = y
    else:
        for x in keys(data):
            ans[str(x)] = data[x]
    return ans
