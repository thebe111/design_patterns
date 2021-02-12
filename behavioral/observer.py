#!/usr/bin/env python3

from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

class Message(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass

class ConcreteMessage(Message):
    _state: int = None
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("[+] notifying observers")
        for observer in self._observers:
            observer.update(self)

    def action(self) -> None:
        print("[+] action")
        self._state = randrange(0, 10)

        print(f"[+] STATE: {self._state}")
        self.notify()

class Observer(ABC):
    @abstractmethod
    def update(self, message: Message) -> None:
        pass

class ConcreteObserverOne(Observer):
    def update(self, message: Message) -> None:
        if message._state < 3:
            print("[1] observer one action")

class ConcreteObserverTwo(Observer):
    def update(self, message: Message) -> None:
        if message._state == 0 or message._state >= 2:
            print("[2] observer two action")

if __name__ == "__main__":
    message = ConcreteMessage()

    observer_one = ConcreteObserverOne()
    message.attach(observer_one)

    observer_two = ConcreteObserverTwo()
    message.attach(observer_two)

    for _ in range(2):
        message.action()

    message.detach(observer_one)

    message.action()
