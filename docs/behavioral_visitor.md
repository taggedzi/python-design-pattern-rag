# The Visitor Pattern (Behavioral)

## Purpose

The Visitor pattern lets you define new operations on a group of related objects without changing their classes. Instead of modifying each class to add new functionality, you create a separate visitor object that “visits” each one and performs the desired operation.

## The Problem It Solves

In object-oriented design, it's common to have a hierarchy of related classes. Over time, you might want to add new operations to these classes. However, modifying each class directly can be messy or even impossible if they come from external libraries. The Visitor pattern solves this by letting you define the new operations in a separate visitor class, keeping the original classes clean and untouched.

## When to Use It

Use the Visitor pattern when:

* You need to add many unrelated operations to objects in an existing class hierarchy.
* You want to keep those operations separate from the objects themselves.
* You want to group related operations in one place, making your code easier to maintain.

## When NOT to Use It

Avoid this pattern if:

* You only have a few types of objects or only need a small number of operations.
* Your class hierarchy changes frequently (you'll need to update the visitor every time).
* Simpler solutions like method overloading or polymorphism already work for your needs.

## How It Works

The pattern has two main parts:

1. **Visitor interface** – Declares a `visit` method for each type of object it can handle.
2. **Element classes** – Implement an `accept()` method that takes a visitor and calls the appropriate `visit` method.

This setup lets each object delegate the operation to the visitor without needing to know what the visitor does.

## Real-World Analogy

Imagine visiting a zoo where each animal (element) can accept a tour guide (visitor). The guide knows how to interact with each animal differently: feeding the giraffes, photographing the lions, etc. The animals don’t need to know the details—they just accept the guide and let them do their job.

## Simplified Example

Here's a basic Python example:

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

# Usage
visitor = ConcreteVisitor()
a = ElementA()
b = ElementB()

a.accept(visitor)  # Visiting Element A
b.accept(visitor)  # Visiting Element B
```

In this example, `ElementA` and `ElementB` accept a visitor that performs different actions based on the element type.

## Learn More

For the full implementation, check the Python example here:
[Visitor Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/behavioral/visitor.py)
