# The Proxy Pattern (Structural)

# The Proxy Pattern (Structural Design Patterns)

## Intent
The Proxy design pattern provides a surrogate or placeholder for another object, controlling its instantiation, access, and/or modification of its behavior. It is used to provide a substitute or placeholder for another object, which can also be called the real subject. The proxy controls access to the real subject and adds additional functionality like logging before or after forwarding requests to it.

## Problem It Solves
The Proxy pattern addresses issues related to performance, control over resources, and security by providing a surrogate for another object. This can be particularly useful in situations where you want to add some extra behavior (like logging) without modifying the original class of that object.

## When to Use It
This pattern is especially effective when:
- You need to control access to an object, like by restricting network requests or limiting resource usage.
- You want to provide a simplified interface for accessing complex systems.
- The real subject class implements the Subject interface and you want to add some additional behaviors before/after forwarding calls to it.

## When NOT to Use It
Misusing this pattern can lead to unnecessary complexity. If your use case doesn't require any of the features provided by the Proxy pattern (like logging), then using a Proxy might be overkill and make your code harder to understand. 

## How It Works
The Proxy class has an interface identical to the RealSubject, which allows it to stand in for both the real subject and its clients. The proxy maintains a reference to a real subject and uses it to perform actions when appropriate. In addition, the proxy can add additional logic before or after delegating requests to the real subject.

## Real-World Analogy
Imagine you're at a bank and you have an ATM card that acts as your 'proxy'. You can use this card to withdraw money from various accounts without actually being in the bank (the real subject). The ATM machine is like the proxy, handling requests for you. It also logs every transaction for security purposes (additional behavior added by the proxy).

## Simplified Example
Here's a simplified pseudocode representation of how the Proxy pattern works:
```python
class Subject:
    def request(self) -> None: pass

class RealSubject(Subject):
    def request(self) -<｜begin▁of▁sentence｜> None: 
        print("RealSubject: Handling request.")

class Proxy(Subject):
    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject
    
    def request(self) -> None:
        if self.checkAccess(): 
            self._real_subject.request()
            self.logAccess()
            
    def checkAccess(self) -> bool:
        print("Proxy: Checking access before forwarding request...")
        return True
    
    def logAccess(self) -> None:
        print("Proxy: Logging the time of request.")
```

## See Also
The code snippet provided here is a part of a larger project. You can find it in the folder `structural/proxy`.

It's important to note that while this pattern provides many benefits, it should be used judiciously as overuse or misuse could lead to unnecessary complexity and increased maintenance overhead.