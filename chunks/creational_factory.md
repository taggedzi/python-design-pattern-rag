---
file: creational/factory.py
chunk: creational_factory.md
---

```python
"""
Creational Pattern: Factory Method

Defines an interface for creating an object but lets subclasses alter the type of objects that will be created.
This pattern promotes loose coupling between client and object creation logic.
"""

from abc import ABC, abstractmethod

class Product(ABC):
    """Abstract Product interface."""

    @abstractmethod
    def operation(self) -> str:
        """Define a common operation interface for all products."""
        pass

class ConcreteProductA(Product):
    def operation(self) -> str:
        return "Result from ConcreteProductA"

class ConcreteProductB(Product):
    def operation(self) -> str:
        return "Result from ConcreteProductB"

class Creator(ABC):
    """Abstract Creator class that declares the factory method."""

    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self) -> str:
        """
        Core business logic that relies on Product instances returned by the factory method.
        """
        product = self.factory_method()
        return f"Creator: Working with {product.operation()}"

class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()

# Example usage
if __name__ == "__main__":
    for creator in (ConcreteCreatorA(), ConcreteCreatorB()):
        print(creator.some_operation())
```

## Summary
Implementation of the Factory Method design pattern in Python.

## Docstrings
- Abstract Product interface.
- Define a common operation interface for all products.
- ConcreteProductA creates and returns an instance of ConcreteProductA.
- ConcreteProductB creates and returns an instance of ConcreteProductB.
- Abstract Creator class that declares the factory method.
- Core business logic that relies on Product instances returned by the factory method.
- ConcreteCreatorA creates and returns an instance of ConcreteProductA via its factory_method.
- ConcreteCreatorB creates and returns an instance of ConcreteProductB via its factory_method.

