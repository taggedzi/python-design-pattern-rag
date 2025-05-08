# The Chain of Responsibility Pattern (Behavioral)

## Intent

The Chain of Responsibility pattern is used to process varied requests from different types of objects, without specifying their classes. It allows an object to bypass the rest of the chain and perform its operation without passing the request along the chain.

## Problem It Solves

This design pattern addresses issues related to decoupling senders and receivers by allowing a chain of handlers (objects) to process requests one after another, until it reaches a handler that can handle the request. This way, each handler has the chance to process the request without knowing about others in the chain.

## When to Use It

The Chain of Responsibility pattern is ideal when you have multiple potential handlers for processing a particular request and you want to decouple senders from receivers. It's also useful when you need to execute several handlers in specific order or randomly.

## When NOT to Use It

If the chain of responsibility needs to be modified frequently, as it can become complex and hard to maintain, Chain of Responsibility might not be the best choice. If there are many levels of indirection involved, this pattern may lead to performance issues.

## How It Works

The Chain of Responsibility pattern involves a chain of handlers (objects) where each handler decides whether it can process the request or pass it on to the next one in the chain. The `set_next()` method is used for setting up this chain and the `handle()` method is responsible for processing the request.

## Real-World Analogy

Imagine a group of friends who are passing an item (request) around until it's found by someone who can handle it (handler). Each friend in the group could be considered a handler, each with its own way to process or pass on the item.

## Simplified Example

Here is a simplified example:

```python
class Handler:  # Abstract base class
    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, request):
        if not self._successor:
            return None
        else:
            return self._successor.handle_request(request)

class ConcreteHandler1(Handler):  # Inherits from Handler
    def handle_request(self, request):
        if request == "RequestType1":
            return f"ConcreteHandler1 handles {request}"
        else:
            return super().handle_request(request)

class ConcreteHandler2(Handler):  # Inherits from Handler
    def handle_request(self, request):
        if request == "RequestType2":
            return f"ConcreteHandler2 handles {request}"
        else:
            return super().handle_request(request)
```

In this example, `ConcreteHandler1` and `ConcreteHandler2` are handlers that can process a specific type of request. The chain is created by setting the successor for each handler to the next one in line. If a handler cannot handle a request (i.e., its condition in `handle_request()` returns `None`), it passes the request on to its successor.

## See Also

The corresponding Python file can be found [here](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/behavioral/chain_of_responsibility.py).
