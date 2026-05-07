import unittest
from typing import *

from namings.core.BaseNaming import BaseNaming
from namings.core.FrozenNaming import FrozenNaming
from namings.core.Naming import Naming

__all__ = ["TestBothClasses"]


class TestBothClasses(unittest.TestCase):

    def test_eq(self: Self) -> None:
        frozenNaming: FrozenNaming
        naming: Naming
        frozenNaming = FrozenNaming([["hello", "world"], [4, 2]])
        naming = Naming([["hello", "world"], [4, 2]])
        self.assertEqual(frozenNaming, naming)
        self.assertEqual(frozenNaming, frozenNaming)
        self.assertEqual(naming, naming)

    def test_both_classes(self: Self) -> None:
        cls: type[BaseNaming]
        for cls in (FrozenNaming, Naming):
            self.dunder(cls)
            self.method(cls)
            self.slots(cls)
            self.stars(cls)

    def dunder(self: Self, cls: type[BaseNaming]) -> None:
        self.dunder_contains(cls)
        self.dunder_eq(cls)
        self.dunder_getitem(cls)
        self.dunder_iter(cls)
        self.dunder_len(cls)
        self.dunder_ne(cls)
        self.dunder_repr(cls)
        self.dunder_reversed(cls)

    def dunder_contains(self: Self, cls: type[BaseNaming]) -> None:
        obj: BaseNaming
        obj = cls([["hello", "world"], [4, 2]])
        self.assertIn(("hello", "world"), obj)
        self.assertNotIn(["hello", "world"], obj)
        self.assertIn(("4", 2), obj)
        self.assertNotIn((4, 2), obj)
        self.assertNotIn(("foo", "bar"), obj)

    def dunder_eq(self: Self, cls: type[BaseNaming]) -> None:
        objA: BaseNaming
        objB: BaseNaming
        objC: BaseNaming
        objD: BaseNaming
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

    def dunder_getitem(self: Self, cls: type[BaseNaming]) -> None:
        obj: BaseNaming
        obj = cls([["hello", "world"], [4, 2]])
        self.assertEqual(obj["hello"], "world")
        self.assertEqual(obj["4"], 2)
        with self.assertRaises(KeyError):
            obj["foo"]

    def dunder_iter(self: Self, cls: type[BaseNaming]) -> None:
        obj: BaseNaming
        obj = cls([["hello", "world"], [4, 2]])
        self.assertEqual(list(obj), [("hello", "world"), ("4", 2)])

    def dunder_len(self: Self, cls: type[BaseNaming]) -> None:
        obj: BaseNaming
        obj = cls([["hello", "world"], [4, 2]])
        self.assertEqual(len(obj), 2)

    def dunder_ne(self: Self, cls: type[BaseNaming]) -> None:
        self.assertIs(cls.__ne__, object.__ne__)

    def dunder_repr(self: Self, cls: type[BaseNaming]) -> None:
        answer: str
        dict_: dict
        obj: BaseNaming
        solution: str
        dict_ = {"hello": "world", "4": 2}
        obj = cls([["hello", "world"], [4, 2]])
        answer = repr(obj)
        solution = cls.__name__ + "(" + repr(dict_) + ")"
        self.assertEqual(answer, solution)

    def dunder_reversed(self: Self, cls: type[BaseNaming]) -> None:
        obj: BaseNaming
        obj = cls([["hello", "world"], [4, 2]])
        self.assertEqual(list(reversed(obj)), [("4", 2), ("hello", "world")])

    def method(self: Self, cls: type[BaseNaming]) -> None:
        self.method_get(cls)
        self.method_keys(cls)
        self.method_items(cls)
        self.method_values(cls)

    def method_get(self: Self, cls: type[BaseNaming]) -> None:
        obj: BaseNaming
        obj = cls([["hello", "world"], [4, 2]])
        self.assertEqual(obj.get("hello"), "world")
        self.assertEqual(obj.get("hello", "bar"), "world")
        self.assertEqual(obj.get("foo"), None)
        self.assertEqual(obj.get("foo", "bar"), "bar")

    def method_keys(self: Self, cls: type[BaseNaming]) -> None:
        obj: BaseNaming
        obj = cls([["hello", "world"], [4, 2]])
        self.assertEqual(list(obj.keys()), ["hello", "4"])

    def method_items(self: Self, cls: type[BaseNaming]) -> None:
        obj: BaseNaming
        obj = cls([["hello", "world"], [4, 2]])
        self.assertEqual(list(obj.items()), [("hello", "world"), ("4", 2)])

    def method_values(self: Self, cls: type[BaseNaming]) -> None:
        obj: BaseNaming
        obj = cls([["hello", "world"], [4, 2]])
        self.assertEqual(list(obj.values()), ["world", 2])

    def slots(self: Self, cls: type[BaseNaming]) -> None:
        obj: BaseNaming
        obj = cls([["hello", "world"], [4, 2]])
        with self.assertRaises(Exception):
            obj.foo = 42

    def stars(self: Self, cls: type[BaseNaming]) -> None:
        dict_: dict
        obj: BaseNaming
        obj = cls([["hello", "world"], [4, 2]])
        dict_ = dict(**obj)
        self.assertEqual(list(dict_.items()), [("hello", "world"), ("4", 2)])


if __name__ == "__main__":
    unittest.main()
