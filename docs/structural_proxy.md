# The Proxy Pattern (Structural)

## Purpose

The Proxy pattern provides a stand-in for another object, allowing you to control access to it. Proxies often add behavior like logging, access control, or lazy initialization—without modifying the original object.

## Problem It Solves

Sometimes you don’t want direct access to an object. It might be expensive to create, live on a remote server, or require authorization. The Proxy pattern introduces a middle layer that can delay creation, enforce rules, or enhance functionality while keeping the core object unchanged.

## When to Use It

Use this pattern when:

* You want to control access to an object (e.g., based on user permissions).
* The object is expensive to create, and you want to delay initialization.
* You need to wrap a remote object (e.g., from a network or external API).
* You want to add cross-cutting concerns like logging, without changing the object’s code.

Common types of proxies include:

* **Virtual proxies** – delay the creation of a resource.
* **Protection proxies** – manage access rights.
* **Remote proxies** – represent objects across a network.
* **Logging proxies** – track interactions.

## When Not to Use It

Avoid this pattern if:

* There’s no need to restrict access or add behavior.
* The extra layer adds unnecessary complexity.
* The object is lightweight and easy to create directly.

## How It Works

The Proxy and the original object (the "real subject") implement the same interface. The client interacts with the Proxy, which can perform checks or add logic before passing the request to the real object.

## Real-World Analogy

A security guard at a concert checks your ticket before letting you in. You don’t talk directly to the performers—the guard (proxy) manages access. They might also record who enters. This is similar to a software proxy managing access and logging requests.

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

```bash
Client: Executing request through the proxy:
Proxy: Checking access before forwarding request...
RealSubject: Handling request.
Proxy: Logging the time of request.
```

## Learn More

See the full Python implementation here:
[Proxy Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/structural/proxy.py)
