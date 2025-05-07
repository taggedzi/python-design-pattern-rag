---
file: structural/bridge.py
chunk: structural_bridge.md
---

```python
"""
Structural Pattern: Bridge

Decouples an abstraction from its implementation so that the two can vary independently.
Useful when you want to avoid a permanent binding between abstraction and implementation.
"""

from abc import ABC, abstractmethod

# Implementation interface
class Renderer(ABC):
    @abstractmethod
    def render_shape(self, shape: str) -> str:
        pass

# Concrete implementations
class VectorRenderer(Renderer):
    def render_shape(self, shape: str) -> str:
        return f"Drawing {shape} as lines."

class RasterRenderer(Renderer):
    def render_shape(self, shape: str) -> str:
        return f"Drawing {shape} as pixels."

# Abstraction
class Shape(ABC):
    def __init__(self, renderer: Renderer) -> None:
        self.renderer = renderer

    @abstractmethod
    def draw(self) -> str:
        pass

# Refined abstraction
class Circle(Shape):
    def draw(self) -> str:
        return self.renderer.render_shape("Circle")

# Example usage
if __name__ == "__main__":
    vector = VectorRenderer()
    raster = RasterRenderer()

    circle_vector = Circle(vector)
    circle_raster = Circle(raster)

    print(circle_vector.draw())
    print(circle_raster.draw())

```

## Summary
This code demonstrates the Bridge design pattern, which decouples an abstraction from its implementation. It shows how different rendering strategies (Vector and Raster) can be applied to a Shape abstraction.

## Docstrings
- Decouples an abstraction from its implementation so that the two can vary independently.
- Useful when you want to avoid a permanent binding between abstraction and implementation.
- Interface for rendering shapes.
- Concrete implementation that renders shapes as lines.
- Concrete implementation that renders shapes as pixels.
- Abstract base class for shapes.
- Concrete shape that draws as a circle using the provided renderer.
- Example usage of the Bridge pattern.

