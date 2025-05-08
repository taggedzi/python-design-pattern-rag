# The Builder Pattern (Creational)

## Intent

The Builder pattern is a design pattern designed to provide a flexible solution to various object creation problems in object-oriented programming. It allows constructing complex objects step by step.

## Problem It Solves

Imagine you are building a complex house, say with multiple rooms and furniture. You don't want to build everything at once because it can take forever and your budget is tight. Instead, you start with the foundation (maybe just the basement), then gradually add more as you need them. This process of constructing an object step by step is what the Builder pattern solves for.

## When to Use It

The Builder pattern should be used when:

1. You want your code to be able to create different representations of some product (for example, stone and wooden houses).
2. The construction process must allow different representations for the product that are implemented in various subclasses.
3. You need a simple interface to create complex objects.

## When NOT to Use It

The Builder pattern is not suitable when:

1. The object creation algorithm can be defined once and does not get changed often.
2. The client code should be simplified, without being overly complicated by the builder pattern.
3. You need a simple interface that creates only complex objects.

## How It Works

The Builder pattern works with four roles: Product, Builder, Director, and Client.

1. **Product**: This is the object we are building. In our house example, it's the entire house.
2. **Builder**: This defines an interface for creating parts of a product. In our house example, this could be adding rooms or furniture to the house.
3. **Director**: This constructs an object using the Builder interface. It knows what part to build and in which order. In our house example, it would decide when to start building the basement first before moving on to add rooms later.
4. **Client**: The client is responsible for creating a builder object, setting its properties, and running the construction process.

## Real-World Analogy

Think of the Builder pattern as a blueprint for your house. You start with the foundation (reset), then gradually add more components like walls, doors, windows, etc., one by one. The director is like a builder guide who knows exactly when to build each part and in what order.

## Simplified Example

Here's a simplified example of how you might use it:

```python
builder = ConcreteBuilder()
director = Director(builder)

director.build_minimal_viable_product() # Builds only part A
print("Minimal product:", builder.get_product().list_parts()) 

director.build_full_featured_product() # Builds parts A and B
print("Full product:", builder.get_product().list_parts())
```

In this example, `ConcreteBuilder` is the Builder that knows how to build a complex object (the house), `Director` guides the construction process by calling the appropriate building steps in sequence, and the client code creates a ConcreteBuilder object, sets its properties, and runs the construction process.

## See Also

You can find more details about this pattern [here](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/creational/builder.py).
