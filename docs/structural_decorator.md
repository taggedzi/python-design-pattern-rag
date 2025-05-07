---
file: structural/decorator.py
chunk: structural_decorator.md
---

```python
"""
Structural Pattern: Decorator

Allows behavior to be added to individual objects, dynamically,
without affecting the behavior of other objects from the same class.
Useful for adhering to the Open/Closed Principle.
"""

from abc import ABC, abstractmethod

# Component interface
class Component(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

# Concrete component
class ConcreteComponent(Component):
    def operation(self) -> str:
        return "ConcreteComponent"

# Base Decorator
class Decorator(Component):
    def __init__(self, component: Component) -> None:
        self._component = component

    def operation(self) -> str:
        return self._component.operation()

# Concrete decorators
class DecoratorA(Decorator):
    def operation(self) -> str:
        return f"DecoratorA({self._component.operation()})"

class DecoratorB(Decorator):
    def operation(self) -> str:
        return f"DecoratorB({self._component.operation()})"

# Example usage
if __name__ == "__main__":
    simple = ConcreteComponent()
    print("Simple:", simple.operation())

    decorated = DecoratorA(DecoratorB(simple))
    print("Decorated:", decorated.operation())

```

## Summary
Implementation of the Decorator Design Pattern in Python

## Docstrings
- Decorator allows behavior to be added to individual objects, dynamically, without affecting the behavior of other objects from the same class. Useful for adhering to the Open/Closed Principle.
- Component interface with an abstract method operation that returns a string.
- Concrete component that implements the Component interface and provides a specific implementation of the operation method.
- Base Decorator class that takes a Component as an argument and delegates the operation to the wrapped component. It also provides an abstract method for adding behavior.
- Concrete decorator A that extends Decorator and adds its own behavior to the operation method by prefixing the result with 'DecoratorA'.
- Concrete decorator B that extends Decorator and adds its own behavior to the operation method by prefixing the result with 'DecoratorB'.

