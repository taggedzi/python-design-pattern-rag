# The Command Pattern (Behavioral)

## Purpose

The Command pattern turns a request into an object, allowing you to store, queue, or undo it later. This makes it easy to separate the object that issues a request from the one that carries it out.

## The Problem It Solves

Sometimes you want to issue a command without knowing exactly how it will be carried out. For example, a user interface might need to perform actions like turning a light on or off, but it shouldn't need to know how the light works. The Command pattern lets you wrap requests as objects, allowing them to be passed around, delayed, or undone.

## When to Use It

Use this pattern when:

* You want to store or delay actions (e.g., in a queue or scheduler).
* You want to support undo/redo functionality.
* You need to pass commands as arguments.
* You want to decouple objects that issue requests from those that handle them.

## When NOT to Use It

Avoid this pattern if:

* You only need simple, immediate method calls.
* Storing or delaying operations adds unnecessary complexity.

## How It Works

The pattern has several roles:

* **Command**: An interface that defines an `execute()` method.
* **ConcreteCommand**: Implements `execute()` and defines what action to take.
* **Receiver**: The object that actually performs the action (e.g., a light).
* **Invoker**: Stores commands and decides when to run them (e.g., a remote control).
* **Client**: Creates commands and assigns them to the invoker.

## Real-World Analogy

Think of a restaurant. You (the client) tell the waiter (invoker) what you want. The waiter takes your order (command) and gives it to the kitchen (receiver). The waiter doesn’t cook, and you don’t need to know how the food is prepared—everyone has a clear role.

## Simplified Example

Here’s a basic implementation in Python:

```python
from abc import ABC, abstractmethod

# Command interface
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

In this example, the commands encapsulate actions on a `Light` object. You could then store these commands in a queue, execute them on demand, or add undo functionality.

## Learn More

View the complete implementation here:
[command.py on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/behavioral/command.py)
