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