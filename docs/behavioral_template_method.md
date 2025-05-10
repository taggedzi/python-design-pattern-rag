# The Template Method Pattern (Behavioral)

## Purpose

The Template Method pattern defines the basic structure (or “template”) of an algorithm in a base class and allows subclasses to change specific steps of the algorithm without altering its overall flow.

## The Problem It Solves

Sometimes, different classes need to follow the same overall process but with slight variations in specific steps. Instead of rewriting the entire process for each class, this pattern lets you define the common parts once and let subclasses handle the parts that vary. This promotes code reuse and simplifies maintenance.

## When to Use It

Use this pattern when:

* You have multiple classes that share the same algorithm structure.
* Most of the behavior is common, but some steps need to be customized.
* You want to keep control over the overall process but allow flexibility in specific areas.

## When NOT to Use It

Avoid this pattern if:

* All the steps are so simple that subclassing adds unnecessary complexity.
* You end up needing to override most or all of the methods in the base class, making inheritance harder to manage.

## How It Works

The pattern involves:

1. **Abstract Class** – Defines the template method that outlines the steps of the algorithm. It may include:

   * **Base operations**: Common steps that shouldn’t be changed.
   * **Required operations**: Steps that subclasses must implement.
   * **Hooks**: Optional steps that subclasses can override if needed.
2. **Concrete Subclass** – Implements the required steps of the algorithm while using the shared structure provided by the template method.

## Real-World Analogy

Think of a cooking recipe. The recipe outlines the general process—gather ingredients, cook, and serve. However, the specific ingredients and cooking methods vary by dish. The recipe provides the template, and the chef (the subclass) fills in the details for each dish.

## Simplified Example

Here's a simple Python implementation:

```python
from abc import ABC, abstractmethod

class CookingRecipe(ABC):
    def prepare_meal(self) -> None:
        self.add_ingredients()
        self.cook()
        self.serve()
    
    @abstractmethod
    def add_ingredients(self) -> None:
        pass
    
    @abstractmethod
    def cook(self) -> None:
        pass
    
    def serve(self) -> None:
        print("Meal is ready to be served.")

class PizzaRecipe(CookingRecipe):
    def add_ingredients(self) -> None:
        print("Adding pizza ingredients.")
    
    def cook(self) -> None:
        print("Cooking the pizza.")

# Example usage
recipe = PizzaRecipe()
recipe.prepare_meal()
```

### Output

```text
Adding pizza ingredients.
Cooking the pizza.
Meal is ready to be served.
```

In this example, `prepare_meal()` is the template method. It defines the structure of the process, while the `PizzaRecipe` class customizes the steps for making a pizza.

## Learn More

To view the complete Python implementation, visit:
[Template Method Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/behavioral/template_method.py)
