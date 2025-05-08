# The Composite Pattern (Structural)

## Intent

The Composite pattern is used to organize and structure complex tree structures made up of objects where each object can be treated individually or collectively. It provides a way to compose objects into tree structures and then work with these structures as if they were individual objects.

## Problem It Solves

This design pattern addresses the problem of treating individual objects and compositions uniformly, which simplifies code management and organization. It allows clients to treat complex trees structured as well-defined data structures (individual objects) in a uniform manner.

## When to Use It

The Composite pattern is ideal when you want to create complex tree structures where each node can be treated individually or collectively, making it suitable for use cases such as file systems, HTML documents, and database queries.

## When NOT to Use It

It's not a good idea to overuse the Composite pattern because it might make code more complicated than necessary. If your application doesn’t require complex tree structures or hierarchies, using simpler patterns like classes could be sufficient.

## How It Works

The Composite pattern involves three main components: Component (abstract base class), Leaf (concrete component with no children) and Composite (concrete component with sub-components). The Component interface declares common operations for both simple and complex objects of a composition. A client uses these classes to work with the compositions in a uniform manner.

## Real-World Analogy

Imagine you have a family tree, where each person can be an individual leaf (you), or they could be part of a larger group (your siblings). If your family grows, it's not uncommon for new members to join the group - just like how a composite object can contain other composites or leaves.

## Simplified Example

Here is a simplified example:

```python
class Component:  # Abstract base class
    def operation(self) -> str: pass

class Leaf(Component):  # Concrete component with no children
    def __init__(self, name: str) -> None: self.name = name
    def operation(self) -> str: return f"Leaf({self.name})"

class Composite(Component):  # Concrete component with sub-components
    def __init__(self, name: str) -> None:
        self.name = name
        self._children: List[Component] = []
    
    def add(self, component: Component) -> None: self._children.append(component)
    def remove(self, component: Component) -> None: self._children.remove(component)
    def operation(self) -> str: 
        results = [child.operation() for child in self._children]
        return f"Composite({self.name})[{' + '.join(results)}]"
```

## See Also

The corresponding Python file can be found [here](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/structural/composite.py).
