# The State Pattern (Behavioral)

## Intent

The State design pattern allows an object to alter its behavior when its internal state changes. It appears that the object is changing its class at runtime, which can be very useful in certain scenarios.

## Problem It Solves

This pattern addresses the problem of having objects change their behavior based on changes in their internal states. This is particularly useful for complex systems where different behaviors are required depending on the current state.

## When to Use It

The State pattern should be used when:
1. An object's behavior depends on its state, and it must be decoupled from that state.
2. A class can be expected to have many states, each represented by a subclass.
3. Operations have large, multipart conditional statements that establish which operations are selected based on the current state of an object.

## When NOT to Use It

The State pattern should not be used when:
1. The number of different states is small and fixed. In such cases, using a simple if-else or switch-case statement might be more straightforward.
2. If the operations are very complex and cannot be encapsulated into separate classes.
3. If the state transitions between objects are not numerous and predictable.

## How It Works

The State pattern involves an abstract base class (State) that declares a method for handling requests, along with subclasses representing different states of the context object. The Context class maintains a reference to one of these states and delegates all requests to it. When the state changes, the Context updates its reference and all further operations are handled by the new state.

## Real-World Analogy

Imagine you're at a restaurant where you can order food items. The waiter (Context) serves your meal based on what item you ordered but also depends on how much time has passed since you placed your order (state). If it's been a while, the waiter might start preparing another dish instead of serving your current one.

## Simplified Example

Here is a simplified pseudocode representation of the above code:

```python
class Context:  # The Waiter
    def __init__(self, state):
        self._state = state
        self._state.set_context(self)

    def transition_to(self, state):
        print("Waiter: Transitioning to", state.__class__.__name__)
        self._state = state
        self._state.set_context(self)

    def request():
        self._state.handle()  # Waiter serves based on the order (state)

class State:  # The Order Interface
    def set_context(self, context):
        self._context = context

    def handle():
        pass

class ConcreteStateA(State):  # A specific order (Meal)
    def handle(self):
        print("Waiter: Serving Meal A")
        self._context.transition_to(ConcreteStateB())

class ConcreteStateB(State):  # Another specific order (Dessert)
    def handle(self):
        print("Waiter: Serving Dessert B")
        self._context.transition_to(ConcreteStateA())

# Example usage
if __name__ == "__main__":
    context = Context(ConcreteStateA())  # Waiter starts serving Meal A
    context.request()  # Serves Meal A and transitions to Dessert B
    context.request()  # Serves Dessert B and transitions back to Meal A
```

## See Also

[state_pattern.py](https://github.com/faif/python-patterns/blob/master/patterns/behavioral/state.py) in the python-patterns repository on GitHub.

This example demonstrates how to use the State pattern effectively, allowing a waiter (Context) to serve different meals based on what order was placed by the customer and also depends on how much time has passed since the order was placed.