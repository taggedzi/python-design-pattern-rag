# The Proxy Pattern (Structural)

## Intent

The Proxy pattern provides a surrogate or placeholder for another object to control access to it. It is used when we want to provide a simplified interface to complex subsystems, manage remote services, or restrict access to certain operations.

## Problem It Solves

Without the need to change existing code and without exposing real objects, Proxy provides a surrogate for another object. This pattern allows us to control the interactions between clients and an object.

## When to Use It

When we want to provide controlled access to complex subsystems or when we need to manage remote services. The Proxy can be used in scenarios where we have a heavy network latency, or where we want to add additional functionality like logging before or after the request is processed.

## When NOT to Use It

It's not suitable for cases where you don’t need any control over interactions between clients and objects. Also, it should be used when there are many similar classes that only differ in one method.

## How It Works

The Proxy class has the same interface as an object it represents. The RealSubject is the actual object being represented by the proxy. The client interacts with the Proxy instead of the RealSubject. Before forwarding a request to the RealSubject, the Proxy can perform some additional operations like checking access rights beforehand or logging requests after they have been processed.

## Real-World Analogy

Imagine you are at a movie theater and there's a person standing in front of all the screens (the Proxy). They check if your ID is valid, let you in (forwarding the request to the screen), and then log that you watched a movie (additional functionality). If they see you don’t have a valid ID, they can refuse entry.

## Simplified Example

Here's a simplified example of how the Proxy pattern might look:

```python
class Subject:
    def request(self) -> None:
        pass

class RealSubject(Subject):
    def request(self) -<｜begin▁of▁sentence｜> None:
        print("RealSubject: Handling request.")

class Proxy(Subject):
    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access before forwarding request...")
        return True

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.")

# Example usage
if __name__ == "__main__":
    real_subject = RealSubject()
    proxy = Proxy(real<｜begin▁of▁sentence｜>ject)

    print("Client: Executing request through the proxy:")
    proxy.request()
```

## See Also

The Python code for this pattern can be found [here](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/structural/proxy.py).
