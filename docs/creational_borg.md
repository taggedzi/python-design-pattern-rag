# The Borg Pattern (Creational)

## Purpose

The Borg pattern allows multiple instances of a class to share the same internal state. Unlike the Singleton pattern—which restricts you to a single instance—Borg lets you create many instances that all behave as if they share one brain.

## The Problem It Solves

In some applications, you need objects to share data—for example, configuration settings or a pool of reusable resources. While global variables or singletons can do this, they often come with drawbacks like tight coupling or reduced flexibility. Borg offers an alternative by letting multiple objects share state without being the same instance.

## When to Use It

Use the Borg pattern when:

* You want multiple instances to share the same internal data.
* You need a lightweight way to synchronize state across objects.
* You want to avoid singletons but still centralize shared information.

## When NOT to Use It

Avoid the Borg pattern if:

* Each object should have its own unique state.
* You're working in a multithreaded environment—Borg is not thread-safe without extra precautions.
* You're storing sensitive data that must be isolated per instance.

## How It Works

The Borg pattern links every instance’s `__dict__` (its storage for instance variables) to a class-level shared dictionary. So any change made through one instance is immediately visible to all others.

## Real-World Analogy

Imagine several scientists using a single shared notebook. Each scientist can write or read from it, but there’s only one notebook. Whatever one scientist writes, the others will see—it’s a shared workspace for data.

## Simplified Example

```python
class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state

# All Borg instances share the same data.
b1 = Borg()
b2 = Borg()

b1.x = 10  # Assigns x through one instance...
print(b2.x)  # ...and it’s immediately visible in the other.
```

In this example, both `b1` and `b2` have access to the same data, even though they're separate instances.

## Learn More

You can explore the full implementation here:
[Borg Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/creational/borg.py)
