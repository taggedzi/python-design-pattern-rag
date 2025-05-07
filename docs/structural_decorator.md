# The Decorator Pattern (Structural)

## Intent
The Decorator pattern allows behavior to be added to individual objects, dynamically, without affecting the behavior of other objects from the same class. This is useful for adhering to the Open/Closed Principle.

## Problem It Solves
Without changing the original object's code, we can extend its functionality by wrapping it with an additional wrapper that contains the added behavior.

## When to Use It
This pattern should be used when you want to add new behavior to objects without affecting other instances of the same class. It is also useful in situations where many different combinations of optional behaviors are needed at runtime, for example, UI components with different decorators applied.

## When NOT to Use It
The Decorator pattern may not be suitable if the added responsibilities are too numerous or complex, and it's better to create a new subclass just for that purpose. Also, avoid using this pattern when you want to remove some behavior from an object at runtime.

## How It Works
In the Decorator pattern, there are three main components: 
1. Component interface with abstract method `operation()`.
2. Concrete component class implementing the operation method.
3. Base decorator class which wraps a component and implements the same interface as the wrapped object. The base decorator forwards all requests to its component.
4. Concrete decorators, extending the base decorator, adding new behavior before or after forwarding the request to the wrapped object.

## Real-World Analogy
Imagine a pizza ordering system where you can add extra toppings like cheese, olives etc., without changing the basic pizza dough. Each additional topping is a decorator that adds its own behavior while still maintaining the interface of the base pizza (component).

## Simplified Example
Here's a simplified example:
```python
class Pizza:  # Component Interface
    def get_cost(self):
        pass

    def get_ingredients(self):
        pass

class Margherita(Pizza):  # Concrete component
    def get_cost(self):
        return 10

    def get_ingredients(self):
        return ['mozzarella', 'tomatoes']

class PizzaDecorator(Pizza):  # Base Decorator
    def __init__(self, pizza):
        self.pizza = pizza

    def get_cost(self):
        return self.pizza.get_cost()

    def get_ingredients(self):
        return self.pizza.get_ingredients()

class ExtraCheese(PizzaDecorator):  # Concrete decorators
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_cost(self):
        return self.pizza.get_cost() + 2

    def get_ingredients(self):
        return self.pizza.get_ingredients() + ['extra cheese']
```
## See Also
The Python code for this lesson can be found [here](https://github.<｜begin▁of▁sentence｜>/