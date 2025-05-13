# The Observer Pattern (Behavioral)

## Purpose

The Observer pattern defines a one-to-many relationship between objects. When one object (the subject) changes state, it automatically notifies all its dependents (observers). This pattern is commonly used in event-driven systems to keep different parts of a program in sync.

## Problem It Solves

In many applications, multiple parts need to respond to changes in another part. For example, when a user updates a setting, other parts of the app might need to react. Hardcoding these relationships creates tight coupling, which makes the system hard to maintain. The Observer pattern solves this by allowing objects to subscribe to changes without needing direct links.

## When to Use It

Use this pattern when:

* Several parts of your program need to react to changes in another object.
* You're building event-driven or GUI systems (e.g., buttons, sliders, or game states).
* You want to reduce dependencies between components.

## When Not to Use It

Avoid this pattern if:

* You have too many observers to manage easily.
* The notification logic becomes overly complex.
* The list of observers changes frequently, making it hard to track or debug.

## How It Works

The pattern involves three core components:

1. **Subject** – Maintains a list of observers and notifies them when its state changes.
2. **Observer** – Defines an `update()` method that receives notifications.
3. **Concrete Observer** – Implements `update()` and responds to changes in the subject.

## Real-World Analogy

Think of a magazine subscription. When you subscribe, you receive each new issue automatically. The publisher is the subject. You, the subscriber, are the observer. A concrete observer might be your email or mailbox receiving the update.

## Simplified Example

Here’s a basic implementation in Python:

```python
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        pass

class ConcreteObserver(Observer):
    def __init__(self, name):
        self._name = name

    def update(self, message):
        print(f"{self._name} received: {message}")

# Usage
subject = Subject()
observer1 = ConcreteObserver("Observer 1")
observer2 = ConcreteObserver("Observer 2")

subject.attach(observer1)
subject.attach(observer2)

subject.notify("State has changed")

subject.detach(observer1)
subject.notify("Another change occurred")
```

In this example:

* `Subject` manages a list of observers.
* `ConcreteObserver` receives updates and reacts to them.
* Observers can subscribe and unsubscribe at any time.

## Learn More

Explore the full implementation here:
[Observer Pattern – Python Example](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/behavioral/observer.py)
