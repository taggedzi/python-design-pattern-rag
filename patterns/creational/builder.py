"""
Creational Pattern: Builder

Separates the construction of a complex object from its representation
so that the same construction process can create different representations.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional

# Product
class Product:
    """Represents the complex object under construction."""

    def __init__(self) -> None:
        self.parts: list[str] = []

    def add(self, part: str) -> None:
        self.parts.append(part)

    def list_parts(self) -> str:
        return ", ".join(self.parts)

# Builder interface
class Builder(ABC):
    @abstractmethod
    def reset(self) -> None: pass

    @abstractmethod
    def build_part_a(self) -> None: pass

    @abstractmethod
    def build_part_b(self) -> None: pass

    @abstractmethod
    def get_product(self) -> Product: pass

# Concrete Builder
class ConcreteBuilder(Builder):
    def __init__(self) -> None:
        self._product: Optional[Product] = None
        self.reset()

    def reset(self) -> None:
        self._product = Product()

    def build_part_a(self) -> None:
        self._product.add("PartA")

    def build_part_b(self) -> None:
        self._product.add("PartB")

    def get_product(self) -> Product:
        product = self._product
        self.reset()
        return product

# Director (optional)
class Director:
    """Director defines the order in which to call building steps."""

    def __init__(self, builder: Builder) -> None:
        self._builder = builder

    def build_minimal_viable_product(self) -> None:
        self._builder.build_part_a()

    def build_full_featured_product(self) -> None:
        self._builder.build_part_a()
        self._builder.build_part_b()

# Example usage
if __name__ == "__main__":
    builder = ConcreteBuilder()
    director = Director(builder)

    director.build_minimal_viable_product()
    print("Minimal product:", builder.get_product().list_parts())

    director.build_full_featured_product()
    print("Full product:", builder.get_product().list_parts())