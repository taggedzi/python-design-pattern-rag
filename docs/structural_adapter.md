# The Adapter Pattern (Structural)

## Intent
The Adapter pattern is used to make two unrelated interfaces work together. It's an alternative way of saying "wire up" or "hook these two things together".

## Problem It Solves
Imagine you have a class that has an incompatible interface with another class, and you want them to work together. The Adapter pattern solves this problem by creating a wrapper around the existing class, which makes it compatible with the client's expectations.

## When to Use It
You would use the Adapter pattern when:
- You want some existing classes to be used as if they were a different class (e.g., an old class that has an incompatible interface).
- You need to make unrelated classes work together, but you don't want to change their interfaces or create subclasses just for the sake of compatibility.

## When NOT to Use It
You should not use the Adapter pattern when:
- The client code is expected to operate with a specific class (e.<｜begin▁of▁sentence｜>craps and bangs, I know you're thinking about it).
- You need to make a large number of classes work together, or all classes in your system must be compatible. In that case, consider using the Bridge pattern instead.

## How It Works
The Adapter wraps one of the existing interfaces and translates the method calls into something else, which is expected by the client code. The wrapped object (Adaptee) remains unaware of this translation. 

## Real-World Analogy
Imagine you're at a party where everyone has a different kind of drink (Target), but the bar keeps giving you a mixed drink (Adaptee). You can order drinks, but they have to be mixed for you (Adapter). The Adapter pattern is about making this process more manageable.

## Simplified Example
Here's a simplified example:
```python
class Target:  # Existing interface
    def request(self) -> str:
        return "Target: The default behavior."

class Adaptee:  # Incompatible interface
    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"  

class Adapter(Target):  # Adapter that makes the incompatible work with compatible
    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"
```
## See Also
The Python code for this lesson can be found [here](https://github.com/username/repo/blob/main/python_patterns/structural/adapter.py).