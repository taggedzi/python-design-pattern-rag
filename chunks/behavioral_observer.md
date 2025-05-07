---
file: behavioral/observer.py
chunk: behavioral_observer.md
---

```python
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

```

## Summary
This code implements the Observer design pattern using Python. It defines an interface for observing state changes, a subject that maintains a list of observers and notifies them of state changes, and concrete observers that implement the update method to react to notifications.

## Docstrings
- Defines a one-to-many dependency so that when one object changes state, all its dependents are notified and updated automatically. Common in event-driven systems.
- Abstract base class representing an observer. Must implement the update method.
- Class representing the subject (observable). Maintains a list of observers and notifies them of state changes.
- Method to attach an observer to the subject.
- Method to detach an observer from the subject.
- Method to notify all observers about a state change.
- Concrete observer class. Overrides the update method to react to notifications with a specific name.
- Entry point for the example usage, demonstrating how to use the Observer pattern.
- Creates a subject instance.

