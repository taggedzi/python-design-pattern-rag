# The Flyweight Pattern (Structural)

## Purpose

The Flyweight pattern is used to reduce memory usage and improve performance by sharing common data between similar objects instead of storing it multiple times. This is especially useful when working with large numbers of similar objects.

## The Problem It Solves

Some applications create many objects that use a lot of memory—even when many of those objects are mostly the same. The Flyweight pattern helps reduce this overhead by sharing the repeated (intrinsic) parts of an object and only storing the unique (extrinsic) data separately.

## When to Use It

Use the Flyweight pattern when:

* Your program creates a huge number of similar objects.
* Many objects share common data that can be reused.
* You want to reduce memory consumption and improve performance.
* The shared part of an object can be separated from the unique part.

## When NOT to Use It

Avoid this pattern when:

* Most objects have unique data and don’t share common parts.
* The overhead of managing shared data is greater than the memory saved.
* Object sharing would make your code harder to read or maintain.
* You need each object to be truly independent from the others.

## How It Works

The Flyweight pattern separates an object into two parts:

* **Shared (intrinsic) state** – the data that's common across many objects.
* **Unique (extrinsic) state** – the data that's specific to each object.

A `Flyweight` object stores the shared state. A `FlyweightFactory` ensures that shared states are reused rather than duplicated. The client code supplies the unique state when calling the flyweight’s method.

## Real-World Analogy

Think of a library where multiple people check out copies of the same book. The content (title, author, chapters) is the shared state. Each reader’s specific notes or the return date is unique to their copy. Flyweight is like using one shared version of the content across all users while only tracking the differences separately.

## Simplified Example

Here’s a basic example in Python:

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

print(flyweight1 is flyweight2)  # True — same shared object
```

This shows how two objects with the same shared state use a single instance, saving memory.

## Learn More

View the complete implementation here:
[Flyweight Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/structural/flyweight.py)
