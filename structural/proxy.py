#!/usr/bin/env python3

from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def request(self) -> None:
        pass

class RealSubject(Subject):
    def request(self) -> None:
        print("real subject")

class Proxy(Subject):
    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: check real req")
        return True

    def log_access(self) -> None:
        print("Proxy: log the time of req")

def client_code(subject: Subject) -> None:
    subject.request()

if __name__ == "__main__":
    print("[+] without proxy")
    real_subject = RealSubject()
    client_code(real_subject)

    print("*" * 20, end="\n")

    print("[+] with proxy")
    proxy = Proxy(real_subject)
    client_code(proxy)
