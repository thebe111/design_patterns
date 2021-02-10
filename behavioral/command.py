#!/usr/bin/env python3

from __future__ import annotations
from abc import ABC, abstractmethod

class CMD(ABC):
    @abstractmethod
    def exec(self) -> None:
        pass

class SimpleCMD(CMD):
    def __init__(self, payload: str) -> None:
        self._payload = payload

    def exec(self) -> None:
        print(f"SIMPLE: {self._payload}", end="\n\n")

class ComplexCMD(CMD):
    def __init__(self, act: Action, x: str, y: str) -> None:
        self._act = act
        self._x = x
        self._y = y

    def exec(self) -> None:
        print(f"COMPLEX: ", end="\n")
        self._act.exec(self._x)
        self._act.log(self._y)

# ---

class Undo():
    def exec(self, identifier: str) -> None:
        print(f"undo: {identifier}")

    def log(self, msg: str) -> None:
        print(f"msg: {msg}")

class Action():
    _exec = None
    _undo = None

    def exec(self, cmd: CMD):
        self._exec = cmd

    def undo(self, cmd: CMD):
        self._undo = cmd

    def run(self) -> None:
        if isinstance(self._exec, CMD):
            self._exec.exec()

        if isinstance(self._undo, CMD):
            self._undo.exec()

if __name__ == "__main__":
    act = Action()
    act.exec(SimpleCMD("Hello World"))
    undo = Undo()
    act.undo(ComplexCMD(undo, "Hello World", "[+] saving log"))
    act.run()
