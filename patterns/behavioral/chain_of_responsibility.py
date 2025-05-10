"""
Behavioral Pattern: Chain of Responsibility

Lets you pass requests along a chain of handlers, where each handler decides
whether to process the request or pass it along.
Promotes loose coupling between sender and receiver.

Class Diagram:

    +------------------+
    |    Handler (ABC) |
    +------------------+
    | - _next_handler  |
    +------------------+
    | + set_next()     |
    | + handle()       |
    | + pass_to_next() |
    +------------------+
              ^
              |
    +-------------------+       +-------------------+      +----------------+
    |  MonkeyHandler    |       | SquirrelHandler   |      |   DogHandler   |
    +-------------------+       +-------------------+      +----------------+
    | + handle()        |       | + handle()        |      | + handle()     |
    +-------------------+       +-------------------+      +----------------+

Runtime Chain Flow:

    Client
      |
      v
    MonkeyHandler --> SquirrelHandler --> CatHandler --> DogHandler --> None
                                           |
                                   [Request: "Fish"]
                                           |
                                           v
                               CatHandler handles it!
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional
import unittest


class Handler(ABC):
    """
    The base Handler class declares the interface for handling requests and for
    setting the next handler in the chain.
    """

    _next_handler: Optional[Handler] = None

    def set_next(self, handler: Handler) -> Handler:
        """
        Set the next handler in the chain and return the handler to allow chaining.
        """
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: str) -> Optional[str]:
        """
        Handle the request or pass it to the next handler in the chain.
        """
        pass

    def pass_to_next(self, request: str) -> Optional[str]:
        """
        Utility method to pass request to the next handler, if any.
        """
        if self._next_handler:
            print(f"{self.__class__.__name__}: Can't handle {request}, passing to next...")
            return self._next_handler.handle(request)
        print(f"{self.__class__.__name__}: No next handler for {request}.")
        return None


class MonkeyHandler(Handler):
    """Handler that processes requests related to Bananas."""

    def handle(self, request: str) -> Optional[str]:
        if request == "Banana":
            return "Monkey: I'll eat the Banana."
        return self.pass_to_next(request)


class SquirrelHandler(Handler):
    """Handler that processes requests related to Nuts."""

    def handle(self, request: str) -> Optional[str]:
        if request == "Nut":
            return "Squirrel: I'll eat the Nut."
        return self.pass_to_next(request)


class DogHandler(Handler):
    """Handler that processes requests related to Meat."""

    def handle(self, request: str) -> Optional[str]:
        if request == "Meat":
            return "Dog: I'll eat the Meat."
        return self.pass_to_next(request)


class CatHandler(Handler):
    """Handler that processes requests related to Fish."""

    def handle(self, request: str) -> Optional[str]:
        if request == "Fish":
            return "Cat: I'll eat the Fish."
        return self.pass_to_next(request)


# Unit Tests
class TestChainOfResponsibility(unittest.TestCase):
    """Test cases for the Chain of Responsibility pattern."""
    def setUp(self):
        self.monkey = MonkeyHandler()
        self.squirrel = SquirrelHandler()
        self.cat = CatHandler()
        self.dog = DogHandler()
        self.monkey.set_next(self.squirrel).set_next(self.cat).set_next(self.dog)

    def test_monkey_handler(self):
        """Test that the MonkeyHandler handles a request."""
        self.assertEqual(self.monkey.handle("Banana"), "Monkey: I'll eat the Banana.")

    def test_squirrel_handler(self):
        """Test that the SquirrelHandler handles a request."""
        self.assertEqual(self.monkey.handle("Nut"), "Squirrel: I'll eat the Nut.")

    def test_cat_handler(self):
        """Test that the CatHandler handles a request."""
        self.assertEqual(self.monkey.handle("Fish"), "Cat: I'll eat the Fish.")

    def test_dog_handler(self):
        """Test that the DogHandler handles a request."""
        self.assertEqual(self.monkey.handle("Meat"), "Dog: I'll eat the Meat.")

    def test_unhandled_request(self):
        """Test that an unhandled request is passed to the next handler."""
        self.assertIsNone(self.monkey.handle("Apple"))

# Example usage
if __name__ == "__main__":
    # Create handlers
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()
    cat = CatHandler()

    # Dynamically construct chain
    monkey.set_next(squirrel).set_next(cat).set_next(dog)

    # Test inputs
    for food in ["Nut", "Banana", "Meat", "Fish", "Apple"]:
        print(f"\nClient: Who wants a {food}?")
        result = monkey.handle(food)
        if result:
            print(result)
        else:
            print(f"No one wants the {food}.")

    # Unit Tests
    unittest.main()
