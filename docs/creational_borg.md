# The Borg Pattern (Creational)

## Purpose

The Borg pattern allows multiple instances of a class to share the same internal state. Unlike the Singleton pattern, which restricts you to one instance, Borg lets you create many instances that all behave as if they share one "brain."

## Problem It Solves

Sometimes, you need multiple objects to share the same data—like configuration settings or a shared resource pool. While singletons or global variables can do this, they often reduce flexibility and create tight coupling. The Borg pattern offers a cleaner way: multiple independent objects that all share the same state.

## When to Use It

Use the Borg pattern when:

* You want several instances to share the same data.
* You need to synchronize state across multiple objects without enforcing a single instance.
* You want to centralize shared information without relying on global variables.

## When Not to Use It

Avoid this pattern if:

* Each instance needs to maintain its own separate state.
* You’re working in a multithreaded environment—Borg is not thread-safe by default.
* The shared data includes sensitive information that should be isolated per instance.

## How It Works

The Borg pattern works by setting each instance’s `__dict__` (which holds its attributes) to point to a shared dictionary defined at the class level. Any change made to one instance’s attributes is immediately reflected in all others.

## Real-World Analogy

Think of several scientists using the same whiteboard. Each person can write on it, and everyone sees the changes instantly. They’re working independently, but sharing the same workspace.

## Simplified Example

```python
class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state

# All Borg instances share the same state
b1 = Borg()
b2 = Borg()

b1.x = 10  # Set x using one instance
print(b2.x)  # The other instance sees the same value
```

In this example, both `b1` and `b2` are separate objects, but they share the same attributes and data.

## Learn More

Explore the complete implementation here:
[Borg Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/creational/borg.py)
