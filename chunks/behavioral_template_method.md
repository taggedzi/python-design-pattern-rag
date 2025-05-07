---
file: behavioral/template_method.py
chunk: behavioral_template_method.md
---

```python
"""
Behavioral Pattern: Template Method

Defines the program skeleton in an operation, deferring some steps to subclasses.
Allows subclasses to redefine certain steps of an algorithm without changing its structure.
"""

from abc import ABC, abstractmethod

class AbstractClass(ABC):
    """Defines a skeleton algorithm using template methods."""

    def template_method(self) -> None:
        self.base_operation_1()
        self.required_operations_1()
        self.base_operation_2()
        self.hook_1()
        self.required_operations_2()
        self.hook_2()

    def base_operation_1(self) -> None:
        print("Base: Doing the bulk of the work (1)")

    def base_operation_2(self) -> None:
        print("Base: Doing the bulk of the work (2)")

    @abstractmethod
    def required_operations_1(self) -> None:
        pass

    @abstractmethod
    def required_operations_2(self) -> None:
        pass

    def hook_1(self) -> None:
        pass  # Optional

    def hook_2(self) -> None:
        pass  # Optional

class ConcreteClassA(AbstractClass):
    def required_operations_1(self) -> None:
        print("ConcreteClassA: Implemented required_operation_1")

    def required_operations_2(self) -> None:
        print("ConcreteClassA: Implemented required_operation_2")

class ConcreteClassB(AbstractClass):
    def required_operations_1(self) -> None:
        print("ConcreteClassB: Implemented required_operation_1")

    def required_operations_2(self) -> None:
        print("ConcreteClassB: Implemented required_operation_2")

    def hook_1(self) -> None:
        print("ConcreteClassB: Hook 1 overridden")

# Example usage
if __name__ == "__main__":
    print("== A version ==")
    a = ConcreteClassA()
    a.template_method()

    print("\n== B version ==")
    b = ConcreteClassB()
    b.template_method()

```

## Summary
This code demonstrates the Template Method design pattern using Python's ABC module. It defines an abstract base class with a template method that outlines the structure of an algorithm, leaving some steps to be implemented by subclasses.

## Docstrings
- Defines a skeleton algorithm using template methods.
- Performs the bulk of the work in the first base operation.
- Performs the bulk of the work in the second base operation.
- Abstract method for subclasses to implement required operations 1.
- Abstract method for subclasses to implement required operations 2.
- Optional hook method that can be overridden by subclasses.
- Optional hook method that can be overridden by subclasses.

