---
file: behavioral/command.py
chunk: behavioral_command.md
---

```python
"""
Behavioral Pattern: Command

Encapsulates a request as an object, thereby allowing for parameterization of clients with queues,
requests, and operations, and supports undoable actions.
"""

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

# Invoker
class RemoteControl:
    def __init__(self) -> None:
        self._commands: list[Command] = []

    def submit(self, command: Command) -> None:
        self._commands.append(command)
        command.execute()

# Example usage
if __name__ == "__main__":
    light = Light()
    on_command = TurnOnCommand(light)
    off_command = TurnOffCommand(light)

    remote = RemoteControl()
    remote.submit(on_command)
    remote.submit(off_command)

```

## Summary
Implementation of the Command Design Pattern in Python

## Docstrings
- Encapsulates a request as an object, allowing for parameterization of clients with queues, requests, and operations, and supports undoable actions.
- Abstract base class representing a command. Must implement the execute method.
- Concrete command that turns on a light.
- Concrete command that turns off a light.
- Abstract base class representing a receiver. Provides methods for turning on and off a light.
- Class representing a remote control that can submit commands and execute them.
- Example usage of the Command pattern to control a light.

