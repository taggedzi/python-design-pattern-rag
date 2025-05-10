# The Adapter Pattern (Structural)

## Purpose

The Adapter pattern allows objects with incompatible interfaces to work together. It acts as a bridge between a class you already have and the interface you need. Instead of changing existing code, you create an adapter that translates one interface into another.

## The Problem It Solves

Sometimes you want to use a class, but its methods don't match what your code expects. This often happens when working with legacy code, third-party libraries, or when following the Single Responsibility Principle (SRP) and keeping classes focused. Rather than modifying the original class (which might be risky or impossible), the Adapter pattern lets you create a wrapper that makes it compatible with your code.

## When to Use It

Use the Adapter pattern when:

* You want to use an existing class, but its interface doesn’t match what you need.
* You’re integrating with legacy code or third-party libraries.
* You want to follow SRP by not changing the original class.
* Classes with different interfaces need to work together.

## When NOT to Use It

Avoid the Adapter pattern if:

* You control the original class and can safely change its interface.
* The classes already work together without modification.
* Adding an adapter would unnecessarily complicate your design.

## How It Works

The Adapter pattern works by wrapping the incompatible class in a new class that implements the desired interface. This wrapper (the adapter) translates method calls or data between the expected interface and the actual one.

## Real-World Analogy

Imagine you have a power plug from Europe, but you're in the U.S. The plug won't fit the outlet directly. An adapter converts the shape of the plug so you can use your device without modifying it. The same idea applies in software—adapters help mismatched parts work together without changing their internal workings.

## Simplified Example

Here's a simple Python example:

```python
# The interface expected by the client
class Target:
    def request(self):
        return "Target: The default behavior."

# An existing class with a different interface
class Adaptee:
    def specific_request(self):
        return ".eetpadA eht fo roivaheb laicepS"  # reversed string

# Adapter converts the interface of Adaptee to match Target
class Adapter(Target):
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee

    def request(self):
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"
```

### Usage

```python
adaptee = Adaptee()
adapter = Adapter(adaptee)
print(adapter.request())  # Output: Adapter: (TRANSLATED) Special behavior of the Adaptee.
```

In this example:

* `Target` is the expected interface.
* `Adaptee` has an incompatible method.
* `Adapter` wraps `Adaptee` and translates its output to match what the client expects.

## Learn More

You can find the complete implementation in Python here:
[Adapter Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/structural/adapter.py)
