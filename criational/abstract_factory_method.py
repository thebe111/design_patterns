#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def create(self) -> str:
        pass


class ButtonLargeWindows(Button):
    def create(self) -> str:
        return "large button windows"


class ButtonLargeLinux(Button):
    def create(self) -> str:
        return "large button linux"


class ButtonShortWindows(Button):
    def create(self) -> str:
        return "short button windows"


class ButtonShortLinux(Button):
    def create(self) -> str:
        return "short button linux"


class ButtonCreator(ABC):
    @abstractmethod
    def createWindowsButton(self) -> Button:
        pass

    @abstractmethod
    def createLinuxButton(self) -> Button:
        pass


class LargeButtonCreator(ButtonCreator):
    def createWindowsButton(self) -> ButtonLargeWindows:
        return ButtonLargeWindows()

    def createLinuxButton(self) -> ButtonLargeLinux:
        return ButtonLargeLinux()


class ShortButtonCreator(ButtonCreator):
    def createLinuxButton(self) -> ButtonShortLinux:
        return ButtonShortLinux()

    def createWindowsButton(self) -> ButtonShortWindows:
        return ButtonShortWindows()


def largeClient(creator: ButtonCreator):
    button = creator.createWindowsButton()

    print(f"{button.create()}")


def shortClient(creator: ButtonCreator):
    button = creator.createLinuxButton()

    print(f"{button.create()}")


largeClient(LargeButtonCreator())
shortClient(ShortButtonCreator())
