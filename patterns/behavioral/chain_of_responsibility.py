"""
Behavioral Pattern: Chain of Responsibility

Lets you pass requests along a chain of handlers, where each handler decides
whether to process the request or pass it along.
Promotes loose coupling between sender and receiver.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional

class Handler(ABC):
    """Base Handler class with chaining support."""

    _next_handler: Optional[Handler] = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: str) -> Optional[str]:
        pass

class MonkeyHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        if request == "Banana":
            return "Monkey: I'll eat the Banana."
        elif self._next_handler:
            return self._next_handler.handle(request)
        return None

class SquirrelHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        if request == "Nut":
            return "Squirrel: I'll eat the Nut."
        elif self._next_handler:
            return self._next_handler.handle(request)
        return None

class DogHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        if request == "Meat":
            return "Dog: I'll eat the Meat."
        elif self._next_handler:
            return self._next_handler.handle(request)
        return None

# Example usage
if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(squirrel).set_next(dog)

    for food in ["Nut", "Banana", "Meat", "Apple"]:
        print(f"Client: Who wants a {food}?")
        result = monkey.handle(food)
        if result:
            print(result)
        else:
            print(f"No one wants the {food}.")