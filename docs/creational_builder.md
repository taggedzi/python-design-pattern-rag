# The Builder Pattern (Creational)

## Purpose

The Builder pattern helps you construct complex objects step by step. It separates the construction process from the final product, making it easier to create different versions or configurations of the same type of object.

## The Problem It Solves

Sometimes an object is too complex to create in one step—like building a house with a foundation, walls, windows, and furniture. You might want different versions of the house, such as a basic layout or a luxury model. The Builder pattern lets you construct such objects gradually, using a consistent process, while still allowing flexibility in the final result.

## When to Use It

Use the Builder pattern when:

* You need to build complex objects with many parts.
* You want to reuse the same construction process for different representations.
* You want to isolate the construction logic from the actual product.

## When NOT to Use It

Avoid this pattern if:

* The object is simple and doesn’t require step-by-step construction.
* You only ever need one version of the object, and its structure rarely changes.
* Adding builders introduces unnecessary complexity for your use case.

## How It Works

The pattern has four key components:

1. **Product** – The final object being built (e.g., a house).
2. **Builder** – Defines methods to build each part of the product (e.g., walls, windows).
3. **ConcreteBuilder** – Implements the builder’s steps to build and assemble parts of the product.
4. **Director** – Controls the construction process and calls builder methods in a specific order.

The **Client** sets up the builder and director, then triggers the construction.

## Real-World Analogy

Think of building a house. You use a blueprint (the builder interface), hire a contractor (the concrete builder), and follow a schedule (the director) to build it step by step. The builder adds pieces like the foundation, walls, and roof. The director decides what to build first and when.

## Simplified Example

```python
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

# Example usage
builder = ConcreteBuilder()
director = Director(builder)

director.build_minimal_viable_product()
print("Minimal product:", builder.get_product().list_parts())

director.build_full_featured_product()
print("Full product:", builder.get_product().list_parts())
```

### Output

```text
Minimal product: PartA
Full product: PartA, PartB
```

## Learn More

For a full implementation and examples, check:
[Builder Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/creational/builder.py)
