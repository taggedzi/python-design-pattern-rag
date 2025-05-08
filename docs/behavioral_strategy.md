# The Strategy Pattern (Behavioral)

## Intent

The strategy pattern is a design pattern that enables selecting an algorithm's behavior at runtime based on certain conditions. It provides a way to define a family of algorithms, put each of them into separate classes, and make their objects interchangeable. This allows the same client code to use different strategies without being modified.

## Problem It Solves

The Strategy pattern is useful when you want to choose an algorithm at runtime based on certain conditions or requirements. For instance, if you have a sorting function that needs to perform different types of sorts (ascending, descending, unique), the strategy pattern allows for these different behaviors to be defined in separate classes and then selected as needed. This can help avoid complex conditional statements and make your code more modular and maintainable.

## When to Use It

The Strategy pattern is best used when you have a variety of algorithms that are similar enough so they can be grouped together, but different enough from each other for them to still be considered the same "family". This could include sorting functions (like ascending, descending, unique), rendering functions, or any situation where there's a need to switch between different behaviors.

## When NOT to Use It

The Strategy pattern should not be used when:

1. The client code needs to execute the same behavior regardless of the algorithm chosen.
2. There are few algorithms that can be grouped together and they all have similar conformance to an interface.
3. You need a simple, one-off change in behaviour without needing to modify existing classes.

## How It Works

The Strategy pattern involves three components:

1. A Context class which uses the strategy. This is typically where you'll see the if/else or switch statements that decide which algorithm to use.
2. An abstract base class (Strategy) with a method for executing the algorithm. All strategies should implement this method.
3. Concrete Strategy classes, each implementing the execute() method in a way suitable for their specific strategy.

## Real-World Analogy

Imagine you're at a restaurant and there are multiple menus (strategies). You can choose to order from one menu or another based on what you want to eat (the context decides which strategy to use).

## Simplified Example

Here is a simplified example of the Strategy pattern:

```python
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: list[int]) -> list[int]:
        pass

class AscendingSortStrategy(SortStrategy):
    def sort(self, data: list[int]) -> list[int]:
        return sorted(data)

class Context:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy
        
    def sort(self, data: list[int]) -> list[int]:
        return self._strategy.sort(data)
```

In this example, `AscendingSortStrategy` is a concrete strategy that implements the `sort()` method to provide an ascending sort. The `Context` class uses this strategy by default but can also change its active strategy at runtime.

## See Also

You can find the full implementation of the Strategy pattern in the Python file [here](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/behavioral/strategy.py) in our GitHub repository.
