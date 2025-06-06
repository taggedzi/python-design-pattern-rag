---
file: creational/chaining.py
chunk: creational_chaining.md
---

```python
"""A Creational Design Pattern using Method Chaining and Fluent Interface

PizzaBuilder Demo:
This script demonstrates the Builder Pattern with method chaining to configure
a customizable pizza object. It includes validation, undo functionality, and is ideal
for teaching fluent interface and creational design principles in Python.
"""
import copy
import unittest

class PizzaBuilder:
    """
    A builder class for constructing a pizza using method chaining.
    This demonstrates a Fluent Interface and the Builder Pattern (Creational).
    """
    def __init__(self):
        self.size = None
        self.crust = None
        self.toppings = []
        self.cheese = True
        self.sauce = "tomato"
        self._history = []  # Stack to keep track of history for undo functionality

    def _save_state(self):
        """Save a deep copy of the current state to support undo functionality."""
        self._history.append(copy.deepcopy(self.__dict__))

    def undo(self):
        """
        Revert the last action taken on the builder.
        Useful to backtrack if a mistake is made in the chain.
        """
        if not self._history:
            raise RuntimeError("No actions to undo.")
        self.__dict__ = self._history.pop()
        return self

    def set_size(self, size):
        """
        Set the pizza size.
        Valid sizes: 'small', 'medium', 'large'.
        """
        if size not in ["small", "medium", "large"]:
            raise ValueError("Size must be 'small', 'medium', or 'large'")
        self._save_state()
        self.size = size
        return self

    def set_crust(self, crust):
        """
        Set the crust type.
        Valid options: 'thin', 'thick', 'stuffed'.
        """
        if crust not in ["thin", "thick", "stuffed"]:
            raise ValueError("Crust must be 'thin', 'thick', or 'stuffed'")
        self._save_state()
        self.crust = crust
        return self

    def add_topping(self, topping):
        """
        Add a topping to the pizza.
        Raises an error if the topping is already added.
        """
        if topping in self.toppings:
            raise ValueError(f"Topping '{topping}' already added.")
        self._save_state()
        self.toppings.append(topping)
        return self

    def no_cheese(self):
        """Remove cheese from the pizza."""
        self._save_state()
        self.cheese = False
        return self

    def set_sauce(self, sauce):
        """Set the sauce type (e.g., tomato, bbq, pesto)."""
        if not sauce:
            raise ValueError("Sauce cannot be empty.")
        self._save_state()
        self.sauce = sauce
        return self

    def build(self):
        """
        Finalize and return the constructed pizza as a dictionary.
        Validates that required fields (size, crust) are set.
        """
        if not all([self.size, self.crust]):
            raise ValueError("Size and crust must be specified.")
        return {
            "size": self.size,
            "crust": self.crust,
            "toppings": self.toppings,
            "cheese": self.cheese,
            "sauce": self.sauce
        }

if __name__ == "__main__":
    # Example usage of the PizzaBuilder with method chaining
    pizza_demo = (
        PizzaBuilder()
        .set_size("large")
        .set_crust("stuffed")
        .add_topping("pepperoni")
        .add_topping("mushrooms")
        .set_sauce("bbq")
        .no_cheese()
        .build()
    )
    print(pizza_demo)

```

## Summary
A Creational Design Pattern using Method Chaining and Fluent Interface

PizzaBuilder Demo:
This script demonstrates the Builder Pattern with method chaining to configure a customizable pizza object. It includes validation, undo functionality, and is ideal for teaching fluent interface and creational design principles in Python.

## Docstrings
- A builder class for constructing a pizza using method chaining. This demonstrates a Fluent Interface and the Builder Pattern (Creational).
- Save a deep copy of the current state to support undo functionality.
- Revert the last action taken on the builder. Useful to backtrack if a mistake is made in the chain.
- Set the pizza size. Valid sizes: 'small', 'medium', 'large'.
- Set the crust type. Valid options: 'thin', 'thick', 'stuffed'.
- Add a topping to the pizza. Raises an error if the topping is already added.
- Remove cheese from the pizza.
- Set the sauce type (e.g., tomato, bbq, pesto).
- Finalize and return the constructed pizza as a dictionary. Validates that required fields (size, crust) are set.

