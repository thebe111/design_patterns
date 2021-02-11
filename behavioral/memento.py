#!/usr/bin/env python3

from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters, digits

class Originator():
    _state = None

    def __init__(self, state: str) -> None:
        self._state = state
        print(f"original state: {self._state}")

    def update(self) -> None:
        print("[+] changing")
        self._state = self._generate_random_string(30)
        print(f"actual state {self._state}")

    def _generate_random_string(self, length: int = 10) -> None:
        return "".join(sample(ascii_letters, length))

    def save(self) -> Memento:
        return ConcreteMemento(self._state)

    def restore(self, memento: Memento) -> None:
        self._state = memento.get_state()
        print(f"actual state {self._state}")

class Memento(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass

class ConcreteMemento(Memento):
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> str:
        return self._state

    def get_name(self) -> str:
        return f"{self._date} / ({self._state[0:9]}...)"

    def get_date(self) -> str:
        return self._date

class Caretaker():
    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator

    def backup(self) -> None:
        print("[+] saving originator state")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"[+] restoring state {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def history(self) -> None:
        print("[+] list of mementos")
        for memento in self._mementos:
            print(memento.get_name())

if __name__ == "__main__":
    originator = Originator("Lorem Ipsum")
    caretaker = Caretaker(originator)

    for _ in range(3):
        caretaker.backup()
        originator.update()

    caretaker.history()
    caretaker.undo()
    caretaker.undo()

