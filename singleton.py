#!/usr/bin/env python3


class SingletonMeta(type):
    _instances = {}

    def __call__(check, *args, **kwargs):
        if check not in check._instances:
            instance = super().__call__(*args, **kwargs)
            check._instances[check] = instance

        return check._instances[check]


class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        print("...")

    def hello_world(self):
        print("hello world")


def execute():
    instance_one = Singleton()
    instance_two = Singleton()

    instance_one.hello_world()

    if id(instance_one) == id(instance_two):
        print("same instance")
    else:
        print("error :/")


if __name__ == "__main__":
    execute()
