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
This code demonstrates the Bridge design pattern, decoupling the rendering of shapes from their implementation. It includes abstract classes for Renderer and Shape, with concrete implementations for VectorRenderer and RasterRenderer. The Circle class is a refined abstraction that uses these renderers to draw shapes.

## Docstrings
- Decorator interface for rendering shapes.

- `render_shape(shape: str) -> str`: Renders a given shape as lines or pixels.
- Concrete implementation of Renderer that renders shapes as lines.

- `render_shape(shape: str) -> str`: Returns a string indicating the drawing of the shape as lines.
- Concrete implementation of Renderer that renders shapes as pixels.

- `render_shape(shape: str) -> str`: Returns a string indicating the drawing of the shape as pixels.
- Abstract base class for shapes.

- `__init__(renderer: Renderer) -> None`: Initializes the shape with a renderer.
- `draw() -> str`: Draws the shape using the provided renderer.
- Concrete implementation of Shape that draws a circle.

- `draw() -> str`: Returns a string indicating the drawing of a circle using the provided renderer.

