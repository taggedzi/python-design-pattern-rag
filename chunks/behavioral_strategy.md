---
file: behavioral/strategy.py
chunk: behavioral_strategy.md
---

```python
"""
Behavioral Pattern: Strategy

Enables selecting an algorithm's behavior at runtime by defining a family of interchangeable strategies.
Useful when you want to avoid multiple conditional branches.
"""

from abc import ABC, abstractmethod

# Strategy interface
class Strategy(ABC):
    @abstractmethod
    def execute(self, data: list[int]) -> list[int]:
        pass

# Concrete strategies
class AscendingSortStrategy(Strategy):
    def execute(self, data: list[int]) -> list[int]:
        return sorted(data)

class DescendingSortStrategy(Strategy):
    def execute(self, data: list[int]) -> list[int]:
        return sorted(data, reverse=True)

class UniqueSortStrategy(Strategy):
    def execute(self, data: list[int]) -> list[int]:
        return sorted(set(data))

# Context
class SortContext:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def sort(self, data: list[int]) -> list[int]:
        return self._strategy.execute(data)

# Example usage
if __name__ == "__main__":
    data = [5, 3, 9, 1, 3, 9]
    context = SortContext(AscendingSortStrategy())

    print("Ascending:", context.sort(data))
    context.set_strategy(DescendingSortStrategy())
    print("Descending:", context.sort(data))
    context.set_strategy(UniqueSortStrategy())
    print("Unique:", context.sort(data))

```

## Summary
This code demonstrates the Strategy pattern in Python, showcasing how different sorting strategies can be implemented and selected at runtime.

## Docstrings
- Behavioral Pattern: Strategy

Enables selecting an algorithm's behavior at runtime by defining a family of interchangeable strategies.
Useful when you want to avoid multiple conditional branches.
- Strategy interface
- Executes the sorting algorithm on the given data list.
- Concrete strategies
- Sorts the data in ascending order.
- Sorts the data in descending order.
- Sorts the data and removes duplicates before sorting.
- Context
- Initializes the context with a specific strategy.
- Sets a new strategy for the context.
- Performs the sorting operation using the current strategy.

