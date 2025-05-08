# The Template Method Pattern (Behavioral)

## Intent

The Template Method pattern is a behavioral design pattern that defines the program skeleton of an algorithm in an operation, deferring some steps to subclasses. It allows subclasses to redefine certain steps of an algorithm without changing its structure.

## Problem It Solves

This pattern addresses the problem of having algorithms with varying implementations and structures. Rather than forcing a client to use one specific implementation or structure, it provides a base template that clients can fill in with their own behavior. This separation allows for greater flexibility and reusability across different scenarios.

## When to Use It

The Template Method pattern is suitable when you have an algorithm composed of steps that are common to all subclasses but may require different or additional implementation by each subclass.

## When NOT to Use It

It's not a good idea to use the Template Method pattern if:

1. The operations to be performed are simple and do not vary between subclasses.
2. You need to override every single method in the base class, which can lead to code that is hard to maintain.

## How It Works

The main component of this pattern is an abstract base class (AbstractClass) that defines a template method (template_method). This template method includes calls to other methods:

- Base operations (base_operation_1 and base_operation_2), which are called by the template method. These represent the invariant parts of the algorithm.
- Required operations (required_operations_1 and required_operations_2), which must be implemented by subclasses. These represent the variant parts of the algorithm.
- Hooks (hook_1 and hook_2) are optional methods that can be overridden in subclasses to provide additional behavior before or after certain steps in the template method.

Subclasses then extend AbstractClass, providing their own implementations for the required operations. The template method is invoked by calling it on an instance of a concrete subclass.

## Real-World Analogy

You can think of the Template Method pattern as a recipe. It defines the steps to cook a meal (the template method), with some ingredients being common and others specific to each dish (base operations, required operations). The chef (client) fills in the blanks by providing their own preparation methods for each step.

## Simplified Example

Here's a simplified example of how you might use this pattern:

```python
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
recipe.prepare_meal()  # Outputs: Adding pizza ingredients., Cooking the pizza., Meal is ready to be served.
```

## See Also

You can find the full implementation of this pattern in the Python file [here](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/behavioral/template_method.py) in our GitHub repository.