# The Abstract Factory Pattern (Creational)

## Intent

The Abstract Factory pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes. It's used to abstract away the details of how a set of products are created, composed and represented.

## Problem It Solves

In software development, we often have systems that need to be flexible and adaptable. This is where the Abstract Factory pattern comes in handy. Imagine you’re developing an application for both Windows and MacOS platforms. You want your codebase to be as platform-independent as possible so it can easily support new operating systems without having to modify a lot of existing code. The Abstract Factory pattern allows you to do this by providing a way to encapsulate a group of individual factories that have a common theme, i.e., they create products belonging to the same product family.

## When to Use It

The Abstract Factory is all about decoupling the client from concrete implementations and making it work with any pre-configured factory or set of related factories without having to modify your codebase. This pattern should be used when you want a run-time pluggability of products, i.e., you need an application that can use instances of different families of products.

## When NOT to Use It

The Abstract Factory is not suitable for systems where the client needs to work with only one product family at a time. If your system deals with just two or three classes related by a common interface, it might be simpler and more straightforward to instantiate these classes directly using constructor injection.

## How It Works

In an Abstract Factory pattern, there are four main components:

1. **Abstract Products** - These are the interfaces that define operations for different types of products. In our example, this would include `Button` and `Checkbox` abstract classes.
2. **Concrete Products** - These are the actual implementations of the Abstract Products. We have separate concrete product classes for each operating system (Windows and MacOS).
3. **Abstract Factory** - This is an interface that provides methods to create different types of products. In our example, this would be `GUIFactory`.
4. **Concrete Factories** - These are the implementations of Abstract Factory interfaces. Each Concrete Factory corresponds to a specific operating system and creates concrete product objects belonging to that family.

## Real-World Analogy

Imagine you're at a supermarket. You have different sections for fruits, vegetables, dairy products etc., each with their own counters and checkout lines. Now imagine if the supermarket had a way of dynamically managing these sections based on your shopping preferences (e.g., vegan or gluten-free). That's similar to how an Abstract Factory pattern allows for dynamic management of product families in an application, based on runtime configuration or user preference.

## Simplified Example

Here is a simplified example:

```python
class ProductA:
    def do_something(self) -> str:
        pass

class ConcreteProductA1(ProductA):
    def do_something(self) -> str:
        return "Implementation of Product A1"

class ConcreteProductA2(ProductA):
    def do_something(self) -> str:
        return "Implementation of Product A2"
```

In this example, `ProductA` is the Abstract Product and `ConcreteProductA1` and `ConcreteProductA2` are its concrete implementations.

## See Also

The corresponding Python file for this lesson can be found [here](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/creational/abstract_factory.py).
