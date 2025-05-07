---
file: creational/singleton.py
chunk: creational_singleton.md
---

```python
"""
Creational Pattern: Singleton

Ensures that only one instance of a class exists and provides a global point of access to it.
This implementation uses a metaclass to enforce the singleton behavior.
"""

from __future__ import annotations
from typing import Any

class SingletonMeta(type):
    """A metaclass that creates a Singleton class."""
    _instances: dict[type, Any] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    """
    Example singleton class.

    All instances created from this class will point to the same object in memory.
    """

    def __init__(self) -> None:
        self.value = 0

    def increment(self) -> None:
        """Increments the internal value by 1."""
        self.value += 1

    def get_value(self) -> int:
        """Returns the current value."""
        return self.value

# Example usage
if __name__ == "__main__":
    a = Singleton()
    b = Singleton()

    a.increment()
    b.increment()

    assert a is b
    print(f"Singleton value from 'a': {a.get_value()}")  # Output: 2
    print(f"Singleton value from 'b': {b.get_value()}")  # Output: 2

```

## Summary
This code implements the Singleton design pattern using a metaclass to ensure that only one instance of a class exists and provides a global point of access to it.

## Docstrings
- Ensures that only one instance of a class exists and provides a global point of access to it.
- A metaclass that creates a Singleton class.
- Example singleton class.
- All instances created from this class will point to the same object in memory.
- Increments the internal value by 1.
- Returns the current value.

