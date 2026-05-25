import unittest
from typing import *

from namings.core.Naming import Naming

__all__ = ["TestNotFrozen"]


class TestNotFrozen(unittest.TestCase):
    def test_copy(self: Self) -> None:
        objA: Naming[int | str]
        objA = Naming([["hello", "world"], [4, 2]])
        objB = objA.copy()
        self.assertEqual(objA, objB)
        self.assertEqual(list(objA), [("hello", "world"), ("4", 2)])
        self.assertEqual(list(objB), [("hello", "world"), ("4", 2)])

    def test_clear(self: Self) -> None:
        objA: Naming[int | str]
        objA = Naming([["hello", "world"], [4, 2]])
        objA.clear()
        self.assertEqual(list(objA), [])

    def test_pop(self: Self) -> None:
        obj: Naming[int | str]
        obj = Naming([["hello", "world"], [4, 2]])
        with self.assertRaises(Exception):
            obj.pop("foo")
        self.assertEqual(obj.pop("foo", "bar"), "bar")
        self.assertEqual(list(obj), [("hello", "world"), ("4", 2)])
        self.assertEqual(obj.pop("hello", "bar"), "world")
        self.assertEqual(list(obj), [("4", 2)])

    def test_setdefault(self: Self) -> None:
        objA: Naming[int | str]
        objA = Naming([["hello", "world"], [4, 2]])
        self.assertEqual(objA.setdefault("hello", "!"), "world")
        self.assertEqual(list(objA), [("hello", "world"), ("4", 2)])
        self.assertEqual(objA.setdefault("foo", 3.14), 3.14)
        self.assertEqual(list(objA), [("hello", "world"), ("4", 2), ("foo", 3.14)])

    def test_update(self: Self) -> None:
        obj: Naming[float | int | set[object] | str]
        obj = Naming([["hello", "world"], [4, 2]])
        obj.update([("foo", "bar"), ("hello", 3.14)], baz=set())
        self.assertEqual(
            list(obj), [("hello", 3.14), ("4", 2), ("foo", "bar"), ("baz", set())]
        )

    def test_dunder_delitem(self: Self) -> None:
        objA: Naming[int | str]
        objA = Naming([["hello", "world"], [4, 2]])
        del objA[4]
        self.assertEqual(list(objA), [("hello", "world")])
        with self.assertRaises(Exception):
            del objA["foo"]

    def test_dunder_hash(self: Self) -> None:
        obj: Naming[int | str]
        obj = Naming([["hello", "world"], [4, 2]])
        with self.assertRaises(Exception):
            hash(obj)

    def test_dunder_ior(self: Self) -> None:
        obj: Naming[int | str]
        obj = Naming([["hello", "world"], [4, 2]])
        obj |= [["foo", "bar"], ["hello", 3.14]]
        self.assertEqual(list(obj), [("hello", 3.14), ("4", 2), ("foo", "bar")])

    def test_dunder_setitem(self: Self) -> None:
        objA: Naming[int | str]
        objA = Naming([["hello", "world"], [4, 2]])
        objA["hello"] = "!"
        self.assertEqual(list(objA), [("hello", "!"), ("4", 2)])
        objA["foo"] = "bar"
        self.assertEqual(list(objA), [("hello", "!"), ("4", 2), ("foo", "bar")])


if __name__ == "__main__":
    unittest.main()
