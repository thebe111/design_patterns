#!/usr/bin/env python3

import json
from typing import Dict

class Flyweight():
    def __init__(self, shared_state: str) -> None:
        self._shared_state = shared_state

    def exec(self, unique_state: str) -> None:
        shared = json.dumps(self._shared_state)
        unique = json.dumps(unique_state)

        print(f"flyweight: \n shared: {shared} \n unique: {unique}", end="\n")

class FlyweightFactory():
    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: Dict) -> None:
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state: Dict) -> str:
        return " | ".join(sorted(state))


    def get_fly(self, shared_state: Dict) -> Flyweight:
        key = self.get_key(shared_state)

        if not self._flyweights.get(key):
            print("[+] creating a new flyweight", end="\n")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("[+] reusing existing flyweight", end="\n")

        return self._flyweights[key]

    def list_fly(self) -> None:
        quant = len(self._flyweights)

        print(f"quantity = {quant}", end="\n")
        print("\n".join(map(str, self._flyweights.keys())))

def add_db_car(factory: FlyweightFactory, plates: str, owner: str, brand: str, model: str, color: str) -> None:
    print("[+] adding car to db", end="\n")

    flyweight = factory.get_fly([brand, model, color])
    flyweight.exec([plates, owner])

if __name__ == "__main__":
    obj = FlyweightFactory([
        ["hello world", "ABC", "red"],
        ["lorem ipsum", "DEF", "green"],
        ["testing", "GHI", "blue"]
    ])

    obj.list_fly()

    items = ["plate", "owner", "brand", "model", "color"]
    out = {}

    for item in items:
        out[item] = input(f"{item}: ")

    add_db_car(
        obj, out["plate"], out["owner"], out["brand"], out["model"], out["color"]
    )

    obj.list_fly()
