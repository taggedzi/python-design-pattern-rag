# The Abstract Factory Pattern (Creational)

## Purpose

The Abstract Factory pattern provides an interface for creating groups of related or dependent objects without needing to specify their exact classes. It’s used to make systems more flexible and easier to extend by abstracting the creation of product families.

## The Problem It Solves

In some programs, you need to support multiple sets of objects that should work together—for example, GUI elements for different operating systems like Windows and macOS. Instead of scattering `if-else` or `switch` logic across your code to decide which object to create, you can use an abstract factory to centralize and simplify that decision. This makes it easier to support new platforms or themes in the future.

## When to Use It

Use the Abstract Factory pattern when:

* Your code needs to work with multiple families of related objects (e.g., a GUI that supports different platforms).
* You want to avoid hard-coding specific class names throughout your codebase.
* You want to provide a way to switch between different product families at runtime.

## When NOT to Use It

Avoid this pattern if:

* Your app only uses a small number of related classes, and adding abstraction would complicate the design.
* You don’t need to support multiple interchangeable families of products.

## How It Works

The pattern includes four main parts:

1. **Abstract Products** – Interfaces that define common operations (e.g., `Button`, `Checkbox`).
2. **Concrete Products** – Actual implementations of those interfaces for each product family (e.g., `WindowsButton`, `MacButton`).
3. **Abstract Factory** – An interface for creating each type of product (e.g., `GUIFactory`).
4. **Concrete Factories** – Implementations of the abstract factory for each product family (e.g., `WindowsFactory`, `MacFactory`).

## Real-World Analogy

Think of a supermarket that adapts to your dietary needs. If you choose "vegan," you’re directed to vegan fruit, vegan dairy alternatives, and vegan baked goods—all tailored to that lifestyle. Similarly, an abstract factory delivers a full set of products matched to a specific family or context, without mixing them up.

## Simplified Example

Here’s a basic structure in Python:

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

* `ProductA` is the abstract product.
* `ConcreteProductA1` and `ConcreteProductA2` are platform- or theme-specific implementations.

In a full version, you’d also have a factory interface and one or more factory classes to create the products.

## Learn More

You can view the complete implementation in Python here:
[Abstract Factory on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/creational/abstract_factory.py)
