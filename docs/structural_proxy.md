# The Proxy Pattern (Structural)

## Purpose

The Proxy pattern provides a substitute or placeholder for another object. It lets you control access to the real object, often adding extra behavior like logging, access control, or lazy loading, without changing the original object’s code.

## The Problem It Solves

Sometimes you don’t want clients to access an object directly. The object might be expensive to create, reside on a remote server, or require security checks before it can be used. The Proxy pattern introduces an intermediary that can manage access, delay creation, or add extra logic without modifying the original object.

## When to Use It

Use the Proxy pattern when:

* You want to add access control or logging to an object.
* You need to defer the creation of an expensive object until it's needed (lazy initialization).
* You want to wrap a remote object (e.g., in a networked system) or simulate one locally.
* You need to manage access to objects without changing their code.

Common uses include virtual proxies (for lazy loading), protection proxies (for access control), and remote proxies (for representing objects over a network).

## When NOT to Use It

Avoid using this pattern when:

* There’s no need to restrict access or add behavior around the object.
* The overhead of using a proxy outweighs its benefits.
* You're adding complexity without a clear benefit (e.g., for simple objects that don’t need guarding or extra logic).

## How It Works

The Proxy and the real object (often called `RealSubject`) share the same interface. The client interacts with the Proxy, which decides whether or not to pass the request to the real object. The Proxy can add extra logic before and/or after delegating the request.

## Real-World Analogy

Think of a theater ticket checker at the entrance. Before letting you into the movie (the RealSubject), they verify your ticket (access control) and log your entry (logging). The ticket checker is the Proxy—controlling access to the real experience.

## Simplified Example

```python
class Subject:
    def request(self) -> None:
        pass

class RealSubject(Subject):
    def request(self) -> None:
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
```

### Usage

```python
if __name__ == "__main__":
    real_subject = RealSubject()
    proxy = Proxy(real_subject)

    print("Client: Executing request through the proxy:")
    proxy.request()
```

### Output

```text
Client: Executing request through the proxy:
Proxy: Checking access before forwarding request...
RealSubject: Handling request.
Proxy: Logging the time of request.
```

## Learn More

View the full implementation in Python here:
[Proxy Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/structural/proxy.py)
