# The Decorator Pattern (Structural)

## Purpose

The Decorator pattern lets you add new behavior to individual objects—either at runtime or compile time—without changing the structure of the original class. It supports the Open/Closed Principle by allowing behavior to be extended without modifying existing code.

## The Problem It Solves

If you need to add features to an object, one option is to create subclasses. But this quickly becomes unmanageable if you need many combinations of features. The Decorator pattern solves this by allowing you to wrap objects with other objects (decorators) that add specific functionality, reducing code duplication and improving flexibility.

## When to Use It

Use the Decorator pattern when:

* You need to add responsibilities to individual objects without affecting others of the same class.
* You want to add behavior dynamically, at runtime.
* You want to avoid subclassing for every new feature combination.

Common use cases include logging, authentication, formatting, or adding user interface behaviors like scrollbars or borders.

## When NOT to Use It

Avoid this pattern when:

* You only need simple inheritance or static behavior that doesn’t change.
* The added complexity of multiple layers makes the code harder to read or debug.
* The functionality you're adding is better handled by a different design (like a strategy or observer).

## How It Works

The pattern includes:

1. **Component interface** – Defines the base behavior.
2. **Concrete component** – The original object being decorated.
3. **Decorator base class** – Wraps a component and delegates calls to it.
4. **Concrete decorators** – Extend the behavior of the component by overriding or adding methods.

Each decorator wraps another object, so you can chain multiple decorators to build up complex behavior.

## Real-World Analogy

Think of ordering a pizza. You start with a base (like a Margherita), then add toppings—mozzarella, olives, mushrooms. Each topping adds something new, but the base pizza stays the same. You don’t need a separate class for every combination of toppings—you just wrap the base with decorators.

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

### Example Usage:

```python
pizza = Mozzarella(Margherita())
print(pizza.get_description())  # Margherita, Mozzarella
print(pizza.get_cost())         # 15
```

Each decorator can be stacked to add more features.

## Learn More

You can explore the full implementation here:
[Decorator Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/structural/decorator.py)
