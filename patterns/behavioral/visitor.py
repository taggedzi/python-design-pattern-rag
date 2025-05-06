"""
Behavioral Pattern: Visitor

Lets you define new operations on objects without changing their classes
by using a separate visitor object.
Useful for separating concerns across many element types.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

# Visitor interface
class Visitor(ABC):
    @abstractmethod
    def visit_element_a(self, element: ElementA) -> None:
        pass

    @abstractmethod
    def visit_element_b(self, element: ElementB) -> None:
        pass

# Element interface
class Element(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass

class ElementA(Element):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_element_a(self)

    def operation_a(self) -> str:
        return "ElementA logic"

class ElementB(Element):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_element_b(self)

    def operation_b(self) -> str:
        return "ElementB logic"

# Concrete visitor
class ConcreteVisitor(Visitor):
    def visit_element_a(self, element: ElementA) -> None:
        print(f"Visitor: Processing {element.operation_a()}")

    def visit_element_b(self, element: ElementB) -> None:
        print(f"Visitor: Processing {element.operation_b()}")

# Example usage
if __name__ == "__main__":
    elements: List[Element] = [ElementA(), ElementB()]
    visitor = ConcreteVisitor()

    for element in elements:
        element.accept(visitor)
