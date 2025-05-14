# The Composite Pattern (Structural)

## Purpose

The Composite pattern allows you to treat individual objects and groups of objects in the same way. It’s useful for building tree-like structures—such as folders, menus, or graphical elements—where each part, whether simple or complex, supports the same operations.

## Problem It Solves

Many applications deal with structures that mix simple and complex elements. Without this pattern, you'd need different logic to handle each type, leading to repetitive and error-prone code. The Composite pattern unifies them under one interface, so they can be processed in the same way.

## When to Use It

Use the Composite pattern when:

* You need to represent part-whole hierarchies, like file systems or organizational charts.
* You want to treat individual objects and groups consistently.
* Your structure is recursive, such as a tree or nested container.

## When Not to Use It

Avoid this pattern if:

* Your data structure is flat and doesn’t need hierarchy.
* A simpler class design would be easier to understand and maintain.
* The abstraction adds more complexity than benefit.

## How It Works

The Composite pattern defines three main components:

1. **Component** – An interface or abstract class for all objects in the structure.
2. **Leaf** – A basic object that performs work and doesn’t have children.
3. **Composite** – A container that can hold other components (leaves or other composites) and delegate operations to them.

Both `Leaf` and `Composite` follow the same interface, making them interchangeable in the structure.

## Real-World Analogy

Think of a company org chart. An employee is a leaf. A department manager (composite) oversees a group of employees and possibly other departments. Whether you’re asking for a report from a person or a department, you use the same method.

## Simplified Example

Here’s a basic implementation in Python:

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

### Usage Example

```python
root = Composite("root")
leaf1 = Leaf("A")
leaf2 = Leaf("B")
subtree = Composite("branch")
subtree.add(Leaf("C"))

root.add(leaf1)
root.add(subtree)
root.add(leaf2)

print(root.operation())  # Output: Composite(root)[Leaf(A) + Composite(branch)[Leaf(C)] + Leaf(B)]
```

## Learn More

See the full implementation here:
[Composite Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/structural/composite.py)
