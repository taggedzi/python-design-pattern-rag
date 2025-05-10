# The Memento Pattern (Behavioral)

## Purpose

The Memento pattern lets you save and restore the state of an object without exposing its internal details. It’s often used to implement features like undo and rollback.

## The Problem It Solves

When you want to allow an object to revert to a previous state, you might be tempted to expose its internal data. But that breaks encapsulation. The Memento pattern solves this by letting an object save its state in a separate object (a memento) and restore it later—without revealing the details to others.

## When to Use It

Use this pattern when:

* You need to save snapshots of an object’s state to support undo/redo or rollback.
* You want to keep the internal structure of an object hidden from other parts of the system.
* You want to control access to saved states.

## When NOT to Use It

Avoid using it if:

* The object changes too often—saving and managing states frequently can be inefficient.
* You need to save states between sessions (in which case, a persistent storage system would be better).
* Your application requires many undo/redo actions and the system can’t reliably manage consistent states.

## How It Works

The Memento pattern has three key parts:

1. **Memento** – Stores the state of an object. It doesn’t expose any details about that state.
2. **Originator** – The object whose state we want to save and restore. It creates and uses mementos.
3. **Caretaker** – Manages the saved mementos. It doesn’t look inside them, it just stores and retrieves them when needed.

## Real-World Analogy

Imagine you’re a chef taking photos of your kitchen as you cook. If something goes wrong, you can look back at a photo and restore the kitchen to how it looked. You don’t need to remember every step—you just need the snapshot.

## Simplified Example

Here’s a basic Python example:

```python
# Originator
class TextEditor:
    def __init__(self):
        self._content = ""

    def write(self, text):
        self._content += text

    def get_content(self):
        return self._content

    def save(self):
        return self._content

    def restore(self, state):
        self._content = state

# Caretaker
class History:
    def __init__(self):
        self._states = []

    def backup(self, state):
        self._states.append(state)

    def undo(self):
        return self._states.pop() if self._states else None

# Demo
editor = TextEditor()
history = History()

editor.write("Hello, ")
history.backup(editor.save())  # Save the current state

editor.write("world")
print(editor.get_content())  # Outputs: Hello, world

editor.restore(history.undo())  # Revert to previous state
print(editor.get_content())  # Outputs: Hello, 
```

In this example:

* `TextEditor` is the originator.
* `History` is the caretaker.
* The editor can write, save its state, and restore it later.

## Learn More

For the full implementation, see the Python example here:
[Memento Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/behavioral/observer.py)
