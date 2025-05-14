# The Bridge Pattern (Structural)

## Purpose

The Bridge pattern separates an abstraction from its implementation so they can evolve independently. It helps reduce tight coupling between what something does (the abstraction) and how it does it (the implementation).

## Problem It Solves

Suppose you're building shapes like circles and squares that can be rendered in different styles—using pixels, lines, or other methods. Without the Bridge pattern, you’d need separate classes for every combination, such as `PixelCircle`, `LineCircle`, `PixelSquare`, and so on. This quickly becomes unmanageable. The Bridge pattern avoids this by allowing you to mix and match shapes and renderers at runtime without creating many subclasses.

## When to Use It

Use this pattern when:

* You want to avoid an explosion of subclasses due to combinations of features.
* You need to change the implementation independently of the abstraction.
* You want to add flexibility by assigning different behaviors to shared logic.

## When Not to Use It

Avoid this pattern if:

* The abstraction and implementation are already tightly bound and unlikely to change.
* Adding the pattern would overcomplicate a simple design.

## How It Works

The Bridge pattern splits a class into two parts:

1. **Abstraction** – Represents the high-level concept (e.g., a shape).
2. **Implementor** – Handles the low-level details (e.g., rendering style).

The abstraction holds a reference to the implementor, so you can easily swap out implementations without modifying the abstraction.

## Real-World Analogy

Think of a TV remote. The remote (abstraction) sends commands, while the TV (implementation) carries them out. You can change the remote or the TV model independently—as long as they support the same basic operations.

## Simplified Example

Here’s a basic Python example:

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
```

### Usage

```python
circle = Shape("Circle", VectorRenderer())
print(circle.draw())  # Output: Drawing Circle as lines

square = Shape("Square", RasterRenderer())
print(square.draw())  # Output: Drawing Square as pixels
```

In this example:

* `Shape` is the abstraction.
* `Renderer` defines the rendering interface.
* `VectorRenderer` and `RasterRenderer` are implementations of that interface.
* You can pair any shape with any renderer without changing their internal code.

## Learn More

See the full Python implementation here:
[Bridge Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/structural/bridge.py)
