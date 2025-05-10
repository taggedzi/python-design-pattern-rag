# The State Pattern (Behavioral)

## Purpose

The State pattern lets an object change its behavior when its internal state changes. Instead of using many `if` or `switch` statements, the pattern helps you organize state-specific behavior into separate classes.

## The Problem It Solves

In many programs, an object’s behavior depends on its current state. For example, a button may behave differently when pressed, hovered, or disabled. If you manage these behaviors using conditionals spread throughout your code, it can become hard to understand and update. The State pattern solves this by letting each state be handled by its own class, keeping logic organized and easier to modify.

## When to Use It

Use this pattern when:

* An object’s behavior changes based on its state.
* You want to avoid a mess of `if`/`else` or `switch` statements.
* You want to make it easy to add new states without modifying existing code.

## When NOT to Use It

Avoid this pattern if:

* The object's behavior doesn’t really depend on state.
* There are only a couple of simple states—using an `enum` or basic conditionals might be easier.
* Adding classes for each state would overcomplicate your design.

## How It Works

The pattern has three main components:

1. **Context** – The object whose behavior changes depending on its state. It holds a reference to the current state and delegates behavior to it.
2. **State (abstract class or interface)** – Defines a common method (like `handle()`) that all concrete states must implement.
3. **Concrete State classes** – Represent specific states. Each implements the behavior for that state and often triggers transitions to other states.

## Real-World Analogy

Imagine ordering food at a restaurant. If you order a burger, you get a burger; if you order a salad, you get a salad. Each order represents a state, and the waiter delivers a different result depending on what you asked for. The waiter (context) changes behavior based on your order (state).

## Simplified Example

Here’s a basic example in Python:

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

### Usage

```python
context = Context(ConcreteStateA())
context.request()  # ConcreteStateA handles request
context.request()  # ConcreteStateB handles request
```

Here, the context starts in `ConcreteStateA`, handles a request, and transitions to `ConcreteStateB`, which then transitions back on the next request. Each state is responsible for its own behavior and any transitions.

## Learn More

For a complete implementation in Python, visit:
[State Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/behavioral/state.py)
