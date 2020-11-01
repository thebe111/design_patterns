#!/usr/bin/env python3
from abc import ABC, abstractmethod, abstractproperty
from typing import Any


class Builder(ABC):
    @abstractproperty
    def product(self) -> None:
        pass

    @abstractmethod
    def add_base(self) -> None:
        pass

    @abstractmethod
    def add_tomato(self) -> None:
        pass

    @abstractmethod
    def add_hamburguer(self) -> None:
        pass

    @abstractmethod
    def add_chicken(self) -> None:
        pass

    @abstractmethod
    def add_egg(self) -> None:
        pass

    @abstractmethod
    def add_lettuce(self) -> None:
        pass

    @abstractmethod
    def add_ketchup(self) -> None:
        pass

    @abstractmethod
    def add_mustard(self) -> None:
        pass

    @abstractmethod
    def add_top(self) -> None:
        pass


class Burguer:
    def __init__(self) -> None:
        self.parts = []

    def add(self, item: Any) -> None:
        self.parts.append(item)

    def show_format(self) -> None:
        for item in self.parts:
            print(item)


class ConcreteBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Burguer()

    @property
    def product(self) -> Burguer:
        product = self._product

        self.reset()

        return product

    def add_base(self) -> None:
        self._product.add("base")

    def add_tomato(self) -> None:
        self._product.add("tomato")

    def add_hamburguer(self) -> None:
        self._product.add("hamburguer")

    def add_chicken(self) -> None:
        self._product.add("chicken")

    def add_egg(self) -> None:
        self._product.add("egg")

    def add_lettuce(self) -> None:
        self._product.add("lettuce")

    def add_ketchup(self) -> None:
        self._product.add("ketchup")

    def add_mustard(self) -> None:
        self._product.add("mustard")

    def add_top(self) -> None:
        self._product.add("top")


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_standard_model(self) -> None:
        self.builder.add_top()
        self.builder.add_hamburguer()
        self.builder.add_base()


if __name__ == "__main__":
    director = Director()
    builder = ConcreteBuilder()
    director.builder = builder

    print("=== standard burguer ===\n")
    director.build_standard_model()
    builder.product.show_format()
    print()

    builder.reset()
    director.builder = builder

    print("=== custom burguer ===\n")
    builder.add_top()
    builder.add_tomato()
    builder.add_lettuce()
    builder.add_ketchup()
    builder.add_hamburguer()
    builder.add_base()
    builder.product.show_format()
    print()
