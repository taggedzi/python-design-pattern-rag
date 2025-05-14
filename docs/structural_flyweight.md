# The Flyweight Pattern (Structural)

## Purpose

The Flyweight pattern reduces memory use and improves performance by sharing common data between many similar objects. It's especially useful when working with large numbers of objects that have repeated data.

## Problem It Solves

In many applications, you might create thousands of objects—many of which store the same data. This can waste memory. The Flyweight pattern helps by splitting objects into shared (intrinsic) and unique (extrinsic) parts, so that only the unique data is stored separately, and the shared part is reused.

## When to Use It

Use this pattern when:

* You need to create a large number of similar objects.
* Many objects share common data that can be reused.
* You want to reduce memory consumption or speed up performance.
* The shared and unique parts of the data can be clearly separated.

## When Not to Use It

Avoid the pattern if:

* Most of your objects have unique data that can't be shared.
* Managing shared state adds more complexity than benefit.
* Sharing objects would hurt readability or create unwanted side effects.
* Each object needs to be fully independent.

## How It Works

The pattern divides an object into:

* **Shared (intrinsic) state**: data that is common and reused.
* **Unique (extrinsic) state**: data that is specific to each use.

A `Flyweight` class holds the shared state. A `FlyweightFactory` checks if that shared state already exists. If so, it reuses it; if not, it creates and stores it. When using the flyweight, the client provides the unique state.

## Real-World Analogy

Think of a public library. Everyone borrows the same book titles (shared content), but each reader may have a different return date or borrow history (unique data). The Flyweight pattern uses the same idea—share the common parts, track only what’s unique per user.

## Simplified Example

Here’s a basic implementation in Python:

```python
class Flyweight:
    def __init__(self, shared_state):
        self._shared_state = shared_state

    def operation(self, unique_state):
        print(f"Shared State: {self._shared_state} | Unique State: {unique_state}")

class FlyweightFactory:
    _flyweights = {}

    @classmethod
    def get_flyweight(cls, shared_state):
        key = str(shared_state)
        if key not in cls._flyweights:
            cls._flyweights[key] = Flyweight(shared_state)
        return cls._flyweights[key]
```

### Usage

```python
factory = FlyweightFactory()

flyweight1 = factory.get_flyweight("Shared-1")
flyweight1.operation("Unique-A")

flyweight2 = factory.get_flyweight("Shared-1")
flyweight2.operation("Unique-B")

print(flyweight1 is flyweight2)  # Output: True — same instance reused
```

This example shows how objects with the same shared data reuse a single instance, saving memory.

## Learn More

View the full Python implementation here:
[Flyweight Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/structural/flyweight.py)
