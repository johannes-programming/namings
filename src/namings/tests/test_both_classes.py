import unittest
from typing import *

from namings.core.FrozenNaming import FrozenNaming
from namings.core.Naming import Naming

__all__ = ["Test0"]


class TestBothClasses(unittest.TestCase):
    def test_both_classes(self: Self) -> None:
        for cls in (FrozenNaming, Naming):
            self.dunder(cls)
            self.method(cls)
            self.slots(cls)
            self.stars(cls)

    def dunder(self: Self, cls: type) -> None:
        self.dunder_contains(cls)
        self.dunder_eq(cls)
        self.dunder_getitem(cls)
        self.dunder_iter(cls)
        self.dunder_len(cls)
        self.dunder_repr(cls)
        self.dunder_reversed(cls)

    def dunder_contains(self: Self, cls: type) -> None:
        obj: Any
        obj = cls([["hello", "world"], [4, 2]])
        self.assertIn(("hello", "world"), obj)
        self.assertIn(["hello", "world"], obj)
        self.assertIn(("4", 2), obj)
        self.assertIn((4, 2), obj)
        self.assertNotIn(("foo", "bar"), obj)

    def dunder_eq(self: Self, cls: type) -> None:
        objA: Any
        objA = cls([["hello", "world"], [4, 2]])
        objB = cls([["hello", "world"], ["4", 2]])
        objC = cls([[4, 2], ["hello", "world"]])
        objD = cls([["hello", "world"], [4, 2], ["foo", "bar"]])
        self.assertEqual(objA, objB)
        self.assertNotEqual(objA, objC)
        self.assertNotEqual(objA, objD)
        self.assertNotEqual(objB, objC)
        self.assertNotEqual(objB, objD)
        self.assertNotEqual(objC, objD)

    def dunder_getitem(self: Self, cls: type) -> None:
        obj: Any
        obj = cls([["hello", "world"], [4, 2]])
        self.assertEqual(obj["hello"], "world")
        self.assertEqual(obj["4"], 2)
        with self.assertRaises(KeyError):
            obj["foo"]

    def dunder_iter(self: Self, cls: type) -> None:
        obj: Any
        obj = cls([["hello", "world"], [4, 2]])
        self.assertEqual(list(obj), [("hello", "world"), ("4", 2)])

    def dunder_len(self: Self, cls: type) -> None:
        obj: Any
        obj = cls([["hello", "world"], [4, 2]])
        self.assertEqual(len(obj), 2)

    def dunder_repr(self: Self, cls: type) -> None:
        answer: str
        dict_: dict
        obj: Any
        solution: str
        dict_ = {"hello": "world", "4": 2}
        obj = cls([["hello", "world"], [4, 2]])
        answer = repr(obj)
        solution = cls.__name__ + "(" + repr(dict_) + ")"
        self.assertEqual(answer, solution)

    def dunder_reversed(self: Self, cls: type) -> None:
        obj: Any
        obj = cls([["hello", "world"], [4, 2]])
        self.assertEqual(list(reversed(obj)), [("4", 2), ("hello", "world")])

    def method(self: Self, cls: type) -> None:
        self.method_fromkeys(cls)
        self.method_get(cls)
        self.method_keys(cls)
        self.method_items(cls)
        self.method_values(cls)

    def method_fromkeys(self: Self, cls: type) -> None:
        objA: Any
        objB: Any
        objC: Any
        objA = cls.fromkeys(["hello", 42])
        objB = cls([["hello", None], [42, None]])
        objC = cls(dict.fromkeys(["hello", 42]).items())
        self.assertEqual(objA, objB)
        self.assertEqual(objA, objC)
        objA = cls.fromkeys(["hello", 42], "foo")
        objB = cls([["hello", "foo"], [42, "foo"]])
        objC = cls(dict.fromkeys(["hello", 42], "foo").items())
        self.assertEqual(objA, objB)
        self.assertEqual(objA, objC)

    def method_get(self: Self, cls: type) -> None:
        obj: Any
        obj = cls([["hello", "world"], [4, 2]])
        self.assertEqual(obj.get("hello"), "world")
        self.assertEqual(obj.get("hello", "bar"), "world")
        self.assertEqual(obj.get("foo"), None)
        self.assertEqual(obj.get("foo", "bar"), "bar")

    def method_keys(self: Self, cls: type) -> None:
        obj: Any
        obj = cls([["hello", "world"], [4, 2]])
        self.assertEqual(list(obj.keys()), ["hello", "4"])

    def method_items(self: Self, cls: type) -> None:
        obj: Any
        obj = cls([["hello", "world"], [4, 2]])
        self.assertEqual(list(obj.items()), [("hello", "world"), ("4", 2)])

    def method_values(self: Self, cls: type) -> None:
        obj: Any
        obj = cls([["hello", "world"], [4, 2]])
        self.assertEqual(list(obj.values()), ["world", 2])

    def slots(self: Self, cls: type) -> None:
        obj: Any
        obj = cls([["hello", "world"], [4, 2]])
        with self.assertRaises(Exception):
            obj.foo = 42

    def stars(self: Self, cls: type) -> None:
        dict_: dict
        obj: Any
        obj = cls([["hello", "world"], [4, 2]])
        dict_ = dict(**obj)
        self.assertEqual(list(dict_.items()), [("hello", "world"), ("4", 2)])


if __name__ == "__main__":
    unittest.main()
