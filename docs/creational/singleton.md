# The Singleton Pattern (Creational)

## Intent

Ensure that a class has only one instance, and provide a global point of access to it. This is useful when exactly one object is needed to coordinate actions across the system.

## Problem It Solves

When we want to control the number of instances of a particular class and ensure that no more than one instance can be created.

## When to Use It

Use this pattern when you need strict control over global variables, logging, driver objects, caching, thread pooling, database connections or other resources that should not be created anew each time they are requested.

## When NOT to Use It

It's not suitable for cases where multiple instances of a class may make sense, such as when the class represents a type of item with different attributes (like in a factory pattern).

## How It Works

The Singleton class is defined using a metaclass. The `__call__` method ensures that only one instance of the class exists by checking if an instance already exists and returning it, or creating a new one otherwise.

## Real-World Analogy

Imagine you're in a restaurant with your friends. You order food from different tables (instances). The waiter (Singleton) ensures that all of them are seated at the same table (instance), and they can communicate without passing around individual plates or chopsticks.

## Simplified Example

In this simplified example, `a` and `b` are both Singleton instances:

```python
a = Singleton()
b = Singleton()
assert a is b  # True
```

The increment method increases the value of the internal counter. If you call it on `a` and then on `b`, they will affect the same shared state:

```python
a.increment()
print(b.get_value())  # Output: 1
```

## See Also

The Singleton pattern is often used in [filename].py in the [folder] directory of a project's source code.

This lesson was generated from [filename].py, a Python file that demonstrates the Singleton design pattern. It can be found in the [folder] directory of the repository.

```python
# Full Source Code
"""
Creational Pattern: Singleton
...
"""
class SingletonMeta(type):
    ...
    
class Singleton(metaclass=SingletonMeta):
    """
    Example singleton class.
    ...
    """
    def increment(self) -> None:
        """Increments the internal value by 1."""
        self.value += 1
        
    def get_value(self) -<｜begin▁of▁sentence｜> int:
        """Returns the current value."""
        return self.value
```
"""

```

This Markdown lesson provides a clear and educational introduction to the Singleton pattern, its benefits and how it can be used in Python code examples.