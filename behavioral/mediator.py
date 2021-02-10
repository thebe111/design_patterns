#!/usr/bin/env python3

from __future__ import annotations
from abc import ABC

class Mediator(ABC):
    def notify(self, sender: object, event: str) -> None:
        pass

class ConcreteMediator(Mediator):
    def __init__(self, component_one: ComponentOne, component_two: ComponentTwo) -> None:
        self._component_one = component_one
        self._component_one.mediator = self
        self._component_two = component_two
        self._component_two.mediator = self

    def notify(self, sender: object, event: str) -> None:
        if event == "A":
            print("-" * 20)
            self._component_two.run()
            print("-" * 20)
        elif event == "D":
            print("-" * 20)
            self._component_one.exec()
            self._component_two.run()
            print("-" * 20)

class BaseComponent():
    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator

class ComponentOne(BaseComponent):
    def run(self) -> None:
        print("[+] component_one A")
        self.mediator.notify(self, "A")

    def exec(self) -> None:
        print("[+] component_one B")
        self.mediator.notify(self, "B")

class ComponentTwo(BaseComponent):
    def run(self) -> None:
        print("[+] component_two C")
        self.mediator.notify(self, "C")

    def exec(self) -> None:
        print("[+] component_two D")
        self.mediator.notify(self, "D")

if __name__ == "__main__":
    component_one = ComponentOne()
    component_two = ComponentTwo()
    mediator = ConcreteMediator(component_one, component_two)

    component_one.run()
    component_two.exec()

