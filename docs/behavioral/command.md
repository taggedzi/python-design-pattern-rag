# The Command Pattern (Behavioral)

## Intent

The Command pattern encapsulates a request as an object, thereby allowing for parameterization of clients with queues, requests, and operations, and supports undoable actions. It provides the means to decouple client from receiver.

## Problem It Solves

Command Pattern solves problems related to communication between objects where sending object is not supposed to know about receiving object's class or identity. The pattern also helps in implementing Undo/Redo operations, providing a way of storing requests for later use and processing them one by one.

## When to Use It

Command Pattern should be used when you want to:
- Parameterize methods with different requests into objects.
- Implementing callbacks or performing actions at some point in the future.
- Support undo/redo operations.

## When NOT to Use It

Do not use Command pattern if your system is simple and doesn't require complex command structures, as it can make code more complicated. Also, avoid using this pattern for cases where you need a quick response or the receiver of the request should know about the sender.

## How It Works

The main components in this pattern are:
- `Command` interface with an abstract method `execute()`.
- `Concrete Commands` that implement the `Command` interface and carry out specific actions on a `Receiver` object.
- `Invoker` which uses these commands to perform operations.
- `Receiver` which knows how to execute the command(s).

In this example, we have a `Light` receiver that can turn light on or off. The invoker is the `RemoteControl` class and it submits commands (TurnOnCommand or TurnOffCommand) to be executed by the receiver.

## Real-World Analogy

Imagine you are a remote control for your smart home devices like lights, TVs etc. You have buttons on your remote that perform different actions when pressed. Each button is essentially an object encapsulating a command (like turning the light ON or OFF). The remote itself doesn't know about the specific device it controls but knows how to execute commands.

## Simplified Example

A simplified example of this pattern could be:
```python
class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

class PrintCommand(Command):
    def __init__(self, text: str) -> None:
        self._text = text
        
    def execute(self) -> None:
        print(self._text)

class Invoker:
    def submit(self, command: Command) -> None:
        command.execute()

# Example usage
if __name__ == "__main__":
    text = "Hello World!"
    print_command = PrintCommand(text)
    
    remote = Invoker()
    remote.submit(print_command)
```
In this simplified example, `PrintCommand` is a concrete command that prints a given string when executed. The `Invoker` submits the command to be executed by calling its `execute()` method.

## See Also

[https://github.com/faif/python-patterns/blob/master/patterns/behavioral/command.py](https://github.com/faif/python-patterns/blob/master/patterns/behavioral/command.py)

```python
# The full source file can be found at the provided link.
```

This pattern is also known as Action or Transactional Method, and it's a fundamental part of Command Query Separation (CQS).