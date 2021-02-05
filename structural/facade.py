#!/usr/bin/env python3

class SubsystemOne:
    def run(self) -> str:
        return "complex method ss1"

class SubsystemTwo:
    def run(self) -> str:
        return "complex method ss2"

class Facade:
    def __init__(self, subsystem_one: SubsystemOne, subsystem_two: SubsystemTwo) -> None:
        self._subsystem_one = subsystem_one or SubsystemOne()
        self._subsystem_two = subsystem_two or SubsystemTwo()

    def operation(self) -> str:
        proccess = []
        proccess.append(self._subsystem_one.run())
        proccess.append(self._subsystem_two.run())
        
        return "\n".join(proccess)

def client_code(facade: Facade) -> None:
    print(facade.operation(), end="\n")

if __name__ == "__main__":
    bart = SubsystemOne()
    lisa = SubsystemTwo()
    facade = Facade(bart, lisa)
    client_code(facade)
