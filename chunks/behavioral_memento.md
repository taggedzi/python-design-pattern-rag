---
file: behavioral/memento.py
chunk: behavioral_memento.md
---

```python
"""
Behavioral Pattern: Memento

Captures and externalizes an object's internal state so that it can be restored later,
without violating encapsulation. Useful for undo mechanisms.
"""

from __future__ import annotations
from typing import List

# Memento
class Memento:
    def __init__(self, state: str) -> None:
        self._state = state

    def get_state(self) -> str:
        return self._state

# Originator
class TextEditor:
    def __init__(self) -> None:
        self._state = ""

    def write(self, text: str) -> None:
        self._state += text

    def save(self) -> Memento:
        return Memento(self._state)

    def restore(self, memento: Memento) -> None:
        self._state = memento.get_state()

    def get_content(self) -> str:
        return self._state

# Caretaker
class History:
    def __init__(self) -> None:
        self._history: List[Memento] = []

    def backup(self, memento: Memento) -> None:
        self._history.append(memento)

    def undo(self) -> Memento:
        return self._history.pop()

# Example usage
if __name__ == "__main__":
    editor = TextEditor()
    history = History()

    editor.write("Hello, ")
    history.backup(editor.save())

    editor.write("world!")
    print("Current content:", editor.get_content())

    editor.restore(history.undo())
    print("After undo:", editor.get_content())
```

## Summary
Implements the Memento design pattern for a text editor, allowing state restoration and undo functionality.

## Docstrings
- Captures and externalizes an object's internal state so that it can be restored later, without violating encapsulation.
- Initializes a Memento object with a given state.
- Returns the internal state of the Memento.
- Initializes a TextEditor object with an empty state.
- Writes text to the editor, updating its internal state.
- Saves the current state of the editor as a Memento.
- Restores the editor's state from a given Memento.
- Returns the current content of the editor.
- Initializes a History object to manage mementos.
- Adds a Memento to the history for undo operations.
- Performs an undo operation by restoring the most recent memento.

