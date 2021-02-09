#!/usr/bin/env python3

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

class Handler(ABC):
    @abstractmethod
    def next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass

class AbstractHandler(Handler):
    _next_handler: Handler = None

    def next(self, handler: Handler) -> Handler:
        self._next_handler = handler

        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None

class OneHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        print("LOG: 1")
        if request == "one":
            return f"[+] handler one called"
        else:
            return super().handle(request)

class TwoHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        print("LOG: 2")
        if request == "two":
            return f"[+] handler two called"
        else:
            return super().handle(request)

class ThreeHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        print("LOG: 3")
        if request == "three":
            return f"[+] handler three called"
        else:
            return super().handle(request)

def client_code(handler: Handler) -> None:
    for item in ["two", "one", "three", "test"]:
        response = handler.handle(item)

        print(response) if response else print("404")


if __name__ == "__main__":
    one = OneHandler()
    two = TwoHandler()
    three = ThreeHandler()

    one.next(three).next(two)

    client_code(one)
