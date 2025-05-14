# The Adapter Pattern (Structural)

## Purpose

The Adapter pattern allows objects with incompatible interfaces to work together. It acts as a bridge between an existing class and the interface your code expects. Rather than modifying existing code, you write a separate adapter that converts one interface to another.

## Problem It Solves

Sometimes you want to use a class, but its methods don't match what your code expects. This often happens with legacy code or third-party libraries. Changing the original class might be risky, impractical, or violate good design principles like the Single Responsibility Principle. The Adapter pattern lets you create a wrapper that makes the class compatible without altering its original code.

## When to Use It

Use the Adapter pattern when:

* You need to integrate a class with an incompatible interface.
* You're working with legacy code or external libraries you can’t change.
* You want to avoid modifying existing classes.
* You need to enable classes with different interfaces to collaborate.

## When Not to Use It

Avoid this pattern if:

* You own and can safely modify the original class.
* The classes already work together as-is.
* Adding an adapter would overcomplicate a simple design.

## How It Works

You create a new class—the adapter—that wraps the existing class. This adapter implements the interface your code expects and translates calls or data to match the behavior of the wrapped class.

## Real-World Analogy

Think of using a travel plug adapter. If your European charger doesn’t fit a U.S. outlet, the adapter converts the plug shape so your device works without needing to redesign the charger. In code, adapters serve the same purpose: making two mismatched pieces work together.

## Simplified Example

Here’s a basic Python example:

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

* `Target` is the interface the client expects.
* `Adaptee` has a different, incompatible method.
* `Adapter` wraps `Adaptee` and makes it compatible with `Target`.

## Learn More

See the complete Python example here:
[Adapter Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/structural/adapter.py)
