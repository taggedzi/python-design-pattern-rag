# The Command Pattern (Behavioral)

## Intent

The Command pattern is a behavioral design pattern that turns a request into a standalone object, thereby allowing you to parameterize clients with queues, requests, and operations, or support undoable actions.

## Problem It Solves

In complex software systems, it's often necessary to issue requests in various forms - simple ones like turning on/off the light, more complicated ones involving data manipulation, etc. The problem this pattern solves is that of decoupling senders and receivers. Senders don't need to know anything about the receiver's implementation; they just need to call a method (the command).

## When to Use It

This pattern should be used when you want to:

- Parameterize methods, actions or operations as objects.
- Create and execute requests at different times.
- Support undoable operations.
- Implement multilevel undo/redo functionality.

## When NOT to Use It

The Command Pattern is not a good fit when you need to encapsulate simple tasks that can be done with few lines of code, or when the command is very small and does not have many parameters.

## How It Works

In this pattern, there are four main components:

1. `Command` interface - declares a method for executing an operation.
2. `Concrete Command` class - implements the `execute()` method to carry out the request.
3. `Invoker` class - asks the command to carry out the request.
4. `Receiver` class - knows how to perform the operations associated with carrying out the request.

## Real-World Analogy

Imagine you're a waiter at a restaurant. You take orders from customers, and when they're ready to be served, you hand them over to the chef. In this analogy, your role as an Invoker is taking customer orders (Commands), and serving food (Receiver).

## Simplified Example

Here's a simplified example of how it works:

```python
class Command(ABC):  # Abstract base class for all commands
    @abstractmethod
    def execute(self) -> None:
        pass

# Concrete command to turn on the light
class TurnOnLightCommand(Command):
    def __init__(self, light: 'Light') -> None:
        self._light = light

    def execute(self) -> None:
        self._light.turn_on()

# Invoker class
class RemoteControl:
    def submit(self, command: Command):
        command.execute()

# Receiver class (Light)
class Light:
    def turn_on(self):
        print("The light is on.")

light = Light()
turn_on_command = TurnOnLightCommand(light)  # Client creates a concrete command
remote = RemoteControl()   # Invoker object
remote.submit(turn_on_command)  # Invoker calls the command
```

## See Also

You can find the full Python implementation of this pattern [here](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/behavioral/command.py).
