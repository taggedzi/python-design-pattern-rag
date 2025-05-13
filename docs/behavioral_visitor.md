# The Visitor Pattern (Behavioral)

## Purpose

The Visitor pattern allows you to define new operations on a set of related objects without modifying their classes. Instead of changing each class to add functionality, you create a separate visitor object that "visits" each one to perform the desired action.

## Problem It Solves

In object-oriented design, you might have a class hierarchy where all the classes share a common interface. Over time, you may want to add operations to these classes. Modifying each one can get messy—especially if you can't change the original code (e.g., it comes from a third-party library). The Visitor pattern solves this by moving those new operations into a visitor class, keeping your data classes clean and unchanged.

## When to Use It

Use the Visitor pattern when:

* You need to apply multiple, unrelated operations to objects in a class hierarchy.
* You want to separate operations from the objects they work on.
* You want to group operations in one place for easier management and updates.

## When Not to Use It

Avoid this pattern if:

* You have only a few object types or don’t need many operations.
* Your object structure changes often—you’ll need to update the visitor each time.
* Polymorphism or method overloading is enough for your use case.

## How It Works

The pattern involves two key roles:

1. **Visitor** – An interface that declares `visit` methods for each object type.
2. **Elements** – Classes that implement an `accept()` method, which passes control to the visitor.

Each element delegates the operation to the visitor, which knows how to handle it based on its type.

## Real-World Analogy

Imagine you're on a zoo tour. Each animal (element) allows a tour guide (visitor) to interact with it. The guide knows how to handle each animal—feeding the giraffes, photographing the lions, etc. The animals don’t need to know what the guide is doing—they just accept the guide.

## Simplified Example

Here's a basic example in Python:

```python
from abc import ABC, abstractmethod

# Visitor interface
class Visitor(ABC):
    @abstractmethod
    def visit_element_a(self, element):
        pass

    @abstractmethod
    def visit_element_b(self, element):
        pass

# Concrete Visitor
class ConcreteVisitor(Visitor):
    def visit_element_a(self, element):
        print("Visiting Element A")

    def visit_element_b(self, element):
        print("Visiting Element B")

# Element base class
class Element(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass

# Concrete Elements
class ElementA(Element):
    def accept(self, visitor: Visitor):
        visitor.visit_element_a(self)

class ElementB(Element):
    def accept(self, visitor: Visitor):
        visitor.visit_element_b(self)
```

### Usage

```python
visitor = ConcreteVisitor()
a = ElementA()
b = ElementB()

a.accept(visitor)  # Visiting Element A
b.accept(visitor)  # Visiting Element B
```

Each element accepts the visitor, which then performs a type-specific operation.

## Learn More

See the complete implementation on GitHub:
[Visitor Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/behavioral/visitor.py)
