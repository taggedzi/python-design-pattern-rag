# The Visitor Pattern (Behavioral Design Patterns)

## Intent

The Visitor pattern is a way of separating an algorithm from the objects on which it operates. It allows you to add new operations to classes without modifying those classes, and also provides a central place to manage these new operations.

## Problem It Solves

This design pattern addresses the problem of adding new operations to classes without changing their structure or code. This is particularly useful when you have an existing inheritance hierarchy with many different types that need to perform additional actions on each type, but those actions are not part of the base class's interface. The Visitor pattern allows you to separate these actions into a centralized place, making your code more maintainable and flexible.

## When to Use It

The Visitor pattern is best used when:

- You have an inheritance hierarchy with many different types that need additional operations performed on them.
- These new operations are not part of the base class's interface (i.e., they don't affect subclasses).
- The operations you need to perform should be centralized and not spread across your codebase.

## When NOT to Use It

The Visitor pattern is not suitable when:

- You have a small number of classes that do not require additional operations.
- Your inheritance hierarchy is simple, or the changes made by the visitor are minimal.
- The operations you need to perform are spread across your codebase and can be easily added without changing existing classes.

## How It Works

The Visitor pattern involves two key components: a `Visitor` interface that declares methods for each operation to be performed, and an object (the visitor) that implements these methods. The `Element` interface has a single method `accept()` which takes a `Visitor` as its argument. This allows the element to delegate the work of performing an operation to the visitor.

## Real-World Analogy

Imagine you have a large family tree with many different types of people (like grandparents, uncles, cousins etc.). Now imagine each type of person has certain characteristics or actions that need to be performed on them. Instead of adding these new operations directly into the classes representing individual types of people, you can create a visitor object that knows how to perform these operations and simply ask each individual in the family tree to accept this visitor.

## Simplified Example

Here's a simplified example:

```python
class Visitor(ABC):
    @abstractmethod
    def visit_element_a(self, element: ElementA) -> None:
        pass

    @abstractmethod
    def visit_element_b(self, element: ElementB) -> None:
        pass

class ConcreteVisitor(Visitor):
    def visit_element_a(self, element: ElementA) -> None:
        print("Visiting Element A")

    def visit_element_b(self, element: ElementB) -> None:
        print("Visiting Element B")
```

In this example, `ConcreteVisitor` is a visitor that knows how to perform operations on elements of type A and B. When an element accepts a visitor, it delegates the work of performing its operation to the visitor.

## See Also

The Python code for the Visitor pattern can be found [here](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/behavioral/visitor.py).
