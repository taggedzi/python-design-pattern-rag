# The Chain of Responsibility Pattern (Behavioral)

## Purpose

The Chain of Responsibility pattern lets you send a request through a chain of potential handlers, giving each one the chance to handle it or pass it along. This allows you to decouple the sender of a request from its potential receivers.

## The Problem It Solves

In many systems, different types of objects may need to respond to the same kind of request. Instead of hardcoding logic to figure out who should respond, this pattern lets you pass the request along a chain until someone handles it. This keeps code flexible and avoids tight coupling between sender and receiver.

## When to Use It

Use this pattern when:

* You have multiple objects that might handle a request.
* You want to avoid hardcoding which object should handle which request.
* You want to process requests in a specific order or allow them to be passed along until handled.

## When NOT to Use It

Avoid this pattern if:

* The chain of handlers changes often, making the setup hard to manage.
* The request needs to be handled quickly and efficiently; passing it through multiple handlers can slow things down.
* Too many handlers make the chain hard to understand or debug.

## How It Works

Each handler has a method to process the request and a reference to the next handler in the chain. If it can handle the request, it does so; if not, it passes the request to the next handler using a method like `set_next()` or by calling the next handler directly.

## Real-World Analogy

Imagine passing a lost item around a group of friends. Each friend checks if it’s theirs. If not, they pass it to the next person. Eventually, someone might recognize it and take action. If no one does, the item goes unclaimed.

## Simplified Example

Here’s a basic example in Python:

```python
class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, request):
        if self._successor:
            return self._successor.handle_request(request)
        return None

class ConcreteHandler1(Handler):
    def handle_request(self, request):
        if request == "RequestType1":
            return f"ConcreteHandler1 handles {request}"
        return super().handle_request(request)

class ConcreteHandler2(Handler):
    def handle_request(self, request):
        if request == "RequestType2":
            return f"ConcreteHandler2 handles {request}"
        return super().handle_request(request)

# Setting up the chain
handler_chain = ConcreteHandler1(ConcreteHandler2())

# Example usage
print(handler_chain.handle_request("RequestType2"))  # Handled by ConcreteHandler2
```

In this example, if `ConcreteHandler1` can't handle the request, it passes it to `ConcreteHandler2`. This setup keeps the logic simple and flexible.

## Learn More

For the full Python implementation, visit:
[chain_of_responsibility.py](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/behavioral/chain_of_responsibility.py)
