"""
Behavioral Pattern: State

Allows an object to alter its behavior when its internal state changes.
The object will appear to change its class.
"""

from __future__ import annotations
from abc import ABC, abstractmethod

class Context:
    """Maintains a reference to the current state and delegates behavior to it."""

    def __init__(self, state: State) -> None:
        self._state = state
        self._state.set_context(self)

    def transition_to(self, state: State) -> None:
        print(f"Context: Transitioning to {state.__class__.__name__}")
        self._state = state
        self._state.set_context(self)

    def request(self) -> None:
        self._state.handle()

class State(ABC):
    """Abstract State interface."""

    def set_context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def handle(self) -> None:
        pass

class ConcreteStateA(State):
    def handle(self) -> None:
        print("State A: Handling and switching to B.")
        self._context.transition_to(ConcreteStateB())

class ConcreteStateB(State):
    def handle(self) -> None:
        print("State B: Handling and switching to A.")
        self._context.transition_to(ConcreteStateA())

# Example usage
if __name__ == "__main__":
    context = Context(ConcreteStateA())
    context.request()
    context.request()
    context.request()
