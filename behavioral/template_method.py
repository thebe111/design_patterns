#!/usr/bin/env python3

from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def template_method(self) -> None:
       self.exec1()
       self.run1()
       self.exec2()
       self.hook1()
       self.run2()
       self.exec3()
       self.hook2()

    def exec1(self) -> None:
        print("[1] execution")

    def exec2(self) -> None:
        print("[2] execution")

    def exec3(self) -> None:
        print("[3] execution")

    @abstractmethod
    def run1(self) -> None:
        pass

    @abstractmethod
    def run2(self) -> None:
        pass

    def hook1(self) -> None:
        pass

    def hook2(self) -> None:
        print("hook TWO unchanged")

class ConcreteClassOne(AbstractClass):
    def run1(self) -> None:
        print("[1] RUN class ONE")

    def run2(self) -> None:
        print("[2] RUN class ONE")

class ConcreteClassTwo(AbstractClass):
    def run1(self) -> None:
        print("[1] RUN class TWO")

    def run2(self) -> None:
        print("[2] RUN class TWO")

    def hook1(self) -> None:
        print("[+] hook ONE")

def client_code(abstract_class: AbstractClass) -> None:
    abstract_class.template_method()

if __name__ == "__main__":
    client_code(ConcreteClassOne())

    client_code(ConcreteClassTwo())
