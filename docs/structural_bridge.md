# The Bridge Pattern (Structural)

## Purpose

The Bridge pattern is used to separate an abstraction from its implementation, so that both can evolve independently. It helps reduce tight coupling between code that defines what something does (abstraction) and code that defines how it does it (implementation).

## The Problem It Solves

Imagine you’re building shapes (like circles and squares) that can be rendered in different ways (like using pixels or lines). Without the Bridge pattern, you'd need a separate class for every combination—`PixelCircle`, `LineCircle`, `PixelSquare`, and so on. This quickly becomes unmanageable as the number of shapes and renderers grows. The Bridge pattern solves this by allowing shapes and renderers to be combined flexibly at runtime.

## When to Use It

Use the Bridge pattern when:

* You want to avoid creating a large number of subclasses to support combinations of features.
* You want to be able to change the implementation details without touching the abstraction.
* You need flexibility in assigning different behaviors (implementations) to high-level logic (abstractions).

## When NOT to Use It

Avoid this pattern if:

* The abstraction and implementation are already tightly bound and unlikely to change.
* Introducing the pattern would add unnecessary complexity to a simple design.

## How It Works

The Bridge pattern breaks a class into two parts:

1. **Abstraction** – The high-level control or logic (e.g., a shape like `Circle`).
2. **Implementor** – The low-level implementation (e.g., how the shape is rendered).

The abstraction holds a reference to the implementor. This means you can swap out implementations without modifying the abstraction.

## Real-World Analogy

Think of a remote control (abstraction) that can operate different types of TVs (implementation). The remote sends commands, but the way the TV responds depends on the model. You can change the TV or the remote without having to redesign the other.

## Simplified Example

Here’s a simple Python implementation:

```python
# Implementor
class Renderer:
    def what_to_render(self):
        raise NotImplementedError

class VectorRenderer(Renderer):
    def what_to_render(self):
        return "lines"

class RasterRenderer(Renderer):
    def what_to_render(self):
        return "pixels"

# Abstraction
class Shape:
    def __init__(self, name, renderer: Renderer):
        self.name = name
        self.renderer = renderer

    def draw(self):
        return f"Drawing {self.name} as {self.renderer.what_to_render()}"

# Usage
circle = Shape("Circle", VectorRenderer())
print(circle.draw())  # Drawing Circle as lines

square = Shape("Square", RasterRenderer())
print(square.draw())  # Drawing Square as pixels
```

In this example:

* `Shape` is the abstraction.
* `Renderer` is the implementation interface.
* `VectorRenderer` and `RasterRenderer` are concrete implementations.
* The `Shape` can work with any renderer.

## Learn More

You can find the full implementation in Python here:
[Bridge Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/structural/bridge.py)
