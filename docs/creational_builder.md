# The Builder Pattern (Creational)

## Purpose

The Builder pattern helps construct complex objects step by step. It separates how an object is made from the final product, allowing you to create different variations using the same construction process.

## Problem It Solves

Some objects are too complex to build all at once—for example, a house that requires a foundation, walls, windows, and furniture. You might want to build different versions, like a basic model or a luxury one. The Builder pattern lets you create these step by step with consistent structure while still supporting variations.

## When to Use It

Use this pattern when:

* An object has many parts or steps in its construction.
* You want to reuse the construction process to build different results.
* You want to keep the construction logic separate from the object itself.

## When Not to Use It

Avoid this pattern if:

* The object is simple and doesn’t need multiple steps.
* There’s only one fixed way to build the object.
* Introducing builders would make the code more complex than necessary.

## How It Works

The Builder pattern has four main parts:

1. **Product** – The object that’s being built.
2. **Builder** – Defines the steps for building parts of the product.
3. **ConcreteBuilder** – Implements the building steps and assembles the product.
4. **Director** – Controls the order and combination of steps to create the product.

The client sets up the builder and director, and the director manages the build sequence.

## Real-World Analogy

Building a house follows a plan (builder interface), with a contractor (concrete builder) performing the work. The construction manager (director) decides when each part—foundation, walls, roof—is added. The builder follows those instructions to complete the house.

## Simplified Example

```python
from abc import ABC, abstractmethod

# Builder interface
class Builder(ABC):
    @abstractmethod
    def build_part_a(self): pass

    @abstractmethod
    def build_part_b(self): pass

    @abstractmethod
    def get_product(self): pass

# Concrete builder
class ConcreteBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Product()

    def build_part_a(self):
        self._product.add("PartA")

    def build_part_b(self):
        self._product.add("PartB")

    def get_product(self):
        product = self._product
        self.reset()
        return product

# Product
class Product:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        return ", ".join(self.parts)

# Director
class Director:
    def __init__(self, builder: Builder):
        self._builder = builder

    def build_minimal_viable_product(self):
        self._builder.build_part_a()

    def build_full_featured_product(self):
        self._builder.build_part_a()
        self._builder.build_part_b()

# Usage
builder = ConcreteBuilder()
director = Director(builder)

director.build_minimal_viable_product()
print("Minimal product:", builder.get_product().list_parts())

director.build_full_featured_product()
print("Full product:", builder.get_product().list_parts())
```

### Output

```
Minimal product: PartA
Full product: PartA, PartB
```

## Learn More

See the full implementation and more examples here:
[Builder Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/creational/builder.py)
