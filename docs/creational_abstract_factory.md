# The Abstract Factory Pattern (Creational)

## Purpose

The Abstract Factory pattern provides a way to create families of related or dependent objects without specifying their exact classes. It helps make your code more flexible and easier to extend by grouping object creation into a unified interface.

## Problem It Solves

In some applications, you need to support multiple sets of objects that should work together—such as GUI components for different platforms like Windows or macOS. Without this pattern, you might end up using `if-else` or `switch` statements scattered throughout your code to choose the right object. Abstract Factory centralizes this logic, making it easier to manage and extend, especially when supporting new platforms or styles.

## When to Use It

Use this pattern when:

* You need to work with families of related objects (e.g., buttons and checkboxes that match in style).
* You want to avoid hardcoding class names throughout your application.
* You want to switch product families at runtime.

## When Not to Use It

Avoid this pattern if:

* Your app only needs a few objects and doesn't benefit from abstraction.
* You don’t plan to support multiple interchangeable families of objects.

## How It Works

The pattern includes four key parts:

1. **Abstract Products** – Interfaces or base classes that define a common set of behaviors (e.g., `Button`, `Checkbox`).
2. **Concrete Products** – Specific implementations for each product family (e.g., `WindowsButton`, `MacButton`).
3. **Abstract Factory** – An interface that declares methods to create each type of product.
4. **Concrete Factories** – Classes that implement the abstract factory and create a set of related products.

## Real-World Analogy

Think of a supermarket that adjusts its offerings based on your dietary choice. If you choose “vegan,” you’re directed to vegan-friendly versions of fruits, dairy alternatives, and baked goods—all tailored to that preference. Similarly, an abstract factory supplies a consistent set of products from the same family.

## Simplified Example

Here's a basic Python example:

```python
from abc import ABC, abstractmethod

# Abstract Product
class ProductA(ABC):
    @abstractmethod
    def do_something(self) -> str:
        pass

# Concrete Products
class ConcreteProductA1(ProductA):
    def do_something(self) -> str:
        return "Implementation of Product A1"

class ConcreteProductA2(ProductA):
    def do_something(self) -> str:
        return "Implementation of Product A2"
```

In this example:

* `ProductA` is the abstract product interface.
* `ConcreteProductA1` and `ConcreteProductA2` are different versions tailored to specific themes or platforms.

A full implementation would also include a factory interface and one or more factory classes to handle product creation.

## Learn More

See the complete implementation in Python here:
[Abstract Factory on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/creational/abstract_factory.py)
