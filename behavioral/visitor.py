#!/usr/bin/env python3

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Component(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass

class ConcreteComponentOne(Component):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_component_one(self)

    def _create_component_one(self) -> str:
        return "[+] component ONE creation"

class ConcreteComponentTwo(Component):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_component_two(self)

    def _create_component_two(self) -> str:
        return "[+] component TWO creation"

class Visitor(ABC):
    @abstractmethod
    def visit_component_one(self, component: ConcreteComponentOne) -> None: pass

    @abstractmethod
    def visit_component_two(self, component: ConcreteComponentTwo) -> None: pass

class ConcreteVisitorOne(Visitor):
    def visit_component_one(self, component):
        print(f"{component._create_component_one()} | visitor ONE")

    def visit_component_two(self, component):
        print(f"{component._create_component_two()} | visitor ONE")

class ConcreteVisitorTwo(Visitor):
    def visit_component_one(self, component):
        print(f"{component._create_component_one()} | visitor TWO")

    def visit_component_two(self, component):
        print(f"{component._create_component_two()} | visitor TWO")

def client_code(components: List[Component], visitor: Visitor) -> None:
    for component in components:
        component.accept(visitor)

if __name__ == "__main__":
    components = [ConcreteComponentOne(), ConcreteComponentTwo()]
    visitor = ConcreteVisitorTwo()

    client_code(components, visitor)

