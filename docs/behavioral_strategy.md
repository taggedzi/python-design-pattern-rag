# The Strategy Pattern (Behavioral)

## Purpose

The Strategy pattern defines a set of interchangeable algorithms, each in its own class. It lets you switch between these algorithms at runtime without changing the core logic of your program.

## Problem It Solves

When a function needs to perform similar tasks in different ways—like sorting data using different criteria—you might end up with a lot of `if-else` or `switch` statements. The Strategy pattern helps by isolating each variation into its own class, making the code cleaner and easier to extend.

## When to Use It

Use this pattern when:

* You have several algorithms that solve the same problem differently.
* You want to switch between these algorithms during runtime.
* You want to avoid hardcoding conditional logic.
* You want your algorithms to be reusable and independent of the main program logic.

## When Not to Use It

Avoid this pattern if:

* The algorithm is fixed and unlikely to change.
* The behavior differences are minor and don’t require separate classes.
* A simple conditional is sufficient for the task.

## How It Works

The Strategy pattern includes three parts:

1. **Strategy** – An abstract class or interface that defines a method all strategies must implement.
2. **Concrete Strategies** – Classes that implement different versions of the method.
3. **Context** – Holds a reference to a Strategy and uses it to perform operations. You can change the strategy at runtime.

## Real-World Analogy

Imagine a restaurant with different menus. You pick the menu based on your mood—vegetarian, vegan, or seafood. The kitchen (context) prepares your meal based on your choice, without changing how it operates behind the scenes.

## Simplified Example

Here’s a basic Python example:

```python
from abc import ABC, abstractmethod

# Strategy interface
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: list[int]) -> list[int]:
        pass

# Concrete strategy
class AscendingSortStrategy(SortStrategy):
    def sort(self, data: list[int]) -> list[int]:
        return sorted(data)

# Context
class Context:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def sort(self, data: list[int]) -> list[int]:
        return self._strategy.sort(data)
```

### Usage

```python
data = [5, 2, 9, 1]
context = Context(AscendingSortStrategy())
print(context.sort(data))  # Output: [1, 2, 5, 9]
```

You can switch the strategy by calling `set_strategy()` with a different sorting class.

## Learn More

See the complete Python implementation here:
[Strategy Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/behavioral/strategy.py)
