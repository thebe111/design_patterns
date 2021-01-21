#!/usr/bin/env python3

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def run(self) -> str:
        pass


class Leaf(Component):
    def __init__(self, name: str) -> None:
        self._name = name

    def run(self) -> str:
        return f"i'm {self._name}"


class Composite(Component):
    def __init__(self) -> None:
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def run(self) -> str:
        results = []

        for child in self._children:
            results.append(child.run())

        return f"( {' + '.join(results)} )"


def client_code_one(component: Component) -> None:
    print(component.run(), end="\n\n")
    print("*" * 20, end="\n\n")


def client_code_two(first: Component, second: Component) -> None:
    if first.is_composite():
        first.add(second)

    print(first.run(), end="\n")


if __name__ == "__main__":
    simple_node = Leaf("homer")

    client_code_one(simple_node)

    tree = Composite()

    branch_one = Composite()
    branch_one.add(Leaf("bart"))
    branch_one.add(Leaf("lisa"))

    branch_two = Composite()
    branch_two.add(Leaf("meggie"))
    branch_two.add(Leaf("marge"))

    tree.add(branch_one)
    tree.add(branch_two)

    client_code_one(tree)

    client_code_two(tree, simple_node)
