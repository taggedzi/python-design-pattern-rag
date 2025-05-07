# The Bridge Pattern (Structural Design Patterns)

## Intent

The Bridge pattern is a design pattern designed to "decouple an abstraction from its implementation so that the two can vary independently". It's useful when you want to avoid permanent binding between abstraction and implementation.

## Problem It Solves

This pattern addresses the problem of having multiple orthogonal dimensions in your system. For example, if you have a UI component (abstraction) that needs to be rendered with different rendering methods (implementation), or if you need to switch from one type of storage to another (like database). 

## When to Use It

This pattern is especially effective when:

1. You want to avoid permanent binding between abstraction and implementation.
2. Your system has multiple orthogonal dimensions, like UI components that need different rendering methods or systems that need to switch from one type of storage to another. 
3. Changes at runtime should be easy and transparent.

## When NOT to Use It

Misuse of this pattern can lead to a high number of subclasses if not handled properly, which could make the code harder to maintain. Alternatives include using inheritance or composition instead of the Bridge pattern.

## How It Works

The Bridge pattern involves creating an abstraction and an implementation interface (Renderer in our case). The abstraction has a reference to the implementation object. This allows the two to vary independently, as shown in the example code.

Key classes or functions involved are:

1. Renderer - An abstract base class that defines the interface for concrete renderers.
2. VectorRenderer and RasterRenderer - Concrete implementations of the Renderer interface.
3. Shape - Abstract base class that has a reference to an object of the Renderer type. It provides the high-level operations, like draw().
4. Circle - Refined abstraction that implements the draw() method using the renderer's render_shape() method.
5. Example usage shows how to use different types of shapes with both vector and raster rendering methods.

## Real-World Analogy

Imagine you have a bridge connecting two islands, one for cars (abstraction) and another for boats (implementation). If the car side needs to be modified or replaced, it shouldn't affect the boat side. This is what Bridge pattern does - decouples the abstraction from its implementation so they can vary independently.

## Simplified Example

Here's a simplified version of our code:

```python
class Abstraction:
    def __init__(self, implementation):
        self.implementation = implementation
    
    def operation(self):
        return f"Abstraction: Base operation with:\n{self.implementation.operation_implementation()}"

class ConcreteImplementationA:
    def operation_implementation(self):
        return "ConcreteImplementationA: Here's the result on platform A."

# Example usage
if __name__ == "__main__":
    concrete_impl = ConcreteImplementationA()
    abstraction = Abstraction(concrete_impl)
    print(abstraction.operation())
```

## See Also

[bridge_pattern.py](https://github.<｜begin▁of▁sentence｜>/patterns/blob/master/python/structural/bridge.py