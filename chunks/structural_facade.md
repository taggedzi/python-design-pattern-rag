---
file: structural/facade.py
chunk: structural_facade.md
---

```python
"""
Structural Pattern: Facade

Provides a simplified interface to a larger body of code, such as a complex subsystem.
Helps decouple a client from complex internal processes or APIs.
"""

class SubsystemA:
    def operation_a1(self) -> str:
        return "SubsystemA: Ready!"

    def operation_a2(self) -> str:
        return "SubsystemA: Go!"

class SubsystemB:
    def operation_b1(self) -> str:
        return "SubsystemB: Fire!"

class Facade:
    """
    The Facade class provides a high-level interface that makes the subsystem easier to use.
    """

    def __init__(self, subsystem_a: SubsystemA, subsystem_b: SubsystemB) -> None:
        self._subsystem_a = subsystem_a
        self._subsystem_b = subsystem_b

    def operation(self) -> str:
        results = [
            self._subsystem_a.operation_a1(),
            self._subsystem_a.operation_a2(),
            self._subsystem_b.operation_b1()
        ]
        return "\n".join(results)

# Example usage
if __name__ == "__main__":
    a = SubsystemA()
    b = SubsystemB()
    facade = Facade(a, b)
    print(facade.operation())

```

## Summary
This code demonstrates the Facade design pattern, providing a simplified interface to complex subsystems.

## Docstrings
- The Facade class provides a high-level interface that makes the subsystem easier to use.
- Initializes the Facade with instances of SubsystemA and SubsystemB.
- Performs operations from both subsystems and returns the results as a string.

