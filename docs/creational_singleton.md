# The Singleton Pattern (Creational)

## Purpose

The Singleton pattern ensures that a class has only one instance and provides a global point of access to it. This is useful when a single object needs to coordinate actions across an application—such as a logging system, configuration manager, or database connection.

## The Problem It Solves

In many applications, certain components should only exist once. Creating multiple instances of these components can cause inconsistency, duplication, or unnecessary overhead. The Singleton pattern provides a controlled way to create and access a single shared instance of a class.

## When to Use It

Use the Singleton pattern when:

* You need exactly one instance of a class throughout your program.
* You want a centralized way to access shared resources like configurations, caches, or loggers.
* Creating multiple instances would lead to problems or unnecessary complexity.

## When NOT to Use It

Avoid using Singleton if:

* You need multiple independent instances (consider Prototype or Factory patterns instead).
* The Singleton class starts holding too much responsibility and becomes difficult to manage.
* You want to unit test code that relies on shared state—Singletons can make testing harder due to hidden dependencies.

## How It Works

The Singleton pattern typically uses a class variable to store the one and only instance. Access to the instance is controlled through a method like `getInstance()` that either creates the instance (if it doesn't exist yet) or returns the existing one. Some implementations use metaclasses to enforce the singleton behavior more cleanly.

## Real-World Analogy

Think of a government issuing passports. No matter how many people request one, they all interact with the same passport office. That office acts as a Singleton—there’s only one place to handle those requests, and it manages all related actions globally.

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
print(s1 is s2)  # True — both variables point to the same instance
```

This ensures that only one instance of `Singleton` is ever created, no matter how many times `getInstance()` is called.

## Learn More

For a full Python implementation, check the source here:
[Singleton Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/creational/singleton.py)
