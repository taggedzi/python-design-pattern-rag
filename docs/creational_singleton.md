# The Singleton Pattern (Creational)

## Purpose

The Singleton pattern ensures that a class has only one instance and provides a global point of access to it. It’s useful for managing shared resources like configuration settings, logging systems, or database connections.

## Problem It Solves

In many programs, certain components—such as a settings manager or logger—should only exist once. Creating multiple instances can cause conflicts or waste resources. The Singleton pattern gives you a structured way to enforce a single instance and provide controlled access to it.

## When to Use It

Use the Singleton pattern when:

* You need only one instance of a class in your program.
* You want to manage a shared resource (e.g., config, logger) globally.
* Creating multiple instances could cause issues or be inefficient.

## When Not to Use It

Avoid this pattern if:

* You need multiple independent instances (use Factory or Prototype patterns instead).
* The Singleton class starts to do too much and becomes hard to maintain.
* You need to write unit tests—Singletons can make testing harder due to hidden state.

## How It Works

The class holds a reference to a single instance, typically using a private variable. Access is controlled through a static method like `getInstance()`, which either returns the existing instance or creates it if it doesn’t exist yet. Some implementations use metaclasses for a cleaner approach.

## Real-World Analogy

Imagine a passport office. No matter how many people apply, there’s only one official place that issues passports. That office is a Singleton—everyone interacts with the same one.

## Simplified Example

Here’s a basic implementation in Python:

```python
class Singleton:
    _instance = None

    @staticmethod
    def getInstance():
        if Singleton._instance is None:
            Singleton()
        return Singleton._instance

    def __init__(self):
        if Singleton._instance is not None:
            raise Exception("This class is a singleton and cannot be instantiated more than once.")
        Singleton._instance = self
```

### Usage

```python
s1 = Singleton.getInstance()
s2 = Singleton.getInstance()
print(s1 is s2)  # True — both refer to the same instance
```

This guarantees that only one instance of the `Singleton` class exists, even if `getInstance()` is called multiple times.

## Learn More

See the full implementation in Python here:
[Singleton Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/creational/singleton.py)
