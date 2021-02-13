#!/usr/bin/env python3

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Context():
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def exec(self) -> None:
        result = self._strategy.run(['a', 'b', 'c', 'd', 'e'])
        print(f"{type(self._strategy).__name__}: " +  ', '.join(result))

class Strategy(ABC):
    @abstractmethod
    def run(self, data: List) -> List:
        pass

class Sorted(Strategy):
    def run(self, data: List) -> List:
        return sorted(data)

class ReversedSorted(Strategy):
    def run(self, data: List) -> List:
        return reversed(sorted(data))

if __name__ == "__main__":
    ctx = Context(Sorted())
    ctx.exec()

    ctx.strategy = ReversedSorted()
    ctx.exec()
