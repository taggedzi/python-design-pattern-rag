# The Facade Pattern (Structural)

## Intent

The Facade Pattern provides a simplified interface to a complex subsystem, such as a set of classes that communicate with each other in a certain way. It helps decouple clients from the complexity of the subsystem by providing a unified and higher-level interface through which users can interact with the system.

## Problem It Solves

The Facade Pattern addresses the problem of making complex subsystems easier to use, while still giving them full access if needed. This is particularly useful in large software systems where clients may not need all features provided by a subsystem. 

## When to Use It

This pattern should be used when:
- A system is very complex and difficult to understand and work with.
- The client code needs to interact with the subsystem, but it shouldn't have direct knowledge of its inner workings.
- You want to provide a simple interface that hides complexity from clients.

## When NOT to Use It

This pattern should not be used when:
- If changes in one part of the system require modifications in many other parts, because it makes subsystems tightly coupled.
- If you need full control over all interactions between different subsystems. In this case, a more complex design might be better.

## How It Works

The Facade class provides a simplified interface to the client code through which it interacts with the complex subsystems (SubsystemA and SubsystemB in this example). The client code doesn't need to know about the internal workings of these classes, as all interactions are handled by the facade. 

## Real-World Analogy

Imagine a complex car engine system that has multiple components interacting with each other. If you want to drive a car, you don't need to understand how every single component works - you just press the accelerator and it moves. This is similar to the Facade Pattern: the client code doesn't need to interact directly with all of the subsystems, but through the facade (the car engine system), they can interact in a simple way.

## Simplified Example

```python
class SubsystemA:
    def operation_a1(self) -> str:
        return "SubsystemA: Ready!"

    def operation_a2(self) -> str:<｜begin▁of▁sentence｜>
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

## See Also

[Design Patterns in Python](https://github.com/faif/python-patterns/blob/master/design_patterns/structural/facade.py)