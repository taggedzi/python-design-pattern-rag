---
file: structural/proxy.py
chunk: structural_proxy.md
---

```python
"""
Structural Pattern: Proxy

Provides a placeholder or surrogate for another object to control access,
reduce cost, or add additional functionality.
"""

from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def request(self) -> None:
        pass

class RealSubject(Subject):
    def request(self) -> None:
        print("RealSubject: Handling request.")

class Proxy(Subject):
    """The Proxy controls access to the RealSubject."""

    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def check_access(self) -> bool:
        print("Proxy: Checking access before forwarding request...")
        return True

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.")

    def request(self) -> None:
        if self.check_access():
            self._real_subject.request()
            self.log_access()

# Example usage
if __name__ == "__main__":
    real_subject = RealSubject()
    proxy = Proxy(real_subject)

    print("Client: Executing request through the proxy:")
    proxy.request()

```

## Summary
Implementation of the Proxy design pattern in Python, providing controlled access to a RealSubject and adding logging functionality.

## Docstrings
- The Proxy controls access to the RealSubject.
- Initializes the Proxy with a RealSubject.
- Checks access before forwarding the request to the RealSubject.
- Logs the time of the request.

