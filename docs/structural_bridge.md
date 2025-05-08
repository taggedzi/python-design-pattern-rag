# The Bridge Pattern (Structural)

## Intent

The Bridge pattern is a design pattern designed to "decouple an abstraction from its implementation so that the two can vary independently". It's useful when you want to avoid permanent binding between abstraction and implementation, which means one shouldn't have to change the other.

## Problem It Solves

Imagine you are designing a software system where there are different ways of rendering shapes (e.g., as lines or pixels). The problem is that this could lead to tight coupling if every shape has its own renderer, making it hard to add new shapes without modifying existing ones. This pattern helps to decouple the abstraction from the implementation so they can vary independently.

## When to Use It

The Bridge Pattern should be used when you want to abstract and separate the implementation details from the high-level interface or abstraction, which makes them independent of each other.

## When NOT to Use It

You shouldn't use the Bridge pattern if the "abstraction" and "implementation" are too tightly coupled. The key idea is that they should be able to vary independently, so a change in one should not require a change in the other.

## How It Works

The Bridge Pattern involves an Abstraction (Shape) which has a reference to its Implementor (Renderer). This allows for different implementations of Renderer and Shape can use any implementation at runtime.

## Real-World Analogy

You could think of the Bridge pattern as a road bridge that connects two different types of roads (abstractions) with varying degrees of difficulty to navigate (implementations). The bridge itself is designed in such a way that it allows both types of vehicles to pass through, without having to change either type.

## Simplified Example

Here's a simplified example:

```python
class Shape:  # Abstraction
    def __init__(self, renderer):
        self.renderer = renderer  # Implementor

    def draw(self):
        pass

class Circle(Shape):  # Refined abstraction
    def draw(self):
        return f"Drawing {self.name} as {self.renderer.what_to_render()}"

class Renderer:  # Implementor
    @staticmethod
    def what_to_render():
        pass

class VectorRenderer(Renderer):  # Concrete implementor
    @staticmethod
    def what_to_render():
        return "lines"

class RasterRenderer(Renderer):  # Another concrete implementor
    @staticmethod
    def what_to_render():
        return "pixels"
```

## See Also

The corresponding Python file can be found [here](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/structural/bridge.py).
