# The Singleton Pattern (Creational)

## Intent

The Singleton pattern ensures that only one instance of a class exists and provides a global point of access to it. This can be useful when exactly one object is needed to coordinate actions across the system.

## Problem It Solves

It addresses issues related to creating objects, especially in situations where you need control over how many instances are created or how they should interact with each other.

## When to Use It

This pattern should be used when:

- You want to ensure that there is only one instance of a class and it can be accessed globally without any additional overhead.
- There's a need for control over object creation, especially in situations where you have a large number of objects or complex initialization logic.

## When NOT to Use It

This pattern should not be used when:

- You want more than one instance of the class. In this case, you would use the Prototype pattern instead.
- The Singleton object needs to interact with other objects in a way that is different from the usual request/response interaction.

## How It Works

The Singleton class uses a metaclass (`SingletonMeta`) to enforce the singleton behavior. When an instance of the Singleton class is created, it checks if there's already an existing instance and either returns that or creates a new one.

## Real-World Analogy

Imagine you are in a restaurant with your friends. The waiter (Singleton) serves drinks to all patrons (clients). If multiple tables request a drink, the waiter can take care of them individually but ensures they all get the same drink. This is similar to how Singletons ensure only one instance exists and provides global access to it.

## Simplified Example

Here's a simplified example:

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
            raise Exception("This class is a singleton and can't be instantiated more than once")
        else:
            Singleton._instance = self
```

In this example, `getInstance()` method ensures that only one instance of the class exists. If an attempt to create another instance is made, it raises an exception.

## See Also

The full Python implementation for the Singleton pattern can be found [here](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/creational/singleton.py).
