#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def show(self) -> str:
        pass


class ConcreteProductOne(Product):
    def show(self) -> str:
        return "product one"


class ConcreteProductTwo(Product):
    def show(self) -> str:
        return "product two"


class ProductCreator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def show_output(self) -> str:
        product = self.factory_method()

        print(f"output: {product.show()}")


class ConcreteProductCreatorOne(ProductCreator):
    def factory_method(self) -> Product:
        return ConcreteProductOne()


class ConcreteProductCreatorTwo(ProductCreator):
    def factory_method(self) -> Product:
        return ConcreteProductTwo()


def execute(creator: ProductCreator) -> None:
    creator.show_output()


execute(ConcreteProductCreatorOne())
execute(ConcreteProductCreatorTwo())
