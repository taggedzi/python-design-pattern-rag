# The Command Pattern (Behavioral)

## Purpose

The Command pattern turns a request into a standalone object. This allows you to store, queue, or undo the request later. It also separates the object making the request from the one carrying it out.

## Problem It Solves

Sometimes you need to issue a command without knowing how it's executed. For example, a user interface might need to turn a light on or off, but it shouldn’t need to know the details of how the light works. The Command pattern wraps actions as objects so they can be passed around, delayed, or undone.

## When to Use It

Use this pattern if:

* You need to store or delay actions (e.g., in a queue or scheduler).
* You want to add undo or redo functionality.
* You need to pass actions as arguments.
* You want to decouple the sender of a request from the handler.

## When Not to Use It

Avoid this pattern if:

* Your needs are simple and only require immediate method calls.
* Storing or delaying operations would overcomplicate your code.

## How It Works

The pattern defines five roles:

* **Command**: An interface with an `execute()` method.
* **ConcreteCommand**: Implements `execute()` and defines the specific action.
* **Receiver**: The object that performs the action (e.g., a light).
* **Invoker**: Stores commands and decides when to execute them (e.g., a remote control).
* **Client**: Creates commands and gives them to the invoker.

## Real-World Analogy

Imagine a restaurant. You (the client) tell the waiter (invoker) what you want. The waiter writes down your order (command) and takes it to the kitchen (receiver). The waiter doesn’t cook, and you don’t need to know how the food is prepared. Each role is clearly defined.

## Simplified Example

Here’s a basic Python implementation:

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

In this example, commands control a `Light` object. You could store these commands in a list, run them later, or add undo features.

## Learn More

See a full implementation on GitHub:
[command.py on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/behavioral/command.py)
