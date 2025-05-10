# The Factory Pattern (Creational)

## Purpose

The Factory pattern provides a way to create objects without having to specify the exact class of the object that will be created. It promotes loose coupling by shifting the responsibility of object creation from the client code to a factory method.

## The Problem It Solves

Sometimes, your code needs to create different types of objects based on certain conditions. Hardcoding `if` or `switch` statements to decide which class to instantiate can make your code rigid and hard to maintain. The Factory pattern helps by centralizing the creation logic, allowing the program to decide which object to create at runtime without modifying the client code.

## When to Use It

Use the Factory pattern when:

* Your application needs to create many types of related objects.
* You want to decouple object creation from the business logic.
* New object types might be added in the future.
* You need to create objects based on dynamic input or configuration.

## When NOT to Use It

Avoid this pattern if:

* There’s only one type of object to create.
* Object creation is simple and doesn't vary.
* Adding a factory adds unnecessary complexity.

## How It Works

The pattern involves:

1. A base class or interface for the type of object to be created.
2. A factory method that creates and returns instances of those types.
3. The client code calls the factory method instead of using `new` or direct class instantiation.

## Real-World Analogy

Think of a pizza restaurant. You don’t tell the chef how to make a Margherita pizza—you just place the order. The kitchen (factory) knows what ingredients to use and how to prepare it. Similarly, the Factory pattern lets the client request an object without knowing the creation steps.

## Simplified Example

Here’s a simple Python example using static factory methods:

```python
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @staticmethod
    def margherita():
        return Pizza(['mozzarella', 'tomatoes'])

    @staticmethod
    def prosciutto():
        return Pizza(['mozzarella', 'tomatoes', 'ham'])

# Usage:
p1 = Pizza.margherita()
print(p1.ingredients)  # Output: ['mozzarella', 'tomatoes']
```

In this example:

* `Pizza` is the product class.
* `margherita()` and `prosciutto()` are factory methods.
* The client (you) gets the right object without worrying about how it’s made.

## Learn More

You can find the full implementation in Python here:
[Factory Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/creational/factory.py)
