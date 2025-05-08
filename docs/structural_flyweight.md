# The Flyweight Pattern (Structural)

## Intent

The Flyweight pattern is used to minimize memory usage or computational expenses by sharing as much data as possible with similar objects. It's particularly useful when a large number of objects are being created, and the cost of creating these objects is high.

## Problem It Solves

This design pattern addresses the problem of over-usage of RAM resources in applications where an application requires a huge number of objects which consume a lot of memory space. The Flyweight pattern aims to reduce such overhead by sharing as much data as possible with similar objects, rather than creating new object for each separate occurrence.

## When to Use It

The Flyweight pattern is best used when:

1. An application uses a large number of objects which consume a lot of memory space.
2. The creation of these objects is costly in terms of computational resources or time.
3. Most group of these objects are identical, and only few state differences exist between them.
4. A part of the object's state can be shared across multiple objects instead of being duplicated for each object.

## When NOT to Use It

The Flyweight pattern should not be used in situations where:

1. Objects have a lot of intrinsic (unique) state that cannot be shared with other objects.
2. The number of distinct classes is small and fixed, so the overhead of managing them can't be justified.
3. You need to create new object for each separate occurrence of an object.
4. Sharing data between objects will cause unnecessary complexity in your code.

## How It Works

The Flyweight pattern involves a `Flyweight` class, which contains the shared state and a `ConcreteFlyweight` class that extends the `Flyweight` base class and adds any additional state management required by the application. The `FlyweightFactory` class is responsible for creating and managing flyweight objects.

## Real-World Analogy

You can think of the Flyweight pattern as a library of books, where each book (object) has common characteristics like title, author etc., that are shared across multiple instances. Each instance (book copy), however, may have unique characteristics like page number, borrower's name etc. The Flyweight pattern helps to manage these shared and unique characteristics efficiently.

## Simplified Example

Here is a simplified example of the Flyweight pattern:

```python
class Flyweight:  # Shared state (Flyweight)
    def __init__(self, shared_state):
        self._shared_state = shared_state

    def operation(self, unique_state):
        print(f"Shared State: {self._shared_state} | Unique State: {unique_state}")

class FlyweightFactory:  # Manages flyweights and ensures their reuse
    _flyweights = {}

    def __new__(cls, shared_state):
        key = hash(shared_state)
        if not cls._flyweights.get(key):
            cls._flyweights[key] = super().__new__(cls)
        return cls._flyweights[key]

    def __init__(self, shared_state):
        Flyweight.__init__(self, shared_state)

# Usage:
factory = FlyweightFactory("Shared State")
flyweight1 = factory.get_flyweight("Unique State 1")
flyweight2 = factory.get_flyweight("Unique State 2")
```

## See Also

The corresponding Python file for the Flyweight pattern can be found [here](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/structural/flyweight.py)
