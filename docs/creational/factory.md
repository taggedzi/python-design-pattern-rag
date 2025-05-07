# The Factory Pattern (Creational)

# The Factory Method Pattern (Creational)

## Intent

The Factory Method pattern provides a way to delegate the instantiation logic to child classes. It promotes loose coupling between client code and concrete product classes, which can be beneficial in large-scale applications where object creation might involve complex steps or dependencies. 

## Problem It Solves

It addresses the problem of creating objects without exposing the instantiation logic to the client. This allows subclasses to alter the type of objects that will be created, leading to more flexible and maintainable code.

## When to Use It

This pattern is particularly effective when:
- A class can't anticipate the type of objects it needs to create at runtime.
- The class wants its subclasses to specify the objects it creates.
- The class delegates responsibility to one of several helper subclasses, and you want to localize that responsibility to a single class.

## When NOT to Use It

Misuse of this pattern can lead to an inflexible system where object creation logic is hardcoded within the base class. Alternatives might be simpler patterns like Simple Factory or Abstract Factory if the client code needs more control over instantiation.

## How It Works

The Factory Method pattern involves a set of factory classes, each responsible for creating one specific product type. The abstract Creator class declares a `factory_method` that returns a Product object. Concrete creators override this method to return the appropriate concrete product. 

In the given Python code, `Creator` is the abstract base class with an abstract factory method and some core business logic. Two specific creator classes (`ConcreteCreatorA` and `ConcreteCreatorB`) inherit from it and override the factory method to return instances of `ConcreteProductA` or `ConcreteProductB` respectively.

## Real-World Analogy

Imagine a pizza restaurant that serves different types of pizzas based on customer orders. The kitchen (the Factory Method pattern) can prepare any type of pizza, but the waiter (the client code) only knows how to order and receive pizzas from the restaurant's menu. 

## Simplified Example

Here is a simplified pseudocode representation:

```python
class Creator:
    def create_product(self):
        pass
    
    def use_product(self):
        product = self.create_product()
        return f"Using {product}"
        
class ConcreteCreatorA(Creator):
    def create_product(self):
        return "Product A"
```

## See Also

You can find the full source file for this pattern in the `creational/factory_method.py` file of the repository.

This example demonstrates how to use the Factory Method pattern effectively, promoting loose coupling between client code and object creation logic. It's a useful pattern for large-scale applications where object instantiation might be complex or needs customization based on runtime conditions.