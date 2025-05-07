---
file: structural/composite.py
chunk: structural_composite.md
---

```python
"""
Structural Pattern: Composite

Lets you compose objects into tree structures to represent part-whole hierarchies.
Clients can treat individual objects and compositions uniformly.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Component(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        return False

class Leaf(Component):
    def __init__(self, name: str) -> None:
        self.name = name

    def operation(self) -> str:
        return f"Leaf({self.name})"

class Composite(Component):
    def __init__(self, name: str) -> None:
        self.name = name
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)

    def remove(self, component: Component) -> None:
        self._children.remove(component)

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        results = [child.operation() for child in self._children]
        return f"Composite({self.name})[{' + '.join(results)}]"

# Example usage
if __name__ == "__main__":
    leaf1 = Leaf("A")
    leaf2 = Leaf("B")
    composite1 = Composite("Group1")
    composite1.add(leaf1)
    composite1.add(leaf2)

    leaf3 = Leaf("C")
    composite2 = Composite("Group2")
    composite2.add(composite1)
    composite2.add(leaf3)

    print(composite2.operation())

```

## Summary
Implementation of the Composite Design Pattern in Python

## Docstrings
- Structural Pattern: Composite

Lets you compose objects into tree structures to represent part-whole hierarchies.
Clients can treat individual objects and compositions uniformly.
- Component(ABC): Abstract base class for components in the composite pattern.
- Leaf(name: str): Represents a leaf node in the composite pattern.
- Composite(name: str): Represents a composite node in the composite pattern, which can contain other components.
- operation(self) -> str: Abstract method to be implemented by subclasses. In Leaf, returns a string representation of the leaf.
In Composite, combines the results of operation calls on its children.

