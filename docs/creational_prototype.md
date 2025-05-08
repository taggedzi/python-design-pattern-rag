# The Prototype Pattern (Creational)

## Intent

The prototype pattern is a creational design pattern that allows cloning objects, even complex ones, without coupling to their specific classes. This pattern provides a mechanism for creating object instances via cloning an existing instance and changing its internal state.

## Problem It Solves

This pattern addresses the problem of creating new objects by copying an existing one. The complexity can be high if we have to create complex objects with many dependencies, or if creation is time-consuming. This pattern allows us to define a prototype object that acts as a blueprint for creating other objects.

## When to Use It

The Prototype Pattern should be used when:

1. We need to create an instance of a class at runtime based on some configuration or parameters.
2. The class instances are expensive in terms of resources and time, we have a similar object ready that can be cloned instead of creating new one from scratch.
3. When the classes to instantiate are specified at run-time, for example, through a user interface or config file.

## When NOT to Use It

The Prototype Pattern should not be used when:

1. The class is simple and does not have many fields that need setting.
2. If the objects are immutable. In this case, we can use simpler creation patterns like Factory Method or Builder.
3. If a class has a complex initialization process. In such cases, it might be better to use Constructor-based instantiation.

## How It Works

The Prototype Pattern works by defining an interface for creating objects that is implemented by the actual classes. The `clone()` method in the prototype class returns a deep copy of itself which can then be modified as required.

## Real-World Analogy

Imagine you have a blueprint (prototype) of a house. You can use this blueprint to build many houses, each with its unique features and decorations. The blueprint acts as the prototype from where new houses are built by cloning it.

## Simplified Example

Here's an example in Python:

```python
class Shape(Prototype):
    def  __init__(self, color: str, position: tuple[int, int]) -> None:
        self.color = color
        self.position = position

    def move(self, dx: int, dy: int) -<｜begin▁of▁sentence｜> None:
        x, y = self.position
        self.position = (x + dx, y + dy)

    def  __str__(self) -> str:
        return f"Shape(color={self.color}, position={self.position})"
```

In this example, `Shape` is a subclass of the `Prototype` class and it overrides the `clone()` method to create a deep copy of itself.

## See Also

You can find the full implementation of the Prototype pattern in the Python file [here](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/creational/prototype.py) in our GitHub repository.
