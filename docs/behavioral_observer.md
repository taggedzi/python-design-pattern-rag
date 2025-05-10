# The Observer Pattern (Behavioral)

## Purpose

The Observer pattern creates a one-to-many relationship between objects, where one object (the subject) notifies multiple other objects (observers) when its state changes. This is commonly used in event-driven systems to manage updates across different parts of a program.

## The Problem It Solves

In many systems, different components need to respond to changes in another part of the system. For example, if a user updates a setting in the interface, other parts of the app might need to react. Hardcoding these relationships makes the system rigid and hard to maintain. The Observer pattern solves this by allowing objects to subscribe to updates without tight coupling.

## When to Use It

Use this pattern when:

* You want multiple parts of your program to react to changes in another object.
* You’re working in an event-driven or GUI system (e.g., buttons, sliders, or game state updates).
* You want to avoid direct dependencies between components.

## When NOT to Use It

Avoid it if:

* You have too many observers, making it hard to track who’s subscribed.
* The update logic becomes too complex or hard to debug.
* Subscriptions are constantly changing in ways that make the pattern hard to manage.

## How It Works

The pattern includes three main parts:

1. **Subject** – Keeps a list of observers and notifies them when its state changes.
2. **Observer** – Defines the `update()` method to receive changes.
3. **Concrete Observer** – A real object that implements the `update()` method and reacts to changes in the subject.

## Real-World Analogy

Think of a magazine subscription. When you subscribe, you’ll receive each new issue automatically. The magazine publisher is the Subject. You, as the subscriber, are the Observer. A Concrete Observer might be your email inbox or mailbox that receives the update.

## Simplified Example

Here’s a basic outline in Python:

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

This shows how multiple observers can be notified when something changes and how one can unsubscribe.

## Learn More

You can explore the full implementation on GitHub:
[Observer Pattern – Python Example](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/behavioral/observer.py)
