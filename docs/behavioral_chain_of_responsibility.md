# The Chain of Responsibility Pattern (Behavioral)

## Intent

The Chain of Responsibility pattern is used to process varied requests in a chain of handlers, where each handler decides whether it can handle the request or passes it along the chain. This promotes loose coupling between sender and receiver.

## Problem It Solves

In complex systems, there might be many different components that could potentially handle a given task. The Chain of Responsibility pattern allows us to create a chain of handlers where each handler decides whether or not it can process the request. This makes our code more flexible and easier to maintain as we don't have to know in advance which component will be able to handle a particular request.

## When to Use It

The Chain of Responsibility pattern is best used when:

- There are multiple potential handlers for a single request.
- You want to decouple senders and receivers, making your code easier to change and maintain.

## When NOT to Use It

The Chain of Responsibility pattern should not be used in situations where:

- The sender needs to know whether the receiver has handled the request (e.g., for error handling).
- There are a small number of handlers, as this makes the code more complex than it needs to be.

## How It Works

The Chain of Responsibility pattern involves three components: Handler, ConcreteHandler, and Client. The Handler class defines an interface for all concrete handlers to follow (e.g., `handle()` method). ConcreteHandlers are classes that extend the base Handler class and override its `handle()` method. Clients create these handlers and chain them together using the `set_next()` method, which allows each handler in the chain to pass on requests it cannot handle itself.

## Real-World Analogy

Imagine a long line of people waiting for buses. The first person in line (the first ConcreteHandler) knows when the bus is coming, so they let someone else take their place. If no one takes their place, then they go and get on the bus. This is similar to how each handler in the chain can pass a request along if it's not its turn to handle it.

## Simplified Example

Here's a simplified example of the Chain of Responsibility pattern:

```python
class Handler:  # Abstract base class
    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, request):
        if not self._successor is None:
            return self._successor.handle_request(request)
        else:
            return f"{self.__class__} can't handle the {request}"

class ConcreteHandler1(Handler):  # Inherits from Handler
    def handle_request(self, request):
        if request == "ConcreteHandler1":
            return f"{self.__class__} handled {request}"
        else:
            return super().handle_request(request)

class ConcreteHandler2(Handler):  # Inherits from Handler
    def handle_request(self, request):
        if request == "ConcreteHandler2":
            return f"{self.__class__} handled {request}"
        else:
            return super().handle_request(request)
```

In this example, `ConcreteHandler1` and `ConcreteHandler2` are both subclasses of the abstract base class `Handler`. They override the `handle_request()` method to handle requests of their own type. If a request is not handled by one of them, they pass it on to the next handler in the chain (if there is one).

## See Also

The corresponding Python file for this lesson can be found [here](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/behavioral/chain_of_responsibility.py).
