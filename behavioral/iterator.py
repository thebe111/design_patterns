#!/usr/bin/env python3

from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List

class AlphabeticalOrderIterator(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value

class WordsCollection(Iterable):
    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection)

    def reverse(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, True)

    def add(self, item: Any):
        self._collection.append(item)

if __name__ == "__main__":
    collection = WordsCollection()
    collection.add("Bart")
    collection.add("Homer")
    collection.add("Lisa")

    print("\n".join(collection))
    print("-" * 20, end="\n")
    print("\n".join(collection.reverse()))

