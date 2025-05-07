# The Decorator Pattern (Structural)

## Intent
The decorator pattern allows behavior to be added to individual objects, dynamically, without affecting the behavior of other objects from the same class. It's useful for adhering to the Open/Closed Principle.

## Problem It Solves
Imagine you have a bunch of classes that all share a common interface (Component). However, at some point in your application's lifecycle, you might need to extend or modify these objects' behavior without changing their class definition. This is where the decorator pattern comes into play. 

## When to Use It
The decorator pattern should be used when you want to add responsibilities to individual objects dynamically and transparently, that is, without affecting other objects from the same class.

## When NOT to Use It
If the additional responsibility added by the decorators doesn't need to be combined together or if it needs to be applied selectively, then a simpler alternative like simple inheritance might be more appropriate. 

## How It Works
The Decorator pattern involves a set of decorator classes that are used to wrap concrete components. The concrete component implements the core functionality while the decorators add additional responsibilities to the component. In this example, we have a Component interface with ConcreteComponent class and two types of Decorator: DecoratorA and DecoratorB.

## Real-World Analogy
Think about a bakery. You have basic bread (ConcreteComponent), but you also want it to be sweet (DecoratorA) or salty (DecoratorB). The decorators add additional flavor without changing the original bread class, adhering to the Open/Closed Principle.

## Simplified Example
Here's a simplified version of the code:
```python
class Component:  # Component interface
    def operation(self) -> str: pass

class ConcreteComponent(Component):  # Concrete component
    def operation(self) -> str: return "ConcreteComponent"

class Decorator(Component):  # Base decorator
    def __init__(self, component: Component) -> None: self._component = component
    def operation(self) -> str: return self._component.operation()

class DecoratorA(Decorator):  # Concrete decorators
    def operation(self) -> str: return f"DecoratorA({self._component.operation()})"

class DecoratorB(Decorator):  
    def operation(self) -> str: return f"DecoratorB({self._component.operation()})"
```
## See Also
You can find the full source file in the repository under [folder_name]/decorator_pattern.py

This pattern is also known as Wrapper, an alternative name for the Decorator pattern. It's a structural design pattern that allows behavior to be added to an individual object, either statically or dynamically, without affecting the behavior of other objects from the same class.

```python
if __name__ == "__main__":
    simple = ConcreteComponent()
    print("Simple:", simple.operation())

    decorated = DecoratorA(DecoratorB(simple))
    print("Decorated:", decorated.operation())
```
In this example, we have a basic bread (ConcreteComponent) which is wrapped in two decorators: one that makes it sweet (DecoratorA) and another that makes it salty (DecoratorB). The result is a piece of bread with both flavors without changing the original bread class. This demonstrates how the Decorator pattern allows for runtime modification of an object's behavior, adhering to the Open/Closed Principle.