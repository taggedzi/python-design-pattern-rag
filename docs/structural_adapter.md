# The Adapter Pattern (Structural)

## Intent

The Adapter pattern is a design pattern that allows the interface of an existing class to be used as another interface without modifying the original class. It's often used when you want to use an existing class, but its interface isn't what you need. The Adapter makes the incompatible classes work together by wrapping its own methods and properties into a new format that is compatible with the client’s code.

## Problem It Solves

The problem this pattern addresses is when we have a class with an incompatible interface, but we want to use it as if it had a different interface. This can be due to various reasons like legacy systems, third-party libraries or simply because you're trying to follow the Single Responsibility Principle (SRP).

## When to Use It

This pattern is best used when:

1. You want to use an existing class but its interface isn’t what you need.
2. You have a working class, but it lacks some of the functionality that you require.
3. The classes are incompatible and cannot work together as they do not share the same interface.
4. You're trying to follow the Single Responsibility Principle (SRP).

## When NOT to Use It

This pattern should be avoided when:

1. If you have control over the original class, it would be better to modify that class directly.
2. The classes are highly compatible and there's no need for an adapter.
3. You're working with a legacy system where modifying the code is not feasible or desirable.
4. When the Adapter introduces complexity into your design.

## How It Works

The Adapter wraps the original class in an interface that clients expect, and it translates between the client’s expectations and the original class's interface. This translation is done by implementing a set of methods that make sense for the client to use.

## Real-World Analogy

Imagine you have a foreign book which has words in your language but written in another language. The Adapter pattern provides an interface where this foreign book can be read, even though it's not understandable yet. It acts as a translator between the original (foreign) and desired (native) languages.

## Simplified Example

Here is a simplified example of how the Adapter pattern works:

```python
class Target:  # The domain-specific interface that clients expect
    def request(self):
        return "Target: The default behavior."

class Adaptee:  # A class with an incompatible interface
    def specific_request(self):
        return ".eetpadA eht fo roivaheb laicepS"   # reversed string

class Adapter(Target):  # Adapts the Adaptee to the Target interface
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee

    def request(self):
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"
```

In this example, `Target` is the interface that we expect to use. However, `Adaptee` has a different interface and cannot be used directly. The `Adapter` class wraps `Adaptee` in such a way that it can be used as if it had the expected interface.

## See Also

The corresponding Python file can be found [here](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/structural/adapter.py).
