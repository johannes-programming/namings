import unittest
from typing import *

from namings.core.FrozenNaming import FrozenNaming

__all__ = ["TestFrozen"]


class TestFrozen(unittest.TestCase):

    def test_frozen(self: Self) -> None:
        obj: FrozenNaming[int | str]
        obj = FrozenNaming([["hello", "world"], [4, 2]])
        hash(obj)
        obj = FrozenNaming([[[], "world"], [4, 2]])
        hash(obj)
        obj = FrozenNaming([["hello", []], [4, 2]])
        with self.assertRaises(Exception):
            hash(obj)


if __name__ == "__main__":
    unittest.main()
