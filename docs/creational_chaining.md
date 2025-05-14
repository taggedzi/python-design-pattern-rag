# The Chaining Pattern (Creational)

## Intent

The Chaining pattern lets you build complex objects step by step using a simple, readable API. It improves clarity and ease of use when creating objects with many options.

## Problem It Solves

Building objects with many attributes and methods can be hard to manage, especially when method order matters or impacts the object's state. The Chaining pattern simplifies this by allowing you to construct an object in a clear, step-by-step way.

## When to Use It

Use this pattern when creating complex objects with multiple settings, especially when construction order matters or when building the object gradually is easier than setting everything at once.

## When Not to Use It

Avoid this pattern for simple objects or when there's no need for a specific construction order. It adds unnecessary complexity in such cases.

## How It Works

Each method in the chain returns the same object (`self`), so you can call methods one after another. This fluent interface continues until a final `build()` method returns the complete object.

## Real-World Analogy

Think of building a castle: you lay the foundation, then add walls, windows, doors, and so on. Each step contributes to the final structure. The Chaining pattern works the same way—each method adds to the final object.

## Simplified Example

```python
class Pizza:
    def __init__(self):
        self.size = None
        self.crust = None
        self.toppings = []
        self.sauce = None
        self.cheese = True

    def __str__(self):
        return (f"Pizza(size={self.size}, crust={self.crust}, "
                f"toppings={self.toppings}, sauce={self.sauce}, cheese={self.cheese})")


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self

    def set_crust(self, crust):
        self.pizza.crust = crust
        return self

    def add_topping(self, topping):
        self.pizza.toppings.append(topping)
        return self

    def set_sauce(self, sauce):
        self.pizza.sauce = sauce
        return self

    def no_cheese(self):
        self.pizza.cheese = False
        return self

    def build(self):
        return self.pizza


# Example usage
pizza = (PizzaBuilder()
         .set_size("large")
         .set_crust("thin")
         .add_topping("pepperoni")
         .add_topping("olives")
         .set_sauce("tomato")
         .no_cheese()
         .build())

print(pizza)
```

This example builds a large stuffed-crust pizza with pepperoni and mushrooms, barbecue sauce, and no cheese. The `build()` method returns the final pizza object.

## See Also

For the full implementation, see the [Chaining Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/creational/chaining.py).
