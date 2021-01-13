#!/usr/bin/env python3

from abc import ABC, abstractmethod


# class Implementation(ABC):
#     @abstractmethod
#     def show_text(self) -> str:
#         pass


# class Abstraction:
#     def __init__(self, implementation: Implementation) -> None:
#         self.implementation = implementation

#     def show(self) -> str:
#         return f"Abstraction: Base operation with: \n {self.implementation.show_text()}"  # noqa: E501


# class ExtendedAbstraction(Abstraction):
#     def show(self) -> str:
#         return f"ExtendedAbstraction: Extended operation with: \n {self.implementation.show_text()}"  # noqa: E501


# class HelloWorld(Implementation):
#     def show_text(self) -> str:
#         return "Hello World"


# class LoremIpsum(Implementation):
#     def show_text(self) -> str:
#         return "Lorem Ipsum"


# def client_code(abstraction: Abstraction) -> None:
#     print(abstraction.show(), end="\n")


# if __name__ == "__main__":
#     implementation = HelloWorld()
#     abstraction = Abstraction(implementation)
#     client_code(abstraction)

#     print("-" * 20)

#     implementation = LoremIpsum()
#     abstraction = ExtendedAbstraction(implementation)
#     client_code(abstraction)


# -------


class GeometricFormulaImplementation(ABC):
    @abstractmethod
    def iam(self) -> str:
        pass


class ColorImplementation(ABC):
    @abstractmethod
    def iam(self) -> str:
        pass


class Square(GeometricFormulaImplementation):
    def iam(self) -> str:
        return "i'm square"


class Circle(GeometricFormulaImplementation):
    def iam(self) -> str:
        return "i'm circle"


class Red(ColorImplementation):
    def iam(self) -> str:
        return "and i'm red"


class Blue(ColorImplementation):
    def iam(self) -> str:
        return "and i'm blue"


class Abstraction:
    def __init__(
        self,
        formula: GeometricFormulaImplementation,
        color: ColorImplementation,
    ) -> None:
        self.formula = formula
        self.color = color

    def describe(self) -> None:
        print(f"{self.formula.iam()} {self.color.iam()}")


def client_code(abstraction: Abstraction):
    return abstraction.describe()


if __name__ == "__main__":
    formulaImplementation = Circle()
    colorImplementation = Blue()

    abstraction = Abstraction(formulaImplementation, colorImplementation)

    client_code(abstraction)
