# The Chain Of Responsibility Pattern (Behavioral)

# The Chain of Responsibility Pattern (Behavioral Design Patterns)

## Intent

The Chain of Responsibility pattern allows passing requests along a chain of handlers, where each handler decides whether to process the request or pass it on to the next one in line. This promotes loose coupling between sender and receiver.

## Problem It Solves

This pattern addresses the issue of how to handle requests when there are multiple potential handlers for that request type. Without this pattern, a client might have to know about all possible handlers before it can send a request. With Chain of Responsibility, clients don't need to know about these handlers; they just pass on the responsibility of handling the request.

## When to Use It

This pattern is particularly effective when there are multiple potential handlers for a request type and you want to decouple sender and receiver. 

## When NOT to Use It

Misuse of this pattern can lead to complex chains where it might be better to use simpler patterns like Command or Strategy. Also, if the client needs to know about all potential handlers before sending a request, then Chain of Responsibility may not be the best fit.

## How It Works

The Chain of Responsibility pattern involves setting up a chain of handler objects where each object can decide whether it is able to handle the request or if it should pass it on to the next in line. The key classes involved are `Handler`, which defines an interface for handling requests and two concrete handlers: `MonkeyHandler`, `SquirrelHandler`, and `DogHandler`.

## Real-World Analogy

Imagine a chain of friends where each friend is responsible for a certain type of task (like eating bananas or nets). If one friend in the chain can't handle a request, it gets passed on to the next friend until it either gets handled or reaches the end of the chain. This is similar to how the Chain of Responsibility pattern works: each handler passes off requests that it cannot handle.

## Simplified Example

Here's a simplified pseudocode example of how this might look in code:

```python
class Handler:
    def set_next(self, handler): pass
    def handle(self, request): pass

class MonkeyHandler(Handler):
    def handle(self, request): 
        if request == "Banana": return "Monkey: I'll eat the Banana."
        else: return None
```
In this example, `MonkeyHandler` is a concrete handler that knows how to process requests of type "Banana". Other handlers would have similar methods.

## See Also

[ChainOfResponsibility.py](https://github.com/faif/python-patterns/blob/master/patterns/behavioral/chain_of_responsibility.py) in the python-patterns repository on GitHub.