# The Adapter Pattern (Structural)

# The Adapter Pattern (Structural Design Patterns)

## Intent
The Adapter pattern is a structural design pattern that allows objects with incompatible interfaces to work together. It wraps itself around an existing class, or adapts it into another interface as required by the client's code. 

## Problem It Solves
In software development, there are often scenarios where classes from different libraries need to interact but they do not have compatible interfaces. This can lead to a lot of boilerplate code and is error-prone. The Adapter pattern solves this by providing a wrapper around the existing class that makes it compatible with the client'<｜begin▁of▁sentence｜> expected interface.

## When to Use It
This pattern should be used when:
1. You want to use an existing class, but its interface does not match your application’s needs. 
2. You need to reuse an existing subclass, but its interface is not compatible with the rest of your code and cannot be subclassed to fulfill new requirements.
3. When you want to create a unified interface for a set of classes that are incompatible with each other.

## When NOT to Use It
This pattern should not be used when:
1. The client code is simple and the adapter is going to add too much indirection, because each object adapter requires more than a single forwarding method. 
2. When you need to create a large number of similar proxies that only differ in their additional behaviour. In this case, it would be simpler to subclass the original class directly and override its methods instead.

## How It Works
The Adapter pattern works by making the Adaptee's interface compatible with the Target's interface. This is done by creating an adapter class that implements the ITarget interface. The adapter receives calls from the client, and translates them to appropriate calls on the adaptee. 

In this specific code, the `Target` class represents the existing interface your application expects. The `Adaptee` class has a different interface than what the client expects. The `Adapter` class wraps the Adaptee in such a way that it becomes compatible with the Target.

## Real-World Analogy
Imagine you are at a party and there is a DJ who can only play music, but everyone wants to listen to songs. This DJ (the adapter) adapts his skills so he can also understand the language of the people (their code), translates it into music (method calls), and plays that music for the audience (clients).

## Simplified Example
Here is a simplified version of the provided Python code:
```python
class Target:
    def request(self):
        return "Target: The default behavior."

class Adaptee:
    def specific_request(self):
        return ".eetpadA eht fo roivaheb laicepS"   # reversed string

class Adapter(Target):
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee

    def request(self):
        return f"Adapter: (TRANSLATED) {self<｜begin▁of▁sentence｜>elf.adaptee.specific_request()[::-1]}"
```

## See Also
The full source file for this pattern can be found in the `structural/adapter` folder of the repository.