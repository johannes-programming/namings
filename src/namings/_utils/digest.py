from typing import *

__all__ = ["digest_data"]

MISSING = object()


def digest_data(data: Any, /) -> dict:
    ans: dict
    keys: Any
    ans = dict()
    keys = getattr(data, "keys", MISSING)
    if keys is not MISSING:
        for x in keys():
            ans[str(x)] = data[x]
        return ans
    keys = getattr(type(data), "keys", MISSING)
    if keys is not MISSING:
        for x in keys(data):
            ans[str(x)] = data[x]
        return ans
    for x, y in data:
        ans[str(x)] = y
    return ans
