#!/usr/bin/env python3

from __future__ import annotations
from abc import ABC, abstractmethod

class Context():
    _state = None

    def __init__(self, state: State) -> None:
        self.transition(state)

    def transition(self, state: State) -> None:
        print(f"[+] transition: {type(state).__name__}")
        self._state = state
        self._state.context = self

    def request_one(self):
        self._state.handle_one()

    def request_two(self):
        self._state.handle_two()

class State(ABC):
    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def handle_one(self) -> None:
        pass

    @abstractmethod
    def handle_two(self) -> None:
        pass

class ConcreteStateOne(State):
    def handle_one(self) -> None:
        print("[+] state ONE request ONE")
        self.context.transition(ConcreteStateTwo())

    def handle_two(self) -> None:
        print("state ONE request TWO")

class ConcreteStateTwo(State):
    def handle_one(self) -> None:
        print("state TWO request ONE")

    def handle_two(self) -> None:
        print("[+] state TWO request TWO")
        self.context.transition(ConcreteStateOne())

if __name__ == "__main__":
    context = Context(ConcreteStateOne())
    context.request_one()
    context.request_two()
    context.request_two()
