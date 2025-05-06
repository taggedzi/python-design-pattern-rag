"""
Behavioral Pattern: Observer

Defines a one-to-many dependency so that when one object changes state,
all its dependents are notified and updated automatically.
Common in event-driven systems.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        pass

# Subject (Observable)
class Subject:
    def __init__(self) -> None:
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        print("Subject: Detached an observer.")
        self._observers.remove(observer)

    def notify(self, message: str) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(message)

# Concrete Observer
class ConcreteObserver(Observer):
    def __init__(self, name: str) -> None:
        self._name = name

    def update(self, message: str) -> None:
        print(f"{self._name} received update: {message}")

# Example usage
if __name__ == "__main__":
    subject = Subject()

    observer1 = ConcreteObserver("Observer1")
    observer2 = ConcreteObserver("Observer2")

    subject.attach(observer1)
    subject.attach(observer2)

    subject.notify("State has changed!")

    subject.detach(observer1)
    subject.notify("Another change occurred.")
