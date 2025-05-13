# The Template Method Pattern (Behavioral)

## Purpose

The Template Method pattern defines the overall structure of an algorithm in a base class and allows subclasses to change specific steps without altering the overall process. This supports code reuse and enforces a consistent flow while allowing flexibility where needed.

## Problem It Solves

Often, multiple classes follow the same general process but differ slightly in how specific steps are done. Instead of duplicating the full process in each class, the Template Method pattern lets you define the shared logic once in a base class and let subclasses handle the parts that vary. This keeps your code clean and easier to maintain.

## When to Use It

Use this pattern when:

* You have several classes that follow the same general algorithm.
* The overall structure should stay the same, but specific steps may vary.
* You want to share logic across classes while allowing customization.

## When Not to Use It

Avoid this pattern if:

* Each step is very simple and duplicating the logic is more straightforward.
* You find yourself overriding most of the base class methods—inheritance might not be the best fit.

## How It Works

The pattern includes:

1. **Abstract Class** – Defines a template method that outlines the full process. It usually includes:

   * **Base operations**: Shared steps that shouldn’t be changed.
   * **Required operations**: Abstract methods that must be implemented by subclasses.
   * **Hooks**: Optional methods that can be overridden if needed.
2. **Concrete Subclass** – Implements the specific steps while reusing the overall structure from the abstract class.

## Real-World Analogy

Think of a recipe. It defines a standard cooking process: gather ingredients, cook, and serve. While the steps are the same, each dish has different ingredients and cooking methods. The recipe is the template; the chef customizes it to make different meals.

## Simplified Example

Here's a basic Python example:

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
```

### Usage

```python
recipe = PizzaRecipe()
recipe.prepare_meal()
```

### Output

```text
Adding pizza ingredients.
Cooking the pizza.
Meal is ready to be served.
```

In this example, `prepare_meal()` is the template method. It controls the flow, while `PizzaRecipe` fills in the specific steps.

## Learn More

See the complete Python implementation here:
[Template Method Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/behavioral/template_method.py)
