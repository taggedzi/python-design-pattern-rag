# The Factory Pattern (Creational)

## Intent

The Factory pattern is a creational design pattern that provides an interface for creating objects, but it lets subclasses decide which class to instantiate. It promotes loose coupling between client and object creation logic.

## Problem It Solves

In software development, we often need to create objects without knowing exactly what type of object will be needed at runtime. This could be due to a variety of reasons such as the complexity of an application, extensibility requirements, or simply because new types are added frequently. The Factory pattern addresses this problem by providing a way to delegate the instantiation logic to child classes.

## When to Use It

The Factory pattern is typically used in situations where we need to create objects dynamically at runtime based on certain conditions. This could be when creating instances of different types of classes, or when dealing with complex configurations that require many steps and dependencies.

## When NOT to Use It

While the Factory pattern can solve a lot of problems, it should not be used in situations where:

- The objects being created are simple and do not have complex creation logic.
- There is only one type of product class.
- The client code does not need to work with an interface or abstract class.

## How It Works

The Factory pattern involves a factory class that has a method for creating objects. This method can be overridden by subclasses to create different types of products. The core business logic in the client code will often use this factory method without knowing about the specific product classes, which is why it's referred to as an abstract factory.

## Real-World Analogy

Imagine a pizza restaurant that serves multiple types of pizzas (products). Instead of having a line of chefs each making a different type of pizza, the restaurant uses a factory that takes orders and delivers the correct type of pizza based on what's ordered by the customer. This is similar to how the Factory pattern works - it creates objects without exposing the instantiation logic to the client code.

## Simplified Example

Here's a simplified example of the Factory pattern in Python:

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
p1 = Pizza.margherita()  # Creates a margherita pizza
print(p1.ingredients)  # ['mozzarella', 'tomatoes']
```

In this example, the `Pizza` class is acting as a factory for creating different types of pizzas (products). The `margherita()` and `prosciutto()` methods are factory methods that create specific types of pizzas.

## See Also

You can find the full implementation of this pattern in the Python file [here](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/creational/factory.py).
