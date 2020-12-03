#!/usr/bin/python3


class Target:
    def normal(self) -> str:
        return "default behavior"


class Adaptee:
    def reverse(self) -> str:
        return "muspi merol"


class Adapter(Target, Adaptee):
    def normal(self) -> str:
        return self.reverse()[::-1]


def client_code(target: Target) -> None:
    print(target.normal(), end="\n")


if __name__ == "__main__":
    target = Target()
    client_code(target)

    adaptee = Adaptee()
    print(adaptee.reverse())

    adapter = Adapter()
    client_code(adapter)
