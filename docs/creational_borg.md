# The Borg Pattern (Creational)

## Purpose

The Borg pattern creates objects that share the same state without having to inherit from a common class. It helps simplify programs by allowing different objects to access and update shared data.

## The Problem It Solves

In complex systems, it's often hard to manage shared data across multiple objects. Normally, you’d use inheritance or global variables to do this, but those approaches can be messy or limiting. The Borg pattern solves this by letting every instance share the same internal state.

## When to Use It

Use the Borg pattern when you need several objects to share and update the same data. For example, if you have many parts of a program that need to access the same settings or manage the same pool of resources, Borg can help keep things in sync without using global variables or inheritance.

## When NOT to Use It

Don’t use the Borg pattern if each object should keep its own separate data. Also, if you’re working in a multithreaded environment and need to prevent unexpected changes, Borg might not be the right choice—it's not designed to be thread-safe.

## How It Works

The Borg class stores all shared data in a single dictionary called `_shared_state`. When you create a new Borg object, it links its internal data (`__dict__`) to this shared dictionary. So any change made by one object shows up in all others.

## Real-World Analogy

Think of a team of scientists using a shared notebook. Each scientist (object) may have their own pen (methods), but they all write in the same notebook (shared data). Whatever one writes, everyone else can see and change.

## Simplified Example

```python
class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state

# All Borg instances share the same data.
b1 = Borg()
b2 = Borg()

b1.x = 10  # Setting a value through one instance...
print(b2.x)  # ...automatically affects the other.
```

## Learn More

You can see the full Borg pattern example on GitHub [here](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/creational/borg.py)
