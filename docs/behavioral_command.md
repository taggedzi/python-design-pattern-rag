# The Command Pattern (Behavioral)

## Intent

The Command pattern is a behavioral design pattern that turns a request into a standalone object, which allows you to parameterize methods with different requests, delay or queue them, and support undoable operations. It provides the means to encapsulate all information needed to perform an action at a later time.

## Problem It Solves

The Command Pattern solves problems related to requesting operations to be performed on objects without knowing anything about the operation being requested (e.g., turning lights on or off). This separation of client and receiver makes it possible for clients to send requests independently from when, where, or who sends them. It also allows for undoable actions by keeping track of previous commands.

## When to Use It

The Command Pattern is useful in scenarios where you want to:

- Parameterize methods with different requests.
- Delay or queue operations.
- Support undoable operations.
- Encapsulate all information needed to perform an action at a later time.

## When NOT to Use It

The Command Pattern should not be used in scenarios where you need to execute commands immediately, because it doesn't support immediate execution of commands.

## How It Works

In the Command pattern:

- `Command` interface declares an `execute()` method for executing a command.
- `ConcreteCommand` class extends the `Command` base and implements the `execute()` method, which defines how to perform the operation.
- `Client` creates a ConcreteCommand object and sets its receiver.
- The invoker is responsible for keeping a history of requests (commands). It can queue commands, execute them in sequence or parallel, and support undoable operations.

## Real-World Analogy

Imagine you are at a restaurant and the waiter serves your order to you. Instead of communicating with the kitchen directly, you communicate with the waiter who takes care of all communication between you and the kitchen. The waiter is like an Invoker in this scenario, serving as an interface for ordering food (commands) from the kitchen (receiver).

## Simplified Example

Here's a simplified example:

```python
class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

# Receiver
class Light:
    def turn_on(self) -> None:
        print("Light is ON")

    def turn_off(self) -> None:
        print("Light is OFF")

# Concrete commands
class TurnOnCommand(Command):
    def __init__(self, light: Light) -> None:
        self._light = light

    def execute(self) -> None:
        self._light.turn_on()

class TurnOffCommand(Command):
    def __init__(self, light: Light) -> None:
        self._light = light

    def execute(self) -> None:
        self._light.turn_off()
```

## See Also

You can find the full Python implementation of this pattern [here](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/behavioral/command.py).
