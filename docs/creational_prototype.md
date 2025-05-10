# The Prototype Pattern (Creational)

## Purpose

The Prototype pattern allows you to create new objects by copying existing ones, rather than building them from scratch. This is especially helpful for creating complex or expensive-to-initialize objects.

## The Problem It Solves

Creating objects can sometimes be slow or resource-intensive—especially when they have many attributes or dependencies. Rather than recreating these objects from the ground up, the Prototype pattern lets you make copies (clones) of a pre-existing object and modify them if needed.

## When to Use It

Use the Prototype pattern when:

* You need to create objects based on a runtime configuration or input.
* Creating objects from scratch is slow or resource-heavy.
* You want to avoid tightly coupling code to specific classes.

## When NOT to Use It

Avoid using this pattern when:

* The object is simple and cheap to create with a constructor.
* Objects are immutable (since they can’t be modified after creation).
* Initialization logic is complex and cloning would skip critical setup steps.

## How It Works

You define a `clone()` method that returns a copy of the object. This method is typically part of a base `Prototype` class or interface that other classes inherit from. The `clone()` method often performs a deep copy so the cloned object doesn’t share references with the original.

## Real-World Analogy

Imagine having a house blueprint (prototype). Instead of designing every new house from scratch, you use the blueprint to create new houses and then customize things like paint color or interior layout. This saves time and ensures consistency.

## Simplified Example

Here’s an example in Python using a simple `Shape` class:

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

# Example usage
original = Shape("blue", (0, 0))
copy1 = original.clone()
copy1.move(5, 10)

print(original)  # Shape(color=blue, position=(0, 0))
print(copy1)     # Shape(color=blue, position=(5, 10))
```

In this example:

* `Shape` is the concrete class implementing the `Prototype` interface.
* `clone()` returns a deep copy of the shape.
* The original and cloned shapes can be changed independently.

## Learn More

You can find the full implementation on GitHub:
[Prototype Pattern in Python](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/creational/prototype.py)
