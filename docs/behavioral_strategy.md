# The Strategy Pattern (Behavioral)

## Purpose

The Strategy pattern lets you define a group of related algorithms, encapsulate each one in its own class, and switch between them at runtime. This allows you to change the behavior of a program without modifying its core logic.

## The Problem It Solves

If you have a function that needs to perform similar actions in different ways—like sorting data in multiple formats—your code might end up cluttered with `if-else` or `switch` statements. The Strategy pattern helps you avoid this by moving each behavior into its own class, making the code cleaner and easier to maintain.

## When to Use It

Use this pattern when:

* You have multiple algorithms that solve the same problem in different ways.
* You want to switch between these algorithms at runtime.
* You want to avoid long conditional logic in your code.
* You want to keep your algorithms flexible and independent from the code that uses them.

## When NOT to Use It

Avoid this pattern if:

* The algorithm never changes or only changes in very rare, simple cases.
* You only need a quick, one-off solution that doesn’t require a reusable structure.
* All the algorithms behave nearly the same and don’t need separate classes.

## How It Works

The Strategy pattern includes three main parts:

1. **Strategy (interface or abstract base class)** – Defines the method each algorithm must implement.
2. **Concrete Strategies** – Implement the actual behavior.
3. **Context** – Uses a Strategy object to perform a task. It delegates the actual work to the selected strategy.

## Real-World Analogy

Think of a restaurant with multiple menus (strategies). You choose a menu depending on what you’re in the mood for. The restaurant (context) serves your meal based on your choice, without changing how the kitchen works behind the scenes.

## Simplified Example

Here’s a simple Python example:

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

The strategy can be changed at runtime by calling `set_strategy()` with a different sorting class.

## Learn More

To see the full implementation in Python, visit:
[Strategy Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/behavioral/strategy.py)
