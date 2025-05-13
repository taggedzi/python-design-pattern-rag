# The Memento Pattern (Behavioral)

## Purpose

The Memento pattern allows an object to save and restore its state without exposing its internal details. It's commonly used for undo and rollback features.

## Problem It Solves

Sometimes you need an object to revert to a previous state. One way is to expose its internal data, but that breaks encapsulation. The Memento pattern solves this by using a separate object (a memento) to store the state. The object can later restore itself from this memento without revealing internal details to other parts of the system.

## When to Use It

Use this pattern when:

* You need to implement undo, redo, or rollback.
* You want to hide an object's internal structure.
* You want precise control over saved states.

## When Not to Use It

Avoid this pattern if:

* The object’s state changes too often, making frequent saves inefficient.
* You need to store states between sessions—use a database or file instead.
* Your application needs many undo/redo levels and can’t manage memory or consistency well.

## How It Works

The pattern includes three main components:

1. **Memento** – Stores an object's state privately.
2. **Originator** – The object whose state is saved and restored. It creates and applies mementos.
3. **Caretaker** – Manages mementos. It stores and retrieves them but doesn’t examine their contents.

## Real-World Analogy

Think of a chef taking photos of their kitchen while cooking. If a mistake happens, they can use a photo to reset the kitchen to how it was. They don’t need to remember every detail—just refer to the snapshot.

## Simplified Example

Here's a basic Python example:

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
* The editor can save and restore its text.

## Learn More

See the full implementation on GitHub:
[Memento Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/behavioral/memento.py)
