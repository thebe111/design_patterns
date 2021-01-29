#!/usr/bin/env python3

from abc import ABC

class IComponent(ABC):
    def operation(self) -> str:
        pass

class Component(IComponent):
    def operation(self) -> str:
        return "concrete component"

class Decorator(Component):
    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        return self._component

    def operation(self) -> str:
        return self._component.operation()

class ConcreteDecoratorOne(Decorator):
    def operation(self) -> str:
        return f"concrete decorator one: {self.component.operation()}"

class ConcreteDecoratorTwo(Decorator):
    def operation(self) -> str:
        return f"concrete decorator two: {self.component.operation()}"

def client_code(component: Component) -> None:
    print(f"EXEC: {component.operation()}", end="\n")

if __name__ == "__main__":
    homer = Component()
    
    client_code(homer)

    print("*" * 20)

    bart = ConcreteDecoratorOne(homer)
    lisa = ConcreteDecoratorTwo(bart)

    client_code(lisa)
