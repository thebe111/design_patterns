#!/usr/bin/env python3

import copy


class Reference:
    def __init__(self):
        self.reference = None

    def set_reference(self, reference):
        self.reference = reference


class Person:
    def __init__(self, name: str, age: int, prototype: Reference):
        self._name = name
        self._age = age
        self.prototype = prototype

    def set_name(self, name):
        self._name = name

    def get_name(self):
        print(self._name)

    def set_age(self, age):
        self._age = age

    def get_age(self):
        print(self._age)

    """
    make a pointer to memory space
    """

    def __copy__(self):
        name = copy.copy(self._name)
        age = copy.copy(self._age)
        prototype = copy.copy(self.prototype)

        clone = self.__class__(name, age, prototype)
        clone.__dict__.update(self.__dict__)

        return clone

    """
    make a copy in a new memory space
    """

    def __deepcopy__(self, memo={}):
        name = copy.deepcopy(self._name, memo)
        age = copy.deepcopy(self._age, memo)
        prototype = copy.deepcopy(self.prototype, memo)

        clone = self.__class__(name, age, prototype)
        clone.__dict__ = copy.deepcopy(self.__dict__, memo)

        return clone


if __name__ == "__main__":
    base = Reference()
    person = Person("bart", 20, base)

    print(f"person prototype == base: {person.prototype.__dict__}")

    clone = copy.deepcopy(person)
    clone.prototype.set_reference(person)

    # clone.set_name("lisa")

    # person.get_name()
    # clone.get_name()

    # clone.prototype.reference.get_name()

    print(
        f"person prototype == base: {person.prototype.__dict__} only on deep copy"
    )
    print(
        f"clone prototype == person: {clone.prototype.__dict__} only on deep copy"
    )
