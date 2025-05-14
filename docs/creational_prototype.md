# The Prototype Pattern (Creational)

## Purpose

The Prototype pattern lets you create new objects by copying existing ones instead of creating them from scratch. It’s useful when objects are complex or costly to initialize.

## Problem It Solves

Creating certain objects can take time or use a lot of resources, especially if they have many attributes or dependencies. Rather than rebuilding these objects each time, the Prototype pattern allows you to clone an existing object and modify the copy if needed.

## When to Use It

Use this pattern when:

* You need to create objects at runtime based on an existing template.
* Creating an object from scratch is slow or resource-intensive.
* You want to reduce coupling between your code and specific classes.

## When Not to Use It

Avoid using this pattern if:

* The object is simple and easy to construct.
* The object is immutable (cannot be changed after creation).
* The object requires complex initialization that cloning might skip.

## How It Works

Each object defines a `clone()` method that returns a new copy. This method is usually part of a base `Prototype` class or interface. In many cases, `clone()` uses a deep copy to ensure the new object doesn’t share references with the original.

## Real-World Analogy

Think of using a house blueprint. Instead of designing each house from scratch, you copy the blueprint and customize the new house as needed. This saves time and ensures consistency.

## Simplified Example

Here’s a basic Python implementation:

```python
import copy
from abc import ABC, abstractmethod

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class Shape(Prototype):
    def __init__(self, color: str, position: tuple[int, int]) -> None:
        self.color = color
        self.position = position

    def move(self, dx: int, dy: int) -> None:
        x, y = self.position
        self.position = (x + dx, y + dy)

    def __str__(self) -> str:
        return f"Shape(color={self.color}, position={self.position})"

    def clone(self):
        return copy.deepcopy(self)
```

### Usage

```python
original = Shape("blue", (0, 0))
copy1 = original.clone()
copy1.move(5, 10)

print(original)  # Shape(color=blue, position=(0, 0))
print(copy1)     # Shape(color=blue, position=(5, 10))
```

In this example:

* `Shape` implements the `Prototype` interface.
* `clone()` returns a deep copy of the object.
* The original and the copy are separate objects that can be modified independently.

## Learn More

See the full Python implementation here:
[Prototype Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/creational/prototype.py)
