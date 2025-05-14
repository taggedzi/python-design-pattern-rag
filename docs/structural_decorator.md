# The Decorator Pattern (Structural)

## Purpose

The Decorator pattern lets you add new behavior to individual objects without changing their original structure. It supports the Open/Closed Principle, allowing classes to be extended without being modified.

## Problem It Solves

If you want to enhance an object’s behavior, one approach is to use inheritance. But this can lead to a large number of subclasses to cover all combinations of features. The Decorator pattern solves this by wrapping objects in other objects (decorators) that add or modify behavior, allowing you to build features dynamically and flexibly.

## When to Use It

Use this pattern when:

* You want to add behavior to an object without affecting other instances of the same class.
* You need to add features at runtime.
* You want to avoid creating many subclasses for different feature combinations.

Typical use cases include logging, input validation, user interface enhancements, or formatting.

## When Not to Use It

Avoid this pattern if:

* Inheritance is simpler and sufficient for your needs.
* The layering of decorators makes your code hard to follow.
* The behavior you're adding is better handled by other patterns, such as Strategy or Observer.

## How It Works

The pattern includes four main parts:

1. **Component interface** – Defines the standard methods.
2. **Concrete component** – The object to which behavior will be added.
3. **Base decorator** – Wraps a component and passes method calls to it.
4. **Concrete decorators** – Add or override functionality by extending the base decorator.

You can stack multiple decorators to build up the desired behavior.

## Real-World Analogy

Think of customizing a pizza. You start with a base (like Margherita), then add toppings such as mozzarella, olives, or mushrooms. Each topping adds a feature, but you don’t need a separate class for every topping combination—just layer decorators.

## Simplified Example

Here’s a basic Python example:

```python
# Component interface
class Pizza:
    def get_cost(self):
        pass

    def get_description(self):
        pass

# Concrete component
class Margherita(Pizza):
    def get_cost(self):
        return 10

    def get_description(self):
        return "Margherita"

# Base decorator
class PizzaDecorator(Pizza):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza

    def get_cost(self):
        return self.pizza.get_cost()

    def get_description(self):
        return self.pizza.get_description()

# Concrete decorator
class Mozzarella(PizzaDecorator):
    def get_cost(self):
        return super().get_cost() + 5

    def get_description(self):
        return f"{super().get_description()}, Mozzarella"
```

### Usage

```python
pizza = Mozzarella(Margherita())
print(pizza.get_description())  # Output: Margherita, Mozzarella
print(pizza.get_cost())         # Output: 15
```

You can stack decorators like `Olives`, `Mushrooms`, and so on, to build complex combinations.

## Learn More

View the complete implementation here:
[Decorator Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/structural/decorator.py)
