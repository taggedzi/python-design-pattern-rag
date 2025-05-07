# The Factory Pattern (Creational)

## Intent
The factory pattern provides an interface for creating objects, but allows subclasses to alter the type of objects that will be created. This pattern promotes loose coupling between client and object creation logic.

## Problem It Solves
In software design, we often have a need to create complex objects with many dependencies. The problem is that such objects are hard to instantiate because they require specific configurations or setup steps. A factory pattern solves this by providing an interface for creating these objects but hiding the details of how the object is created from clients.

## When to Use It
The Factory Pattern should be used in situations where we want to abstract away the creation logic and provide a simple, unified way to create objects without exposing too much detail about what's happening under the hood. Factories are commonly used when dealing with configuration settings or external dependencies. 

## When NOT to Use It
Factory pattern should not be overused as it can make code harder to understand and maintain. If a simple `new` call would do, then there is no need for a Factory class.

## How It Works
The factory method in the Creator class defines an interface for creating objects but lets subclasses alter the type of objects that will be created. The ConcreteCreators override this method to return specific types of Product objects. 

## Real-World Analogy
Imagine you are a bakery owner and you have multiple kinds of pastries (Products) like cake, muffin, etc. You don't know exactly how each pastry is made but you provide an interface for ordering the pastries through your shop (Creator). Customers can order any type of pastry they want without knowing about the underlying manufacturing process.

## Simplified Example
```python
class Creator:
    def factory_method(self):
        pass
    
    def some_operation(self):
        product = self.factory_method()
        return f"Creator: Working with {product}"
        
class ConcreteCreator(Creator):
    def factory_method(self):
        return "ConcreteProduct"
```
In the above example, `some_operation` in Creator class uses `factory_method` to create a product. The actual creation of the product is delegated to subclasses like ConcreteCreator.

## See Also
[Factory Pattern Python Code](https://github.com/your-repo/python-design-patterns/blob/main/creational/factory.py)
___
```
"""
Creational Pattern: Factory Method

Defines an interface for creating an object but lets subclasses alter the type of objects that will be created.
This pattern promotes loose coupling between client and object creation logic.
"""

from abc import ABC, abstractmethod

class Product(ABC):
    """Abstract Product interface."""

    @abstractmethod
    def operation(self) -> str:
        pass

class ConcreteProductA(Product):
    def operation(self) -> str:
        return "Result from ConcreteProductA"

class ConcreteProductB(Product):
    def operation(self) -> str:
        return "Result from ConcreteProductB"

class Creator(ABC):
    """Abstract Creator class that declares the factory method."""

    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        return f"Creator: Working with {product.operation()}"

class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()
"""
Example usage
if __name__ == "__main__":
    for creator in (ConcreteCreatorA(), ConcreteCreatorB()):
        print(creator.some_operation())
"""
```
___
This lesson is designed to be beginner-friendly and easy to understand, making it a great starting point for anyone new to design patterns or Python programming.