# The Decorator Pattern (Structural)

## Intent

The decorator pattern allows behavior to be added to an individual object, either statically or dynamically, without affecting the behavior of other objects from the same class. It's useful for adhering to the Open/Closed Principle.

## Problem It Solves

Imagine you have a component that needs some additional functionality. You could subclass it and add the new functionality, but this can lead to a lot of code duplication if you need many variations on the same functionality. The decorator pattern allows you to add such functionality without having to modify the original object or subclasses.

## When to Use It

The decorator pattern is useful in situations where you want to add responsibilities to objects dynamically and transparently, that is, without affecting other objects of a class. For example, when you need to add logging, caching, or transactional behavior to individual objects at run-time.

## When NOT to Use It

The decorator pattern should be used sparingly as it can make code more complex and harder to understand if overused or misapplied. Avoid using the pattern when you want to add responsibilities that are orthogonal, unrelated, or not expected in advance.

## How It Works

In the Decorator pattern, there's a base component class with an operation() method. This is the object we want to add additional behavior to. There's also a decorator class that has a reference to a Component and implements the same interface. The concrete decorators (DecoratorA and DecoratorB) are examples of these, adding specific behaviors to the objects they decorate.

## Real-World Analogy

Imagine you have a pizza place where you can add different toppings to your pizza. Each topping is like a decorator - it adds an extra bit of functionality (like cheese or pepperoni) without affecting the base pizza itself. The same concept applies in software development: each additional piece of functionality is like a decorator, adding behavior that's orthogonal and unrelated to other behaviors.

## Simplified Example

Here's a simplified example of how this might look:

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

# Base Decorator
class PizzaDecorator(Pizza):
    def __init__(self, pizza: Pizza) -> None:
        self.pizza = pizza

    def get_cost(self):
        return self.pizza.get_cost()

    def get_description(self):
        return self.pizza.get_description()

# Concrete decorators
class Mozzarella(PizzaDecorator):
    def __init__(self, pizza: Pizza) 
        super().__init__(pizza)

    def get_cost(self):
        return self.pizza.get_cost() + 5

    def get_description(self):
        return f"{self.pizza.get_description()}, Mozzarella"
```

In this example, `Margherita` is the component (the pizza we're adding toppings to), and `Mozzarella` is a decorator that adds cheese to our pizza. The cost of the pizza increases by $5 with each piece of mozzarella added.

## See Also

The Python code for this lesson can be found [here](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/structural/decorator.py).