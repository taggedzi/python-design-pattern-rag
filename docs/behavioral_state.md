# The State Pattern (Behavioral)

## Intent

The State pattern allows an object to alter its behavior when its internal state changes. This is particularly useful for managing complex states within an application, where each state could have a different set of behaviors associated with it.

## Problem It Solves

In software development, we often encounter objects that behave differently based on their current state. For example, a UI button might change color or label when its state changes (pressed vs unpressed). This pattern helps to encapsulate these variations and makes the code more readable and maintainable by separating each possible state into its own class.

## When to Use It

The State pattern is best used in situations where an object's behavior depends on its current state, and you want to separate the different states into their own classes. This can make your code easier to understand and modify as it grows over time.

## When NOT to Use It

While the State pattern provides a powerful way to manage complex state transitions, it should not be used if:

1. The object's behavior doesn't change based on its current state (in which case, other design patterns like Strategy might be more appropriate).
2. There are only a few distinct states that need encapsulation (in which case, using an enum or a switch-case statement might be simpler).

## How It Works

The State pattern involves three key components:

1. **Context** - This is the object whose behavior changes based on its state. It maintains a reference to one of several possible states and delegates requests for behavior to that state object.
2. **State abstract class** - This provides an interface for all concrete state classes, including methods for setting the context (which is common to all states) and defining the interface for handling requests from the context.
3. **Concrete State classes** - These are each of the different possible states that the Context can be in. Each one implements the handle() method to define what happens when a request is made by the Context.

## Real-World Analogy

Imagine you're at a restaurant and your table has a waiter who serves you food based on your order (the current state). If you order a burger, the waiter might serve you a hamburger (state A); if you order a salad, the waiter might serve you a fresh garden salad (state B), etc. Each of these states could have different behaviors associated with them.

## Simplified Example

Here's a simplified example:

```python
class Context:
    def __init__(self, state):
        self._state = state
        self._state.set_context(self)

    def transition_to(self, state):
        print("Context: Transitioning to", type(state).__name__)
        self._state = state
        self._state.set_context(self)

    def request(self):
        self._state.handle()

class State:
    def set_context(self, context):
        self._context = context

    def handle(self):
        pass

class ConcreteStateA(State):
    def handle(self):
        print("ConcreteStateA handles request")
        self._context.transition_to(ConcreteStateB())

class ConcreteStateB(State):
    def handle(self):
        print("ConcreteStateB handles request")
        self._context.transition_to(ConcreteStateA())
```

In this example, `Context` maintains a reference to the current state and delegates behavior to it. The states are represented by `ConcreteStateA` and `ConcreteStateB` classes, each implementing the `handle()` method to define what happens when a request is made by the Context.

## See Also

You can find this Python code for this pattern [here](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/behavioral/state.py).
