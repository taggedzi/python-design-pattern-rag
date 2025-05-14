# The Factory Pattern (Creational)

## Purpose

The Factory pattern provides a way to create objects without specifying the exact class. It centralizes object creation, which promotes flexibility and reduces direct dependencies in your code.

## Problem It Solves

Sometimes your code needs to create different types of objects depending on conditions. Using hardcoded `if` or `switch` statements to decide which class to use can make your code harder to maintain. The Factory pattern simplifies this by putting the creation logic into one place. This allows you to add new object types without changing the code that uses them.

## When to Use It

Use the Factory pattern when:

* Your program needs to create different types of related objects.
* You want to separate creation logic from business logic.
* You expect to add new types of objects in the future.
* Object creation depends on dynamic conditions or configuration.

## When Not to Use It

Avoid this pattern if:

* There's only one type of object being created.
* The creation logic is simple and unlikely to change.
* Introducing a factory adds more complexity than benefit.

## How It Works

The Factory pattern includes:

1. A base class or interface that defines the object type.
2. A factory method that creates and returns objects.
3. Client code that calls the factory method instead of instantiating objects directly.

## Real-World Analogy

Think of ordering pizza at a restaurant. You don’t give instructions for how to make a Margherita—you just order it by name. The kitchen knows how to prepare it. In the same way, a factory method lets you request an object without knowing the details of how it’s created.

## Simplified Example

Here’s a basic Python example using static factory methods:

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

* `Pizza` is the main product class.
* `margherita()` and `prosciutto()` are factory methods that return pre-configured pizza objects.
* The client code gets the right type of pizza without needing to know how it’s built.

## Learn More

Explore the full Python implementation here:
[Factory Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/creational/factory.py)
