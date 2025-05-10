# The Composite Pattern (Structural)

## Purpose

The Composite pattern is used to treat individual objects and groups of objects in a uniform way. It allows you to build tree-like structures (like folders, menus, or graphical elements) where each part of the tree can be treated the same—whether it's a single item or a group of items.

## The Problem It Solves

In many applications, you may need to work with structures made of both simple and complex elements. Without the Composite pattern, you’d have to write separate logic to handle individual items and groups, leading to repetitive code. This pattern unifies them under a common interface, simplifying how they’re managed and manipulated.

## When to Use It

Use the Composite pattern when:

* You need to represent part-whole hierarchies (e.g., file systems, document outlines).
* You want to treat individual objects and groups of objects uniformly.
* You need to support recursive structures, such as trees or nested containers.

## When NOT to Use It

Avoid this pattern if:

* Your structure is flat and doesn’t benefit from a hierarchy.
* Adding abstraction through a component interface makes your code unnecessarily complex.
* Simpler class designs can get the job done more clearly.

## How It Works

The pattern involves three core parts:

1. **Component** – The base interface or abstract class that defines common operations.
2. **Leaf** – Represents the individual objects with no children.
3. **Composite** – Represents complex objects that can have child components (both leaves and other composites).

The key is that both `Leaf` and `Composite` implement the same interface, allowing client code to interact with them the same way.

## Real-World Analogy

Imagine a company org chart. An individual employee is a leaf, while a department head (composite) manages a group of employees and possibly other departments. Whether you're interacting with an individual or a department, you treat them the same when asking for a task report.

## Simplified Example

Here’s a basic example in Python:

```python
from typing import List

class Component:
    def operation(self) -> str:
        pass

class Leaf(Component):
    def __init__(self, name: str):
        self.name = name

    def operation(self) -> str:
        return f"Leaf({self.name})"

class Composite(Component):
    def __init__(self, name: str):
        self.name = name
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)

    def remove(self, component: Component) -> None:
        self._children.remove(component)

    def operation(self) -> str:
        results = [child.operation() for child in self._children]
        return f"Composite({self.name})[{' + '.join(results)}]"
```

### Example Usage:

```python
root = Composite("root")
leaf1 = Leaf("A")
leaf2 = Leaf("B")
subtree = Composite("branch")
subtree.add(Leaf("C"))

root.add(leaf1)
root.add(subtree)
root.add(leaf2)

print(root.operation())  # Composite(root)[Leaf(A) + Composite(branch)[Leaf(C)] + Leaf(B)]
```

## Learn More

For the full implementation in Python, visit:
[Composite Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/structural/composite.py)
