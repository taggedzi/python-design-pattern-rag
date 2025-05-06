"""
Creational Pattern: Prototype

Specifies the kinds of objects to create using a prototypical instance,
and creates new objects by copying this prototype.
Useful when object creation is costly or complex.
"""

from __future__ import annotations
import copy

class Prototype:
    """Base class providing a cloning interface."""

    def clone(self) -> Prototype:
        """Returns a deep copy of the current object."""
        return copy.deepcopy(self)

class Shape(Prototype):
    def __init__(self, color: str, position: tuple[int, int]) -> None:
        self.color = color
        self.position = position

    def move(self, dx: int, dy: int) -> None:
        x, y = self.position
        self.position = (x + dx, y + dy)

    def __str__(self) -> str:
        return f"Shape(color={self.color}, position={self.position})"

# Example usage
if __name__ == "__main__":
    original = Shape("blue", (10, 20))
    print("Original:", original)

    clone = original.clone()
    clone.move(5, -5)
    clone.color = "green"

    print("Cloned:", clone)
    print("Original after cloning:", original)
